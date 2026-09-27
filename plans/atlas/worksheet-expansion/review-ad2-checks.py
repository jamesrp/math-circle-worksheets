"""Independent AD2 instance checks; general proofs are reviewed in the companion note.

This script does not import the author's checker or mutate author-owned data.
All calculations are exact. Finite scans supplement, not replace, the stated proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, lcm
from pathlib import Path
import json

OUT = {}

# AD09: compare direct full-period inventories with the proposed gcd criterion.
cases = 0
for m, n in product(range(1, 13), repeat=2):
    period = lcm(m, n)
    seen = {(t % m, t % n) for t in range(period)}
    predicted = {(a, b) for a in range(m) for b in range(n)
                 if (b-a) % gcd(m, n) == 0}
    assert seen == predicted and len(seen) == period
    cases += m*n
assert [t for t in range(60) if t%4 == 3 and t%6 == 5 and t%5 == 2] == [47]
OUT['AD-09'] = {'modulus_pairs': 144, 'report_pairs': cases, 'three_clock_first': 47}

# AD10: direct square testing is independent of the recurrence generator.
pairs = []
for y in range(1, 20001):
    x = isqrt(2*y*y+1)
    if x*x == 2*y*y+1:
        pairs.append((x, y))
assert pairs == [(3,2),(17,12),(99,70),(577,408),(3363,2378),(19601,13860)]
for x,y in pairs[1:]:
    a,b = 3*x-4*y, 3*y-2*x
    assert a>0 and 0<b<y and a*a-2*b*b==1
    assert (3*a+4*b,2*a+3*b)==(x,y)
totals = [0]+[(y//2)**2 for _,y in pairs]
assert all(c==34*b-a+2 for a,b,c in zip(totals,totals[1:],totals[2:]))
assert totals == [0,1,36,1225,41616,1413721,48024900]
OUT['AD-10'] = {'direct_scan_y_max': 20000, 'solutions': pairs, 'totals': totals}

# AD11: bit-polynomial convolution and long remainder division.
def mul(a,b,modulus):
    raw=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                raw ^= 1<<(i+j)
    while raw.bit_length() >= modulus.bit_length():
        raw ^= modulus << (raw.bit_length()-modulus.bit_length())
    return raw
A=lambda a,b:mul(a,b,0b110)
B=lambda a,b:mul(a,b,0b111)
assert [[j for j in range(4) if A(i,j)==1] for i in range(4)] == [[],[1],[],[]]
assert [[j for j in range(4) if B(i,j)==1] for i in range(4)] == [[],[1],[3],[2]]
affine_cases=0
for r,s in product(range(4),repeat=2):
    if r==s: continue
    reports={}
    for a,b in product(range(4),repeat=2):
        report=(B(a,r)^b,B(a,s)^b)
        assert report not in reports
        reports[report]=(a,b)
    assert len(reports)==16
    affine_cases+=16
assert [(a,b) for a,b in product(range(4),repeat=2) if B(a,1)^b==2 and B(a,2)^b==0]==[(3,1)]
assert not [(a,b) for a,b in product(range(4),repeat=2) if A(a,1)^b==2 and A(a,2)^b==0]
for a,b in product(range(4),repeat=2):
    assert B(a^b,a^b)==(B(a,a)^B(b,b))
    assert B(B(a,b),B(a,b))==B(B(a,a),B(b,b))
OUT['AD-11']={'all_distinct_input_output_cases':affine_cases,'decode_a_b':[3,1], 'encoding':'0=0,1=1,t=2,u=3'}

# AD12: exact bracketing and the rational-root candidates of both irreducible cubics.
assert F(1442,1000)**3 < 3 < F(1443,1000)**3
assert [z**3-3 for z in [-3,-1,1,3]] == [-30,-4,-2,24]
assert [z**3-3*z-1 for z in [-1,1]] == [1,-3]
OUT['AD-12']={'bracket_cubes':[str(F(1442,1000)**3),str(F(1443,1000)**3)],
              'irreducibility':'Manual rational-root and cubic factor-degree proofs reviewed; finite evaluation checks listed candidates.'}

# AD13: infinite finiteness criterion first, then a bounding-rectangle enumeration.
corners=[(3,0),(2,1),(1,3),(0,4)]
def survivors(cs):
    xbounds=[a for a,b in cs if b==0]
    ybounds=[b for a,b in cs if a==0]
    if not xbounds or not ybounds: return None
    return {(i,j) for i in range(min(xbounds)) for j in range(min(ybounds))
            if not any(i>=a and j>=b for a,b in cs)}
S=survivors(corners)
assert len(S)==8
moves=[]
for k,(a,b) in enumerate(corners):
    for di,dj in [(1,0),(0,1)]:
        cs=corners.copy();cs[k]=(a+di,b+dj)
        s=survivors(cs)
        moves.append({'old':[a,b],'new':[a+di,b+dj],'count':None if s is None else len(s)})
assert [m['count'] for m in moves]==[9,None,10,9,9,9,None,9]
socle={(i,j) for i,j in S if (i+1,j) not in S and (i,j+1) not in S}
assert socle=={(0,3),(1,2),(2,0)}
assert {(i,j) for i,j in S if (i,j+1) not in S}==socle
for r,s in product(range(1,9),repeat=2):
    rect=survivors([(r,0),(0,s)])
    assert len(rect)==r*s
    assert {(i,j) for i,j in rect if (i+1,j) not in rect and (i,j+1) not in rect}=={(r-1,s-1)}
OUT['AD-13']={'moves':moves,'common_annihilator_monomials':sorted(socle),'rectangle_cases':64}

# AD14: truncated coefficient-array arithmetic, without derivative code in evaluation.
def jetmul(a,b):
    n=len(a)
    return tuple(sum(a[i]*b[k-i] for i in range(k+1)) for k in range(n))
def jeteval(coeffs,z):
    out=(F(0),)*len(z)
    for c in reversed(coeffs):
        out=jetmul(out,z)
        out=(out[0]+c,)+out[1:]
    return out
coeffs=(-2,1,-2,1)
assert jeteval(coeffs,(F(3),F(1)))==(10,16)
assert jeteval(coeffs,(F(3),F(2)))==(10,32)
assert jeteval((0,0,0,1),(F(2),F(1),F(3)))==(8,12,42)
jet_cases=0
for degree in range(7):
    coeffs=tuple(F((-1)**k*(k+1),k+2) for k in range(degree+1))
    for a,b,c in product([F(-2),F(0),F(1,2)],repeat=3):
        val=sum(co*a**k for k,co in enumerate(coeffs))
        d1=sum(k*coeffs[k]*a**(k-1) for k in range(1,len(coeffs)))
        d2=sum(k*(k-1)*coeffs[k]*a**(k-2) for k in range(2,len(coeffs)))
        assert jeteval(coeffs,(a,b,c))==(val,b*d1,c*d1+b*b*d2/2)
        jet_cases+=1
OUT['AD-14']={'second_order_jet_cases':jet_cases,'cube_jet':[8,12,42]}

# AD15: exact forward/inverse verification, primitive triples, including zero/negative slope.
triples=0
for p in range(-20,21):
    for q in range(1,21):
        if gcd(p,q)!=1: continue
        a,b,c=q*q-2*p*p,2*p*q,q*q+2*p*p
        assert a*a+2*b*b==c*c
        assert gcd(gcd(a,b),c)==(1 if q%2 else 2)
        x,y=F(a,c),F(b,c)
        assert x*x+2*y*y==1 and x!=-1 and y/(x+1)==F(p,q)
        triples+=1
assert F(1,17)**2+2*F(12,17)**2==1
OUT['AD-15']={'coprime_slope_cases':triples,'special_decode_slope':str(F(6,11)/(F(-7,11)+1))}

# AD16: enumerate actual projective equivalence classes, then independently check
# the finite addition law and its isomorphism with a clock.
aff={(x,y) for x,y in product(range(5),repeat=2) if (y*y-x*x*x-x-1)%5==0}
def canon(t):
    first=next(x for x in t if x)
    inv=pow(first,-1,5)
    return tuple(x*inv%5 for x in t)
proj={canon((x,y,z)) for x,y,z in product(range(5),repeat=3)
      if (x,y,z)!=(0,0,0) and (y*y*z-x*x*x-x*z*z-z*z*z)%5==0}
assert len(proj)==9 and sum(z==0 for x,y,z in proj)==1
def add(p,q):
    if p is None:return q
    if q is None:return p
    x,y=p; u,v=q
    if x==u and (y+v)%5==0:return None
    slope=((3*x*x+1)*pow(2*y,-1,5) if p==q else (v-y)*pow(u-x,-1,5))%5
    xx=(slope*slope-x-u)%5
    return xx,(slope*(x-xx)-y)%5
P=(0,1); orbit=[None]
for i in range(9):orbit.append(add(orbit[-1],P))
assert orbit==[None,(0,1),(4,2),(2,1),(3,4),(3,1),(2,4),(4,3),(0,4),None]
points=orbit[:-1]
assert set(points)==aff|{None}
for i,j in product(range(9),repeat=2):
    assert add(points[i],points[j])==points[(i+j)%9]
for p,q,r in product(points,repeat=3):assert add(add(p,q),r)==add(p,add(q,r))
subgroups=[]
for mask in range(1<<9):
    labels={i for i in range(9) if mask>>i&1}
    if 0 in labels and all((a+b)%9 in labels for a,b in product(labels,repeat=2)):
        subgroups.append(sorted(labels))
assert subgroups==[[0],[0,3,6],list(range(9))]
assert [[i for i in range(9) if a*i%9==b] for a,b in [(2,1),(3,1),(3,0),(3,3)]]==[[5],[],[0,3,6],[1,4,7]]
OUT['AD-16']={'projective_point_count':len(proj),'orbit':orbit,'all_addition_pairs':81,
              'associativity_triples':729,'all_subset_subgroup_scan':512,'subgroup_labels':subgroups}

OUT['status']='PASS'
Path(__file__).with_name('review-ad2-checks-results.json').write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps(OUT,indent=2))
