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
WEEK=41
TOPIC='Portals'

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

def replay_example(word_text,letters,y,copy_labels=None):
    label(word_text,44,y+18,12,bold=True)
    xs=[220,340,460]
    for i,(x,s) in enumerate(zip(xs,letters)):
        box(x-19,y-17,38,38)
        label(s,x,y-2,14,True,bold=True)
        label(['start','after '+word_text[0],'round end'][i],x,y-35,9,True)
        if copy_labels:label(copy_labels[i],x,y-49,9,True)
    for i,a in enumerate(word_text):
        arrow(xs[i]+25,y+2,xs[i+1]-25,y+2)
        label(a,(xs[i]+xs[i+1])/2,y+12,10,True)
    if copy_labels:
        C.setStrokeColor(black);C.setDash(3,3);C.line(400,y-18,400,y+7);C.setDash()

def make():
    page('Grades 2-5',1)
    para('R, L, U, D mean one cell right, left, up, down. On the 3-by-3 board, cross an edge to the opposite edge in the same row or column. One word is a whole round. Repeated maps continue beyond the page; their borders do not wrap.',y=718)
    replay_example('RL',['H','E','H'],620)
    para('<b>Problem 1:</b> Start at H. Repeat each word without resetting your pawn. Mark the cell after each whole round. Which words reach every cell at round ends? Make words with different repeating patterns.',y=566)
    portal(65,228,78)
    for i,w in enumerate(['R','RU','RRR','RULD','RRU']):
        word(w,363,437-i*48);lines(413,433-i*48,134,1)
    box(44,66,524,130)
    lines(56,169,495,4,25)
    end()
    page('Grades 4-5',2)
    replay_example('RR',['H','E','D'],693,['original copy','original copy','right copy'])
    para('<b>Problem 2:</b> Make a nine-step trip from H that visits every cell once before returning to H. Find tours with different finishing copies of H on the repeated map. Could a nine-step tour finish in the original copy?',y=628)
    portal(62,304,78)
    copies(346,310,24)
    for yy in [259,210,161,112]:lines(44,yy,524,1)
    end()
    page('Grades 4-5',3)
    para('<b>Problem 3:</b> B and E are closed in every copy. From the original H, reach each circled H in as few steps as possible. Keep a move word for each route. What makes a shorter route impossible?',y=718)
    cell=64;x0=82;y0=181
    letters={(-1,1):'A',(0,1):'B',(1,1):'C',(-1,0):'D',(0,0):'H',(1,0):'E',(-1,-1):'F',(0,-1):'G',(1,-1):'I'}
    for yy in range(-2,5):
        for xx in range(-2,5):
            xxm=(xx+1)%3-1;yym=(yy+1)%3-1;s=letters[(xxm,yym)]
            xp=x0+(xx+2)*cell;yp=y0+(yy+2)*cell
            box(xp,yp,cell,cell,fill='#dddddd' if s in 'BE' else None)
            label('X' if s in 'BE' else s,xp+cell/2,yp+cell/2+3,14,True,bold=s=='H')
            if (xx,yy)==(0,0):label('original',xp+cell/2,yp+cell/2-14,9,True)
            if (xx,yy) in [(3,0),(0,3),(3,3)]:
                C.setStrokeColor(black);C.setLineWidth(1.5);C.circle(xp+cell/2,yp+cell/2+7,17,stroke=1,fill=0)
                label({(3,0):'right copy',(0,3):'up copy',(3,3):'right + up'}[(xx,yy)],xp+cell/2,yp+cell/2-16,9,True)
    for target,yy in [('right copy',149),('up copy',120),('right + up',91)]:
        label(target,44,yy,11);lines(143,yy,425,1)
    lines(44,62,524,1)
    end()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT.parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    C=canvas.Canvas(str(args.out/'bonus.pdf'),pagesize=(W,H),invariant=1);C.setTitle(f'Week {WEEK} bonus - {TOPIC}');C.setAuthor('Bellingham Math Circle');make();C.save()
