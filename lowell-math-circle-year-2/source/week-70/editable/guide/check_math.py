#!/usr/bin/env python3
"""Independent exact checks of Week 70 guide answers; standard library only.
Finite evidence supplements, and does not replace, the guide's proofs.
"""
from fractions import Fraction as F
from math import gcd
from itertools import product, combinations
SHIELDS = {(1,1),(1,3),(3,1),(3,3)}
def first_target(x,y):
    # Target coordinates are 2 modulo 4. Find times by x; test y independently.
    possible = []
    for tx in range(min(0,x), max(0,x)+1):
        if tx % 4 == 2:
            t = F(tx,x)
            ty = t*y
            if 0 < t <= 1 and ty.denominator == 1 and ty % 4 == 2:
                possible.append((t,(F(tx),ty)))
    return min(possible)
def check():
    expect = {(2,6):((2,6),(1,3)), (6,2):((6,2),(3,1)),
              (6,6):((2,2),(1,1)), (10,6):((10,6),(1,3))}
    for end,(hit,shield) in expect.items():
        t,p = first_target(*end)
        assert p == hit
        assert tuple((v/2)%4 for v in p) == shield
    finite = list(product((-2,2,6,10), repeat=2))
    broad = [(2+4*m,2+4*n) for m,n in product(range(-25,26),repeat=2)]
    for end in finite + broad:
        t,p = first_target(*end)
        assert tuple((v/2)%4 for v in p) in SHIELDS
        d = gcd(abs(end[0]//2), abs(end[1]//2))
        assert p == (F(end[0],d), F(end[1],d))
        assert 0 < t/2 < t
    # Distinct open coordinate quadrants contain the four necessary paths.
    quadrants = set()
    for sx,sy in product((-1,1),repeat=2):
        for t in (F(k,20) for k in range(1,20)):
            x,y = (2*sx*t)%4, (2*sy*t)%4
            assert 0<x<4 and x!=2 and 0<y<4 and y!=2
            assert (x<2,y<2) == (sx>0,sy>0)
        quadrants.add((sx>0,sy>0))
    assert len(quadrants)==4
    # Non-task shared convention picture and simplest folded Problem 2 path.
    assert F(1)+F(1,2)*(4-3) == F(3,2)
    assert (5%4,2%4)==(1,2)
    assert F(2,6)*4 == F(4,3)
    assert (F(4,3),4%4)==(F(4,3),0)
    print('PASS: four task rays; all 16 map targets; 2,601 wider lift cases; shield-copy and folded-path coordinates.')

# --- October 23, 2026 (GGT70-S-v2, GGT70-FAC-v2): the review card's changes ---
def canon(p):
    return (F(p[0]) % 4, F(p[1]) % 4)
def on_segment(p, a, b):
    """p lies on the closed segment ab of the plane."""
    (px,py),(ax,ay),(bx,by) = [tuple(map(F,q)) for q in (p,a,b)]
    if (bx-ax)*(py-ay) != (by-ay)*(px-ax): return False
    return min(ax,bx) <= px <= max(ax,bx) and min(ay,by) <= py <= max(ay,by)
def on_shot(p, pieces):
    p = canon(p)
    return any(on_segment((p[0]+4*i, p[1]+4*j), a, b) for a,b in pieces for i in (-1,0,1) for j in (-1,0,1))
def crossings(a, b, c, d):
    """Intersection points of closed plane segments ab and cd (none collinear here)."""
    a,b,c,d = [tuple(map(F,q)) for q in (a,b,c,d)]
    r = (b[0]-a[0], b[1]-a[1]); q = (d[0]-c[0], d[1]-c[1])
    den = r[0]*q[1]-r[1]*q[0]
    if den == 0:
        if (c[0]-a[0])*r[1] != (c[1]-a[1])*r[0]: return []          # parallel, apart
        shared = [x for x in (a,b) if on_segment(x,c,d)] + [x for x in (c,d) if on_segment(x,a,b)]
        assert len(set(shared)) <= 1, 'collinear pieces overlap'      # touching at one end only
        return shared[:1]
    t = ((c[0]-a[0])*q[1]-(c[1]-a[1])*q[0])/den
    u = ((c[0]-a[0])*r[1]-(c[1]-a[1])*r[0])/den
    return [(a[0]+t*r[0], a[1]+t*r[1])] if 0 <= t <= 1 and 0 <= u <= 1 else []
FORBIDDEN = {canon((0,0)), canon((2,2))}
def fewest_shields(shots):
    """Smallest point sets meeting every shot. Candidates: every point on two or more
    shots, and one point on each shot alone (any point on one shot only can be
    swapped for it). Returns the minimum size and every minimum set of candidates."""
    names = list(shots)
    cands = set()
    for i,m in enumerate(names):
        for n in names[i+1:]:
            for a,b in shots[m]:
                for c,d in shots[n]:
                    for x in crossings(a,b,c,d):
                        if canon(x) not in FORBIDDEN: cands.add(canon(x))
    lone = {}
    for n in names:
        a,b = shots[n][0]
        for k in range(1,200):
            x = canon((F(a[0])+(F(b[0])-a[0])*F(k,200), F(a[1])+(F(b[1])-a[1])*F(k,200)))
            if x not in FORBIDDEN and sum(on_shot(x, shots[o]) for o in names) == 1:
                lone[n] = x; break
        cands.add(lone[n])
    hits = {x: {n for n in names if on_shot(x, shots[n])} for x in cands}
    for size in range(1, len(names)+1):
        best = [set(c) for c in combinations(sorted(cands), size) if set().union(*(hits[x] for x in c)) == set(names)]
        if best: return size, best, lone

def problem1():
    diagonals = {'SW': [((0,0),(2,2))], 'SE': [((4,0),(2,2))], 'NW': [((0,4),(2,2))], 'NE': [((4,4),(2,2))]}
    drawn = {'steep': [((0,0),(F(4,3),4)), ((F(4,3),0),(2,2))],      # toward the copy (2,6)
             'shallow': [((0,0),(4,F(4,3))), ((0,F(4,3)),(2,2))]}    # toward the copy (6,2)
    # The drawn pieces are the folded shots to (2,6) and (6,2), each up to its first T.
    for (u,v),pieces in (((2,6),drawn['steep']), ((6,2),drawn['shallow'])):
        assert gcd(u//2, v//2) == 1
        (a,b),(c,d) = pieces
        assert canon(b) == canon(c) and (b[0] in (0,4) or b[1] in (0,4))   # leave and re-enter at one seam point
        assert F(b[1]-a[1])*u == F(b[0]-a[0])*v and F(d[1]-c[1])*u == F(d[0]-c[0])*v
    shots = {**diagonals, **drawn}
    size, best, lone = fewest_shields(shots)
    assert size == 4
    assert all({(1,3),(3,1)} <= b for b in best)
    # the free pair: one point on each of the SW and NE diagonals
    for b in best:
        rest = b - {(1,3),(3,1)}
        assert len(rest) == 2 and {n for x in rest for n in ('SW','NE') if on_shot(x, shots[n])} == {'SW','NE'}
    # where the drawn shots meet: each diagonal crossing, and their own two crossings
    steep_meets = {canon(x) for p in drawn['steep'] for q in [v[0] for v in diagonals.values()] for x in crossings(*p,*q)} - FORBIDDEN
    shallow_meets = {canon(x) for p in drawn['shallow'] for q in [v[0] for v in diagonals.values()] for x in crossings(*p,*q)} - FORBIDDEN
    assert steep_meets == {(1,3)} and shallow_meets == {(3,1)}
    both = {canon(x) for p in drawn['steep'] for q in drawn['shallow'] for x in crossings(*p,*q)} - FORBIDDEN
    assert both == {(F(1,2),F(3,2)), (F(3,2),F(1,2))}
    # a shield where the drawn shots cross blocks no diagonal, so that start needs five
    assert not any(on_shot(x, diagonals[n]) for x in both for n in diagonals)
    return len(best)

def problem3_forcing():
    """On the map, (6,-2) meets the diagonals only at (3,3); (10,2) meets the SW/NE
    diagonals only at (1,1); so with Problem 1's (1,3) and (3,1) the answer is unique."""
    def diag_meets(u, v):
        # the shot to its first T copy (u,v) at time t is (tu, tv); it is on the SW/NE
        # diagonals when tu = tv (mod 4) and on the SE/NW ones when tu = -tv (mod 4)
        assert gcd(abs(u)//2, abs(v)//2) == 1
        out = set()
        for w, sign in ((u-v, 'SW/NE'), (u+v, 'SE/NW')):
            if w == 0: continue
            for j in range(-abs(w), abs(w)+1):
                t = F(4*j, w)
                if 0 < t < 1:
                    out.add((canon((t*u, t*v)), sign))
        return out
    m1 = diag_meets(6, -2); assert m1 == {((3,3),'SW/NE')}
    m2 = diag_meets(10, 2); assert {p for p,s in m2 if s == 'SW/NE'} == {(1,1)}
    assert (1,3) not in {p for p,_ in m2} and (3,1) not in {p for p,_ in m2}
    assert all(c in {-2,2,6,10} for c in (6,-2,10,2))
    return True

def extension():
    """No T: shots from S back to S. First S copy (4a,4b), a and b coprime."""
    three = {(2,0),(0,2),(2,2)}
    n = 0
    for m, k in product(range(-40,41), repeat=2):
        if (m,k) == (0,0): continue
        g = gcd(abs(m), abs(k)); a, b = m//g, k//g
        # the first S copy on the segment to (4m,4k) is (4a,4b): the point at time j/q of
        # (4a,4b), with j/q in lowest terms, is an S copy only if q divides a and b
        assert gcd(abs(a), abs(b)) == 1
        assert all((4*a*j) % (4*q) or (4*b*j) % (4*q) for q in range(2, 13) for j in range(1, q) if gcd(j, q) == 1)
        assert ((2*a) % 4, (2*b) % 4) in three
        n += 1
    # the three disjoint returning shots: interiors (4t,0), (0,4t), (4t,4t) never meet mod 4
    shots = [(4,0),(0,4),(4,4)]
    for (u1,v1),(u2,v2) in combinations(shots, 2):
        for i, j in product(range(-2,3), repeat=2):
            den = u1*(-v2) - v1*(-u2)
            assert den != 0
            t = F(4*i*(-v2) - 4*j*(-u2), den); s = F(u1*4*j - v1*4*i, den)
            assert not (0 < t < 1 and 0 < s < 1)
    return n

import pathlib
here = pathlib.Path(__file__).resolve().parent
guide = (here/'facilitator.tex').read_text()
student = (here.parent/'student'/'students.tex').read_text()
def wording():
    for phrase in ['GGT70-FAC-v3', 'GGT70-S-v2 student packet', 'about 5 minutes on Problem 1',
                   'meets the diagonals only at $(1,3)$', 'only at $(3,1)$', 'at $(\\frac12,1\\frac12)$ or $(1\\frac12,\\frac12)$, needs five',
                   'tracing paper about 6\\,cm square', 'clear counters with a centre dot',
                   'the shot toward $(6,-2)$ meets the diagonals only at $(3,3)$', 'the shot toward $(10,2)$ then forces $(1,1)$',
                   'Extension: shots back to $S$', 'folds to $(2,0)$, $(0,2)$ or $(2,2)$', 'The shots to $(4,0)$, $(0,4)$ and $(4,4)$',
                   'A possible Grades 2--3 route, untested', 'A $(2,6)$ & $(2,6)$ & $(1,3)$',
                   # critic follow-up, October 23, 2026 (GGT70-FAC-v3): the Grades 2-3 route continues to Problem 2's A-C
                   'about 15--20 minutes', "then Problem 2's shots A--C, laying a ruler from S to each letter", "A and B are Problem 1's drawn shots unfolded",
                   "C stops at the room's own T."]:
        assert phrase in guide, phrase
    for phrase in ['Problem 1 alone', 'roughly 10 minutes on Problem 1', 'four small counters', 'All four small student rooms', 'GGT70-S-v1', 'move a counter']:
        assert phrase not in guide, phrase
    for phrase in ['GGT70-S-v2', 'marked with a small pencil cross', 'A shield stops a shot only if the shot passes exactly through that point',
                   'each large square is another copy of the same room, and every T is the same target',
                   'stops all six shots', 'T copies A $(2,6)$, B $(6,2)$, C $(6,6)$ and D $(10,6)$', 'crosses an X or Y edge',
                   'in the bold room that stop every shot', '\\mapwindow[1.05]{}',
                   '(0,0)--(4/3,4)', '(4/3,0)--(2,2)', '(0,0)--(4,4/3)', '(0,4/3)--(2,2)', '{2/6/A,6/2/B,6/6/C,10/6/D}']:
        assert phrase in student, phrase
    for phrase in ['Swap jobs', 'A counter marks', 'The bold square is the room shown below', 'crosses a portal', 'A shot stops only if']:
        assert phrase not in student, phrase
    p3 = student.split('\\problem{3}')[1].split('\\problem{4}')[0]
    assert '\\room' not in p3
    p1 = student.split('\\problem{1}')[1].split('\\problem{2}')[0]
    assert p1.count('\\room') == 1
if __name__ == '__main__':
    check()
    problem1(); problem3_forcing(); n = extension(); wording()
    print(f'PASS: Problem 1 six shots need 4 shields, (1,3) and (3,1) forced; map answer unique; {n:,} returning shots fold to (2,0), (0,2), (2,2) and three disjoint ones need 3; printed wording.')
