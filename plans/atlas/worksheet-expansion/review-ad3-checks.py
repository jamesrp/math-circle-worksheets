#!/usr/bin/env python3
"""Independent finite-instance checks supporting the AD3 written proof review."""
from itertools import combinations, product
from math import comb, gcd
from fractions import Fraction as F
from functools import reduce
import json

# AD-17: exact first-entry boundary, including both excluded endpoints.
for d, first in [(F(3),2),(F(-3),2),(F(6),3),(F(-6),3),(F(12),3),(F(-12),3),(F(13),4)]:
    x,y=F(2)+d/3,F(2)-2*d/3
    errors=[]
    for n in range(6):
        assert 2*x+y==6
        errors.append(max(abs(x-2),abs(y-2)))
        x,y=(3*x+y)/4,(x+y)/2
    assert next(i for i,e in enumerate(errors) if e<=F(1,8))==first

# AD-20: independent entrywise multiplication and finite centralizer inventory.
def mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
def bracket(a,b):return tuple(x-y for x,y in zip(mul(a,b),mul(b,a)))
N=(1,1,-1,-1);C=(1,0,0,0);zero=(0,0,0,0)
assert mul(N,N)==zero
centralizer_trials=0
for B in product(range(-2,3),repeat=4):
    a,b,c,d=B
    assert (bracket(N,B)==zero)==(c==-b and d==a-2*b)
    centralizer_trials+=1
assert bracket(bracket(N,C),C)==(0,1,-1,0)
assert bracket(N,bracket(C,C))==zero

# AD-22: build every cycle directly from incidence, without the author's
# four-coordinate parametrization, and compare all face-subset reachability.
edges=['AB','BC','CD','DA','OA','OB','OC','OD']
vertices='ABCDO'
cycles={mask for mask in range(256) if all(sum(bool(mask&(1<<i)) for i,e in enumerate(edges) if v in e)%2==0 for v in vertices)}
triangles=[['AB','OA','OB'],['BC','OB','OC'],['CD','OC','OD'],['DA','OD','OA']]
faces=[sum(1<<edges.index(e) for e in tri) for tri in triangles]
assert len(cycles)==16 and set(faces)<=cycles
for subset in range(16):
    moves=[faces[i] for i in range(4) if subset&(1<<i)]
    reached={0};front=[0]
    while front:
        x=front.pop()
        for m in moves:
            y=x^m
            if y not in reached:reached.add(y);front.append(y)
    assert len(reached)==2**len(moves)
    classes={frozenset(x^r for r in reached) for x in cycles}
    assert len(classes)==2**(4-len(moves))
    for x,y in product(cycles,repeat=2):
        same_untouched=all(bool(x&(1<<i))==bool(y&(1<<i)) for i in range(4) if not subset&(1<<i))
        assert ((x^y) in reached)==same_untouched
outer=sum(1<<edges.index(e) for e in ['AB','BC','CD','DA'])
loop=sum(1<<edges.index(e) for e in ['AB','BC','OC','OA'])
assert outer==faces[0]^faces[1]^faces[2]^faces[3]
assert loop==faces[0]^faces[1]
cap=outer
kernel=[s for s in range(32) if reduce(int.__xor__,[m for i,m in enumerate(faces+[cap]) if s&(1<<i)],0)==0]
assert kernel==[0,31]

# AD-24: actual orbit enumeration independently checks the fixed-point formula
# for all weights through n=9, plus the reflection merge and named instances.
def rot(x,j):return x[j:]+x[:j]
def strings(n,r):
    return [tuple(int(i in red) for i in range(n)) for red in combinations(range(n),r)]
def fixed_formula(n,r,j):
    g=gcd(n,j);L=n//g
    return comb(g,r//L) if r%L==0 else 0
cases=0
for n in range(1,10):
    for r in range(n+1):
        xs=strings(n,r)
        actual=[sum(rot(x,j)==x for x in xs) for j in range(n)]
        assert actual==[fixed_formula(n,r,j) for j in range(n)]
        orbits={min(rot(x,j) for j in range(n)) for x in xs}
        assert sum(actual)==n*len(orbits)
        if gcd(n,r)==1 and 0<r<n:
            assert all(len({rot(x,j) for j in range(n)})==n for x in xs)
        cases+=1
xs=strings(6,3)
necklaces={min(rot(x,j) for j in range(6)) for x in xs}
bracelets={min([rot(x,j) for j in range(6)]+[rot(x[::-1],j) for j in range(6)]) for x in xs}
assert len(necklaces)==4 and len(bracelets)==3
assert sorted(len({rot(x,j) for j in range(6)}) for x in necklaces)==[2,6,6,6]
assert [sum(rot(x,j)==x for x in xs) for j in range(6)]==[20,0,2,0,2,0]
assert [sum(rot(x,j)==x for x in strings(8,4)) for j in range(8)]==[70,0,2,0,6,0,2,0]
print(json.dumps({'status':'pass','threshold_boundary_examples':7,'centralizer_trials':centralizer_trials,'closed_patterns':16,'face_subsets':16,'necklace_weight_cases':cases,'six_bead_necklaces':4,'six_bead_bracelets':3,'scope':'Finite checks support, and do not replace, independently reviewed general proofs.'}))
