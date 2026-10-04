#!/usr/bin/env python3
"""Portable student-companion builder. Requires reportlab. No repository imports."""
from pathlib import Path
import argparse, math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

W,H=612,792
ROOT=Path(__file__).resolve().parent
STYLE=ParagraphStyle('body',fontName='Helvetica',fontSize=13,leading=18,textColor=black)
C=None
WEEK=44
TOPIC='The bag that copies'

def para(s,x=44,y=718,width=524,size=13,leading=18):
    style=ParagraphStyle('p',parent=STYLE,fontSize=size,leading=leading)
    p=Paragraph(s,style); w,h=p.wrap(width,700);p.drawOn(C,x,y-h);return y-h

def label(s,x,y,size=11,center=False,bold=False):
    C.setFillColor(black);C.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
    (C.drawCentredString if center else C.drawString)(x,y,str(s))

def page(band,n):
    label(f'Week {WEEK} / {TOPIC} / {band}',44,751,13,bold=True)
    C.setStrokeColor(HexColor('#555555'));C.setLineWidth(.55);C.line(44,738,568,738)
    label(f'Bellingham Math Circle / Week {WEEK} / W{WEEK}-BONUS-v1',44,34,9)
    label(n,560,34,9)

def end(): C.showPage()

def box(x,y,w,h,stroke='#888888',fill=None):
    C.setStrokeColor(HexColor(stroke));C.setLineWidth(.7)
    if fill:C.setFillColor(HexColor(fill))
    C.rect(x,y,w,h,stroke=1,fill=bool(fill))

def lines(x,y,w,count=3,step=25):
    C.setStrokeColor(HexColor('#bbbbbb'));C.setLineWidth(.4)
    for i in range(count):C.line(x,y-i*step,x+w,y-i*step)

def grid(x,y,rows,cols,cell=50,labels=None):
    for r in range(rows):
        for col in range(cols):
            box(x+col*cell,y+r*cell,cell,cell)
            if labels:label(labels[r][col],x+(col+.5)*cell,y+(r+.5)*cell-4,12,True)

def token(s,x,y,r=15):
    fill={'R':'#e9a09f','B':'#aac5e6','G':'#b8d6aa'}.get(s[0],'#f2f2f2')
    C.setStrokeColor(black);C.setLineWidth(.8);C.setFillColor(HexColor(fill));C.circle(x,y,r,stroke=1,fill=1)
    label(s,x,y-4,10,True)

def arrow(x1,y1,x2,y2):
    C.setStrokeColor(black);C.setFillColor(black);C.setLineWidth(1.1);C.line(x1,y1,x2,y2)
    a=math.atan2(y2-y1,x2-x1);p=C.beginPath();p.moveTo(x2,y2)
    p.lineTo(x2-7*math.cos(a-.4),y2-7*math.sin(a-.4));p.lineTo(x2-7*math.cos(a+.4),y2-7*math.sin(a+.4));p.close();C.drawPath(p,stroke=1,fill=1)

def word(w,x,y,size=15):
    label(w,x,y,size,bold=True)

def portal(x,y,cell=78):
    grid(x,y,3,3,cell,[['F','G','I'],['D','H','E'],['A','B','C']])
    # Seam connections preserve direction and row/column.
    for t in [0.5,1.5,2.5]:
        arrow(x+3*cell+4,y+t*cell,x+3*cell+18,y+t*cell)
        arrow(x-18,y+t*cell,x-4,y+t*cell)
    C.setStrokeColor(black)

def copies(x,y,cell=24):
    for r in range(9):
        for q in range(9):
            s=[['F','G','I'],['D','H','E'],['A','B','C']][r%3][q%3]
            box(x+q*cell,y+r*cell,cell,cell,stroke='#bbbbbb')
            label(s,x+(q+.5)*cell,y+(r+.5)*cell-3,7.8,True)
    C.setStrokeColor(black);C.setLineWidth(1.2)
    for j in range(4): C.line(x+j*3*cell,y,x+j*3*cell,y+9*cell);C.line(x,y+j*3*cell,x+9*cell,y+j*3*cell)
    C.setLineWidth(2);C.rect(x+3*cell,y+3*cell,3*cell,3*cell,stroke=1,fill=0)
    label('original',x+4.5*cell,y+4*cell-4,7,True)

def make():
    page('Grades 2-5',1)
    para('Start with R0 and B0. A random draw gives every counter the same chance. Always return the draw and mix. Any new counter gets the number of the draw that added it.',y=718)
    label('input',48,640,10);token('R0',72,605);token('B0',112,605)
    label('draw R0; add the other color',165,640,10);token('R0',213,605);arrow(245,605,309,605)
    label('output',348,640,10);token('R0',355,605);token('B0',396,605);token('B1',437,605)
    para('<b>Problem 1:</b> Compare three rules: add the drawn color, add the other color, or add nothing. Start R0, B0 for each story. Which rule most often gives one red and one blue draw in two draws? Settle it using all the marked stories.',y=549)
    for i,rule in enumerate(['add drawn color','add other color','add nothing']):
        xx=44+i*178;box(xx,168,166,285);label(rule,xx+83,431,11,True)
        for j in range(6):lines(xx+12,397-j*35,142,1)
    lines(44,129,524,2,31)
    end()
    page('Grades 2-5',2)
    para('Use the copying rule: start R0, B0; return each draw, add its own color, and mix. Choose a possible story yourself when designing a bag. For the next random draw, every counter now in the bag has the same chance.',y=718)
    para('<b>Problem 2:</b> After four copying draws, make the next red draw as likely as possible, as unlikely as possible, and exactly as likely as blue. Give a story and a forecast for each. Can different stories give the same forecast?',y=629)
    for i,name in enumerate(['red most likely','red least likely','red and blue tied']):
        yy=386-i*130;box(44,yy,354,112);box(411,yy,157,112)
        label(name,56,yy+92,11);label('next red forecast',424,yy+92,10)
        label('story:',56,yy+19,10);lines(96,yy+19,288,1);lines(425,yy+44,127,1)
    end()
    page('Grades 4-5',3)
    para('Start R0, B0, G0. Return each draw, add one of its own color, and mix. A new copy gets the number of the draw that added it. Original counters stay in the bag.',y=718)
    label('input',44,646,10)
    for i,s in enumerate(['R0','B0','G0']):token(s,63+i*41,610)
    label('draw G0, add G1',196,646,10);token('G0',234,610);arrow(266,610,308,610)
    label('output',341,646,10)
    for i,s in enumerate(['R0','B0','G0','G1']):token(s,348+i*42,610)
    para('<b>Problem 3:</b> Use these equally likely marked two-draw stories to find every final color-count bag. Do all bags have the same chance, even though color words may not? Predict the color-count bags after three draws and test your prediction exactly.',y=550)
    stories=[]
    for a in ['R0','B0','G0']:
        stories += [(a,b) for b in ['R0','B0','G0',a[0]+'1']]
    for i,(a,b) in enumerate(stories):
        xx=44+(i%3)*178;yy=376-(i//3)*79
        box(xx,yy,166,65)
        token(a,xx+35,yy+35,13);arrow(xx+56,yy+35,xx+77,yy+35);token(b,xx+99,yy+35,13)
        label('final:',xx+10,yy+10,9);lines(xx+42,yy+10,113,1)
    lines(44,101,524,2,26)
    end()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT.parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    C=canvas.Canvas(str(args.out/'bonus.pdf'),pagesize=(W,H),invariant=1);C.setTitle(f'Week {WEEK} bonus - {TOPIC}');C.setAuthor('Bellingham Math Circle');make();C.save()
