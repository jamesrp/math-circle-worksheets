#!/usr/bin/env python3
from itertools import product
from fractions import Fraction as F

def intersect(cards):return max(a for a,b in cards),min(b for a,b in cards)
def gaprange(a,b):
    return max(0,a[0]-b[1],b[0]-a[1]),max(abs(a[0]-b[1]),abs(a[1]-b[0]))

if __name__=='__main__':
    pairs=[(a,6-a) for a in range(1,6)];areas=[a*b for a,b in pairs]
    assert areas==[5,8,9,8,5];print('Rectangles:',list(zip(pairs,areas)),'tight area [5,9]')
    sets=[[(2,7),(4,9),(5,6)],[(1,4),(3,8),(5,9)],[(1,4),(6,8),(7,9)]]
    assert intersect(sets[0])==(5,6)
    for cards,expected in [(sets[1],[1,3]),(sets[2],[1])]:
        possible=[]
        for i in range(3):
            lo,hi=intersect(cards[:i]+cards[i+1:])
            # False card must actually fail, not merely be discarded.
            witnesses=[F(k,2) for k in range(0,21) if lo<=F(k,2)<=hi and not cards[i][0]<=F(k,2)<=cards[i][1]]
            if witnesses:possible.append(i+1);print('False candidate',i+1,'witness',witnesses[0])
        assert possible==expected
    for a,b,expect in [((3,7),(5,9),(0,6)),((2,4),(6,8),(2,6)),((3,5),(5,7),(0,4))]:
        assert gaprange(a,b)==expect
        vals=[abs(F(i,2)-F(j,2)) for i in range(2*a[0],2*a[1]+1) for j in range(2*b[0],2*b[1]+1)]
        assert (min(vals),max(vals))==expect;print('End gaps',a,b,expect)
    assert gaprange((4,6),(4,6))==(0,2)
    print('Designed cards [4,6] and [4,6] permit either order and guarantee gap <=2.')
