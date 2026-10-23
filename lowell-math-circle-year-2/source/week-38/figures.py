"""Week 38 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py and examples.py).

Coordinates are millimetres from the top-left corner of the paper, y down: each page
is a TikZ overlay on the whole page that draws its own header, rule, footer and page
number. Problem files call the functions below by name in their `figure` sections;
the rule and prompt wording lives in the problem files.
"""


# ---------------------------------------------------------------- drawing primitives (make_packets.py)

def text(x,y,w,s,size=13):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,align=left,font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def lab(x,y,s,size=11,anchor='center'):
    s=s.replace('_',r'\_')
    return rf'\node[anchor={anchor},inner sep=1pt,font=\fontsize{{{size}}}{{{size*1.2}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x1,y1,x2,y2,opts=''):
    return rf'\draw[{opts}] ({x1},{y1})--({x2},{y2});'+'\n'
def blank(x,y,w,h):
    return rf'\draw[gray!45,line width=.3pt] ({x},{y}) rectangle ++({w},{h});'+'\n'


# ---------------------------------------------------------------- page template (make_packets.py's page and write)

def page_preamble(week, topic, header, footer):
    return r'''\documentclass[letterpaper]{article}
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


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay,shift={(current page.north west)},x=1mm,y=-1mm,line cap=round,line join=round]'+'\n'
            + text(16,11,182,rf'Week {page.week} / {page.topic} / {page.header}',10.5)+line(16,19,200,19,'gray!55'))


def page_close(page):
    return text(16,266,174,rf'Bellingham Math Circle / Week {page.week} / {page.footer}',9)+lab(198,268,str(page.number),9)+r'\end{tikzpicture}'+'\n'


def page_prompt(n, body, x, y, size):
    return text(16,y,180,rf'\textbf{{Problem {n}:}} {body}',size)


def page_text(x, y, body, w, size):
    return text(x,y,w,body,size)


# ---------------------------------------------------------------- drawing code (make_packets.py, unchanged)

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

def choices(y,left='A',right='B',gap=29):
    s=''
    for i,parts in enumerate([(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]):
        yy=y+i*gap
        s+=dot_groups(23,yy,parts)+lab(153,yy,left+': ___',11)+lab(184,yy,right+': ___',11)
    return s

def moving_arrow(y):
    s=line(25,y,178,y)+line(25,y+28,178,y+28)+line(25,y+14,178,y+14,'dashed,gray')
    s+=line(56,y+5,56,y+23,'-{Stealth[length=3mm]},line width=1.4pt')
    s+=line(142,y+5,142,y+23,'-{Stealth[length=3mm]},line width=1.4pt')
    s+=line(73,y+14,125,y+14,'-{Stealth[length=2mm]},line width=.8pt')
    s+=lab(56,y+35,'start marker',10)+lab(142,y+35,'after a short slide',10)
    return s


# ---------------------------------------------------------------- the washer example (examples.py)

def washer_example():
    # examples.py's edge_groups_example without its two sentences, which are text sections in the problem files.
    s=lab(58,82,'flat paper washer',11)+lab(153,82,'dot groups',11)
    s+=r'\fill[gray!10] (58,121) circle (29);\fill[white] (58,121) circle (13);'+'\n'
    s+=r'\draw[line width=1.2pt] (58,121) circle (29);\draw[dashed,line width=1.2pt] (58,121) circle (13);'+'\n'
    s+=r'\draw[-{Stealth[length=2.2mm]},line width=1.2pt] (58,92) arc[start angle=-90,end angle=0,radius=29];'+'\n'
    s+=r'\draw[dashed,-{Stealth[length=2.2mm]},line width=1.2pt] (58,108) arc[start angle=-90,end angle=-180,radius=13];'+'\n'
    for x,y,ch,lx,ly in ((58,92,'P',58,87),(87,121,'Q',94,121),(58,134,'R',58,126)):
        s+=fr'\fill ({x},{y}) circle (1.5);'+'\n'+lab(lx,ly,ch,11)
    s+=line(102,121,121,121,'-{Stealth[length=2.6mm]},line width=.9pt')
    s+=r'\draw[line width=.7pt] (153,108) ellipse (25 and 12);\draw[line width=.7pt] (153,143) ellipse (16 and 12);'+'\n'
    for x,y,ch in ((145,110,'P'),(161,110,'Q'),(153,146,'R')):
        s+=fr'\fill ({x},{y}) circle (1.5);'+'\n'+lab(x,y-6,ch,11)
    s+=line(27,164,44,164,'line width=1.2pt')+lab(57,164,'outer trip',10)
    s+=line(94,164,111,164,'dashed,line width=1.2pt')+lab(124,164,'inner trip',10)
    return s


# ---------------------------------------------------------------- added October 23, 2026 (v4)

def shifted(dy, tikz):
    """Draw the TikZ of a figure dy mm lower on the page (negative: higher)."""
    return r'\begin{scope}[shift={(0,'+str(dy)+r')}]'+'\n'+tikz+r'\end{scope}'+'\n'

def choices_one(y,label,gap=29):
    """The five four-dot pictures with one blank each."""
    s=''
    for i,parts in enumerate([(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]):
        yy=y+i*gap
        s+=dot_groups(23,yy,parts)+lab(168,yy,label+': ___',11)
    return s

def strip_thirds(x,y,w,h,name=None):
    """A B recipe (reversed right end) with the two one-third lines dotted instead of the middle line."""
    s=rf'\draw[line width=1pt] ({x},{y}) rectangle ++({w},{h});'+'\n'
    s+=line(x+3,y+h/3,x+w-3,y+h/3,'dotted,line width=1pt')+line(x+3,y+2*h/3,x+w-3,y+2*h/3,'dotted,line width=1pt')
    for xx,r in [(x+4,False),(x+w-4,True)]:
        s+=mark(xx,y+(h-5 if r else 5),'dot')+mark(xx,y+(5 if r else h-5),'sq')
        ax=xx+(5 if xx==x+4 else -5)
        s+=line(ax,y+(7 if r else h-7),ax,y+(h-7 if r else 7),'-{Stealth[length=2mm]},line width=.7pt')
    if name:s+=lab(x-6,y+h/2,name,13)
    return s
