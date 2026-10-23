#!/usr/bin/env python3
"""Independent BFS on the unbounded state graph; no writer-code imports."""
from collections import deque

def search(depth,left=True):
    d={(0,0):0}; todo=deque([(0,0)])
    while todo:
        x,h=todo.popleft(); n=d[(x,h)]
        if n==depth: continue
        candidates=[(x,h+1),(x+(1<<h),h)]
        if h: candidates.append((x,h-1))
        if left: candidates.append((x-(1<<h),h))
        for p in candidates:
            if p not in d:
                d[p]=n+1;todo.append(p)
    return d

def run(word):
    x=h=0
    for ch in word:
        if ch=='U': h+=1
        elif ch=='D':
            h-=1
            assert h>=0
        elif ch=='R': x+=1<<h
        elif ch=='L': x-=1<<h
        else: raise AssertionError(ch)
    return x,h

d=search(12); nr=search(12,False)
targets={3:3,7:6,9:7,15:9,16:8,17:9,23:10}
for x,c in targets.items(): assert d[x,0]==c
for x,c in {9:7,15:9,17:9,23:11}.items(): assert nr[x,0]==c
witnesses={3:'RRR',7:'URRRDR',9:'UURRDDR',15:'UUURRDDDL',16:'UURRRRDD',17:'UUURRDDDR',23:'UUURRRDDDL'}
for x,w in witnesses.items(): assert run(w)==(x,0) and len(w)==targets[x]
assert run('UUURRDDD')==(16,0) and len('UUURRDDD')==8
for x,w in {9:'UURRDDR',15:'UURRRDRDR',17:'UUURRDDDR',23:'UUURRDRDRDR'}.items():
    assert 'L' not in w and run(w)==(x,0) and len(w)==nr[x,0]
for n,x,w in [(4,4,'RRRR'),(5,6,'URRRD'),(6,8,'UURRDD'),(7,12,'UURRRDD'),(8,16,'UUURRDDD')]:
    assert max(a for (a,h),cost in d.items() if h==0 and cost<=n)==x
    assert max((n-2*h)*(1<<h) for h in range(n//2+1))==x
    assert run(w)==(x,0) and len(w)==n
assert [(7-2*h)*(1<<h) for h in range(4)]==[7,10,12,8]
assert [(9-2*h)*(1<<h) for h in range(5)]==[9,14,20,24,16]
assert [2*h+23//(1<<h)+bin(23%(1<<h)).count('1') for h in range(5)]==[23,14,11,11,12]
assert round(.23*25.4,2)==5.84
assert 1+4+4+4==13 and 1+8==9 and 1+8+8==17
# October 23, 2026 review-card additions.
from itertools import product
def words(n):
    for k in range(n+1):
        for w in product('UDRL',repeat=k):
            try:
                if run(w)[1]==0: yield ''.join(w)
            except AssertionError: pass  # a D below level 0
short=list(words(8))
assert sorted(w for w in short if run(w)==(16,0))==['UURRRRDD','UUURRDDD']
assert sorted(w for w in short if run(w)==(8,0) and len(w)<=6)==['URRRRD','UURRDD']
assert d[8,0]==6 and d[4,0]==4 and d[6,0]==5
assert run('RRRR')==run('URRD')==(4,0) and run('URRRD')==(6,0) and run('RRRRRR')==(6,0)
reach=lambda n:max((n-2*h)*(1<<h) for h in range(n//2+1))
assert [reach(n) for n in (4,6,8,10)]==[4,8,16,32]
assert [max(a for (a,h),cost in d.items() if h==0 and cost<=n) for n in (4,6,8,10)]==[4,8,16,32]
assert all(reach(n+2)==2*reach(n) for n in range(2,40)) and reach(3)==3!=2*reach(1)
assert all(reach(2*k)==1<<k and reach(2*k-1)<1<<k for k in range(1,20))
assert all(d[1<<k,0]==2*k for k in range(1,6))
assert (1+(1<<2),2)==(5,2)
assert [round(.23*s,2) for s in (1,2,4,8,16)]==[.23,.46,.92,1.84,3.68]
print(f'PASS Week 74: {len(d)} unbounded-coordinate states through depth 12, all targets/budgets/route words/no-left costs, the doubling reach, the two six-move trips to 8, the strip ticks and 5.84 mm spacing.')
