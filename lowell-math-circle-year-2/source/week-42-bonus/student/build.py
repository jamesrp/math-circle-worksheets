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
WEEK=42
TOPIC='Fair results from a bag'

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

def symbol(s,x,y):
    C.setStrokeColor(black);C.setFillColor(white);C.setLineWidth(1)
    if s=='square':C.rect(x-10,y-10,20,20,stroke=1,fill=0)
    elif s=='circle':C.circle(x,y,11,stroke=1,fill=0)
    else:
        p=C.beginPath();p.moveTo(x,y+12);p.lineTo(x-12,y-10);p.lineTo(x+12,y-10);p.close();C.drawPath(p,stroke=1,fill=0)

def make():
    page('Grades 2-5',1)
    para('Use one unchanged bag containing both colors. Choose each draw independently without looking; each counter has the same chance. Return it and mix after every draw. A rule sees only the color word, in order.',y=718)
    para('<b>Problem 1:</b> Make a three-draw rule that gives a square, circle, or triangle with equal chances for every fixed bag containing both colors. Skip RRR and BBB; use every other word.',y=638)
    for i,s in enumerate(['square','circle','triangle']):symbol(s,182+i*115,542)
    words=['RRR','RRB','RBR','RBB','BRR','BRB','BBR','BBB']
    for i,w in enumerate(words):
        x=44+(i%2)*268;y=452-(i//2)*79
        box(x,y,256,65)
        for j,s in enumerate(w):token(s,x+25+j*37,y+34,13)
        label('output',x+147,y+39,10);lines(x+147,y+19,92,1)
    lines(44,135,524,3,25)
    end()
    page('Grades 4-5',2)
    para('For each pair: BR gives a square, RB a circle, and RR or BB gives nothing. Make four draws from one fixed bag; use the first pair and the second pair. Keep both outputs already made.',y=718)
    label('BRRB',44,620,13,bold=True)
    arrow(111,624,168,624)
    word('BR | RB',183,619,13)
    arrow(274,624,332,624)
    symbol('square',363,624);symbol('circle',407,624)
    label('four draws',44,598,10);label('first pair | second pair',183,598,10)
    label('both outputs kept',344,598,10)
    para('<b>Problem 2:</b> If both pairs were skipped, can you use them to make one extra fair output? Design a rule. Compare output totals on all sixteen equally likely stories from a one-red, one-blue bag. Would it also work for three reds and one blue?',y=569)
    import itertools
    words=[''.join(p) for p in itertools.product('RB',repeat=4)]
    for i,w in enumerate(words):
        x=44+(i%4)*134;y=390-(i//4)*83
        box(x,y,122,73)
        word(w[:2]+' | '+w[2:],x+11,y+49,13)
        label('outputs:',x+11,y+27,10);lines(x+11,y+11,100,1)
    lines(44,116,243,3,24)
    box(306,58,262,69)
    C.setStrokeColor(HexColor('#888888'));C.setLineWidth(.7)
    for x in [410,489]:C.line(x,58,x,127)
    for y in [81,104]:C.line(306,y,568,y)
    symbol('square',449,115);symbol('circle',528,115)
    label('Basic',317,89,10);label('Recycled',317,66,10)
    end()
    page('Grades 2-5',3)
    para('<b>Problem 3:</b> Make two cups of four equal-chance tickets, each showing a left shape and a right shape. At each position, square and circle must have equal chances. One cup must give only two possible pairs; the other must give all four. Does fairness at each position make the whole pair fair?',y=718)
    for group in range(2):
        label(f'Cup {group+1}',44,605-group*258,12)
        for i in range(4):
            x=44+(i%2)*268;y=491-group*258-(i//2)*108
            box(x,y,244,87);label('left',x+63,y+65,10,True);label('right',x+180,y+65,10,True)
            C.setStrokeColor(HexColor('#bbbbbb'));C.line(x+122,y+9,x+122,y+77)
    lines(44,95,524,2,25)
    end()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT.parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    C=canvas.Canvas(str(args.out/'bonus.pdf'),pagesize=(W,H),invariant=1);C.setTitle(f'Week {WEEK} bonus - {TOPIC}');C.setAuthor('Bellingham Math Circle');make();C.save()
