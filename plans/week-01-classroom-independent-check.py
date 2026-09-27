#!/usr/bin/env python3
"""Independent geometry/packing audit; does not import author checkers.

Reads polygon data as the specification, constructs cells with exact winding
numbers, and enumerates physical purple placements by transformed vertex sets.
Verifies generated TikZ diagrams by reading their coordinates back to the lattice.
"""
from pathlib import Path
import json
from itertools import combinations
from functools import lru_cache
from math import sqrt
import re

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'week-01-classroom-middle-checks.json').read_text())
TEX=(ROOT/'../lowell-math-circle-year-2/source/week-01/middle-geometry.tex').resolve().read_text()

def triangle(i,j,up):
    return frozenset([(i,j),(i+1,j),(i,j+1)] if up else [(i+1,j),(i,j+1),(i+1,j+1)])

def inside3(q,poly):
    # q is three times the centroid; signed winding number, all integer arithmetic.
    wn=0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ay,by=3*a[1],3*b[1]
        det=(b[0]-a[0])*(q[1]-3*a[1])-(b[1]-a[1])*(q[0]-3*a[0])
        if ay<=q[1]<by and det>0: wn+=1
        if by<=q[1]<ay and det<0: wn-=1
    return wn!=0

def cells(poly):
    out=set()
    for i in range(min(p[0] for p in poly)-1,max(p[0] for p in poly)+1):
        for j in range(min(p[1] for p in poly)-1,max(p[1] for p in poly)+1):
            for isup in [True,False]:
                c=triangle(i,j,isup)
                if inside3(tuple(sum(p[k] for p in c) for k in [0,1]),poly): out.add(c)
    return frozenset(out)

def rotate(p): return (-p[1],p[0]+p[1])
def reflect(p): return (p[0]+p[1],-p[1])

def purple_placements(board, reflections=False):
    # The chevron is this explicit four-triangle chain, independent of polygon code.
    seed=frozenset([triangle(0,0,True),triangle(0,0,False),triangle(0,1,True),triangle(-1,1,False)])
    shapes=[]
    for mirror in range(2 if reflections else 1):
        cur=frozenset(frozenset(reflect(v) if mirror else v for v in c) for c in seed)
        for _ in range(6):
            shapes.append(cur)
            cur=frozenset(frozenset(rotate(v) for v in c) for c in cur)
    vertices=set().union(*board)
    result=set()
    for shape in shapes:
        origin=next(iter(next(iter(shape))))
        for anchor in vertices:
            dx,dy=anchor[0]-origin[0],anchor[1]-origin[1]
            candidate=frozenset(frozenset((x+dx,y+dy) for x,y in c) for c in shape)
            if candidate<=board: result.add(candidate)
    return result

def blue_placements(board):
    return {frozenset([a,b]) for a,b in combinations(board,2) if len(a&b)==2}

def optimum(board,placements):
    # Enumerate reachable unions of disjoint placements, one piece count at a time.
    # This is a different exhaustive state space from the author's uncovered-cell DP.
    ix={c:i for i,c in enumerate(board)}
    masks={sum(1<<ix[c] for c in p) for p in placements}
    reachable={0}
    k=0
    while True:
        nxt={mask|p for mask in reachable for p in masks if not mask&p}
        if not nxt: return k
        k+=1
        reachable=nxt


def decode_path(s):
    out=[]
    for x,y in re.findall(r'\((-?[0-9.]+),(-?[0-9.]+)\)',s):
        a,b=float(x),float(y)
        v=round(b*2/sqrt(3));u=round(a-v/2)
        assert abs(a-(u+v/2))<1e-8 and abs(b-v*sqrt(3)/2)<1e-8
        out.append((u,v))
    return out

def commands(name):
    line=next(line for line in TEX.splitlines() if r'\csname '+name+r'\endcsname{' in line)
    return [(style,decode_path(path)) for style,path in re.findall(r'\\draw\[([^]]+)\]\s*([^;]+);',line)]

def cell_name(c):
    for i in range(-3,6):
        for j in range(-3,6):
            for isup in [True,False]:
                if c==triangle(i,j,isup): return ('U' if isup else 'D')+f'({i},{j})'
    raise ValueError(c)

for name,d in DATA.items():
    board=cells(d['polygon'])
    supplied=frozenset(frozenset(map(tuple,c)) for c in d['cells'])
    assert supplied==board,(name,'cells disagree with polygon')
    up=sum(sum(v==min(y for x,y in c) for u,v in c)==2 for c in board)
    assert (len(board),up,len(board)-up)==(d['total'],d['up'],d['down'])
    area2=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(d['polygon'],d['polygon'][1:]+d['polygon'][:1])))
    assert area2==len(board)
    grid=commands('MiddleGrid'+name)
    assert {frozenset(p) for style,p in grid if style=='gridline'}==board
    assert [p for style,p in grid if style=='outline']==[list(map(tuple,d['polygon']))]
    for color,ps in [('blue',blue_placements(board)),('purple',purple_placements(board))]:
        k=optimum(board,ps)
        assert k==d[color]['pieces'],(name,color,k,d[color]['pieces'])
        assert len(ps)==d[color]['legal_placements']
        all_covered=set()
        for poly in d[color]['placements']:
            cs=cells(poly)
            assert cs in ps and not(cs&all_covered)
            all_covered|=cs
        assert len(board-all_covered)==d[color]['gaps']
        graphics=commands('MiddlePacking'+name+color)
        drawn=[p for style,p in graphics if style.startswith('tile,')]
        assert drawn==[list(map(tuple,p)) for p in d[color]['placements']]
    # Turning the physical piece over adds no new chevron shapes or packings.
    assert purple_placements(board,True)==purple_placements(board)
    print(name, 'area/up/down',len(board),up,len(board)-up,
          'minimum blue/purple gaps',d['blue']['gaps'],d['purple']['gaps'])

b=cells(DATA['ThreeB']['polygon'])
ps=purple_placements(b)
print('Diamond purple placements:')
for p in sorted(ps,key=lambda p:sorted(cell_name(c) for c in p)):
    print(' ',sorted(cell_name(c) for c in p))
assert all(a&b for a,b in combinations(ps,2))
# Human proof checks: the acute tip cells are never covered by a chevron.
assert all(triangle(0,0,True) not in p and triangle(1,1,False) not in p for p in ps)
# Force the unique blue tiling by repeatedly taking a cell with one partner.
remaining=set(b)
forced=[]
while remaining:
    pairs=blue_placements(remaining)
    c=next(c for c in remaining if sum(c in p for p in pairs)==1)
    pair=next(p for p in pairs if c in p)
    forced.append(pair)
    remaining-=pair
assert len(forced)==4
# In the diamond all four forced rhombi share the same internal-edge direction.
def join_direction(pair):
    a,b=tuple(set.intersection(*(set(c) for c in pair)))
    d=(b[0]-a[0],b[1]-a[1])
    return min(d,(-d[0],-d[1]))
assert len({join_direction(p) for p in forced})==1
# Any chevron has a unique two-blue subdivision, with different orientations.
for p in ps:
    splits=[(a,b) for a,b in combinations(blue_placements(p),2) if a|b==p and not a&b]
    assert len(splits)==1 and join_direction(splits[0][0])!=join_direction(splits[0][1])
print('PASS: all 6 possible chevrons in the diamond intersect pairwise.')
print('PASS: all data counts, optima, witnesses, and generated TikZ coordinates agree.')
