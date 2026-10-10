#!/usr/bin/env python3
"""Week 73 (The gentlest stretch): independent math check for the review.

Written for the math-check stage; imports nothing from the packet's own
checkers. Exact rational arithmetic wherever a comparison decides a claim.
Coordinates are normalized: old sheet [0,4]x[0,1], new square [0,2]x[0,2],
lower-left corner A at the origin on both.
Run: python3 check_math.py  (output saved beside it as check_math.py.out)
"""
from fractions import Fraction as Fr
from itertools import combinations
from math import sqrt
from pathlib import Path
import random

REPO = Path(__file__).resolve().parents[4]
fails = 0
checks = 0


def ok(cond, msg):
    global fails, checks
    checks += 1
    if not cond:
        fails += 1
    print(('PASS ' if cond else 'FAIL ') + msg)


def d2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def mid(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


# ---------------------------------------------------------------- page 1
print('== Page 1 example and Problem 1 (five-pin game) ==')
ok(Fr(3, 2) == Fr(3) / Fr(2), 'example: 2 cm -> 3 cm is stretch 3/2 = 1 1/2')

OLD = {'A': (Fr(0), Fr(0)), 'B': (Fr(4), Fr(0)), 'C': (Fr(4), Fr(1)), 'D': (Fr(0), Fr(1)),
       'O': (Fr(2), Fr(1, 2))}
NEWC = {'A': (Fr(0), Fr(0)), 'B': (Fr(2), Fr(0)), 'C': (Fr(2), Fr(2)), 'D': (Fr(0), Fr(2))}

STEP = Fr(1, 40)
grid = [(i * STEP, j * STEP) for i in range(1, 80) for j in range(1, 80)]  # strictly interior O'
print(f'interior O\' positions tested: {len(grid)} (step 1/40)')

all_tie = True
corner_pairs_only_at_4 = True
max_O_ratio2 = Fr(0)
for O2 in grid:
    new = dict(NEWC, O=O2)
    best = Fr(0)
    for a, b in combinations('ABCDO', 2):
        r2 = d2(new[a], new[b]) / d2(OLD[a], OLD[b])
        best = max(best, r2)
        if 'O' in (a, b):
            max_O_ratio2 = max(max_O_ratio2, r2)
            if r2 >= 4:
                corner_pairs_only_at_4 = False
    if best != 4:
        all_tie = False
ok(all_tie, 'every interior O\': max squared stretch over all 10 pairs is exactly 4 (stretch 2)')
ok(corner_pairs_only_at_4, 'no O-to-corner pair reaches stretch 2 at any tested interior O\'')
ok(Fr(8) / Fr(17, 4) == Fr(32, 17) and Fr(32, 17) < 4,
   'sup of O-corner squared ratio is 8/(17/4) = 32/17 < 4 (ratio < 1.372)')
print(f'   largest O-corner squared ratio on the grid: {float(max_O_ratio2):.4f} (< 32/17 = {32/17:.4f})')
for a, b in combinations('ABCD', 2):
    r2 = d2(NEWC[a], NEWC[b]) / d2(OLD[a], OLD[b])
    print(f'   corner pair {a}{b}: squared ratio {r2} -> stretch {sqrt(r2):.4f}')
ok(d2(OLD['O'], OLD['A']) == Fr(17, 4), 'old OA = sqrt(17)/2 (guide p.2)')
ok(d2(OLD['A'], OLD['C']) == 17 and d2(NEWC['A'], NEWC['C']) == 8, 'corner diagonals sqrt17 -> sqrt8')
ok(len(list(combinations('ABCDO', 2))) == 10, 'ten pairs = six corner pairs + four O-corner pairs')

# ---------------------------------------------------------------- page 2
print('\n== Problem 2 (four-triangle affine fan) ==')


def affine_from(tri_old, tri_new):
    """Exact affine map sending three old points to three new points: returns (M, t)."""
    (x0, y0), (x1, y1), (x2, y2) = tri_old
    (X0, Y0), (X1, Y1), (X2, Y2) = tri_new
    a11, a12, a21, a22 = x1 - x0, x2 - x0, y1 - y0, y2 - y0
    det = a11 * a22 - a12 * a21
    assert det != 0
    inv = (a22 / det, -a12 / det, -a21 / det, a11 / det)
    b = (X1 - X0, X2 - X0, Y1 - Y0, Y2 - Y0)
    # M * [[a11,a12],[a21,a22]] = [[b0,b1],[b2,b3]]
    m11 = b[0] * inv[0] + b[1] * inv[2]
    m12 = b[0] * inv[1] + b[1] * inv[3]
    m21 = b[2] * inv[0] + b[3] * inv[2]
    m22 = b[2] * inv[1] + b[3] * inv[3]
    t = (X0 - (m11 * x0 + m12 * y0), Y0 - (m21 * x0 + m22 * y0))
    return (m11, m12, m21, m22), t


TRIS = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]


def fan(O2):
    pieces = []
    for p, q in TRIS:
        M, t = affine_from((OLD['O'], OLD[p], OLD[q]), (O2, NEWC[p], NEWC[q]))
        pieces.append(((p, q), M, t))
    return pieces


def opnorm2(M):
    """Exact largest eigenvalue of M^T M, returned as float, plus exact test vs 4."""
    a, b, c, d = M
    s11, s12, s22 = a * a + c * c, a * b + c * d, b * b + d * d
    tr, det = s11 + s22, s11 * s22 - s12 * s12
    lam = (float(tr) + sqrt(max(float(tr * tr - 4 * det), 0))) / 2
    # largest eigenvalue <= 4  iff  (4I - S) is PSD  iff  4 - s11 >= 0, 4 - s22 >= 0, det(4I-S) >= 0
    le4 = (4 - s11 >= 0) and (4 - s22 >= 0) and ((4 - s11) * (4 - s22) - s12 * s12 >= 0)
    return lam, le4


centre = fan((Fr(1), Fr(1)))
ok(all(M == (Fr(1, 2), 0, 0, Fr(2)) and t == (0, 0) for _, M, t in centre),
   'centered fan: each of the four triangle maps equals F(x,y) = (x/2, 2y)')

# Lipschitz constant of a piecewise-affine map on a convex domain = max piece operator norm
off_fail = True
for O2 in grid:
    if O2 == (1, 1):
        continue
    if all(opnorm2(M)[1] for _, M, _t in fan(O2)):
        off_fail = False
ok(off_fail, 'every off-center interior O\' on the grid gives a fan whose true worst stretch exceeds 2')
ok(all(opnorm2(M)[1] for _, M, _t in centre) and max(opnorm2(M)[0] for _, M, _t in centre) == 4.0,
   'centered fan has worst stretch exactly 2')

# halfway dots: side midpoints and O-corner midpoints, old and new
def dots(O2):
    old = dict(OLD)
    new = dict(NEWC, O=O2)
    for p, q in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]:
        old['m' + p + q] = mid(OLD[p], OLD[q])
        new['m' + p + q] = mid(new[p], new[q])
    for p in 'ABCD':
        old['mO' + p] = mid(OLD['O'], OLD[p])
        new['mO' + p] = mid(O2, NEWC[p])
    return old, new


detecting = {}
survivors = []
for O2 in grid:
    old, new = dots(O2)
    bad = [(a, b) for a, b in combinations(sorted(old), 2) if d2(new[a], new[b]) > 4 * d2(old[a], old[b])]
    if not bad:
        survivors.append(O2)
    for pr in bad:
        detecting[pr] = detecting.get(pr, 0) + 1
ok(survivors == [(1, 1)], 'with all 13 dots (5 original + 8 halfway), exactly the center survives on the grid')
print('   pairs that ever exceed stretch 2 (pair: number of grid positions caught):')
for pr, n in sorted(detecting.items(), key=lambda kv: -kv[1]):
    print(f'     {pr}: {n}')

# disk argument
disk_only = [O2 for O2 in grid if (O2[0] - 1) ** 2 + O2[1] ** 2 <= 1 and (O2[0] - 1) ** 2 + (O2[1] - 2) ** 2 <= 1]
ok(disk_only == [(1, 1)], 'O-M and O-N tests alone: (u-1)^2+v^2<=1 and (u-1)^2+(v-2)^2<=1 only at (1,1)')

# halfway-only pairs (a child who pairs two halfway dots only)
hw_surv = []
for O2 in grid:
    old, new = dots(O2)
    keys = [k for k in old if k.startswith('m')]
    if all(d2(new[a], new[b]) <= 4 * d2(old[a], old[b]) for a, b in combinations(keys, 2)):
        hw_surv.append(O2)
print(f'   (info) positions surviving pairs of halfway dots only: {len(hw_surv)} of {len(grid)}')

# measurement claim: O' a quarter unit sideways
u, v = 1.25, 1.0
exc_units = sqrt((u - 1) ** 2 + v ** 2) - 1.0
exc_mm = exc_units * 0.94 * 25.4
ok(abs(exc_mm - 0.735) < 0.001, f'quarter-unit sideways O\'=(1.25,1): midpoint excess {exc_mm:.4f} mm (guide: about 0.735 mm)')
old, new = dots((Fr(5, 4), Fr(1)))
best = max(sqrt(d2(new[a], new[b])) - 2 * sqrt(d2(old[a], old[b])) for a, b in combinations(old, 2))
print(f'   (info) best excess over all 78 dot pairs at (1.25,1): {best * 0.94 * 25.4:.4f} mm')
for O2 in [(1, 1.25), (1.25, 1.25)]:
    e = max(sqrt((O2[0] - 1) ** 2 + O2[1] ** 2), sqrt((O2[0] - 1) ** 2 + (O2[1] - 2) ** 2)) - 1
    print(f'   (info) O\'={O2}: midpoint excess {e * 0.94 * 25.4:.2f} mm')

# example triangle on p.2: old P(0,0) Q(2,0) R(0,1.3); new P(4.2,0) Q(6.2,0) R(5.1,1.3)
P, Q, R = (Fr(0), Fr(0)), (Fr(2), Fr(0)), (Fr(0), Fr(13, 10))
P2, Q2, R2 = (Fr(42, 10), Fr(0)), (Fr(62, 10), Fr(0)), (Fr(51, 10), Fr(13, 10))
ok(mid(P, Q) == (1, 0) and mid(P, R) == (0, Fr(13, 20)), 'p.2 example old M, N at source coordinates (1,0), (0,.65)')
ok(mid(P2, Q2) == (Fr(52, 10), 0) and mid(P2, R2) == (Fr(465, 100), Fr(65, 100)),
   'p.2 example new M, N at source coordinates (5.2,0), (4.65,.65)')

# ---------------------------------------------------------------- pages 3-4
print('\n== Problems 3-4 (whole-sheet rule F and lower bound) ==')
random.seed(73)
viol = 0
for _ in range(20000):
    p = Fr(random.randint(-4000, 4000), 1000)
    q = Fr(random.randint(-1000, 1000), 1000)
    if p == q == 0:
        continue
    lhs = p * p / 4 + 4 * q * q
    if lhs > 4 * (p * p + q * q) or 4 * (p * p + q * q) - lhs != Fr(15, 4) * p * p:
        viol += 1
ok(viol == 0, 'F: |dF|^2 = p^2/4 + 4q^2 and 4(p^2+q^2) - |dF|^2 = 15p^2/4 >= 0 on 20000 exact displacements')
ok([Fr(k, 2) / 2 for k in range(1, 8)] == [Fr(k, 4) for k in range(1, 8)] and Fr(1, 2) * 2 == 1,
   'F sends dotted lines x=k/2 to x=k/4 (k=1..7) and y=1/2 to y=1')
# vertical pair lower bound: (x,0) and (x,1) have old distance 1; images on y=0 and y=2
ok(True, 'lower bound: (x,0),(x,1) old distance 1; images on lines y=0 and y=2 so new distance >= 2 (argument)')
# non-uniqueness of optimal maps: (a(x), 2y) with a(x)=x on [0,1], 1+(x-1)/3 on [1,4]
pieces = [(Fr(1), 0, 0, Fr(2)), (Fr(1, 3), 0, 0, Fr(2))]
ok(all(opnorm2(M)[1] for M in pieces), 'a different optimal rule exists: (a(x),2y), a piecewise slopes 1 and 1/3 (guide says "one valid rule": right)')

print('\n== Problems 5-6 (other targets) ==')


def optimum(W, H):
    return max(Fr(W) / 4, Fr(H))


def diag_norm_ok(W, H):
    L = optimum(W, H)
    M = (Fr(W) / 4, 0, 0, Fr(H))
    a, b, c, d = M
    return max(a * a, d * d) == L * L


for (W, H), want in [((6, 2), 2), ((2, 3), 3), ((6, 1), Fr(3, 2)), ((3, Fr(3, 2)), Fr(3, 2)), ((2, 2), 2)]:
    ok(optimum(W, H) == want and diag_norm_ok(W, H),
       f'target {W} by {H}: lower bounds W/4={Fr(W)/4}, H={H}; diagonal map attains -> optimum {want}')
ok(optimum(4, 1) == 1, 'the 4-by-1 sheet itself has optimum 1, so it is not a Problem 6 answer')
q = Fr(1, 4)
found = [(i * q, j * q) for i in range(1, 41) for j in range(1, 41) if optimum(i * q, j * q) == Fr(3, 2)]
pred = [(W, H) for W, H in ((i * q, j * q) for i in range(1, 41) for j in range(1, 41))
        if W <= 6 and H <= Fr(3, 2) and (W == 6 or H == Fr(3, 2))]
ok(found == pred, f'quarter-unit grid W,H<=10: optimum 1.5 exactly on {len(found)} targets = "W<=6, H<=1.5, one equality"')
ok(Fr(6) * Fr(1, 4) == Fr(3, 2) and Fr(3) * Fr(1, 4) == Fr(3, 4),
   'guide rules (3x/2, y) for 6 by 1 and (3x/4, 3y/2) for 3 by 1.5 have the stated factors')

print(f'\n{checks} checks, {fails} failures')
