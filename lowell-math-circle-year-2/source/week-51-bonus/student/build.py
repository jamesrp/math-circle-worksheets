#!/usr/bin/env python3
import argparse
from pathlib import Path
from support import *

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,51,'Honest measurement ranges','Grades 2-5',1)
    problem(c,1,'Build every rectangle with whole-number sides at least 1 and A + B = 6. Find its area in square tiles. What are the smallest and largest possible areas? Someone uses A and B each from 1 to 5 and promises an area from 1 to 25. Can either end happen with A + B = 6? Make the tightest honest range.')
    grid(c,64,556,3,2,s=25)
    label(c,'3',101,539,12,True);label(c,'2',49,579,12,True)
    arrow(c,158,581,222,581);label(c,'6 square tiles',239,576,13)
    x,y,s=87,193,56.6929133858
    grid(c,x,y,5,5,s=s)
    label(c,'One square is one tile.',87,168,11)
    for i,l in enumerate(('A','B','Area')):label(c,l,433+i*48,478,11,True)
    for j in range(5):
        for i in range(3):box(c,409+i*48,422-j*47,48,47)
    lines(c,113,1)
    save(c)
    page(c,51,'Honest measurement ranges','Grades 2-5',2)
    para(c,'All cards in one row describe the SAME unchanged hidden length. An end may lie anywhere in a range, including its edges and between ticks.',720,size=13)
    problem(c,2,'In the first row all cards are true: find every possible length. In each other row, exactly one card is false. Which card could it be? Give a possible hidden length for each choice you keep.',658)
    for rowy,vals in [(480,('2 to 7','4 to 9','5 to 6')),(318,('1 to 4','3 to 8','5 to 9')),(156,('1 to 4','6 to 8','7 to 9'))]:
        for i,v in enumerate(vals):
            xx=53+i*177;box(c,xx,rowy,149,61);label(c,v,xx+74.5,rowy+23,16,True)
        ruler(c,69,rowy-41,0,0,maxv=10,unit=45)
    save(c)
    page(c,51,'Honest measurement ranges','Grades 2-5',3)
    para(c,'Align both starts at 0. Each length may vary separately anywhere in its band, including the edges. The end gap is the distance between the ends, whichever strip is longer.',720,size=13)
    problem(c,3,'For each pair, find the closest and farthest possible ends. Can A be longer, can B be longer, and can they match? Then invent two range cards that always keep the gap at most 2 units, while either strip can be longer.',654)
    for yy,a,b in [(501,(3,7),(5,9)),(350,(2,4),(6,8)),(199,(3,5),(5,7))]:
        ruler(c,95,yy,*a,maxv=10,unit=39,tag='A')
        ruler(c,95,yy-61,*b,maxv=10,unit=39,tag='B')
    label(c,'My cards:',43,92,12);lines(c,81,1,x=113,width=456)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
