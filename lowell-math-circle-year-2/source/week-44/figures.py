"""Week 44 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/write.py and common.py); the October 23, 2026
card fixes changed the figures noted below.

Coordinates are centimetres on an 18.2 x 23.6 cm page picture; a figure's y grows
downward and is negated when drawn, as the old builder did. Problem files call the
functions below by name in their `figure` sections; the rule and prompt wording
lives in the problem files.
"""


class Board:
 """The drawing half of the old builder's Book (common.py): each call appends TikZ."""
 def __init__(self): self.items = []
 def put(self,s):self.items.append(s+'\n')
 def text(self,y,s,x=0,w=18,size=14):
  self.put(r'\node[anchor=north west,text width='+str(w)+r'cm,inner sep=0pt,font=\fontsize{'+str(size)+'}{'+str(size+3)+r'}\selectfont] at ('+str(x)+','+str(-y)+') {'+s+'};')
 def p(self,n,y,s,size=14):self.text(y,r'\textbf{Problem '+str(n)+':} '+s,size=size)
 def line(self,y,w=18,x=0):self.put(fr'\draw[gray!45] ({x},{-y}) -- ({x+w},{-y});')
 def space(self,y,n=3,gap=1):
  for i in range(n):self.line(y+i*gap)
 def box(self,x,y,w,h,label=''):
  self.put(fr'\draw[gray!65,rounded corners=2pt] ({x},{-y}) rectangle ({x+w},{-y-h});')
  if label:self.text(y+.15,label,x+.2,w-.4,11)
 def token(self,x,y,color,label='',r=.44):
  fill={'R':'red!18','B':'blue!18','':'white'}.get(color,'white')
  self.put(fr'\draw[fill={fill},line width=.7pt] ({x},{-y}) circle ({r});')
  if color:self.put(fr'\node[font=\bfseries\small] at ({x},{-y}) {{{label or color}}};')
 def pair(self,x,y,a,b,labels=None,scale=1):
  self.box(x,y,3.5*scale,1.35*scale)
  self.token(x+.9*scale,y+.67*scale,a,labels[0] if labels else '',.44*scale)
  self.token(x+2.6*scale,y+.67*scale,b,labels[1] if labels else '',.44*scale)
 def bag(self,x,y,colors,label='',ident=False):
  cols=min(4,len(colors)); rows=(len(colors)+cols-1)//cols
  w=max(3,cols*1.1+.45); h=rows*1.1+.55
  self.box(x,y,w,h)
  for i,c in enumerate(colors):self.token(x+.75+(i%cols)*1.05,y+.7+(i//cols)*1.05,c, c+str(i+1) if ident else '')
  if label:self.text(y+h+.18,label,x,w,12)
 def arrow(self,x,y,x2,y2,label=''):
  self.put(fr'\draw[-{{Stealth[length=2mm]}},line width=.8pt] ({x},{-y}) -- ({x2},{-y2}) node[midway,above,font=\small] {{{label}}};')
 def shape(self,x,y,s):
  if s=='square':self.put(fr'\draw[line width=1pt] ({x-.35},{-y-.35}) rectangle ({x+.35},{-y+.35});')
  elif s=='circle':self.put(fr'\draw[line width=1pt] ({x},{-y}) circle (.35);')
  else:self.text(y-.3,'none',x-.5,1.4,11)


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


# ---------------------------------------------------------------- shared pictures (write.py)

def strip(b,x,y,n,w=1.8):
 for i in range(n):b.box(x+i*w,y,w,1.8)
def bowl(b,x,y,w=7,h=3):b.box(x,y,w,h)


@draw
def rules_picture(b):  # 00: RB, draw R, return + copy, RRB
 b.bag(0,2.5,'RB');b.arrow(3.4,3.2,5,3.2,'draw R');b.token(5.8,3.2,'R');b.arrow(6.7,3.2,10,3.2,'return + copy');b.bag(11,2.5,'RRB')


@draw
def marks_picture(b,y):  # 11, 20: R1 -> R1 B1 R2 -> R2, with captions (the old identities(b,y) after its text)
 b.token(.6,y+2.5,'R','R1');b.arrow(1.4,y+2.5,3,y+2.5)
 for x,c,l in [(4,'R','R1'),(5.2,'B','B1'),(6.4,'R','R2')]:b.token(x,y+2.5,c,l)
 b.arrow(7.3,y+2.5,9,y+2.5);b.token(10,y+2.5,'R','R2')
 b.text(y+3.5,'draw R1',0,3,11);b.text(y+3.5,'return it and add R2',3.5,5,11);b.text(y+3.5,'next draw could be R2',9,8,11)


# ---------------------------------------------------------------- problem figures, by file

@draw
def k1_two_draw_bowls(b):  # 01
 for x,y in [(0,8),(9,8),(0,13)]:bowl(b,x,y,8,4)
 strip(b,0,21.5,2,3.5);strip(b,10,21.5,2,3.5)


@draw
def k1_three_draw_bags(b):  # 02
 for i,colors in enumerate(['RRRRB','RRBBB','RRRRR','RBBBB']):
  x=(i%2)*9.2;y=3+(i//2)*9;b.bag(x,y,colors);strip(b,x,y+4.2,3,2.5)


@draw
def k1_story_rows(b):  # 03: eight story rows, then two bag boxes with a row each
 b.bag(0,2.3,'RRRBBB')
 for i in range(8):strip(b,(i%2)*9.2,round(5.8+(i//2)*2.5,2),4,1.9)
 for x in (0,9.2):bowl(b,x,16.3,7.6,3);strip(b,x,19.8,4,1.9)


@draw
def k1_before_last(b):  # 04
 b.text(1.8,'after four draws',0,6,12);b.text(1.8,'before the last draw',8,10,12)
 for i,colors in enumerate(['RRRRRB','RRRRBB','RRRBBB']):
  y=3+i*6.5;b.bag(0,y,colors);b.arrow(5,y+1.2,7,y+1.2);bowl(b,8,y,10,4.5)


@draw
def story_bowls(b):  # 10: five story slots (one spare), lines beside the fifth
 for i in range(5):
  x=(i%2)*9.2;y=7.6+(i//2)*5;strip(b,x,y,2,2.2);bowl(b,x,round(y+2.1,2),7.8,2.6)
 for y in (19.3,20.6,21.9):b.line(y,8.8,9.2)


@draw
def marked_tree(b,y):  # 12 (the old tree(b,y))
 b.text(y,'first draw',0,3,12);b.text(y,'second draw',8,5,12);b.text(y,'bag colors only',13,4.8,12)
 for row,c in enumerate(['R','B']):
  yy=y+2+row*7;b.token(2,yy+1.8,c,c+'1',.6)
  for j in range(3):
   b.arrow(3,yy+1.8,7.5,yy+j*1.9);b.box(8,yy+j*1.9-.7,3,1.4);b.arrow(11.4,yy+j*1.9,12.5,yy+j*1.9);b.box(13,yy+j*1.9-.7,4.8,1.4)


@draw
def two_rules(b):  # 13
 b.text(3.3,'return and add a copy',0,8,14);b.text(3.3,'return only',10,8,14)
 for x in [0,10]:b.token(x+1,5,'R','R1');b.token(x+2.4,5,'B','B1');bowl(b,x,7,8,8)


@draw
def four_draw_bags(b):  # 15: room for 2, 6 and 8 stories (1, 4 and 6 are needed)
 for y,colors,rows in [(2.2,'RRRRRB',1),(6.0,'RRRRBB',3),(13.4,'RRRBBB',4)]:
  b.bag(0,y,colors)
  for r in range(rows):
   for x in (5.6,11.9):strip(b,x,round(y+r*2.3,2),4,1.5)


@draw
def which_bag(b):  # 16: the two bags, a work box and lines
 b.bag(0,2.3,'RRRRRB');b.bag(9.2,2.3,'RRRBBB');b.box(0,5.8,18,13);b.space(20,4)


@draw
def order_boxes(b):  # 23
 for i,s in enumerate(['RRB','RBR','BRR']):
  b.text(17,s,i*6.1,5.7,14);b.box(i*6.1,18.2,5.7,4.8)


@draw
def total_boxes(b):  # 24 ('1 red draw', singular, from October 23)
 for i in range(4):
  x=(i%2)*9.2;y=4+(i//2)*8.2;b.text(y,str(i)+(' red draw' if i==1 else ' red draws'),x,8,14);b.box(x,y+1.2,8,5.7)
 b.space(22,2)


@draw
def box_lines(b,x,y,w,h,lines=None):  # a box, then ruled lines (y, n)
 b.box(x,y,w,h)
 if lines:b.space(*lines)


@draw
def lines(b,y,n,gap=1):
 b.space(y,n,gap)
