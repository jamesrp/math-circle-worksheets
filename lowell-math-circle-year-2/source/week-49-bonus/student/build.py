#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import *

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,49,'Four-tower differences','Grades 2-5',1)
    para(c,'At each station, the new height is the gap between its old height and the next old height, in A-B-C-D-A order. Keep the whole old ring unchanged until every new height is ready.',720,size=13)
    row(c,68,617,[1,3,2,0],n=4,step=45,rad=15,letters=list('ABCD'))
    arrow(c,238,617,351,617);label(c,'A gap: 3 - 1 = 2',294,643,10,True)
    row(c,391,617,[2,1,2,1],n=4,step=45,rad=15,letters=list('ABCD'))
    problem(c,1,'Find every old ring that makes each printed new ring. Use whole heights from 0 to 3, with at least one 0. Two rings count as different when their A, B, C, D heights differ.',566)
    cycle(c,164,369,4,r=78,side=58,labels=list('ABCD'),values=[1,1,1,1])
    cycle(c,446,369,4,r=78,side=58,labels=list('ABCD'),values=[1,2,1,2])
    for x in (63,345):
        for i,l in enumerate('ABCD'):label(c,l,x+(i+.5)*51,220,10,True)
        record_rows(c,4,x,187,rows=6,w=204,indices=False)
    save(c)
    page(c,49,'Four-tower differences','Grades 4-5',2)
    para(c,'Use only heights 0 and 1. At each station compare its old height with the next old height in number order, wrapping back to 1. Equal gives 0; different gives 1. Keep the old ring unchanged until every new height is ready.',720,size=13)
    problem(c,2,'Try the six-station and eight-station starts. Can a six-station ring repeat without becoming all 0? Can an eight-station start still have a 1 after seven rounds? Decide whether every eight-station start is all 0 by round eight, and explain why.',654)
    cycle(c,160,443,6,r=84,side=62,values=[1,0,0,1,0,0])
    cycle(c,430,443,8,r=90,side=62,values=[1,0,0,0,0,0,0,0])
    for n,x in [(6,64),(8,339)]:
        for i in range(n):label(c,str(i+1),x+(i+.5)*202/n,285,9,True)
    record_rows(c,6,64,258,rows=9,w=202)
    record_rows(c,8,339,258,rows=9,w=202)
    save(c)
    page(c,49,'Four-tower differences','Grades 4-5',3)
    para(c,'Now keep the direction: new = next old - current old. A rise of 2 is +2; a fall of 2 is -2. All four new values still use the same old ring.',720,size=13)
    row(c,68,617,[1,3,3,1],n=4,step=45,rad=15,letters=list('ABCD'))
    arrow(c,238,617,351,617);label(c,'A: 3 - 1 = +2',294,643,10,True)
    row(c,391,617,['+2',0,'-2',0],n=4,step=45,rad=15,letters=list('ABCD'))
    problem(c,3,'Run both starts with the directed rule. Which start gets an entry more than 10 away from 0 within five rounds? Can that run get farther from 0 than any chosen ceiling? Explain why your pattern keeps going.',567)
    row(c,86,433,[0,1,0,1],n=4,step=47,rad=18,letters=list('ABCD'))
    row(c,365,433,[0,0,1,1],n=4,step=47,rad=18,letters=list('ABCD'))
    for x in (64,339):
        for i,l in enumerate('ABCD'):label(c,l,x+(i+.5)*202/4,375,10,True)
    record_rows(c,4,64,345,rows=8,w=202)
    record_rows(c,4,339,345,rows=8,w=202)
    lines(c,95,1)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
