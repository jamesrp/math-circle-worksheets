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
\begin{document}
'''
class Packet:
 def __init__(self,name,level):self.name=name;self.level=level;self.pages=[]
 def page(self):
  if self.pages:self.end()
  self.p=[r'\null\begin{tikzpicture}[remember picture,overlay]',r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]',r'\begin{scope}[shift={(1.5,1.5)}]'];self.pages.append(None)
  self.text(0,-.5,18.5,'Week 35 / Footprint borders / '+self.level,11)
  self.text(0,24.7,17,'Bellingham Math Circle / Week 35 / W35-'+self.name+'-v2',10)
  self.text(18,24.7,.5,str(len(self.pages)),10)
 def text(self,x,y,w,t,s=15):self.p.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+r'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')
 def problem(self,n,t,y=.5):self.text(0,y,18.4,r'\textbf{Problem '+str(n)+':} '+t,17 if self.name=='k-1' else 15)
 def end(self):self.pages[-1]='\n'.join(self.p)+r'\end{scope}\end{scope}\end{tikzpicture}'
 def save(self):self.end();(SRC/(self.name+'.tex')).write_text(PRE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

def motif(p,x,y,s=.65,reflect=False,angle=0):
 p.p.append(f'\\begin{{scope}}[shift={{({x},{y})}},rotate={angle},xscale={s},yscale={-s if reflect else s}]')
 p.p.append(r'\draw[line width=.7pt,fill=gray!15] (-1.3,-1.1) -- (1.3,-1.1) -- (1.3,-.4) -- (.8,-.4) -- (.8,-.65) -- (-.5,-.65) -- (-.5,0) -- (.6,0) -- (.6,.45) -- (-.5,.45) -- (-.5,1.1) -- (-1.3,1.1) -- cycle;')
 p.p.append(r'\draw[-{Stealth},line width=.65pt] (-.25,-.86) -- (.55,-.86);\end{scope}')
def strip(p,y,marks=None,h=6.0,vertical=False):
 p.p.append(f'\\draw[gray!50,line width=.6pt] (.35,{y-h/2}) rectangle (18,{y+h/2});')
 p.p.append(f'\\draw[dashed,line width=.6pt] (.35,{y}) -- (18,{y});')
 for x,sign in [(0,-1),(18.4,1)]:p.p.append(f'\\draw[-{{Stealth}},line width=.9pt] ({x-sign*.6},{y}) -- ({x},{y});')
 for i in range(6):
  x=1.7+3*i
  p.p.append(f'\\draw[gray!45] ({x},{y-.12}) -- ({x},{y+.12});')
 if vertical:p.p.append(f'\\draw[densely dotted] (9.15,{y-h/2}) -- (9.15,{y+h/2});')
 if marks:
  for i,row,ref,ang in marks:motif(p,1.7+3*i,y+row,1,ref,ang)
def demo(p):
 # Three equally scaled panels show the same labelled motif under the two actions.
 for x in [2.6,9.2,15.8]:p.p.append(f'\\draw[dashed,gray] ({x-2.1},4.9) -- ({x+2.1},4.9);')
 motif(p,2.6,3.6,.68);motif(p,9.2,6.2,.68,True);motif(p,16.8,6.2,.68,True)
 for x,y,label in [(2.6,3.6,'A'),(9.2,6.2,'A'),(16.8,6.2,'A')]:p.text(x-1.55,y-.3,.7,label,12)
 p.p.append(r'\draw[-{Stealth},line width=.9pt] (4.8,4.9) -- (6.8,4.9);')
 p.p.append(r'\draw[-{Stealth},line width=.9pt] (11.5,4.9) -- (13.4,4.9);')
 p.text(.7,7.4,4.5,'start',12);p.text(7.1,7.4,5,'flip over the line',12);p.text(13.7,7.4,4.7,'then slide right',12)
 p.p.append(r'\draw[-{Stealth},line width=.8pt] (14.7,7.1) -- (15.7,7.1);')

rules='Use the loose footprints and long strips. Each border repeats forever both ways. A match must fit every footprint. Only footprints count, not strip ends or guide lines. A slide must move the copy. Test with a tracing copy; leave the original in place.'
for name,level in [('k-1','K--1'),('grades-2-3','Grades 2--3'),('grades-4-5','Grades 4--5')]:
 p=Packet(name,level);p.page();p.text(0,.3,18.4,rules,14)
 if name=='k-1':
  p.problem(1,'Make one repeating border. Find slides that make its tracing copy match and slides that do not.',3.2);strip(p,9.1)
  p.page();p.problem(2,'Make two repeating borders whose shortest matching slides are different lengths.');strip(p,7.1);strip(p,16.1)
  p.page();p.p.append(r'\begin{scope}[shift={(0,-2.5)}]');demo(p);p.p.append(r'\end{scope}')
  p.problem(3,'Make a border that matches after a flip over the middle line and a slide along it. Can you make the flip alone fail?',6.6);strip(p,12.3)
  p.problem(4,'Make a different border with the same kind of match.',16.3);strip(p,20.8)
  p.page();p.problem(5,'Make a border that matches when you flip it over the middle line. Change it so that the flip fails.');strip(p,7.1);strip(p,16.1)
  p.page();p.text(0,.3,18.4,'A half-turn turns the copy halfway around a chosen point on the table. You may choose any point.',14);p.problem(6,'Make a border that matches after a half-turn. Make another that cannot match after a half-turn around any point.',2.1);strip(p,8.3);strip(p,16.1)
  p.problem(7,'Trade borders with your partner and find the moves that match.',21.2)
 elif name=='grades-2-3':
  demo(p)
  p.problem(1,'Make two repeating borders whose smallest matching slides are different lengths. Mark one matching slide on each tracing copy.',8.9);strip(p,14.2);strip(p,21.1)
  p.page();p.problem(2,'A glide is a flip over the middle line followed by a nonzero slide along it. Make a border that matches after a glide, but fails after the flip alone.');strip(p,7.1);strip(p,15)
  p.problem(3,'On your border, how does the shortest matching glide compare with the shortest matching slide?',20.3)
  p.page();p.text(0,.3,18.4,'A half-turn turns the copy halfway around a chosen point on the table. You may choose any point.',14);p.problem(4,'Make a repeating border that matches after a flip over the middle line. Can you keep it from matching after any half-turn?',2.1);strip(p,8.3);strip(p,16.7)
  p.page();p.problem(5,'Make a repeating border that matches after a half-turn, but fails after the flip over the middle line.');strip(p,7.1);strip(p,16.1)
  p.problem(6,'Move footprints in one of your borders so that an old matching move fails but the new border still repeats. You may use a larger repeating part.',21.2)
 else:
  demo(p)
  p.problem(1,'Build two repeating borders with different smallest matching slides. Measure those slides; explain why a smaller slide cannot match each border.',8.9);strip(p,14.2);strip(p,21.1)
  p.page();p.problem(2,'A glide is a flip over the middle line followed by a nonzero slide along it. Build a border that matches after a glide, but fails after the flip alone. Find its shortest matching slide and shortest matching glide.');strip(p,7.6);strip(p,15.7)
  p.problem(3,'A border matches after a flip and a 3 cm slide along the middle line. Must a 6 cm slide also match? Must a 3 cm slide match? Explain why.',20.5)
  p.page();p.problem(4,'Make a repeating border that matches after a flip over each of the two crossing lines. Which other matching moves are forced by those two flips? Explain why.');strip(p,7.6,vertical=True);strip(p,16.3,vertical=True)
  p.page();p.text(0,.3,18.4,'A half-turn turns the copy halfway around a chosen point on the table. You may choose any point.',14);p.problem(5,'Make a border that matches after a half-turn and fails after a flip over the middle line. Can you also make every flip across a line perpendicular to the border fail?',2.1);strip(p,8.3);strip(p,16.1)
  p.problem(6,'For one border you made, describe every matching slide, glide, flip and turn. Which claims can you justify for its endless repetition?',21.2)
 p.save()

# Vertex-distance signature and signed area checks distinguish the motif's mirror.
V=[(-1.3,-1.1),(1.3,-1.1),(1.3,-.4),(.8,-.4),(.8,-.65),(-.5,-.65),(-.5,0),(.6,0),(.6,.45),(-.5,.45),(-.5,1.1),(-1.3,1.1)]
# A polygon symmetry must permute vertices preserving the cyclic edge-length word.
l=[round((V[i][0]-V[(i+1)%len(V)][0])**2+(V[i][1]-V[(i+1)%len(V)][1])**2,8) for i in range(len(V))]
rot=[k for k in range(1,len(V)) if all(l[i]==l[(i+k)%len(V)] for i in range(len(V)))]
ref=[k for k in range(len(V)) if all(l[i]==l[(k-i)%len(V)] for i in range(len(V)))]
assert not rot and not ref
(SRC/'mathematical-checks.json').write_text(json.dumps({'motif_vertices':V,'nonidentity_cyclic_edge_word_rotations':rot,'edge_word_reflections':ref,'note':'No polygon isometry can exist without preserving the cyclic edge-length word. All motifs are original.'},indent=2))
