#!/usr/bin/env python3
"""Independent guide checker for printed tree graphs and grid triangles."""
from collections import deque, Counter
from itertools import combinations, product
from math import comb
import json

def graph(names,edges):
    g={a:set() for a in names}
    for a,b in edges:g[a].add(b);g[b].add(a)
    return g

def path(g,a,b):
    parents={a:None};q=deque([a])
    while b not in parents:
        u=q.popleft()
        for v in g[u]:
            if v not in parents:parents[v]=u;q.append(v)
    route=[b]
    while route[-1]!=a:route.append(parents[route[-1]])
    return route[::-1]

trees=[
 graph('abcdefghijkl',[('a','b'),('b','c'),('c','d'),('d','e'),('d','f'),('c','g'),('g','h'),('h','k'),('b','i'),('i','j'),('a','l')]),
 graph('abcdefghijk',[('a','b'),('b','c'),('c','d'),('d','e'),('b','f'),('f','g'),('f','h'),('d','i'),('i','j'),('i','k')])]
tree_triples=0
for g in trees:
    assert len(g)-1==sum(len(v) for v in g.values())//2
    for homes in combinations(g,3):
        routes=[path(g,a,b) for a,b in combinations(homes,2)]
        counts=Counter(frozenset((a,b)) for route in routes for a,b in zip(route,route[1:]))
        assert set(counts.values())=={2}
        for i,s in enumerate(routes):assert set(s)<=set().union(*(set(t) for j,t in enumerate(routes) if i!=j))
        tree_triples+=1
assert tree_triples==385

def gap(sides):
    # Grid graph distance, including uncolored interior roads.
    return max(min(abs(x-u)+abs(y-v) for j,t in enumerate(sides) if j!=i for u,v in t)
               for i,s in enumerate(sides) for x,y in s)

def routes(n):
    for right_slots in combinations(range(2*n),n):
        right_slots=set(right_slots);x=y=0;route=[(0,0)]
        for k in range(2*n):
            if k in right_slots:x+=1
            else:y+=1
            route.append((x,y))
        yield route

results={}
for n in (2,4,6):
    bottom=[(x,0) for x in range(n+1)]
    right=[(n,y) for y in range(n+1)]
    via_b=bottom+right[1:]
    assert gap([bottom,right,via_b])==0
    left_top=[(0,y) for y in range(n+1)]+[(x,n) for x in range(1,n+1)]
    assert gap([bottom,right,left_top])==n
    values=[gap([bottom,right,r]) for r in routes(n)]
    assert len(values)==comb(2*n,n)
    assert max(values)==n
    results[n]={'routes':len(values),'maximum_gap':max(values)}
assert [results[n]['routes'] for n in (2,4,6)]==[6,70,924]
# Validate the guide's general bound on a wider finite family; proof is separate.
for n in range(1,13):
    bottom=[(x,0) for x in range(n+1)];right=[(n,y) for y in range(n+1)]
    left_top=[(0,y) for y in range(n+1)]+[(x,n) for x in range(1,n+1)]
    assert gap([bottom,right,left_top])==n
# Review card, October 23, 2026 (GGT69-S-v3, GGT69-FAC-v3)
# Problem 3's middle board: homes A=(0,0), B=(4,2), C=(2,4); 15, 6 and 15 shortest routes;
# over all 1,350 road triangles the biggest gap is 3, only at (0,3) or (3,0)
def monotone(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1];sx=1 if dx>0 else -1;sy=1 if dy>0 else -1
    for xs in combinations(range(abs(dx)+abs(dy)),abs(dx)):
        p=a;r=[p]
        for i in range(abs(dx)+abs(dy)):
            p=(p[0]+sx,p[1]) if i in xs else (p[0],p[1]+sy);r.append(p)
        yield r
def gaps_at(sides):
    return {(i,p):min(abs(p[0]-u)+abs(p[1]-v) for j,t in enumerate(sides) if j!=i for u,v in t)
            for i,s in enumerate(sides) for p in s}
A,B,C=(0,0),(4,2),(2,4)
S=[list(monotone(A,B)),list(monotone(B,C)),list(monotone(C,A))]
assert [len(x) for x in S]==[15,6,15]
best=0;where=set();n_tri=0
for ab in S[0]:
    for bc in S[1]:
        for ca in S[2]:
            g=gaps_at([ab,bc,ca]);m=max(g.values());n_tri+=1
            if m>best:best,where=m,set()
            if m==best:where|={p for (i,p),v in g.items() if v==m}
assert (n_tri,best,where)==(1350,3,{(0,3),(3,0)})
# the guide's example triangle and the child's bound
ex=[[(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2)],[(4,2),(3,2),(3,3),(3,4),(2,4)],[(2,4),(1,4),(0,4),(0,3),(0,2),(0,1),(0,0)]]
assert all(len(r)-1==abs(r[0][0]-r[-1][0])+abs(r[0][1]-r[-1][1]) for r in ex)
assert gaps_at(ex)[(2,(0,3))]==3
assert max(min(abs(x-u)+abs(y-v) for u,v in (A,B,C)) for x in range(5) for y in range(5))==3
# Problem 2's key: AC up 2, right 4, up 2; biggest gap 2, at the dot two up from A
bottom=[(x,0) for x in range(5)];right=[(4,y) for y in range(5)]
ac=[(0,0),(0,1),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(4,4)]
g=gaps_at([bottom,right,ac])
assert max(g.values())==2 and g[(2,(0,2))]==2 and sorted(p for (i,p),v in g.items() if v==2)==[(0,2),(1,2),(2,0),(2,2)]
# printed wording
import pathlib
here=pathlib.Path(__file__).resolve().parent
guide=(here/'facilitator.tex').read_text()
student=(here.parent/'student'/'students.tex').read_text()
for phrase in ['GGT69-FAC-v3','take AC up 2, right 4, up 2','its gap is \\textbf{2}','Save the left/top choice of AC for Problem 3','so do the next two dots along AC and the middle dot of AB',
               'A $(0,0)$, B $(4,2)$, C $(2,4)$ & 6, 4, 6 & 15, 6, 15 & \\textbf{3}','reached only at $(0,3)$ or $(3,0)$',
               'within 3 steps of a home','two extra copies of pages 1 and 3 per pair','marked A, B and C',
               'colour it after the partner\'s check','Younger tables','1,350 road triangles']:
    assert phrase in guide, phrase
for phrase in ['Its gap is \\textbf{4}','mark-and-erase','All student and guide pages were digitally inspected']:
    assert phrase not in guide, phrase
for phrase in ['GGT69-S-v3','the nearer of the other two colored sides','have a gap bigger than 0?',
               '\\grid{4}\\home{0}{0}{A}\\home{4}{2}{B}\\home{2}{4}{C}']:
    assert phrase in student, phrase
assert 'positive gap' not in student and 'either of the other two' not in student
p2=student.split('\\problem{2}')[1].split('\\newpage')[0]
assert '\\rule' not in p2
print(json.dumps({'status':'PASS','tree_distinct_triples':tree_triples,'grid_results':results,
 'P2':[0,2],'P3_middle_board':{'triangles':1350,'maximum_gap':3,'at':[[0,3],[3,0]]},'scope':'Finite enumeration verifies printed instances; proofs in the guide establish all trees and arbitrarily large gaps.'},indent=2))
