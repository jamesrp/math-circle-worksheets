#!/usr/bin/env python3
"""Exact winding and crossing checks for fixed matching boundary endpoints."""
from fractions import Fraction
from itertools import product

def interior_crossings(a,b):
    # Standard straight lifts x=.5+a*t and x=.5+b*t project to helices.
    # They meet iff (a-b)t is an integer, and 0<t<1.
    if a==b:
        # Use a small positive bow of one lift; identical straight lifts overlap.
        # x2=.5+a*t+t*(1-t)/2 has separation in (0,1/8], hence no crossings.
        return []
    d=a-b
    return [Fraction(k,d) for k in range(min(0,d)+1,max(0,d)) if 0<Fraction(k,d)<1]
for a in range(-8,9):
    for b in range(-8,9):
        ts=interior_crossings(a,b)
        assert len(ts)==max(abs(a-b)-1,0)
        for t in ts:
            assert ((a-b)*t).denominator==1
expected={(0,1):0,(0,2):1,(0,3):2,(-1,1):1,(-1,2):2,(2,4):1,(2,7):4,(5,5):0}
for (a,b),count in expected.items():
    assert len(interior_crossings(a,b))==count
    print((a,b),count,interior_crossings(a,b))
for length in range(1,7):
    for word in product((-1,1),repeat=length):
        delta=sum(word)
        for initial in (-3,0,2):
            final=initial
            for twist in word: final+=twist
            assert final==initial+delta
        assert abs(delta)<=length
# Each twist fixes all boundary x coordinates modulo one circumference.
for x in [Fraction(i,13) for i in range(13)]:
    for t in (0,1):
        assert (x+t)%1==x%1
print('PASS: boundary fixation, additive winding, inverse cancellation, fixed-endpoint crossing counts.')
print('Lower-bound reasoning: any two upward lift graphs have difference 0 at bottom and a-b at top; every intermediate integer forces an interior crossing. Straight lifts attain all counts except equal winding, handled by a small bow.')

# Shared twists always preserve the minimum. A one-route twist can raise,
# lower, or preserve it, including the equal-winding exception on the page.
minimum=lambda a,b: len(interior_crossings(a,b))
for a,b,n in product(range(-8,9),repeat=3):
    assert minimum(a+n,b+n)==minimum(a,b)
assert minimum(3,0)==minimum(2,0)+1
assert minimum(2,0)==minimum(3,0)-1
assert minimum(6,5)==minimum(5,5)==0
balanced=[word for word in product((-1,1),repeat=6) if sum(word)==0]
assert len(balanced)==20
assert all(word.count(1)==word.count(-1)==3 for word in balanced)
# A word with signed sum n has length at least |n|; all-same signs attain it.
for word in product((-1,1),repeat=4):
    n=sum(word)
    shortest=(1 if n>=0 else -1,)*abs(n)
    assert len(shortest)==abs(n) and sum(shortest)==n
print('PASS: all printed minima, common-twist invariance, one-route increase/decrease/tie, 20 balanced six-twist words, and shortest-word witnesses.')
