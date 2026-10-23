from pathlib import Path
import math,itertools,json
SRC=Path(__file__).resolve().parent
PRE=r'''\RequirePackage{fix-cm}
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
class Packet:
 def __init__(self,name,level):self.name=name;self.level=level;self.pages=[]
 def page(self):
  if self.pages:self.end()
  self.p=[r'\null\begin{tikzpicture}[remember picture,overlay]',r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]',r'\begin{scope}[shift={(1.5,1.5)}]'];self.pages.append(None)
  self.text(0,-.5,18.5,'Week 36 / Making threes / '+self.level,11)
  self.text(0,24.7,17,'Bellingham Math Circle / Week 36 / W36-'+self.name+'-v2',10)
  self.text(18,24.7,.5,str(len(self.pages)),10)
 def text(self,x,y,w,t,s=15):self.p.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')
 def problem(self,n,t,y=.5):self.text(0,y,18.4,r'\textbf{Problem '+str(n)+':} '+t,17 if self.name=='k-1' else 15)
 def end(self):self.pages[-1]='\n'.join(self.p)+r'\end{scope}\end{scope}\end{tikzpicture}'
 def save(self):self.end();(SRC/(self.name+'.tex')).write_text(PRE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

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
def demo(p):
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
def pairs(p):
 for x,y,pair in [(.3,12.3,[(0,0),(0,1)]),(10.05,12.3,[(0,0),(1,0)]),(.3,18.2,[(0,1),(1,2)]),(10.05,18.2,[(1,1),(2,0)])]:
  for j,(a,b) in enumerate(pair):tile(p,x+1.1+2.75*j,y,a,b,2.2)
  tile(p,x+7,y,None,None,2.2)
  p.p.append(f'\\draw[-{{Stealth}}] ({x+5.05},{y}) -- ({x+5.68},{y});')
def mat(p,y=4.8,shown=False):
 for i in range(4):
  p.p.append(f'\\draw[gray!65] (.2,{y+6*i}) -- (18.2,{y+6*i});')
  p.p.append(f'\\draw[gray!65] ({.2+6*i},{y}) -- ({.2+6*i},{y+18});')
 if shown:
  for a in range(3):
   for b in range(3):tile(p,3.2+6*b,y+3+6*a,a,b,3.5,False)
def mini(p,x,y,sel=()):
 for a in range(3):
  for b in range(3):
   tile(p,x+1.1+2.35*b,y+1.1+2.35*a,a,b,2.2)
   if (a,b) in sel:p.p.append(f'\\draw[line width=1.2pt] ({x+1.1+2.35*b},{y+1.1+2.35*a}) circle (1.05);')

rules='Use the nine tiles, one of each shape and fill. An allowed three uses three different tiles. Its shapes are all the same or all different. Its fills are also all the same or all different. Tile positions do not matter.'
for name,level in [('k-1','K--1'),('grades-2-3','Grades 2--3'),('grades-4-5','Grades 4--5')]:
 p=Packet(name,level);p.page();p.text(0,.3,18.4,rules,14);demo(p)
 if name=='k-1':
  p.problem(1,'Pick a third tile for each pair to make an allowed three. Then give your partner new pairs.',9);pairs(p)
  p.page();p.problem(2,'Put all nine tiles into three allowed threes. Find different ways.');mat(p)
  p.page();p.problem(3,'Choose tiles without making any allowed three. How many can you keep?');mat(p,shown=True)
  p.page();p.problem(4,'Choose one tile and keep it in the middle of the table. Find all allowed threes using it; then try other middle tiles.');mat(p)
 elif name=='grades-2-3':
  p.problem(1,'Complete each pair to make an allowed three. Choose other pairs to give your partner; can any pair have two different answers?',9);pairs(p)
  p.page();p.problem(2,'Split all nine tiles into three allowed threes. Find different splits; changing the order of the same three groups does not make a new split.');mat(p)
  p.page();p.problem(3,'Choose as many tiles as you can with no allowed three among them. Can you change one chosen tile and then add another?');mat(p,shown=True)
  p.page();p.problem(4,'Choose one tile. Find all the allowed threes that use it, and explain why you have them all.');mini(p,.4,4.2);mini(p,10.3,4.2)
  p.problem(5,'Start with no tiles chosen. Take turns adding an unused tile to the same collection without making an allowed three. The first player who cannot move loses. Can your choices change how many moves the game lasts?',13.1);mini(p,.4,16);mini(p,10.3,16)
 else:
  p.problem(1,'Complete the pairs. Explain why any two different tiles have exactly one tile that completes an allowed three.',9);pairs(p)
  p.page();p.problem(2,'Choose as many tiles as possible without an allowed three among them. Explain why a larger collection is impossible.');mat(p,shown=True)
  p.page();p.problem(3,'Two different allowed threes may share a tile. How many tiles can they share? Find as many allowed threes through one chosen tile as possible, and explain why you have them all.');mini(p,.4,4.2);mini(p,10.3,4.2)
  p.page();p.problem(4,'Split the nine tiles into three allowed threes. Find every split, and explain why your list is complete.');mini(p,.4,4.2);mini(p,10.3,4.2);mini(p,.4,14);mini(p,10.3,14)
  p.page();p.problem(5,'Start with no tiles chosen. Add one unused tile at a time without making an allowed three. Can different choices make you stop at different numbers of tiles? Explain why you can or cannot get stuck early.');mat(p)
 p.save()

pts=list(itertools.product(range(3),repeat=2))
def ok(t):return all(len({p[k] for p in t}) in [1,3] for k in [0,1])
lines=[tuple(t) for t in itertools.combinations(pts,3) if ok(t)]
def cap(t):return not any(set(l)<=set(t) for l in lines)
caps={n:sum(cap(t) for t in itertools.combinations(pts,n)) for n in [3,4,5]}
parts=[ls for ls in itertools.combinations(lines,3) if len(set().union(*map(set,ls)))==9]
assert len(lines)==12 and caps[4]==54 and caps[5]==0 and len(parts)==4
# Every maximal legal collection has four tiles; no arbitrary tile ban is used.
maximal_sizes=[]
for n in range(10):
 for t in itertools.combinations(pts,n):
  if cap(t) and not any(cap(t+(p,)) for p in pts if p not in t):maximal_sizes.append(n)
assert set(maximal_sizes)=={4}
(SRC/'mathematical-checks.json').write_text(json.dumps({'lines':lines,'line_free_counts':caps,'partitions_into_three_lines':parts,'maximal_legal_collection_sizes':sorted(set(maximal_sizes))},indent=2))
