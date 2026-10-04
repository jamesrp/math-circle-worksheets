"""Portable drawing helpers. Requires reportlab>=4.0; US Letter at actual size."""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import math

W,H=612,792
INK=HexColor('#222b33'); LIGHT=HexColor('#d5dadd'); GRAY=HexColor('#a8b2b8')
RED=HexColor('#dc7470'); BLUE=HexColor('#70a3d0')

def make_canvas(path):
    c=canvas.Canvas(str(path),pagesize=(W,H),invariant=1)
    c.setTitle('Bellingham Math Circle: bonus investigations')
    return c

def page(c,week,topic,band,num):
    c.setFillColor(INK); c.setStrokeColor(INK)
    c.setFont('Helvetica',12)
    c.drawString(43,754,f'Week {week} / {topic} / {band}')
    c.setLineWidth(.55); c.line(43,743,569,743)
    c.setFont('Helvetica',9)
    c.drawString(43,29,f'Bellingham Math Circle / Week {week} / F{week}B-S')
    c.drawRightString(569,29,str(num))

def para(c,text,y,x=43,width=526,size=14,leading=19):
    sty=ParagraphStyle('plain',fontName='Helvetica',fontSize=size,leading=leading,textColor=INK)
    p=Paragraph(text,sty); _,h=p.wrap(width,720)
    p.drawOn(c,x,y-h); return y-h

def problem(c,n,text,y=720):
    return para(c,f'<b>Problem {n}:</b> {text}',y)

def label(c,text,x,y,size=11,center=False):
    c.setFillColor(INK); c.setFont('Helvetica',size)
    (c.drawCentredString if center else c.drawString)(x,y,text)

def box(c,x,y,w,h,fill=None):
    c.setStrokeColor(LIGHT); c.setLineWidth(.8)
    if fill: c.setFillColor(fill)
    c.rect(x,y,w,h,stroke=1,fill=bool(fill)); c.setFillColor(INK)

def lines(c,y,count=3,x=43,width=526,gap=27):
    c.setStrokeColor(LIGHT); c.setLineWidth(.55)
    for k in range(count): c.line(x,y-k*gap,x+width,y-k*gap)
    c.setStrokeColor(INK)

def arrow(c,x1,y1,x2,y2):
    c.setStrokeColor(INK); c.setLineWidth(.8); c.line(x1,y1,x2,y2)
    a=math.atan2(y2-y1,x2-x1); d=7
    for s in [-1,1]:
        c.line(x2,y2,x2-d*math.cos(a+s*.43),y2-d*math.sin(a+s*.43))

def row(c,x,y,values=None,n=3,step=78,rad=29,letters=None):
    if values is None: values=[None]*n
    for i,v in enumerate(values):
        cx=x+i*step
        c.setStrokeColor(INK);c.setLineWidth(.9)
        c.setFillColor(RED if v=='R' else BLUE if v=='B' else white)
        c.circle(cx,y,rad,stroke=1,fill=1)
        if v is not None: label(c,str(v),cx,y-5,14,True)
        label(c,str(i+1) if letters is None else letters[i],cx,y+rad+9,10,True)
    c.setFillColor(INK)

def record_rows(c,n,x,y,rows=6,w=215):
    step=w/n
    for r in range(rows):
        label(c,str(r),x-13,y-r*24+7,9)
        for i in range(n): box(c,x+i*step,y-r*24,step,23)

def graph(c,pts,edges,clues=None,labels=None,side=62):
    clues=clues or {}; labels=labels or [str(i+1) for i in range(len(pts))]
    c.setStrokeColor(INK); c.setLineWidth(1.1)
    for a,b in edges: c.line(*pts[a],*pts[b])
    for i,(x,y) in enumerate(pts):
        c.setFillColor(Color(.90,.92,.94) if i in clues else white)
        c.rect(x-side/2,y-side/2,side,side,stroke=1,fill=1)
        if i in clues: label(c,str(clues[i]),x,y-5,16,True)
        label(c,labels[i],x,y+side/2+8,11,True)

def cycle(c,x,y,n,r=115,clues=None,side=62,labels=None,values=None):
    pts=[(x+r*math.cos(math.pi/2-i*2*math.pi/n),y+r*math.sin(math.pi/2-i*2*math.pi/n)) for i in range(n)]
    graph(c,pts,[(i,(i+1)%n) for i in range(n)],clues,['']*n,side)
    for i,(px,py) in enumerate(pts):
        a=math.pi/2-i*2*math.pi/n
        label(c,(labels or [str(k+1) for k in range(n)])[i],px+(side/2+18)*math.cos(a)/max(abs(math.cos(a)),abs(math.sin(a))),py+(side/2+18)*math.sin(a)/max(abs(math.cos(a)),abs(math.sin(a)))-3,11,True)
    if values is not None:
        for (px,py),v in zip(pts,values): label(c,str(v),px,py-5,15,True)
    return pts

def grid(c,x,y,nx,ny,s=30,labels=False,dots=False):
    c.setStrokeColor(LIGHT); c.setLineWidth(.7)
    for i in range(nx+1): c.line(x+i*s,y,x+i*s,y+ny*s)
    for j in range(ny+1): c.line(x,y+j*s,x+nx*s,y+j*s)
    if dots:
        c.setFillColor(INK)
        for i in range(nx+1):
            for j in range(ny+1): c.circle(x+i*s,y+j*s,2.5,fill=1,stroke=0)
    if labels:
        for i in range(nx+1): label(c,str(i),x+i*s,y-17,10,True)
        for j in range(ny+1): label(c,str(j),x-17,y+j*s-3,10,True)

def poly(c,pts,fill=GRAY,stroke=True):
    p=c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]:p.lineTo(*pt)
    p.close(); c.setFillColor(fill);c.setStrokeColor(INK);c.setLineWidth(.9)
    c.drawPath(p,stroke=int(stroke),fill=1);c.setFillColor(INK)

def ruler(c,x,y,lo,hi,maxv=12,unit=31,tag=''):
    if tag: label(c,tag,x,y+28,12)
    c.setFillColor(Color(.80,.84,.87)); c.rect(x+lo*unit,y+2,(hi-lo)*unit,13,stroke=0,fill=1)
    c.setStrokeColor(INK);c.setLineWidth(.8);c.line(x,y,x+maxv*unit,y)
    for i in range(maxv+1):
        c.line(x+i*unit,y-3,x+i*unit,y+3);label(c,str(i),x+i*unit,y-18,10,True)
    c.setFillColor(INK)

def save(c): c.showPage()
