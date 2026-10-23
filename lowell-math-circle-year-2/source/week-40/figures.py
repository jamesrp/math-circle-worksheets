"""Week 40 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py and common.py) and the trefoil
geometry of editable/src/knot_geometry.py. The October 23, 2026 card fixes (v3) added
the figure-eight, the curl and the slide, the end-color table, and moved or renamed
parts of the page-1 example and the end dots (R became S).

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
\hyphenpenalty=10000
\exhyphenpenalty=10000
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

def arc_demo(y1=52,y2=88,ty=67):
 s=''
 for yy,output in [(y1,False),(y2,True)]:
  # A whole X arc begins after the left underpass, passes over the middle,
  # and ends before the right underpass.
  s+=rope([(32,yy),(40,yy)])+rope([(50,yy),(160,yy)])+rope([(170,yy),(186,yy)])
  # Middle horizontal is over; vertical below has a six-mm gap.
  s+=rope([(105,yy-12),(105,yy-5)])+rope([(105,yy+5),(105,yy+12)])
  for x in [45,165]:s+=rope([(x,yy-12),(x,yy+12)])
  s+=lab(54,yy-6,'X',12)
  if output:
   s+=cord_path([(51,yy),(159,yy)],'blue!65!black',1.6)
   s+=lab(57,yy+7,'start',9)+lab(153,yy+7,'stop',9)
 s+=text(16,ty,181,'Follow X across the overpass to the next gap.',11)
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
 # Fixed four endpoints: L,S at horizontal height; P,Q at top.
 s=''
 if before:
  s+=rope([(x,y+32),(x+18,y+32)])+rope([(x+28,y+32),(x+45,y+32)])+rope([(x+55,y+32),(x+74,y+32)])
  s+=rope([(x+23,y),(x+23,y+48),(x+50,y+48),(x+50,y)])
 else:
  s+=rope([(x,y+32),(x+74,y+32)])+rope([(x+23,y),(x+23,y+17),(x+50,y+17),(x+50,y)])
 for a,xx,yy in [('L',x,y+32),('S',x+74,y+32),('P',x+23,y),('Q',x+50,y)]:
  s+=rf'\fill ({xx},{yy}) circle (1);'+'\n'
  s+=lab(xx+( -5 if a=='L' else 5 if a=='S' else 0),yy+( -5 if a in 'PQ' else 0),a,10)
 return s


# ---------------------------------------------------------------- page figures (make_packets.py's per-page drawing)

def valid_crossings(y=207):
 return crossing(46,y,'R','R','R','valid')+crossing(106,y,'R','B','G','valid')+crossing(166,y,'R','R','B','invalid')

def missing_colours():
 s=''
 for i,(a,over) in enumerate(itertools.product('RBG',repeat=2)):
  s+=crossing(46+60*(i%3),92+66*(i//3),a,over,None)
 return s

def move_pictures(title_y,top=85):
 return lab(61,title_y,'before',11)+lab(154,title_y,'after',11)+rtwo(22,top,True)+rtwo(118,top,False)

def move_arrow(y=121):
 return line(98,y,112,y,'-{Stealth[length=3mm]},line width=1pt')

def end_cases(top=172):
 cases=[('R','B','R','B'),('R','R','B','R'),('G','B','G','B'),('B','G','B','R'),('B','B','B','B'),('R','G','R','G')]
 s=''
 for i,case in enumerate(cases):
  xx=23+90*(i%2); yy=top+29*(i//2)
  s+=lab(xx-9,yy,str(i+1),12)
  for j,(name,val) in enumerate(zip('LPSQ',case)):
   s+=lab(xx+17*j,yy-6,name,9)
   s+=rf'\draw[fill={COL[val]},line width=.5pt] ({xx+17*j},{yy}) circle (3.4);'+'\n'
   s+=lab(xx+17*j,yy+7,val,8)
 return s


# ---------------------------------------------------------------- added October 23, 2026 (card fixes, v3)

def _gap_cut(path, cuts, gap):
 """Split a polyline at the given point indices, leaving gap mm free on each side."""
 cum=[0.0]
 for a,b in zip(path,path[1:]):cum.append(cum[-1]+math.dist(a,b))
 L=cum[-1]
 marks=sorted(cum[i] for i in cuts)
 pieces=[];start=0.0
 for m in marks+[None]:
  stop=L if m is None else m-gap
  if stop>start:pieces.append([p for p,c in zip(path,cum) if start<=c<=stop])
  if m is not None:start=m+gap
 return [q for q in pieces if len(q)>1]


# The figure-eight knot drawn from the plane curve
# (cos t - 1.5 cos 3t + 0.5 sin 2t, sin t + 0.5 sin 2t - 1.5 sin 3t), whose shadow has four
# crossings (all at about 58 degrees or more: 57.9, 58.3, 73.6 and 88.9). Each crossing is made over or under by meeting them
# over-under-over-under along the curve, so the diagram is alternating; the review script
# checks 3 three-colorings and 25 five-colorings (determinant 5).
def _f8(t):return (math.cos(t)-1.5*math.cos(3*t)+0.5*math.sin(2*t),math.sin(t)+0.5*math.sin(2*t)-1.5*math.sin(3*t))
_F8N=2400
_f8pts=[_f8(TAU*i/_F8N) for i in range(_F8N+1)]
_f8x=[]
for _i in range(_F8N):
 _a=_f8pts[_i];_v=_sub(_f8pts[_i+1],_a)
 for _j in range(_i+2,_F8N):
  if _i==0 and _j==_F8N-1:continue
  _b=_f8pts[_j];_w=_sub(_f8pts[_j+1],_b);_den=_cross(_v,_w)
  if abs(_den)<1e-14:continue
  _d=_sub(_b,_a);_u=_cross(_d,_w)/_den;_q=_cross(_d,_v)/_den
  if 0<=_u<1 and 0<=_q<1:
   _f8x.append((TAU*(_i+_u)/_F8N,TAU*(_j+_q)/_F8N))
assert len(_f8x)==4,_f8x
_f8ev=sorted(t for x in _f8x for t in x)
f8_under=_f8ev[1::2]
f8_crossings=[{'t_over':a if b in f8_under else b,'t_under':b if b in f8_under else a} for a,b in _f8x]
assert all((c['t_over'] in f8_under)!=(c['t_under'] in f8_under) for c in f8_crossings)
F8_W=max(p[0] for p in _f8pts)-min(p[0] for p in _f8pts)
F8_H=max(p[1] for p in _f8pts)-min(p[1] for p in _f8pts)

def figure8(top,width=148,labels=False,cx=106,gap=5.8):
 """The figure-eight knot drawn as cord, width mm wide, its top edge at y=top."""
 sc=width/F8_W
 cy=top-min(p[1] for p in _f8pts)*sc
 pts=[(cx+sc*x,cy+sc*y) for x,y in _f8pts]
 s=''
 for i,a in enumerate(f8_under):
  b=f8_under[(i+1)%4]
  if b<a:b+=TAU
  ts=[a+(b-a)*j/400 for j in range(401)]
  p=[(cx+sc*_f8(t)[0],cy+sc*_f8(t)[1]) for t in ts]
  cum=[0.0]
  for u,v in zip(p,p[1:]):cum.append(cum[-1]+math.dist(u,v))
  p=[q for q,c in zip(p,cum) if gap<=c<=cum[-1]-gap]
  s+=rope(p)
  if labels:
   # the label sits 6.5 mm off the middle of the arc, on the side farther from the rest of the cord
   m=p[len(p)//2];d=_sub(p[len(p)//2+1],p[len(p)//2-1]);n=math.hypot(*d);nx,ny=-d[1]/n,d[0]/n
   best=max(((m[0]+k*6.5*nx,m[1]+k*6.5*ny) for k in (1,-1)),key=lambda q:min(math.dist(q,r) for r in pts))
   s+=lab(best[0],best[1],'1234'[i],13)
 return s

def records4(y,rows=2,per_row=3):
 s=''
 for row in range(rows):
  for col in range(per_row):
   x=30+60*col; yy=y+12*row
   for k in range(4):
    s+=rf'\draw[gray,line width=.4pt] ({x+9*k},{yy}) circle (3.3);'+'\n'
    s+=lab(x+9*k,yy-5,str(k+1),7)
 return s

def lp_table(y,x=56,row=5.5,cols=('L','P','middle','S','Q'),widths=(18,18,28,18,18)):
 """A nine-row table with a header row, for every choice at L and P."""
 s='';xx=x
 w=sum(widths)
 for k in range(11):
  s+=line(x,y+row*k,x+w,y+row*k,'gray!70,line width=.4pt' if k else 'line width=.6pt')
 for c,wd in zip(cols,widths):
  s+=line(xx,y,xx,y+10*row,'gray!70,line width=.4pt')
  s+=lab(xx+wd/2,y+row/2,c,10)
  xx+=wd
 s+=line(xx,y,xx,y+10*row,'gray!70,line width=.4pt')
 return s

def _dot(x,y,name,dx,dy):
 return rf'\fill ({x},{y}) circle (1);'+'\n'+lab(x+dx,y+dy,name,10)

def curl(x,y,before=True):
 """Type I: one strand between end dots J and K, with a curl (before) or straight (after).
 The picture is 70 mm wide; the end dots are at height y+44."""
 a=2.0;sc=70/(2*math.pi)
 ends=[(x,y+44),(x+70,y+44)]
 if not before:
  s=rope([ends[0],ends[1]])
 else:
  us=[-math.pi+2*math.pi*j/600 for j in range(601)]
  # a prolate cycloid: from (x, y+44) up round the loop and back down to (x+70, y+44)
  path=[(x+35+sc*(u-a*math.sin(u)),y+44-sc*a*(math.cos(u)+1)) for u in us]
  # the first pass is under: cut it where the second pass crosses it
  ux=1.8955
  i_under=min(range(len(us)),key=lambda j:abs(us[j]+ux))
  s=''.join(rope(q) for q in _gap_cut(path,[i_under],4.6))
 s+=_dot(*ends[0],'J',-5,0)+_dot(*ends[1],'K',5,0)
 return s

def slide(x,y,before=True):
 """Type III: a strand from U to Y over both diagonals T-Z and V-X, passing below the
 diagonals' crossing (before) or above it (after). 70 mm wide, 50 mm tall."""
 T,V,X,Z=(x,y),(x,y+50),(x+70,y),(x+70,y+50)
 U,Y=(x,y+25),(x+70,y+25)
 sg=1 if before else -1
 mv=[(x+70*j/200,y+25+sg*19*math.sin(math.pi*j/200)) for j in range(201)]
 def hits(seg):
  # index along seg nearest the moving strand
  best=None
  for i,(px,py) in enumerate(seg):
   d=min(math.dist((px,py),q) for q in mv)
   if best is None or d<best[0]:best=(d,i)
  return best[1]
 d1=[(T[0]+70*j/200,T[1]+50*j/200) for j in range(201)]
 d2=[(V[0]+70*j/200,V[1]-50*j/200) for j in range(201)]
 # the diagonals pass under the moving strand, and V-X under T-Z at their crossing (index 100)
 s=''.join(rope(q) for q in _gap_cut(d1,[hits(d1)],4.6))+''.join(rope(q) for q in _gap_cut(d2,[hits(d2),100],4.6))+rope(mv)
 for (px,py),n,dx in [(T,'T',-5),(U,'U',-5),(V,'V',-5),(X,'X',5),(Y,'Y',5),(Z,'Z',5)]:
  s+=_dot(px,py,n,dx,0)
 return s

def moves_page(title_y=50):
 s=lab(61,title_y,'before',11)+lab(157,title_y,'after',11)+move_arrow(title_y)
 s+=lab(109,92,'curl',10)+curl(26,62,True)+curl(122,62,False)
 s+=lab(109,132,'slide',10)+slide(26,120,True)+slide(122,120,False)
 return s

def cord_choices(y):
 s=''
 for i,c in enumerate('ABCD'):
  x=30+45*i
  s+=lab(x,y,c,14)+lab(x+13,y,'yes',12)+lab(x+27,y,'no',12)
 return s
