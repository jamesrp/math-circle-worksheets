"""Week 16 figures, carried over unchanged from the old student generator
(archive-before-problem-files-2026-10-23/generate.py): the triangle boards, the door
example, the local-case sheet and the boundary rows. Problem files call these
functions in their `figure` sections; the wording lives in the problem files.

FANLABELS, R3 and R4 are the printed letters of the fan board and the two route
boards, read from the package's math_checks.json as the old generator read them.

October 23, 2026 card fixes: every blank side dot is split in the tints of the letters
its side allows (bottom R and B, left R and Y, right B and Y; all three on the K-1
Problem 6 bottom and at the Grades 4-5 Problem 6 star), K-1 rings are 0.30 in across
instead of 0.18 in, and record_triangles() draws the four small K-1 Problem 6 records.
"""
import ast
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Repository: source/week-16/editable/src/; portable ZIP: <top>/src/ beside problem-files/.
for _p in (HERE / 'editable' / 'src' / 'math_checks.json', HERE.parent / 'src' / 'math_checks.json'):
    if _p.exists():
        D = json.loads(_p.read_text())
        break
else:
    raise FileNotFoundError('math_checks.json not found beside the Week 16 problem files')

def mesh(n,fan=False):
 vs=[(i,j) for j in range(n+1) for i in range(n-j+1)]
 xy={v:((v[0]+v[1]/2)/n,math.sqrt(3)/2*v[1]/n) for v in vs}
 ts=[]
 for j in range(n):
  for i in range(n-j):
   ts.append(((i,j),(i+1,j),(i,j+1)))
   if i+j<n-1:ts.append(((i+1,j),(i+1,j+1),(i,j+1)))
 if fan:
  nt=[]
  for k,t in enumerate(ts):
   v=(10,k);vs.append(v);xy[v]=tuple(sum(xy[a][d] for a in t)/3 for d in [0,1]);nt.extend([(t[0],t[1],v),(t[1],t[2],v),(t[2],t[0],v)])
  ts=nt
 return vs,xy,ts

# Half (or third) discs of a side dot: (letter, start angle, end angle), the half nearer
# a corner taking that corner's tint.
TINTS={'bottom':[('R',90,270),('B',-90,90)],'left':[('R',150,330),('Y',-30,150)],
 'right':[('B',210,390),('Y',30,210)],'all':[('Y',30,150),('R',150,270),('B',270,390)]}

def side_of(v,n):
 """The outside side a mesh dot lies on (None inside, and for the fan board's inserted centres)."""
 i,j=v
 if i==10 or not(j==0 or i==0 or i+j==n):return None
 return 'bottom' if j==0 else 'left' if i==0 else 'right'

def record_triangles(count=4,width=1.5,gap=0.3):
 """Small unlettered three-step triangles for an adult to letter each filling found."""
 vs,xy,ts=mesh(3)
 edges=sorted({tuple(sorted(e)) for t in ts for e in itertools.combinations(t,2)})
 out=[r'\begin{center}',r'\begin{tikzpicture}[x=1in,y=1in,line cap=round,line join=round]']
 for c in range(count):
  ox=c*(width+gap)
  for a,b in edges:
   out.append(f'\\draw[line width=0.6pt] ({ox+xy[a][0]*width:.4f},{xy[a][1]*width:.4f}) -- ({ox+xy[b][0]*width:.4f},{xy[b][1]*width:.4f});')
  for v in vs:
   out.append(f'\\draw[line width=0.6pt,fill=white] ({ox+xy[v][0]*width:.4f},{xy[v][1]*width:.4f}) circle[radius=0.05in];')
 out.extend([r'\end{tikzpicture}',r'\end{center}'])
 return '\n'.join(out)

def board(n,width=5.25,fan=False,labels=None,exception=None,counter=False):
 vs,xy,ts=mesh(n,fan)
 edges=sorted({tuple(sorted(e)) for t in ts for e in itertools.combinations(t,2)})
 labels=labels or {(0,0):'R',(n,0):'B',(0,n):'Y'}
 h=width*math.sqrt(3)/2
 blank_radius=0.15 if counter else 0.145
 out=[r'\begin{center}',r'\begin{tikzpicture}[x=1in,y=1in,line cap=round,line join=round]']
 out.append(r'\path[use as bounding box] (-0.63,-0.64) rectangle ('+f'{width+.63:.4f},{h+.25:.4f}'+');')
 for a,b in edges:
  xa,ya=xy[a];xb,yb=xy[b]
  out.append(f'\\draw[line width=0.8pt] ({xa*width:.4f},{ya*width:.4f}) -- ({xb*width:.4f},{yb*width:.4f});')
 for v in vs:
  x,y=(a*width for a in xy[v]);lab=labels.get(v)
  if lab:
   out.append(f'\\node[circle,draw,line width=0.8pt,fill={lab}fill,minimum size=0.30in,inner sep=0pt,font=\\sffamily\\bfseries\\fontsize{{11.5}}{{12}}\\selectfont] at ({x:.4f},{y:.4f}) {{{lab}}};')
  else:
   side=side_of(v,n)
   if side and (exception=='whole' and side=='bottom' or exception=='single' and v==(n//2,0)):side='all'
   for letter,a1,a2 in TINTS.get(side,[]):
    out.append(f'\\fill[{letter}fill] ({x:.4f},{y:.4f}) -- +({a1}:{blank_radius:.3f}in) arc[start angle={a1},end angle={a2},radius={blank_radius:.3f}in] -- cycle;')
   for letter,a1,a2 in TINTS.get(side,[]):
    out.append(f'\\draw[line width=0.4pt,black!45] ({x:.4f},{y:.4f}) -- +({a1}:{blank_radius:.3f}in);')
   out.append(f'\\draw[line width=0.8pt{"" if side else ",fill=white"}] ({x:.4f},{y:.4f}) circle[radius={blank_radius:.3f}in];')
 out += [f'\\node[rotate=60,font=\\sffamily\\fontsize{{11}}{{12}}\\selectfont] at ({width/4-.33:.4f},{h/2+.16:.4f}) {{R or Y}};',f'\\node[rotate=-60,font=\\sffamily\\fontsize{{11}}{{12}}\\selectfont] at ({width*3/4+.33:.4f},{h/2+.16:.4f}) {{B or Y}};']
 bot={'whole':'R or B or Y','single':r'R or B, except $*$'}.get(exception,'R or B')
 out.append(f'\\node[font=\\sffamily\\fontsize{{11}}{{12}}\\selectfont] at ({width/2:.4f},-0.48) {{{bot}}};')
 if exception=='single':out.append(f'\\node[font=\\large] at ({width/2:.4f},-0.23) {{$*$}};')
 out.extend([r'\end{tikzpicture}',r'\end{center}'])
 return '\n'.join(out)

def door_example():
 return r'''\begin{center}\begin{tikzpicture}[x=1in,y=1in]
\draw (0,0)--(1.2,0)--(.6,.65)--cycle;
\draw[line width=3pt] (.43,0)--(.77,0);
\draw[line width=3pt] (.80,.433)--(1.00,.217);
\node[left,font=\small] at (0,0){R};\node[right,font=\small] at (1.2,0){B};\node[above,font=\small] at (.6,.65){R};
\draw[->,dashed,line width=1pt] (.6,-.22)--(.6,.17)--(1.14,.44);
\node[anchor=west,align=left,text width=4.3in,font=\small] at (1.7,.28){Example: enter one thick door and leave through the other.\\The dashed route crosses edges; it does not follow them.};
\end{tikzpicture}\end{center}
'''

def localsheet():
 out=[r'\begin{center}',r'\begin{tikzpicture}[x=1in,y=1in,line cap=round]']
 out.append(r'\path[use as bounding box] (-0.2,-0.35) rectangle (6.3,6.05);')
 w=1.36;h=w*math.sqrt(3)/2
 for row in range(4):
  for col in range(3):
   x=col*2.25;y=(3-row)*1.55
   p=[(x,y),(x+w,y),(x+w/2,y+h)]
   out.append('\\draw[line width=0.8pt] '+' -- '.join(f'({a:.4f},{b:.4f})' for a,b in p)+' -- cycle;')
   for a,b in p:out.append(f'\\draw[line width=0.8pt,fill=white] ({a:.4f},{b:.4f}) circle[radius=0.11in];')
 out += [r'\end{tikzpicture}',r'\end{center}']
 return '\n'.join(out)

def chains(endletters,edges):
 out=[r'\begin{center}',r'\begin{tikzpicture}[x=1in,y=1in,line cap=round]']
 out.append(r'\path[use as bounding box] (-0.3,-0.25) rectangle (5.9,5.65);')
 for row,(ends,n) in enumerate(zip(endletters,edges)):
  y=5.3-row*1.22
  out.append(f'\\draw[line width=0.8pt] (0,{y:.4f}) -- (5.6,{y:.4f});')
  for k in range(n+1):
   x=5.6*k/n;lab=ends[0] if k==0 else ends[1] if k==n else ''
   if lab:out.append(f'\\node[circle,draw,line width=0.8pt,fill={lab}fill,minimum size=0.30in,inner sep=0pt,font=\\sffamily\\bfseries\\fontsize{{11.5}}{{12}}\\selectfont] at ({x:.4f},{y:.4f}) {{{lab}}};')
   else:out.append(f'\\draw[line width=0.8pt,fill=white] ({x:.4f},{y:.4f}) circle[radius=0.13in];')
 out += [r'\end{tikzpicture}',r'\end{center}']
 return '\n'.join(out)


FANLABELS = {ast.literal_eval(v): l for v, l in D['fan']['fixed_boundary'].items()}
R3 = {ast.literal_eval(v): l for v, l in D['3']['route_labels'].items()}
R4 = {ast.literal_eval(v): l for v, l in D['4']['route_labels'].items()}
