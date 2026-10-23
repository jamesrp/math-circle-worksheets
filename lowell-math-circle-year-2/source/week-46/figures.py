"""Week 46 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/write.py and editable/src/common.py).

Coordinates are centimetres on an 18.2 x 23.6 cm page picture; a figure's y grows
downward and is negated when drawn, as the old builder did. Problem files call the
functions below by name in their `figure` sections; the rule and prompt wording
lives in the problem files.
"""


class Board:
    """The drawing half of the old builder's Book (common.py): each call appends TikZ."""

    def __init__(self):
        self.items = []

    def put(self, s): self.items.append(s+'\n')

    def text(self, y, s, x=0, w=18, size=14):
        self.put(r'\node[anchor=north west,text width='+str(w)+r'cm,inner sep=0pt,font=\fontsize{'+str(size)+'}{'+str(size+3)+r'}\selectfont] at ('+str(x)+','+str(-y)+') {'+s+'};')

    def line(self, y, w=18, x=0): self.put(fr'\draw[gray!45] ({x},{-y}) -- ({x+w},{-y});')

    def space(self, y, n=3, gap=1):
        for i in range(n): self.line(y+i*gap)

    def box(self, x, y, w, h, label=''):
        self.put(fr'\draw[gray!65,rounded corners=2pt] ({x},{-y}) rectangle ({x+w},{-y-h});')
        if label: self.text(y+.15, label, x+.2, w-.4, 11)

    def token(self, x, y, color, label='', r=.44):
        fill = {'R': 'red!18', 'B': 'blue!18', '': 'white'}.get(color, 'white')
        self.put(fr'\draw[fill={fill},line width=.7pt] ({x},{-y}) circle ({r});')
        if color: self.put(fr'\node[font=\bfseries\small] at ({x},{-y}) {{{label or color}}};')

    def arrow(self, x, y, x2, y2, label=''):
        self.put(fr'\draw[-{{Stealth[length=2mm]}},line width=.8pt] ({x},{-y}) -- ({x2},{-y2}) node[midway,above,font=\small] {{{label}}};')


def draw(fn):
    """Run a drawing function on a fresh Board and return the TikZ it drew."""
    def figure(*args, **kw):
        b = Board()
        fn(b, *args, **kw)
        return ''.join(b.items)
    figure.__name__ = fn.__name__
    return figure


# ---------------------------------------------------------------- page template
# The old builder's page: Latin Modern, 0.65 in margins, one picture per page.

def page_preamble(week, topic, header, footer):
    pre = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=.65in,top=.72in,bottom=.62in,headheight=16pt,headsep=15pt,footskip=19pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,tikz,fancyhdr}\pdfmapfile{+lm.map}
\usetikzlibrary{arrows.meta,shapes.geometric}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}
'''
    pre += r'\fancyhead[L]{\small Week '+str(week)+' / '+topic+' / '+header+'}\n'
    pre += r'\fancyfoot[L]{\footnotesize Bellingham Math Circle / Week '+str(week)+' / '+footer+'}'+r'\fancyfoot[R]{\footnotesize\thepage}'+'\n'+r'\begin{document}'+'\n'
    return pre


PAGE_OPEN = r'\noindent\begin{tikzpicture}[x=1cm,y=1cm]\path[use as bounding box] (0,0) rectangle (18.2,-23.6);'+'\n'
PAGE_CLOSE = r'\end{tikzpicture}'+'\n'


def page_prompt(n, body, x, y, size):
    b = Board()
    b.text(y or 0, r'\textbf{Problem '+str(n)+':} '+body, size=size or 14)
    return ''.join(b.items)


def page_text(x, y, body, w, size):
    b = Board()
    b.text(y or 0, body, x or 0, w or 18, size or 14)
    return ''.join(b.items)


# ---------------------------------------------------------------- shared pictures
# A board is three slots; R and B tokens sit in them. An instruction card names a slot
# and a color (pos -> col), with the named slot outlined.

def row(b,x,y,word='',cell=1.35,labels=False):
 for i in range(3):
  b.box(x+i*cell,y,cell,cell)
  if labels:b.text(y+.07,str(i+1),x+i*cell+.12,.6,9)
  if word:b.token(x+(i+.5)*cell,y+cell*.56,word[i],r=min(.42,cell*.3))


def pairrows(b,x,y,a,c,cell=1.35):row(b,x,y,a,cell);row(b,x,y+cell+.35,c,cell)


def card(b,x,y,pos,col,w=2.2):
 b.box(x,y,w,1.5)
 d=(w-.3)/3
 for j in range(3):
  xx=x+.15+j*d
  b.box(xx,y+.15,d,.78)
  if j==pos-1:
   b.put(fr'\draw[line width=1.4pt] ({xx},{-y-.15}) rectangle ({xx+d},{-y-.93});')
   b.token(xx+d/2,y+.54,col,r=min(.24,d*.35))
 b.text(y+1.05,str(pos)+r'$\to$'+col,x+.16,w-.2,9)


def history(b,x,y,h):
 for i,(p,c) in enumerate(h):card(b,x+i*2.6,y,p,c)


def tcard(b,x,y,pos,w=2.2):  # a toggle card: the named slot holds a half-red, half-blue token
 b.box(x,y,w,1.5)
 d=(w-.3)/3
 for j in range(3):
  xx=x+.15+j*d
  b.box(xx,y+.15,d,.78)
  if j==pos-1:
   b.put(fr'\draw[line width=1.4pt] ({xx},{-y-.15}) rectangle ({xx+d},{-y-.93});')
   cx,cy,r=xx+d/2,y+.54,min(.24,d*.35)
   b.put(fr'\fill[red!18] ({cx},{-cy}) -- ++(90:{r}) arc (90:270:{r}) -- cycle;\fill[blue!18] ({cx},{-cy}) -- ++(-90:{r}) arc (-90:90:{r}) -- cycle;')
   b.put(fr'\draw[line width=.7pt] ({cx},{-cy}) circle ({r});')
 b.text(y+1.05,'toggle '+str(pos),x+.16,w-.2,9)


@draw
def intro_picture(b):  # 00: BBR/RBB, then 1->B on both boards (a non-task pair)
 pairrows(b,0,2.5,'BBR','RBB',1.4);card(b,6,3.4,1,'B');b.arrow(4.7,4.1,5.6,4.1);b.arrow(8.7,4.1,10,4.1);pairrows(b,10.5,2.5,'BBR','BBB',1.4)


@draw
def toggle_picture(b):  # toggle rules: RBR/BRB, toggle slot 2
 pairrows(b,0,2.4,'RBR','BRB',1.4);b.arrow(4.8,4,9.5,4,'toggle slot 2');pairrows(b,10.3,2.4,'RRR','BBB',1.4)


@draw
def cases(b,y):  # four starting pairs, each with an answer box
 for i,(a,c) in enumerate([('RBR','RRR'),('RRB','BRR'),('BRB','BRB'),('RRR','BBB')]):
  x=(i%2)*9.2;yy=y+(i//2)*7.2;pairrows(b,x,yy,a,c,1.65);b.box(x+5.8,yy+1,2.2,1.6)


@draw
def cardsix(b,y):  # the six instruction cards
 for i,(p,c) in enumerate([(1,'R'),(2,'R'),(3,'R'),(1,'B'),(2,'B'),(3,'B')]):card(b,(i%3)*5.7,y+(i//3)*2.3,p,c,3.8)


@draw
def board(b,x,y,word='',cell=1.35,labels=False):
 row(b,x,y,word,cell,labels)


@draw
def board_pair(b,x,y,a,c,cell=1.35):
 pairrows(b,x,y,a,c,cell)


@draw
def story(b,x,y,h):
 history(b,x,y,h)


@draw
def g23_stories(b,y=5):  # grades 2-3: three stories, each with a board beside it
 for yy,h in [(y,[(1,'R'),(1,'B'),(3,'R')]),(y+5,[(2,'R'),(3,'B'),(1,'R')]),(y+10,[(2,'B'),(2,'R'),(2,'B')])]:history(b,0,yy,h);row(b,10,yy,'',2.3,True)


@draw
def g45_stories(b):  # grades 4-5: the same three stories, each with an answer box
 for y,h in [(3,[(1,'R'),(1,'B'),(3,'R')]),(8,[(2,'R'),(3,'B'),(1,'R')]),(13,[(2,'B'),(2,'R'),(2,'B')])]:history(b,0,y,h);b.box(9,y,9,3.7)


@draw
def toggle_pairs(b,y=10):  # three starting pairs for shared toggles
 for i,(a,c) in enumerate([('RBR','RRR'),('RRB','BRR'),('BRB','BRB')]):pairrows(b,i*6.1,y,a,c,1.65)


@draw
def mixed_stories(b,y):  # grades 4-5: three stories of setting and toggle cards, each with a finish board
 for k,h in enumerate([[(1,'R'),(1,'T'),(2,'B'),(3,'R')],[(3,'B'),(2,'T'),(1,'R'),(2,'T')],
                       [(3,'T'),(2,'R'),(3,'B'),(1,'B'),(3,'T')]]):
  yy=y+k*2.4
  for i,(p,c) in enumerate(h):
   if c=='T':tcard(b,i*2.6,yy,p)
   else:card(b,i*2.6,yy,p,c)
  b.text(yy-.05,'finish',13.6,2,9);row(b,13.6,yy+.3,'',1.4)


@draw
def box(b,x,y,w,h,label=''):
 b.box(x,y,w,h,label)


@draw
def space(b,y,n=3,gap=1):
 b.space(y,n,gap)
