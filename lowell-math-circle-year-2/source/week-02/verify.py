#!/usr/bin/env python3
"""Exhaustive checks independent of worksheet diagrams; no third-party packages."""
from collections import defaultdict
from itertools import product

def outcomes(n,edges):
    out=defaultdict(list)
    for choices in product((0,1),repeat=len(edges)):
        lamps=[0]*n
        for used,(a,b) in zip(choices,edges):
            if used: lamps[a]^=1; lamps[b]^=1
        out[tuple(lamps)].append(choices)
    return out
for n in (4,5,6,7):
    edges=[(i,(i+1)%n) for i in range(n)]
    out=outcomes(n,edges)
    assert len(out)==2**(n-1)
    assert all(sum(t)%2==0 for t in out)
    assert all(len(v)==2 and all(a+b==1 for a,b in zip(*v)) for v in out.values())
    assert max(min(map(sum,v)) for v in out.values())==n//2
    print(f'C{n}: {len(out)} even states, 2 complementary solutions each, worst minimum {n//2}')
out5=outcomes(5,[(i,(i+1)%5) for i in range(5)])
assert out5[(1,0,1,0,0)]==[(0,0,1,1,1),(1,1,0,0,0)]
assert min(map(sum,out5[(1,1,1,1,0)]))==2
extra=outcomes(5,[(0,1),(1,2),(2,0),(3,4)])
assert (1,0,0,1,0) not in extra
assert min(map(sum,extra[(1,0,1,1,1)]))==2
# Independently verify every tree on a small fixed topology and all even targets.
tree=[(0,1),(1,2),(1,3),(3,4),(3,5)]
tout=outcomes(6,tree)
assert len(tout)==32 and all(len(v)==1 for v in tout.values())
for t,sols in tout.items():
 for j,(a,b) in enumerate(tree):
  seen={a}; todo=[a]
  while todo:
   v=todo.pop()
   for i,(x,y) in enumerate(tree):
    if i==j: continue
    nxt=y if x==v else x if y==v else None
    if nxt is not None and nxt not in seen: seen.add(nxt);todo.append(nxt)
  assert sols[0][j]==sum(t[v] for v in seen)%2
print('Disconnected obstruction and all 32 tree cut-parity solutions verified.')
