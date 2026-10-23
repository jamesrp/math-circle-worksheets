"""Finite checks of the examples; the last lines record the infinite arguments."""
from collections import deque
from itertools import combinations

def comps(vs,edges,blocked):
    vs=set(vs)-set(blocked);adj={v:set() for v in vs}
    for a,b in edges:
        if a in vs and b in vs:adj[a].add(b);adj[b].add(a)
    parts=[]
    while vs:
        todo=[vs.pop()];part=set(todo)
        while todo:
            for w in adj[todo.pop()]&vs:vs.remove(w);part.add(w);todo.append(w)
        parts.append(part)
    return parts
# Long finite windows: count pieces touching ends, not all components.
vs=list(range(-8,9));edges=list(zip(vs,vs[1:]))
for blocked in [(-1,),(-2,2),(-3,-2,0,3)]:
    cs=comps(vs,edges,blocked);assert sum(bool(c&{-8,8}) for c in cs)==2
assert len([c for c in comps(vs,edges,(-3,-2,0,3)) if not c&{-8,8}])==2
vs=[(x,y) for x in range(-8,9) for y in (0,1)]
edges=[(v,w) for v,w in combinations(vs,2) if abs(v[0]-w[0])+abs(v[1]-w[1])==1]
interior=[(x,y) for x in range(-2,3) for y in (0,1)]
for n in range(5):
    for blocked in combinations(interior,n):
        cs=comps(vs,edges,blocked)
        outer=[c for c in cs if any(abs(x)==8 for x,y in c)]
        assert len(outer)<=2
assert len(comps(vs,edges,[(0,0)]))==1
assert len(comps(vs,edges,[(0,0),(0,1)]))==2
vs=[(x,y) for x in range(-5,6) for y in range(-5,6)];edges=[(v,w) for v,w in combinations(vs,2) if abs(v[0]-w[0])+abs(v[1]-w[1])==1]
cs=comps(vs,edges,[(-1,0),(1,0),(0,-1),(0,1)]);assert {frozenset(c) for c in cs}=={frozenset({(0,0)}),frozenset(set(vs)-{(-1,0),(1,0),(0,-1),(0,1),(0,0)})}
assert len(comps(vs,edges,[(0,y) for y in range(-2,3)]))==1
tree_vs=[''];tree_edges=[];layer=['']
for depth in range(5):
    next_layer=[]
    for v in layer:
        for i in range(3 if depth==0 else 2):
            w=v+str(i);tree_vs.append(w);tree_edges.append((v,w));next_layer.append(w)
    layer=next_layer
for radius,expected in enumerate([3,6,12,24]):
    cs=comps(tree_vs,tree_edges,[v for v in tree_vs if len(v)<=radius])
    assert len(cs)==expected and all(any(len(v)==5 for v in c) for c in cs)
print('PASS: line examples, all up-to-four-blocker placements in a ladder core, grid pocket/wall, tree counts 3,6,12,24.')
print('Infinite arguments: outside any finite ladder blockage lie at most two connected tails. Any finite grid blockage fits in a square; the outside of a larger square is connected. Tree components do not rejoin by definition. These arguments, not finite experiments alone, justify the ends claims.')
