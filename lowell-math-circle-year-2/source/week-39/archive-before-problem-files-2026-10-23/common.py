from pathlib import Path
import math
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
def page(week,topic,band,num,body,total=4):
    level={'k-1':'K--1','grades-2-3':'Grades 2--3','grades-4-5':'Grades 4--5'}[band]
    bid={'k-1':'K','grades-2-3':'23','grades-4-5':'45'}[band]
    return r'\null\begin{tikzpicture}[remember picture,overlay,shift={(current page.north west)},x=1mm,y=-1mm,line cap=round,line join=round]'+'\n'+text(16,11,182,rf'Week {week} / {topic} / {level}',10.5)+line(16,19,200,19,'gray!55')+body+text(16,266,174,rf'Bellingham Math Circle / Week {week} / F{week}-{bid}-v2',9)+lab(198,268,str(num),9)+r'\end{tikzpicture}'+('\n\\newpage\n' if num<total else '\n')
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
    (ROOT/(band+'.tex')).write_text(pre+''.join(page(week,topic,band,i+1,b,len(bodies)) for i,b in enumerate(bodies))+r'\end{document}'+'\n')
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
    s+=text(166,y+22,30,'same seam marks',10)
    return s
