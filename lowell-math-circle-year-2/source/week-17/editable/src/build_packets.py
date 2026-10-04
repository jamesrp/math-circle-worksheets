from pathlib import Path
ROOT=Path(__file__).resolve().parent
PRE=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{tikz}
\usepackage{amssymb,amsmath}
\pdfmapfile{+lm.map}
\pdfmapfile{+symbols.map}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\definecolor{cardred}{RGB}{203,45,45}
\definecolor{cardblue}{RGB}{34,95,176}
\tikzset{state/.style={circle,draw=black,line width=1.1pt,minimum size=.66in,inner sep=0pt,font=\sffamily\bfseries\fontsize{13}{14}\selectfont},edge/.style={-{Stealth[length=7pt,width=5pt]},line width=1.15pt},lab/.style={fill=white,inner sep=2pt,font=\sffamily\bfseries\fontsize{12}{13}\selectfont}}
\newcommand{\R}{\tikz[baseline=-.045in,x=1in,y=1in]{\node[draw=cardred,fill=cardred!10,rectangle,minimum size=.23in,inner sep=0pt,line width=.85pt,text=black,font=\sffamily\bfseries\fontsize{11}{12}\selectfont] {R};}}
\newcommand{\B}{\tikz[baseline=-.045in,x=1in,y=1in]{\node[draw=cardblue,fill=cardblue!10,circle,minimum size=.23in,inner sep=0pt,line width=.85pt,text=black,font=\sffamily\bfseries\fontsize{11}{12}\selectfont] {B};}}
\newcommand{\Y}{$\checkmark$}
\newcommand{\N}{$\times$}
\begin{document}
'''
class Packet:
 def __init__(self,band,pid): self.band=band; self.pid=pid; self.parts=[PRE]; self.n=0
 def page(self):
  if self.n: self.parts.append('\\end{tikzpicture}\\null\\newpage\n')
  self.n+=1
  self.parts.append(r'\begin{tikzpicture}[remember picture,overlay,x=1in,y=-1in,shift={(current page.north west)}]'+'\n')
  self.text(.6,.34,7.3,rf'Week 17 / Machine memory / {self.band}',11,13)
  self.parts.append(r'\draw[line width=.45pt] (.6,.66)--(7.9,.66);'+'\n')
  self.text(.6,10.49,6.8,f'Bellingham Math Circle / Week 17 / {self.pid}',9,11)
  self.text(7.55,10.49,.35,str(self.n),9,11)
 def text(self,x,y,w,s,size=14,leading=None):
  leading=leading or size*1.25
  self.parts.append(rf'\node[anchor=north west,inner sep=0pt,align=left,text width={w}in,font=\sffamily\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n')
 def problem(self,n,s,y=.96,size=15): self.text(.65,y,7.2,rf'\textbf{{Problem {n}:}} {s}',size)
 def line(self,x,y,w): self.parts.append(rf'\draw[black!38,line width=.45pt] ({x},{y})--({x+w},{y});'+'\n')
 def cards(self,word,x,y,step=.35,size=.28):
  if not word: self.text(x,y-.14,1.2,'no cards',12,14); return
  for j,c in enumerate(word):
   shape='rectangle' if c=='R' else 'circle'; color='cardred' if c=='R' else 'cardblue'
   self.parts.append(rf'\node[draw={color},fill={color}!10,{shape},minimum size={size}in,inner sep=0pt,line width=.9pt,font=\bfseries\fontsize{{12}}{{13}}\selectfont] at ({x+j*step},{y}) {{{c}}};'+'\n')
 def blank_cards(self,x,y,n=6,size=.42,step=.54):
  for j in range(n): self.parts.append(rf'\draw[black!35,line width=.6pt,rounded corners=1.5pt] ({x+j*step-size/2},{y-size/2}) rectangle ++({size},{size});'+'\n')
 def choices(self,x,y):
  self.parts.append(rf'\node[font=\fontsize{{22}}{{24}}\selectfont] at ({x},{y}) {{\Y}};\node[font=\fontsize{{22}}{{24}}\selectfont] at ({x+.65},{y}) {{\N}};'+'\n')
 def state(self,name,x,y,answer,k=False,blank=False,label=None):
  a='' if blank else ((r'\Y' if answer else r'\N') if k else ('YES' if answer else 'NO'))
  if label: a=rf'\shortstack{{{{\fontsize{{9}}{{10}}\selectfont {label}}}\\{a}}}'
  self.parts.append(rf'\node[state] ({name}) at ({x},{y}) {{{a}}};'+'\n')
 def two(self,kind,x1,x2,y,k=False,prefix='s',labels=False):
  # even: red toggles and blue loops. lastR/lastB: each symbol sets the current answer.
  if kind=='even': answers=[True,False]; forward='R'; backward='R'; loops=['B','B']
  elif kind=='lastR': answers=[False,True]; forward='R'; backward='B'; loops=['B','R']
  elif kind=='lastB': answers=[False,True]; forward='B'; backward='R'; loops=['R','B']
  for i,(x,a) in enumerate(zip([x1,x2],answers)): self.state(prefix+str(i),x,y,a,k,label=str(i+1) if labels else None)
  self.parts.append(rf'\draw[edge] ({x1-.95},{y})--({prefix}0.west);'+'\n')
  for i,l in enumerate(loops): self.parts.append(rf'\draw[edge] ({prefix}{i}) edge[loop above,min distance=.57in] node[lab] {{\{l}}} ({prefix}{i});'+'\n')
  self.parts.append(rf'\draw[edge] ({prefix}0) to[bend left=24] node[lab,above] {{\{forward}}} ({prefix}1);'+'\n')
  self.parts.append(rf'\draw[edge] ({prefix}1) to[bend left=24] node[lab,below] {{\{backward}}} ({prefix}0);'+'\n')
 def three(self,y,k=False,prefix='t',xs=(2.0,4.25,6.5),labels=False):
  for i,x in enumerate(xs): self.state(prefix+str(i),x,y,i==0,k,label=str(i+1) if labels else None)
  self.parts.append(rf'\draw[edge] ({xs[0]-.95},{y})--({prefix}0.west);'+'\n')
  for i in range(3): self.parts.append(rf'\draw[edge] ({prefix}{i}) edge[loop above,min distance=.56in] node[lab] {{\B}} ({prefix}{i});'+'\n')
  for i in range(2): self.parts.append(rf'\draw[edge] ({prefix}{i})--node[lab,above] {{\R}} ({prefix}{i+1});'+'\n')
  self.parts.append(rf'\draw[edge] ({prefix}2.south) .. controls ({xs[2]},{y+1.03}) and ({xs[0]},{y+1.03}) .. node[lab,below] {{\R}} ({prefix}0.south);'+'\n')
 def pair(self,a,b,y,k=False):
  if k:
   self.parts.append(rf'\draw[black!45,line width=.6pt] (.8,{y-.22})--(.72,{y-.22})--(.72,{y+.72})--(.8,{y+.72});'+'\n')
   for word,yy in [(a,y),(b,y+.48)]:
    self.cards(word,1.25,yy)
    self.text(3.25,yy-.13,.3,'+',18,19)
    self.line(3.75,yy+.15,2.65)
    self.choices(7.03,yy)
  else:
   for word,x in [(a,.9),(b,4.5)]:
    self.cards(word,x,y,step=.31,size=.25)
    self.text(x+1.35,y-.13,.25,'+',15,16)
    self.line(x+1.75,y+.12,1.3)
    self.text(x+1.7,y+.3,1.5,'YES / NO',10.5,12)
   self.line(.9,y+.85,6.8)
 def finish(self,path):
  self.parts.append('\\end{tikzpicture}\\null\n\\end{document}\n'); (ROOT/path).write_text(''.join(self.parts))

k=Packet('K--1','W17-K-v2')
k.page()
k.text(.65,.88,7.2,r'Start at the small arrow with one marker. Read left to right. Follow one matching arrow for each card, then hide the card. Each circle has one arrow for each kind of card and a fixed \Y\ or \N.',12.5,16)
k.problem(1,r'Try each row, starting fresh each time, and circle its answer. Make three different six-card rows that finish at \Y.',1.78,16)
k.two('even',2.6,5.9,3.47,True,labels=True)
k.text(.8,4.14,6.9,r'Example B R: start 1 $\xrightarrow{\ B\ }$ 1 $\xrightarrow{\ R\ }$ 2; stop at $\times$.',12,15)
for row,y in zip(['','B','RBR','RRR','RRRR','BBBRB'],[4.85,5.35,5.85,6.35,6.85,7.35]):
 k.cards(row,1.45,y,step=.4,size=.31); k.choices(6.75,y)
for y in [8.15,8.9,9.65]: k.blank_cards(1.5,y,6,.46,.65)
k.finish('k-1.tex') if False else None
k.page(); k.problem(2,r'Make every four-card row that finishes at \Y. Show each row once.',size=17)
k.two('lastR',2.6,5.9,2.58,True)
for y in [3.9,4.95,6.0,7.05,8.1,9.15]:
 for x in [1.05,4.75]: k.blank_cards(x,y,4,.48,.65)
k.page(); k.problem(3,r'Make six different rows that give these machines different answers. Use six cards in each row.',size=17)
k.two('even',1.75,3.25,2.8,True,'a'); k.two('lastR',5.35,6.85,2.8,True,'b')
for y in [4.2,5.25,6.3,7.35,8.4,9.45]: k.blank_cards(1.45,y,6,.48,.65)
k.page(); k.problem(4,r'Use two circles to make a machine that says \Y\ exactly when the last card is blue. With no cards, it must say \N.',size=17)
k.state('e0',2.2,3.3,False,True,True); k.state('e1',6.15,3.3,False,True,True)
k.parts.append(r'\draw[edge] (1.2,3.3)--(e0.west);'+'\n')
k.problem(5,r'Make a machine that says \Y\ when no red cards appear and \N\ when any red card appears. Use as few circles as you can.',5.45,17)
k.page(); k.problem(6,r'For each pair, can you add the same cards in the same order after both printed rows to get \Y\ and \N? Adding no cards is allowed.',size=17)
k.three(2.88,True)
for a,b,y in [('', 'R',4.65),('R','RR',5.98),('RR','RBR',7.31),('B','RRR',8.64)]: k.pair(a,b,y,True)
k.finish('k-1.tex')

RULE=r'R means red; B means blue. A machine has one start circle and a fixed YES or NO on each circle. Each circle has exactly one R arrow and one B arrow. Read left to right with one marker, hiding used cards. Only the current circle and the card being read may affect the next move.'
m=Packet('Grades 2--3','W17-23-v2')
m.page(); m.text(.65,.86,7.2,RULE,12,15)
m.problem(1,'Find every four-card row that makes exactly one of these machines say YES. Start both machines fresh for each row, and write each row once.',1.86,14.5)
m.two('even',1.75,3.25,3.7,False,'a',labels=True); m.two('lastR',5.35,6.85,3.7,False,'b')
m.text(.8,4.48,6.9,r'Left machine, input B R: start 1 $\xrightarrow{\ B\ }$ 1 $\xrightarrow{\ R\ }$ 2; stop: NO.',11.5,14)
for y in [5.2,6.03,6.86,7.69,8.52,9.35]:
 for x in [.95,4.75]: m.line(x,y,2.6)
m.page(); m.problem(2,'Draw a machine that says YES exactly when at least one red card has appeared. Use as few circles as you can.',size=15)
m.problem(3,'Draw a machine that says YES exactly when its last card is blue. It must say NO if there are no cards. Use as few circles as you can.',5.4,15)
m.page(); m.problem(4,'A row gets YES exactly when its red cards can be put in groups of three with none left over, including no red cards. For each pair, add the same extra cards in the same order to both rows to give one YES and one NO, or explain why this cannot be done. Adding no cards is allowed.',size=14.5)
for a,b,y in [('', 'R',2.65),('R','RR',3.85),('RR','RRR',5.05),('RBR','RR',6.25),('B','RRR',7.45),('RB','BR',8.65)]: m.pair(a,b,y)
m.page(); m.problem(5,'Draw a machine that says YES exactly when its red cards can be put in groups of three with none left over. A row with no red cards must give YES. Your machine must work for rows of any length. Use as few circles as you can, and explain why fewer circles cannot work.',size=15)
for y in [8.7,9.35,10.0]: m.line(.85,y,6.8)
m.page(); m.problem(6,'Draw a machine that says YES exactly when the last two cards are red followed by blue. Every other row must give NO. Use as few circles as you can, and explain why fewer circles cannot work.',size=15)
for y in [8.7,9.35,10.0]: m.line(.85,y,6.8)
m.finish('grades-2-3.tex')

h=Packet('Grades 4--5','W17-45-v2')
h.page(); h.text(.65,.86,7.2,RULE,12,15)
h.problem(1,'Find every five-card row this machine sends to YES. Describe exactly which rows it sends to YES, for any length.',1.86,14.5)
h.three(3.5,labels=True)
h.text(.8,4.74,6.9,r'Example R B: start 1 $\xrightarrow{\ R\ }$ 2 $\xrightarrow{\ B\ }$ 2; stop: NO.',11.5,14)
for y in [5.45,5.95,6.45,6.95,7.45]:
 for x in [.85,3.28,5.72]: h.line(x,y,1.85)
for y in [8.5,9.15,9.8]: h.line(.85,y,6.8)
h.page(); h.problem(2,'A row gets YES exactly when its red cards can be grouped in threes with none left over, including no red cards. For each pair, add the same extra cards in the same order to both rows to give one YES and one NO, or explain why this cannot be done. Adding no cards is allowed.',size=14.5)
for a,b,y in [('', 'R',2.6),('R','RR',3.9),('RR','BRR',5.2),('BBB','RRR',6.5)]: h.pair(a,b,y)
h.problem(3,'Two rows have left a machine on the same circle. Could adding the same extra cards in the same order to both ever give them different answers? Explain, for any machine obeying the rules on page 1.',7.9,14.5)
for y in [9.25,9.9]: h.line(.85,y,6.8)
h.page(); h.problem(4,'Find the fewest circles needed by a machine that says YES exactly when its red cards can be grouped in fours with none left over. A row with no red cards must give YES. Draw a machine that works for rows of any length, and explain why no machine with fewer circles can work.',size=15)
for y in [8.05,8.7,9.35,10.0]: h.line(.85,y,6.8)
h.page(); h.problem(5,'Find the fewest circles needed by a machine that says YES exactly when the last two cards are red followed by blue. Every other row must give NO. Draw a machine that works for rows of any length, and explain why no machine with fewer circles can work.',size=15)
for y in [8.05,8.7,9.35,10.0]: h.line(.85,y,6.8)
h.page(); h.problem(6,'A machine must say YES exactly when its red cards can be grouped in fives with none left over. Find the fewest circles it needs, and do the same for groups of six. A row with no red cards must give YES. For any group size of one or more, describe a machine, explain why it works for every row, and explain why fewer circles cannot work.',size=15)
for y in [8.05,8.7,9.35,10.0]: h.line(.85,y,6.8)
h.finish('grades-4-5.tex')
