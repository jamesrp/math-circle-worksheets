from pathlib import Path
import math, subprocess, shutil, os, argparse
parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
parser.add_argument('--work',type=Path)
args=parser.parse_args()
ROOT=args.out.resolve()
SRC=(args.work or ROOT/'build').resolve()
ROOT.mkdir(parents=True,exist_ok=True)
SRC.mkdir(parents=True,exist_ok=True)
PRE=r'''\documentclass[11pt,letterpaper]{article}
\usepackage[margin=12mm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pagestyle{empty}\setlength{\parindent}{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
'''
class Packet:
 def __init__(self,name,level,tag): self.name=name; self.level=level; self.tag=tag; self.pages=[]
 def page(self):
  self.pages.append([r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\begin{scope}[shift={(current page.north west)},xshift=12mm,yshift=-19mm]'])
  self.text(0,-10,192,'Week 86 / Pursuit and escape / '+self.level,10)
  self.text(0,245,192,f'Bellingham Math Circle / Week 86 / {self.tag} / {len(self.pages)}',9)
 def add(self,s): self.pages[-1].append(s)
 def text(self,x,y,w,s,size=12): self.add(r'\node[anchor=north west,inner sep=0,text width='+str(w)+r'mm,font=\fontsize{'+str(size)+'}{'+str(size+3)+r'}\selectfont] at ('+f'{x},{y}'+') {'+s+'};')
 def problem(self,n,s,y=0): self.text(0,y,192,rf'\textbf{{Problem {n}:}} '+s)
 def graph(self,pts,edges,x,y,diam=22,label='',occup=None):
  if label:self.text(x+min(v[0] for v in pts.values())-diam/2,y+min(v[1] for v in pts.values())-diam/2-9,180,label,10)
  for a,b in edges:
   pa,pb=pts[a],pts[b];self.add(r'\draw[line width=1.1pt] '+f'({x+pa[0]},{y+pa[1]}) -- ({x+pb[0]},{y+pb[1]});')
  for k,(px,py) in pts.items():
   self.add(r'\draw[fill=white,line width=.8pt] '+f'({x+px},{y+py}) circle ({diam/2}mm);')
   self.add(r'\node[fill=white,inner sep=.5mm,font=\fontsize{9}{10}\selectfont] at ('+f'{x+px},{y+py+diam/2+3}'+') {'+k+'};')
   if occup and k in occup:self.add(r'\node[inner sep=0,font=\fontsize{10}{11}\selectfont] at ('+f'{x+px},{y+py}'+') {'+occup[k]+'};')
 def lines(self,y,n=2):
  for i in range(n):self.add(r'\draw[gray!40] '+f'(0,{y+12*i}) -- (192,{y+12*i});')
 def save(self):
  pages=['\n'.join(p)+r'\end{scope}\end{tikzpicture}\par' for p in self.pages]
  tex=PRE+'\n\\newpage\n'.join(pages)+'\n\\end{document}\n'
  (SRC/(self.name+'.tex')).write_text(tex)
  subprocess.run([os.environ.get('PDFLATEX', shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'),'-interaction=nonstopmode','-halt-on-error','-output-directory',str(SRC),str(SRC/(self.name+'.tex'))],check=True,stdout=subprocess.DEVNULL)
  subprocess.run([os.environ.get('PDFLATEX', shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'),'-interaction=nonstopmode','-halt-on-error','-output-directory',str(SRC),str(SRC/(self.name+'.tex'))],check=True,stdout=subprocess.DEVNULL)
  shutil.copy2(SRC/(self.name+'.pdf'),ROOT/(self.name+'.pdf'))
def path(n,spacing=32):
 p={chr(97+i):(i*spacing,0) for i in range(n)};return p,[(chr(97+i),chr(98+i)) for i in range(n-1)]
def cycle(n,r):
 p={chr(97+i):(r*math.cos(-math.pi/2+2*math.pi*i/n),r*math.sin(-math.pi/2+2*math.pi*i/n)) for i in range(n)}
 return p,[(chr(97+i),chr(97+(i+1)%n)) for i in range(n)]
def rules_page(p):
 p.page();p.text(0,0,192,'One player controls C; the other controls R. C chooses a dot first, then R chooses. C takes the first turn. On your turn, stay or take one road to the next dot. Flip the turn tile even if you stay. Sharing a dot means immediate capture. Both counters stay visible. Swap jobs between games.',11)
 pts={'w':(0,0),'x':(20,0),'y':(40,0),'z':(20,-15)};e=[('w','x'),('x','y'),('x','z')]
 for i,(occ,cap,tile) in enumerate([({'w':'C','y':'R'},'Start','C turn'),({'x':'C','y':'R'},'C takes one road','R turn'),({'x':'C','y':'R'},'R stays','C turn')]):
  x=6+64*i;p.text(x,41,60,cap,10);p.graph(pts,e,x,74,8,occup=occ);p.text(x+6,86,45,tile,10)
 p.problem(1,'Play on both paths. Choose a starting dot for C that guarantees capture in the fewest C turns, even when R chooses its hardest starting dot and moves.',106)
 p.graph(*path(5),32,150,label='P5');p.graph(*path(7,28),12,197,20,label='P7')
 p.lines(232,1)
shared=Packet('shared','Grades 2--5','W86-S-v1')
rules_page(shared)
shared.page();shared.problem(2,'Find a cop plan that catches R on each map, wherever R starts and however R moves. Challenge your partner to escape.')
t1={'a':(-64,0),'b':(-32,0),'c':(0,0),'d':(32,0),'e':(64,0),'f':(0,-32),'g':(0,-64)}
e1=[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g')]
shared.graph(t1,e1,96,110,label='T1')
t2={'a':(-64,0),'b':(-32,0),'c':(0,0),'d':(32,0),'e':(64,0),'f':(0,32),'g':(-32,64),'h':(32,64)}
e2=[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g'),('f','h')]
shared.graph(t2,e2,96,151,label='T2');shared.lines(239,1)
shared.page();shared.problem(3,'Play on both rings. On which can C always catch R? On which can R keep escaping forever? Find a plan that works against every reply.')
shared.graph(*cycle(3,34),96,77,label='R3');shared.graph(*cycle(4,39),96,179,label='R4');shared.lines(238,1)
shared.page();shared.problem(4,'Find an escape plan for R on each ring that keeps working however C moves. A long game is a test; your plan must work forever.')
shared.graph(*cycle(5,36),96,78,label='R5');shared.graph(*cycle(6,36),96,181,label='R6');shared.lines(238,1)
upper=Packet('upper','Grades 4--5','W86-U-v1');rules_page(upper)
upper.page();upper.problem(2,'Add as few roads as possible to each ring so C can always catch R. A road joins two existing dots. A crossing is not a new dot. Show a winning cop plan for each changed map.')
upper.graph(*cycle(4,36),96,82,label='E4');upper.graph(*cycle(5,36),96,185,label='E5');upper.lines(238,1)
upper.page();upper.problem(3,'Draw two connected maps using all six dots and at least six roads on each. Make one where C can always catch R and one where R can escape forever. Challenge your partner on both. Roads join dots; crossings are not junctions. Join any pair at most once.')
pts,_=cycle(6,32)
upper.graph(pts,[],96,86,label='D1: C can always catch R');upper.graph(pts,[],96,186,label='D2: R can escape forever')
upper.page();upper.text(0,0,192,'Try shrinking a map without changing who can force a win. You may remove a dot v when a neighboring dot u can reach every place v can reach by staying or taking one road. This is a fold, written v $\\to$ u. Remove v and all its roads. Test the next fold on the remaining map.',11)
wp,we=path(4,18);wp={k:(v[0],v[1]) for k,v in zip(['w','x','y','z'],wp.values())};we=[('w','x'),('x','y'),('y','z')]
upper.text(0,45,90,'Original: w can reach w, x.',10);upper.text(99,45,93,'Compare: x can reach w, x, y.',10)
upper.graph(wp,we,7,67,8);upper.graph(wp,we,106,67,8)
# The comparison marks both accessible sets on unchanged input.
upper.add(r'\draw[blue!55!black,line width=1pt,rounded corners=5mm] (1,60) rectangle (31,75);')
upper.add(r'\draw[blue!55!black,line width=1pt,rounded corners=5mm] (100,60) rectangle (148,75);')
upper.text(0,89,90,'w $\\to$ x: remove w and road w--x.',10)
upper.graph({'x':(0,0),'y':(18,0),'z':(36,0)},[('x','y'),('y','z')],118,97,8)
upper.problem(4,'Use boards F1 and F2 in the materials packet. Can each map fold down to one dot? Find a sequence of legal folds, or a remaining map with no legal fold. What does this suggest about the chasing game? Keep the original visible. On the working copy, cover each removed dot and its roads with removable opaque pieces. Leave surviving dots and roads visible.',121)
upper.lines(191,4)
upper.page();upper.text(0,0,192,'Use C1 and C2. Put down both cops before R chooses. On a cop turn, each cop may stay or take one road. Then R gets one turn. Flip the tile after the whole cop turn and after R\'s turn. Capture is immediate. Cops may share a dot.',11)
upper.problem(5,'Start both cops at a. Use them to catch R on this ring. Find a plan that works however R starts and moves.',40)
upper.graph(*cycle(6,42),96,129,label='Q6');upper.lines(202,3)
upper.page();upper.problem(6,'Find a two-cop plan for this ring. Will your plan work on every ring, however many dots it has? Explain why.')
upper.graph(*cycle(8,51),96,114,label='Q8');upper.lines(197,4)
materials=Packet('materials','Grades 2--5','W86-M-v1')
f1={'a':(0,0),'b':(32,-32),'c':(64,0),'d':(96,0),'e':(128,0),'f':(0,32)};fe1=[('a','b'),('b','c'),('c','a'),('c','d'),('d','e'),('a','f')]
materials.page();materials.text(0,0,192,'F1: original and working copy for upper Problem 4.',12);materials.graph(f1,fe1,32,68,label='Original');materials.graph(f1,fe1,32,177,label='Working copy')
f2,fe2=cycle(5,37);fe2=fe2+[('a','c')]
materials.page();materials.text(0,0,192,'F2: original and working copy for upper Problem 4.',12);materials.graph(f2,fe2,96,76,label='Original');materials.graph(f2,fe2,96,185,label='Working copy')
materials.page();materials.text(0,0,192,'Cut out each pair of squares. Attach them back to back to make a two-sided turn tile. Use the first tile with one cop and the second with two cops. Cut out counters, or use 14--18 mm counters marked C, R, C1 and C2.',12)
materials.text(0,173,192,'For folds: prepare opaque paper or card rectangles (24 by 32 mm) and strips about 5 mm wide, scissors, and removable tape. Trim covers to hide removed dots, labels and roads while leaving surviving dots and roads visible. Stack cops when they share a dot.',10)
for j,pair in enumerate([('C turn','R turn'),('Both cops','R turn')]):
 for i,lab in enumerate(pair):
  x=25+i*90;y=62+j*65;materials.add(r'\draw '+f'({x},{y}) rectangle ({x+35},{y+35});');materials.text(x+2,y+13,32,lab,11)
for i,lab in enumerate(['C','R','C1','C2']):
 x=35+i*40;materials.add(r'\draw '+f'({x},220) circle (9mm);');materials.text(x-5,216,14,lab,11)
for p in [shared,upper,materials]: p.save();print(p.name,len(p.pages))
