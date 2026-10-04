from pathlib import Path
import json, sys, math
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parent
for name,file in [('Body','DejaVuSans.ttf'),('Body-Bold','DejaVuSans-Bold.ttf'),('Body-Oblique','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(ROOT.parent/'fonts'/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Oblique',boldItalic='Body-Bold')
styles={
 'p':ParagraphStyle('p',fontName='Body',fontSize=10.1,leading=14.4,spaceAfter=7.5),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.7,leading=12.1,spaceAfter=6),
 'h':ParagraphStyle('h',fontName='Body-Bold',fontSize=12.4,leading=16.2,spaceBefore=9,spaceAfter=6,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='Body-Bold',fontSize=21,leading=25.2,spaceAfter=12),
 'subtitle':ParagraphStyle('subtitle',fontName='Body',fontSize=10,leading=14,spaceAfter=14),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.4,leading=12.7),
}
class Sketch(Flowable):
 def __init__(self,kind):self.kind=kind;self.width=500;self.height={'seams':100,'graph':106,'crossing':100,'portal':120}[kind]
 def draw(self):
  c=self.canv;c.setFont('Body',9);c.setLineWidth(1.4)
  def text(x,y,s):c.drawCentredString(x,y,s)
  def arrow(x1,y1,x2,y2):
   c.line(x1,y1,x2,y2);a=math.atan2(y2-y1,x2-x1);l=6
   c.line(x2,y2,x2-l*math.cos(a-.45),y2-l*math.sin(a-.45));c.line(x2,y2,x2-l*math.cos(a+.45),y2-l*math.sin(a+.45))
  if self.kind=='seams':
   for x,rev,label in [(8,False,'A'),(269,True,'B')]:
    text(x+5,84,label);c.rect(x+22,22,202,55);c.setDash(3,3);c.line(x+22,49.5,x+224,49.5);c.setDash()
    for xx,r in [(x+29,False),(x+217,rev)]:
     c.circle(xx,65 if not r else 34,3,fill=1);c.rect(xx-3,(34 if not r else 65)-3,6,6,fill=0)
    text(x+123,58,'U');text(x+123,33,'L')
    text(x+125,5,'U → U, L → L' if not rev else 'U → L, L → U')
  elif self.kind=='graph':
   maps=[({'A':(15,45),'B':(65,45),'C':(65,85),'D':(115,45),'E':(165,85),'F':(165,5)},['AB','BC','BD','DE','DF']),({'A':(215,45),'B':(255,85),'C':(295,45),'D':(255,5)},['AB','BC','CD','DA']),({'H':(400,45),'A':(345,85),'B':(345,5),'C':(455,85),'D':(455,5)},['HA','AB','BH','HC','CD','DH'])]
   for pts,edges in maps:
    for e in edges:c.line(*pts[e[0]],*pts[e[1]])
    for l,(x,y) in pts.items():c.circle(x,y,2,fill=1);text(x+8,y+5,l)
  elif self.kind=='crossing':
   for x,label in [(45,'input'),(280,'output')]:
    y=51;text(x+74,88,label)
    c.setLineWidth(3)
    for a,b in [(0,15),(29,119),(133,148)]:c.line(x+a,y,x+b,y)
    for xx in [22,126]:c.line(x+xx,y-19,x+xx,y+19)
    c.line(x+74,y-19,x+74,y-7);c.line(x+74,y+7,x+74,y+19)
    if label=='output':
     c.setStrokeColor(colors.HexColor('#275b9e'));c.setLineWidth(2);c.line(x+30,y,x+118,y);c.setStrokeColor(colors.black)
    text(x+34,y+7,'X');text(x+29,15,'start');text(x+119,15,'stop')
   c.setLineWidth(1.4);arrow(210,51,250,51)
  elif self.kind=='portal':
   labs=[['F','G','I'],['D','H','E'],['A','B','C']]
   for x,label in [(25,'original copy'),(115,'right copy')]:
    for i in range(4):c.line(x+30*i,18,x+30*i,108);c.line(x,18+30*i,x+90,18+30*i)
    for iy,row in enumerate(labs):
     for ix,l in enumerate(row):text(x+15+ix*30,30+iy*30,l)
    text(x+45,3,label)
   c.setStrokeColor(colors.HexColor('#275b9e'));arrow(70,55,100,55);arrow(100,55,130,55);c.setStrokeColor(colors.black)
   text(330,76,'H → E → D')
   text(330,51,'two steps right')
class CheckCanvas(canvas.Canvas):
 def __init__(self,*a,**k):super().__init__(*a,**k);self._saved=[]
 def showPage(self):self._saved.append(dict(self.__dict__));self._startPage()
 def save(self):
  total=len(self._saved)
  for state in self._saved:
   self.__dict__.update(state);self.setFont('Body',8);self.setFillColor(colors.HexColor('#444444'));self.drawString(48,28,footer);self.drawRightString(564,28,f'{self._pageNumber} / {total}');super().showPage()
  super().save()
def build(content,output):
 global footer
 footer=f"Bellingham Math Circle / Week {content['week']} / Adult guide / Unpiloted"
 story=[]
 for i,page in enumerate(content['pages']):
  if i:story.append(PageBreak())
  story.append(Paragraph(page['title'],styles['title'] if not i else styles['h']))
  if not i:story.append(Paragraph('Facilitator guide keyed to the revised student packets',styles['subtitle']))
  for node in page['body']:
   kind=node[0]
   if kind in styles:story.append(Paragraph(node[1],styles[kind]))
   elif kind=='diagram':story.append(Sketch(node[1]));story.append(Spacer(1,7))
   elif kind=='table':
    data=[[Paragraph(str(v),styles['cell']) for v in row] for row in node[1]]
    t=Table(data,colWidths=node[2],hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5e7eb')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#cccccc')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t);story.append(Spacer(1,10))
 doc=SimpleDocTemplate(str(output),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=38,bottomMargin=48,title=f"Week {content['week']} {content['topic']} facilitator guide",author='Bellingham Math Circle')
 doc.build(story,canvasmaker=CheckCanvas)
if __name__=='__main__':
 content=json.loads((ROOT/'content.json').read_text());build(content,ROOT.parent/'facilitator-guide.pdf')
