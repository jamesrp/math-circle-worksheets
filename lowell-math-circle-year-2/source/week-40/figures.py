"""Week 40 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py and common.py) and the trefoil
geometry of editable/src/knot_geometry.py.

Coordinates are millimetres from the top-left corner of the paper, y down: each page
is a TikZ overlay on the whole page that draws its own header, rule, footer and page
number. Problem files call the functions below by name in their `figure` sections;
the rule and prompt wording lives in the problem files.
"""
import itertools
import math


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


# ---------------------------------------------------------------- trefoil geometry (knot_geometry.py, unchanged)

TAU=2*math.pi
N=1200
pts=[(math.sin(t)+2*math.sin(2*t),math.cos(t)-2*math.cos(2*t)) for t in [TAU*i/N for i in range(N+1)]]
def _cross(a,b):return a[0]*b[1]-a[1]*b[0]
def _sub(a,b):return a[0]-b[0],a[1]-b[1]
_xs=[]
for _i in range(N):
 _a=pts[_i];_v=_sub(pts[_i+1],_a)
 for _j in range(_i+3,N):
  if _i==0 and _j>=N-2:continue
  _b=pts[_j];_w=_sub(pts[_j+1],_b);_den=_cross(_v,_w)
  if abs(_den)<1e-12:continue
  _d=_sub(_b,_a);_u=_cross(_d,_w)/_den;_q=_cross(_d,_v)/_den
  if 0<=_u<1 and 0<=_q<1:
   _t1=TAU*(_i+_u)/N;_t2=TAU*(_j+_q)/N
   _z1=-math.sin(3*_t1);_z2=-math.sin(3*_t2)
   _xs.append({'t_under':_t1 if _z1<_z2 else _t2,'t_over':_t2 if _z1<_z2 else _t1})
assert len(_xs)==3,_xs
under=sorted(x['t_under'] for x in _xs)
S=148/(max(x[0] for x in pts)-min(x[0] for x in pts))


# ---------------------------------------------------------------- drawing code (make_packets.py, unchanged)

COL={'R':'red!75!black','B':'blue!70!black','G':'green!45!black'}
def cord_path(coords,color='black',thick=1.5):
 co='--'.join(f'({a:.3f},{b:.3f})' for a,b in coords)
 return rf'\draw[{color},line width={thick}mm] {co};'+'\n'
def rope(coords):
 return cord_path(coords,'black',3.2)+cord_path(coords,'white',2.4)
def trefoil(top,labels=True):
 cy=top-min(y for x,y in pts)*S;cx=106
 s=''
 for i,a in enumerate(under):
  b=under[(i+1)%3]
  if b<a:b+=TAU
  ts=[a+.045+(b-a-.090)*j/280 for j in range(281)]
  p=[(cx+S*(math.sin(t)+2*math.sin(2*t)),cy+S*(math.cos(t)-2*math.cos(2*t))) for t in ts]
  s+=rope(p)
  if labels:
   t=(a+b)/2
   xx=math.sin(t)+2*math.sin(2*t);yy=math.cos(t)-2*math.cos(2*t)
   norm=math.hypot(xx,yy)
   s+=lab(cx+S*xx+8*xx/norm,cy+S*yy+8*yy/norm,'123'[i],13)
 return s

def arc_demo():
 s=lab(22,63,'input',10,anchor='west')
 for yy,output in [(77,False),(132,True)]:
  # A whole X arc begins after the left underpass, passes over the middle,
  # and ends before the right underpass.
  s+=rope([(32,yy),(40,yy)])+rope([(50,yy),(160,yy)])+rope([(170,yy),(186,yy)])
  # Middle horizontal is over; vertical below has a six-mm gap.
  s+=rope([(105,yy-12),(105,yy-5)])+rope([(105,yy+5),(105,yy+12)])
  for x in [45,165]:s+=rope([(x,yy-12),(x,yy+12)])
  s+=lab(54,yy-6,'X',12)
  if output:
   s+=cord_path([(51,yy),(159,yy)],'blue!65!black',1.6)
   s+=lab(49,yy+8,'start',9)+lab(161,yy+8,'stop',9)
 s+=text(16,98,181,'process: follow X across the overpass to the next gap.',11)
 s+=lab(22,118,'output',10,anchor='west')
 return s


def crossing(x,y,a,b,c,title=None):
 segments=[[(x-16,y),(x-5,y)],[(x,y-13),(x,y+13)],[(x+5,y),(x+16,y)]]
 s=''
 for coords,val in zip(segments,[a,b,c]):
  s+=rope(coords)
  if val in COL:s+=cord_path(coords,COL[val],1.7)
 for val,xx,yy in [(a,x-20,y),(b,x,y-18),(c,x+20,y)]:s+=lab(xx,yy,val if val else '?',12)
 if title:s+=lab(x,y+20,title,10)
 return s

def records(y):
 s=''
 for row in range(3):
  for col in range(4):
   x=25+45*col; yy=y+11*row
   for k in range(3):
    s+=rf'\draw[gray,line width=.4pt] ({x+9*k},{yy}) circle (3.3);'+'\n'
    s+=lab(x+9*k,yy-5,str(k+1),7)
 return s

def loop(top):return rf'\draw[black,line width=3.2mm] (106,{top+64}) ellipse (74 and 57);\draw[white,line width=2.4mm] (106,{top+64}) ellipse (74 and 57);'+'\n'
def rtwo(x,y,before=True):
 # Fixed four endpoints: L,R at horizontal height; P,Q at top.
 s=''
 if before:
  s+=rope([(x,y+32),(x+18,y+32)])+rope([(x+28,y+32),(x+45,y+32)])+rope([(x+55,y+32),(x+74,y+32)])
  s+=rope([(x+23,y),(x+23,y+48),(x+50,y+48),(x+50,y)])
 else:
  s+=rope([(x,y+32),(x+74,y+32)])+rope([(x+23,y),(x+23,y+17),(x+50,y+17),(x+50,y)])
 for a,xx,yy in [('L',x,y+32),('R',x+74,y+32),('P',x+23,y),('Q',x+50,y)]:
  s+=rf'\fill ({xx},{yy}) circle (1);'+'\n'
  s+=lab(xx+( -5 if a=='L' else 5 if a=='R' else 0),yy+( -5 if a in 'PQ' else 0),a,10)
 return s


# ---------------------------------------------------------------- page figures (make_packets.py's per-page drawing)

def valid_crossings():
 return crossing(46,207,'R','R','R','valid')+crossing(106,207,'R','B','G','valid')+crossing(166,207,'R','R','B','invalid')

def missing_colours():
 s=''
 for i,(a,over) in enumerate(itertools.product('RBG',repeat=2)):
  s+=crossing(46+60*(i%3),92+66*(i//3),a,over,None)
 return s

def move_pictures(title_y):
 return lab(61,title_y,'before',11)+lab(154,title_y,'after',11)+rtwo(22,85,True)+rtwo(118,85,False)

def move_arrow():
 return line(98,121,112,121,'-{Stealth[length=3mm]},line width=1pt')

def end_cases():
 cases=[('R','B','R','B'),('R','R','B','R'),('G','B','G','B'),('B','G','B','R'),('B','B','B','B'),('R','G','R','G')]
 s=''
 for i,case in enumerate(cases):
  xx=23+90*(i%2); yy=172+29*(i//2)
  for j,(name,val) in enumerate(zip('LP RQ'.replace(' ',''),case)):
   s+=lab(xx+17*j,yy-6,name,9)
   s+=rf'\draw[fill={COL[val]},line width=.5pt] ({xx+17*j},{yy}) circle (3.4);'+'\n'
   s+=lab(xx+17*j,yy+7,val,8)
 return s
