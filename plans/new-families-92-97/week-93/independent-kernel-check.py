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

print(json.dumps({'status':'pass','positive_rational_pairs':tested,
                  'factor_pairs_24':pairs,'card_order':'B,D,A,C',
                  'card_gaps':['4','1','1/14','1/2716'],
                  'decimal_bracket':['3.46','3.47'],
                  'limits':'General proof is supplied separately. Digitally valid cut coordinates do not establish physical rehearsal.'},indent=2))
