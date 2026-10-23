#!/usr/bin/env python3
"""Independent shortest-road guide check, without student code or dependencies."""
from collections import deque
from itertools import combinations, product
import json

def graph(vertices, edges):
    g={v:set() for v in vertices}
    for a,b in edges:
        g[a].add(b); g[b].add(a)
    return g

def distances(g):
    out={}
    for start in g:
        row={start:0}; q=deque([start])
        while q:
            a=q.popleft()
            for b in g[a]:
                if b not in row: row[b]=row[a]+1; q.append(b)
        assert len(row)==len(g)
        out[start]=row
    return out

def meetings(g, d, homes):
    return {m for m in g if all(d[a][m]+d[m][b]==d[a][b] for a,b in combinations(homes,2))}

verts=list(product(range(5),repeat=2))
g=graph(verts,[(a,b) for a,b in combinations(verts,2) if sum(abs(x-y) for x,y in zip(a,b))==1]); d=distances(g)
assert meetings(g,d,[(0,0),(4,1),(1,4)]) == {(1,1)}
assert meetings(g,d,[(0,3),(4,0),(4,4)]) == {(4,3)}
triples=0
for homes in combinations(verts,3):
    med=tuple(sorted(h[k] for h in homes)[1] for k in range(2))
    assert meetings(g,d,homes)=={med}; triples+=1
assert [d[a][b] for a,b in combinations([(0,0),(4,1),(1,4)],2)]==[5,5,6]
assert [d[a][b] for a,b in combinations([(0,3),(4,0),(4,4)],2)]==[7,5,4]
# Exact student tree. Lowercase letters are temporary author labels, not printed labels.
names='auvw bcts rq'.replace(' ','')
tree=graph(names,[('a','u'),('u','v'),('v','w'),('w','b'),('v','t'),('t','c'),('w','s'),('s','r'),('u','q')]); td=distances(tree)
assert meetings(tree,td,'abc')=={'v'}
assert [td[a][b] for a,b in combinations('abc',2)]==[4,4,4]
tri=graph('abc',[('a','b'),('b','c'),('c','a')]); assert not meetings(tri,distances(tri),'abc')
cycle=graph('abcd',[('a','b'),('b','c'),('c','d'),('d','a')]); assert meetings(cycle,distances(cycle),'abc')=={'b'}
verts=[''.join(s) for s in product('01',repeat=3)]
cube=graph(verts,[(a,b) for a,b in combinations(verts,2) if sum(x!=y for x,y in zip(a,b))==1]); cd=distances(cube)
assert meetings(cube,cd,['000','110','101'])=={'100'}
assert meetings(cube,cd,['000','001','111'])=={'001'}   # GGT67-S-v2: the right map's homes
ct=0
for homes in combinations(verts,3):
    majority=''.join(str(int(sum(h[k]=='1' for h in homes)>=2)) for k in range(3))
    assert meetings(cube,cd,homes)=={majority}; ct+=1
assert all(cd[a][m]+cd[m][b]==cd[a][b]==2 for a,b in combinations(['000','110','101'],2) for m in ['100'])
assert [cd[a][b] for a,b in combinations(['000','001','111'],2)]==[1,3,2] and cd['001']['111']==2
# October 23, 2026 (GGT67-FAC-v2): the launch, the K-1 key and the two extra maps.
small=[(x,y) for x in range(3) for y in range(2)]
sg=graph(small,[(a,b) for a,b in combinations(small,2) if sum(abs(x-y) for x,y in zip(a,b))==1]); sd=distances(sg)
assert {m for m in sg if sd[(0,0)][m]+sd[m][(2,1)]==sd[(0,0)][(2,1)]}==set(small)
two={m for m in g if d[(0,0)][m]+d[m][(4,1)]==d[(0,0)][(4,1)]}
assert two=={(x,y) for x in range(5) for y in range(2)} and len(two)==10
k23=graph('abcxy',[(h,c) for h in 'abc' for c in 'xy']); assert meetings(k23,distances(k23),'abc')=={'x','y'}
ring=graph(range(6),[(i,(i+1)%6) for i in range(6)]); assert meetings(ring,distances(ring),[0,2,4])==set()
print(json.dumps({'status':'PASS','grid_distinct_triples':triples,'cube_distinct_triples':ct,
 'P1':[[1,1],[4,3]],'P3':['central junction below C',None,'B'],'P4':['100','001'],
 'scope':'Finite checks certify the printed boards; coordinate and tripod proofs establish the general claims.'},indent=2))
