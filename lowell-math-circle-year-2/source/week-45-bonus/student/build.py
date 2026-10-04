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
WEEK=45
TOPIC='The visible side'

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
    para('Choose RR, RB, or BB with equal chances; keep that card hidden. For each clue, independently draw an equal-chance L/R ticket, show that face, then replace and mix. Hide the ticket, face marks, and turning. The guesser sees only the two color clues.',y=718)
    label('input: one card',44,632,10);token('G',68,595);token('B',109,595)
    label('L, replace ticket, R',157,632,10);arrow(145,595,227,595)
    label('output: two clues',259,632,10);token('G',278,595);token('B',319,595)
    label('L face',68,567,9,True);label('R face',109,567,9,True)
    para('<b>Problem 1:</b> Two clues are red, then red. Which card is the best guess? What if the clues are red, then blue? Settle both questions using all twelve equally likely card-and-face stories.',y=538)
    xs=[44,143,249,355,461]; widths=[99,106,106,106,107]
    headers=['card','L then L','L then R','R then L','R then R']
    for j,h in enumerate(headers):box(xs[j],405,widths[j],40);label(h,xs[j]+widths[j]/2,419,10,True)
    for i,cardword in enumerate(['RR','RB','BB']):
        yy=327-i*78
        for j in range(5):box(xs[j],yy,widths[j],78)
        token(cardword[0],69,yy+39,12);token(cardword[1],111,yy+39,12)
        for j in range(1,5):lines(xs[j]+12,yy+32,widths[j]-24,1)
    lines(44,121,524,2,28)
    end()
    page('Grades 4-5',2)
    para('Fix the first choice at door 1. Choose the prize uniformly from doors 1, 2, 3. Independently draw ticket 2 or 3 with equal chances. Host A knows the prize and opens an unchosen empty door; use the ticket only if both are empty. Host B opens the ticket\'s door blindly; discard prize reveals. Hide prize placement and all tickets. The guesser sees only which empty door opens.',y=718)
    label('input: choose P, prize R',44,591,10)
    for i,s in enumerate(['P','Q','R']):
        xx=44+i*59;box(xx,532,49,45);label(s,xx+24.5,548,13,True)
        if s=='R':label('*',xx+39,566,12,True)
        if s=='P':C.setFillColor(black);C.circle(xx+24.5,538,2.5,stroke=0,fill=1)
    arrow(234,555,283,555);label('Host A opens Q',312,591,10)
    for i,s in enumerate(['P','Q','R']):
        xx=312+i*66;box(xx,532,56,45,fill='#eeeeee' if s=='Q' else None);label('empty' if s=='Q' else s,xx+28,548,10 if s=='Q' else 13,True)
        if s=='P':C.setFillColor(black);C.circle(xx+28,538,2.5,stroke=0,fill=1)
    para('<b>Problem 2:</b> After an empty door opens, should you stay at door 1 or switch to the other closed door? Decide for each host using every prize-ticket story. Does the host\'s knowledge change the answer?',y=509)
    for g,name in enumerate(['Host A','Host B']):
        xx=44+g*268;label(name,xx,417,12)
        widths=[45,45,63,91];xs=[xx,xx+45,xx+90,xx+153]
        for j,s in enumerate(['prize','ticket','opens','switch wins?']):box(xs[j],373,widths[j],30);label(s,xs[j]+widths[j]/2,384,9,True)
        for i,(prize,ticket) in enumerate([(1,2),(1,3),(2,2),(2,3),(3,2),(3,3)]):
            yy=338-i*35
            for j in range(4):box(xs[j],yy,widths[j],35)
            label(prize,xs[0]+22.5,yy+13,11,True);label(ticket,xs[1]+22.5,yy+13,11,True)
    lines(44,117,524,2,29)
    end()
    page('Grades 4-5',3)
    para('Draw a hidden counter uniformly from R1, R2, R3, B. The reporter sees its color, then independently draws H1, H2, or F with equal chances. H1 and H2 report the true color; F reports the other color. Hide the counter identity and ticket; show only the R/B report. Return and mix both draws each round.',y=718)
    label('input: hidden B',44,608,10);token('B',97,569)
    label('ticket F: flip color',184,608,10);box(203,550,43,38);label('F',224.5,563,14,True);arrow(274,569,334,569)
    label('output: report R',366,608,10);token('R',416,569)
    para('<b>Problem 3:</b> A blue report arrives. Which hidden color is the better guess? Use every counter-and-report-ticket story. Replace the reporter\'s tickets with four equal-chance tickets, each honest or flipping. Can you make a blue report give both hidden colors equal chances?',y=514)
    x0=44;columns=[86,146,146,146];xs=[44,130,276,422]
    for j,s in enumerate(['counter','H1','H2','F']):box(xs[j],397,columns[j],32);label(s,xs[j]+columns[j]/2,408,10,True)
    for i,s in enumerate(['R1','R2','R3','B']):
        yy=347-i*50
        for j in range(4):box(xs[j],yy,columns[j],50)
        token(s,87,yy+25,13)
        for j in range(1,4):lines(xs[j]+15,yy+20,columns[j]-30,1)
    for i in range(4):
        xx=44+i*134;box(xx,92,122,60);label(i+1,xx+10,133,9);lines(xx+15,xx*0+113,92,1)
    end()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=ROOT.parent);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    C=canvas.Canvas(str(args.out/'bonus.pdf'),pagesize=(W,H),invariant=1);C.setTitle(f'Week {WEEK} bonus - {TOPIC}');C.setAuthor('Bellingham Math Circle');make();C.save()
