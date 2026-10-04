from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.graphics.shapes import Drawing, Line, Circle, String, Polygon
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from portable_fonts import font_directory
FONTS=font_directory('Liberation Sans',[f'LiberationSans-{v}.ttf' for v in ['Regular','Bold','Italic','BoldItalic']],'LIBERATION_FONT_DIR')
for name,file in [('Helvetica','Regular'),('Helvetica-Bold','Bold'),('Helvetica-Oblique','Italic'),('Helvetica-BoldOblique','BoldItalic')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTS/f'LiberationSans-{file}.ttf')))
pdfmetrics.registerFontFamily('Helvetica',normal='Helvetica',bold='Helvetica-Bold',italic='Helvetica-Oblique',boldItalic='Helvetica-BoldOblique')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=10.6,leading=14.1,spaceAfter=7))
styles.add(ParagraphStyle(name='SmallX',fontName='Helvetica',fontSize=9.1,leading=11.8,spaceAfter=5))
styles.add(ParagraphStyle(name='HeadingX',fontName='Helvetica-Bold',fontSize=15,leading=18,spaceAfter=11))
styles.add(ParagraphStyle(name='SubX',fontName='Helvetica-Bold',fontSize=11.4,leading=14,spaceBefore=5,spaceAfter=5))
styles.add(ParagraphStyle(name='TitleX',fontName='Helvetica-Bold',fontSize=24,leading=28,spaceAfter=12))
def p(t,small=False):return Paragraph(t,styles['SmallX' if small else 'BodyX'])
def h(t):return Paragraph(t,styles['HeadingX'])
def sub(t):return Paragraph(t,styles['SubX'])
def problem(n,goal,answer,hint,gate):return [sub(f'Problem {n}  {goal}'),p('<b>Solution.</b> '+answer),p('<b>Hold these hints.</b> '+hint),p('<b>Readiness and stopping point.</b> '+gate)]
def table(rows,widths=None):
 data=[[p(str(x),True) for x in row] for row in rows]
 t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7edf1')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#bbc5cc')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
 return t

def net(n,bars,label,width=510,height=115):
 d=Drawing(width,height); left=32;right=width-12; top=height-29;gap=min(23,(height-40)/(n-1))
 d.add(String(0,height-11,label,fontName='Helvetica-Bold',fontSize=10))
 for i in range(n):
  y=top-i*gap;d.add(String(8,y-3,str(i+1),fontName='Helvetica',fontSize=9));d.add(Line(left,y,right,y,strokeWidth=.65,strokeColor=colors.HexColor('#71808b')))
  d.add(Polygon([right,y,right-5,y+2,right-5,y-2],fillColor=colors.black,strokeColor=None))
 for k,(a,b) in enumerate(bars):
  x=left+25+k*(right-left-55)/max(1,len(bars)-1);y1=top-(a-1)*gap;y2=top-(b-1)*gap
  d.add(Line(x,y1,x,y2,strokeWidth=1.6));d.add(Circle(x,y1,2.7,fillColor=colors.black));d.add(Circle(x,y2,2.7,fillColor=colors.black))
 return d

def build(pages,path,week,topic):
 story=[]
 for i,page in enumerate(pages):
  if i:story.append(PageBreak())
  story.extend(page)
 def deco(c,doc):
  c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#54616a'));c.drawString(42,766,f'Bellingham Math Circle / Week {week} / {topic} / Facilitator guide')
  c.drawString(42,24,'Draft and unpiloted / Unscheduled library slot / 2026-10-03');c.drawRightString(570,24,str(doc.page))
 doc=SimpleDocTemplate(str(path),pagesize=(612,792),rightMargin=42,leftMargin=42,topMargin=47,bottomMargin=43,title=f'Week {week} {topic} facilitator guide',author='Bellingham Math Circle')
 doc.build(story,onFirstPage=deco,onLaterPages=deco)
