"""Independent exact checks supporting the editor's GA2 proof review.

Finite checks validate arithmetic/encodings. General completeness arguments are
recorded separately in review-ga2-design.md; these checks do not replace them.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

def tent(x):return 2*x if x<=F(1,2) else 2-2*x

def coded_point(word):
    a,b=F(1),F(0)
    # Build B0 o B1 o ... o B(n-1), applying rightmost branch first.
    for letter in reversed(word):
        a,b=(a/2,b/2) if letter=='L' else (-a/2,1-b/2)
    return b/(1-a)

orbits=0
for n in range(1,9):
 for word in product('LR',repeat=n):
    x=coded_point(word);z=x;seen=[]
    for letter in word:
        assert 0<=z<=1 and z!=F(1,2)
        assert (z<F(1,2))==(letter=='L')
        seen.append(z);z=tent(z)
    assert z==x
    period=next(k for k in range(1,n+1) if seen[k%n]==x)
    word_period=next(k for k in range(1,n+1) if n%k==0 and tuple(word)==tuple(word[:k])*(n//k))
    assert period==word_period
    orbits+=1

# Orthogonality/inverse and translation signs for the two-bit character basis.
bits=list(product(range(2),repeat=2))
chars=[[(-1)**sum(a*b for a,b in zip(k,x)) for x in bits] for k in bits]
assert [[sum(a*b for a,b in zip(u,v)) for v in chars] for u in chars]==[[4*int(i==j) for j in range(4)] for i in range(4)]
patterns=0
for vals in product(range(-2,3),repeat=4):
    coeff=[sum(F(v)*s for v,s in zip(vals,c))/4 for c in chars]
    assert [sum(coeff[j]*chars[j][i] for j in range(4)) for i in range(4)]==list(vals)
    for shift in bits:
        moved=[vals[bits.index(tuple(a^b for a,b in zip(x,shift)))] for x in bits]
        changed=[sum(F(v)*s for v,s in zip(moved,c))/4 for c in chars]
        signs=[(-1)**sum(a*b for a,b in zip(k,shift)) for k in bits]
        assert changed==[c*s for c,s in zip(coeff,signs)]
    patterns+=1

# Integrate each affine overlap piece exactly using its endpoint trapezoid area.
windows=0
for a,b in product([F(1,3),F(1,2),F(1),F(3,2),F(2),F(4)],repeat=2):
    cuts=sorted(set([F(0),min(a,b),max(a,b),a+b]))
    overlap=lambda t:max(F(0),min(a,t)-max(F(0),t-b))
    area=sum((q-p)*(overlap(p)+overlap(q))/2 for p,q in zip(cuts,cuts[1:]))
    assert area==a*b
    height=min(a,b);support=a+b
    assert sorted([height,support-height])==sorted([a,b])
    for t in [F(-1),F(0),min(a,b)/2,min(a,b),max(a,b),a+b,F(10)]:
        expected=max(F(0),min(t,a,b,a+b-t))
        assert overlap(t)==expected
    windows+=1

# Affine minimax x² on [l,r]: secant minus (r-l)²/8; all three
# certificate errors alternate with exactly that magnitude.
intervals=0
for l in range(-4,5):
 for r in range(l+1,6):
    l,r=F(l),F(r);E=(r-l)**2/8
    p=lambda x:(l+r)*x-l*r-E
    assert [x*x-p(x) for x in [l,(l+r)/2,r]]==[E,-E,E]
    intervals+=1

result={'status':'pass','tent_branch_words_lengths_1_through_8':orbits,
        'signed_brightness_patterns_all_four_translations':patterns,
        'rational_window_pairs':windows,'minimax_interval_certificates':intervals,
        'limits':'Exact instances and finite inventories; see written review for general proofs and calculus.'}
Path(__file__).with_name('review-ga2-checks-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
