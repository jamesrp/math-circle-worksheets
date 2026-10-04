from pathlib import Path
import json, math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parent
# Discover installed fonts; no font binaries or machine-specific project paths are bundled.
import os, subprocess
from reportlab import rl_config
font_names=('DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSans-Oblique.ttf')
font_roots=[Path(os.environ['DEJAVU_FONT_DIR'])] if os.environ.get('DEJAVU_FONT_DIR') else []
font_roots += [Path(p) for p in rl_config.TTFSearchPath]
try:
    found=subprocess.run(['fc-match','-f','%{file}','DejaVu Sans'],check=True,capture_output=True,text=True).stdout
    if found: font_roots.append(Path(found).parent)
except (FileNotFoundError,subprocess.CalledProcessError): pass
font_roots += [Path.home()/'.fonts',Path.home()/'Library'/'Fonts']
if os.environ.get('WINDIR'): font_roots.append(Path(os.environ['WINDIR'])/'Fonts')
FONT_DIR=next((d for d in font_roots if all((d/f).is_file() for f in font_names)),None)
if FONT_DIR is None: raise FileNotFoundError('Install DejaVu Sans regular, bold and oblique, or set DEJAVU_FONT_DIR to their folder.')
D=json.loads((ROOT/'guide.json').read_text())
for face,file in [('Guide','DejaVuSans.ttf'),('Guide-Bold','DejaVuSans-Bold.ttf'),('Guide-Oblique','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(face,str(FONT_DIR/file)))
pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='Guide-Bold',italic='Guide-Oblique',boldItalic='Guide-Bold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyX',fontName='Guide',fontSize=10.5,leading=14.2,spaceAfter=6,textColor=colors.black))
styles.add(ParagraphStyle(name='SmallX',fontName='Guide',fontSize=9.2,leading=12,spaceAfter=5))
styles.add(ParagraphStyle(name='TitleX',fontName='Guide-Bold',fontSize=22,leading=26,spaceAfter=12))
styles.add(ParagraphStyle(name='HeadingX',fontName='Guide-Bold',fontSize=14.5,leading=18,spaceBefore=5,spaceAfter=9))
styles.add(ParagraphStyle(name='SubX',fontName='Guide-Bold',fontSize=11.7,leading=15,spaceBefore=7,spaceAfter=5))
P=lambda s,sty='BodyX':Paragraph(s,styles[sty])
class Diagram(Flowable):
 def __init__(self,kind):Flowable.__init__(self);self.kind=kind;self.width=504;self.height={'cycle3':120,'suffix':155,'chains':220,'ambiguity':112,'repetition':102}[kind]
 def draw(self):
  c=self.canv;c.setStrokeColor(colors.black);c.setFillColor(colors.black)
  def txt(x,y,t,sz=10):c.setFont('Guide',sz);c.drawCentredString(x,y,t)
  def arrow(x1,y1,x2,y2,label=None):
   c.line(x1,y1,x2,y2);a=math.atan2(y2-y1,x2-x1)
   p=c.beginPath();p.moveTo(x2,y2);p.lineTo(x2-6*math.cos(a-.45),y2-6*math.sin(a-.45));p.lineTo(x2-6*math.cos(a+.45),y2-6*math.sin(a+.45));p.close();c.drawPath(p,fill=1)
   if label:txt((x1+x2)/2,(y1+y2)/2+7,label)
  def state(x,y,t,yes=False):c.circle(x,y,21);txt(x,y+2,t);c.setFont('Guide',8);c.drawCentredString(x,y-10,'YES' if yes else 'NO')
  if self.kind=='cycle3':
   for x,t,y in [(80,'0',True),(250,'1',False),(420,'2',False)]:
    state(x,70,t,y);c.bezier(x-12,88,x-45,120,x+45,120,x+12,88);arrow(x+18,96,x+12,88);txt(x,113,'B loop')
   arrow(15,70,57,70,'start');arrow(103,70,227,70,'R');arrow(273,70,397,70,'R')
   c.line(420,47,420,14);c.line(420,14,80,14);arrow(80,14,80,47);txt(250,19,'R')
  elif self.kind=='suffix':
   for x,t,yes in [(80,'N',False),(250,'R',False),(420,'RB',True)]:state(x,90,t,yes)
   arrow(10,90,57,90,'start');arrow(103,100,227,100,'R');arrow(273,100,397,100,'B')
   c.line(420,67,420,15);c.line(420,15,80,15);arrow(80,15,80,67);txt(250,20,'B')
   arrow(397,80,273,80,'R')
   for x,t in [(80,'B loop'),(250,'R loop')]:c.bezier(x-12,108,x-45,145,x+45,145,x+12,108);arrow(x+18,116,x+12,108);txt(x,141,t)
  elif self.kind=='chains':
   rows=[['empty','A','AB','ABC','ABCD'],['D','AD','ABD'],['C','AC','ACD'],['CD'],['B','BC','BCD'],['BD']]
   for i,r in enumerate(rows):
    y=199-i*34
    for j,t in enumerate(r):
     x=48+j*99;c.roundRect(x-29,y-12,58,24,3);txt(x,y-3,t)
     if j:arrow(x-66,y,x-31,y)
   txt(250,2,'Every arrow means strict containment. Every one of the 16 cards appears once.',9)
  elif self.kind=='ambiguity':
   txt(92,82,'sent 00');txt(412,82,'sent 11');txt(252,31,'received 01',12)
   arrow(122,73,221,43,'flip right');arrow(382,73,283,43,'flip left')
   txt(252,5,'The same observation has two allowed explanations.',10)
  elif self.kind=='repetition':
   for x,head,vals in [(126,'triangle 000',['000','100','010','001']),(378,'square 111',['111','011','101','110'])]:
    txt(x,82,head,12)
    for i,v in enumerate(vals):txt(x-72+48*i,37,v,11)
    c.line(x-90,64,x+90,64)
   txt(252,8,'No received row belongs to both lists. The unchanged row is included.',10)

def table(rows,widths=None):
 cooked=[[P(str(v),'SmallX') for v in row] for row in rows]
 t=Table(cooked,colWidths=widths or [504/len(rows[0])]*len(rows[0]),hAlign='LEFT',repeatRows=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf0')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#cbd0d4')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
 return t
story=[]
for i,page in enumerate(D['pages']):
 if i:story.append(PageBreak())
 story.append(P(page['title'],'TitleX' if i in (0,1) else 'HeadingX'))
 for el in page['elements']:
  if isinstance(el,str):story.append(P(el))
  elif 'h' in el:story.append(P(el['h'],'SubX'))
  elif 'table' in el:story.extend([table(el['table'],el.get('widths')),Spacer(1,7)])
  elif 'diagram' in el:story.extend([Diagram(el['diagram']),Spacer(1,7)])
  elif 'small' in el:story.append(P(el['small'],'SmallX'))
  elif 'space' in el:story.append(Spacer(1,el['space']))
  else:raise ValueError(el)
def footer(c,doc):
 c.saveState();c.setFont('Guide',8);c.setFillColor(colors.HexColor('#555555'));c.drawString(54,33,f'Bellingham Math Circle | Week {D["week"]} library slot | Draft and unpiloted');c.drawRightString(558,33,str(doc.page));c.restoreState()
out=ROOT.parent/'build'/'facilitator-guide.pdf'
SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=54,leftMargin=54,topMargin=44,bottomMargin=51,title=D['title'],author='Bellingham Math Circle').build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
