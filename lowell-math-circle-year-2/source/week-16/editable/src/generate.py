from pathlib import Path
import itertools,math,json,ast
P=Path(__file__).resolve().parent
D=json.loads((P/'math_checks.json').read_text())

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

def board(n,width=5.25,fan=False,labels=None,exception=None,counter=False):
 vs,xy,ts=mesh(n,fan)
 edges=sorted({tuple(sorted(e)) for t in ts for e in itertools.combinations(t,2)})
 labels=labels or {(0,0):'R',(n,0):'B',(0,n):'Y'}
 h=width*math.sqrt(3)/2
 blank_radius=0.092 if counter else 0.145
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
   out.append(f'\\draw[line width=0.8pt,fill=white] ({x:.4f},{y:.4f}) circle[radius={blank_radius:.3f}in];')
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

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[letterpaper,left=0.62in,right=0.62in,top=0.75in,bottom=0.65in,headheight=14pt,headsep=0.17in,footskip=0.32in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usepackage{fancyhdr}
\definecolor{Rfill}{RGB}{251,227,225}
\definecolor{Bfill}{RGB}{223,235,251}
\definecolor{Yfill}{RGB}{255,247,203}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\emergencystretch}{2em}
\raggedbottom
\sffamily
'''

def packet(name,level,pid,problems,k=False,repeat_first=False):
 body=PRE+f'\\fancyhead[L]{{\\fontsize{{10.5}}{{12}}\\selectfont Week 16 / Three-color triangles / {level}}}\n'+f'\\fancyfoot[L]{{\\fontsize{{9}}{{11}}\\selectfont Bellingham Math Circle / Week 16 / {pid}}}\n'+r'\fancyfoot[R]{\fontsize{9}{11}\selectfont\thepage}'+'\n\\begin{document}\n'
 body+=r'\fontsize{15}{19}\selectfont' if k else r'\fontsize{12.5}{16.5}\selectfont'
 body+='\n'
 for num,(txt,diag) in enumerate(problems,1):
  if num>1:body+='\\newpage\n'
  if num==1:
   rule=('Put one R, B, or Y counter on every dot. Keep the corner letters. Each outside side allows only the letters beside it. A little triangle has no lines inside.' if k else 'Write R, B, or Y on every empty dot. Keep the printed letters. Each outside side allows only the letters beside it. A little triangle has no lines inside.')
   body+=rule+'\\par\\vspace{0.23in}\n'
  body+=f'\\textbf{{Problem {num}:}} '+txt+'\\par\\vspace{0.16in}\n'+diag+'\n'
  if num==1 and repeat_first:
   body+='\\newpage\n'+f'\\textbf{{Problem {num}:}} '+txt+'\\par\\vspace{0.16in}\n'+diag+'\n'
 body+='\\end{document}\n'
 (P/f'{name}.tex').write_text(body)

fanlabels={ast.literal_eval(v):l for v,l in D['fan']['fixed_boundary'].items()}
r3={ast.literal_eval(v):l for v,l in D['3']['route_labels'].items()}
r4={ast.literal_eval(v):l for v,l in D['4']['route_labels'].items()}
packet('k-1','K--1','F16-K-v2',[
 ('Fill the dots with counters. Move the counters to put a little triangle with R, B, and Y in each of the four places, one at a time.',board(2,counter=True)),
 ('Can you fill the dots without making a little triangle with R, B, and Y?',board(3,counter=True)),
 ('Fill the dots to make as many little triangles with R, B, and Y as you can.',board(3,counter=True)),
 ('Keep every printed letter. Fill the empty dots to make as many little triangles with R, B, and Y as you can.',board(2,fan=True,labels=fanlabels,counter=True)),
 ('Make just one little triangle with R, B, and Y. Move the counters to put it in as many different places as you can.',board(4,counter=True)),
 ('The bottom side now allows R, B, or Y. Find four different fillings with no little triangle that has R, B, and Y.',board(3,exception='whole',counter=True)),
],True)
packet('grades-2-3','Grades 2--3','F16-23-v2',[
 ('Find a filling with as few little triangles containing R, B, and Y as you can. Find another filling with as many as you can.',board(3)),
 ('An edge with R at one end and B at the other is a door. Mark every door. Draw every route that starts at an outside door. A route must leave a two-door triangle through its other door; it stops at a one-door triangle or outside. Which entrances lead back outside?',door_example()+board(3,width=4.8,labels=r3)),
 ('Put R, B, or Y on each dot. Find every different filling, counting turns and flips as the same. Mark the doors in each filling. Could a triangle have three doors?',localsheet()),
 ('Write R or B on every empty dot and mark the doors. Can any row have an even number of doors? Explain why or why not.',chains(['RB']*5,[2,3,4,5,6])),
 ('Fill the dots so that exactly three little triangles have R, B, and Y. Draw all routes that start at outside doors. Can all those routes end outside?',board(4)),
 ('Can the dots be filled so that no little triangle has R, B, and Y? Give a reason that covers every filling allowed by the side rules.',board(2,fan=True)),
],repeat_first=True)
packet('grades-4-5','Grades 4--5','F16-45-v2',[
 ('Find a filling with as few little triangles containing R, B, and Y as you can, and another with as many as you can. Which counts between your two records can you make?',board(3)),
 ('Call an edge with R at one end and B at the other a door. Mark every door. A route crosses through doors and uses no door twice. In a two-door triangle it must use both doors. Draw all the routes, including any that stay inside the big triangle. Can every route from outside return outside?',door_example()+board(4,width=4.8,labels=r4)),
 ('Put R, B, or Y on each dot. Find every different filling, counting turns and flips as the same. Record the number of doors in each filling. Which fillings have exactly one door? Could a triangle have three doors?',localsheet()),
 ('Write R or B on every empty dot and mark the doors. Decide which rows must have an odd number of doors and which must have an even number. Explain your answer for rows of any length.',chains(['RB','RR','RB','RR','RB'],[3,4,5,6,7])),
 ('Must the number of little triangles with R, B, and Y be odd? Explain your answer for every filling allowed by the side rules, on this board and on any division into little triangles that meet only at corners or along whole edges.',board(2,fan=True)),
 ('The starred dot may now use R, B, or Y. All other side rules still hold. Find a filling with no little triangle that has R, B, and Y. Explain why this does not contradict your answer to Problem 5.',board(4,exception='single')),
],repeat_first=True)
