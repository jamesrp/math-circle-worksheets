from pathlib import Path
import math, itertools, json
from collections import deque

ROOT = Path(__file__).resolve().parent
FINAL = ROOT.parent

# Independent enumeration by pairwise noncrossing diagonal sets.
def diagonals(n):
    return [(a,b) for a in range(n) for b in range(a+1,n) if b-a>1 and (a,b)!=(0,n-1)]
def cross(e,f):
    a,b=e; c,d=f
    return (a<c<b<d) or (c<a<d<b)
def fillings(n):
    return [frozenset(t) for t in itertools.combinations(diagonals(n),n-3)
            if all(not cross(a,b) for a,b in itertools.combinations(t,2))]
def graph(ts):
    return {t:[s for s in ts if len(t^s)==2] for t in ts}
def dist(g,s,t):
    q=deque([(s,0)]); seen={s}
    while q:
        u,d=q.popleft()
        if u==t: return d
        for v in g[u]:
            if v not in seen: seen.add(v); q.append((v,d+1))
def fan(n,v):
    return frozenset(e for e in diagonals(n) if v in e)
def es(*pairs): return frozenset((min(a,b)-1,max(a,b)-1) for a,b in pairs)

T={n:fillings(n) for n in range(3,9)}
G={n:graph(ts) for n,ts in T.items()}
assert [len(T[n]) for n in range(3,9)] == [1,2,5,14,42,132]
hex_fan_b=fan(6,1)
hex_center=es((1,3),(3,5),(1,5))
hex_fan_d=fan(6,3)
oct_start=es((1,3),(1,4),(4,6),(4,7),(4,8))
oct_end=es((2,4),(2,5),(5,7),(5,8),(1,5))
for n,s in [(6,hex_fan_b),(6,hex_center),(6,hex_fan_d),(8,oct_start),(8,oct_end)]:
    assert s in T[n]
checks={
    'counts':{n:len(ts) for n,ts in T.items()},
    'pentagon_graph_degrees':[len(G[5][t]) for t in T[5]],
    'k1_fixed_line_counts':{
        'pentagon_1_3':sum((0,2) in t for t in T[5]),
        'hexagon_1_4':sum((0,3) in t for t in T[6])},
    'upper_problem_4_distances':[dist(G[6],s,fan(6,0)) for s in [hex_fan_b,hex_center,hex_fan_d]],
    'upper_problem_5_distances':{c:dist(G[8],oct_start,fan(8,v)) for c,v in [('A',0),('E',4)]},
    'upper_problem_7_distance':dist(G[8],oct_start,oct_end),
    'fan_distance_checked_for_all_octagons':all(dist(G[8],s,fan(8,v))==5-sum(v in e for e in s) for s in T[8] for v in range(8))
}
assert checks['upper_problem_4_distances']==[3,1,2]
assert checks['upper_problem_5_distances']=={'A':3,'E':5}
assert checks['fan_distance_checked_for_all_octagons']
(ROOT/'mathematical-checks.json').write_text(json.dumps(checks,indent=2)+'\n')

# All coordinates are in inches from the page's top left.
# Thick outlines and vertex dots remain legible on a monochrome copier.
def text(x,y,w,s,size=14,bold=False):
    style='\\bfseries ' if bold else ''
    return (rf'\node[anchor=north west,inner sep=0pt,text width={w}in,align=left,'
            rf'font=\sffamily\fontsize{{{size}}}{{{size*1.25:.2f}}}\selectfont] at ({x},{y}) '
            '{'+style+s+'};\n')

def polygon(n,cx,cy,w,h,edges=(),labels='numbers',small=False,regular=True):
    # Use one physical scale for every regular board, fitted inside its layout box.
    # The small flip examples explicitly opt out to preserve general quadrilaterals.
    raw=[(math.cos(math.pi/2-2*math.pi*i/n),-math.sin(math.pi/2-2*math.pi*i/n)) for i in range(n)]
    xmin=min(x for x,y in raw); xmax=max(x for x,y in raw)
    ymin=min(y for x,y in raw); ymax=max(y for x,y in raw)
    sx=w/(xmax-xmin); sy=h/(ymax-ymin)
    if regular: sx=sy=min(sx,sy)
    pts=[(cx+(x-(xmin+xmax)/2)*sx,cy+(y-(ymin+ymax)/2)*sy) for x,y in raw]
    p='\\begin{scope}\n' + f'% polygon: {"regular" if regular else "general-convex"} n={n}\n'
    for i,(x,y) in enumerate(pts): p+=rf'\coordinate (v{i}) at ({x:.4f},{y:.4f});'+'\n'
    p+=r'\draw[line width=0.95pt,line join=round] '+' -- '.join(f'(v{i})' for i in range(n))+r' -- cycle;'+'\n'
    for a,b in sorted(edges): p+=rf'\draw[line width=0.85pt] (v{a}) -- (v{b});'+'\n'
    for i,(x,y) in enumerate(pts):
        p+=rf'\fill (v{i}) circle[radius={0.014 if small else 0.022}in];'+'\n'
        # Outward label offsets in physical units, independent of polygon aspect ratio.
        dx=x-cx; dy=y-cy; norm=math.hypot(dx,dy)
        off=0.12 if small else 0.19
        lx=x+off*dx/norm; ly=y+off*dy/norm
        lab=str(i+1) if labels=='numbers' else chr(65+i)
        p+=rf'\node[inner sep=0pt,font=\sffamily\fontsize{{{8 if small else 13}}}{{14}}\selectfont] at ({lx:.4f},{ly:.4f}) {{{lab}}};'+'\n'
    return p+'\\end{scope}\n'

class Packet:
    def __init__(self,filename,level,code,k=False):
        self.filename=filename; self.level=level; self.code=code; self.k=k; self.pages=[]
    def page(self,number,problem,drawings,rule=None):
        s='\\begin{tikzpicture}[remember picture,overlay,x=1in,y=-1in]\n'
        s+='\\begin{scope}[shift={(current page.north west)}]\n'
        s+=text(.55,.36,7.4,rf'Week 14 / Polygon triangulations and flips / {self.level}',10.8,True)
        top=.91
        if rule:
            s+=text(.65,.91,7.2,rule,12.3)
            top=1.78
        s+=text(.65,top,7.2,rf'\textbf{{Problem {number}:}} '+problem,14.2 if self.k else 13.4)
        s+=drawings
        s+=text(.55,10.48,6.9,rf'Bellingham Math Circle / Week 14 / {self.code}',9)
        s+=text(7.56,10.48,.36,str(len(self.pages)+1),9)
        s+='\\end{scope}\n\\end{tikzpicture}\n\\null\n'
        self.pages.append(s)
    def save(self):
        pre=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0in]{geometry}
\pdfmapfile{+cm.map}
\usepackage{type1cm}
\usepackage{tikz}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''
        (ROOT/(self.filename+'.tex')).write_text(pre+'\\newpage\n'.join(self.pages)+'\\end{document}\n')

# Small polygons are recording copies; investigations retain a larger working polygon.
def copies(n,rows,cols,starty,labels='numbers',rowgap=1.30,w=1.35,h=.87):
    xs=[.95+i*(6.60/(cols-1)) for i in range(cols)] if cols>1 else [4.25]
    # Center copies in a narrower horizontal range when only three columns are used.
    if cols==3: xs=[1.45,4.25,7.05]
    if cols==4: xs=[1.35,3.28,5.22,7.15]
    return ''.join(polygon(n,x,starty+r*rowgap,w,h,labels=labels,small=True) for r in range(rows) for x in xs)
def large_plus_copies(n,edges=(),labels='numbers',topcy=4.25,copyy=7.45):
    if n==6:
        return polygon(n,4.25,topcy,4.8,4.40,edges,labels)+copies(n,2,4,7.55,labels,rowgap=1.78,w=1.30,h=1.30)
    return polygon(n,4.25,topcy,4.8,3.35,edges,labels)+copies(n,2,4,copyy,labels,rowgap=1.50,w=1.30,h=.92)
def map_drawings():
    positions=[(2.00,4.05),(6.25,4.25),(6.65,6.90),(4.25,9.00),(1.55,6.65)]
    order=[0,2,4,1,3]
    assert all(fan(5,order[(i+1)%5]) in G[5][fan(5,order[i])] for i in range(5))
    example=polygon(4,1.35,2.47,.95,.60,es((1,3)),'letters',True,regular=False)+polygon(4,3.20,2.47,.95,.60,es((2,4)),'letters',True,regular=False)
    example+=r'\draw[rounded corners=2pt,black!55] (.65,1.94) rectangle (2.05,3.00); \draw[rounded corners=2pt,black!55] (2.50,1.94) rectangle (3.90,3.00); \draw[line width=.8pt] (2.05,2.47)--(2.50,2.47);'+'\n'
    example+=text(4.02,2.12,3.60,'Example: erase AC, draw BD. The join connects whole fillings; it is not an inside line.',11.5)
    return example+''.join(polygon(5,x,y,1.9,1.40,fan(5,j),'letters') for (x,y),j in zip(positions,order))

def first_page_pair(n1,n2,labels='numbers'):
    drawings=''
    for n,y in [(n1,4.20),(n2,8.05)]:
        if n==7 and n1==6: y=8.25
        if n==6:
            if n==n1: y=4.35
            drawings+=polygon(n,3.00,y,4.20,3.50,labels=labels)
            for dy in [-.97,.97]:
                drawings+=polygon(n,6.70,y+dy,1.50,1.35,labels=labels,small=True)
        else:
            drawings+=polygon(n,3.00,y,4.20,2.80,labels=labels)
            for dy in [-.80,.80]:
                drawings+=polygon(n,6.70,y+dy,1.50,1.05,labels=labels,small=True)
    return drawings

def two_cases_with_records(n1,n2,e1=(),e2=(),labels='numbers',keep_edges=False):
    drawings=''
    for n,y,edges in [(n1,3.05,e1),(n2,7.10,e2)]:
        if n==6:
            cy=3.75 if y<5 else 8.00
            drawings+=polygon(n,2.35,cy,4.80,3.45,edges,labels)
            for x in [5.25,7.15]:
                for dy in [-.90,.90]:
                    drawings+=polygon(n,x,cy+dy,1.30,1.30,edges if keep_edges else (),labels,small=True)
        else:
            drawings+=polygon(n,4.25,y,4.80,2.30,edges,labels)
            for x in [1.35,3.28,5.22,7.15]:
                drawings+=polygon(n,x,y+2.00,1.30,.80,edges if keep_edges else (),labels,small=True)
    return drawings

def three_routes():
    drawings=''
    for x,edges in zip([1.65,4.25,6.85],[hex_fan_b,hex_center,hex_fan_d]):
        drawings+=polygon(6,x,2.50,1.75,1.50,edges,'letters',True)
    drawings+=polygon(6,4.25,4.50,1.75,1.50,fan(6,0),'letters',True)
    drawings+=polygon(6,2.35,7.70,4.80,4.00,labels='letters')
    for x in [5.25,7.15]:
        for y in [5.70,7.05,8.40,9.75]:
            drawings+=polygon(6,x,y,1.30,.95,labels='letters',small=True)
    return drawings

krules='Join printed corners with straight lines. Lines inside a shape may meet at corners but may not cross. Fill the whole shape with triangles. Keep the corner numbers fixed. Use tracing paper to change printed lines.'
rules='Fill the whole polygon with triangles, using straight lines between printed corners. Lines inside a polygon may meet at corners but may not cross. Keep the corner labels fixed, even if you turn the page. Use tracing paper to change printed lines.'

k=Packet('k-1','K--1','F14-K-v2',True)
k.page(1,'Fill each shape with triangles in two different ways.',first_page_pair(5,6),krules)
k.page(2,'Find every way to fill this five-corner shape with triangles.',large_plus_copies(5))
k.page(3,'Can you fill this shape with 3 triangles, or with 4 triangles? Explain why any impossible case cannot work.',large_plus_copies(6))
k.page(4,'Fill each shape with triangles, keeping the printed line. Find every way.',two_cases_with_records(5,6,es((1,3)),es((1,4)),keep_edges=True))
k.page(5,'Erase one inside line and draw a different one. Keep the shape full of triangles and find every possible result from each drawing.',two_cases_with_records(6,6,fan(6,0),hex_center))
k.page(6,'Start with this filling and change one inside line at a time. Can you visit every other filling once and then return?',large_plus_copies(5,fan(5,0)))
k.save()

m=Packet('grades-2-3','Grades 2--3','F14-23-v2')
m.page(1,'Fill each polygon in two different ways. Can the two fillings of one polygon have different numbers of triangles?',first_page_pair(6,7,labels='letters'),rules)
m.page(2,'Find every filling of this five-corner polygon. Organize your drawings so that you can explain why none are missing.',large_plus_copies(5,labels='letters'))
m.page(3,'Erase one inside line and replace it with a different line so the polygon stays filled with triangles. Find every result of one such change from each drawing.',two_cases_with_records(6,6,fan(6,0),hex_center,'letters'))
m.page(4,'A change of one inside line that keeps the polygon filled with triangles is called a flip. Join two drawings when one flip changes one into the other. Include every possible join.',map_drawings())
m.page(5,'Start with this filling and return to it after an odd number of flips. Show every filling along your route.',large_plus_copies(5,fan(5,0),'letters'))
m.page(6,'Change the first filling into the second using as few flips as you can. Find another route with a different number of flips, without visiting any filling twice.',polygon(6,2.05,2.85,2.15,1.85,hex_fan_b,'letters')+polygon(6,6.35,2.85,2.15,1.85,fan(6,0),'letters')+r'\draw[-stealth,line width=.8pt] (3.45,2.85) -- (4.95,2.85);'+'\n'+polygon(6,4.25,5.90,4.8,3.80,labels='letters')+copies(6,2,4,8.38,'letters',rowgap=1.40,w=1.30,h=.96))
m.page(7,'Find every filling of this six-corner polygon. Organize your drawings so you can tell whether any are missing or repeated.',large_plus_copies(6,labels='letters'))
m.page('7 (continued)','Extra hexagons for your collection. Use these to continue Problem 7 on the previous page.',copies(6,3,3,2.75,'letters',rowgap=2.85,w=1.80,h=2.00))
m.save()

u=Packet('grades-4-5','Grades 4--5','F14-45-v2')
u.page(1,'Find every filling of the five-corner polygon. Explain how your collection shows that none are missing.',large_plus_copies(5,labels='letters',topcy=4.6,copyy=7.85),rules)
u.page(2,'Erase one inside line and replace it with a different line so the polygon stays filled with triangles. Find every result of one such change from each drawing.',two_cases_with_records(6,6,fan(6,0),hex_center,'letters'))
u.page(3,'A change of one inside line that keeps the polygon filled with triangles is called a flip. Join two drawings when one flip changes one into the other. Include every possible join. Can you return to a filling after an odd number of flips? Show a route, or explain why it is impossible.',map_drawings())
u.page(4,'Change each of the three starting fillings into the fourth filling using as few flips as possible. Explain why no shorter routes can work.',three_routes())
u.page(5,'A filling whose inside lines all meet at one corner is called a fan. Find the fewest flips from this filling to a fan at A, and to a fan at E. Explain why each route is shortest.',large_plus_copies(8,oct_start,'letters',topcy=4.4,copyy=7.7))
u.page(6,'Find a rule for the fewest flips needed to turn any filling into a fan at A. Explain why your rule works for every starting filling and every number of corners, when all corners point outward.',polygon(8,4.25,4.35,4.8,3.6,labels='letters'))
u.page(7,'Find a route of flips between these two fillings. Can any two fillings of the same polygon be joined by flips? Explain why your answer works for any polygon with no inward-pointing corners.',polygon(8,2.05,3.0,2.15,1.65,oct_start,'letters')+polygon(8,6.35,3.0,2.15,1.65,oct_end,'letters')+r'\draw[-stealth,line width=.8pt] (3.45,3.0) -- (4.95,3.0);'+'\n'+polygon(8,4.25,6.10,4.8,3.0,labels='letters'))
u.save()
print(json.dumps(checks,indent=2))
print('Created source packets:',[(p.filename,len(p.pages)) for p in [k,m,u]])
