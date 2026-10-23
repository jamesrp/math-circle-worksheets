"""Week 37 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres with y pointing down, measured from a point 1.5 cm in
from the page's top-left corner, as the old builder drew them. Problem files call
the figure functions at the end by name; the rule and prompt wording lives in the
problem files. The header, footer and page number open each page's picture, as
before, drawn by page_open(page), so the rebuilt LaTeX is the old builder's byte
for byte. Every drawn line starts with a line break, as the old builder joined them.
"""
import math


class Page:
    """The drawing half of the old builder's Packet: text() and figure code append TikZ lines to p."""

    def __init__(self):
        self.p = []

    def text(self,x,y,w,t,s=15):self.p.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')


def draw(fn):
    """Run a drawing function on a fresh Page and return its lines, as the old builder joined them."""
    def figure(*args, **kw):
        p = Page()
        fn(p, *args, **kw)
        return ''.join('\n'+line for line in p.p)
    figure.__name__ = fn.__name__
    return figure


# ---------------------------------------------------------------- page template
# The old builder's page: Computer Modern sans, 0.5 in margins, one overlay picture
# per page that opens with the header, footer and page number.

def page_preamble(week, topic, header, footer):
    return r'''\RequirePackage{fix-cm}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,patterns}
\pdfmapfile{+cm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''


def page_open(page):
    """The old builder's Packet.page(): the nested pictures, header, footer and page number."""
    p = Page()
    p.p = [r'\null\begin{tikzpicture}[remember picture,overlay]',r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]',r'\begin{scope}[shift={(1.5,1.5)}]']
    p.text(0,-.5,18.5,f'Week {page.week} / {page.topic} / {page.header}',11)
    p.text(0,24.7,17,f'Bellingham Math Circle / Week {page.week} / {page.footer}',10)
    p.text(18,24.7,.5,str(page.number),10)
    return '\n'.join(p.p)


def page_close(page):
    return r'\end{scope}\end{scope}\end{tikzpicture}'+'\n'


def page_prompt(n, body, x, y, size):
    """The old builder's problem(): label and statement in one node; 17 pt for K-1, 15 pt otherwise (week.toml)."""
    p = Page()
    p.text(0,.5 if y is None else y,18.4,r'\textbf{Problem '+str(n)+':} '+body,size)
    return '\n'+p.p[0]


def page_text(x, y, body, w, size):
    p = Page()
    p.text(x or 0,y or 0,w or 18.4,body,size or 15)
    return '\n'+p.p[0]


# ---------------------------------------------------------------- drawing code (unchanged)

COL={'A':'blue!12','B':'orange!22','C':'green!18','D':'violet!20','':'white'}
def badge(p,x,y,lab,s=.46):
 # Letters, in addition to distinct tints, identify all markers in grayscale.
 p.p.append(f'\\node[circle,draw,line width=.9pt,fill={COL.get(lab,"white")},minimum size={2*s}cm,inner sep=0,font=\\sffamily\\bfseries\\fontsize{{15}}{{17}}\\selectfont] at ({x},{y}) {{{lab}}};')
def tetra(p,x,y,labels=('A','B','C','D'),s=1):
 # Exact orthographic projection of a regular tetrahedron.
 # World A=(0,0,sqrt(2/3)), B=(-1/2,-sqrt(3)/6,0),
 # C=(1/2,-sqrt(3)/6,0), D=(0,sqrt(3)/3,0).
 # Horizontal = X; vertical = -Z - 0.55 Y (up to an overall scale).
 L=5*s; q=math.sqrt(1+.55**2)
 coords=[(x,y-L*math.sqrt(2/3)/q),(x-L*.5,y+L*.55*math.sqrt(3)/(6*q)),(x+L*.5,y+L*.55*math.sqrt(3)/(6*q)),(x,y-L*.55*math.sqrt(3)/(3*q))]
 for i,j in [(0,3),(1,3),(2,3)]:
  a,b=coords[i],coords[j];p.p.append(f'\\draw[dashed,line width=.9pt,gray!75] ({a[0]},{a[1]}) -- ({b[0]},{b[1]});')
 for i,j in [(0,1),(0,2),(1,2)]:
  a,b=coords[i],coords[j];p.p.append(f'\\draw[line width=1.15pt] ({a[0]},{a[1]}) -- ({b[0]},{b[1]});')
 for (xx,yy),l in zip(coords,labels):badge(p,xx,yy,l,.45 if s>=.8 else .34)
 return coords

def pair(p,y=9,left=('A','B','C','D'),right=('A','C','B','D'),mirror=True,s=1.1):
 tetra(p,4.3,y,left,s);tetra(p,14.1,y,right,s)
 if mirror:
  p.p.append(f'\\draw[gray!55,line width=2pt] (9.2,{y-5.4*s}) -- (9.2,{y+1.2*s});')
  p.text(8.45,y+1.6*s,2,'mirror',11)

def turn_demo(p):
 tetra(p,4.0,8.15,('A','B','C','D'),1.03);tetra(p,14.4,8.15,('A','D','B','C'),1.03)
 p.p.append(r'\draw[-{Stealth},line width=1pt] (7.4,6.1) to[bend left=25] (11,6.1);')
 p.text(7.35,6.7,3.9,'turn around A',12)
 p.text(1.3,10,5.5,'before the turn',12);p.text(11.7,10,5.8,'after the turn',12)

def topview(p,x,y,labels=('B','C','D'),s=1):
 # As seen from A toward the opposite face: B left, C right, D far/top.
 vs=[(x-2.3*s,y+1.3*s),(x+2.3*s,y+1.3*s),(x,y-2.6*s)]
 for i in range(3):
  u,v=vs[i],vs[(i+1)%3];p.p.append(f'\\draw[line width=1pt] ({u[0]},{u[1]}) -- ({v[0]},{v[1]});')
 for u in vs:p.p.append(f'\\draw[gray!55,line width=.6pt] ({x},{y}) -- ({u[0]},{u[1]});')
 for u,lab in zip(vs,labels):badge(p,*u,lab,.43)
 badge(p,x,y,'A',.4)
 p.text(x-1.6,y+2.1*s,3.7,'A nearest you',11)

def lines(p,ys):
 for y in ys:p.p.append(f'\\draw[gray!40] (0,{y}) -- (18.3,{y});')


# ---------------------------------------------------------------- figures
# Each draws what followed a rule or problem statement on its page.

@draw
def turn_example(p):  # the rules: a successful turn, before and after
 turn_demo(p)

@draw
def two_models(p):  # Problem 1 in every band
 tetra(p,4.3,21.1,('A','B','C','D'),1);tetra(p,14.1,21.1,('A','B','C','D'),1)

@draw
def mirror_pair(p,ruled=()):  # the A, B, C, D mirror pair
 pair(p,10.5)
 if ruled:lines(p,ruled)

@draw
def view_from_a(p):  # grades 4-5: the model, its view from A, and two blank views
 tetra(p,4.1,10.1,('A','B','C','D'),1.05);topview(p,14.4,8.2)
 p.p.append(r'\draw[-{Stealth},line width=1pt] (7.1,8.2) -- (11.1,8.2);')
 p.text(6.8,9.0,4.7,r'look from A\\toward face BCD',12)
 p.text(1.5,12.2,5.8,'model',12);p.text(11.8,12.2,5.5,'view from A',12)
 topview(p,4.4,18.5,('','',''),.75);topview(p,14.1,18.5,('','',''),.75)
 lines(p,[23.4])

@draw
def equal_letter_pair(p,ruled=()):  # the mirror pair with D changed to C
 pair(p,10.5,('A','B','C','C'),('A','C','B','C'),False)
 if ruled:lines(p,ruled)

@draw
def repeated_a_pair(p):  # A, A, B, C on each model
 pair(p,10.5,('A','A','B','C'),('A','B','A','C'),False)

@draw
def bare_frame(p):  # grades 4-5: an unlabelled tetrahedron
 tetra(p,9.2,11,('','','',''),1.35)

@draw
def answer_lines(p,ys):  # ruled lines across the page
 lines(p,ys)
