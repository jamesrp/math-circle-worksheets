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
WEEK=43
TOPIC='Shuffling picture cards'

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

def card(s,x,y,size=58,picture=False):
    box(x,y,size,size,stroke='#555555')
    if picture:
        if s[0]=='A':C.setStrokeColor(black);C.rect(x+size/2-10,y+size/2-6,20,20,stroke=1,fill=0)
        else:C.setStrokeColor(black);C.circle(x+size/2,y+size/2+4,11,stroke=1,fill=0)
        label(s,x+size/2,y+8,10,True)
    else:label(s,x+size/2,y+size/2-5,16,True,bold=True)

def row(s,x,y,size=44):
    for i,a in enumerate(s):card(a,x+i*(size+7),y,size)

def blankrow(x,y,size=44):
    for i in range(4):box(x+i*(size+7),y,size,size)

def make():
    page('Grades 2-5',1)
    para('<b>Problem 1:</b> Use cards A1, A2, B1, B2. The two A cards show the same picture, and so do the two B cards. Cover the numbers and find every different picture row. If every labeled order has the same chance, do all picture rows have the same chance? Give an exact reason.',y=718)
    for i,s in enumerate(['A1','A2','B1','B2']):card(s,112+i*99,539,72,True)
    for i in range(8):blankrow(58+(i%2)*274,432-(i//2)*78,44)
    lines(44,117,524,3,25)
    end()
    page('Grades 2-5',2)
    para('A cut moves a front packet to the end without changing either packet\'s order. Choose 0, 1, 2, or 3 front cards with equal chances. Keep the current row between cuts.',y=718)
    label('input',44,642,10);row('WXYZ',44,581,40)
    C.setStrokeColor(black);C.setLineWidth(1.6);C.line(135,575,135,627)
    label('move the front two',151,642,10);arrow(245,600,301,600)
    label('output',329,642,10);row('YZWX',329,581,40)
    para('<b>Problem 2:</b> Start A B C D. Find every row that any number of cuts can make. Can you make A B D C? Now allow reversing the entire row as well as cuts. Which rows become possible? Is a fair first card enough to call this a fair shuffle?',y=545)
    row('ABCD',184,397,44)
    for i in range(10):blankrow(58+(i%2)*274,309-(i//2)*48,34)
    lines(44,84,524,1)
    end()
    page('Grades 4-5',3)
    para('A gap may be before the first card, between two cards, or after the last. Number gaps from left to right. Insert the new card into the chosen gap; keep the old cards in their order.',y=718)
    label('input: X Y and new Z',44,645,10)
    row('XY',90,584,42);card('Z',211,584,42)
    for i,xx in enumerate([83,135.5,188]):
        C.setStrokeColor(black);C.setLineWidth(.6);C.line(xx,580,xx,629)
        label(i+1,xx,568,10,True)
    label('choose gap 2',289,645,10);arrow(270,605,325,605)
    label('output',366,645,10);row('XZY',363,584,42)
    para('<b>Problem 3:</b> Start with all six orders of A, B, C equally likely. Independently draw one of four equal-chance gap tickets to insert D. Find the old row and gap that make each target below. Could one final order come from two different stories? Does this rule give all four-card orders the same chance? Explain.',y=548)
    for i,s in enumerate(['ABCD','DACB','BDCA','CBAD']):
        yy=391-i*70;row(s,58,yy,39);label('old row:',300,yy+27,10);lines(357,yy+25,100,1);label('gap:',469,yy+27,10);lines(497,yy+25,58,1)
    lines(44,81,524,1)
    end()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT.parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    C=canvas.Canvas(str(args.out/'bonus.pdf'),pagesize=(W,H),invariant=1);C.setTitle(f'Week {WEEK} bonus - {TOPIC}');C.setAuthor('Bellingham Math Circle');make();C.save()
