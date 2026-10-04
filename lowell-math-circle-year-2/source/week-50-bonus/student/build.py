#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import *

def endpoints(c,x,y,nx,ny,s):
    label(c,'S',x-34,y-10,14,True);label(c,'F',x+nx*s+15,y+ny*s+6,14,True)

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,50,'Staircases and lengths','Grades 2-5',1)
    para(c,'Move from dot to neighboring dot: one step right R, up U, or diagonally right-and-up D. R and U each cost 1 coin. D costs the amount on its price card. These are prices, not string lengths.',720,size=13)
    grid(c,77,603,1,1,s=44,dots=True)
    c.setStrokeColor(INK);arrow(c,77,603,121,647)
    label(c,'R then U: 2 coins',160,635,12);label(c,'D: its card price',160,612,12)
    problem(c,1,'For each price card, build the cheapest route from S to F. Do all cheapest routes use the same number of diagonal steps? Explain how the price changes your choice.',565)
    x,y,s=157,260,74
    grid(c,x,y,4,3,s=s,dots=True);endpoints(c,x,y,4,3,s)
    for i,price in enumerate((1,2,3)):
        xx=58+i*174;box(c,xx,139,148,63);label(c,f'D costs {price}',xx+74,176,14,True);label(c,'Cheapest:',xx+12,153,11)
    lines(c,96,1)
    save(c)
    page(c,50,'Staircases and lengths','Grades 2-5',2)
    problem(c,2,'Use only right and up steps along grid lines. Find every S-to-F route. Then block one dot other than S or F: routes cannot pass through it. Find a blocked dot that leaves exactly 8 routes, and one that leaves exactly 11. Could one blocked dot stop every route? Explain how you check your counts.')
    x,y,s=186,300,80
    grid(c,x,y,3,3,s=s,dots=True,labels=True);endpoints(c,x,y,3,3,s)
    label(c,'A route can be recorded as a word, such as RRUURU.',43,254,12)
    lines(c,223,6,gap=27)
    save(c)
    page(c,50,'Staircases and lengths','Grades 4-5',3)
    problem(c,3,'Stay inside the gray strip, including its boundary, using only horizontal and vertical pieces. Left and down are allowed. Retracing a piece counts its full length again. Make an S-to-F route of length 30 units, then one of length 100 units. Is there a longest finite route? A record may give a piece and its repeat count.')
    x,y,s=136,175,85.0393700787
    pts=[(x,y),(x+.25*s,y),(x+4*s,y+3.75*s),(x+4*s,y+4*s),(x+3.75*s,y+4*s),(x,y+.25*s)]
    poly(c,pts,fill=Color(.85,.88,.90),stroke=False)
    grid(c,x,y,4,4,s=s,labels=True)
    c.setStrokeColor(INK);c.setLineWidth(.65);c.line(x,y,x+4*s,y+4*s)
    c.setFillColor(INK);c.circle(x,y,3,fill=1,stroke=0);c.circle(x+4*s,y+4*s,3,fill=1,stroke=0)
    endpoints(c,x,y,4,4,s)
    label(c,'Gray strip: at most 1/4 unit vertically from the diagonal.',43,139,12)
    c.setStrokeColor(INK);c.line(43,91,43+s,91);c.line(43,86,43,96);c.line(43+s,86,43+s,96)
    label(c,'1 unit = 30 mm',43,69,11)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
