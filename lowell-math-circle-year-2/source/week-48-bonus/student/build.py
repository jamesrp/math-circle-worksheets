#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import *

def lshape(c,x,y,s,shiftx=0,shifty=0):
    # Shape remains unchanged; the grid origin changes by the given fraction.
    poly(c,[(x,y),(x+2*s,y),(x+2*s,y+2*s),(x+s,y+2*s),(x+s,y+s),(x,y+s)])
    ox=x+shiftx*s;oy=y+shifty*s
    c.saveState();clip=c.beginPath();clip.rect(x-.6*s,y-.6*s,3.2*s,3.2*s);c.clipPath(clip,stroke=0,fill=0)
    c.setStrokeColor(INK);c.setLineWidth(.55)
    for i in range(-1,4):
        c.line(ox+i*s,y-.6*s,ox+i*s,y+2.6*s)
        c.line(x-.6*s,oy+i*s,x+2.6*s,oy+i*s)
    c.restoreState()

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,48,'Inside and outside covers','Grades 2-5',1)
    para(c,'One grid square has area 1. Whole gray squares give a lower bound. Every square with positive gray area gives the cover bound. An edge or corner touch alone adds no square.',720,size=13)
    problem(c,1,'Keep this L shape fixed and slide a grid of the same square size. Try the three placements below. Find both bounds for each. Which gives the tightest range? Does moving a grid always improve its bounds?',650)
    for x,y,s,dx,dy,tag in [(107,393,56,0,0,'Aligned'),(401,393,56,.5,0,'Half a square sideways'),(253,143,56,.5,.5,'Half a square both ways')]:
        lshape(c,x,y,s,dx,dy);label(c,tag,x+s,y-58,11,True)
    save(c)
    page(c,48,'Inside and outside covers','Grades 2-5',2)
    para(c,'A range card promises that the same unchanged shape has at least the first area and at most the second area, in square units. Both end numbers are allowed. Each small grid square has area 1.',720,size=13)
    # Essential card convention, not an intersection method.
    poly(c,[(56,600),(113,600),(56,657)])
    box(c,56,600,57,57);arrow(c,130,627,190,627)
    label(c,'0 to 1',232,622,16,True);label(c,'one partial square',85,584,10,True)
    problem(c,2,'Each pair of cards reports on one shape. Make the narrowest range card that keeps every possible area. Which pair cannot be true? For each possible pair, draw a shape whose area fits both cards.',577)
    for y,vals in [(438,('2 to 8','4 to 9')),(344,('3 to 5','6 to 7')),(250,('1 to 6','4 to 4'))]:
        for x,v in [(74,vals[0]),(247,vals[1])]:
            box(c,x,y,136,67);label(c,v,x+68,y+24,16,True)
        box(c,437,y,112,67)
    for x,tag in [(86,'First pair'),(359,'Third pair')]:
        label(c,tag,x+81,211,11,True)
        grid(c,x,84,6,4,s=27)
    save(c)
    page(c,48,'Inside and outside covers','Grades 4-5',3)
    para(c,'The three marked cells must each contain some gray area and some white area. The unmarked cell stays white. Each shape must be connected, with no holes. Keep each shape inside its 2-by-2 board.',720,size=13)
    problem(c,3,'Draw one shape with less than 1 square of gray and another with more than 2. Then make a shape with the same gray area as your first shape but a longer boundary. Can you keep making the boundary longer while keeping its area and cell pattern?',636)
    for x,y in [(92,337),(350,337),(92,105),(350,105)]:
        grid(c,x,y,2,2,s=80)
        for i,j in [(0,0),(1,0),(1,1)]:label(c,'partial',x+(i+.5)*80,y+(j+.5)*80-4,10,True)
        # White mark makes the mask, not an extra gray region.
        label(c,'white',x+40,y+116,10,True)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
