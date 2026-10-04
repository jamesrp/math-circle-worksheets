#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import *

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,47,'Gentle-step landscapes','Grades 2-5',1)
    para(c,'Put a nonnegative whole height at every square. Joined squares may differ by at most 1. Gray clues stay fixed. There is no fixed total number of cubes.',720,size=13)
    problem(c,1,'Fill each board, or explain why it cannot be filled. Does closing a row into a ring change what is possible? On the ring that works, make B and C as high as they can be at the same time.',656)
    pts=[(95+i*104,518) for i in range(5)]
    graph(c,pts,[(i,i+1) for i in range(4)],{0:0,3:3},list('ABCDE'),side=62)
    cycle(c,167,281,5,r=83,clues={0:0,3:3},labels=list('ABCDE'),side=62)
    cycle(c,446,281,5,r=83,clues={0:0,3:2},labels=list('ABCDE'),side=62)
    lines(c,120,2)
    save(c)
    page(c,47,'Gentle-step landscapes','Grades 4-5',2)
    problem(c,2,'Change the start into the finish with the fewest moves. A move raises or lowers one white height by 1; the row must stay legal after every move. Can two legal rows with the same fixed clues ever require extra moves beyond their individual height changes? Try other pairs and explain your conclusion.')
    for y,title,vals in [(575,'Start',[1,2,3,2,1,0,1]),(483,'Finish',[1,0,1,2,3,2,1])]:
        label(c,title,43,y+8,12)
        for i,v in enumerate(vals):
            x=117+i*65;box(c,x-24,y-23,48,46,Color(.9,.92,.94) if i in (0,6) else white)
            label(c,str(v),x,y-5,16,True);label(c,chr(65+i),x,y+31,10,True)
    label(c,'One height marker per column',306,398,11,True)
    x,y,s,level=90,140,69,57
    c.setStrokeColor(LIGHT);c.setLineWidth(.7)
    for i in range(7):c.line(x+i*s,y,x+i*s,y+4*level)
    for j in range(5):c.line(x,y+j*level,x+6*s,y+j*level)
    for i in range(7):label(c,chr(65+i),x+i*s,y-20,11,True)
    for j in range(5):label(c,str(j),x-18,y+j*level-4,11,True)
    c.setFillColor(INK)
    for i in (0,6):c.circle(x+i*s,y+level,6,stroke=1,fill=1)
    lines(c,90,1)
    save(c)
    page(c,47,'Gentle-step landscapes','Grades K-5',3)
    problem(c,3,'Build this ring with exactly 2, 5, 8, 10, and 11 cubes. Which budgets work? Find the smallest and largest possible totals. Can every whole budget between them be built? Gray towers stay at 1; neighboring towers differ by at most 1.')
    cycle(c,306,447,6,r=141,clues={0:1,3:1},side=68,labels=list('ABCDEF'))
    label(c,'Budget',79,206,12)
    for i,t in enumerate((2,5,8,10,11)):
        x=180+i*83;label(c,str(t),x,206,14,True);box(c,x-29,132,58,53)
    lines(c,97,1)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
