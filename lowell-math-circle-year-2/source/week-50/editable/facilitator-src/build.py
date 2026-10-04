from pathlib import Path
import json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether,Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parent
fontdir=ROOT.parent/'fonts'
for name,file in [('Guide','DejaVuSans.ttf'),('Guide-Bold','DejaVuSans-Bold.ttf'),('Guide-Italic','DejaVuSans-Oblique.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='Guide-Bold',italic='Guide-Italic')
styles={
 'title':ParagraphStyle('title',fontName='Guide-Bold',fontSize=20,leading=24,spaceAfter=8,textColor=colors.black),
 'sub':ParagraphStyle('sub',fontName='Guide',fontSize=9,leading=12,spaceAfter=11,textColor=colors.black),
 'h':ParagraphStyle('h',fontName='Guide-Bold',fontSize=12,leading=15,spaceBefore=8,spaceAfter=6,keepWithNext=True),
 'p':ParagraphStyle('p',fontName='Guide',fontSize=10.3,leading=14.1,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='Guide',fontSize=8.8,leading=12,spaceAfter=6),
 'cell':ParagraphStyle('cell',fontName='Guide',fontSize=9.2,leading=12),
}
class Route(Flowable):
 def __init__(self,pts,d=15):super().__init__();self.pts=pts;self.d=d;self.width=480;self.height=181
 def draw(self):
  c=self.canv;ox=115;oy=15;s=1.18
  x=lambda v:ox+s*v;y=lambda v:oy+s*v
  d=self.d;p=c.beginPath()
  vertices=[(0,0),(0,d),((120-d)/.75,120),(160,120),(160,120-d),(d/.75,0)]
  p.moveTo(x(vertices[0][0]),y(vertices[0][1]))
  for a,b in vertices[1:]:p.lineTo(x(a),y(b))
  p.close();c.setFillColor(colors.HexColor('#e9e9e9'));c.drawPath(p,fill=1,stroke=0)
  c.setStrokeColor(colors.HexColor('#999999'));c.setLineWidth(.4);c.rect(ox,oy,160*s,120*s)
  c.setDash(2,3);c.line(x(0),y(0),x(160),y(120));c.setDash()
  c.setStrokeColor(colors.black);c.setLineWidth(1.4)
  for a,b in zip(self.pts,self.pts[1:]):c.line(x(a[0]),y(a[1]),x(b[0]),y(b[1]))
  c.setFillColor(colors.black);c.setFont('Guide',8);c.drawString(x(0)-12,y(0)-5,'S');c.drawString(x(160)+5,y(120),'F')
  c.drawCentredString(x(80),y(0)-12,'160 mm');c.drawString(x(160)+10,y(60),'120 mm')
  c.drawString(5,165,'Guide diagram');c.drawString(5,153,'not to scale')

def build(data,out):
 doc=SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=49,leftMargin=49,topMargin=57,bottomMargin=48,title=f"Week {data['week']} {data['title']} facilitator guide",author='Bellingham Math Circle')
 story=[]
 for i,page in enumerate(data['pages']):
  if i:story.append(PageBreak())
  if i==0:
   story.append(Paragraph(f"Week {data['week']} {data['title']}",styles['title']))
   story.append(Paragraph('Facilitator guide | Final student packets v2 | Prepared 3 October 2026 | Unpiloted',styles['sub']))
  for item in page:
   typ=item[0]
   if typ in styles:story.append(Paragraph(item[1],styles[typ]))
   elif typ=='table':
    rows=[[Paragraph(str(t),styles['cell']) for t in row] for row in item[1]]
    t=Table(rows,colWidths=item[2] if len(item)>2 else None,hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story.extend([t,Spacer(1,8)])
   elif typ=='route':story.append(Route(item[1],item[2] if len(item)>2 else 15))
 def footer(c,d):
  c.saveState();c.setFillColor(colors.black);c.setFont('Guide',8.4)
  c.drawString(49,766,f"Bellingham Math Circle / Week {data['week']} / Adult reference")
  c.drawString(49,28,'Facilitator guide - prepared material, not classroom-tested')
  c.drawRightString(563,28,str(d.page));c.restoreState()
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
if __name__=='__main__':
 data=json.loads((ROOT/'content.json').read_text());build(data,ROOT.parent/'facilitator-guide.pdf')
