#!/usr/bin/env python3
"""Independent exact checks of Week 70 guide answers; standard library only.
Finite evidence supplements, and does not replace, the guide's proofs.
"""
from fractions import Fraction as F
from math import gcd
from itertools import product, combinations
SHIELDS = {(1,1),(1,3),(3,1),(3,3)}
def first_target(x,y):
    # Target coordinates are 2 modulo 4. Find times by x; test y independently.
    possible = []
    for tx in range(min(0,x), max(0,x)+1):
        if tx % 4 == 2:
            t = F(tx,x)
            ty = t*y
            if 0 < t <= 1 and ty.denominator == 1 and ty % 4 == 2:
                possible.append((t,(F(tx),ty)))
    return min(possible)
def check():
    expect = {(2,6):((2,6),(1,3)), (6,2):((6,2),(3,1)),
              (6,6):((2,2),(1,1)), (10,6):((10,6),(1,3))}
    for end,(hit,shield) in expect.items():
        t,p = first_target(*end)
        assert p == hit
        assert tuple((v/2)%4 for v in p) == shield
    finite = list(product((-2,2,6,10), repeat=2))
    broad = [(2+4*m,2+4*n) for m,n in product(range(-25,26),repeat=2)]
    for end in finite + broad:
        t,p = first_target(*end)
        assert tuple((v/2)%4 for v in p) in SHIELDS
        d = gcd(abs(end[0]//2), abs(end[1]//2))
        assert p == (F(end[0],d), F(end[1],d))
        assert 0 < t/2 < t
    # Distinct open coordinate quadrants contain the four necessary paths.
    quadrants = set()
    for sx,sy in product((-1,1),repeat=2):
        for t in (F(k,20) for k in range(1,20)):
            x,y = (2*sx*t)%4, (2*sy*t)%4
            assert 0<x<4 and x!=2 and 0<y<4 and y!=2
            assert (x<2,y<2) == (sx>0,sy>0)
        quadrants.add((sx>0,sy>0))
    assert len(quadrants)==4
    # Non-task shared convention picture and simplest folded Problem 2 path.
    assert F(1)+F(1,2)*(4-3) == F(3,2)
    assert (5%4,2%4)==(1,2)
    assert F(2,6)*4 == F(4,3)
    assert (F(4,3),4%4)==(F(4,3),0)
    print('PASS: four task rays; all 16 map targets; 2,601 wider lift cases; shield-copy and folded-path coordinates.')
if __name__ == '__main__': check()
