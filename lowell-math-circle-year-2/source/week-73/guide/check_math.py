#!/usr/bin/env python3
"""Independent exact regression checks. Universal arguments are in facilitator.tex."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt

def sqdist(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))

corners=[(F(0),F(0)),(F(4),F(0)),(F(4),F(1)),(F(0),F(1))]
newcorners=[(F(0),F(0)),(F(2),F(0)),(F(2),F(2)),(F(0),F(2))]
old=corners+[(F(2),F(1,2))]
placements=offcenter=0
for i in range(1,32):
    for j in range(1,32):
        q=(F(i,16),F(j,16)); new=newcorners+[q]
        ratios=[sqdist(new[a],new[b])/sqdist(old[a],old[b]) for a,b in combinations(range(5),2)]
        assert len(ratios)==10 and max(ratios)==4
        mtests=[sqdist(q,(F(1),F(k)))/F(1,4) for k in [0,2]]
        assert (max(mtests)<=4)==(q==(1,1))
        placements+=1; offcenter+=q!=(1,1)
# Independent algebra check via the nonnegative difference identity.
for p in range(-11,12):
    for q in range(-9,10):
        assert 4*(p*p+q*q)-(F(p,2)**2+(2*q)**2)==F(15,4)*p*p
for w,h,answer in [(6,2,2),(2,3,3),(6,1,F(3,2)),(3,F(3,2),F(3,2))]:
    assert max(F(w,4),h)==answer
    for p in range(-4,5):
        for q in range(-4,5):
            assert (F(w,4)*p)**2+(h*q)**2<=answer**2*(p*p+q*q)
assert F(3,2)==F(3)/2
excess_mm=(sqrt(1+0.25**2)-1)*0.94*25.4
assert round(excess_mm,3)==0.735
assert F(94,100)/4==F(47,200)
print(f'PASS Week 73: {placements} rational placements; {offcenter} off-center midpoint failures; all stated target factors and 0.735 mm example. Finite checks are not universal proofs.')
