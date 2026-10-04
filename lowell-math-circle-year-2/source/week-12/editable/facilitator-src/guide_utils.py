from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Flowable,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import math
# Portable font lookup. DejaVu Sans is needed for release-identical line breaks.
import os
roots=[Path(os.environ['DEJAVU_FONT_DIR'])] if os.environ.get('DEJAVU_FONT_DIR') else []
roots += [Path('/usr/share/fonts/truetype/dejavu'),Path('/usr/share/fonts/dejavu'),Path('/usr/local/share/fonts'),Path.home()/'.fonts',Path.home()/'Library'/'Fonts',Path('/Library/Fonts'),Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts']
font=next((str(d/'DejaVuSans.ttf') for d in roots if (d/'DejaVuSans.ttf').exists() and (d/'DejaVuSans-Bold.ttf').exists()),None)
if not font:raise FileNotFoundError('Install DejaVu Sans regular/bold, or set DEJAVU_FONT_DIR to their folder.')
pdfmetrics.registerFont(TTFont('Body',font));pdfmetrics.registerFont(TTFont('BodyBold',font.replace('.ttf','-Bold.ttf')))
F='Body' if font else 'Helvetica';FB='BodyBold' if font else 'Helvetica-Bold'
S=getSampleStyleSheet()
S.add(ParagraphStyle(name='Main',fontName=F,fontSize=10.3,leading=14,spaceAfter=7))
S.add(ParagraphStyle(name='SmallGuide',fontName=F,fontSize=9,leading=12,spaceAfter=5))
S.add(ParagraphStyle(name='GuideTitle',fontName=FB,fontSize=21,leading=25,spaceAfter=13,textColor=colors.black))
S.add(ParagraphStyle(name='GuideHeading',fontName=FB,fontSize=14,leading=18,spaceBefore=8,spaceAfter=8,textColor=colors.black))
S.add(ParagraphStyle(name='GuideSub',fontName=FB,fontSize=11,leading=15,spaceBefore=8,spaceAfter=5,textColor=colors.black))
def P(t,small=False):return Paragraph(t,S['SmallGuide' if small else 'Main'])
def H(t):return Paragraph(t,S['GuideHeading'])
def SH(t):return Paragraph(t,S['GuideSub'])
def T(t):return Paragraph(t,S['GuideTitle'])
def B(t):return P('<b>'+t+'</b>')
def table(rows,widths):
 t=Table([[P(str(v),True) for v in row] for row in rows],colWidths=widths,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5ebee')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#c7ced1')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));return t
class Figure(Flowable):
 def __init__(self,w,h,fn):Flowable.__init__(self);self.width=w;self.height=h;self.fn=fn
 def draw(self):self.fn(self.canv,self.width,self.height)
def build(path,story,week,topic):
 def footer(c,d):
  c.setFont(F,8);c.setFillColor(colors.HexColor('#4d5459'));c.drawString(45,27,f'Bellingham Math Circle | Library slot {week} | Draft and unpiloted');c.drawRightString(567,27,str(d.page));c.setFillColor(colors.black)
  if d.page>1:c.setFont(F,8);c.drawString(45,766,topic+' facilitator guide')
 SimpleDocTemplate(str(path),pagesize=(612,792),rightMargin=45,leftMargin=45,topMargin=43,bottomMargin=46,title=topic+' facilitator guide',author='Bellingham Math Circle').build(story,onFirstPage=footer,onLaterPages=footer)
def label(c,x,y,s,size=9,bold=False):c.setFont(FB if bold else F,size);c.drawString(x,y,s)
def pairs(w):
 stack=[];out=[]
 for i,x in enumerate(w,1):
  if x=='U':stack.append(i)
  else:out.append((stack.pop(),i))
 return sorted(out)
def draw_pair(c,w,x,y,width=130,height=42):
 n=len(w);dx=width/(n-1)
 c.setLineWidth(.8)
 for a,b in pairs(w):
  xa=x+(a-1)*dx;xb=x+(b-1)*dx;hh=height*(b-a)/(n-1)
  p=c.beginPath();p.moveTo(xa,y);p.curveTo(xa,y+hh*1.34,xb,y+hh*1.34,xb,y);c.drawPath(p)
 for i in range(n):c.circle(x+i*dx,y,1.5,fill=1);label(c,x+i*dx-2,y-11,str(i+1),7)
def tree(w):
 root=[];stack=[root]
 for x in w:
  if x=='U':a=[];stack[-1].append(a);stack.append(a)
  else:stack.pop()
 return root
def draw_tree(c,w,x,y,width=90,dy=13):
 nodes=[];edges=[];leaf=0
 def rec(t,depth):
  nonlocal leaf
  idx=len(nodes);nodes.append(None);ch=[]
  for child in t:j=rec(child,depth+1);ch.append(j);edges.append((idx,j))
  if ch:xx=sum(nodes[j][0] for j in ch)/len(ch)
  else:xx=leaf;leaf+=1
  nodes[idx]=(xx,depth);return idx
 rec(tree(w),0);scale=width/max(1,leaf-1);pos=[(x+(xx-(leaf-1)/2)*scale,y-depth*dy) for xx,depth in nodes]
 for a,b in edges:c.line(*pos[a],*pos[b])
 for i,(xx,yy) in enumerate(pos):c.circle(xx,yy,2,fill=int(i==0))
def draw_path(c,w,x,y,dx=9,dy=9):
 c.setStrokeColor(colors.HexColor('#aaaaaa'));c.line(x,y,x+len(w)*dx,y);c.setStrokeColor(colors.black)
 h=0;p=c.beginPath();p.moveTo(x,y)
 for i,v in enumerate(w,1):h+=1 if v=='U' else -1;p.lineTo(x+i*dx,y+h*dy)
 c.drawPath(p)
