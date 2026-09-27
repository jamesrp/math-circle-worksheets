"""Small shared drawing vocabulary for the ten worksheet investigations.

All helper coordinates are points measured from the TOP LEFT of US Letter.
The underlying ``book.c`` is an ordinary ReportLab canvas with bottom-left
coordinates. Use helpers or explicitly convert H-y for direct canvas drawing.
"""
from pathlib import Path
from html import escape
import json
import math
import re

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT/'plans/atlas/worksheet-trial'
TMP = ROOT/'tmp/pdfs/atlas-random-ten'
W, H = 612, 792
MARGIN = 44
CONTENT_W = W-2*MARGIN
NAVY = colors.HexColor('#173747')
TEAL = colors.HexColor('#126E78')
INK = colors.HexColor('#192E38')
GRAY = colors.HexColor('#65737B')
PALE = colors.HexColor('#F1F5F5')
LIGHT = colors.HexColor('#CBD5D9')
WHITE = colors.white
FONT = 'Circle'
BOLD = 'CircleBold'
ITALIC = 'CircleItalic'


def register_fonts():
    if FONT in pdfmetrics.getRegisteredFontNames():
        return
    directory = Path('/System/Library/Fonts/Supplemental')
    for name, filename in [(FONT,'Arial Unicode.ttf'), (BOLD,'Arial Bold.ttf'), (ITALIC,'Arial Italic.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(directory/filename)))
    pdfmetrics.registerFont(TTFont('CircleSymbols','/System/Library/Fonts/Apple Symbols.ttf'))
    pdfmetrics.registerFontFamily(FONT,normal=FONT,bold=BOLD,italic=ITALIC,boldItalic=BOLD)


def clean(text):
    return str(text).replace('–','-').replace('—','-').replace('‑','-').replace('\u00ad','')


def text_markup(text, font=FONT):
    """Escape prose and select verified per-character mathematical fallbacks."""
    result=[]
    for ch in clean(text):
        if ch.isspace() or ord(ch) in pdfmetrics.getFont(font).face.charWidths:
            result.append(escape(ch))
        elif ord(ch) in pdfmetrics.getFont(FONT).face.charWidths:
            result.append(f'<font name="{FONT}">{escape(ch)}</font>')
        elif ord(ch) in pdfmetrics.getFont('CircleSymbols').face.charWidths:
            result.append(f'<font name="CircleSymbols">{escape(ch)}</font>')
        else:
            raise ValueError(f'Unsupported character {ch!r} U+{ord(ch):04X}')
    return ''.join(result)


class Book:
    def __init__(self,path,title,kind='student'):
        register_fonts()
        self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True)
        self.c=canvas.Canvas(str(path),pagesize=(W,H),invariant=1)
        self.c.setTitle(title);self.c.setAuthor('Bellingham Math Circle')
        self.kind=kind;self.page_no=0;self.family_id='';self.page_title=''
        self.page_map=[];self.bounds=[];self.seen=set();self.y=120
        self.pending_heading=None

    def new_page(self,family_id,title,subtitle='',part=''):
        self._flush_heading()
        if self.page_no:self._finish_page()
        self.page_no+=1;self.family_id=family_id;self.page_title=title
        self.page_map.append(dict(page=self.page_no,family_id=family_id,title=title,part=part))
        key=f'page-{self.page_no}'
        self.c.bookmarkPage(key)
        if family_id not in self.seen:
            self.c.addOutlineEntry(f'{family_id} - {title}',key,0,False)
            self.seen.add(family_id)
        else:self.c.addOutlineEntry(title,key,1,False)
        self.label('MATH CIRCLE  /  '+family_id,44,25,size=9,color=GRAY)
        self.label(('FACILITATOR' if self.kind=='facilitator' else part),568,25,size=9,align='right',color=GRAY)
        self.line(44,43,568,43,color=LIGHT,width=.65)
        bottom=self.p(title,y=55,size=23,leading=27,font=BOLD,color=NAVY)
        if subtitle:bottom=self.p(subtitle,y=bottom+7,size=10.5,leading=14,color=GRAY)
        self.y=bottom+18
        return self.y

    page=new_page

    def _finish_page(self):
        self.line(44,755,568,755,color=LIGHT,width=.65)
        self.label('Bellingham Math Circle  /  '+self.family_id,44,764,size=8,color=GRAY)
        self.label(str(self.page_no),568,764,size=8,align='right',color=GRAY)
        self.c.showPage()

    def save(self):
        self._flush_heading()
        if self.page_no:self._finish_page()
        self.c.save()
        return dict(path=str(self.path),pages=self.page_no,page_map=self.page_map,bounds=self.bounds)

    def p(self,text,x=44,y=None,width=CONTENT_W,size=12,leading=None,font=FONT,color=INK,rich=False,align=0):
        if y is None:y=self.y
        style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.35,textColor=color,alignment=align,spaceAfter=0)
        para=Paragraph(clean(text) if rich else text_markup(text,font),style)
        _,height=para.wrap(width,1000)
        if x<30 or x+width>582 or y<44 or y+height>746:
            raise ValueError(f'Paragraph outside content on {self.family_id} p{self.page_no}: {(x,y,width,height)} {str(text)[:80]}')
        para.drawOn(self.c,x,H-y-height)
        self.bounds.append(dict(page=self.page_no,kind='paragraph',x=x,y=y,w=width,h=height,text=re.sub('<[^>]+>','',str(text))))
        self.y=y+height
        return self.y

    def h(self,text,y=None,x=44,width=CONTENT_W,size=14):
        return self.p(text,x=x,y=y,width=width,size=size,font=BOLD,color=TEAL)

    def label(self,text,x,y,size=11,font=FONT,color=INK,align='left'):
        text=clean(text)
        # Labels with rare glyphs use the same fallback paragraph machinery.
        markup=text_markup(text,font)
        style=ParagraphStyle('label',fontName=font,fontSize=size,leading=size*1.2,textColor=color,alignment={'left':0,'center':1,'right':2}[align])
        width=max(12,pdfmetrics.stringWidth(text,FONT,size)+8,pdfmetrics.stringWidth(text,font,size)+8)
        p=Paragraph(markup,style);_,height=p.wrap(width,1000)
        left=x if align=='left' else x-width/2 if align=='center' else x-width
        p.drawOn(self.c,left,H-y-height)
        self.bounds.append(dict(page=self.page_no,kind='label',x=left,y=y,w=width,h=height,text=text))

    def line(self,x1,y1,x2,y2,color=INK,width=1,dash=None):
        self.c.saveState();self.c.setStrokeColor(color);self.c.setLineWidth(width)
        if dash:self.c.setDash(dash)
        self.c.line(x1,H-y1,x2,H-y2);self.c.restoreState()

    def box(self,x,y,w,h,label='',fill=None,stroke=LIGHT,width=.8,radius=0):
        self.c.saveState();self.c.setStrokeColor(stroke);self.c.setLineWidth(width)
        if fill:self.c.setFillColor(fill)
        if radius:self.c.roundRect(x,H-y-h,w,h,radius,stroke=1,fill=int(fill is not None))
        else:self.c.rect(x,H-y-h,w,h,stroke=1,fill=int(fill is not None))
        self.c.restoreState()
        self.bounds.append(dict(page=self.page_no,kind='box',x=x,y=y,w=w,h=h))
        if label:self.label(label,x+8,y+6,size=10,color=GRAY)

    def rule(self,text,y=None,height=None):
        if y is None:y=self.y
        style=ParagraphStyle('rule',fontName=FONT,fontSize=11.5,leading=15.2)
        para=Paragraph(text_markup(text),style);_,ph=para.wrap(CONTENT_W-20,1000)
        height=height or ph+18
        self.box(44,y,CONTENT_W,height,fill=PALE,stroke=PALE)
        self.p(text,x=54,y=y+8,width=CONTENT_W-20,size=11.5,leading=15.2)
        self.y=y+height
        return self.y

    def lines(self,x,y,w,n=3,spacing=24):
        for i in range(n):self.line(x,y+i*spacing,x+w,y+i*spacing,color=LIGHT,width=.55)

    def circle(self,x,y,r=5,fill=WHITE,stroke=INK,width=1):
        self.c.saveState();self.c.setStrokeColor(stroke);self.c.setLineWidth(width)
        if fill:self.c.setFillColor(fill)
        self.c.circle(x,H-y,r,stroke=1,fill=int(fill is not None));self.c.restoreState()

    def poly(self,points,closed=False,fill=None,stroke=INK,width=1):
        self.c.saveState();self.c.setStrokeColor(stroke);self.c.setLineWidth(width)
        if fill:self.c.setFillColor(fill)
        p=self.c.beginPath();p.moveTo(points[0][0],H-points[0][1])
        for x,y in points[1:]:p.lineTo(x,H-y)
        if closed:p.close()
        self.c.drawPath(p,stroke=1,fill=int(fill is not None));self.c.restoreState()

    def arrow(self,x1,y1,x2,y2,color=INK,width=1,head=6):
        self.line(x1,y1,x2,y2,color,width)
        angle=math.atan2(y2-y1,x2-x1)
        points=[(x2,y2),(x2-head*math.cos(angle-.45),y2-head*math.sin(angle-.45)),(x2-head*math.cos(angle+.45),y2-head*math.sin(angle+.45))]
        self.poly(points,closed=True,fill=color,stroke=color,width=.5)

    def grid(self,x,y,w,h,cols,rows,color=LIGHT):
        for i in range(cols+1):self.line(x+i*w/cols,y,x+i*w/cols,y+h,color,.5)
        for j in range(rows+1):self.line(x,y+j*h/rows,x+w,y+j*h/rows,color,.5)

    def table(self,rows,x=44,y=None,widths=None,header=True,size=11,row_height=None):
        if y is None:y=self.y
        widths=widths or [CONTENT_W/len(rows[0])]*len(rows[0])
        cells=[]
        for i,row in enumerate(rows):
            font=BOLD if header and i==0 else FONT
            style=ParagraphStyle('cell',fontName=font,fontSize=size,leading=size*1.25,textColor=INK)
            cells.append([Paragraph(text_markup(value,font),style) for value in row])
        t=Table(cells,colWidths=widths,rowHeights=row_height)
        commands=[('GRID',(0,0),(-1,-1),.6,LIGHT),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]
        if header:commands.append(('BACKGROUND',(0,0),(-1,0),PALE))
        t.setStyle(TableStyle(commands));tw,th=t.wrap(1000,1000)
        if y+th>746:raise ValueError(f'Table overflows {self.family_id}: {y+th}')
        t.drawOn(self.c,x,H-y-th);self.y=y+th
        self.bounds.append(dict(page=self.page_no,kind='table',x=x,y=y,w=tw,h=th))
        return self.y

    def flow_p(self,text,size=11,rich=False):
        style=ParagraphStyle('measure',fontName=FONT,fontSize=size,leading=size*1.35)
        p=Paragraph(clean(text) if rich else text_markup(text),style);_,height=p.wrap(CONTENT_W,1000)
        heading=self.pending_heading
        self.pending_heading=None
        heading_height=0
        if heading is not None:
            hs=ParagraphStyle('measure-heading',fontName=BOLD,fontSize=14,leading=18.9)
            hp=Paragraph(text_markup(heading,BOLD),hs)
            _,heading_height=hp.wrap(CONTENT_W,1000)
            heading_height+=7
        if self.y+heading_height+height>730:self.new_page(self.family_id,self.page_title,part='continued')
        if heading is not None:
            self.h(heading,y=self.y);self.y+=7
        self.p(text,y=self.y,size=size,rich=rich);self.y+=9

    def flow_h(self,text):
        # Keep every guide heading with its first complete paragraph. Deferring
        # the draw prevents a stranded question number at the page foot.
        self._flush_heading()
        self.pending_heading=text

    def _flush_heading(self):
        if self.pending_heading is not None:
            text=self.pending_heading;self.pending_heading=None
            if self.y>685:self.new_page(self.family_id,self.page_title,part='continued')
            self.h(text,y=self.y);self.y+=7


def data(name):
    return json.loads((DATA/name).read_text())
