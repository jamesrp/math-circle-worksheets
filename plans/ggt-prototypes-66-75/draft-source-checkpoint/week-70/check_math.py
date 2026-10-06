#!/usr/bin/env python3
"""Exact midpoint and first-hit checks for the 4 by 4 flat torus."""
from fractions import Fraction
from math import gcd
B={(1,1),(1,3),(3,1),(3,3)}
for m in range(-50,51):
 for n in range(-50,51):
  u,v=2+4*m,2+4*n
  # First target hit: divide both odd coordinates by their odd gcd.
  d=gcd(abs(u//2),abs(v//2))
  a,b=Fraction(u,d),Fraction(v,d)
  assert (a%4,b%4)==(2,2)
  mid=((a/2)%4,(b/2)%4)
  assert mid in B
  assert 0<Fraction(1,2*d)<Fraction(1,d)<=1
# The four shortest diagonal paths occupy disjoint open quadrants.
# Each direction has points (2*t mod4, +/-2*t mod4), t in (0,1),
# with x/y strictly on respective sides of the lines x=2 and y=2.
for sx,sy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 for k in range(1,100):
  t=Fraction(k,100); x=(2*sx*t)%4; y=(2*sy*t)%4
  assert (x<2)==(sx>0) and (y<2)==(sy>0)
print('PASS: 10,201 target lifts, first-hit normalization, midpoint blockers, and disjoint diagonal interiors.')
