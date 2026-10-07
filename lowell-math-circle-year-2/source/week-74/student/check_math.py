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
expected={3:(3,3),7:(6,6),9:(7,7),15:(9,9),16:(8,8),17:(9,9),23:(10,11)}
for n,(left_cost,no_left_cost) in expected.items():
    a,b=solve(n),solve(n,False)
    assert end(a)==end(b)==(n,0)
    assert (len(a),len(b))==(left_cost,no_left_cost)
    print(n, a,len(a),'without left:',b,len(b))
assert len(solve(23))<len(solve(23,False))
expected_maxima={4:4,5:6,6:8,7:12,8:16}
for budget in range(4,9):
    bound=max((budget-2*h)*2**h for h in range(budget//2+1))
    # Universal upper bound: at least 2*h vertical moves, at most
    # budget-2*h horizontal moves, each of absolute size at most 2**h.
    # This includes left moves and repeated vertical excursions.
    assert bound==expected_maxima[budget]
    height=max(range(budget//2+1),key=lambda h:(budget-2*h)*2**h)
    witness='U'*height+'R'*(budget-2*height)+'D'*height
    assert len(witness)==budget and end(witness)==(bound,0)
    print('Budget',budget,'greatest possible ground displacement',bound)
print('PASS: moves preserve coordinates vertically; both optimal routes verified.')

# Exact no-left coin counts at each possible useful maximum level.
no_left_23=[2*h+23//(2**h)+bin(23%(2**h)).count('1') for h in range(5)]
assert no_left_23==[23,14,11,11,12]
assert min(no_left_23)==11
print('PASS: all printed target distances, budget maxima with witness routes, and no-left 23 counts checked.')
