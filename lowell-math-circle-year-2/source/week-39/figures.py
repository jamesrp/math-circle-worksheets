"""Week 39 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py and common.py).

Coordinates are millimetres from the top-left corner of the paper, y down: each page
is a TikZ overlay on the whole page that draws its own header, rule, footer and page
number. Problem files call the functions below by name in their `figure` sections;
the rule and prompt wording lives in the problem files.
"""


# ---------------------------------------------------------------- drawing primitives (common.py)

def text(x,y,w,s,size=13):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,align=left,font=\fontsize{{{size}}}{{{size*1.25}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def lab(x,y,s,size=11,anchor='center'):
    s=s.replace('_',r'\_')
    return rf'\node[anchor={anchor},inner sep=1pt,font=\fontsize{{{size}}}{{{size*1.2}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x1,y1,x2,y2,opts=''):
    return rf'\draw[{opts}] ({x1},{y1})--({x2},{y2});'+'\n'
def blank(x,y,w,h):
    return rf'\draw[gray!45,line width=.3pt] ({x},{y}) rectangle ++({w},{h});'+'\n'


# ---------------------------------------------------------------- page template (common.py's page and write)

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


# ---------------------------------------------------------------- maps (make_packets.py)

TREE={'A':(0,1),'B':(1,1),'C':(1,0),'D':(2,1),'E':(3,0),'F':(3,2)}
TEDGES=['AB','BC','BD','DE','DF']
RING={'A':(0,1),'B':(1,0),'C':(2,1),'D':(1,2)}
REDGES=['AB','BC','CD','DA']
EIGHT={'H':(2,1),'A':(0,0),'B':(0,2),'C':(4,0),'D':(4,2)}
EEDGES=['HA','AB','BH','HC','CD','DH']
COLORS={'A':'red!65!black','B':'blue!70!black','C':'yellow!80!black','D':'green!55!black','E':'orange','F':'violet','H':'black'}
def graph(x,y,sc,nodes,edges,labels=True):
 s=''
 for e in edges:
  a,b=nodes[e[0]],nodes[e[1]]
  s+=line(x+a[0]*sc,y+a[1]*sc,x+b[0]*sc,y+b[1]*sc,'line width=3mm,gray!25')
  s+=line(x+a[0]*sc,y+a[1]*sc,x+b[0]*sc,y+b[1]*sc,'line width=.7pt')
 for k,(a,b) in nodes.items():
  s+=rf'\draw[fill={COLORS[k]}!20,line width=.7pt] ({x+a*sc},{y+b*sc}) circle (3.5);'+'\n'
  if labels:s+=lab(x+a*sc,y+b*sc,k,12)
 return s


# ---------------------------------------------------------------- the worked example under the rules (problems/00-rules.md)

def step_card(x,y,a,b,removed=False):
    nd={'A':(0,1),'B':(1,1),'C':(1,0),'D':(2,1)}
    s=blank(x,y,31,26)
    for e in ['AB','BC','BD']:
        u,v=nd[e[0]],nd[e[1]]
        s+=line(x+5+u[0]*10,y+7+u[1]*10,x+5+v[0]*10,y+7+v[1]*10,'gray!40,line width=1mm')
    u,v=nd[a],nd[b]
    # Draw the step direction in place on a miniature copy of the same map.
    s+=line(x+5+u[0]*10,y+7+u[1]*10,x+5+v[0]*10,y+7+v[1]*10,'-{Stealth[length=2.3mm]},line width=1pt')
    for k,(xx,yy) in nd.items():
        s+=rf'\fill[{COLORS[k]}] ({x+5+xx*10},{y+7+yy*10}) circle (1.2);'+'\n'
        s+=lab(x+5+xx*10,y+3+yy*10,k,7)
    if removed:s+=line(x+2,y+24,x+29,y+2,'gray,line width=.7pt')
    return s

def demo(y):
    s=lab(21,y+13,'input',9,anchor='east')
    for i,(a,b) in enumerate(zip('ABCB','BCBD')):s+=step_card(25+38*i,y,a,b)
    s+=lab(173,y+13,r'$A\to B\to C\to B\to D$',9,anchor='west')
    s+=lab(21,y+47,'remove',9,anchor='east')
    for i,(a,b) in enumerate(zip('ABCB','BCBD')):s+=step_card(25+38*i,y+34,a,b,i in (1,2))
    s+=lab(21,y+81,'output',9,anchor='east')
    for i,(a,b) in enumerate([('A','B'),('B','D')]):s+=step_card(25+38*i,y+68,a,b)
    s+=lab(98,y+81,r'$A\to B\to D$',9,anchor='west')
    s+=text(130,y+74,66,'No steps left means the pawn stays at its start.',10)
    return s


# ---------------------------------------------------------------- recorded routes (grades 2-3 and 4-5)

def routes(y,rs,size=13):
 s=''
 for i,r in enumerate(rs):
  yy=y+i*21
  s+=text(19,yy,175,r'$'+r'\to '.join(r)+r'$'+r'\hfill $\longrightarrow$ \rule{48mm}{.3pt}',size)
 return s

def routes_with_answers(y,rs):
 """Problem 1, grades 2-3 and 4-5: each recorded route with an answer line under it, left of
 the map, then two lines for the new seven-step trip (card fix 8, October 23, 2026)."""
 s=''
 for i,r in enumerate(rs):
  yy=y+i*20
  s+=text(19,yy,92,r'$'+r'\to '.join(r)+r'$',13)
  s+=text(19,yy+8,92,r'$\longrightarrow$ \rule{70mm}{.3pt}',13)
 for k in range(2):s+=line(19,y+70+k*11,110,y+70+k*11,'gray!60,line width=.3pt')
 return s

def routes_beside_map(y,rs):
 """Problem 1, grades 2-3 and 4-5: short route strings recorded to the left of the map,
 as the old builder's replace() on that page made them."""
 return routes(y,rs).replace('text width=175mm','text width=90mm').replace(r'\hfill $\longrightarrow$ \rule{48mm}{.3pt}',r' $\longrightarrow$')
