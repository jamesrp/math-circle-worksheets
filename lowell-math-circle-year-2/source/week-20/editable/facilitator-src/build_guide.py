#!/usr/bin/env python3
"""Portable PDF builder. Requires reportlab. Outputs beside facilitator-src by default."""
from pathlib import Path
import argparse, math, re, os, reportlab
from fractions import Fraction
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import black,HexColor,white
from reportlab.lib.pagesizes import letter
from graphs import G
from content import PAGES
ROOT=Path(__file__).resolve().parent
FONT_DIR=Path(os.environ.get('MATH_CIRCLE_FONT_DIR', ROOT/'fonts'))
if not FONT_DIR.is_dir(): FONT_DIR=Path(reportlab.__file__).resolve().parent/'fonts'
for name,filename in [('Vera','Vera.ttf'),('Vera-Bold','VeraBd.ttf'),('Vera-Italic','VeraIt.ttf'),('Vera-BoldItalic','VeraBI.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(FONT_DIR/filename)))
pdfmetrics.registerFontFamily('Vera',normal='Vera',bold='Vera-Bold',italic='Vera-Italic',boldItalic='Vera-BoldItalic')
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT.parent/'build'/'facilitator-guide.pdf');args=ap.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
W,H=letter;M=48;CW=W-2*M
styles={
 'title':ParagraphStyle('Title',fontName='Vera-Bold',fontSize=20,leading=24,spaceAfter=7,textColor=black),
 'sub':ParagraphStyle('Subtitle',fontName='Vera',fontSize=10,leading=14,spaceAfter=12,textColor=HexColor('#454545')),
 'body':ParagraphStyle('Body',fontName='Vera',fontSize=10.2,leading=14,spaceAfter=9,textColor=black),
}
class GraphGrid(Flowable):
 def __init__(self,keys):
  Flowable.__init__(self);self.keys=keys;self.width=CW
  self.cols=2 if len(keys)>1 else 1;self.rows=math.ceil(len(keys)/self.cols)
  self.panel=120 if len(keys)>2 else 150
  if len(keys)==1:self.panel=150
  self.height=self.panel*self.rows+6
 def draw(self):
  c=self.canv;pw=self.width/self.cols
  for i,key in enumerate(self.keys):
   g=G[key];x0=(i%self.cols)*pw;y0=self.height-(i//self.cols+1)*self.panel
   nodes=g['nodes'];xs=[n[1] for n in nodes];ys=[n[2] for n in nodes]
   r=11.5;dx=max(xs)-min(xs);dy=max(ys)-min(ys)
   aw=pw-42;ah=self.panel-54
   scale=min(aw/(dx or 1), ah/(dy or 1), 70)
   xx=x0+pw/2-(max(xs)+min(xs))/2*scale
   yy=y0+ah/2+13-(max(ys)+min(ys))/2*scale
   pos={n:(xx+x*scale,yy+y*scale) for n,x,y,f,v in nodes}
   c.setStrokeColor(black);c.setLineWidth(.8)
   if key=='O6.2':
    px=[q[0] for q in pos.values()];py=[q[1] for q in pos.values()]
    pad=r+6
    c.setDash(3,2);c.roundRect(min(px)-pad,min(py)-pad,max(px)-min(px)+2*pad,max(py)-min(py)+2*pad,7,stroke=1,fill=0);c.setDash()
   for a,b in g['edges']:c.line(*pos[a],*pos[b])
   for n,x,y,f,v in nodes:
    cx,cy=pos[n];c.setFillColor(white)
    if f:c.rect(cx-r,cy-r,2*r,2*r,fill=1,stroke=1)
    else:c.circle(cx,cy,r,fill=1,stroke=1)
    c.setFillColor(black);c.setFont('Vera-Bold' if not f else 'Vera',10)
    c.drawCentredString(cx,cy-3.5,str(v))
   c.setFillColor(black);c.setFont('Vera',9)
   # Figure captions are short and centered; wrap long single-panel caption.
   caption=g['title'];c.drawCentredString(x0+pw/2,y0+self.panel-13,caption)

class CountCanvas(canvas.Canvas):
 def __init__(self,*a,**kw):canvas.Canvas.__init__(self,*a,**kw);self.saved=[]
 def showPage(self):self.saved.append(dict(self.__dict__));self._startPage()
 def save(self):
  n=len(self.saved)
  for s in self.saved:
   self.__dict__.update(s);self.footer(n);canvas.Canvas.showPage(self)
  canvas.Canvas.save(self)
 def footer(self,n):
  self.setFont('Vera',8);self.setFillColor(HexColor('#555555'))
  self.drawString(M, H-29,'Bellingham Math Circle / Averaging / Adult guide')
  self.drawString(M,25,'Week 20 library slot / Draft and unpiloted / 2026-10-03')
  self.drawRightString(W-M,25,f'{self._pageNumber} / {n}')

story=[]
for i,p in enumerate(PAGES):
 if i:story.append(PageBreak())
 story.append(Paragraph(p['title'],styles['title']));story.append(Paragraph(p['sub'],styles['sub']))
 if p['figs']:story.extend([GraphGrid(p['figs']),Spacer(1,4)])
 for label,body in p['sections']:
  text=(f'<b>{label}.</b> ' if label else '')+body
  text=re.sub(r'<(?!/?(?:b|i|link)(?:>|\s))', '&lt;', text)
  story.append(Paragraph(text,styles['body']))
doc=SimpleDocTemplate(str(args.output),pagesize=letter,leftMargin=M,rightMargin=M,topMargin=49,bottomMargin=43,title='Averaging facilitator guide',author='Bellingham Math Circle',subject='Week 20 unscheduled library slot; draft and unpiloted')
doc.build(story,canvasmaker=CountCanvas)
print(args.output)
