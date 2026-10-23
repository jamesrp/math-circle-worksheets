#!/usr/bin/env python3
"""Checks carried over from the old student builder (make.py, archived in the
repository's source/week-50/archive-before-problem-files-2026-10-23/). checks.txt,
which make.py wrote, records what they establish."""


def stairs(n):
    pts = [(0, 0)]
    for i in range(n):
        pts.extend([((i+1)*160/n, i*120/n), ((i+1)*160/n, (i+1)*120/n)])
    return pts


for n in [1, 2, 4, 8]:
    ps = stairs(n)
    length = sum(abs(a-c)+abs(b-d) for (a, b), (c, d) in zip(ps, ps[1:]))
    assert length == 280
assert 120**2+160**2 == 200**2
# An eight-horizontal-piece centered staircase fits the narrow 8 mm corridor.
ps = [(0, 0), (0, 7.5)]
for i in range(1, 9):
    ps.append((20*i, 15*i-7.5)); ps.append((20*i, min(120, 15*i+7.5)))
assert ps[-1] == (160, 120) and max(abs(b-.75*a) for a, b in ps) == 7.5
print('PASS student checks: staircases of 1, 2, 4 and 8 steps are 280 mm; the diagonal is 200 mm; an '
      '8-horizontal-piece staircase fits the 8 mm strip with greatest gap 7.5 mm.')

# October 23, 2026 card fixes: every changed claim on the pages and in the guide.
from fractions import Fraction as F
from heapq import heappush, heappop


def length(ps):
    return sum(abs(a-c)+abs(b-d) for (a, b), (c, d) in zip(ps, ps[1:]))


def turns(ps):
    dirs = [('H' if a != c else 'V') for (a, b), (c, d) in zip(ps, ps[1:])]
    return sum(1 for u, v in zip(dirs, dirs[1:]) if u != v)


def gap(x, y):
    return y-F(3, 4)*x


def inside(ps, d, closed=True):
    # The gap is linear along a piece, so its corners decide.
    return all((abs(gap(x, y)) <= d) if closed else (abs(gap(x, y)) < d) for x, y in ps)


# Page 1: the example's pieces in path order, A right 10, B up 20, C right 30, D up 10,
# and the one bar holds them end to end: 70 mm = 40 right + 30 up.
pieces = [('A', 10, 'right'), ('B', 20, 'up'), ('C', 30, 'right'), ('D', 10, 'up')]
pts = [(15, 56), (25, 56), (25, 36), (55, 36), (55, 26)]   # canvas mm, y down
for (name, n, way), (a, b) in zip(pieces, zip(pts, pts[1:])):
    assert abs(a[0]-b[0])+abs(a[1]-b[1]) == n and (way == 'right') == (a[1] == b[1]) and b[0] >= a[0] and b[1] <= a[1]
assert sum(n for _, n, _ in pieces) == 70 == 40+30
# B's label at (31,46) is nearer B (x = 25, y 36..56) than any other piece.
lab = (31, 46)
def dist(p, a, b):
    x = min(max(p[0], min(a[0], b[0])), max(a[0], b[0])); y = min(max(p[1], min(a[1], b[1])), max(a[1], b[1]))
    return ((p[0]-x)**2+(p[1]-y)**2)**.5
ds = [dist(lab, a, b) for a, b in zip(pts, pts[1:])]
assert min(ds) == ds[1] == 6 and sorted(ds)[1] >= 10

# Problem 3: the printed four-step staircase has lower corners 30 mm below the diagonal,
# so it leaves the 15 mm strip; the guide's 8 x (R20, U15) fits it.
four = [(F(x), F(y)) for x, y in stairs(4)]
assert max(abs(gap(x, y)) for x, y in four) == 30 and not inside(four, 15)
eight = [(F(0), F(0))]
for i in range(8):
    eight += [(F(20*(i+1)), F(15*i)), (F(20*(i+1)), F(15*(i+1)))]
assert inside(eight, 15) and length(eight) == 280


def span(y, d):
    """Width of the strip |y - 3x/4| <= d at height y, inside 0 <= x <= 160."""
    lo = max(F(0), (y-d)/F(3, 4)); hi = min(F(160), (y+d)/F(3, 4))
    return max(F(0), hi-lo)


def lower_bound(d):
    """Fewest turns the counting argument allows: k turns give at most k+1 alternating
    pieces; a horizontal piece spans at most 2d/(3/4), and an end piece (from S at
    height 0 or to F at height 120) at most d/(3/4)."""
    full, end = 2*d/F(3, 4), d/F(3, 4)
    assert all(span(F(y, 4), d) <= full for y in range(0, 481)) and span(F(0), d) == end == span(F(120), d)
    for k in range(0, 40):
        n = k+1
        best = 0
        for first in 'HV':
            seq = [('H' if (i % 2 == 0) == (first == 'H') else 'V') for i in range(n)]
            h = [i for i, s in enumerate(seq) if s == 'H']
            ends = sum(1 for i in h if i in (0, n-1))
            best = max(best, ends*end+(len(h)-ends)*full)
        if best >= 160:
            return k


def lattice_min_turns(d, m=1):
    """Fewest turns over right/up lattice staircases with steps 5/m by 3.75/m mm."""
    N = 32*m; lim = d/F(15, 4)*m       # gap = 3.75/m (j - i)
    ok = lambda i, j: abs(j-i) <= lim
    best = {}; q = [(0, 0, 0, '')]
    while q:
        t, i, j, last = heappop(q)
        if (i, j) == (N, N):
            return t
        if best.get((i, j, last), 99) <= t:
            continue
        best[(i, j, last)] = t
        for di, dj, w in ((1, 0, 'H'), (0, 1, 'V')):
            a, b = i+di, j+dj
            if a <= N and b <= N and ok(a, b):
                heappush(q, (t+(last not in ('', w)), a, b, w))


# Problem 4 (15 mm, boundary included): 8 by the bound and by the guide's witness.
wide = [(F(x), F(y)) for x, y in [(0, 0), (20, 0), (20, 30), (60, 30), (60, 60), (100, 60), (100, 90),
                                  (140, 90), (140, 120), (160, 120)]]
assert inside(wide, 15) and turns(wide) == 8 and length(wide) == 280
assert lower_bound(F(15)) == 8 and lattice_min_turns(F(15)) == 8
# Grades 4-5 Problem 5 (7.5 mm): 16 by the bound (10 + 7 x 20 = 150 < 160) and the
# guide's U7.5, (R20, U15) x 7, R20, U7.5.
narrow = [(F(0), F(0)), (F(0), F(15, 2))]
for i in range(1, 9):
    narrow += [(F(20*i), F(15*i)-F(15, 2)), (F(20*i), min(F(120), F(15*i)+F(15, 2)))]
assert narrow[-1] == (160, 120) and inside(narrow, F(15, 2)) and turns(narrow) == 16 and length(narrow) == 280
assert lower_bound(F(15, 2)) == 16 and 10+7*20 == 150 < 160 and 7*20 == 140
assert all(lattice_min_turns(F(15, 2), m) == 16 for m in (1, 2, 4))
# Overview: without the boundary, 8 turns cannot work (every span strictly shorter:
# at most 5 horizontal pieces, both ends horizontal if 5, < 2 x 20 + 3 x 40 = 160);
# 9 turns suffice.
open9 = [(0, 0), (18, 0), (18, 27), (F(107, 2), 27), (F(107, 2), F(107, 2)), (89, F(107, 2)), (89, 80),
         (F(249, 2), 80), (F(249, 2), F(213, 2)), (160, F(213, 2)), (160, 120)]
open9 = [(F(x), F(y)) for x, y in open9]
assert inside(open9, 15, closed=False) and turns(open9) == 9 and length(open9) == 280
assert 2*20+3*40 == 160 and 4*40 == 160 and 20+3*40 < 160

# Leftward travel: Routes A and B are 280 + 2 x 40 = 360 mm; any leftward travel adds length.
for route in ([(0, 0), (80, 0), (80, 40), (40, 40), (40, 80), (160, 80), (160, 120)],
              [(0, 0), (120, 0), (120, 90), (80, 90), (80, 120), (160, 120)]):
    left = sum(max(0, a-c) for (a, b), (c, d) in zip(route, route[1:]))
    assert left == 40 and length(route) == 280+2*left == 360

# Guide: a 30 cm pipe cleaner leaves a 2 cm tail; the first-visit hour is contiguous,
# with the 4-minute launch the guide names.
assert 300-280 == 20
hour = [(0, 5), (5, 9), (9, 48), (48, 55), (55, 60)]
assert all(a[1] == b[0] for a, b in zip(hour, hour[1:])) and hour[1][1]-hour[1][0] == 4

print('PASS card fixes: the example pieces A-D in path order make one 70 mm bar and B\'s label is 6 mm from B; '
      'Problem 3\'s printed staircase leaves the strip; fewest turns 8 in the 15 mm strip (9 without its boundary) '
      'and 16 in the 7.5 mm strip, by the counting bound, the witnesses and lattice searches; Routes A and B are '
      '360 mm; the pipe cleaner\'s tail and the hour.')
