"""Week 41 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/make_packets.py and common.py); the October 23, 2026
card fixes renamed the worked example's panels and added the layouts at the end.

Coordinates are millimetres from the top-left corner of the paper, y down: each page
is a TikZ overlay on the whole page that draws its own header, rule, footer and page
number. Problem files call the functions below by name in their `figure` sections;
the rule and prompt wording lives in the problem files.
"""
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
def rules(y,w=180):return line(16,y,16+w,y,'gray!40')


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


# ---------------------------------------------------------------- seam pictures (common.py; no packet uses them)

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


# ---------------------------------------------------------------- portal maps and trips (make_packets.py)

LETTERS=[['A','B','C'],['D','H','E'],['F','G','I']]
def tile(x,y,s,portals=True,all_letters=True,home=True,fs=11):
 out=rf'\draw[line width=.9pt] ({x},{y}) rectangle ++({s},{s});'+'\n'
 for k in [1,2]:out+=line(x+k*s/3,y,x+k*s/3,y+s,'gray!50,line width=.4pt')+line(x,y+k*s/3,x+s,y+k*s/3,'gray!50,line width=.4pt')
 for r in range(3):
  for c in range(3):
   if all_letters or (home and r==c==1):
    out+=lab(x+(c+.5)*s/3,y+(r+.5)*s/3-4,LETTERS[r][c],fs)
    out+=rf'\fill[gray] ({x+(c+.5)*s/3},{y+(r+.5)*s/3}) circle (.55);'+'\n'
 if portals:
  for xx in [x,x+s]:
   out+=rf'\draw[fill=white,line width=.7pt] ({xx},{y+s*.18}) circle (1.7);'+'\n'
   out+=line(xx,y+s*.77,xx,y+s*.61,'-{Stealth[length=2.4mm]},line width=1.3pt')
  for yy in [y,y+s]:
   xx=x+s*.18
   out+=rf'\draw[fill=white,line width=.7pt] ({xx},{yy-1.8})--({xx+1.8},{yy})--({xx},{yy+1.8})--({xx-1.8},{yy})--cycle;'+'\n'
   out+=line(x+s*.61,yy,x+s*.77,yy,'-{Stealth[length=2.4mm]},line width=1.3pt')
 return out

def tiled(x,y,s,coords=False):
 out=''
 for r in range(3):
  for c in range(3):
   out+=tile(x+c*s,y+r*s,s,False,False,True,10 if s>40 else 8)
   if coords:out+=lab(x+(c+.5)*s,y+(r+1)*s-4,f'$({c-1},{1-r})$',9)
 out+=rf'\draw[line width=1.7pt] ({x+s},{y+s}) rectangle ++({s},{s});'+'\n'
 if not coords:out+=lab(x+1.5*s,y+1.88*s,'original',9 if s>40 else 7)
 return out

def arrtrip(x,y,w,s,size=15):return text(x,y,w,'$'+r'\;'.join({'R':r'\rightarrow','L':r'\leftarrow','U':r'\uparrow','D':r'\downarrow'}[c] for c in s)+'$',size)
def example():
 s=lab(41,62,'portal map',10)+lab(151,62,'repeated map',10)
 s+=tile(17,73,48,True,True,True,9)
 # H -> E -> D on quotient, paired with a continuous path in two copies.
 s+=line(41,97,65,97,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')+line(17,97,25,97,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')
 s+=text(73,80,29,'two steps right',10)
 s+=tile(106,73,45,False,True,True,9)+tile(151,73,45,False,True,True,9)
 s+=line(128.5,95.5,158.5,95.5,'-{Stealth[length=2mm]},blue!65!black,line width=1.1pt')
 s+=lab(128.5,125,'original copy',9)+lab(173.5,125,'next copy',9)
 return s


def slide_example(y):
 out=''
 for x,title,way in [(23,'input',0),(144,'output',1)]:
  out+=lab(x+24,y-7,title,10)+blank(x,y,48,48)
  out+=line(x+24,y,x+24,y+48,'gray!50')+line(x,y+24,x+48,y+24,'gray!50')
  # These are the lower-left four cells of the same portal map.
  for k,xx,yy in [('D',x+12,y+12),('H',x+36,y+12),('F',x+12,y+36),('G',x+36,y+36)]:
   out+=lab(xx-5,yy-5,k,11)+rf'\fill ({xx},{yy}) circle (.7);'+'\n'
  path=[(x+12,y+36),(x+36,y+36),(x+36,y+12)] if way==0 else [(x+12,y+36),(x+12,y+12),(x+36,y+12)]
  out+=rf'\draw[-{{Stealth[length=2.5mm]}},blue!65!black,line width=1.4pt] '+'--'.join(f'({a},{b})' for a,b in path)+';\n'
 out+=line(82,y+19,132,y+19,'{Stealth[length=2.5mm]}-{Stealth[length=2.5mm]},line width=.8pt')
 out+=text(82,y+25,52,'slide through the squares',10)
 return out


# ---------------------------------------------------------------- problem layouts (make_packets.py's page loops)

def predict_trips():
 """Problem 1: the portal map and four trips, each with an answer line."""
 s=tile(20,177,75,True,True,True,14)
 for j,rt in enumerate(['RRD','UU','LD','UURR']):
  s+=arrtrip(113,177+20*j,62,rt)+line(175,183+20*j,195,183+20*j,'gray')
 return s

def k1_step_maps():
 """K-1 Problem 3: four maps headed 2, 3, 4 and 5 steps."""
 s=''
 for j,n in enumerate([2,3,4,5]):
  xx=23+(j%2)*94;yy=79+(j//2)*93
  s+=lab(xx+36,yy-10,f'{n} steps',13)+tile(xx,yy,72,True,True,True,11)
 return s

def trip_list(trips,y,w,size):
 """Trips in two columns of arrows, 10 mm apart."""
 return ''.join(arrtrip(18+(j%2)*93,y+(j//2)*10,w,rt,size) for j,rt in enumerate(trips))


# ---------------------------------------------------------------- October 23, 2026 card fixes

def ruled(y0,y1,step=10,x=16,w=180):
 """Ruled lines for a running list of trips, from y0 to y1."""
 out='';y=y0
 while y<=y1+1e-6:out+=line(x,y,x+w,y,'gray!40');y+=step
 return out

def board_and_lines():
 """Grades 2-3 trips home: a 120 mm portal map with ruled lines beside and below it."""
 return tile(18,50,120,True,True,True,14)+ruled(58,168,10,148,48)+ruled(184,254,10)

def compare_three():
 """Grades 2-3: three trips from H, each on its own repeated map (25 mm copies), and an answer box."""
 s=''
 for x,y,rt in [(20,48,'RRRUUU'),(116,48,'RURURU'),(20,145,'RRRDDD')]:
  s+=arrtrip(x,y,81,rt,13)+tiled(x,y+12,25)
 return s+blank(112,157,84,75)

def _block(x,y,c=20):
 """The lower-left 2-by-2 block of the portal map (D H over F G), cells c mm; returns centres."""
 out=blank(x,y,2*c,2*c)+line(x+c,y,x+c,y+2*c,'gray!50')+line(x,y+c,x+2*c,y+c,'gray!50')
 pts={'D':(x+c/2,y+c/2),'H':(x+1.5*c,y+c/2),'F':(x+c/2,y+1.5*c),'G':(x+1.5*c,y+1.5*c)}
 for k,(a,b) in pts.items():out+=lab(a-4,b-4,k,11)+rf'\fill ({a},{b}) circle (.7);'+'\n'
 return out,pts

def _path(pts,o=(0,0)):
 return rf'\draw[-{{Stealth[length=2.5mm]}},blue!65!black,line width=1.4pt] '+'--'.join(f'({a+o[0]},{b+o[1]})' for a,b in pts)+';\n'

def move_pictures(y):
 """Grades 4-5: the two allowed changes, each a before/after pair with one line of text beside it."""
 out=''
 for row,(name,words) in enumerate([('slide','Slide: swap two sides of a square of four neighboring centers for its other two sides, in any rotation.'),
                                    ('backtrack','Backtrack: add or erase a step followed straight away by the opposite step.')]):
  yy=y+row*50
  left,p=_block(20,yy);right,q=_block(84,yy)
  out+=left+right
  if name=='slide':
   out+=_path([p['F'],p['G'],p['H']])+_path([q['F'],q['D'],q['H']])
  else:
   out+=_path([p['F'],p['G']],(0,-1.6))+_path([p['G'],p['F']],(0,1.6))+_path([p['F'],p['D']])+_path([q['F'],q['D']])
  out+=line(64,yy+20,80,yy+20,'{Stealth[length=2.5mm]}-{Stealth[length=2.5mm]},line width=.8pt')
  out+=text(128,yy+13,68,words,11)
 return out
