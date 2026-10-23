#!/usr/bin/env python3
"""Exact rational sample checks, with the universal proof recorded separately.

Finite samples are regression tests, not an all-pairs certificate.
For the global upper bound, subtract the image square from 4 times the
source square: 4(u*u+v*v)-(u*u/4+4*v*v)=15*u*u/4 >= 0.
Named opposite boundaries force the matching lower bound. For midpoint
probes, adding both squared unit-disk inequalities yields
(a-1)**2+(b-1)**2 <= 0, hence a=b=1.
"""
from fractions import Fraction as F
from itertools import combinations

corners=[(0,0),(4,0),(4,1),(0,1)]
images=[(0,0),(2,0),(2,2),(0,2)]

def d2(p,q): return (p[0]-q[0])**2+(p[1]-q[1])**2
placements=0
for i in range(1,20):
    for j in range(1,20):
        o=(F(i,10),F(j,10))
        old=corners+[(2,F(1,2))]; new=images+[o]
        ratios2=[F(d2(new[a],new[b]))/d2(old[a],old[b])
                 for a,b in combinations(range(5),2)]
        assert max(ratios2)==4
        probe2=max(4*d2(o,(1,0)),4*d2(o,(1,2)))
        assert probe2>=4
        assert (probe2==4)==(o==(1,1))
        placements+=1
for u in range(-40,41):
    for v in range(-10,11):
        source2=u*u+v*v
        image2=F(u*u,4)+4*v*v
        assert 4*source2-image2==F(15*u*u,4)>=0
for w,h,k in [(2,2,2),(6,2,2),(2,3,3),(6,1,F(3,2)),(4,F(3,2),F(3,2)),(3,F(3,2),F(3,2))]:
    assert max(F(w)/4,F(h))==k
print(f'PASS: {placements} exact sampled five-pin placements score 2; all sampled off-center fans fail a midpoint test.')
print('PASS: exact squared-distance identity and all printed target constants checked.')
print('Universal proof: nonnegative squared-distance difference, tangent midpoint disks, and opposite named boundary separations; see source README.')
