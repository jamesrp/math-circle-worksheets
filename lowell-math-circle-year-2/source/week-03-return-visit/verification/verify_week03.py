"""Independent checks of Week 3 represented examples (standard library)."""
from collections import deque
from itertools import permutations
from pathlib import Path
import json

def inversions(p):
    return sum(a>b for i,a in enumerate(p) for b in p[i+1:])
def neighbors(p):
    for i in range(len(p)-1):
        q=list(p);q[i],q[i+1]=q[i+1],q[i];yield tuple(q)
def distances(home,moves):
    q=deque([home]);d={home:0}
    while q:
        p=q.popleft()
        for nxt in moves(p):
            if nxt not in d:d[nxt]=d[p]+1;q.append(nxt)
    return d
def square(p):return tuple(p[p[i]-1] for i in range(len(p)))

out={}
for n in [3,4,5,6]:
    home=tuple(range(1,n+1));ps=list(permutations(home))
    ds=distances(home,neighbors)
    assert all(ds[p]==inversions(p) for p in ps)
    rotate=lambda p:(p[-1:]+p[:-1],p[::-1])
    orbit=distances(home,rotate);assert len(orbit)==2*n
    targets={square(p) for p in ps}
    out[str(n)]={'adjacent_orders_checked':len(ps),'rotate_reverse_orders':[list(p) for p in sorted(orbit)],'targets_with_roots':len(targets)}
    if n in [3,4,6]:assert len(targets)=={3:3,4:12,6:270}[n]
assert inversions((3,1,4,2))==3
route=[(3,1,4,2),(1,3,4,2),(1,3,2,4),(1,2,3,4)]
assert all(b in neighbors(a) for a,b in zip(route,route[1:]))
assert (2,1,3) not in {square(p) for p in permutations((1,2,3))}
assert square((3,1,2))==(2,3,1)
assert square((3,4,2,1))==(2,1,4,3)

# Actual printed output rows: arrows map input positions to destination slots.
def run(row,p):
    out=[None]*len(p)
    for i,destination in enumerate(p):out[destination-1]=row[i]
    return tuple(out)
for target,p,mid in [((2,3,1),(2,3,1),(3,1,2)),((2,1,4,3),(3,4,2,1),(4,3,1,2)),((2,3,1,5,6,4),(2,3,1,5,6,4),(3,1,2,6,4,5))]:
    home=tuple(range(1,len(p)+1));assert run(home,p)==mid and run(mid,p)==target
    count=sum(run(run(home,q),q)==target for q in permutations(home));assert count=={3:1,4:2,6:4}[len(p)]
assert [inversions(p) for p in [(2,1,3,5,4),(3,1,4,2,5),(5,3,4,2,1),(5,4,3,2,1)]]==[2,3,9,10]
assert run((7,8),(2,1))==(8,7) and run((8,7),(2,1))==(7,8)
rot=lambda p:p[-1:]+p[:-1]
assert rot(rot((1,2,3,4)))==(3,4,1,2)
assert rot(rot((1,2,3,4)))[::-1]==(2,1,4,3)
assert (1,3,2,4) not in distances((1,2,3,4),lambda p:(rot(p),p[::-1]))
assert (2,4,1,3) not in distances((1,2,3,4),lambda p:(rot(p),p[::-1]))

Path(__file__).with_name('week03-represented-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Week 3 sorting, restricted orders, and represented roots independently verified')
