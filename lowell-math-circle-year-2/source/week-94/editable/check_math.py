#!/usr/bin/env python3
"""Independent Week 94 review. Python standard library only; no draft imports.

Run: python3 check_math_independent.py
Records a solution/check for every problem in all three student packets.
"""
from fractions import Fraction as F
from itertools import combinations, product


def affine(p, q):
    x, y = p
    u, v = q
    b = F(v-y, u-x)
    return y-b*x, b


def say(label, result):
    print(f'{label}: {result}')

# K-1 Problem 1 asks for lengths, then placement invariance.
lengths = {'A': 2, 'B': 3, 'C': 4, 'D': 6}
say('K1 P1', lengths)
for n in lengths.values():
    assert all((s+n)-s == n for s in range(2, 15-n))
# Problem 2 asks all placements with one endpoint at 7.
placements = {k: [(min(7,t), max(7,t)) for t in (7-n,7+n)
                  if 2 <= t <= 14] for k,n in lengths.items()}
assert placements == {'A': [(5,7),(7,9)], 'B': [(4,7),(7,10)],
                      'C': [(3,7),(7,11)], 'D': [(7,13)]}
say('K1 P2 (fit on printed ruler)', placements)
assert 7-lengths['D'] == 1
say('K1 P2 (overhang allowed)', 'D also has endpoint pair (1,7)')
# P3: distinct supplied strips, each available once. Order is immaterial.
triples = [(i,j,k) for i,j in combinations(lengths,2) for k in lengths
           if k not in (i,j) and lengths[i]+lengths[j] == lengths[k]]
assert triples == [('A','C','D')]
say('K1 P3', triples)

# K-1 Problems 4-6 (added October 23, 2026): the tower machine, extras 1-3.
k1_extras = (1, 2, 3)
assert 2 + 1 == 3  # worked picture on page 3: 2 cubes in, 1 extra, 3 out
# P4: any one known tower shows the extra as the cubes left over beside a twin.
for c, n in product(k1_extras, range(1, 10)):
    out = n + c
    assert out - n == c and out > n
say('K1 P4', 'one known tower always shows the extra')
# P5: towers (at least one cube) coming out as 4 and 6.
k1_pairs = [(4-c, 6-c, c) for c in k1_extras if 4-c >= 1]
assert k1_pairs == [(3,5,1),(2,4,2),(1,3,3)]
assert all(q-p == 2 for p,q,c in k1_pairs)
assert [c for c in range(1, 6) if 4-c >= 1] == [1, 2, 3]  # extras 4, 5 leave no P
assert len(k1_pairs) < 4 and max(q for p,q,c in k1_pairs) <= 6  # 4 slots, 6-cell columns
assert sum(p+q for p,q,c in k1_pairs) == 18 and 18 + 4 + 6 == 28 <= 30
say('K1 P5', k1_pairs)
# P6: each known tower (in, out) fixes the extra and picks one P5 pair.
k1_rows = [(1,2),(2,5),(3,5)]
picked = [(4-(o-i), 6-(o-i), o-i) for i,o in k1_rows]
assert all(c in k1_extras for p,q,c in picked)
assert picked == [(3,5,1),(1,3,3),(2,4,2)]
assert sorted(picked) == sorted(k1_pairs)
say('K1 P6 (P, Q, extra)', picked)

# Middle P1: any known input identifies offset from report minus input.
for b,x in product(range(1,7), lengths.values()):
    assert (x+b)-x == b
say('M P1', 'one known strip always determines the offset')
# Middle P2 all pairs; P3 invariant difference.
possibilities = [(7-b,10-b,b) for b in range(1,7)]
assert possibilities == [(6,9,1),(5,8,2),(4,7,3),(3,6,4),(2,5,5),(1,4,6)]
assert all(y-x == 3 for x,y,b in possibilities)
say('M P2', possibilities)
say('M P3', 'B is exactly 3 units longer; A cannot be longer')
# Middle P4 calibration from a known reference.
rows = [(x,8-x,9-(8-x),12-(8-x)) for x in (4,6,2)]
assert rows == [(4,4,5,8),(6,2,7,10),(2,6,3,6)]
say('M P4 (known length, offset, hidden lengths)', rows)
# Middle P5 uses the same six choices, recovered from any known strip.
for x,y,b in possibilities:
    for known in lengths.values():
        inferred = (known+b)-known
        assert (7-inferred,10-inferred) == (x,y)
say('M P5', 'all six rounds solvable from any known reference')
# Middle P6 repair exactly one report, keep all input lengths.
inputs = (2,4,6)
boxes = [(5,7,10),(8,10,12),(3,6,7)]
for idx, box in enumerate(boxes,1):
    repairs = [(b,tuple(x+b for x in inputs)) for b in range(1,7)
               if sum(y != x+b for x,y in zip(inputs,box)) == 1]
    if idx == 1: assert repairs == [(3,(5,7,9))]
    if idx == 2: assert repairs == [] and len({y-x for x,y in zip(inputs,box)}) == 1
    if idx == 3: assert repairs == [(1,(3,5,7))]
    say(f'M P6 box {idx}', repairs if repairs else 'already correct: offset 6')
# Middle P7 invented challenge; two good reports fix offset uniquely.
assert (5-2) == (7-4) == 3 and (10-6) != 3
say('M P7', 'example (2,5),(4,7),(6,10), repair last report to 9')

# Upper P1 finite machine set. Two different inputs always suffice.
machines = list(product(range(1,4),range(7)))  # (copies,extra)
assert len(machines) == 21
for x,z in combinations(lengths.values(),2):
    signatures = {(b*x+a,b*z+a) for b,a in machines}
    assert len(signatures) == 21
# A 6-unit request identifies 17 rules, leaves two two-rule collisions.
groups = {}
for b,a in machines: groups.setdefault(6*b+a,[]).append((b,a))
assert {y:rules for y,rules in groups.items() if len(rules)>1} == {
    12:[(1,6),(2,0)],18:[(2,6),(3,0)]}
assert len({7*b+a for b,a in machines}) == 21
say('U P1', 'one request sometimes suffices; two distinct supplied lengths always suffice; length 7 if constructed separates all 21 at once')
# Upper P2 candidates; any second length other than 2 separates them.
candidates = [(b,a) for b,a in machines if 2*b+a == 6]
assert candidates == [(1,4),(2,2),(3,0)]
assert [3*b+a for b,a in candidates] == [7,8,9]
say('U P2', {'candidates':candidates,'3-unit reports':[7,8,9], 'single first possible':'yes'})
# Upper P3 exact affine calibration.
A = affine((2,8),(6,16)); B = affine((2,8),(6,12))
assert A == (4,2) and B == (6,1)
say('U P3', {'A reports':[A[0]+A[1]*x for x in (0,4,10)],
             'B reports':[B[0]+B[1]*x for x in (0,4,10)]})
# Uniqueness: subtract equations for two rules, then (b-b')*(6-2)=0.
# Upper P4: keep any two observations, uniquely repair the third.
points = [(2,7),(4,11),(6,16)]
repaired = []
for changed in range(3):
    a,b = affine(*[p for j,p in enumerate(points) if j != changed])
    assert b > 0
    x,y = points[changed]
    assert a+b*x != y
    repaired.append((x,a+b*x,a,b))
assert repaired == [(2,F(6),F(1),F(5,2)),
                    (4,F(23,2),F(5,2),F(9,4)),
                    (6,F(15),F(3),F(2))]
say('U P4 (changed input,new report,shift,stretch)',repaired)
# Upper P5 arbitrary fixed rules can agree at EVERY x <8 and differ at 8.
f = lambda x: 2*x+3
g = lambda x: 2*x+3 if x<8 else 2*x+4
assert all(f(x)==g(x) for x in range(1,8)) and f(8) != g(8)
say('U P5', {'table A':[f(x) for x in range(1,9)],
             'table B':[g(x) for x in range(1,9)],'forced at 8':False})
# Upper P6 optimize linear difference over rectangle of possible true reports.
for label,x,y,u,v,expected in [('A',2,8,4,12,(F(1),F(3))),
                              ('B',2,8,10,24,(F(7,4),F(9,4)))]:
    rules = [affine((x,y+e),(u,v+d)) for e,d in product((-1,1),repeat=2)]
    lo = min(rules,key=lambda rule:rule[1]); hi=max(rules,key=lambda rule:rule[1])
    assert (lo[1],hi[1]) == expected
    assert all(abs(a+b*x-y)<=1 and abs(a+b*u-v)<=1 for a,b in (lo,hi))
    say(f'U P6 pair {label} (shift,stretch)',[lo,hi])
# Upper P7 worst-case interval width =4/(u-x), before positivity intersection.
widths = {(x,u):F(4,u-x) for x,u in combinations(range(1,11),2)}
assert min(widths,key=widths.get) == (1,10) and widths[(1,10)] == F(4,9)
# Repeated reference x=3, exact repeated displayed report 8: ANY slope t>0
# works with shift 8-3t. These ten repetitions yield no slope bound.
for t in (F(1,1000),F(1),F(1000)):
    assert all((8-3*t)+3*t == 8 for _ in range(10))
# Guide P7 example (corrected October 23, 2026): with exact displays the stretch
# interval is [s-2/D, s+2/D]. Stretch 3 stays positive for every separation D >= 1;
# stretch 2 reaches 0 at D = 1; any stretch above 2/D stays positive.
def exact_display_interval(stretch, D):
    delta = stretch*D          # displayed difference when both displays are exact
    return (delta-2)/D, (delta+2)/D
for k in range(100, 901):
    D = F(k, 100)
    lo, hi = exact_display_interval(3, D)
    assert lo >= 1 and hi - lo == F(4)/D
    assert exact_display_interval(2/D + F(1,1000), D)[0] > 0
assert exact_display_interval(2, 1) == (0, 4)
# Guide P1 note: strips laid end to end. B + C = 7 (and any total of 7 or more)
# separates all 21 rules in one request.
assert lengths['B'] + lengths['C'] == 7
for n in range(7, 30):
    assert len({b*n+a for b,a in machines}) == 21
assert len({6*b+a for b,a in machines}) < 21
say('U P7', 'choose 1 and 10 for minimum worst-case width 4/9; repetitions at one reference cannot bound slope')
print('PASS: every student problem independently checked.')
