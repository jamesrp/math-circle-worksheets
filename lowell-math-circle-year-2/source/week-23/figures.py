"""Week 23 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres from the top-left corner of the paper, y down. Each page is
one overlay picture on the whole sheet that draws its own header, footer and page number
(page_open and page_close); the page body is shifted to (1.5, 1.8). Problem files call the
functions below by name in their `figure` sections and give the machines' bars there; the
rule, prompt and example wording lives in the problem files.
"""
from itertools import permutations

WIDTH=18.59


# ---------------------------------------------------------------- drawing primitives (build_packets.py)

def txt(x,y,text,width=18.59,size=14,leading=None):
    if leading is None: leading=size*1.30
    return rf'\node[anchor=north west,inner sep=0pt,align=left,text width={width}cm,font=\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{text}}};'+'\n'

def problem(n,text,size=14,y=0):
    return txt(0,y,rf'\textbf{{Problem {n}:}} '+text,size=size)

def card(x,y,val=None,size=1.05,dots=False):
    s=rf'\draw[line width=0.65pt,fill=white] ({x-size/2},{y-size/2}) rectangle ({x+size/2},{y+size/2});'+'\n'
    if val is None:return s
    if dots:
        points={0:[],1:[(0,0)],2:[(-.19,0),(.19,0)],3:[(-.19,.16),(.19,.16),(0,-.19)],4:[(-.19,-.19),(-.19,.19),(.19,-.19),(.19,.19)]}[int(val)]
        for dx,dy in points:s+=rf'\fill ({x+dx*size},{y+dy*size}) circle[radius={.066*size}cm];'+'\n'
    else:
        s+=rf'\node[font=\fontsize{{14}}{{17}}\selectfont] at ({x},{y}) {{{val}}};'+'\n'
    return s

def bank(vals,x=4.8,y=3,dots=False,size=1.35,step=2.2):
    return ''.join(card(x+i*step,y,v,size,dots) for i,v in enumerate(vals))

def network(n,bars,x=.25,y=5,w=18.0,gap=1.3,blank=True,bar_xs=None,outs=None,ins=None):
    s=''
    for i in range(n):
        yy=y+i*gap
        s+=rf'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({x+.1},{yy}) {{{i+1}}};'+'\n'
        s+=rf'\draw[line width=.65pt,->,>=stealth] ({x+1.8},{yy}) -- ({x+w-1.18},{yy});'+'\n'
        s+=card(x+1.1,yy,ins[i] if ins else None,.92)
        s+=card(x+w-.57,yy,outs[i] if outs else None,.92)
    if bar_xs is None:
        bar_xs=[x+3.1+j*(w-6.4)/max(1,len(bars)-1) for j in range(len(bars))]
    for (a,b),xx in zip(bars,bar_xs):
        s+=rf'\draw[line width=1.4pt] ({xx},{y+(a-1)*gap}) -- ({xx},{y+(b-1)*gap});'+'\n'
        for k in (a,b):s+=rf'\fill ({xx},{y+(k-1)*gap}) circle[radius=.095cm];'+'\n'
    return s

def start_column(vals,x,y,step=.91,size=.72,dots=False):
    s=''
    for j,v in enumerate(vals):s+=card(x,y+j*step,v,size,dots)
    return s

def line(x1,y,x2=18.59):
    return rf'\draw[black!20,line width=.4pt] ({x1},{y}) -- ({x2},{y});'+'\n'


# ---------------------------------------------------------------- page template (build_packets.py's packet)

PREAMBLE=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[letterpaper,margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PREAMBLE


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=-1cm]'+'\n'
            + r'\begin{scope}[shift={(current page.north west)}]'+'\n'
            + txt(1.5,.75,f'Week {page.week} / {page.topic} / {page.header}',width=18.59,size=11.5,leading=14)
            + r'\begin{scope}[shift={(1.5,1.8)}]'+'\n')


def page_close(page):
    return (r'\end{scope}'+'\n'
            + txt(1.5,26.85,f'Bellingham Math Circle / Week {page.week} / {page.footer}',width=16.7,size=9,leading=11)
            + txt(19.3,26.85,str(page.number),width=.8,size=9,leading=11)
            + r'\end{scope}\end{tikzpicture}'+'\n')


# The shared rules keep their own leading: 14 pt on 18 (K-1) and 12.5 pt on 16 (grades 2-5).
# Other text, and every prompt, uses the old default of 1.3 times the size.
RULE_LEADING={14:18,12.5:16}


def page_prompt(n, body, x, y, size):
    """The old problem(): 17 pt for K-1, 14 pt for grades 2-3 and 13.5 pt for grades 4-5 (week.toml)."""
    return problem(n,body,size=size,y=0 if y is None else y)


def page_text(x, y, body, w, size):
    return txt(0 if x is None else x,0 if y is None else y,body,size=size,leading=RULE_LEADING.get(size))


# ---------------------------------------------------------------- figures used by more than one problem

def start_grid(starts,xs,ys,step=1.05,size=.9,dots=True):
    """Starting orders as columns of cards, filling each row of xs before the next y."""
    return ''.join(start_column(v,xs[j%len(xs)],ys[j//len(xs)],step=step,size=size,dots=dots) for j,v in enumerate(starts))

ORDERS3=list(permutations([1,2,3]))


# ---------------------------------------------------------------- grades 4-5 worked examples

def threshold_example(caption,input_label,row_label,rule):  # Problem 3: 3, 7, 4 at t = 4
    p=txt(0,0,caption,size=12.5)
    p+=txt(0,1.2,input_label,width=2.0,size=12)
    p+=txt(0,2.6,row_label,width=2.6,size=12)
    for j,(value,result) in enumerate([(3,0),(7,1),(4,0)]):
        xx=4.3+j*1.6
        p+=card(xx,1.3,value,.90)+card(xx,2.75,result,.90)
        p+=rf'\draw[->,>=stealth] ({xx},1.83) -- ({xx},2.22);'+'\n'
    p+=txt(10,1.12,rule,width=8.0,size=12)
    return p

def record_example(caption,swap,stay,record):  # Problem 6: 3, 1 through the same bar twice
    p=txt(0,0,caption,size=12.5)
    p+=network(2,[(1,2),(1,2)],x=.25,y=1.6,w=13.8,gap=1.2,ins=[3,1],outs=[1,3],bar_xs=[5.1,9.6])
    p+=txt(4.3,.85,swap,width=2.5,size=11)
    p+=txt(8.8,.85,stay,width=2.5,size=11)
    p+=card(7.4,1.6,1,.85)+card(7.4,2.8,3,.85)
    p+=txt(14.8,1.5,record,width=3.7,size=12)
    return p
