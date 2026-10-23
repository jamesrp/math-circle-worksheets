"""Independently verify the positive-rectangle identities and printed instances."""
from fractions import Fraction as Q
import json

def reshape(a,b):
    m=(a+b)/2
    return a*b/m,m

pairs=[(a,24//a) for a in range(1,25) if 24%a==0 and a<=24//a]
assert pairs==[(1,24),(2,12),(3,8),(4,6)]
assert [m*m-a*b for a,b,m in [(2,6,4),(2,4,3)]]==[4,1]
assert reshape(Q(1),Q(3))==(Q(3,2),2)
assert reshape(Q(2),Q(6))==(3,4)
assert reshape(Q(3),Q(6))==(4,Q(9,2))
assert reshape(Q(2),Q(10))==(Q(10,3),6)

cards={'A':(Q(24,7),Q(7,2)), 'B':(Q(2),Q(6)),
       'C':(Q(336,97),Q(97,28)), 'D':(Q(3),Q(4))}
for c in cards.values():assert c[0]*c[1]==12
for old,new in zip('BDA','DAC'):assert reshape(*cards[old])==cards[new]
assert [b-a for a,b in [cards[x] for x in 'BDAC']]==[4,1,Q(1,14),Q(1,2716)]
gaps=[b-a for a,b in [cards[x] for x in 'BDAC']]
assert all(new<old/2 for old,new in zip(gaps,gaps[1:]))   # guide: each range less than half the one before
assert Q('3.46')**2==Q('11.9716')<12<Q('12.0409')==Q('3.47')**2
assert Q('3.465')-Q('3.455')==Q('0.01')
assert Q('3.455')**2 < 12 < Q('3.465')**2

tested=0
for denom in [1,2,3,5,7]:
    for i in range(1,36):
        for j in range(i,36):
            a,b=Q(i,denom),Q(j,denom)
            h,m=reshape(a,b)
            assert h*m==a*b
            assert a<=h<=m<=b
            assert h*h<=a*b<=m*m
            assert m*m-a*b==((b-a)/2)**2
            assert m-h==(b-a)**2/(2*(a+b))
            if a<b:assert 0<m-h<(b-a)/2
            else:assert h==m==a==b
            tested+=1

# Digital dissection fit: every rectangle piece lies within the target square,
# interiors do not overlap, and the missing corner is exactly the stated square.
for a,b in [(Q(2),Q(6)),(Q(2),Q(4)),(Q(5,2),Q(9,2))]:
    m=(a+b)/2;d=(b-a)/2
    bottom=m*a;top=a*d;hole=d*d
    assert bottom+top==a*b
    assert bottom+top+hole==m*m
    assert a+d==m and m+d==b

# October 23 revision.
# Problem 1's new question: a square with the area of 24 tiles has a side between 4 and 5.
assert 4*4 < 24 < 5*5
# Problem 2's third case: 5 by 1 into the 3 by 3 square (side = average 3), uncovered area 9 - 5 = 4,
# a 2 by 2 square = (5 - 1)/2. "Half the long side minus 1", which fits A and B, gives 3/2 here.
from itertools import product
def cells(x,y,w,h):return {(i,j) for i in range(x,x+w) for j in range(y,y+h)}
def one_cut_fits(W,H,S):
    """Hole sides of every no-cut or one-straight-grid-cut placement of W x H in S x S leaving one square hole."""
    cuts=[[(W,H)]]+[[(c,H),(W-c,H)] for c in range(1,W)]+[[(W,c),(W,H-c)] for c in range(1,H)]
    sides=[]
    for pieces in cuts:
        opts=[[cells(x,y,pw,ph) for pw,ph in {(w,h),(h,w)} for x in range(S-pw+1) for y in range(S-ph+1)] for w,h in pieces]
        for choice in product(*opts):
            used=set()
            if any(used & c or used.update(c) for c in choice):continue
            hole=cells(0,0,S,S)-used
            xs={i for i,j in hole};ys={j for i,j in hole};k=len(xs)
            if hole and len(ys)==k and len(hole)==k*k and max(xs)-min(xs)==k-1 and max(ys)-min(ys)==k-1:
                sides.append((len(pieces),k))
    return sides
p2={}
for name,(W,H,S) in {'A':(6,2,4),'B':(4,2,3),'C':(5,1,3)}.items():
    assert Q(W+H,2)==S and S*S-W*H==((W-H)//2)**2
    sides=one_cut_fits(W,H,S)
    assert sides and {k for n,k in sides}=={(W-H)//2} and all(n==2 for n,k in sides)
    p2[name]={'hole_side':(W-H)//2,'one_cut_placements':len(sides)}
assert Q(5,2)-1!=2 and Q(6,2)-1==2 and Q(4,2)-1==1
# The guide's dissection of C: 3 by 1 along the bottom, the 2 by 1 piece upright in a corner.
C_pieces=[cells(0,0,3,1),cells(0,1,1,2)]
assert not (C_pieces[0] & C_pieces[1]) and cells(0,0,3,3)-C_pieces[0]-C_pieces[1]==cells(1,1,2,2)
# Guide K-1 route with 12 tiles: three rectangles, 3 by 4 closest; a square of area 12 has side between 3 and 4.
assert [(a,12//a) for a in range(1,13) if 12%a==0 and a<=12//a]==[(1,12),(2,6),(3,4)]
assert 3*3 < 12 < 4*4
# Guide overview in the gap g = b - a: g_new = (b-a)^2/(2(a+b)) < g/2, so widths < g/2^n after n moves.
for a,b in [(Q(2),Q(6)),(Q(1),Q(3)),(Q(4),Q(9))]:
    g=b-a;lo,hi=a,b
    for n in range(1,6):
        lo,hi=reshape(lo,hi)
        assert 0<hi-lo<g/2**n
print(json.dumps({'status':'pass','positive_rational_pairs':tested,
                  'factor_pairs_24':pairs,'problem_2_cases':p2,'card_order':'B,D,A,C',
                  'card_gaps':['4','1','1/14','1/2716'],
                  'decimal_bracket':['3.46','3.47'],
                  'limits':'General proof is supplied separately. Digitally valid cut coordinates do not establish physical rehearsal.'},indent=2))
