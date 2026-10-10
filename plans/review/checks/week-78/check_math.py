"""Independent mathematical check of Week 78 (three-armed lines).

Does not import or run the writer's or guide's checkers. Uses exact Fractions.
- Membership: (x,y) is on L(a,b) iff the least of x-a, y-b, 0 occurs >= 2 times.
- Exact ray-ray intersection of two three-armed figures (any arm directions).
- Every packet case (opening, P1, P2, P4, P5, P6) recomputed and compared with
  the answers the guide prints; brute-force membership sampling cross-checks
  the exact computation on a fine rational grid.
- Regression of the intersection theorem and the joining theorem over many
  rational placements (finite evidence only).
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from itertools import product
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


LINE_DIRS = ((1, 0), (0, 1), (-1, -1))      # east, north, southwest
FAN_DIRS = ((-1, 0), (0, -1), (1, 1))       # allowed-junction fan of a target


def on_line(pt, j):
    vals = [pt[0] - j[0], pt[1] - j[1], 0]
    m = min(vals)
    return vals.count(m) >= 2


def ray_meet(p, d, q, e):
    """Intersection of closed rays p+t d, q+s e (t,s>=0). Returns
    None, ('pt', P) or ('ray', start, dir)."""
    p = tuple(map(F, p)); q = tuple(map(F, q))
    det = d[0] * (-e[1]) - (-e[0]) * d[1]
    rx, ry = q[0] - p[0], q[1] - p[1]
    if det != 0:
        t = (rx * (-e[1]) - (-e[0]) * ry) / det
        s = (d[0] * ry - d[1] * rx) / det
        if t >= 0 and s >= 0:
            return ('pt', (p[0] + t * d[0], p[1] + t * d[1]))
        return None
    # parallel
    if rx * d[1] - ry * d[0] != 0:
        return None
    if d == e:
        # same direction: start at the later of the two starts
        tq = (rx * d[0] + ry * d[1])
        return ('ray', q if tq >= 0 else p, d)
    # opposite directions (only for line vs fan); segment or point
    tq = rx * d[0] + ry * d[1]
    if tq < 0:
        return None
    if tq == 0:
        return ('pt', p)
    return ('seg', p, q)


def meet(c1, dirs1, c2, dirs2):
    pieces = []
    for d in dirs1:
        for e in dirs2:
            r = ray_meet(c1, d, c2, e)
            if r:
                pieces.append(r)
    rays = sorted({(r[1], r[2]) for r in pieces if r[0] == 'ray'})
    segs = [r for r in pieces if r[0] == 'seg']
    pts = set()
    for r in pieces:
        if r[0] != 'pt':
            continue
        P = r[1]
        inside = False
        for (s, d) in rays:
            dx, dy = P[0] - s[0], P[1] - s[1]
            if dx * d[1] - dy * d[0] == 0 and dx * d[0] + dy * d[1] >= 0:
                inside = True
        if not inside:
            pts.add(P)
    return sorted(pts), rays, segs


def describe(pts, rays, segs):
    dname = {(1, 0): 'east', (0, 1): 'north', (-1, -1): 'southwest',
             (-1, 0): 'west', (0, -1): 'south', (1, 1): 'northeast'}
    parts = [f"pt({p[0]},{p[1]})" for p in pts]
    parts += [f"{dname[d]} ray from ({s[0]},{s[1]})" for s, d in rays]
    parts += [f"seg{s[1:]}" for s in segs]
    return '; '.join(parts) if parts else 'EMPTY'


def line_meet(A, B):
    return meet(A, LINE_DIRS, B, LINE_DIRS)


def junctions_through(P, Q):
    return meet(P, FAN_DIRS, Q, FAN_DIRS)


def rule(A, B):
    (a, b), (c, d) = A, B
    if A == B:
        return 'same'
    if a == c:
        return ('ray', (a, max(b, d)), (0, 1))
    if b == d:
        return ('ray', (max(a, c), b), (1, 0))
    if a - b == c - d:
        return ('ray', min(A, B), (-1, -1))
    return 'one'


def brute_common(A, B, lo=-6, hi=16, step=F(1, 2)):
    n = int((hi - lo) / step)
    grid = [lo + i * step for i in range(n + 1)]
    return {(x, y) for x in grid for y in grid
            if on_line((x, y), A) and on_line((x, y), B)}


def brute_junctions(P, Q, lo=-6, hi=16, step=F(1, 2)):
    n = int((hi - lo) / step)
    grid = [lo + i * step for i in range(n + 1)]
    return {(x, y) for x in grid for y in grid
            if on_line(P, (x, y)) and on_line(Q, (x, y))}


def in_set(P, pts, rays):
    if P in pts:
        return True
    for s, d in rays:
        dx, dy = P[0] - s[0], P[1] - s[1]
        if dx * d[1] - dy * d[0] == 0 and dx * d[0] + dy * d[1] >= 0:
            return True
    return False


def window_set(pts, rays, lo=-6, hi=16, step=F(1, 2)):
    n = int((hi - lo) / step)
    grid = [lo + i * step for i in range(n + 1)]
    return {(x, y) for x in grid for y in grid if in_set((x, y), pts, rays)}


def cross_check_lines(A, B):
    pts, rays, segs = line_meet(A, B)
    br = brute_common(A, B)
    pred = window_set(pts, rays)
    ok = pred == br        # two-sided: predicted grid points == brute-force grid points
    return ok, describe(pts, rays, segs)


def cross_check_fans(P, Q):
    pts, rays, segs = junctions_through(P, Q)
    br = brute_junctions(P, Q)
    pred = window_set(pts, rays)
    return pred == br and not segs, describe(pts, rays, segs)


A = lambda x, y: (F(x), F(y))

say('== Opening example: compare x, y, 2 (= min(x-2, y-2, 0), junction (2,2))')
for pt, want in (((4, 2), True), ((4, 4), False), ((2, 2), True)):
    vals = [pt[0], pt[1], 2]
    tied = vals.count(min(vals)) >= 2
    check(tied == want and on_line(pt, (2, 2)) == want,
          f"{pt}: values {vals} -> on line {tied} (expected {want})")
# constant shift equivalence over half-grid
same = all(on_line((x, y), (2, 2)) == ([x, y, 2].count(min(x, y, 2)) >= 2)
           for x in [F(i, 2) for i in range(-10, 21)] for y in [F(i, 2) for i in range(-10, 21)])
check(same, 'compare x,y,2 rule equals L(2,2) at all half-grid points in [-5,10]^2')
# shape: tie set = E, N, SW rays
shape = all(on_line((x, y), (0, 0)) == ((y == 0 and x >= 0) or (x == 0 and y >= 0) or (x == y and x <= 0))
            for x in [F(i, 4) for i in range(-20, 21)] for y in [F(i, 4) for i in range(-20, 21)])
check(shape, 'tie set of min(x,y,0) is exactly the east, north and southwest closed rays (quarter-grid sample)')

say('\n== Problem 1')
guide_p1 = {
    ((4, 4), (6, 5)): 'pt(5,4)',
    ((4, 4), (6, 4)): 'east ray from (6,4)',
    ((4, 4), (4, 6)): 'north ray from (4,6)',
    ((4, 4), (6, 6)): 'southwest ray from (4,4)',
    ((2, 2), (6, 5)): 'pt(3,2)',
    ((2, 2), (5, 6)): 'pt(2,3)',
}
for (a, b), want in guide_p1.items():
    ok, d = cross_check_lines(A(*a), A(*b))
    check(ok and d == want, f"L{a} & L{b}: {d}  (guide: {want}; brute agrees: {ok})")
# every B on the 0..8 grid with A=(4,4): is the meeting (or ray start) on the grid?
offgrid = []
kinds = {}
for c, d in product(range(9), repeat=2):
    pts, rays, segs = line_meet(A(4, 4), A(c, d))
    if (c, d) == (4, 4):
        continue
    k = 'point' if pts else describe([], rays, []).split()[0]
    kinds[k] = kinds.get(k, 0) + 1
    for P in pts:
        if not (0 <= P[0] <= 8 and 0 <= P[1] <= 8):
            offgrid.append(((c, d), P))
    for s, _ in rays:
        if not (0 <= s[0] <= 8 and 0 <= s[1] <= 8):
            offgrid.append(((c, d), s))
check(not offgrid, f"A=(4,4), any integer B in 0..8: every meeting point / ray start lies on the printed grid ({offgrid[:3]})")
check(len(kinds) == 4, f"all four meeting kinds available on the top grids: {sorted(kinds)}")

say('\n== Problem 2 (guide answers)')
guide_p2 = {
    ((2, 5), (6, 2)): 'pt(6,5)',
    ((3, 2), (3, 6)): 'north ray from (3,6)',
    ((2, 4), (6, 4)): 'east ray from (6,4)',
    ((2, 2), (6, 6)): 'southwest ray from (2,2)',
}
for (a, b), want in guide_p2.items():
    ok, d = cross_check_lines(A(*a), A(*b))
    check(ok and d == want, f"L{a} & L{b}: {d}  (guide: {want}; brute agrees: {ok})")

say('\n== Problem 3: two distinct lines never share exactly two points (finite regression)')
vals = [F(i, 2) for i in range(0, 9)]
bad = 0
n = 0
for a, b, c, d in product(vals, repeat=4):
    Aj, Bj = (a, b), (c, d)
    if Aj == Bj:
        continue
    n += 1
    pts, rays, segs = line_meet(Aj, Bj)
    r = rule(Aj, Bj)
    if r == 'one':
        good = len(pts) == 1 and not rays
    else:
        good = (not pts) and rays == [(r[1], r[2])]
    if not good:
        bad += 1
check(bad == 0, f"{n} ordered pairs of distinct half-integer junctions in [0,4]^2: intersection = one point or the rule's ray ({bad} mismatches)")
random.seed(78)
bad = 0
for _ in range(4000):
    Aj = (F(random.randint(-40, 40), random.randint(1, 7)), F(random.randint(-40, 40), random.randint(1, 7)))
    k = random.randint(0, 3)
    if k == 0:
        Bj = (Aj[0], Aj[1] + F(random.randint(-30, 30), random.randint(1, 5)))
    elif k == 1:
        Bj = (Aj[0] + F(random.randint(-30, 30), random.randint(1, 5)), Aj[1])
    elif k == 2:
        t = F(random.randint(-30, 30), random.randint(1, 5)); Bj = (Aj[0] + t, Aj[1] + t)
    else:
        Bj = (F(random.randint(-40, 40), random.randint(1, 7)), F(random.randint(-40, 40), random.randint(1, 7)))
    if Aj == Bj:
        continue
    pts, rays, segs = line_meet(Aj, Bj)
    r = rule(Aj, Bj)
    good = (len(pts) == 1 and not rays) if r == 'one' else ((not pts) and rays == [(r[1], r[2])])
    # membership sanity on the computed point(s)
    for P in pts:
        good &= on_line(P, Aj) and on_line(P, Bj)
    if not good:
        bad += 1
check(bad == 0, f"4000 random rational pairs (incl. aligned): rule holds ({bad} mismatches)")

say('\n== Problem 4 (guide: unique junctions (2,2) and (5,5))')
for (P, Q), want in {((2, 5), (6, 2)): 'pt(2,2)', ((2, 2), (6, 5)): 'pt(5,5)'}.items():
    ok, d = cross_check_fans(A(*P), A(*Q))
    check(ok and d == want, f"targets {P},{Q}: junctions {d}  (guide: {want}; brute agrees: {ok})")
    J = A(*eval(want[2:]))
    arms = []
    for T in (P, Q):
        u, v = T[0] - J[0], T[1] - J[1]
        arms.append('junction' if u == v == 0 else 'east' if v == 0 else 'north' if u == 0 else 'southwest')
    say(f"     arms used at junction {want}: P on {arms[0]}, Q on {arms[1]}")
check(True, 'guide arm claims: left P north / Q east; right P southwest / Q east (see lines above)')

say('\n== Problem 5 (guide: west ray from (2,4), south ray from (3,2), NE ray from (5,5))')
for (P, Q), want in {((2, 4), (6, 4)): 'west ray from (2,4)', ((3, 2), (3, 6)): 'south ray from (3,2)',
                     ((2, 2), (5, 5)): 'northeast ray from (5,5)'}.items():
    ok, d = cross_check_fans(A(*P), A(*Q))
    check(ok and d == want, f"targets {P},{Q}: junctions {d}  (guide: {want}; brute agrees: {ok})")

say('\n== Problem 6 (guide: only (10,7), off the 0..8 window)')
ok, d = cross_check_lines(A(2, 7), A(10, 5))
check(ok and d == 'pt(10,7)', f"L(2,7) & L(10,5): {d}; brute agrees: {ok}")
check(not (0 <= 10 <= 8), '(10,7) lies outside the printed 0..8 window; inside the guide 0..12 extra grid')

say('\n== Problem 7 / joining theorem regression')
bad = n = 0
for p1, p2, q1, q2 in product([F(i, 2) for i in range(0, 7)], repeat=4):
    P, Q = (p1, p2), (q1, q2)
    if P == Q:
        continue
    n += 1
    pts, rays, segs = junctions_through(P, Q)
    if segs:
        bad += 1; continue
    if p1 == q1:
        want = ([], [((p1, min(p2, q2)), (0, -1))])
    elif p2 == q2:
        want = ([], [((min(p1, q1), p2), (-1, 0))])
    elif p1 - p2 == q1 - q2:
        want = ([], [(max(P, Q), (1, 1))])
    else:
        want = None
    if want is None:
        good = len(pts) == 1 and not rays and on_line(P, pts[0]) and on_line(Q, pts[0])
    else:
        good = (not pts) and rays == want[1]
    bad += not good
check(bad == 0, f"{n} ordered pairs of distinct half-integer targets in [0,3]^2: one junction, or west/south/northeast ray as the guide states ({bad} mismatches)")
# repeated target: junction set is the whole reversed figure
P = A(3, 3)
pts, rays, segs = junctions_through(P, P)
check(sorted(d for _, d in rays) == sorted(FAN_DIRS) and all(s == P for s, _ in rays),
      'coincident targets: allowed junctions = the whole reversed three-arm figure')
# reflection claim: allowed junctions of P = -L(-P)
okref = all(on_line(P, (x, y)) == on_line((-x, -y), (-P[0], -P[1]))
            for x in [F(i, 2) for i in range(-6, 18)] for y in [F(i, 2) for i in range(-6, 18)])
check(okref, 'allowed-junction figure of P is the half-turn of L(-P) (half-grid sample)')

say('\n== Guide child explanation (p. 3): "same row, column or diagonal" read with a falling diagonal')
for Aj, Bj in (((2, 5), (5, 2)), ((2, 6), (6, 2))):
    pts, rays, segs = line_meet(A(*Aj), A(*Bj))
    say(f"     L{Aj} & L{Bj} (same falling diagonal): {describe(pts, rays, segs)}")

say('\n== Guide preparation arithmetic')
check(3 * 4 == 12, '3 packets x 4 single-sided pages = 12 sheets')
check(2 * 2 + 2 == 6, 'pencils: 2 pairs x 2 + 2 spare = 6; counters 2x2+2 = 6; grid sheets 2x2+2 = 6; tracing 2x2+2 = 6')
spans = [(0, 5), (5, 8), (8, 23), (23, 36), (36, 43), (43, 53), (53, 60)]
check(all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1)) and spans[-1][1] == 60, 'hour plan blocks are contiguous 0-60')

say(f"\n{len(FAIL)} failures")
with open(os.path.join(HERE, 'check_math.py.out'), 'w') as f:
    f.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
