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
  self.text(0,-.5,18.5,'Week 34 / Hidden turns / '+self.level,11)
  self.text(0,24.7,17,'Bellingham Math Circle / Week 34 / W34-'+self.name+'-v2',10)
  self.text(18,24.7,.5,str(len(self.pages)),10)
 def text(self,x,y,w,t,s=15):self.p.append(r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+r'cm,font=\sffamily\fontsize{'+str(s)+'}{'+str(s*1.25)+'}\selectfont] at ('+str(x)+','+str(y)+') {'+t+'};')
 def problem(self,n,t,y=.5):self.text(0,y,18.4,r'\textbf{Problem '+str(n)+':} '+t,17 if self.name=='k-1' else 15)
 def ring(self,x,y,n,R=7,spot=1.4,vals=None):
  # Blank unlabelled positions have no printed home tick.
  self.p.append(f'\\draw[gray!45,line width=.5pt] ({x},{y}) circle ({R});')
  for i in range(n):
   a=2*math.pi*i/n-math.pi/2;xx=x+R*math.cos(a);yy=y+R*math.sin(a)
   self.p.append(f'\\draw[line width=1pt,fill=white] ({xx:.5f},{yy:.5f}) circle ({spot});')
   if vals is not None:self.symbol(xx,yy,vals[i],spot*.45)
 def symbol(self,x,y,v,s=.25):
  if v==0:self.p.append(f'\\fill ({x},{y}) circle ({s});')
  elif v==1:self.p.append(f'\\draw[line width=1pt] ({x},{y}) circle ({s});')
  elif v==2:self.p.append(f'\\draw[line width=1pt] ({x-s},{y-s}) rectangle ({x+s},{y+s});')
 def line(self,y):self.p.append(f'\\draw[gray!40] (0,{y}) -- (18.3,{y});')
 def demo(self):
  for x,v,label in [(2.7,[0,1,0,1],'start'),(9.1,[0,1,0,1],'turn 2 spots: match'),(15.5,[1,0,1,0],'turn 1 spot: no match')]:
   self.ring(x,3.9,4,1,.37,v);self.text(x-2.5,5.4,5,label,12)
  for x in [4.25,10.6]:self.p.append(f'\\draw[-{{Stealth}},line width=1pt] ({x},3.9) -- ({x+2.8},3.9);')
 def end(self):self.pages[-1]='\n'.join(self.p)+r'\end{scope}\end{scope}\end{tikzpicture}'
 def save(self):self.end();(SRC/(self.name+'.tex')).write_text(PRE+'\n\\newpage\n'.join(self.pages)+'\n\\end{document}\n')

rules='Fill every spot. Only counter kinds and spots count; the direction of a symbol does not. Keep the original still. Turn or turn over its tracing copy until all spots line up. A whole turn does not count.'
for name,level in [('k-1','K--1'),('grades-2-3','Grades 2--3'),('grades-4-5','Grades 4--5')]:
 p=Packet(name,level);p.page();p.text(0,.25,18.4,rules,14 if name=='k-1' else 13);p.demo()
 if name=='k-1':
  p.problem(1,'Make different patterns on this ring with two kinds of counter. Let your partner find turns or flips that match.',6.2);p.ring(9.2,16,3)
  p.page();p.problem(2,'Make a pattern on this ring that no turn or flip can hide. How few kinds of counter can you use?');p.ring(9.2,13,4);p.problem(3,'Change just one counter in different ways. Find changes that allow a matching turn or flip and changes that do not.',21.8)
  p.page();p.problem(4,'Can two kinds of counter stop every turn and flip on this ring? Try three kinds too.');p.ring(9.2,13,5)
  p.page();p.problem(5,'Make a pattern with two kinds of counter that no turn or flip can hide. Let your partner test it.');p.ring(9.2,13,6)
  p.page();p.problem(6,'Build two two-kind patterns that no turn or flip can hide and that cannot match each other. Keep each on its own tracing copy.');p.ring(9.2,13,8)
 elif name=='grades-2-3':
  p.problem(1,'Find how few kinds of counter can stop every turn and flip on this ring. Use up to three kinds; neighbors may match.',6.2);p.ring(9.2,16,3)
  p.page();p.problem(2,'Find how few kinds of counter can stop every turn and flip on this ring. Let someone test your best pattern.');p.ring(9.2,13,4);p.line(22.5);p.line(24)
  p.page();p.problem(3,'Find how few kinds of counter can stop every turn and flip on this ring. Can you explain why fewer kinds would fail?');p.ring(9.2,13,5);p.line(23);p.line(24.1)
  p.page();p.problem(4,'Find a six-ring pattern using only two kinds of counter that stops every turn and flip. Show how you know every possible move fails.');p.ring(9.2,13,6);p.line(23);p.line(24.1)
  p.page();p.problem(5,'Find an eight-ring pattern with two kinds of counter that stops every turn and flip. How few counters of one kind can it have?');p.ring(9.2,13,8);p.line(23);p.line(24.1)
 else:
  p.problem(1,'Find the fewest kinds of counter that stop every turn and flip on the three-ring. Neighbors may match. Can you rule out every pattern with fewer kinds?',6.2);p.ring(9.2,16,3)
  p.page();p.problem(2,'Find the fewest kinds of counter that stop every turn and flip on the four-ring. Explain why fewer kinds cannot work.');p.ring(9.2,13,4);p.line(23);p.line(24.1)
  p.page();p.problem(3,'Find the fewest kinds of counter that stop every turn and flip on the five-ring. Find an explanation that also works for the three-ring and four-ring.');p.ring(9.2,13,5);p.line(23);p.line(24.1)
  p.page();p.problem(4,'Use two kinds of counter to stop every turn and flip on this six-ring. Explain why no turn or flip can match it.');p.ring(9.2,13,6);p.line(23);p.line(24.1)
  p.page();p.problem(5,'Can you make a two-kind pattern that stops every turn and flip on any ring with at least six spots? Test your idea on this eight-ring, then explain why it always works.');p.ring(9.2,13,8);p.line(23);p.line(24.1)
 p.save()

def surviving(w):
 n=len(w);return [('turn',k) for k in range(1,n) if all(w[i]==w[(i+k)%n] for i in range(n))]+[('flip',k) for k in range(n) if all(w[i]==w[(k-i)%n] for i in range(n))]
checks={}
for n in range(3,11):
 c=next(q for q in [1,2,3] if any(not surviving(w) for w in itertools.product(range(q),repeat=n)))
 witness=[int(i in [0,1,3]) for i in range(n)]
 checks[n]={'minimum_kinds':c,'013_binary_asymmetric':not surviving(witness)}
assert [checks[n]['minimum_kinds'] for n in range(3,11)]==[3,3,3,2,2,2,2,2]
(SRC/'mathematical-checks.json').write_text(json.dumps(checks,indent=2))
