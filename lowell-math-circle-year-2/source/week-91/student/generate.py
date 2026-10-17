from pathlib import Path
import subprocess, os, sys, shutil
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()/'tmp/week91-authoring'
(D/'src').mkdir(parents=True,exist_ok=True)
LATEX=os.environ.get('W91_PDFLATEX') or shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
PRE=r'''\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0mm]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand\familydefault{\sfdefault}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfoomitdate=1\pdftrailerid{}\pdfsuppressptexinfo=15
\begin{document}
'''

def text(x,y,w,s,size=13):
 return rf'\node[anchor=north west,inner sep=0,text width={w}mm,font=\fontsize{{{size}}}{{{size*1.28}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'
def line(x,y,xx,yy,style=''):
 return rf'\draw[{style}] ({x},{y}) -- ({xx},{yy});'+'\n'
def circle(x,y,r,label='',size=11):
 return rf'\draw[fill=white,line width=.6pt] ({x},{y}) circle ({r}mm);\node[font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{y}) {{{label}}};'+'\n'
def arrow(x,y,dx,dy):
 return line(x-dx/2,y-dy/2,x+dx/2,y+dy/2,'-{Latex[length=2mm]},line width=1.1pt')
def strip(x,y,n=12,sz=12,label='Arrival order'):
 s=text(x,y-8,n*sz,label,10)
 for i in range(n):
  s+=rf'\draw[gray] ({x+i*sz},{y}) rectangle ++({sz},{sz});'+'\n'
 return s

def tree(x,y,depth=2,scale=1,states=None,leaves=None):
 # compact tree bounding width 70 (d2) or 150 (d3)
 n=2**depth; gap=19*scale; width=(n-1)*gap
 levels=[]
 for level in range(depth+1):
  a=[]
  for j in range(2**level):
   xx=x+((j+.5)*n/(2**level)-.5)*gap
   a.append((xx,y+level*21*scale))
  levels.append(a)
 s=''
 for k in range(depth):
  for j,(xx,yy) in enumerate(levels[k]):
   for end in levels[k+1][j*2:j*2+2]: s+=line(xx,yy,*end)
 idx=0
 for k,coords in enumerate(levels):
  for j,(xx,yy) in enumerate(coords):
   if k==depth: s+=circle(xx,yy,4*scale,(leaves or list('ABCDEFGH'))[j],10)
   else:
    s+=circle(xx,yy,4.4*scale)
    if states and states[idx]: s+=arrow(xx,yy,(-1 if states[idx]=='L' else 1)*4*scale,4*scale)
    idx+=1
 return s

def road(x,y,m=4,gap=25,states=None,entry=None):
 s=line(x,y,x+m*gap,y)
 for i in range(m+1):
  s+=circle(x+i*gap,y,4.5, str(i) if i in (0,m) else '',10)
  if 0<i<m:
   s+=text(x+i*gap-3,y+7,10,str(i),10)
   if states and states[i-1]:s+=arrow(x+i*gap,y,5*(1 if states[i-1]=='R' else -1),0)
 if entry is not None:
  s+=text(x+entry*gap-8,y-19,22,'entry',9)+arrow(x+entry*gap,y-8,0,7)
 return s

class Doc:
 def __init__(self,name):self.name=name;self.pages=[]
 def add(self,body,band='Grades 2--3',land=False,id=None):
  w,h=(279.4,215.9) if land else (215.9,279.4)
  page=rf'\paperwidth={w}mm\paperheight={h}mm\pdfpagewidth={w}mm\pdfpageheight={h}mm\begin{{tikzpicture}}[remember picture,overlay,x=1mm,y=-1mm,shift={{(current page.north west)}}]'+'\n'
  page+=text(15,12,w-30,rf'Week 91 / Rotor-router machines / {band}',11)
  page+=line(15,21,w-15,21,'gray')
  page+=body
  page+=line(15,h-18,w-15,h-18,'gray')
  page+=text(15,h-13,w-40,rf'Bellingham Math Circle / Week 91 / {id or self.name}-v1',9)
  page+=text(w-24,h-13,10,str(len(self.pages)+1),9)
  page+='\\end{tikzpicture}\\null\\newpage\n'
  self.pages.append(page)
 def save(self):
  f=D/'src'/f'{self.name}.tex';f.write_text(PRE+''.join(self.pages)+r'\end{document}')
  r=subprocess.run([LATEX,'-halt-on-error','-interaction=nonstopmode',f'-output-directory={D}',str(f)],stdout=subprocess.PIPE,text=True)
  if r.returncode == 0:
   r=subprocess.run([LATEX,'-halt-on-error','-interaction=nonstopmode',f'-output-directory={D}',str(f)],stdout=subprocess.PIPE,text=True)
  (D/'src'/f'{self.name}-build.log').write_text(r.stdout)
  if r.returncode: raise RuntimeError(r.stdout[-3000:])

S=Doc('students')
b=text(15,29,186,'Send counters to the exits, one at a time. At each circle, follow the NEXT arrow, then flip its card. Leave every card as it is for the next counter. Keep the counter beside the card so its arrow stays visible. A partner checks each move.',13)
b+=text(15,65,55,'Input',10)+text(81,65,55,'Move to X',10)+text(148,65,55,'Flip; ready again',10)
for x,state,dot in [(31,'L','top'),(97,'L','left'),(164,'R','left')]:
 b+=line(x,86,x-12,104)+line(x,86,x+12,104)+circle(x,86,7)+arrow(x,86,-5 if state=='L' else 5,5)
 b+=text(x-17,108,12,'X',11)+text(x+9,108,12,'Y',11)
 b+=rf'\fill ({x+9 if dot=="top" else x-12},{83 if dot=="top" else 104}) circle (2mm);'
b+=arrow(65,94,12,0)+arrow(132,94,12,0)
b+=text(15,123,186,r'\textbf{Problem 1:} Use the one-switch board. Choose its first arrow. Send 12 counters through and keep their arrival order. Then start a new trial with the other first arrow.',14)
b+=strip(15,163,12,15)+strip(15,201,12,15)
b+=text(15,234,186,'Which arrival strings can this switch make: XYXY, XXYY, YXYX, XYYX?',14)
S.add(b)
b=text(15,31,186,r'\textbf{Problem 2:} Use the four-exit tree. Choose starting arrows that send the first counter to D. Keep those cards and send seven more counters. Record the starting arrows and arrival order.',14)
b+=tree(60,79,2,1)+strip(15,135,8,15)
b+=text(15,162,186,'What can you change in the starting arrows while keeping D first? Find every arrival order.',14)
b+=tree(60,184,2,1)+strip(15,240,8,15)
S.add(b)
b=text(15,31,186,r'\textbf{Problem 3:} Program the four-exit tree to make each arrival order below. Start a new trial for each order. If an order is impossible, explain what stops it.',14)
for i,(order,x,y) in enumerate([('A C B D',21,81),('B D A C',117,81),('A B C D',21,166),('D A B C',117,166)]):
 b+=text(x,y,80,order,17)+tree(x+3,y+19,2,1)
b+=text(15,249,186,'',10)
S.add(b)
b=text(15,31,186,r'\textbf{Problem 4:} Use the eight-exit tree. Choose starting arrows to make each order. Which orders can the machine make?',14)
orders=['A E C G B F D H','H D F B G C E A','A E B F C G D H']
for i,o in enumerate(orders):
 y=65+i*65
 b+=text(15,y,186,o,16)
 b+=tree(55,y+13,3,.75)
S.add(b,band='Grades 4--5')
b=text(15,31,186,r'\textbf{Problem 5:} Invent an eight-counter order that visits every exit once but cannot be made by the eight-exit tree. Explain why it cannot work.',14)
b+=strip(15,70,8,19)
b+=text(15,116,186,r'\textbf{Problem 6:} Choose any starting arrows on either tree. Send four counters through the four-exit tree or eight through the eight-exit tree. Must every exit get a counter before any exit gets a second one? Must the arrows return to their starting positions? Explain what makes your answers work for every starting position.',14)
b+=tree(24,181,2,1)+tree(111,183,3,.59)
S.add(b,band='Grades 4--5')
b=text(15,31,186,r'\textbf{Problem 7:} Make a second way to choose exits: toss a coin for each counter, sending heads to X and tails to Y. Compare 12 coin choices with 12 arrivals from the one-switch board.',14)
b+=strip(15,88,12,15,'Coin')+strip(15,135,12,15,'Switch')
b+=text(15,184,186,'Find a six-counter arrival order that the coin could make but the switch could never make. Could the coin make every order that the switch can make?',14)
b+=strip(15,230,6,15,'')
S.add(b,band='Grades 2--5')
S.save()

R=Doc('return-visit')
b=text(15,29,186,'On a road, a counter may revisit a circle. Follow its NEXT arrow, then flip that card, every time. Stop at either end. Finish one counter before launching the next; keep the cards between counters. Keep the counter beside the card so its arrow stays visible. A partner checks each move.',12)
b+=text(15,68,186,'Example: enter at 2 on this short road.',11)
b+=road(29,99,3,23,['R','L'],2)+rf'\fill (83,96) circle (2mm);'+text(119,84,80,r'Input: counter at 2.\\Cards at 1 and 2: R, L.',11)
b+=road(29,132,3,23,['R','R'])+rf'\fill (52,124) circle (2mm);'+text(119,118,80,r'After $2\to1$:\\counter at 1; cards R, R.',11)
b+=road(29,165,3,23,['L','L'])+rf'\fill (98,157) circle (2mm);'+text(119,149,80,r'Then $1\to2\to3$.\\Exit: 3. Cards: L, L.',11)
b+=text(15,190,186,r'\textbf{Problem 1:} Use the road from 0 to 4. Enter at 1, with starting cards L, L, R at 1, 2, 3. Send eight counters. Keep the arrival order. Where will the next four counters exit?',14)
b+=strip(15,239,12,15)
R.add(b,'Grades 4--5')
b=text(15,31,186,r'\textbf{Problem 2:} On the road from 0 to 4, find out how moving the entry changes the exits. Choose any starting arrows for each new trial. Send eight counters from each marked entry.',14)
for i,e in enumerate([1,2,3]):
 y=87+58*i
 b+=road(35,y,4,32,entry=e)+strip(15,y+21,8,15,'')
b+=text(15,253,186,'',10)
R.add(b,'Grades 4--5')
b=text(15,31,186,r'\textbf{Problem 3:} Use the road from 0 to 5. Can you choose starting arrows so that all five counters exit at 5? Try entry 1, entry 2 and entry 4. Find a rule for the number reaching each end in five launches.',14)
for i,e in enumerate([1,2,4]):
 y=94+57*i
 b+=road(24,y,5,33,entry=e)+strip(15,y+21,5,15,'')
R.add(b,'Grades 4--5')
b=text(15,31,186,r'\textbf{Problem 4:} Choose a road and an entry. Can the exit counts repeat in equal blocks while the complete arrow positions change? Find an example or explain why none can exist.',14)
b+=text(15,75,186,r'Road: \rule{22mm}{.3pt}\quad Entry: \rule{22mm}{.3pt}\quad Block size: \rule{22mm}{.3pt}',12)
b+=text(15,97,48,'Starting arrows',10)+text(80,97,48,'After one block',10)+text(145,97,48,'After two blocks',10)
for x in [15,80,145]:
 for j in range(4):
  b+=rf'\draw[gray] ({x+j*12},107) rectangle ++(12,13);'
  b+=text(x+j*12+4,121,10,str(j+1),9)
b+=text(15,130,186,'Position 4 is only for the road from 0 to 5.',10)
b+=strip(15,150,12,15)
b+=text(15,179,186,r'\textbf{Problem 5:} Imagine a longer road: $0,1,2,\ldots,m$. Always enter at the same inside circle, $s$. Predict how many of $m$ counters reach each end, for any starting arrows. Explain why your rule works.',14)
b+=text(15,232,186,r'\textbf{Problem 6:} Could a counter travel forever without reaching either end? Explain your answer for any finite road.',14)
R.add(b,'Grades 4--5')
R.save()

M=Doc('materials')
b=text(15,30,186,'One-switch board',16)+text(15,43,186,'One counter waits beside the card. Exits: X and Y.',11)
b+=line(108,95,55,175)+line(108,95,161,175)+circle(108,95,16)+circle(55,175,16,'X',18)+circle(161,175,16,'Y',18)
b+=text(93,70,35,'ENTRY',11)
M.add(b,'Materials')
for depth in [2,3]:
 b=text(15,28,240,f'{2**depth}-exit tree board',16)
 if depth==2:
  levels=[[(140,45)],[(84,100),(196,100)],[(56,173),(112,173),(168,173),(224,173)]];exitdiam=30
 else:
  levels=[[(140,43)],[(84,82),(196,82)],[(56,123),(112,123),(168,123),(224,123)],[(x,175) for x in [42,70,98,126,154,182,210,238]]];exitdiam=22
 for k in range(depth):
  for j,(x,y) in enumerate(levels[k]):
   for end in levels[k+1][2*j:2*j+2]:b+=line(x,y,*end,'line width=1pt')
 for k,lev in enumerate(levels):
  for j,(x,y) in enumerate(lev):b+=circle(x,y,exitdiam/2 if k==depth else 12,list('ABCDEFGH')[j] if k==depth else '',17)
 b+=text(158,41,40,'ENTRY',10)
 M.add(b,'Materials',True)
for m,coords,diam,ed in [(4,[40,90,140,190,240],30,36),(5,[35,77,119,161,203,245],28,32)]:
 b=text(15,30,249,f'Road from 0 to {m}',16)+text(15,46,249,'Place the ENTRY marker beside the launch circle.',11)
 b+=line(coords[0],105,coords[-1],105,'line width=1pt')
 for i,x in enumerate(coords):
  b+=circle(x,105,ed/2 if i in [0,m] else diam/2,str(i) if i in [0,m] else '',19)
  if 0<i<m:b+=text(x-4,127,15,str(i),15)
 b+=text(coords[0]-12,133,30,'STOP',11)+text(coords[-1]-12,133,30,'STOP',11)
 M.add(b,'Materials',True)
b=text(15,30,186,'Reversible cards / one kit',16)
b+=text(15,43,186,r'Cut each paired rectangle. Fold on its dotted middle line and glue the two backs together. Both faces keep NEXT at the top. Print at 100\%.',11)
for i in range(7):
 x=26+(i%2)*87;y=72+(i//2)*29
 for k in range(2):
  b+=rf'\draw ({x+18*k},{y}) rectangle ++(18,22);'
  b+=text(x+18*k+1,y+1,17,'NEXT',7)
  b+=arrow(x+18*k+9,y+13,(-1 if k==0 else 1)*8,8)
 b+=line(x+18,y,x+18,y+22,'dotted,white,line width=1.5pt')+line(x+18,y,x+18,y+22,'dotted')
 b+=text(x+39,y+7,36,f'Tree {i+1}',10)
for i in range(4):
 x=24+(i%2)*88;y=194+(i//2)*28
 for k in range(2):
  b+=rf'\draw ({x+20*k},{y}) rectangle ++(20,20);'
  b+=text(x+20*k+1,y+1,18,'NEXT',7)+arrow(x+20*k+10,y+12,(-1 if k==0 else 1)*10,0)
 b+=line(x+20,y,x+20,y+20,'dotted,white,line width=1.5pt')+line(x+20,y,x+20,y+20,'dotted')
 b+=text(x+43,y+7,35,f'Road {i+1}',10)
M.add(b,'Materials')
b=text(15,30,186,'Arrival strips / entry markers',16)+text(15,44,186,r'Print at 100\%. Each square is 15 mm wide. Write exit letters or numbers in arrival order. Cut strips on their outside edges.',11)
for y in [78,113,148,183]: b+=strip(15,y,12,15,'Arrival order')
for x in [25,90,155]:
 b+=rf'\draw ({x},222) rectangle ++(35,20);'+text(x+2,226,32,'ENTRY',11)+arrow(x+28,233,0,8)
b+=line(20,254,70,254)+line(20,251,20,257)+line(70,251,70,257)+text(75,250,90,'50 mm scale check',10)
M.add(b,'Materials')
M.save()
print('Built',[(x.name,len(x.pages)) for x in [S,R,M]])
