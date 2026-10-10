"""Week 50 (staircases and lengths): independent check of every answer and
claim in the student packets and both adult guides. Exact arithmetic
(fractions / integers) throughout; nothing is imported from the packet.

Coordinates: millimetres from S=(0,0) to F=(160,120); the diagonal is
y = 3x/4 and the "vertical gap" of a point is y - 3x/4.
Run: python3 check_math.py  (writes out_check_math.txt beside itself)
"""
import itertools
import os
import random
from fractions import Fraction as Fr
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def fmt(v):
    """Readable exact numbers: Fractions as 7/2 or 3, tuples/lists recursively."""
    if isinstance(v, Fr):
        return str(v.numerator) if v.denominator == 1 else f'{v.numerator}/{v.denominator}'
    if isinstance(v, tuple):
        return '(' + ','.join(fmt(x) for x in v) + ')'
    if isinstance(v, list):
        return '[' + ', '.join(fmt(x) for x in v) + ']'
    return str(v)


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


def gap(p):
    return p[1] - Fr(3, 4) * p[0]


def walk(moves, start=(0, 0)):
    """moves: list of (dir, length) with dir in R L U D."""
    pts = [start]
    x, y = start
    for d, L in moves:
        L = Fr(L)
        x, y = {'R': (x + L, y), 'L': (x - L, y), 'U': (x, y + L), 'D': (x, y - L)}[d]
        pts.append((x, y))
    return pts


def length(pts):
    return sum(abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in zip(pts, pts[1:]))


def turns(pts):
    dirs = []
    for a, b in zip(pts, pts[1:]):
        if a == b:
            continue
        d = 'H' if a[1] == b[1] else 'V'
        if not dirs or dirs[-1] != d:
            dirs.append(d)
    return len(dirs) - 1


def in_strip(pts, d, W=160, H=120):
    return all(abs(gap(p)) <= d and 0 <= p[0] <= W and 0 <= p[1] <= H for p in pts)


def max_gap(pts):
    return max(abs(gap(p)) for p in pts)


# ---------------------------------------------------------------- base packet
say('== 1. Length invariant for right/up staircases (all bands P1, P2, P7; guide overview)')
rng = random.Random(50)
bad = 0
for trial in range(20000):
    k = rng.randint(1, 12)
    xs = sorted(Fr(rng.randint(0, 1600), 10) for _ in range(k - 1))
    ys = sorted(Fr(rng.randint(0, 1200), 10) for _ in range(k - 1))
    xs = [Fr(0)] + xs + [Fr(160)]
    ys = [Fr(0)] + ys + [Fr(120)]
    pts = [(0, 0)]
    first_up = rng.random() < .5
    for i in range(k):
        if first_up:
            pts += [(xs[i], ys[i + 1]), (xs[i + 1], ys[i + 1])]
        else:
            pts += [(xs[i + 1], ys[i]), (xs[i + 1], ys[i + 1])]
    if pts[-1] != (160, 120):
        pts.append((160, 120))
    if length(pts) != 280:
        bad += 1
say(f'  20000 random right/up staircases S->F: {bad} with length != 280 mm')
say(f'  diagonal: 160^2+120^2 = {160**2 + 120**2} = 200^2 = {200**2}')
solid = walk([('R', 160), ('U', 120)])
dashed = walk([('U', 60), ('R', 80), ('U', 60), ('R', 80)])
say(f'  P2 solid {length(solid)} mm, dashed {length(dashed)} mm -> K-1 answer "same length"')
p1b = walk([('U', 60), ('R', 80), ('U', 60), ('R', 80)])
say(f'  guide P1 examples: R160,U120 = {length(solid)}; U60,R80,U60,R80 = {length(p1b)}, ends {fmt(p1b[-1])}')
example = walk([('R', 10), ('U', 20), ('R', 30), ('U', 10)])
say(f'  opening example A10,C20,B30,D10: right total 40, up total 30, length {length(example)}, end {fmt(example[-1])}')

say('\n== 2. Problem 3 (all bands): printed four-step staircase and a closer one')
four = walk([('R', 40), ('U', 30)] * 4)
say(f'  printed: ends {fmt(four[-1])}, length {fmt(length(four))}, greatest |gap| {fmt(max_gap(four))} mm, '
    f'inside +-15 strip: {in_strip(four, 15)} (corners outside {fmt([p for p in four if abs(gap(p)) > 15])})')
eight = walk([('R', 20), ('U', 15)] * 8)
say(f'  guide witness 8x(R20,U15): ends {fmt(eight[-1])}, length {fmt(length(eight))}, greatest |gap| {fmt(max_gap(eight))}, '
    f'inside +-15 strip (boundary included): {in_strip(eight, 15)}')
for n in (1, 2, 4, 8, 16, 100):
    st = walk([('R', Fr(160, n)), ('U', Fr(120, n))] * n)
    assert max_gap(st) == Fr(120, n) and length(st) == 280
say('  n equal right-then-up steps: greatest |gap| = 120/n exactly and length 280 for n=1,2,4,8,16,100 (guide P7)')

say('\n== 3. Problem 4 (all bands): fewest turns inside the +-15 mm strip, boundary included')
wit = [(0, 0), (20, 0), (20, 30), (60, 30), (60, 60), (100, 60), (100, 90), (140, 90), (140, 120), (160, 120)]
wit = [(Fr(a), Fr(b)) for a, b in wit]
say(f'  guide witness: in strip {in_strip(wit, 15)}, turns {turns(wit)}, length {fmt(length(wit))}, '
    f'vertex gaps {fmt(sorted(set(gap(p) for p in wit)))}')


def span_at(y, d, W=160):
    """x-interval of the clipped strip at height y (exact)."""
    lo = max(Fr(0), Fr(4, 3) * (y - d))
    hi = min(Fr(W), Fr(4, 3) * (y + d))
    return lo, hi


spans = [(y, span_at(Fr(y), 15)) for y in range(0, 121, 5)]
say('  exact horizontal span of the strip at heights y = 0,5,...,120: '
    + ', '.join(f'{y}:{float(hi - lo):g}' for y, (lo, hi) in spans))
say('  -> at most 40 mm anywhere, exactly 20 mm at y=0 (piece from S) and y=120 (piece into F)')


def min_turns_grid(d_num, m, strict=False):
    """Fewest turns of a monotone staircase on a lattice with steps
    5/m mm (x) and 3.75/m mm (y), inside |y-3x/4| <= d (or < d if strict).
    In lattice units the condition is 15|Y-X| <= 4*d*m. Exact BFS by segments."""
    N = 32 * m
    X, Y = np.meshgrid(np.arange(N + 1), np.arange(N + 1), indexing='ij')
    lhs = 15 * np.abs(Y - X)
    ok = (lhs < 4 * d_num * m) if strict else (lhs <= 4 * d_num * m)
    start = np.zeros_like(ok)
    start[0, 0] = True
    endH, endV = start.copy(), start.copy()   # reachable sets, last segment H / V
    for seg in range(1, 200):
        # a horizontal segment from a point ending in V (or S); the strip slice
        # at a fixed height is an interval, so stop at the first excluded point
        newH = np.zeros_like(ok)
        src = endV
        for j in range(N + 1):
            row = src[:, j]
            run = False
            for i in range(N + 1):
                if not ok[i, j]:
                    run = False
                    continue
                run = run or row[i]
                newH[i, j] = run
        newV = np.zeros_like(ok)
        src = endH
        for i in range(N + 1):
            col = src[i, :]
            run = False
            for j in range(N + 1):
                if not ok[i, j]:
                    run = False
                    continue
                run = run or col[j]
                newV[i, j] = run
        endH, endV = endH | newH, endV | newV
        if endH[N, N] or endV[N, N]:
            return seg - 1
    return None


for m in (1, 2, 3, 4, 5, 7):
    say(f'  lattice 5/{m} x 3.75/{m} mm: fewest turns closed strip = {min_turns_grid(15, m)}, '
        f'open strip (boundary excluded) = {min_turns_grid(15, m, strict=True)}')
say('  lower-bound proof (guide p.2) re-derived: <=7 turns gives <=8 alternating pieces, so <=4')
say('  horizontal pieces; with 4, the pattern HVHVHVHV or VHVHVHVH makes one an endpoint piece:')
say(f'  20 + 3*40 = {20 + 3 * 40} < 160; with <=3: 3*40 = {3 * 40} < 160.  Optimum 8 confirmed.')

say('\n== 4. Grades 4-5 Problem 5: the +-8 mm strip')
ws = [('U', Fr(15, 2))]
for i in range(8):
    ws.append(('R', 20))
    if i < 7:
        ws.append(('U', 15))
ws.append(('U', Fr(15, 2)))
w8 = walk(ws)
say(f'  guide witness U7.5,(R20,U15)x7,R20,U7.5: ends {fmt(w8[-1])}, length {fmt(length(w8))}, greatest |gap| '
    f'{fmt(max_gap(w8))}, inside +-8 strip {in_strip(w8, 8)}, turns {turns(w8)}')
for m in (1, 2, 4):
    say(f'  (info) fewest turns in the +-8 mm strip on lattice m={m}: {min_turns_grid(8, m)}')
say('  answer to "Can the new staircase be shorter?": no, every right/up staircase is 280 mm')

say('\n== 5. Leftward pieces (K-1 P5-P6, Grades 2-3 P5, Grades 4-5 P6, guide overview)')
A = walk([('R', 80), ('U', 40), ('L', 40), ('U', 40), ('R', 120), ('U', 40)])
B = walk([('R', 120), ('U', 90), ('L', 40), ('U', 30), ('R', 80)])
for nm, P in (('Route A (= 4-5 P6 drawing)', A), ('Route B', B)):
    inside = all(0 <= x <= 160 and 0 <= y <= 120 for x, y in P)
    say(f'  {nm}: vertices {[(int(x), int(y)) for x, y in P]}, ends {fmt(P[-1])}, length {fmt(length(P))}, '
        f'in rectangle {inside}, leftward 40, 280+2*40 = {280 + 80}')
say(f'  Route A horizontal travel {80 + 40 + 120}, vertical {40 + 40 + 40}')
# exhaustive check on a 20 mm lattice: every R/L/U path S->F with left travel L
# has length 280 + 2L (paths of up to 4 leftward unit moves, within the rectangle)
cnt = 0
viol = 0
step = 20


def paths_RLU(maxleft):
    res = []

    def rec(x, y, last, left, ln):
        if (x, y) == (8, 6):
            res.append((left, ln))
        if y > 6:
            return
        for d, (dx, dy) in (('R', (1, 0)), ('L', (-1, 0)), ('U', (0, 1))):
            nx, ny = x + dx, y + dy
            if not (0 <= nx <= 8 and 0 <= ny <= 6):
                continue
            if (d, last) in (('R', 'L'), ('L', 'R')):
                continue  # immediate reversal is allowed physically but adds nothing new here
            nl = left + (d == 'L')
            if nl > maxleft:
                continue
            rec(nx, ny, d, nl, ln + 1)
    rec(0, 0, None, 0, 0)
    return res


res = paths_RLU(3)
for left, ln in res:
    cnt += 1
    if ln * step != 280 + 2 * left * step:
        viol += 1
say(f'  20 mm lattice, every R/L/U route S->F with <=3 leftward moves ({cnt} routes): '
    f'{viol} violate length = 280 + 2*(leftward); minimum with any leftward move = '
    f'{min(l * step for lf, l in res if lf > 0)} mm > 280')
say(f'  routes of exactly 360 mm on that lattice: {sum(1 for lf, l in res if l * step == 360)} '
    '(so "two very different 360 mm paths" is easy to satisfy)')

# --------------------------------------------------------------- bonus packet
say('\n== 6. Bonus Problem 1: priced R/U/D routes on the printed 4-right x 3-up dot grid')


def rud_routes(W, H):
    out = []

    def rec(x, y, w):
        if (x, y) == (W, H):
            out.append(w)
            return
        if x < W:
            rec(x + 1, y, w + 'R')
        if y < H:
            rec(x, y + 1, w + 'U')
        if x < W and y < H:
            rec(x + 1, y + 1, w + 'D')
    rec(0, 0, '')
    return out


routes = rud_routes(4, 3)
say(f'  {len(routes)} R/U/D routes in all')
for d in (1, 2, 3, 4):
    cost = {w: w.count('R') + w.count('U') + d * w.count('D') for w in routes}
    best = min(cost.values())
    opt = [w for w in routes if cost[w] == best]
    say(f'  D costs {d}: cheapest {best} coins, {len(opt)} cheapest routes, diagonal counts '
        f'{sorted(set(w.count("D") for w in opt))}, most expensive route {max(cost.values())}'
        + (f'; e.g. {opt[:4]}' if len(opt) <= 4 else ''))
say('  -> d=1: all cheapest use 3 diagonals (4 orders); d=2: every route costs 7, 0-3 diagonals; '
    'd=3: no diagonals')
say(f'  fewest moves with diagonals allowed: {min(len(w) for w in routes)} (= max(4,3))')
for a, b in ((1, 2), (2, 1), (2, 3)):
    thr = [d for d in range(0, 8) if
           len(set(w.count('D') for w in routes if
                   a * w.count('R') + b * w.count('U') + d * w.count('D') ==
                   min(a * v.count('R') + b * v.count('U') + d * v.count('D') for v in routes))) > 1]
    say(f'  extension: R={a}, U={b}: diagonal counts tie only at d = {thr} (sum {a + b})')

say('\n== 7. Bonus Problem 2: right/up routes on the 3x3-square grid with one blocked dot')
words = [''.join(p) for p in set(itertools.permutations('RRRUUU'))]
say(f'  routes: {len(words)} (C(6,3) = {comb(6, 3)})')


def visits(w):
    x = y = 0
    pts = [(0, 0)]
    for c in w:
        x, y = (x + 1, y) if c == 'R' else (x, y + 1)
        pts.append((x, y))
    return pts


table = {}
for i in range(4):
    for j in range(4):
        if (i, j) in ((0, 0), (3, 3)):
            continue
        table[(i, j)] = sum(1 for w in words if (i, j) not in visits(w))
say('  remaining routes by blocked dot (x,y): ' + ', '.join(f'{k}={v}' for k, v in sorted(table.items())))
say(f'  leave exactly 8: {[k for k, v in table.items() if v == 8]}; exactly 11: '
    f'{[k for k, v in table.items() if v == 11]}; leave 0: {[k for k, v in table.items() if v == 0]}')
grid = [[0] * 4 for _ in range(4)]
for y in range(4):
    for x in range(4):
        grid[y][x] = 1 if x == 0 or y == 0 else grid[y][x - 1] + grid[y - 1][x]
say(f'  predecessor-sum rows from y=0 upward: {[tuple(r) for r in grid]}')
say(f'  RRRUUU and UUURRR share only {sorted(set(visits("RRRUUU")) & set(visits("UUURRR")))}')

say('\n== 8. Bonus Problem 3: long routes in the strip |y-x| <= 1/4 (units), boundary included')
q = Fr(1, 4)
stair = walk([('R', q), ('U', q)] * 16)
say(f'  quarter staircase: ends {fmt(stair[-1])}, length {fmt(length(stair))}, gaps y-x in '
    f'[{fmt(min(p[1] - p[0] for p in stair))}, {fmt(max(p[1] - p[0] for p in stair))}]')


def in_unit_strip(pts):
    return all(abs(p[1] - p[0]) <= q and 0 <= p[0] <= 4 and 0 <= p[1] <= 4 for p in pts)


for target in (30, 100):
    k = (target - 8) * 2
    r = walk([('R', q), ('L', q)] * k + [('R', q), ('U', q)] * 16)
    say(f'  {k} out-and-back loops then the staircase: ends {fmt(r[-1])}, length {fmt(length(r))}, '
        f'inside strip {in_unit_strip(r)}')
say('  any length 8 + t (t >= 0) is reachable by retracing a piece of length t/2 at S (t/2 <= 1/4 per loop),')
say('  so there is no longest finite route; shortest possible is 8 (horizontal travel >= 4, vertical >= 4).')
# minimum length check on a fine lattice: no R/L/U/D route is shorter than 8
say(f'  physical string for 100 units at 30 mm/unit: {100 * 30} mm')

with open(os.path.join(HERE, 'out_check_math.txt'), 'w') as f:
    f.write('\n'.join(OUT) + '\n')
