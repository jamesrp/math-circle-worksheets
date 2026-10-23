from pathlib import Path
import math
from examples import edge_groups_example
ROOT=Path(__file__).resolve().parent

def text(x,y,w,s,size=13):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,align=left,font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def lab(x,y,s,size=11,anchor='center'):
    s=s.replace('_',r'\_')
    return rf'\node[anchor={anchor},inner sep=1pt,font=\fontsize{{{size}}}{{{size*1.2}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x1,y1,x2,y2,opts=''):
    return rf'\draw[{opts}] ({x1},{y1})--({x2},{y2});'+'\n'
def blank(x,y,w,h):
    return rf'\draw[gray!45,line width=.3pt] ({x},{y}) rectangle ++({w},{h});'+'\n'
def rules(y,w=180):return line(16,y,16+w,y,'gray!40')
def problem(n,y,s,band):return text(16,y,180,rf'\textbf{{Problem {n}:}} {s}',14 if band=='k-1' else 12.5)
def page(week,topic,band,num,body,last=False):
    level={'k-1':'K--1','grades-2-3':'Grades 2--3','grades-4-5':'Grades 4--5'}[band]
    bid={'k-1':'K','grades-2-3':'23','grades-4-5':'45'}[band]
    return r'\null\begin{tikzpicture}[remember picture,overlay,shift={(current page.north west)},x=1mm,y=-1mm,line cap=round,line join=round]'+'\n'+text(16,11,182,rf'Week {week} / {topic} / {level}',10.5)+line(16,19,200,19,'gray!55')+body+text(16,266,174,rf'Bellingham Math Circle / Week {week} / F{week}-{bid}-v3',9)+lab(198,268,str(num),9)+r'\end{tikzpicture}'+('\n\\newpage\n' if not last else '\n')
def write(week,topic,band,bodies):
    pre=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz,amssymb}
\pdfmapfile{+lm.map}
\pdfmapfile{+symbols.map}
\usetikzlibrary{arrows.meta,calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''
    (ROOT/(band+'.tex')).write_text(pre+''.join(page(week,topic,band,i+1,b,last=(i+1==len(bodies))) for i,b in enumerate(bodies))+r'\end{document}'+'\n')
def mark(x,y,kind):
    if kind=='dot':return rf'\fill ({x},{y}) circle (1.6);'+'\n'
    return rf'\draw[line width=.8pt,fill=white] ({x-1.5},{y-1.5}) rectangle ({x+1.5},{y+1.5});'+'\n'
def strip(x,y,w,h,rev=False,halves=False,name=None):
    s=rf'\draw[line width=1pt] ({x},{y}) rectangle ++({w},{h});'+'\n'
    s+=line(x+3,y+h/2,x+w-3,y+h/2,'dashed,gray')
    for xx,r in [(x+4,False),(x+w-4,rev)]:
        s+=mark(xx,y+(h-5 if r else 5),'dot')+mark(xx,y+(5 if r else h-5),'sq')
        ax=xx+(5 if xx==x+4 else -5)
        s+=line(ax,y+(7 if r else h-7),ax,y+(h-7 if r else 7),'-{Stealth[length=2mm]},line width=.7pt')
    if halves:s+=lab(x+w/2,y+h/4,'U',14)+lab(x+w/2,y+3*h/4,'L',14)
    if name:s+=lab(x-6,y+h/2,name,13)
    return s

def seam_example(y):
    s=lab(46,y,'input',10)+lab(102,y,'process',10)+lab(158,y,'output',10)
    s+=strip(18,y+9,61,24)
    s+=text(86,y+12,31,r'Join $\bullet$ to $\bullet$ and $\square$ to $\square$.',10)
    # Genuine annulus shown as cylinder with same identified seam labels.
    s+=r'\draw[line width=1pt] (136,'+str(y+18)+r') ellipse (23 and 6);'+'\n'
    s+=rf'\draw[line width=1pt] (113,{y+18})--(113,{y+39}) arc[start angle=180,end angle=0,x radius=23,y radius=6]--(159,{y+18});'+'\n'
    s+=rf'\draw[dashed] (113,{y+39}) arc[start angle=180,end angle=360,x radius=23,y radius=6];'+'\n'
    s+=line(136,y+24,136,y+45,'line width=1pt')+mark(136,y+25,'dot')+mark(136,y+43,'sq')
    return s


def dot_groups(x,y,parts):
    s=''; cursor=x
    for n in parts:
        w=max(17,8*n+6)
        s+=rf'\draw[line width=.6pt] ({cursor+w/2},{y}) ellipse ({w/2} and 6);'+'\n'
        for k in range(n):s+=mark(cursor+w/2+8*(k-(n-1)/2),y,'dot')
        cursor+=w+4
    return s

def choices(y,left='A',right='B'):
    s=''
    for i,parts in enumerate([(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]):
        yy=y+i*29
        s+=dot_groups(23,yy,parts)+lab(153,yy,left+': ___',11)+lab(184,yy,right+': ___',11)
    return s

def moving_arrow(y):
    s=line(25,y,178,y)+line(25,y+28,178,y+28)+line(25,y+14,178,y+14,'dashed,gray')
    s+=line(56,y+5,56,y+23,'-{Stealth[length=3mm]},line width=1.4pt')
    s+=line(142,y+5,142,y+23,'-{Stealth[length=3mm]},line width=1.4pt')
    s+=line(73,y+14,125,y+14,'-{Stealth[length=2mm]},line width=.8pt')
    s+=lab(56,y+35,'start marker',10)+lab(142,y+35,'after a short slide',10)
    return s

for band in ['k-1','grades-2-3','grades-4-5']:
    b=[]
    shared='Keep the bands on the table. An adult makes every cut. The rectangles are joining recipes.'
    convention='An edge trip stays on an edge, follows its seam marks, and stops on its first return to the start dot.'
    q1={
    'k-1':'Trace every edge of A and B. Give each separate closed edge its own color.',
    'grades-2-3':'Trace all the edges of A and B. How many separate closed edges does each band have?',
    'grades-4-5':'Trace all the edges of A and B. Show on each flat recipe where each separate closed edge goes through the seam.'}[band]
    s=text(16,25,180,shared,11.5)+seam_example(47)+text(16,97,180,convention,11.5)+problem(1,124,q1,band)
    s+=strip(26,162,163,30,False,name='A')+strip(26,210,163,30,True,name='B')
    s+=lab(103,253,'A: ____________       B: ____________',12)
    b.append(s)
    q2={
    'k-1':'Put two dots on the edges of A so one edge trip reaches both, then try to place them so no one trip reaches both. Repeat with B.',
    'grades-2-3':'On A and B, find two edge dots that one edge trip can visit together, and two that it cannot. Which requests are impossible?',
    'grades-4-5':'One separate closed edge is a boundary component. Explain the number of boundary components of A and B from their seam recipes.'}[band]
    s=problem(2,27,q2,band)
    q3='Place four edge dots to match each picture on A and on B, or cross it out. Each ring means a different closed edge; other edges may have no dots.'
    s+=edge_groups_example(text,lab,line)
    b.append(s)
    b.append(problem(3,27,q3,band)+choices(85))
    q4={
    'k-1':'Guess how many pieces each band will make when an adult cuts its middle line. Ask the adult to cut A and B, and draw what you get.',
    'grades-2-3':'Predict how many connected pieces a middle-line cut will make in A and B. Ask an adult to make both cuts and record what happened.',
    'grades-4-5':'Predict the number of connected pieces after a middle-line cut in A and B. Have an adult cut both bands, then count the pieces and the boundary components of each piece.'}[band]
    s=problem(4,27,q4,band)+strip(25,78,73,28,False,True,'A')+strip(124,78,73,28,True,True,'B')
    s+=lab(58,125,'I predict: ______',12)+lab(158,125,'I predict: ______',12)
    s+=blank(16,141,84,94)+blank(112,141,84,94)+lab(58,244,'after cutting A',11)+lab(154,244,'after cutting B',11)
    b.append(s)
    q5={
    'k-1':'Trace every edge of each cut piece. Can two dots be on the same piece but on different closed edges?',
    'grades-2-3':'Use the U and L marks to explain why the cuts made that many pieces. On each cut result, can two edge dots lie on the same piece but on different closed edges?',
    'grades-4-5':'Use U and L to explain the connected pieces after the cuts. Explain separately the number of boundary components on each piece.'}[band]
    s=problem(5,27,q5,band)+strip(23,82,173,30,False,True,'A')+strip(23,137,173,30,True,True,'B')+blank(16,188,180,60)
    b.append(s)
    if band!='grades-4-5':
        s=problem(6,27,'Use all the cut pieces from A together, then all those from B. Which four-dot pictures from Problem 3 can you now make?',band)
        s+=choices(88)
        s+=problem(7,226,'Arrange four edge dots so every cut piece has a dot and no edge trip reaches two dots. Can you do it with each cut result?',band)
    else:
        s=problem(6,27,'Ask an adult to rebuild uncut A and B from the two spare strips. Put a removable arrow across each strip, pointing from U toward L. Slide it along the middle line for one full trip, keeping it across the strip.',band)
        s+=moving_arrow(85)
        s+=text(16,132,180,'Compare the returning arrow with its starting position. Explain its return direction from the seam.',12.5)+blank(16,154,180,44)
        s+=problem(7,211,'Which four-dot pictures from Problem 3 are possible after each cut? Explain how your answer separates connected pieces from boundary components.',band)+blank(16,244,180,13)
    b.append(s)
    write(38,'Seams',band,b)
