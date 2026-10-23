#!/usr/bin/env python3
"""Independent exact checks for the guide's instances, without external packages."""
from fractions import Fraction as F
from itertools import product
from math import comb

def intersection_heights(a,b):
    d=abs(a-b)
    return [F(k,d) for k in range(1,d)] if d else []

def minimum(a,b): return max(abs(a-b)-1,0)

def twist(p,k):
    x,t=p
    return ((x+k*t)%1,t)

# Detect equality modulo a circumference for every candidate crossing height.
for a in range(-8,9):
    for b in range(-8,9):
        heights=intersection_heights(a,b)
        assert len(heights)==minimum(a,b)
        assert len(set(heights))==len(heights)
        for t in heights:
            assert 0<t<1 and ((F(1,2)+a*t)-(F(1,2)+b*t)).denominator==1
        for k in range(-4,5): assert minimum(a+k,b+k)==minimum(a,b)
# Equal-winding representatives separated by epsilon*t*(1-t) are disjoint inside.
for n in range(-8,9):
    for j in range(1,32):
        t=F(j,32); gap=F(1,4)*t*(1-t)
        assert 0<gap<1
        assert (F(1,2)+n*t+gap)%1!=(F(1,2)+n*t)%1
for theta in [F(i,8) for i in range(8)]:
    for t in [F(i,8) for i in range(9)]:
        for j,k in product(range(-4,5),repeat=2):
            assert twist(twist((theta,t),j),k)==twist((theta,t),j+k)
            assert twist(twist((theta,t),j),-j)==(theta,t)
    for t in [F(0),F(1)]:
        for k in range(-8,9): assert twist((theta,t),k)==(theta,t)
assert F(1,2)+2==F(5,2) and F(1,2)-1==-F(1,2)
assert [minimum(a,b) for a,b in [(0,1),(0,2),(0,3),(-1,1),(-1,2),(2,4)]]==[0,1,2,1,2,1]
assert minimum(2,7)==4 and minimum(5,5)==0
assert (minimum(0,2),minimum(0,3))==(1,2)
assert (minimum(0,2),minimum(1,2))==(1,0)
assert (minimum(5,5),minimum(6,5))==(0,0)
for length in range(7):
    for word in product([-1,1],repeat=length):
        n=sum(word)
        assert abs(n)<=length
        assert sum([1 if n>0 else -1]*abs(n))==n
        if length==6 and n==0: assert word.count(1)==3
assert sum(sum(word)==0 for word in product([-1,1],repeat=6))==comb(6,3)==20
for word,expected in [('++-',1),('+--',-1),('+--+',0),('+++---',0)]:
    assert sum(1 if sign=='+' else -1 for sign in word)==expected
assert [F(i,4) for i in range(5)]==[0,F(1,4),F(1,2),F(3,4),1]
print('PASS Week 75: 289 winding pairs, all eight printed minima, one-route increase/decrease/tie examples, 20 balanced words, exact rational twist composition and fixed rims. Universal topological claims use the guide proofs.')
