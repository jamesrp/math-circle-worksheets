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
  self.text(0,-.5,18.5,'Week 37 / Mirror twins / '+self.level,11)
  self.text(0,24.7,17,'Bellingham Math Circle / Week 37 / W37-'+self.name+'-v2',10)
  self.text(18,24.7,.5,str(len(self.pages)),10)
 def text(self,x,y,w,t,s=15):self.p.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')
 def problem(self,n,t,y=.5):self.text(0,y,18.4,r'\textbf{Problem '+str(n)+':} '+t,17 if self.name=='k-1' else 15)
 def end(self):self.pages[-1]='\n'.join(self.p)+r'\end{scope}\end{scope}\end{tikzpicture}'
 def save(self):self.end();(SRC/(self.name+'.tex')).write_text(PRE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

COL={'A':'blue!12','B':'orange!22','C':'green!18','D':'violet!20','':'white'}
def badge(p,x,y,lab,s=.46):
 # Letters, in addition to distinct tints, identify all markers in grayscale.
 p.p.append(f'\\node[circle,draw,line width=.9pt,fill={COL.get(lab,"white")},minimum size={2*s}cm,inner sep=0,font=\\sffamily\\bfseries\\fontsize{{15}}{{17}}\\selectfont] at ({x},{y}) {{{lab}}};')
def tetra(p,x,y,labels=('A','B','C','D'),s=1):
 # Exact orthographic projection of a regular tetrahedron.
 # World A=(0,0,sqrt(2/3)), B=(-1/2,-sqrt(3)/6,0),
 # C=(1/2,-sqrt(3)/6,0), D=(0,sqrt(3)/3,0).
 # Horizontal = X; vertical = -Z - 0.55 Y (up to an overall scale).
 L=5*s; q=math.sqrt(1+.55**2)
 coords=[(x,y-L*math.sqrt(2/3)/q),(x-L*.5,y+L*.55*math.sqrt(3)/(6*q)),(x+L*.5,y+L*.55*math.sqrt(3)/(6*q)),(x,y-L*.55*math.sqrt(3)/(3*q))]
 for i,j in [(0,3),(1,3),(2,3)]:
  a,b=coords[i],coords[j];p.p.append(f'\\draw[dashed,line width=.9pt,gray!75] ({a[0]},{a[1]}) -- ({b[0]},{b[1]});')
 for i,j in [(0,1),(0,2),(1,2)]:
  a,b=coords[i],coords[j];p.p.append(f'\\draw[line width=1.15pt] ({a[0]},{a[1]}) -- ({b[0]},{b[1]});')
 for (xx,yy),l in zip(coords,labels):badge(p,xx,yy,l,.45 if s>=.8 else .34)
 return coords

def pair(p,y=9,left=('A','B','C','D'),right=('A','C','B','D'),mirror=True,s=1.1):
 tetra(p,4.3,y,left,s);tetra(p,14.1,y,right,s)
 if mirror:
  p.p.append(f'\\draw[gray!55,line width=2pt] (9.2,{y-5.4*s}) -- (9.2,{y+1.2*s});')
  p.text(8.45,y+1.6*s,2,'mirror',11)

def turn_demo(p):
 tetra(p,4.0,8.15,('A','B','C','D'),1.03);tetra(p,14.4,8.15,('A','D','B','C'),1.03)
 p.p.append(r'\draw[-{Stealth},line width=1pt] (7.4,6.1) to[bend left=25] (11,6.1);')
 p.text(7.35,6.7,3.9,'turn around A',12)
 p.text(1.3,10,5.5,'before the turn',12);p.text(11.7,10,5.8,'after the turn',12)

def topview(p,x,y,labels=('B','C','D'),s=1):
 # As seen from A toward the opposite face: B left, C right, D far/top.
 vs=[(x-2.3*s,y+1.3*s),(x+2.3*s,y+1.3*s),(x,y-2.6*s)]
 for i in range(3):
  u,v=vs[i],vs[(i+1)%3];p.p.append(f'\\draw[line width=1pt] ({u[0]},{u[1]}) -- ({v[0]},{v[1]});')
 for u in vs:p.p.append(f'\\draw[gray!55,line width=.6pt] ({x},{y}) -- ({u[0]},{u[1]});')
 for u,lab in zip(vs,labels):badge(p,*u,lab,.43)
 badge(p,x,y,'A',.4)
 p.text(x-1.6,y+2.1*s,3.7,'A nearest you',11)

def lines(p,ys):
 for y in ys:p.p.append(f'\\draw[gray!40] (0,{y}) -- (18.3,{y});')

rules='Use the rigid models. Move and turn them so same-letter corners match. Which way a letter points does not count. Keep the markers fixed unless a problem says to change them. Dashed edges pass behind the front face.'
for name,level in [('k-1','K--1'),('grades-2-3','Grades 2--3'),('grades-4-5','Grades 4--5')]:
 p=Packet(name,level);p.page();p.text(0,.3,18.4,rules,14);turn_demo(p)
 if name=='k-1':
  p.problem(1,'Make two models like the first picture. Hide and turn one, then let your partner turn it back to match.',12)
  tetra(p,4.3,21.1,('A','B','C','D'),1);tetra(p,14.1,21.1,('A','B','C','D'),1)
  p.page();p.problem(2,'Build this pair with your adult. Can you turn the models to match every letter?');pair(p,10.5)
  p.page();p.problem(3,'Change D to C on both models from Problem 2. Can you turn them to match now?');pair(p,10.5,('A','B','C','C'),('A','C','B','C'),False)
  p.page();p.problem(4,'Put A, A, B and C on each frame. Can your partner make a pair that you cannot turn to match?');pair(p,10.5,('A','A','B','C'),('A','B','A','C'),False)
  p.problem(5,'Use A, B, C and D again. Make one pair that matches and one pair that you think cannot match.',17.4)
 elif name=='grades-2-3':
  p.problem(1,'Build two copies of the first model. Take turns hiding and rotating one model, then matching all four letters again.',12)
  tetra(p,4.3,21.1,('A','B','C','D'),1);tetra(p,14.1,21.1,('A','B','C','D'),1)
  p.page();p.problem(2,'Build this model and its mirror twin. Can you match every letter by moving and turning one of them? If no turn has worked, does that mean no turn can work?');pair(p,10.5)
  p.problem(3,'Make another pair with A, B, C and D. Can you match the two models by turning?',18)
  p.page();p.problem(4,'Change D to C on both models from Problem 2 and test for a match. Try other choices of two letters to make equal; start each trial with the original A, B, C, D mirror pair.');pair(p,10.5,('A','B','C','C'),('A','C','B','C'),False)
  p.page();p.problem(5,'Use A, A, B and C on each frame. Find out whether your partner can make a pair that will not match by turning.');pair(p,10.5,('A','A','B','C'),('A','B','A','C'),False)
  p.problem(6,'Change one A on each model to D. Can you choose the changes to make a matching pair? Can you choose them to make a pair that will not match?',18)
 else:
  p.problem(1,'Build two copies of the first model. Turn one without changing any labels, and challenge a partner to match it. What has to match besides the letter at the top?',12)
  tetra(p,4.3,21.1,('A','B','C','D'),1);tetra(p,14.1,21.1,('A','B','C','D'),1)
  p.page();p.problem(2,'Build the model and its mirror twin. Can one be moved and turned to match the other? Seek a reason that settles this even if no more turns are tried.');pair(p,10.5);lines(p,[17,19,21,23])
  p.page();p.problem(3,'Look straight from A toward the center of the opposite face, with A nearest your eye. Use this view of both models from Problem 2 to explain whether any turn can match them.');tetra(p,4.1,10.1,('A','B','C','D'),1.05);topview(p,14.4,8.2)
  p.p.append(r'\draw[-{Stealth},line width=1pt] (7.1,8.2) -- (11.1,8.2);')
  p.text(6.8,9.0,4.7,r'look from A\\toward face BCD',12)
  p.text(1.5,12.2,5.8,'model',12);p.text(11.8,12.2,5.5,'view from A',12)
  topview(p,4.4,18.5,('','',''),.75);topview(p,14.1,18.5,('','',''),.75)
  lines(p,[23.4])
  p.page();p.problem(4,'Choose two letters in the mirror pair and make them equal on both models. Start each trial with the original A, B, C, D mirror pair. Which choices allow a match by turning? Explain why your conclusion covers every choice.');pair(p,10.5,('A','B','C','C'),('A','C','B','C'),False);lines(p,[17,19,21,23])
  p.page();p.problem(5,'How many rotations put a bare regular tetrahedral frame back onto the same four positions? Count leaving it still as one. Turns count as the same when every starting corner ends at the same destination. Explain why your count is complete.');tetra(p,9.2,11,('','','',''),1.35)
  p.problem(6,'Put four different letters on the frame. How many genuinely different models can be made if models that match by turning count as the same? Explain.',17.2);lines(p,[21,23])
 p.save()

# Exact integer regular tetrahedron: all six squared distances are 8.
V=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def orient(q):return det(*[tuple(V[q[i]][j]-V[q[0]][j] for j in range(3)) for i in [1,2,3]])
base=orient((0,1,2,3));rots=[q for q in itertools.permutations(range(4)) if orient(q)==base]
def equivalent(a,b):return any(all(a[i]==b[q[i]] for i in range(4)) for q in rots)
assert len(rots)==12
assert equivalent('ABCD','ADBC')
assert not equivalent('ABCD','ACBD')
assert equivalent('ABCC','ACBC')
assert equivalent('AABC','ABAC')
repeated={}
for i,j in itertools.combinations('ABCD',2):
 a='ABCD'.replace(j,i);b='ACBD'.replace(j,i);repeated[i+j]=equivalent(a,b)
assert all(repeated.values())
(SRC/'mathematical-checks.json').write_text(json.dumps({'regular_integer_vertices':V,'proper_rotations':rots,'proper_rotation_count':12,'true_copy_example':['ABCD','ADBC'],'mirror_pair_not_rotation_equivalent':['ABCD','ACBD'],'repeated_label_pair_equivalent':['ABCC','ACBC'],'all_label_merges_remove_this_pair_chirality':repeated,'physical_pretest_performed':False},indent=2))
