from pathlib import Path
from itertools import permutations, product, combinations
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
WIDTH=18.59

def txt(x,y,text,width=18.59,size=14,leading=None):
    if leading is None: leading=size*1.30
    return rf'\node[anchor=north west,inner sep=0pt,align=left,text width={width}cm,font=\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{text}}};'+'\n'

def problem(n,text,size=14,y=0):
    return txt(0,y,rf'\textbf{{Problem {n}:}} '+text,size=size)

def card(x,y,val=None,size=1.05,dots=False):
    s=rf'\draw[line width=0.65pt,fill=white] ({x-size/2},{y-size/2}) rectangle ({x+size/2},{y+size/2});'+'\n'
    if val is None:return s
    if dots:
        points={0:[],1:[(0,0)],2:[(-.19,0),(.19,0)],3:[(-.19,.16),(.19,.16),(0,-.19)],4:[(-.19,-.19),(-.19,.19),(.19,-.19),(.19,.19)]}[int(val)]
        for dx,dy in points:s+=rf'\fill ({x+dx*size},{y+dy*size}) circle[radius={.066*size}cm];'+'\n'
    else:
        s+=rf'\node[font=\fontsize{{14}}{{17}}\selectfont] at ({x},{y}) {{{val}}};'+'\n'
    return s

def bank(vals,x=4.8,y=3,dots=False,size=1.35,step=2.2):
    return ''.join(card(x+i*step,y,v,size,dots) for i,v in enumerate(vals))

def network(n,bars,x=.25,y=5,w=18.0,gap=1.3,blank=True,bar_xs=None,outs=None,ins=None):
    s=''
    for i in range(n):
        yy=y+i*gap
        s+=rf'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({x+.1},{yy}) {{{i+1}}};'+'\n'
        s+=rf'\draw[line width=.65pt,->,>=stealth] ({x+1.8},{yy}) -- ({x+w-1.18},{yy});'+'\n'
        s+=card(x+1.1,yy,ins[i] if ins else None,.92)
        s+=card(x+w-.57,yy,outs[i] if outs else None,.92)
    if bar_xs is None:
        bar_xs=[x+3.1+j*(w-6.4)/max(1,len(bars)-1) for j in range(len(bars))]
    for (a,b),xx in zip(bars,bar_xs):
        s+=rf'\draw[line width=1.4pt] ({xx},{y+(a-1)*gap}) -- ({xx},{y+(b-1)*gap});'+'\n'
        for k in (a,b):s+=rf'\fill ({xx},{y+(k-1)*gap}) circle[radius=.095cm];'+'\n'
    return s

def start_column(vals,x,y,step=.91,size=.72,dots=False):
    s=''
    for j,v in enumerate(vals):s+=card(x,y+j*step,v,size,dots)
    return s

def line(x1,y,x2=18.59):
    return rf'\draw[black!20,line width=.4pt] ({x1},{y}) -- ({x2},{y});'+'\n'

PRE=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[letterpaper,margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\begin{document}
'''

def packet(filename,level,pid,pages):
    source=PRE
    for i,body in enumerate(pages,1):
        source+=r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=-1cm]'+'\n'
        source+=r'\begin{scope}[shift={(current page.north west)}]'+'\n'
        source+=txt(1.5,.75,f'Week 23 / Sorting machines / {level}',width=18.59,size=11.5,leading=14)
        source+=r'\begin{scope}[shift={(1.5,1.8)}]'+'\n'+body+r'\end{scope}'+'\n'
        source+=txt(1.5,26.85,f'Bellingham Math Circle / Week 23 / {pid}',width=16.7,size=9,leading=11)
        source+=txt(19.3,26.85,str(i),width=.8,size=9,leading=11)
        source+=r'\end{scope}\end{tikzpicture}'+'\n'
        if i<len(pages):source+=r'\newpage'+'\n'
    source+=r'\end{document}'+'\n'
    (HERE/f'{filename}.tex').write_text(source)

k=[]
rules=r'Move left to right. A bar compares the two lanes with black dots: fewer dots go above, more dots below. Equal cards may stay put. Keep every bar fixed and move cards only at bars. A machine sorts when the cards finish in order from fewest dots at the top to most dots at the bottom.'
p=txt(0,0,rules,size=14,leading=18)
p+=problem(1,'Try every start. Circle the starts that finish in order.',size=17,y=3.7)
p+=network(3,[(1,2),(2,3)],y=6.0,gap=1.45,bar_xs=[6.5,11.7])
for j,v in enumerate(permutations([1,2,3])):
    x=[3.3,9.3,15.3][j%3]; y=[12.4,18.0][j//3]
    p+=start_column(v,x,y,step=1.05,size=.9,dots=True)
k.append(p)
p=problem(2,'Build a machine that sorts these three cards from every start. Use as few bars as you can.',size=17)
p+=bank([1,2,3],x=6,y=3,dots=True)
p+=network(3,[],y=6.0,gap=1.8)
p+=network(3,[],y=15.0,gap=1.8)
k.append(p)
p=problem(3,'Use the three cards. Find every start that makes either machine finish in the wrong order.',size=17)
p+=bank([1,2,3],x=6.0,y=3.0,dots=True)
p+=network(3,[(1,2),(2,3),(1,2)],y=6.0,gap=1.8)
p+=network(3,[(1,2),(1,2),(2,3)],y=15.0,gap=1.8)
k.append(p)
p=problem(4,'Build a machine that always sorts the left set but sometimes fails on the right set. Make another that always sorts the right set but sometimes fails on the left set.',size=17)
p+=bank([0,0,1],x=2.25,y=3.6,dots=True,step=1.7)
p+=bank([0,1,1],x=12.25,y=3.6,dots=True,step=1.7)
p+=network(3,[],y=7.0,gap=1.8)
p+=network(3,[],y=15.8,gap=1.8)
k.append(p)
p=problem(5,'Each machine needs one more bar at the right. Add it so that every start of the three cards finishes in order.',size=17)
p+=bank([1,2,3],x=6,y=3.25,dots=True)
for y,b in [(6,[(1,2),(2,3)]),(12,[(2,3),(1,2)]),(18,[(1,3),(1,2)])]:
    p+=network(3,b,y=y,gap=1.2,bar_xs=[5.0,9.0])
k.append(p)
p=problem(6,'Build a machine that sorts these four cards from every start. Use as few bars as you can.',size=17)
p+=bank([1,2,3,4],x=4.9,y=3,dots=True)
p+=network(4,[],y=6,gap=1.45)
p+=network(4,[],y=15,gap=1.45)
k.append(p)
packet('k-1',r'K--1','F23-K-v2',k)

rules=r'Move from left to right. At each bar, compare only the two lanes with black dots. Put the smaller value in the lower-numbered lane and the larger in the other. Ties may stay put. Keep every bar fixed for every start; move cards only at bars. A machine sorts when its final values increase from lane 1 downward, allowing ties.'
m=[]
p=txt(0,0,rules,size=12.5,leading=16)
p+=problem(1,'For each machine, find every starting order of 1, 2, 3 that it sorts. Which machines sort all starting orders?',size=14,y=3.1)
for y,b in [(6,[(1,2),(2,3)]),(12,[(2,3),(1,2)]),(18,[(1,3),(1,2),(2,3)])]:
    p+=network(3,b,y=y,gap=1.15)
m.append(p)
p=problem(2,'Build a three-lane machine that sorts every starting order of 1, 2, 3. Use as few bars as you can, and explain why fewer bars cannot work.',size=14)
p+=network(3,[],y=4.4,gap=1.5)
p+=network(3,[],y=11.4,gap=1.5)
m.append(p)
p=problem(3,'For each machine, add one bar at the right end so that it sorts every starting order of 1, 2, 3, 4. If one new bar cannot do it, explain why.',size=14)
for y,b in [(4.1,[(1,2),(3,4),(1,3),(2,4)]),(10.7,[(1,3),(2,4),(1,2),(3,4)]),(17.3,[(1,2),(3,4),(1,4),(2,3)])]:
    p+=network(4,b,y=y,gap=1.1,bar_xs=[4.4,6.5,8.6,10.7])
m.append(p)
p=problem(4,'Use the cards 0, 0, 1, 1. Find every different starting order and test it on this machine. Decide whether the machine also sorts every other four-card start made of 0s and 1s.',size=14)
p+=bank([0,0,1,1],x=4.9,y=3.5)
p+=network(4,[(1,2),(1,3),(2,3),(2,4)],y=6.0,gap=1.3)
m.append(p)
p=problem(5,'Build a four-lane machine that sorts every start made of 0s and 1s. Make a complete record of the starting arrangements you checked.',size=14)
p+=network(4,[],y=4.3,gap=1.3)
m.append(p)
p=problem(6,'Build a four-lane machine that sorts every order of 1, 2, 3, 4. Every bar must join neighboring lanes: 1 and 2, 2 and 3, or 3 and 4. Use as few bars as you can, and explain why fewer cannot work.',size=14)
p+=network(4,[],y=4.3,gap=1.4)
p+=network(4,[],y=14.4,gap=1.4)
m.append(p)
packet('grades-2-3','Grades 2--3','F23-23-v2',m)

o=[]
p=txt(0,0,rules,size=12.5,leading=16)
p+=problem(1,'For each machine, decide whether it sorts every order of 1, 2, 3. Give a failing start or a complete test record. Decide whether either machine can fail with 1, 1, 3 or 1, 3, 3.',size=13.5,y=3.1)
p+=network(3,[(1,2),(2,3)],y=6.1,gap=1.3)
p+=network(3,[(1,3),(1,2),(2,3)],y=13,gap=1.3)
o.append(p)
p=problem(2,'Build a four-lane machine that sorts every order of 1, 2, 3, 4. Use as few bars as you can.',size=13.5)
p+=network(4,[],y=4,gap=1.4)
p+=network(4,[],y=13.8,gap=1.4)
o.append(p)
p=txt(0,0,r'Example: choose $t=4$. Keep each card in its position.',size=12.5)
p+=txt(0,1.2,'Input',width=2.0,size=12)
p+=txt(0,2.6,'0--1 row',width=2.6,size=12)
for j,(value,result) in enumerate([(3,0),(7,1),(4,0)]):
    xx=4.3+j*1.6
    p+=card(xx,1.3,value,.90)+card(xx,2.75,result,.90)
    p+=rf'\draw[->,>=stealth] ({xx},1.83) -- ({xx},2.22);'+'\n'
p+=txt(10,1.12,r'At most 4 $\to$ 0\\Larger than 4 $\to$ 1',width=8.0,size=12)
p+=problem(3,r'Choose a number $t$. Replace a value by 0 when it is at most $t$, and by 1 when it is larger than $t$. For each start, find every different row of 0s and 1s that choosing $t$ can produce.',size=13.5,y=4.0)
for yy,values in [(7.0,[-2,8,5,8]),(11.0,[6,2,9,4]),(15.0,[4,4,4,4])]:
    p+=bank(values,x=.72,y=yy,size=1.12,step=1.42)
    p+=line(0,yy+2.3)
p+=txt(0,19.1,r'Can replacing values before a bar ever give different final 0s and 1s from replacing them after the bar? Explain for any two values and any $t$.',size=13.5)
o.append(p)
p=problem(4,'A fixed four-lane machine sorts every start made of 0s and 1s. Could some other start finish with 9 in lane 2 and 4 in lane 3? Explain. Decide whether sorting every 0--1 start guarantees sorting every start made of numbers, including repeats.',size=13.5)
p+=network(4,[],y=5.5,gap=1.5,outs=['',9,4,''])
p+=r'\draw[fill=white,line width=.7pt] (4.4,4.75) rectangle (13.65,10.75);'+'\n'
p+=txt(7.97,7.35,'?',width=2.0,size=25)
o.append(p)
p=problem(5,'Decide which machine sorts every start made of numbers. Give an explanation covering all inputs, including repeated values.',size=13.5)
p+=network(4,[(1,2),(3,4),(1,3),(2,4),(2,3)],y=4,gap=1.3)
p+=network(4,[(1,2),(3,4),(1,3),(2,3),(2,4)],y=13.1,gap=1.3)
o.append(p)
p=txt(0,0,r'Example: compare the same two lanes twice.',size=12.5)
p+=network(2,[(1,2),(1,2)],x=.25,y=1.6,w=13.8,gap=1.2,ins=[3,1],outs=[1,3],bar_xs=[5.1,9.6])
p+=txt(4.3,.85,'swap S',width=2.5,size=11)
p+=txt(8.8,.85,'stay N',width=2.5,size=11)
p+=card(7.4,1.6,1,.85)+card(7.4,2.8,3,.85)
p+=txt(14.8,1.5,'Record: SN',width=3.7,size=12)
p+=problem(6,'Write S when two cards swap at a bar and N when they stay put, in order from left to right. For each machine, find every record made by orders of 1, 2, 3, and find every start that makes each record.',size=13.5,y=4.0)
p+=network(3,[(1,2),(2,3)],y=7.4,gap=1.15,bar_xs=[6.5,11.7])
p+=network(3,[(1,2),(2,3),(1,2)],y=14.0,gap=1.15)
p+=txt(0,21.0,'Could a fixed machine sort two different starting orders of distinct cards while making the same swap/no-swap record? Explain.',size=13.5)
o.append(p)
p=problem(7,'Find the fewest bars a three-lane sorting machine can have and the fewest bars a four-lane sorting machine can have. Give a working machine for each and explain why fewer bars cannot work. Count each bar, even when two bars could happen at the same time.',size=13.5)
p+=network(3,[],y=4.7,gap=1.25)
p+=network(4,[],y=10.3,gap=1.25)
o.append(p)
packet('grades-4-5','Grades 4--5','F23-45-v2',o)

# Mathematical checks, kept out of student packets.
def run(values,bars):
    values=list(values)
    for a,b in bars:
        if values[a-1]>values[b-1]:values[a-1],values[b-1]=values[b-1],values[a-1]
    return tuple(values)
def passes(bars,starts):return all(run(s,bars)==tuple(sorted(s)) for s in starts)
three=list(permutations([1,2,3]));four=list(permutations([1,2,3,4]));binary=list(product([0,1],repeat=4))
S3=[(1,2),(2,3),(1,2)];S3b=[(1,3),(1,2),(2,3)];S4=[(1,2),(3,4),(1,3),(2,4),(2,3)]
assert passes(S3,three) and passes(S3b,three)
assert passes(S4,four) and passes(S4,binary)
for b,repair in [([(1,2),(2,3)],(1,2)), ([(2,3),(1,2)],(2,3)), ([(1,3),(1,2)],(2,3))]:assert passes(b+[repair],three)
P4=list(combinations(range(1,5),2)); P3=list(combinations(range(1,4),2))
assert not any(passes(b,three) for b in product(P3,repeat=2))
assert not any(passes(b,four) for b in product(P4,repeat=4))
weight2=[(1,2),(1,3),(2,3),(2,4)]
assert passes(weight2,[s for s in binary if sum(s)==2]) and not passes(weight2,binary)
repairs=[]
for b in [[(1,2),(3,4),(1,3),(2,4)],[(1,3),(2,4),(1,2),(3,4)],[(1,2),(3,4),(1,4),(2,3)]]:
    repairs.append({'bars':b,'working_last_bars':[bar for bar in P4 if passes(b+[bar],four)]})
assert repairs[0]['working_last_bars']==[(2,3)] and repairs[1]['working_last_bars']==[(2,3)] and repairs[2]['working_last_bars']==[]
wrong=[(1,2),(3,4),(1,3),(2,3),(2,4)]
report={'three_lane_sorters_verified':2,'four_lane_sorter_distinct_inputs':len(four),'four_lane_sorter_binary_inputs':len(binary),'length_4_four_lane_lists_audited':len(P4)**4,'repair_results':repairs,'weight_two_network_failures':[s for s in binary if run(s,weight2)!=tuple(sorted(s))],'older_problem_5_second_machine_failures':[s for s in binary if run(s,wrong)!=tuple(sorted(s))]}
(HERE/'math-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

# Fresh revision checks: selective binary sorting, neighboring lanes, and records.
from collections import defaultdict
small_binary=list(product([0,1],repeat=3))
left=[v for v in small_binary if sum(v)==1]
right=[v for v in small_binary if sum(v)==2]
left_machine=[(1,2),(2,3)]
right_machine=[(2,3),(1,2)]
assert passes(left_machine,left) and not passes(left_machine,right)
assert passes(right_machine,right) and not passes(right_machine,left)
adjacent=[(1,2),(2,3),(3,4)]
adjacent_sorter=[(1,2),(3,4),(2,3),(1,2),(3,4),(2,3)]
assert passes(adjacent_sorter,four) and passes(adjacent_sorter,binary)
assert not any(passes(b,four) for b in product(adjacent,repeat=5))
def records(bars):
    groups=defaultdict(list)
    for start in three:
        vals=list(start);record=''
        for a,b in bars:
            swap=vals[a-1]>vals[b-1]
            record+='S' if swap else 'N'
            if swap:vals[a-1],vals[b-1]=vals[b-1],vals[a-1]
        groups[record].append({'start':start,'finish':vals,'sorted':vals==sorted(vals)})
    assert all(sum(row['sorted'] for row in group)<=1 for group in groups.values())
    return dict(groups)
record_groups=[records(left_machine),records(S3)]
assert [len(g) for g in record_groups]==[4,6]
report['revision_checks']={
    'k1_problem_4_left_machine':left_machine,
    'k1_problem_4_right_machine':right_machine,
    'k1_left_machine_failures':[v for v in right if run(v,left_machine)!=tuple(sorted(v))],
    'k1_right_machine_failures':[v for v in left if run(v,right_machine)!=tuple(sorted(v))],
    'middle_problem_6_adjacent_sorter':adjacent_sorter,
    'middle_problem_6_length_5_lists_audited':len(adjacent)**5,
    'middle_problem_6_minimum':6,
    'middle_problem_6_lower_bound':'The reverse order 4,3,2,1 has six inverted pairs. Each adjacent swap removes exactly one; a no-swap removes none.',
    'older_problem_6_record_groups':record_groups,
    'older_problem_7_minima':[3,5],
    'older_problem_7_history_bound':'A fixed record applies one fixed permutation of distinct tokens. It can sort at most one input order; a k-bar machine has at most 2^k records.'
}
(HERE/'math-audit.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report['revision_checks'],indent=2))

# Guidance-revision notation examples: checked independently of the diagram code.
assert tuple(0 if v <= 4 else 1 for v in (3, 7, 4)) == (0, 1, 0)
_example = [3, 1]
_record = []
for _ in range(2):
    _swap = _example[0] > _example[1]
    _record.append('S' if _swap else 'N')
    _example.sort()
assert _example == [1, 3] and ''.join(_record) == 'SN'
