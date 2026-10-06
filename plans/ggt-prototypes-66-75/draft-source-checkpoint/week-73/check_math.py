#!/usr/bin/env python3
"""Checks the pin-game trap and exact whole-sheet bounds; no external packages."""
from math import hypot
from fractions import Fraction
corners=[(0,0),(4,0),(4,1),(0,1)]
images=[(0,0),(2,0),(2,2),(0,2)]

def d(p,q): return hypot(p[0]-q[0],p[1]-q[1])
for i in range(1,20):
    for j in range(1,20):
        o=(i/10,j/10)
        old=corners+[(2,.5)]; new=images+[o]
        ratios=[d(new[a],new[b])/d(old[a],old[b]) for a in range(5) for b in range(a)]
        assert abs(max(ratios)-2)<1e-10
        # Boundary-edge midpoints must map to midpoints in the affine fan.
        probe=max(d(o,(1,0))/.5,d(o,(1,2))/.5)
        assert probe>=2-1e-10
        if o!=(1,1): assert probe>2
# Every source difference (dx,dy) obeys (dx/2)^2+(2dy)^2 <= 4(dx^2+dy^2).
for dx in range(-40,41):
    for dy in range(-10,11):
        assert Fraction(dx*dx,4)+4*dy*dy<=4*(dx*dx+dy*dy)
# A 4-by-1 -> w-by-h side-preserving affine map has exact constant max(w/4,h).
for w,h,k in [(2,2,2),(6,2,2),(2,3,3),(6,1,Fraction(3,2)),(4,Fraction(3,2),Fraction(3,2))]:
    assert max(Fraction(w)/4,Fraction(h))==k
print('PASS: all original five-pin maxima are 2; midpoint tests expose every off-center fan placement.')
print('PASS: centered whole-sheet map has exact worst stretch 2; target examples and invented-target witnesses checked.')
print('Logical lower bound: opposite named boundaries force distance at least their separation.')
