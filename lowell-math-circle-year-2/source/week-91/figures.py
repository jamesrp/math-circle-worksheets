"""Week 91 (Rotor-router machines) figures and page template for the problem files.

The drawing helpers are carried over unchanged from the old student generator
(editable/student/generate.py, which still writes the return-visit packet and the
materials). Coordinates are millimetres with y downward on a US Letter page.
"""

W, H = 215.9, 279.4


def text(x,y,w,s,size=13):
 return rf'\node[anchor=north west,inner sep=0,text width={w}mm,font=\fontsize{{{size}}}{{{size*1.28}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x,y,xx,yy,style=''):
 return rf'\draw[{style}] ({x},{y}) -- ({xx},{yy});'+'\n'
def circle(x,y,r,label='',size=11):
 return rf'\draw[fill=white,line width=.6pt] ({x},{y}) circle ({r}mm);\node[font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{y}) {{{label}}};'+'\n'
def arrow(x,y,dx,dy):
 return line(x-dx/2,y-dy/2,x+dx/2,y+dy/2,'-{Latex[length=2mm]},line width=1.1pt')
def strip(x,y,n=12,sz=12,label='Arrival order'):
 s=text(x,y-8,n*sz,label,10)
 for i in range(n):
  s+=rf'\draw[gray] ({x+i*sz},{y}) rectangle ++({sz},{sz});'+'\n'
 return s

def tree(x,y,depth=2,scale=1,states=None,leaves=None):
 # compact tree bounding width 70 (d2) or 150 (d3)
 n=2**depth; gap=19*scale; width=(n-1)*gap
 levels=[]
 for level in range(depth+1):
  a=[]
  for j in range(2**level):
   xx=x+((j+.5)*n/(2**level)-.5)*gap
   a.append((xx,y+level*21*scale))
  levels.append(a)
 s=''
 for k in range(depth):
  for j,(xx,yy) in enumerate(levels[k]):
   for end in levels[k+1][j*2:j*2+2]: s+=line(xx,yy,*end)
 idx=0
 for k,coords in enumerate(levels):
  for j,(xx,yy) in enumerate(coords):
   if k==depth: s+=circle(xx,yy,4*scale,(leaves or list('ABCDEFGH'))[j],10)
   else:
    s+=circle(xx,yy,4.4*scale)
    if states and states[idx]: s+=arrow(xx,yy,(-1 if states[idx]=='L' else 1)*4*scale,4*scale)
    idx+=1
 return s


# ---------------------------------------------------------------- figures named in the problem files

def head(band):
    """The page header with its grade range, and the rule under it. Starts each page."""
    return text(15,12,W-30,rf'Week 91 / Rotor-router machines / {band}',11)+line(15,21,W-15,21,'gray')


def demo():
    """Page 1: one move at a switch, in three pictures (Input, Move to X, Flip)."""
    b=text(15,65,55,'Input',10)+text(81,65,55,'Move to X',10)+text(148,65,55,'Flip; ready again',10)
    for x,state,dot in [(31,'L','top'),(97,'L','left'),(164,'R','left')]:
        b+=line(x,86,x-12,104)+line(x,86,x+12,104)+circle(x,86,7)+arrow(x,86,-5 if state=='L' else 5,5)
        b+=text(x-17,108,12,'X',11)+text(x+9,108,12,'Y',11)
        b+=rf'\fill ({x+9 if dot=="top" else x-12},{83 if dot=="top" else 104}) circle (2mm);'
    return b+arrow(65,94,12,0)+arrow(132,94,12,0)


def targets(orders):
    """Problem 3: a target order above each four-exit tree, (order, x, y)."""
    return ''.join(text(x,y,80,order,17)+tree(x+3,y+19,2,1) for order,x,y in orders)


def eight_targets(orders, label_dy=0):
    """Problem 4: each target order beside an eight-exit tree, one every 65 mm."""
    b=''
    for i,o in enumerate(orders):
        y=65+i*65
        b+=text(15,y+label_dy,186,o,16)
        b+=tree(55,y+13,3,.75)
    return b


# ---------------------------------------------------------------- page template

def page_preamble(week, topic, header, footer):
    return r'''\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
'''


def page_open(page):
    return rf'\paperwidth={W}mm\paperheight={H}mm\pdfpagewidth={W}mm\pdfpageheight={H}mm\begin{{tikzpicture}}[remember picture,overlay,x=1mm,y=-1mm,shift={{(current page.north west)}}]'+'\n'


def page_close(page):
    # The tools put \newpage between pages; the last page ends with its own, as the old generator's did.
    footer = page.footer
    return (line(15,H-18,W-15,H-18,'gray')+text(15,H-13,W-40,rf'Bellingham Math Circle / Week 91 / {footer}',9)
            +text(W-24,H-13,10,str(page.number),9)+'\\end{tikzpicture}\\null'+('\\newpage\n' if page.number == page.count else ''))


def page_prompt(n, body, x, y, size):
    return text(x,y,186,rf'\textbf{{Problem {n}:}} {body}',size)


def page_text(x, y, body, w, size):
    return text(x,y,w,body,size)
