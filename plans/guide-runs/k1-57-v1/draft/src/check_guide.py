#!/usr/bin/env python3
"""Independent exact checks for the Week 57 K-1 adult section.

No student author/reviewer module is imported. Regions are unions of quarter-cell
triangles, encoded by their centroids on a six-times lattice. Boundary edges are
cancelled exactly; lattice-point incidence and boundary connectivity give dot
counts and reject gaps/pinches without using Pick's theorem. All half-piece
regions to size eight are generated, including inadmissible intermediate regions.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def student_pdf():
    direct = HERE.parent / 'k-1.pdf'
    if direct.is_file():
        return direct
    for root in HERE.parents:
        candidate = root / 'plans/k1-drafts/week-57/k-1.pdf'
        if candidate.is_file():
            return candidate
    raise FileNotFoundError('Place k-1.pdf beside src/ (or run inside the repository).')

# Quarter centroids in cell coordinates scaled by six: S, E, N, W.
Q = ((3,1),(5,3),(3,5),(1,3))

def half(x,y,o):
    return frozenset((6*x+Q[i][0],6*y+Q[i][1]) for i in (o,(o+1)%4))

def square(x,y):
    return frozenset((6*x+a,6*y+b) for a,b in Q)

def normal(s):
    dx = 6*(min(x for x,y in s)//6)
    dy = 6*(min(y for x,y in s)//6)
    return tuple(sorted((x-dx,y-dy) for x,y in s))

def transform(s,r,flip=False):
    out=[]
    for x,y in s:
        if flip: x=-x
        for _ in range(r): x,y=-y,x
        out.append((x,y))
    return out

def canonical(s,flips=True):
    return min(normal(transform(s,r,f)) for f in (False,True)[:1+flips] for r in range(4))

@lru_cache(None)
def vertices(q):
    x,y=q; cx,cy=x//6,y//6
    d=Q.index((x%6,y%6))
    corners=((2*cx,2*cy),(2*cx+2,2*cy),(2*cx+2,2*cy+2),(2*cx,2*cy+2))
    return (corners[d],corners[(d+1)%4],(2*cx+1,2*cy+1))

def edge(a,b): return tuple(sorted((a,b)))

def boundary(s):
    counts=Counter()
    for q in s:
        v=vertices(q)
        counts.update(edge(v[i],v[(i+1)%3]) for i in range(3))
    assert max(counts.values())<=2
    return {e for e,c in counts.items() if c==1}

def measure(s):
    incidence=Counter()
    for q in s:
        for x,y in vertices(q):
            if x%2==y%2==0: incidence[(x//2,y//2)]+=1
    inside={p for p,n in incidence.items() if n==8}
    outside={p for p,n in incidence.items() if 0<n<8}
    edges=boundary(s); graph=defaultdict(set)
    for a,b in edges: graph[a].add(b); graph[b].add(a)
    simple=all(len(v)==2 for v in graph.values())
    unseen=set(graph); components=0
    while unseen:
        components+=1; todo=[unseen.pop()]
        while todo:
            for p in graph[todo.pop()]:
                if p in unseen: unseen.remove(p); todo.append(p)
    return len(outside),len(inside),simple and components==1,inside

def fits(s,w,h):
    xs=[x//6 for x,y in s]; ys=[y//6 for x,y in s]
    a,b=max(xs)-min(xs)+1,max(ys)-min(ys)+1
    return (a<=w and b<=h) or (b<=w and a<=h)

def legal_join(region,new):
    if region & new: return False
    shared=boundary(region)&boundary(new)
    # A unit axis side is one full atom edge. The hypotenuse has two.
    axis=[e for e in shared if e[0][0]==e[1][0] or e[0][1]==e[1][1]]
    return bool(axis) or len(shared)==2

def enumerate_halves(nmax):
    levels={1:{canonical(half(0,0,0))}}
    for n in range(2,nmax+1):
        nxt=set()
        for shape in levels[n-1]:
            s=frozenset(shape); old_boundary=boundary(s)
            xs=[x//6 for x,y in s]; ys=[y//6 for x,y in s]
            for x in range(min(xs)-1,max(xs)+2):
                for y in range(min(ys)-1,max(ys)+2):
                    for o in range(4):
                        t=half(x,y,o)
                        if s&t: continue
                        shared=old_boundary & boundary(t)
                        if not shared: continue
                        axis=any(a[0]==b[0] or a[1]==b[1] for a,b in shared)
                        if axis or len(shared)==2: nxt.add(canonical(s|t))
        levels[n]=nxt
        print(f'Enumerated {n} halves: {len(nxt)} regions',flush=True)
    return levels

def polygon_data(poly):
    # Independent winding/cross product test and shoelace, no Pick dependency.
    twice=abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))
    b=i=0
    for x in range(min(p[0] for p in poly),max(p[0] for p in poly)+1):
        for y in range(min(p[1] for p in poly),max(p[1] for p in poly)+1):
            winding=0; on=False
            for (a,c),(d,e) in zip(poly,poly[1:]+poly[:1]):
                cross=(d-a)*(y-c)-(e-c)*(x-a)
                if cross==0 and min(a,d)<=x<=max(a,d) and min(c,e)<=y<=max(c,e): on=True
                if c<=y<e and cross>0: winding+=1
                if e<=y<c and cross<0: winding-=1
            if on: b+=1
            elif winding: i+=1
    return twice,b,i

P1=[[(0,0),(1,0),(0,1)],[(0,0),(1,0),(1,1),(0,1)],
    [(0,0),(2,0),(1,1)],[(0,0),(1,0),(2,1),(1,1)],
    [(0,0),(2,0),(2,1),(0,1)],[(0,0),(3,0),(2,1),(1,1)]]
DIAMOND=[(1,0),(2,1),(1,2),(0,1)]
HEXAGON=[(0,1),(1,0),(2,0),(3,1),(2,2),(1,2)]
TILTED=[(1,0),(3,2),(2,3),(0,1)]

# In each quadrant, the right angle of the chosen half is at (0,0).
QUADRANTS=[(0,0,3),(-1,0,0),(-1,-1,1),(0,-1,2)]

def four_piece(bits):
    return frozenset().union(*(square(x,y) if full else half(x,y,o)
        for (x,y,o),full in zip(QUADRANTS,bits)))

def run():
    pdf=student_pdf()
    text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
    pages=text.rstrip('\f\n').split('\f')
    assert len(pages)==7
    for p in range(1,8):
        assert f'Problem {p}:' in pages[p-1]
        assert f'Problem {p+1}:' not in pages[p-1]
    assert 'A turned shape' in pages[4] and 'both stars inside' in pages[5]
    assert 'whole sides' in pages[0] and 'A square counts as' in pages[0]
    # Pin the exact final diagrams, not merely the historical outline.
    expected='3eb8603152b88bac06f94aa54f59ee39c7afb76cf94b31c4ca52f6baad7bc28f'
    assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected,'Student PDF changed: recheck diagrams and page mapping.'
    assert [polygon_data(p) for p in P1]==[(1,3,0),(2,4,0),(2,4,0),(2,4,0),(4,6,0),(4,6,0)]
    assert polygon_data(DIAMOND)==(4,4,1)
    assert polygon_data(HEXAGON)==polygon_data(TILTED)==(8,6,2)
    # Kit/printing counts; one kit can cover all six P1 figures at once.
    assert 5*10+10==60 and 5*20+20==120 and 60*2==120
    assert 2*7==14 and 2*3==6
    assert sum(polygon_data(p)[0] for p in P1)==15<=20
    # Demonstration: 3x1 rectangle, three intact squares, not a numbered task instance.
    assert polygon_data([(0,0),(3,0),(3,1),(0,1)])==(6,8,0)
    levels=enumerate_halves(8)
    assert [len(levels[n]) for n in range(1,9)]==[1,3,4,14,30,107,318,1116]
    good={n:[s for s in ss if measure(s)[2]] for n,ss in levels.items()}
    for n,ss in good.items():
        for s in ss:
            b,i,_,_=measure(s)
            assert b+2*i==n+2
    assert len(good[3])==4 and {measure(s)[:2] for s in good[3]}=={(5,0)}
    assert all(fits(s,2,3) for s in good[3]+good[4])
    assert Counter(measure(s)[:2] for s in good[4])=={(6,0):13,(4,1):1}
    assert Counter(measure(s)[:2] for s in good[8])=={(10,0):1038,(8,1):65,(6,2):2}
    assert all(fits(s,3,4) for s in good[8] if measure(s)[0]<8)
    # Three pieces each offer at most a right angle at a lattice point.
    for t in [square(0,0)]+[half(0,0,o) for o in range(4)]:
        incidence=Counter(p for q in t for p in vertices(q) if p[0]%2==p[1]%2==0)
        assert max(incidence.values())==2 # 2 eighth-turns = one quarter-turn
    assert 3*2<8
    all4={canonical(four_piece(bits),False) for bits in product((0,1),repeat=4)}
    assert len(all4)==6
    assert sorted((len(s)//2,*measure(s)[:2]) for s in all4)==[(4,4,1),(5,5,1),(6,6,1),(6,6,1),(7,7,1),(8,8,1)]
    assert all(fits(s,2,2) for s in all4)
    # P6 requires positive coverage of every one of the six unit cells beside
    # (0,0),(1,0). Each uncut piece lies in one such cell: >=6 pieces.
    targets={(0,0),(1,0)}
    cells={(x,y) for X,Y in targets for x,y in ((X-1,Y-1),(X,Y-1),(X-1,Y),(X,Y))}
    assert len(cells)==6
    choices=[]
    for x,y in sorted(cells):
        needed={(2*X,2*Y) for X,Y in targets if X in (x,x+1) and Y in (y,y+1)}
        choices.append([t for t in [square(x,y)]+[half(x,y,o) for o in range(4)]
            if all(sum(p in vertices(q) for q in t)==2 for p in needed)])
    candidates=[frozenset().union(*ts) for ts in product(*choices)]
    assert len(candidates)==16
    assert all(targets<=measure(s)[3] and measure(s)[2] for s in candidates)
    assert len({canonical(s) for s in candidates})==7
    assert min(len(s)//2 for s in candidates)==8
    rect=frozenset().union(*(square(x,y) for x in (-1,0,1) for y in (-1,0)))
    assert measure(rect)[:2]==(10,2) and len(rect)//4==6
    guide=HERE.parent/'k1-guide.pdf'
    if guide.exists():
        gt=subprocess.check_output(['pdftotext','-layout',str(guide),'-'],text=True)
        assert len(gt.rstrip('\f\n').split('\f'))==4
        for p in range(1,8): assert f'Problem {p}, student page {p}' in gt
        for phrase in ['N57-K-FAC-v1','Three pieces cannot','Six shapes','Six pieces','six outline dots','outside the numbered packet']:
            assert phrase in gt,phrase
    print('PASS: seven final student pages pinned; all printed numerical answers; complete P5 catalog; P6 bound and constructions; half enumeration through eight; guide mapping.')

if __name__=='__main__': run()
