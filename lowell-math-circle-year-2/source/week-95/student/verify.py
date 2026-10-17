#!/usr/bin/env python3
"""Exact arithmetic checks for authored examples (no external packages)."""
from math import comb
from fractions import Fraction

def ways(N,M,n,r):
    return comb(M,r)*comb(N-M,n-r) if 0<=r<=M and 0<=n-r<=N-M else 0

def support(N,M,n):
    return [r for r in range(min(M,n)+1) if ways(N,M,n,r)]

# Non-task fraction bridge: exactly the same A,B,C sample appears in the model.
example_sample=set('ABC')
example_model=set('ABCDEF')
example_marks=set('AD')
assert example_sample <= example_model
assert len(example_sample & example_marks)==1
assert Fraction(len(example_marks),len(example_model))==Fraction(1,3)
assert Fraction(2*3,1)==6
assert set('ABCDE') | set('BDEFG') == set('ABCDEFG')
assert len(set('ABCDE') | set('FGHIJ')) == 10
assert [N for N in [6,7,8,12,20] if 3 in support(N,5,5)] == [7,8,12,20]
assert {N:support(N,5,4) for N in (6,8,12)} == {6:[3,4],8:[1,2,3,4],12:[0,1,2,3,4]}
for N in [8,16]:
    assert all(r in support(N,4,4) for r in [2,1,3,1,2,0])
assert all(r in support(18,6,6) for r in [1,2,3,2,0])
assert [Fraction(36,r) for r in [1,2,3,2]] == [36,18,12,18]
for N in range(2,25):
    for M in range(1,N+1):
        for n in range(1,N+1):
            counts=[ways(N,M,n,r) for r in range(min(M,n)+1)]
            assert sum(counts)==comb(N,n)
            assert Fraction(sum(r*w for r,w in enumerate(counts)),sum(counts))==Fraction(M*n,N)
            assert support(N,M,n)==list(range(max(0,M+n-N),min(M,n)+1))
for budget in range(2,25):
    best=max(m*(budget-m) for m in range(1,budget))
    winners=[m for m in range(1,budget) if m*(budget-m)==best]
    assert winners==sorted(set([budget//2,(budget+1)//2]))
print('PASS: fraction-matching visual, identities, sharp feasible-overlap ranges, both printed repeat series, estimates, exact expectations through N=24, and all budget optima 2..24.')
