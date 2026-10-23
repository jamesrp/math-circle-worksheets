#!/usr/bin/env python3
"""Exact checks for finite cases and bounded-error endpoints in the packets."""
from fractions import Fraction as F
from itertools import combinations
lengths = dict(A=2,B=3,C=4,D=6)
placements={k:[(a,a+n) for a in range(2,15-n) if 7 in (a,a+n)] for k,n in lengths.items()}
assert placements == {'A':[(5,7),(7,9)],'B':[(4,7),(7,10)],'C':[(3,7),(7,11)],'D':[(7,13)]}
assert [(a,b,c) for a,b in combinations(lengths,2) for c in lengths if lengths[a]+lengths[b]==lengths[c]]==[('A','C','D')]
k1=[(4-c,6-c) for c in (1,2,3)]
assert k1==[(3,5),(2,4),(1,3)] and all(q-p==2 for p,q in k1)
assert [(4-(o-i),6-(o-i)) for i,o in [(1,2),(2,5),(3,5)]]==[(3,5),(1,3),(2,4)]
pairs=[(7-e,10-e,e) for e in range(1,7)]
assert all(b-a==3 for a,b,e in pairs)
assert [(9-(8-x),12-(8-x)) for x in (4,6,2)] == [(5,8),(7,10),(3,6)]
reports=[[(2,5),(4,7),(6,10)],[(2,8),(4,10),(6,12)],[(2,3),(4,6),(6,7)]]
assert [[y-x for x,y in box] for box in reports]==[[3,3,4],[6,6,6],[1,2,1]]
machines=[(n,e) for n in (1,2,3) for e in range(7)]
assert [(n,e) for n,e in machines if 2*n+e==6]==[(1,4),(2,2),(3,0)]
assert len({3*n+e for n,e in machines if 2*n+e==6})==3
assert [(n,e) for n,e in machines if 6*n+e==24]==[(3,6)]
# Every repair retaining two exact observations has a unique line.
points=[(2,F(7)),(4,F(11)),(6,F(16))]
repairs=[]
for omit in range(3):
 retained=[p for i,p in enumerate(points) if i!=omit]
 (x,y),(u,v)=retained
 stretch=(v-y)/(u-x);shift=y-stretch*x
 assert stretch>0
 repairs.append(stretch*points[omit][0]+shift)
assert repairs == [F(6),F(23,2),F(15)]
# Corners give attainable extrema; every convex combination remains feasible.
for x1,x2,y1,y2,want in [(2,4,8,12,(F(1),F(3))),(2,10,8,24,(F(7,4),F(9,4)))]:
 slopes=[]
 for e1 in (-1,1):
  for e2 in (-1,1):
   b=F(y2+e2-y1-e1,x2-x1);a=F(y1+e1)-b*x1
   assert abs(a+b*x1-y1)<=1 and abs(a+b*x2-y2)<=1
   slopes.append(b)
 assert (min(slopes),max(slopes))==want
 assert max(slopes)-min(slopes)==F(4,x2-x1)
assert min((F(4,j-i),i,j) for i in range(1,11) for j in range(i+1,11))==(F(4,9),1,10)
print('All exact mathematical checks passed.')
