#!/usr/bin/env python3
"""Build the standalone Week 46 bonus student companion."""
import argparse
from pathlib import Path
from support import *

def build(out):
    out.mkdir(parents=True,exist_ok=True);c=make_canvas(out/'bonus.pdf')
    page(c,46,'Boards that forget','Grades 2-5',1)
    para(c,'COPY i to j reads slot i and gives its color to slot j, on each board separately. RESET i to R makes slot i red on both boards. Use the same instructions on both boards.',720,size=13)
    row(c,74,613,['R','B','R'],step=58,rad=18);row(c,74,550,['B','R','B'],step=58,rad=18)
    arrow(c,236,582,347,582);label(c,'COPY 1 to 2',291,604,11,True)
    row(c,391,613,['R','R','R'],step=58,rad=18);row(c,391,550,['B','B','B'],step=58,rad=18)
    problem(c,1,'Find two starts that copies alone can never make alike. Then allow exactly one RESET and find the shortest instruction story that makes every pair of starts finish alike. Choose the story before seeing the starts.',493)
    row(c,222,334,step=84,rad=31);row(c,222,230,step=84,rad=31)
    lines(c,151,3)
    save(c)
    page(c,46,'Boards that forget','Grades 4-5',2)
    para(c,'Draw one of three equal tickets, labeled 1, 2, 3. A story is the tickets in order. Coverage means that every number has appeared.',720,size=13)
    problem(c,2,'With replacement and mixing after each draw, how many three-draw stories have coverage? How many four-draw stories have coverage? Find a way to check that your counts miss none. Compare the three-draw result with drawing without replacement. Could any fixed number of draws guarantee coverage when tickets are replaced?',658)
    for i in range(3):
        box(c,101+i*151,436,105,76);label(c,str(i+1),153+i*151,460,23,True)
    label(c,'Three draws',163,399,12,True);label(c,'Four draws',446,399,12,True)
    box(c,43,171,243,212);box(c,326,171,243,212)
    lines(c,128,2)
    save(c)
    page(c,46,'Boards that forget','Grades 2-5',3)
    para(c,'S sets only the left slot to R. T rotates the whole row one slot left; the old left color moves to the right end. Apply each instruction to both boards.',720,size=13)
    row(c,87,607,['R','B','B'],step=58,rad=18)
    arrow(c,256,607,340,607);label(c,'T',298,624,14,True)
    row(c,390,607,['B','B','R'],step=58,rad=18)
    problem(c,3,'Find the shortest word using S and T that makes any pair of starting boards finish alike. Choose it before seeing the starts. Explain why a shorter word cannot work.',552)
    row(c,222,393,step=84,rad=31);row(c,222,286,step=84,rad=31)
    label(c,'Word:',43,195,13);lines(c,185,4)
    save(c);c.save()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
    build(p.parse_args().out)
