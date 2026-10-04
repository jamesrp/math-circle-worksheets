#!/usr/bin/env python3
"""Unit-step reflection independently checks unfolded formulas."""
from math import gcd,lcm
from fractions import Fraction

def trace(w,h):
 x=y=0; dx=dy=1; bounces=0; points=[(x,y)]
 for step in range(1,2*w*h+2):
  x+=dx;y+=dy
  if x in (0,w) and y in (0,h):
   points.append((x,y));return (x,y),bounces,step,points
  if x in (0,w):dx=-dx;bounces+=1;points.append((x,y))
  if y in (0,h):dy=-dy;bounces+=1;points.append((x,y))
 raise AssertionError((w,h))
for w in range(1,31):
 for h in range(1,31):
  end,bounces,distance,_=trace(w,h);g=gcd(w,h);a,b=w//g,h//g
  assert end==((b%2)*w,(a%2)*h)
  assert bounces==a+b-2
  assert distance==lcm(w,h)
assert [(w,h) for w in range(1,7) for h in range(1,7) if gcd(w,h)==1 and w%2==h%2==1 and w+h-2==4]==[(1,5),(5,1)]
for w,h in [(2,2),(2,4),(4,2),(2,3),(4,6),(6,9),(6,10),(8,14)]:
 print((w,h),trace(w,h))
for p,q in [(2,3),(3,2),(4,3),(5,7)]:
 events=sorted({Fraction(i*q,p) for i in range(1,p)} | {Fraction(i) for i in range(1,q)})
 assert len(events)==p+q-2
print('PASS: all 900 integer rectangles through 30x30, inverse designs and rational-slope event counts.')

# Additional v3 printed traces and reduced-slope comparisons.
for w,h,endpoint,bounces in [(2,6,(2,6),2),(3,2,(0,2),3),(3,3,(3,3),0),(3,6,(0,6),1),(3,9,(3,9),2),(1,5,(1,5),4),(5,1,(5,1),4),(2,10,(2,10),4)]:
 assert trace(w,h)[:2]==(endpoint,bounces)
for p,q,first in [(1,2,(2,1)),(2,4,(2,1)),(2,3,(3,2)),(3,2,(2,3)),(3,4,(4,3))]:
 hits=[(u,Fraction(p*u,q)) for u in range(1,q+1) if Fraction(p*u,q).denominator==1]
 assert hits[0]==first
print('PASS: v3 added rectangle, first-corner, scaling and rational-slope examples.')
