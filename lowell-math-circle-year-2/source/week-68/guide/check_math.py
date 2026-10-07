#!/usr/bin/env python3
"""Independent finite graph checks for the exact guide examples.
Infinite conclusions require the exterior/tail proofs in facilitator.tex.
"""
from collections import deque
from itertools import combinations, product
import json

def graph(vertices,edges):
    g={v:set() for v in vertices}
    for a,b in edges: g[a].add(b);g[b].add(a)
    return g

def components(g,blocked):
    todo=set(g)-set(blocked); ans=[]
    while todo:
        root=next(iter(todo)); todo.remove(root); found={root}; stack=[root]
        while stack:
            a=stack.pop()
            for b in g[a]&todo: todo.remove(b);found.add(b);stack.append(b)
        ans.append(found)
    return ans

def distances(g,start,blocked):
    d={start:0};q=deque([start])
    while q:
        a=q.popleft()
        for b in g[a]-blocked:
            if b not in d:d[b]=d[a]+1;q.append(b)
    return d

line=graph(range(-8,9),[(x,x+1) for x in range(-8,8)])
for k in (1,2,4):
    for blocked in combinations(range(-4,5),k):
        cs=components(line,blocked)
        assert sum(bool(c&{-8,8}) for c in cs)==2
cs=components(line,{-3,-1,0,2})
assert sorted(sorted(c) for c in cs if not c&{-8,8})==[[-2],[1]]
assert [x+5 for x in (-3,-1,0,2)]==[2,4,5,7]
assert [-2+5,1+5]==[3,6]

vs=list(product(range(-7,8),range(2)))
ladder=graph(vs,[(a,b) for a,b in combinations(vs,2) if abs(a[0]-b[0])+abs(a[1]-b[1])==1])
assert len(components(ladder,{(0,0)}))==1
assert len(components(ladder,{(0,0),(0,1)}))==2
assert len(components(ladder,{(0,0),(1,0)}))==1
border={(-7,0),(-7,1),(7,0),(7,1)}
for blocked in combinations(list(product(range(-2,3),range(2))),4):
    assert sum(bool(c&border) for c in components(ladder,blocked))<=2
cs=components(ladder,{(-1,0),(-1,1),(1,0),(1,1)})
assert {frozenset(c) for c in cs if not c&border}=={frozenset({(0,0),(0,1)})}

vs=list(product(range(-5,6),repeat=2))
grid=graph(vs,[(a,b) for a,b in combinations(vs,2) if abs(a[0]-b[0])+abs(a[1]-b[1])==1])
cs=components(grid,{(1,0),(-1,0),(0,1),(0,-1)})
assert len(cs)==2 and {(0,0)} in cs
wall={(0,y) for y in range(-2,3)}
assert len(components(grid,wall))==1
assert distances(grid,(-2,0),wall)[(2,0)]==10
p=(-2,0)
for dx,dy in [(0,1)]*3+[(1,0)]*4+[(0,-1)]*3:
    p=(p[0]+dx,p[1]+dy);assert p not in wall
assert p==(2,0)

# A depth-6 window of the 3-regular tree: center has three children;
# every other nonterminal vertex has two. Only this explicit rule is used.
verts=[()];edges=[]
for depth in range(6):
    for v in [v for v in verts if len(v)==depth]:
        for k in range(3 if not v else 2):
            nxt=v+(k,);verts.append(nxt);edges.append((v,nxt))
tree=graph(verts,edges);counts=[];blocked_counts=[]
for r in range(4):
    blocked={v for v in verts if len(v)<=r}
    cs=components(tree,blocked)
    assert all(any(len(v)==6 for v in c) for c in cs)
    counts.append(len(cs));blocked_counts.append(len(blocked))
assert counts==[3,6,12,24]
assert blocked_counts==[1,4,10,22]
print(json.dumps({'status':'PASS','P1':[2,2,2],'P2_blocked_visible_dots':[2,4,5,7],
 'P2_trapped_visible_dots':[3,6],'P5_wall_shortest_route':10,'P7_P8':counts,
 'blocked_vertices_by_radius':blocked_counts,
 'scope':'Finite windows check examples only. Tails, connected exterior, and continuing-tree proofs handle infinity.'},indent=2))
