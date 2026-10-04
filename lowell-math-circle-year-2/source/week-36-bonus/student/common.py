from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, black, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from pathlib import Path
import argparse, math
W,H=612,792
RED=HexColor('#BA3035'); BLUE=HexColor('#2863AD'); GREEN=HexColor('#288346'); GRAY=Color(.55,.55,.55)
STYLE=ParagraphStyle('body',fontName='Helvetica',fontSize=13,leading=18,textColor=black)
SMALL=ParagraphStyle('small',fontName='Helvetica',fontSize=11,leading=15,textColor=black)
def outdir():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);return a.out
class Packet:
 def __init__(self,out,week,topic):
  self.c=canvas.Canvas(str(out/'bonus.pdf'),pagesize=(W,H),invariant=1,pageCompression=1);self.week=week;self.topic=topic;self.page=0
 def start(self,band):
  self.page+=1;c=self.c;c.setFillColor(black);c.setStrokeColor(black);c.setLineWidth(1);c.setFont('Helvetica',11)
  c.drawString(36,755,f'Week {self.week} / {self.topic} / {band}')
  c.setFont('Helvetica',10);c.drawString(36,28,f'Bellingham Math Circle / Week {self.week} / W{self.week}-BONUS-v1');c.drawRightString(576,28,str(self.page))
 def end(self):self.c.showPage()
 def save(self):self.c.save()
def para(c,text,y=715,x=36,width=540,small=False):
 p=Paragraph(text,SMALL if small else STYLE);_,h=p.wrap(width,700);p.drawOn(c,x,y-h);return y-h
def problem(c,n,text,y=715):return para(c,f'<b>Problem {n}:</b> {text}',y)
def label(c,t,x,y,size=11):c.setFillColor(black);c.setFont('Helvetica',size);c.drawCentredString(x,y,t)
def poly(c,pts,fill=None,width=1):
 p=c.beginPath();p.moveTo(*pts[0]);
 for q in pts[1:]:p.lineTo(*q)
 p.close();c.setLineWidth(width);c.setFillColor(fill or white);c.setStrokeColor(black);c.drawPath(p,fill=bool(fill),stroke=1)
def line(c,x1,y1,x2,y2,width=1,color=black,dash=None):
 c.setStrokeColor(color);c.setLineWidth(width);c.setDash(dash or []);c.line(x1,y1,x2,y2);c.setDash([])
def circle(c,x,y,r,fill=None):
 c.setStrokeColor(black);c.setLineWidth(1);c.setFillColor(fill or white);c.circle(x,y,r,fill=bool(fill),stroke=1)
def workspace(c,y=300,height=190):
 c.setStrokeColor(Color(.85,.85,.85));c.setLineWidth(.7);c.roundRect(36,y-height,540,height,6,fill=0,stroke=1)
def motif(c,x,y,s=25,mirror=False,color=None):
 pts=[(-.36,-.5),(-.1,-.5),(-.1,-.08),(.22,-.08),(.22,.15),(-.1,.15),(-.1,.3),(.36,.3),(.36,.5),(-.36,.5)]
 poly(c,[(x+s*a,y+s*(-b if mirror else b)) for a,b in pts],color)
def tile(c,x,y,shape,fill,s=20):
 # The three fills are open, striped, solid; ownership colors are separate counters.
 def path():
  p=c.beginPath()
  if shape==0:p.circle(x,y,s/2)
  elif shape==1:
   p.moveTo(x,y+s*.58);p.lineTo(x-s*.55,y-s*.4);p.lineTo(x+s*.55,y-s*.4);p.close()
  else:p.rect(x-s/2,y-s/2,s,s)
  return p
 p=path();c.setLineWidth(1.5);c.setStrokeColor(black);c.setFillColor(GRAY if fill==2 else white);c.drawPath(p,fill=1,stroke=1)
 if fill==1:
  c.saveState();c.clipPath(path(),stroke=0,fill=0)
  for d in range(-40,41,7):line(c,x+d-20,y-30,x+d+40,y+30,.8,GRAY)
  c.restoreState()
def board9(c,x,y,cell=108,numbers=None):
 for a in range(3):
  for b in range(3):
   cx=x+b*cell;cy=y-a*cell;c.setStrokeColor(Color(.8,.8,.8));c.setLineWidth(.7);c.rect(cx-cell/2,cy-cell/2,cell,cell)
   tile(c,cx,cy,a,b,cell*.37)
   if numbers:label(c,str(numbers),cx,cy-cell*.36,10)
def graph(c,points,edges):
 for a,b in edges:line(c,*points[a],*points[b],1.5)
 for a,(x,y) in points.items():circle(c,x,y,10,white);label(c,a,x,y-4,11)
def arrow(c,x1,y1,x2,y2):
 line(c,x1,y1,x2,y2,1)
 ang=math.atan2(y2-y1,x2-x1)
 for a in [ang+.45,ang-.45]:line(c,x2,y2,x2-8*math.cos(a),y2-8*math.sin(a),1)
