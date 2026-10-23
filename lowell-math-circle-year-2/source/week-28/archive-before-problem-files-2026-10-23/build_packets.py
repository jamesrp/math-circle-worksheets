from pathlib import Path
import math, itertools, json
ROOT=Path(__file__).resolve().parent

def coord(x,y): return f'({x:.4f},{y:.4f})'
def text(x,y,s,size=13,width=18.7,bold=False,align='left'):
    f=r'\bfseries ' if bold else ''
    return rf'\node[anchor=north west,inner sep=0pt,text width={width}cm,align={align},font=\fontsize{{{size}}}{{{size*1.3}}}\selectfont {f}] at {coord(x,y)} {{{s}}};'+'\n'
def point(cx,cy,r,a): return cx+r*math.sin(math.radians(a)),cy-r*math.cos(math.radians(a))
def line(x1,y1,x2,y2,opts='black!32,line width=.35pt'):
    return rf'\draw[{opts}] {coord(x1,y1)} -- {coord(x2,y2)};'+'\n'
def node(x,y,s,size=11,bold=False):
    return rf'\node[inner sep=1pt,fill=white,font=\fontsize{{{size}}}{{{size+2}}}\selectfont '+(r'\bfseries' if bold else '')+rf'] at {coord(x,y)} {{{s}}};'+'\n'
def disk(cx,cy,r=2,sectors=None,rays=None,nums=False,labels=None,degrees=False,shade=False,tag=None,ticks=False,sector_labels=None):
    o=''
    if sectors is not None:
        rays=[0]
        for a in sectors[:-1]: rays.append(rays[-1]+a)
    if rays is None: rays=[0,90,180,270]
    if shade and sectors:
        a=0
        for j,span in enumerate(sectors):
            if j%2==0:
                points=[(cx,cy)]+[point(cx,cy,r,a+span*k/60) for k in range(61)]
                o+=r'\fill[black!14] '+' -- '.join(coord(*p) for p in points)+r' -- cycle;'+'\n'
            a+=span
    o+=rf'\draw[black,line width=.65pt] {coord(cx,cy)} circle[radius={r}cm];'+'\n'
    if ticks:
        for a in range(0,360,30):
            x1,y1=point(cx,cy,r+.02,a);x2,y2=point(cx,cy,r+.12,a)
            o+=line(x1,y1,x2,y2,'black!50,line width=.4pt')
    for j,a in enumerate(rays):
        x,y=point(cx,cy,r,a); o+=line(cx,cy,x,y,'black,line width=.65pt')
        if nums:
            x,y=point(cx,cy,r+.22,a);o+=node(x,y,str(j+1),max(9,min(12,r*5.8)))
        if labels and j<len(labels) and labels[j]:
            x,y=point(cx,cy,r*.66,a);o+=node(x,y,labels[j],max(12,min(18,r*9)),True)
    o+=rf'\fill {coord(cx,cy)} circle[radius=.045cm];'+'\n'
    if degrees and sectors:
        a=0
        for span in sectors:
            x,y=point(cx,cy,r*.66,a+span/2)
            o+=node(x,y,rf'${span}^\circ$',10.5 if r<2 else 12)
            a+=span
    if sector_labels and sectors:
        a=0
        for span,label in zip(sectors,sector_labels):
            x,y=point(cx,cy,r*.68,a+span/2)
            o+=node(x,y,label,12,True)
            a+=span
    if tag:o+=node(cx-r-.2,cy-r-.38,tag,13,True)
    return o

def wedge(cx,cy,r,a,label,degrees=False):
    points=[(cx,cy)]+[point(cx,cy,r,-a/2+a*k/60) for k in range(61)]
    o=r'\draw[line width=.65pt,fill=black!4] '+' -- '.join(coord(*p) for p in points)+r' -- cycle;'+'\n'
    o+=node(cx,cy-r*.62,label,13,True)
    if degrees:o+=node(cx,cy-r*.31,rf'${a}^\circ$',10)
    return o

def half(cx,cy,r=2.2):
    ps=[point(cx,cy,r,-90+i*3) for i in range(61)]
    return r'\draw[line width=.65pt] '+' -- '.join(coord(*p) for p in ps)+r' -- cycle;'+'\n'

def record_lines(ys,cols=1):
    out=''
    for y in ys:
        for c in range(cols):
            w=18.7/cols
            out+=line(c*w+.1,y,(c+1)*w-.5,y)
    return out

def page(level,pid,n,body):
    return r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=-1cm]'+'\n'+r'\coordinate (O) at ([xshift=1.4cm,yshift=-1.15cm]current page.north west);\begin{scope}[shift={(O)}]'+'\n'+text(0,0,f'Week 28 / Flat folds / {level}',11.5,bold=True)+line(0,.59,18.7,.59)+body+text(0,25.2,f'Bellingham Math Circle / Week 28 / {pid}',9.3,width=16)+text(17.4,25.2,str(n),9.3,width=1.3,align='right')+r'\end{scope}\end{tikzpicture}\newpage'+'\n'
def problem(n,s,y=1.1,size=14):return text(0,y,rf'\textbf{{Problem {n}:}} '+s,size)
def doc(pages):
    return r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=1.4cm]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''+''.join(pages).removesuffix('\\newpage\n')+r'\end{document}'+'\n'

# K-1: one substantial question per page, read aloud by an adult.
p=[]
rules=r'Use the marked front when you label folds. M means mountain; V means valley. Fold every ray fully flat. Keep the paper whole, with no extra creases.'
b=text(0,1.05,rules,12.5)+problem(1,"Make the four-ray disk close flat in four different ways. Mark each fold's mountains M and valleys V.",y=3.65,size=16)
for y in (9.0,18.0):
 for x in (4.5,14.0): b+=disk(x,y,2.55,nums=True)
p.append(page('K--1','F28-K-v2',1,b))
b=problem(2,'Which of these folds can you make with the four-ray disk? Circle each one you make.',size=16)
assignments=['MMMV','MMMM','MVVV','MMVV','MMVM','MVMV']
for i,labs in enumerate(assignments): b+=disk((4.5,14)[i%2],(6.2,13.4,20.6)[i//2],2.05,nums=True,labels=labs,tag='ABCDEF'[i])
p.append(page('K--1','F28-K-v2',2,b))
b=problem(3,'Ray 1 must be a mountain. Find every flat fold with that label.',size=16)
for y in (6.1,13.3,20.5):
 for x in (4.5,14): b+=disk(x,y,2.05,nums=True,labels=['M','','',''])
p.append(page('K--1','F28-K-v2',3,b))
b=problem(4,'For each row, use its six tabs to finish the disks. Can all three disks close flat?',size=16)
partial_models=[['M','','V',''],['M','M','',''],['V','','V','']]
for j,tabs in enumerate(['MMVVVV','MMMVVV','MMMMVV']):
 y=5.9+j*6.6
 for i,x in enumerate((3.1,9.4,15.7)):
  b+=disk(x,y,1.6,nums=True,labels=partial_models[i],tag='ABC'[j] if i==0 else None)
 for k,label in enumerate(tabs):
  x=5.1+k*1.55
  b+=r'\draw[line width=.5pt] '+coord(x-.45,y+2.2)+' rectangle '+coord(x+.45,y+3.05)+';\n'
  b+=node(x,y+2.625,label,15,True)
p.append(page('K--1','F28-K-v2',4,b))
b=problem(5,'Find every flat fold of the four-ray disk. Keep ray 1 at the top and mark every ray M or V.',size=16)
for y in (5.0,9.2,13.4,17.6,21.8):
 for x in (4.5,14):b+=disk(x,y,1.58,nums=True)
p.append(page('K--1','F28-K-v2',5,b))
b=problem(6,'Visit all eight folds once, changing exactly two labels at each move. Find a route from A to H and a route from A to D.',size=16)
route_labels=['MMMV','MMVM','MVMM','VMMM','MVVV','VMVV','VVMV','VVVM']
for i,labs in enumerate(route_labels):
 b+=disk((2.2,7.0,11.8,16.6)[i%4],(6.3,13.0)[i//4],1.5,nums=True,labels=labs,tag='ABCDEFGH'[i])
for y,end in [(19.2,'H'),(22.6,'D')]:
 for j in range(8):
  x=1.15+j*2.35
  if j==0 or j==7:b+=node(x,y,'A' if j==0 else end,16,True)
  else:b+=line(x-.65,y+.2,x+.65,y+.2)
  if j<7:b+=line(x+.8,y,x+1.55,y,'black!55,line width=.5pt,->')
p.append(page('K--1','F28-K-v2',6,b))
(ROOT/'k-1.tex').write_text(doc(p))

# Grades 2-3: matching pieces make the exact angle test accessible without degrees.
p=[]
b=text(0,1.05,r'For folds, use the marked front: M means mountain and V means valley. Fold every ray in the finished pattern fully flat. Keep the disk whole, with no other creases. Loose wedges are for measuring.',12)+problem(1,'Use the seven loose wedges to make half-turns. Find as many different groups of letters as you can; use each wedge at most once in a group.',y=3.55,size=14)
for x,a,lab in zip((2.2,6.8,11.4,16.0),(30,30,60,60),'ABCD'):b+=wedge(x,8.0,2.25,a,lab)
for x,a,lab in zip((4.3,9.4,14.5),(90,120,150),'EFG'):b+=wedge(x,12.0,2.25,a,lab)
b+=half(9.35,16.3,2.25)+record_lines((18.0,19.4,20.8,22.2,23.6),2)
p.append(page('Grades 2--3','F28-23-v2',1,b))
angles=[[90,90,90,90],[45,90,90,135],[60,120,120,60],[30,60,150,120]]
b=problem(2,r'Use the 16 separate loose wedges cut to match \mbox{A1--A4}, \mbox{B1--B4}, \mbox{C1--C4}, and \mbox{D1--D4}. For each disk, can the shaded pair fill a half-turn exactly, and can the white pair?',size=14)
for i,ss in enumerate(angles):
 x=(4.5,14)[i%2];y=(7.1,17.1)[i//2]
 b+=disk(x,y,2.5,sectors=ss,shade=True,tag='ABCD'[i],sector_labels=['ABCD'[i]+str(j) for j in range(1,5)])
 b+=text(x-2.5,y+3.15,'Shaded: '+r'\rule{1.5cm}{.35pt}',11,width=5)+text(x-2.5,y+4.0,'White: '+r'\rule{1.5cm}{.35pt}',11,width=5)
p.append(page('Grades 2--3','F28-23-v2',2,b))
b=problem(3,'Which of these disks can close flat along every ray? Make one flat fold of each disk that can close and mark its rays M or V; explain any exact mismatch.',size=14)
for i,ss in enumerate(angles): b+=disk((4.5,14)[i%2],(7.1,16.4)[i//2],2.4,sectors=ss,nums=True,tag='ABCD'[i])
b+=record_lines((21.0,22.4,23.8))
p.append(page('Grades 2--3','F28-23-v2',3,b))
b=problem(4,'Add one ray to each pattern so the two alternating groups of wedges both make a half-turn. Make a flat fold of each completed pattern.',size=14)
for i,rays in enumerate(([0,90,180],[0,60,180],[0,30,180],[0,120,180])):b+=disk((4.5,14)[i%2],(7.3,18.0)[i//2],2.65,rays=rays,tag='ABCD'[i],ticks=True)
p.append(page('Grades 2--3','F28-23-v2',4,b))
b=problem(5,'Find every mountain/valley labeling of the four-right-angle disk that can close flat. Keep ray 1 at the top and make each fold on your disk.',size=14)
for y in (5.0,9.2,13.4,17.6,21.8):
 for x in (4.5,14):b+=disk(x,y,1.58,nums=True)
p.append(page('Grades 2--3','F28-23-v2',5,b))
b=problem(6,'Use these six wedges once each to fill a disk. Find four different orders of A, B, and C in which the alternating wedges make two half-turns. Read clockwise from the top ray.',size=14)
for i,(a,lab) in enumerate(zip((30,30,60,60,90,90),'AABBCC')):b+=wedge((3.1,9.4,15.7)[i%3],(6.0,9.4)[i//3],2.4,a,lab)
for y in (13.0,21.0):
 for x in (4.5,14):b+=disk(x,y,2.4,rays=[0])
p.append(page('Grades 2--3','F28-23-v2',6,b))
(ROOT/'grades-2-3.tex').write_text(doc(p))

# Grades 4-5: construction, necessity, and completeness have separate jobs.
p=[]
b=text(0,1.05,r'Use the same marked front for all mountain (M) and valley (V) labels. Fold every listed ray fully flat, with no extra creases or cuts. Layers may touch but may not pass through one another. A failed attempt alone does not establish impossibility.',12)+problem(1,'Decide which patterns can close flat. Record a successful fold with M/V labels for each one you can make; leave any undecided pattern marked with a question mark.',y=3.85,size=13.5)
for i,ss in enumerate(angles):b+=disk((4.5,14)[i%2],(9.0,19.0)[i//2],2.45,sectors=ss,nums=True,degrees=True,tag='ABCD'[i])
p.append(page('Grades 4--5','F28-45-v2',1,b))
b=problem(2,'Can any of these patterns close flat along every ray? Explain an answer that covers all three patterns.',size=14)
for i,ss in enumerate(([120,120,120],[60,60,60,90,90],[30,30,60,60,60,60,60])):
 x,y=[(4.5,7.2),(14,7.2),(9.35,16.0)][i]
 b+=disk(x,y,2.35,sectors=ss,degrees=True,tag='ABC'[i])
b+=record_lines((20.3,21.8,23.3,24.8))
p.append(page('Grades 4--5','F28-45-v2',2,b))
b=problem(3,r'Explain why every other sector must total $180^\circ$ in any flat-folding pattern with an even number of rays. Which patterns does your explanation rule out?',size=13.5)
checks=[[45,90,90,135],[30,30,60,60,90,90],[30,30,30,60,90,120],[45]*8]
for i,ss in enumerate(checks):b+=disk((4.5,14)[i%2],(6.4,13.8)[i//2],2.0,sectors=ss,degrees=True,shade=True,tag='ABCD'[i])
b+=record_lines((18.2,19.7,21.2,22.7,24.2))
p.append(page('Grades 4--5','F28-45-v2',3,b))
b=problem(4,'Find as many mountain/valley labelings of the four-right-angle disk that can close flat as you can. Explain why each labeling on your list works.',size=13.5)
for y in (6.1,10.9):
 for x in (1.7,5.55,9.4,13.25,17.1):b+=disk(x,y,1.32,nums=True)
b+=record_lines((14.8,16.4,18.0,19.6,21.2,22.8,24.4))
p.append(page('Grades 4--5','F28-45-v2',4,b))
b=problem(5,'Can any of these labelings close flat? Explain why your folds from Problem 4 and the patterns you rule out account for every M/V labeling of the four-right-angle disk.',size=13.5)
for i,labs in enumerate(['MMMM','VVVV','MMVV','MVMV']):
 b+=disk((4.5,14)[i%2],(6.1,13.1)[i//2],2.05,nums=True,labels=labs,tag='ABCD'[i])
b+=record_lines((17.5,19.1,20.7,22.3,23.9))
p.append(page('Grades 4--5','F28-45-v2',5,b))
b=problem(6,r'Use the angles $30^\circ,30^\circ,60^\circ,60^\circ,90^\circ,90^\circ$ once each, clockwise around one center. How many different orders start with $30^\circ$ and have alternating totals of $180^\circ$? Explain why your count is complete. Swapping equal angles does not make a new order.',size=13.5)
b+=disk(15.75,7.0,1.75,rays=[0])+node(15.75,4.85,'start',10)
# Recording strips show ordered slots, without supplying an approach.
for j in range(12):
 y=6.0+j*1.15
 for k in range(6):
  x=.35+k*1.7
  b+=line(x,y,x+1.35,y)
b+=record_lines((21.6,23.0,24.4))
p.append(page('Grades 4--5','F28-45-v2',6,b))
(ROOT/'grades-4-5.tex').write_text(doc(p))

# Independent arithmetic checks for exact diagrams and finite tasks.
orders=sorted(set(itertools.permutations([30,30,60,60,90,90])))
valid=[s for s in orders if s[0]==30 and sum(s[::2])==180]
wedges=[30,30,60,60,90,120,150]
groups=[''.join('ABCDEFG'[i] for i in range(7) if mask>>i&1) for mask in range(1,1<<7) if sum(wedges[i] for i in range(7) if mask>>i&1)==180]
labels=[''.join(s) for s in itertools.product('MV',repeat=4) if abs(s.count('M')-s.count('V'))==2]
assert len(labels)==8
assert len([s for s in labels if s[0]=='M'])==4
assert len([s for s in labels if s[0]=='M' and s[2]=='V'])==2
assert len([s for s in labels if s[0]=='M' and s[1]=='M'])==2
assert len([s for s in labels if s[0]=='V' and s[2]=='V'])==2
for a in [90,60,30,120]:
    rs=sorted([0,a,180,360-a])
    ss=[rs[i+1]-rs[i] for i in range(3)]+[360-rs[-1]]
    assert sum(ss[::2])==sum(ss[1::2])==180
assert min(sum(a!=b for a,b in zip('MMMV',s)) for s in labels if s!='MMMV')==2
for ss in angles+checks+[[120]*3,[60,60,60,90,90],[30,30,60,60,60,60,60]]:assert sum(ss)==360 and min(ss)>0
report={'four_sector_checks':[{'sectors':s,'alternating_totals':[sum(s[::2]),sum(s[1::2])]} for s in angles], 'half_turn_wedge_groups':groups,'valid_right_angle_assignments':labels,'six_angle_orders_starting_30':valid,'six_angle_order_count':len(valid),'all_diagram_angles_total_360':True}
(ROOT/'math_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'half_turn_groups':len(groups),'right_angle_assignments':len(labels),'six_angle_orders':len(valid)}))

partial=['M?V?','MM??','V?V?']
completions=[[lab for lab in labels if all(a=='?' or a==b for a,b in zip(p,lab))] for p in partial]
tab_solutions={}
for n in (2,3,4):
 sols=[case for case in itertools.product(*completions) if sum(sum(c=='M' for c,p in zip(lab,mask) if p=='?') for lab,mask in zip(case,partial))==n]
 tab_solutions[str(n)]=sols
assert [len(tab_solutions[str(n)]) for n in (2,3,4)]==[4,0,4]
route_map=dict(zip('ABCDEFGH',route_labels))
paths={}
for end in ('H','D'):
 rest=[x for x in 'BCDEFGH' if x!=end]
 for middle in itertools.permutations(rest):
  route=('A',)+middle+(end,)
  if all(sum(a!=b for a,b in zip(route_map[u],route_map[v]))==2 for u,v in zip(route,route[1:])):
   paths[end]=route
   break
 assert end in paths
# All 16 measurement pieces have radius 2.5 cm, exactly matching their sector template.
matching_wedges=[{'label':f'{tag}{j+1}','degrees':angle,'radius_cm':2.5,'shaded':j%2==0} for tag,ss in zip('ABCD',angles) for j,angle in enumerate(ss)]
assert len(matching_wedges)==16
assert [x['degrees'] for x in matching_wedges if x['label'].startswith('B')]==[45,90,90,135]
invalid=['MMMM','VVVV','MMVV','MVMV']
rotations={s[k:]+s[:k] for s in invalid for k in range(4)}
assert rotations==set(''.join(p) for p in itertools.product('MV',repeat=4))-set(labels)
report.update({'k1_tab_completions':tab_solutions,'k1_route_witnesses':paths,'matching_wedges':matching_wedges,'right_angle_obstruction_cases_cover_all_remaining_labels':True,'physical_models_tested':False})
(ROOT/'math_checks.json').write_text(json.dumps(report,indent=2))
