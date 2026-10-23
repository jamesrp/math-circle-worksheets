"""Week 36 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres with y pointing down, measured from a point 1.5 cm in
from the page's top-left corner, as the old builder drew them. Problem files call
the figure functions at the end by name; the rule and prompt wording lives in the
problem files. The header, footer and page number open each page's picture, as
before, drawn by page_open(page), so the rebuilt LaTeX is the old builder's byte
for byte. Every drawn line starts with a line break, as the old builder joined them.
"""


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

def tile(p,x,y,shape,fill,s=2.25,frame=True):
 if frame:p.p.append(f'\\draw[gray!70,line width=.65pt] ({x-s/2},{y-s/2}) rectangle ({x+s/2},{y+s/2});')
 if shape is None:return
 r=s*.3
 opt='fill=white' if fill==0 else 'pattern=north east lines' if fill==1 else 'fill=black'
 if shape==0:cmd=f'({x},{y}) circle ({r})'
 elif shape==1:cmd=f'({x},{y-r*1.1}) -- ({x+r},{y+r*.85}) -- ({x-r},{y+r*.85}) -- cycle'
 else:cmd=f'({x-r},{y-r}) rectangle ({x+r},{y+r})'
 p.p.append(f'\\draw[line width=1pt,{opt}] '+cmd+';')
def swatch(p,x,y,f):
 opt='fill=white' if f==0 else 'pattern=north east lines' if f==1 else 'fill=black'
 p.p.append(f'\\draw[{opt},line width=.7pt] ({x-.18},{y-.18}) rectangle ({x+.18},{y+.18});')
def demo_(p):
 # Left: two inputs, arrow, completing third. Right: two fills equal is invalid.
 for x,y,sh,fi in [(1.1,4.1,0,0),(3.8,4.9,1,2),(7.3,4.1,2,1),(11.2,4.1,0,0),(13.9,4.1,1,0),(16.6,4.1,2,2)]:tile(p,x,y,sh,fi,2.1)
 p.p.append(r'\draw[-{Stealth},line width=1pt] (5.05,4.7) -- (6.02,4.25);')
 p.text(.15,6.1,8.6,'allowed three',13);p.text(10.1,6.1,8.2,'not allowed',13)
 p.text(.15,6.85,2.3,'shapes',12);p.text(10.1,6.85,2.3,'shapes',12)
 for x,sh in [(2.7,0),(4,1),(5.3,2),(12.65,0),(13.95,1),(15.25,2)]:tile(p,x,7.12,sh,0,.63,False)
 p.text(6.0,6.85,2.9,'all different',11);p.text(16,6.85,2.7,'all different',11)
 p.text(.15,7.8,2.3,'fills',12);p.text(10.1,7.8,2.3,'fills',12)
 for x,fi in [(2.7,0),(4,2),(5.3,1),(12.65,0),(13.95,0),(15.25,2)]:swatch(p,x,8.05,fi)
 p.text(6,7.8,2.9,'all different',11);p.text(16,7.8,2.7,'two the same',11)
def pairs_(p):
 for x,y,pair in [(.3,12.3,[(0,0),(0,1)]),(10.05,12.3,[(0,0),(1,0)]),(.3,18.2,[(0,1),(1,2)]),(10.05,18.2,[(1,1),(2,0)])]:
  for j,(a,b) in enumerate(pair):tile(p,x+1.1+2.75*j,y,a,b,2.2)
  tile(p,x+7,y,None,None,2.2)
  p.p.append(f'\\draw[-{{Stealth}}] ({x+5.05},{y}) -- ({x+5.68},{y});')
def mat_(p,y=4.8,shown=False):
 for i in range(4):
  p.p.append(f'\\draw[gray!65] (.2,{y+6*i}) -- (18.2,{y+6*i});')
  p.p.append(f'\\draw[gray!65] ({.2+6*i},{y}) -- ({.2+6*i},{y+18});')
 if shown:
  for a in range(3):
   for b in range(3):tile(p,3.2+6*b,y+3+6*a,a,b,3.5,False)
def mini_(p,x,y,sel=()):
 for a in range(3):
  for b in range(3):
   tile(p,x+1.1+2.35*b,y+1.1+2.35*a,a,b,2.2)
   if (a,b) in sel:p.p.append(f'\\draw[line width=1.2pt] ({x+1.1+2.35*b},{y+1.1+2.35*a}) circle (1.05);')


# ---------------------------------------------------------------- figures
# Each draws what followed a rule or problem statement on its page.

@draw
def demo(p):  # the rules: an allowed three and a near miss, with shape and fill rows
 demo_(p)

@draw
def pairs(p):  # Problem 1 in every band: four pairs to complete
 pairs_(p)

@draw
def mat(p,y=4.8,shown=False):  # a 3 x 3 mat of 60 mm cells, empty or with the nine tiles
 mat_(p,y,shown)

@draw
def minis(p,*corners):  # small nine-tile record boards, one per (x, y) corner
 for x,y in corners:mini_(p,x,y)
