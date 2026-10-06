#!/usr/bin/env python3
"""Finite exact search plus an unbounded displacement bound for the packet."""
from collections import deque

def solve(target, allow_left=True):
    q=deque([(0,0,'')]); seen={(0,0)}
    while q:
        x,h,w=q.popleft()
        if (x,h)==(target,0): return w
        if len(w)>=12: continue
        moves=[(x,h+1,'U'),(x+2**h,h,'R')]
        if h: moves.append((x,h-1,'D'))
        if allow_left: moves.append((x-2**h,h,'L'))
        for xx,hh,c in moves:
            if hh>12-len(w)-1: continue  # cannot return to ground by depth 12
            if (xx,hh) not in seen:
                seen.add((xx,hh)); q.append((xx,hh,w+c))
    raise AssertionError('not reached')

def end(word):
    x=h=0
    for c in word:
        if c=='U': h+=1
        if c=='D': h-=1
        if c=='R': x+=2**h
        if c=='L': x-=2**h
        assert h>=0
    return x,h
assert end('UURRRRDD')==end('UUURRDDD')==(16,0)
assert len(solve(16))==8
assert [(7-2*h)*2**h for h in range(4)]==[7,10,12,8]
for n in (3,7,9,15,16,17,23):
    a,b=solve(n),solve(n,False)
    print(n, a,len(a),'without left:',b,len(b))
assert len(solve(23))<len(solve(23,False))
for budget in range(4,9):
    bound=max((budget-2*h)*2**h for h in range(budget//2+1))
    # Upper bound holds for arbitrary routes, not merely the drawn board.
    print('Budget',budget,'greatest possible ground displacement',bound)
print('PASS: moves preserve coordinates vertically; both optimal routes verified.')
