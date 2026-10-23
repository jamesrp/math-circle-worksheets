from pathlib import Path
import json
from examples import blocking_example
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'math_checks.json').read_text())

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usetikzlibrary{calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''

def tx(x,y,s,w=7.25,size=14,lead=None):
 if lead is None:lead=size*1.24
 return rf'\node[anchor=north west,inner sep=0pt,text width={w}in,font=\fontsize{{{size}}}{{{lead}}}\selectfont] at ({x},{-y}) {{{s}}};'+'\n'
def ln(x,y,x2,y2,style='gray!40,line width=0.5pt'):
 return rf'\draw[{style}] ({x},{-y}) -- ({x2},{-y2});'+'\n'
def token(x,y,label,side,d=.79,size=20):
 style='circle' if side=='L' else 'rectangle'
 return rf'\node[draw,line width=0.8pt,{style},fill=white,minimum size={d}in,inner sep=0pt,font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{-y}) {{{label}}};'+'\n'
def box(x,y,w,h,style='gray!45,line width=.5pt'):
 return rf'\draw[{style}] ({x},{-y}) rectangle ({x+w},{-(y+h)});'+'\n'

def page(level,pid,n,content):
 return '\\null\n\\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]\n\\begin{scope}[shift={(current page.north west)}]\n'+tx(.55,.35,rf'Week 27 / Stable pairings / {level}',size=11.5)+ln(.55,.66,7.95,.66,'black,line width=.55pt')+content+tx(.55,10.49,rf'Bellingham Math Circle / Week 27 / {pid}',size=10.2,w=6.8)+tx(7.60,10.49,str(n),size=10.2,w=.35)+'\\end{scope}\n\\end{tikzpicture}\n\\newpage\n'
def prob(n,y,text,size=15):return tx(.6,y,rf'\textbf{{Problem {n}:}} {text}',size=size)
def write(name,pages): (ROOT/(name+'.tex')).write_text(PRE+''.join(pages)+r'\end{document}'+'\n')
def get(key):return DATA[key]['left'],DATA[key]['right']

# Large two-choice strips for the adult-read entry.
def kstrips(y,L,R):
 out=''
 for col,side,prof in [(0,'L',L),(1,'R',R)]:
  base=.6+col*3.85
  for row,(who,prefs) in enumerate(prof.items()):
   cy=y+.50+row*.86
   out+=token(base+.45,cy,who,side)
   out+=tx(base+.94,cy-.19,':',w=.2,size=20)
   out+=box(base+1.11,cy-.425,2.0,.85,'black,line width=.65pt')
   for j,val in enumerate(prefs):
    xx=base+1.60+j*.99
    out+=token(xx,cy,val,'R' if side=='L' else 'L')
 return out

def kboard(x,y,kind=None):
 # Every icon is 20.1 mm wide at 100 percent scale.
 out='';lx=x+.40;rx=x+2.30
 if kind:
  for i,j in enumerate(kind):out+=ln(lx,y+i*.87,rx,y+j*.87,'black,line width=1.2pt')
 for i,ch in enumerate('AB'):out+=token(lx,y+i*.87,ch,'L')
 for i,ch in enumerate('XY'):out+=token(rx,y+i*.87,ch,'R')
 return out

def kcase(y,L,R,kinds=((0,1),(1,0))):
 s=kstrips(y,L,R)
 for i,kind in enumerate(kinds):s+=kboard(.72+i*3.85,y+2.27,kind)
 return s

k=[]
rules='Pair each circle with a different square. Each strip uses both choices once, with its first choice on the left. A pairing can stay if no two pieces in different pairs both want each other more than their partners.'
k.append(page('K--1','W27-K-v3',1,blocking_example(tx,ln,token,box,rules)))
c=prob(1,1.97,'Circle every pairing that can stay.',15.5)
c+=kcase(2.43,*get('k_unique_mutual'))+ln(.6,6.18,7.9,6.18)+kcase(6.41,*get('k_unique_shared'))
k.append(page('K--1','W27-K-v3',2,c))
c=prob(2,.91,'Draw every pairing that can stay.',15.5)
c+=kcase(1.80,*get('k_two_stable'),kinds=(None,None))+ln(.6,5.80,7.9,5.80)+kcase(6.25,*get('k_unique_cross'),kinds=(None,None))
k.append(page('K--1','W27-K-v3',3,c))
c=prob(3,.91,'Swap the two choices on just one strip to make the drawn pairing stay. Circle every strip that works on its own, or cross out the pairing if none works.',15)
for y,key in [(2.0,'k_one_blocker'),(6.30,'k_unique_cross')]:
 c+=kstrips(y,*get(key))+kboard(2.68,y+2.27,(0,1))
c+=ln(.6,5.99,7.9,5.99)
k.append(page('K--1','W27-K-v3',4,c))
c=prob(4,.91,'Fill each empty strip so both drawn pairings can stay. If it cannot be done, cross out the empty strip.',15)
L,R=get('k_two_stable');R={**R,'Y':['','']}
c+=kcase(2.0,L,R)+ln(.6,5.99,7.9,5.99)
L={'A':['X','Y'],'B':['X','Y']};R={'X':['B','A'],'Y':['','']}
c+=kcase(6.3,L,R)
k.append(page('K--1','W27-K-v3',5,c))
blankL={'A':['',''],'B':['','']};blankR={'X':['',''],'Y':['','']}
c=prob(5,.91,'Fill the strips so only the pairing on the left can stay. Make two different sets of strips.',15)
c+=kcase(2.0,blankL,blankR)+ln(.6,5.99,7.9,5.99)+kcase(6.3,blankL,blankR)
k.append(page('K--1','W27-K-v3',6,c))
c=prob(6,.91,'Fill the strips so both drawn pairings can stay. Find every way to fill the strips.',15)
c+=kcase(2.0,blankL,blankR)+ln(.6,5.99,7.9,5.99)+kcase(6.3,blankL,blankR)
k.append(page('K--1','W27-K-v3',7,c))
write('k-1',k)

# Compact pencil-recording diagrams for the reading groups.
# Full-size table manipulatives are supplied separately, as specified in PROMPT.md:
# tokens and preference-strip icons at least 20 mm across. These recording diagrams
# are not cut-out tokens or substitutes for the separately supplied table materials.
def strips(y,L,R,n=None,step=.62,d=.47,size=16):
 out='';n=n or len(L)
 # Rows are first-to-last left-to-right. Both sides use the same rank labels.
 for col,side,prof in [(0,'L',L),(1,'R',R)]:
  base=.65+col*3.85
  dx=.75 if n==3 else (.61 if n==4 else 1.05)
  for j in range(n):out+=tx(base+.92+j*dx-.025,y-.12,str(j+1),w=.18,size=10)
  for row,(who,prefs) in enumerate(prof.items()):
   cy=y+.35+row*step
   out+=token(base+.23,cy,who,side,d=d,size=size)
   out+=tx(base+.57,cy-.16,':',w=.18,size=size)
   out+=box(base+.70,cy-.27,(n-1)*dx+.54,.54,'black,line width=.55pt')
   for j,val in enumerate(prefs):out+=token(base+.97+j*dx,cy,val,'R' if side=='L' else 'L',d=d,size=size)
 return out

def board(x,y,left='ABC',right='XYZ',match=None,w=1.72,step=.54,d=.39,size=15):
 out='';lx=x+.20;rx=x+w
 if match:
  for i,a in enumerate(left):out+=ln(lx,y+i*step,rx,y+right.index(match[a])*step,'black,line width=.95pt')
 for i,a in enumerate(left):out+=token(lx,y+i*step,a,'L',d=d,size=size)
 for i,r in enumerate(right):out+=token(rx,y+i*step,r,'R',d=d,size=size)
 return out

def sixboards(y,left='ABC',right='XYZ',rowgap=2.35):
 return ''.join(board(.70+col*2.55,y+row*rowgap,left,right) for row in range(2) for col in range(3))
def lines(y,n,step=.55,x=.65,w=7.15):
 return ''.join(ln(x,y+i*step,x+w,y+i*step) for i in range(n))

m=[]
rules23='Pair each circle with one square, using every letter once. Each strip runs from first choice to last. A pairing can stay if no two letters in different pairs both prefer each other to their current partners.'
m.append(page('Grades 2--3','W27-23-v3',1,blocking_example(tx,ln,token,box,rules23)))
c=prob(1,1.87,'Circle every pairing that can stay. On each other pairing, join two letters that both want to change.',14)
for y,key in [(2.72,'k_unique_shared'),(6.40,'k_two_stable')]:
 c+=strips(y,*get(key),n=2,step=.68,d=.51,size=17)
 c+=board(1.05,y+1.9,'AB','XY',{'A':'X','B':'Y'},w=1.9,step=.68,d=.51,size=17)
 c+=board(4.88,y+1.9,'AB','XY',{'A':'Y','B':'X'},w=1.9,step=.68,d=.51,size=17)
c+=ln(.6,6.02,7.9,6.02)
m.append(page('Grades 2--3','W27-23-v3',2,c))
c=prob(2,.93,'Find every pairing that can stay.',15)+strips(2.00,*get('middle_unique'))+sixboards(4.80,rowgap=2.70)
m.append(page('Grades 2--3','W27-23-v3',3,c))
c=prob(3,.93,'Find every pairing that can stay. How do you know your list is complete?',15)+strips(2.00,*get('middle_three'))+sixboards(4.80,rowgap=2.70)
m.append(page('Grades 2--3','W27-23-v3',4,c))
c=prob(4,.93,'Find every pairing that can stay. Can one pairing give all eight letters their first choice?',15)+strips(2.00,*get('middle_four'),n=4,step=.65,d=.45,size=16)
for row in range(2):
 for col in range(2):c+=board(1.10+col*3.75,5.48+row*2.62,'ABCD','WXYZ',w=1.90,step=.52,d=.41,size=15)
m.append(page('Grades 2--3','W27-23-v3',5,c))
BL={a:['','',''] for a in 'ABC'};BR={a:['','',''] for a in 'XYZ'}
c=prob(5,.93,'Put X, Y, Z in each circle\'s strip and A, B, C in each square\'s strip, in any order. Make exactly two pairings that can stay. Explain why every other pairing fails.',14)
c+=strips(2.20,BL,BR)+board(1.15,4.85,w=1.9)+board(4.88,4.85,w=1.9)+lines(6.95,6,step=.55)
m.append(page('Grades 2--3','W27-23-v3',6,c))
write('grades-2-3',m)

h=[]
rules45='Pair each circle with one square, using every letter once. Each list runs from first choice to last, with no ties. A pairing is stable if no two letters in different pairs both prefer one another to their current partners.'
c=tx(.6,.87,rules45,size=13,lead=16)+prob(1,1.79,'Find all stable pairings for each set of lists.',14)
c+=strips(2.56,*get('k_two_stable'),n=2,step=.58,d=.43,size=16)
c+=board(1.18,4.18,'AB','XY',w=1.9,step=.56,d=.42)+board(4.94,4.18,'AB','XY',w=1.9,step=.56,d=.42)
c+=ln(.6,5.13,7.9,5.13)+strips(5.63,*get('middle_unique'),step=.56,d=.43,size=16)
c+=sixboards(7.88,rowgap=0) if False else ''.join(board(.70+col*2.55,8.13,step=.56) for col in range(3))
h.append(page('Grades 4--5','W27-45-v2',1,c))
c=prob(2,.91,'Use these rules with A, B, C, D asking. Show or record the requests and final pairs. Run them again with W, X, Y, Z asking. Does changing the asking side change the final pairing?',13.5)
asking='Begin with everyone free. A free asker asks its highest choice that it has not asked before. A free receiver holds its asker. A receiver already holding someone keeps whichever of the two it prefers and releases the other. Holds are temporary. Stop when every asker is held.'
c+=tx(.6,1.94,asking,size=12.7,lead=16)
c+=tx(.6,3.12,r'One step with other letters: U ranks Q ahead of P. Free Q asks U.',size=11.8,lead=14)
c+=ln(1.15,3.74,2.35,3.74,'black,line width=.9pt')+token(1.15,3.74,'P','L',d=.30,size=12)+token(2.35,3.74,'U','R',d=.30,size=12)
c+=tx(.65,4.02,'Before: P held; Q free.',w=3.20,size=11.5)
c+=ln(5.10,3.74,6.30,3.74,'black,line width=.9pt')+token(5.10,3.74,'Q','L',d=.30,size=12)+token(6.30,3.74,'U','R',d=.30,size=12)
c+=tx(4.55,4.02,'After: Q held; P released.',w=3.25,size=11.5)
c+=r'\draw[->,line width=.7pt] (3.43,-3.74) -- (4.26,-3.74);'+'\n'
c+=strips(4.56,*get('older_four'),n=4,step=.56,d=.41,size=15)
c+=box(.65,7.24,3.35,.75)+box(4.5,7.24,3.35,.75)
c+=board(1.10,8.43,'ABCD','WXYZ',w=1.9,step=.48,d=.38,size=14)+board(4.85,8.43,'ABCD','WXYZ',w=1.9,step=.48,d=.38,size=14)
h.append(page('Grades 4--5','W27-45-v2',2,c))
c=prob(3,.91,'Change the rule: a receiver must keep the first asker and reject every later asker. Choose complete lists for A, B, C and X, Y, Z that make these changed rules end with an unstable pairing. Let A, B, C ask; record the requests and two letters in different pairs that both prefer each other.',13.5)
c+=strips(2.66,BL,BR)+box(.65,5.09,7.2,1.86)+board(2.80,7.65,w=1.9,step=.64,d=.46,size=17)+lines(9.35,2,step=.48)
h.append(page('Grades 4--5','W27-45-v2',3,c))
c=prob(4,.91,'Four letters on each side follow the asking rules from Problem 2. Give a number of requests that can never be exceeded, and explain why the rules must finish with everyone paired. Would your argument work with ten letters on each side?',14)
c+=lines(2.65,13,step=.56)
h.append(page('Grades 4--5','W27-45-v2',4,c))
c=prob(5,.91,'When the asking rules from Problem 2 finish, could two letters in different pairs both prefer one another to their final partners? Explain why your answer holds for every set of complete lists with no ties and equal-sized sides.',14)
c+=lines(2.65,13,step=.56)
h.append(page('Grades 4--5','W27-45-v2',5,c))
c=prob(6,.91,'Choose complete lists for A, B, C and X, Y, Z and a stable pairing in which as many of the six letters as possible get their last choice. Explain why a larger number is impossible.',14)
c+=strips(2.31,BL,BR)+board(2.81,4.89,w=1.9,step=.57,d=.42,size=16)+lines(6.62,7,step=.51)
h.append(page('Grades 4--5','W27-45-v2',6,c))
write('grades-4-5',h)
print('Generated',len(k),len(m),len(h),'pages')

# Guidance-revision single hold/release step uses distinct example labels.
_receiver_order = ['Q', 'P']
_old_hold, _new_asker = 'P', 'Q'
_kept = min((_old_hold, _new_asker), key=_receiver_order.index)
_released = next(x for x in (_old_hold, _new_asker) if x != _kept)
assert (_kept, _released) == ('Q', 'P')
