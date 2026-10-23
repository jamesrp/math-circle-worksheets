"""Week 42 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/write.py and common.py); the October 23, 2026
card fixes added the blank and marked-pair grids and changed the figures noted below.

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

def ruleboard(b,y):
 for i,(a,c) in enumerate([('R','R'),('R','B'),('B','R'),('B','B')]):
  x=0 if i<2 else 9.3; yy=y+(i%2)*2.8
  b.pair(x,yy,a,c);b.arrow(x+3.8,yy+.68,x+4.8,yy+.68);b.box(x+5.1,yy,2,1.35)
def pairs_grid(b,y=6):
 labels=['R1','R2','R3','B']; cols=['R','R','R','B'];x=3;d=3
 b.text(y-2.1,'First draw down the side; second draw across the top.',size=12)
 for i in range(4):
  b.token(x+i*d+d/2,y-.7,cols[i],labels[i],.45)
  b.token(x-.8,y+i*d+d/2,cols[i],labels[i],.45)
  for j in range(4):b.box(x+j*d,y+i*d,d,d)
 b.put(fr'\draw[line width=1.4pt] ({x+3*d},{-y-d}) rectangle ({x+4*d},{-y-2*d});')
 b.token(x+3*d+.7,y+d+1.5,'R','R2',.42);b.token(x+3*d+2.2,y+d+1.5,'B','B',.42)

def storyslot(b,x,y):
 b.box(x,y,3.6,1.65);b.put(fr'\draw[gray!50] ({x+1.8},{-y}) -- ({x+1.8},{-y-1.65});')
 b.arrow(x+3.8,y+.82,x+4.45,y+.82);b.box(x+4.65,y+.3,1.05,1.05)
def markedpair(b,x,y,a,c):
 b.box(x,y,5.5,2.7)
 b.token(x+1.35,y+1.35,a[0],a,.52);b.token(x+4.15,y+1.35,c[0],c,.52)
def blank_grid(b,x,y,d,heads=None,r=.4):
 """A 4-by-4 grid of d-cm cells with x, y its top left; head circles above the columns
 and left of the rows, labeled with heads or left empty for the children to label."""
 for i in range(4):
  c,lab=(heads[i][0],heads[i]) if heads else ('','')
  b.token(round(x+i*d+d/2,3),round(y-.65,3),c,lab,r)
  b.token(round(x-.65,3),round(y+i*d+d/2,3),c,lab,r)
  for j in range(4):b.box(round(x+j*d,3),round(y+i*d,3),d,d)
def labeled_bag(b,x,y,labels):
 """A one-row bag whose counters carry their marks (R, B1, ...)."""
 b.box(x,y,round(len(labels)*1.1+.45,2),1.65)
 for i,l in enumerate(labels):b.token(round(x+.75+i*1.05,2),y+.7,l[0],l)
def marked_grid(b,y,labels):
 """All 16 marked pairs from a four-counter bag in compact boxes, one row per first counter."""
 for i,a in enumerate(labels):
  for j,c in enumerate(labels):
   x,yy=round(j*4.5,2),round(y+i*1.85,2)
   b.box(x,yy,4.3,1.65)
   b.token(x+1.15,round(yy+.825,3),a[0],a,.45);b.token(x+3.15,round(yy+.825,3),c[0],c,.45)


@draw
def sample_rule(b,y,ay,ty):
 """A sample rule, BR gives a square, with its caption (the old rules(b) and K-1 page 2)."""
 b.pair(.5,y,'B','R');b.arrow(4.5,ay,6,ay);b.shape(7,ay,'square')
 b.text(ty,'A sample rule: BR gives a square.',9,8.5,12)


# ---------------------------------------------------------------- problem figures, by file

@draw
def k1_bag_and_pair(b):  # 00
 b.bag(0,1.7,'RRRB');b.pair(7,1.7,'R','B');b.arrow(5,2.4,6.4,2.4)


@draw
def k1_pair_boxes(b):  # 01
 for x,y in [(0,8),(9,8),(0,13),(9,13)]:
  b.box(x,y,7.4,3.5);b.put(fr'\draw[gray!50] ({x+3.7},{-y}) -- ({x+3.7},{-y-3.5});')
 b.bag(1,19,'RRRB','the bag');b.bag(10,19,'RRR','blue taken out')


@draw
def rule_board(b,y):  # 03, 10, 20
 ruleboard(b,y)


@draw
def answer_box(b,y,h=5.5):  # 03
 b.box(0,y,18,h)


@draw
def k1_marked_pairs(b):  # 05
 labels=['R1','R2','R3','B']
 for i,(a,c) in enumerate((a,c) for a in labels for c in labels):
  markedpair(b,(i%3)*6.1,3.5+(i//3)*3.35,a,c)


@draw
def k1_other_bags(b):  # 06: the four bags, then every marked pair of the two mixed bags
 one,two=['R','B1','B2','B3'],['R1','R2','B1','B2']
 labeled_bag(b,0,2,one);labeled_bag(b,10,2,two);b.bag(0,4.1,'RRRR');b.bag(10,4.1,'BBBB')
 b.text(6.4,'Marked pairs from R, B1, B2, B3',size=13);marked_grid(b,7.1,one)
 b.text(14.75,'Marked pairs from R1, R2, B1, B2',size=13);marked_grid(b,15.45,two)


@draw
def k1_two_boxes(b):  # 07, now on its own page
 b.box(0,2.6,8.6,6);b.box(9.4,2.6,8.6,6)


@draw
def k1_stories(b):  # 08
 for y,lab in [(3,'no shapes'),(9.7,'exactly one square and no circles'),(16.4,'exactly three circles and no squares')]:
  b.text(y,lab,size=13)
  for i in range(6):storyslot(b,(i%3)*6.1,y+1.1+(i//3)*2.3)


@draw
def board_box_lines(b):  # 11
 ruleboard(b,8.4);b.box(0,15.1,18,3.5);b.space(20,3)


@draw
def labeled_pair_grid(b):  # 12
 b.pair(0,2.1,'R','B',('R2','B'));b.arrow(4,2.8,5.2,2.8);b.text(2.1,'row R2, column B',5.7,10,13)
 pairs_grid(b,5.8);b.space(20.3,3)


@draw
def bags(b,specs,lines=None):  # bags as (x, y, colors, caption), then ruled lines (y, n)
 for x,y,cs,lab in specs:b.bag(x,y,cs,lab)
 if lines:b.space(*lines)


@draw
def bags_blank_grids(b):  # 13: each bag over a blank grid with empty heads
 for x,gx,cs in [(1,1.1,'RRBB'),(10,10.4,'RBBB')]:
  b.bag(x,2,cs);blank_grid(b,gx,5.1,1.75)
 b.space(13.1,2)


@draw
def two_bags_grid(b):  # 15: the two bags over one blank grid, lines beside it
 b.bag(0,2.2,'RRRB','first draw');b.bag(11,2.2,'RBBB','second draw');b.arrow(5.5,3,10,3)
 blank_grid(b,1.1,5.7,1.75)
 for y in (6.7,7.9,9.1,10.3,11.5,12.7):b.line(y,8.4,9.6)


@draw
def labeled_grid_lines(b):  # 21: a grid headed R1, R2, R3, B; the pair example and lines beside it
 x,y,d=1.1,15.6,1.85
 blank_grid(b,x,y,d,['R1','R2','R3','B'])
 # The R2-row, B-column cell is outlined, as in Grades 2-3 Problem 3, so the example shows which head is the first draw.
 b.put(fr'\draw[line width=1.4pt] ({round(x+3*d,3)},{round(-y-d,3)}) rectangle ({round(x+4*d,3)},{round(-y-2*d,3)});')
 b.pair(9.8,15.6,'R','B',('R2','B'));b.text(17.3,'R2 then B is one labeled pair.\\\\ Its cell is outlined.',9.8,8.2,12)
 for y in (19.2,20.2,21.2,22.2,23.2):b.line(y,8.2,9.8)


@draw
def changed_bags(b):  # 24
 for y,a,c in [(3,'RRRB','RBBB'),(8,'RRRB','RRRRRRBB'),(14,'RRBB','RB')]:
  b.bag(0,y,a,'first');b.bag(10,y,c,'second');b.arrow(5,y+.75,9,y+.75)
 b.space(20,4)


@draw
def bag_and_pair(b):  # 25
 b.bag(0,3,'RRRB');b.pair(8,3,'R','B',('R1','B'));b.space(6.5,5)


@draw
def lines(b,y,n,gap=1):
 b.space(y,n,gap)

