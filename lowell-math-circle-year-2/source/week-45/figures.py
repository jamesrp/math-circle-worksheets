"""Week 45 figures and canvas page template, carried over unchanged from the old builder
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
\hyphenation{better differ}
\hyphenpenalty=10000
\exhyphenpenalty=10000
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
# Faces 1, 2 and 3 are red, 4, 5 and 6 blue; the cards are the face pairs (1,2), (3,4), (5,6).
COL={1:'R',2:'R',3:'R',4:'B',5:'B',6:'B'}
OTHER={1:2,2:1,3:4,4:3,5:6,6:5}


def face(b,x,y,n,w=2.1,h=2.8,hide=False):
 fill='red!15' if COL[n]=='R' else 'blue!15'
 b.put(fr'\draw[fill={fill},rounded corners=2pt] ({x},{-y}) rectangle ({x+w},{-y-h});')
 b.text(y+.7, COL[n],x+w/2-.22,.6,17)
 if hide:b.put(fr'\draw[fill=black] ({x+.15},{-y-h+.2}) rectangle ({x+.65},{-y-h+.6});')
 else:b.text(y+h-.6,str(n),x+.2,.7,10)


def ticket(b,x,y,n):b.box(x,y,1.25,1.25);b.text(y+.28,str(n),x+.4,.5,14)


@draw
def cards(b,y):  # the three cards, each face pair bracketed as "same card"
 for i,(a,c) in enumerate([(1,2),(3,4),(5,6)]):
  x=i*6.1;face(b,x,y,a);face(b,x+2.6,y,c);b.put(fr'\draw[gray] ({x+1.05},{-y-3.05}) -- ({x+1.05},{-y-3.35}) -- ({x+3.65},{-y-3.35}) -- ({x+3.65},{-y-3.05});');b.text(y+3.6,'same card',x+.65,4,11)


@draw
def intro_example(b,top=9.4):  # 00: ticket 4 shows blue with its number covered, red underneath
 ticket(b,0,top+.4,4);b.arrow(1.7,top+1,3.2,top+1);face(b,3.8,top,4,hide=True);b.arrow(6.5,top+1.2,9,top+1.2,'turn over');face(b,9.7,top,3)
 b.text(top+3.2,'ticket 4',0,3,11);b.text(top+3.2,'blue showing',3.4,5,11);b.text(top+3.2,'red underneath',9.3,7,11)


@draw
def bins(b,y,labels=('red underneath','blue underneath'),h=6):  # two labelled answer boxes side by side
 for i,l in enumerate(labels):
  b.text(y,l,i*9.2,8,13);b.box(i*9.2,y+1.1,8,h)


@draw
def changed_picture(b,top=3):  # 10: tickets 1 and 3 each show red with the number covered
 for x,n in [(0,1),(9.2,3)]:
  ticket(b,x,top+.4,n);b.arrow(x+1.6,top+1,x+3,top+1);face(b,x+3.5,top,n,hide=True)


@draw
def pair_slots(b,y,n=6,s=1.5,gap=2.6):  # 02, grades 2-3: n answer slots of two ticket boxes, three to a row
 for j in range(n):
  x=(j%3)*6.1;yy=y+(j//3)*gap
  for i in range(2):b.box(x+i*(s+.35),yy,s,s)


@draw
def ticket_slots(b,y,groups,gap=2):  # 12, K-1: groups of three ticket boxes, three groups to a row
 for j in range(groups):
  for i in range(3):b.box((j%3)*6.1+i*1.55,y+(j//3)*gap,1.25,1.25)


@draw
def boxes_row(b,y,n,w,h,gap):  # 17, K-1: n answer boxes in a row
 for i in range(n):b.box(i*(w+gap),y,w,h)


@draw
def fact_lines(b,y,labels,gap=1.75):  # 09, grades 4-5: a label and two writing lines per fact
 for i,l in enumerate(labels):
  yy=y+i*gap;b.text(yy,l,0,3.6,12);b.line(yy+.5,14.2,3.8);b.line(yy+1.3,14.2,3.8)


@draw
def ticket_row(b,y):  # 19, grades 4-5: the six tickets in a row
 for i in range(6):ticket(b,i*2.9,y,i+1)


@draw
def box(b,x,y,w,h,label=''):
 b.box(x,y,w,h,label)


@draw
def space(b,y,n=3,gap=1):
 b.space(y,n,gap)
