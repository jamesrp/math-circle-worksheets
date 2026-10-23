"""Week 43 figures and canvas page template, carried over unchanged from the old builder
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

def icon(b,x,y,c,s=.35):
 if c=='A':b.put(fr'\draw[fill=orange!22,line width=.8pt] ({x-s},{-y-s}) rectangle ({x+s},{-y+s});')
 if c=='B':b.put(fr'\draw[fill=green!22,line width=.8pt] ({x},{-y}) circle ({s});')
 if c=='C':b.put(fr'\draw[fill=violet!22,line width=.8pt] ({x},{-y+s}) -- ({x+s},{-y-s}) -- ({x-s},{-y-s}) -- cycle;')
 if c=='D':b.put(fr'\draw[fill=cyan!22,line width=.8pt] ({x},{-y+s}) -- ({x+s},{-y}) -- ({x},{-y-s}) -- ({x-s},{-y}) -- cycle;')
 if c=='E':b.put(fr'\draw[fill=yellow!25,line width=.8pt] ({x-s},{-y-s}) -- ({x+s},{-y-s}) -- ({x+s},{-y}) -- ({x},{-y+s}) -- ({x-s},{-y}) -- cycle;')
def row(b,x,y,word='',w=4.7,h=1.8,labels=False):
 for i in range(3):
  b.box(x+i*w/3,y,w/3,h)
  if word:icon(b,x+(i+.5)*w/3,y+h*.43,word[i],min(.38,w/9))
  if word and labels:b.text(y+h*.72,word[i],x+i*w/3+.15,w/3-.2,9)
def mat(b,x,y):
 for i in range(3):b.box(x+i*4.7,y,4.7,6.1);b.text(y+.12,str(i+1),x+i*4.7+.15,1,11)
def tickets(b,x,y,nums):
 for i,n in enumerate(nums):b.box(x+i*1.2,y,1,1);b.text(y+.17,str(n),x+i*1.2+.3,.5,13)
def swapdemo(b,y):
 row(b,0,y,'ABC',4.3,1.7,True);b.arrow(4.7,y+.8,6.1,y+.8,'1 with 3');row(b,6.5,y,'CBA',4.3,1.7,True)
 b.arrow(11.1,y+.8,12.7,y+.8,'2 with 2');row(b,13.2,y,'CBA',4.3,1.7,True)


@draw
def chooser_picture(b,y):
 """The chooser example under its rule (problems/01-chooser.md): C, then A, gives C A B."""
 icon(b,1,y+3,'C');b.arrow(2,y+3,3,y+3);icon(b,4,y+3,'A');b.arrow(5,y+3,6,y+3);row(b,7,y+2.1,'CAB',5,1.8,True)


@draw
def swap_picture(b,y):
 """The ticket sets and the swap demonstration under the two-swap rule (problems/03-swap-rule.md)."""
 tickets(b,0,y+3.1,[1,2,3]);b.text(y+3.3,'swap with slot 1',4,5,11)
 tickets(b,9.2,y+3.1,[2,3]);b.text(y+3.3,'swap with slot 2',12,6,11)
 swapdemo(b,y+4.8)


# ---------------------------------------------------------------- problem figures, by file

@draw
def k1_every_row(b):  # 00
 row(b,1,1.7,'ABC',6,2.2,True);mat(b,2,5)
 for i in range(6):row(b,(i%2)*9,13+(i//2)*3.3,w=7.8,h=2.5)


@draw
def k1_first_card_rows(b):  # 02, K-1
 for i,c in enumerate('ABC'):
  y=9+i*4.5;icon(b,.7,y+.7,c,.4)
  b.put(fr'\draw[line width=1pt] (0,{-y}) -- (1.4,{-y-1.4});')
  for j in range(4):row(b,2+(j%2)*8,y+(j//2)*1.9,w=7,h=1.55)


@draw
def chooser_answer_rows(b,h):  # 02, grades 2-3 (h=2.6) and 4-5 (h=2.5)
 for i in range(6):row(b,(i%2)*9,9+(i//2)*3.6,w=7.8,h=h)
 b.space(21,3)


@draw
def k1_ticket_records(b):  # 04, K-1
 mat(b,2,10)
 for i in range(6):
  x=(i%3)*6.1;y=17+(i//3)*3.2
  tickets(b,x,y,['','']);row(b,x+2.6,y,w=3.1,h=1.4)


@draw
def printed_stories(b):  # 04, grades 2-3
 for i,(u,v) in enumerate([(1,2),(2,2),(3,2),(1,3),(2,3),(3,3)]):
  x=(i%2)*9.2;y=9.7+(i//2)*4.3;tickets(b,x,y,[u,v]);row(b,x,y+1.3,w=7.8,h=2.5)


@draw
def answer_box(b,y,h):  # 04 and 11, grades 4-5
 b.box(0,y,18,h)


@draw
def bac_targets(b):  # 05, grades 2-3
 for i,word in enumerate(['ABC','ACB','BAC','BCA','CAB','CBA']):
  x=(i%2)*9.2;y=3+(i//2)*4.9;row(b,x,y,word,6.4,2,True);b.box(x,y+2.4,2,1.5);b.box(x+2.5,y+2.4,2,1.5)


@draw
def start_row_and_lines(b,word,y,lines):  # 05 and 12, grades 4-5
 row(b,0,y,word,6,2,True);b.space(y+3,lines)


@draw
def k1_missing_ticket_rows(b):  # 06
 for i,u in enumerate([1,2,3]):
  y=3+i*4.8;tickets(b,0,y,[v for v in [1,2,3] if v!=u])
  for j in range(2):row(b,4+j*7,y,w=6.4,h=2.2)


@draw
def k1_two_starts(b):  # 07
 row(b,0,21,'ABC',6,2,True);row(b,10,21,'CBA',6,2,True)


@draw
def lines(b,y,n):  # 08 and 11, grades 2-3
 b.space(y,n)


@draw
def three_swap_demo(b):  # 09, grades 2-3
 swapdemo(b,3)
 row(b,0,5.2,'CBA',4.3,1.4,True);b.arrow(4.8,5.9,7,5.9,'3 with 1');row(b,7.5,5.2,'ABC',4.3,1.4,True)


@draw
def three_ticket_records(b):  # 10
 for i in range(3):tickets(b,1,10+i*3.1,['','','']);row(b,9,9.6+i*3.1,w=7.5,h=2.1)


@draw
def four_card_design(b):  # 13
 for i,c in enumerate('ABCD'):
  b.box(i*4.5,3.1,4.5,2.5);icon(b,i*4.5+2.25,4,c,.45);b.text(4.9,c,i*4.5+2,.8,11)
 b.box(0,7,18,4.5)


@draw
def five_card_design(b):  # 14
 for i,c in enumerate('ABCDE'):
  b.box(i*3.6,16.4,3.6,2.5);icon(b,i*3.6+1.8,17.3,c,.45);b.text(18.2,c,i*3.6+1.55,.8,11)
 b.box(0,20,18,3.2)
