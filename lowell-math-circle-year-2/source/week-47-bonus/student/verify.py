#!/usr/bin/env python3
from itertools import product
from collections import Counter,deque

def legal(v,edges):return all(abs(v[a]-v[b])<=1 for a,b in edges)
def enum(n,edges,clues,maxh):
    free=[i for i in range(n) if i not in clues];ans=[]
    for hs in product(range(maxh+1),repeat=len(free)):
        v=[clues.get(i,0) for i in range(n)]
        for i,h in zip(free,hs):v[i]=h
        if legal(v,edges):ans.append(tuple(v))
    return ans

if __name__=='__main__':
    row=[(i,i+1) for i in range(4)];ring=row+[(4,0)]
    r=enum(5,row,{0:0,3:3},4);bad=enum(5,ring,{0:0,3:3},4);good=enum(5,ring,{0:0,3:2},4)
    assert len(r)==3 and not bad and len(good)==3
    assert tuple(max(v[i] for v in good) for i in range(5))==(0,1,2,2,1)
    print('P1: row 3 completions, first ring none, second ring',good)
    start=(1,2,3,2,1,0,1);target=(1,0,1,2,3,2,1);edges=[(i,i+1) for i in range(6)]
    space=set(enum(7,edges,{0:1,6:1},4));q=deque([(start,0)]);seen={start};distance=None
    while q:
        s,d=q.popleft()
        if s==target:distance=d;break
        for i in range(1,6):
            for delta in (-1,1):
                v=list(s);v[i]+=delta;v=tuple(v)
                if v in space and v not in seen:seen.add(v);q.append((v,d+1))
    assert distance==sum(abs(a-b) for a,b in zip(start,target))==8
    route=[start,(1,2,2,2,1,0,1),(1,1,2,2,1,0,1),(1,1,1,2,1,0,1),(1,0,1,2,1,0,1),(1,0,1,2,1,1,1),(1,0,1,2,2,1,1),(1,0,1,2,2,2,1),target]
    assert all(v in space for v in route)
    assert all(sum(abs(x-y) for x,y in zip(a,b))==1 for a,b in zip(route,route[1:]))
    print('P2 shortest route:',distance,'moves; feasible rows:',len(space))
    edges=[(i,(i+1)%6) for i in range(6)];states=enum(6,edges,{0:1,3:1},2)
    counts=Counter(map(sum,states));assert set(counts)==set(range(2,11))
    assert len(states)==49
    print('P3 budget counts:',dict(sorted(counts.items())))
    for budget in (2,5,8,10):print('Witness',budget,next(v for v in states if sum(v)==budget))
