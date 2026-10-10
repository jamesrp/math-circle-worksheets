#!/usr/bin/env python3
"""Independent check of the Week 21 bonus companion (W21-BON-v1) and its adult guide.

1. Reads the boards back out of the delivered PDF (grid unit, walls, windows,
   rectangle, dots) and converts them to grid units.
2. P1/P2: brute-force search over both contact points (coarse grid, then a local
   refinement) for each contact order, compared with the double-reflection answer.
3. P3: scan both closed windows; exact comparison of the two window winners.
4. P4/P5: enumerate every corner sequence (up to all four corners, any order),
   keep the legal ones (no segment meets the open interior; exact Liang-Barsky
   test in fractions), and list the shortest lengths and ties.
5. Guide extras: the practice visual, the height formula for contact orders,
   and the mid-height tie rule for rectangles (checked on a family of heights).
Output: check_bonus.out
"""
import math, itertools
from fractions import Fraction as F
import pdfplumber
from common import WEEK, HERE

out = []
def say(*a):
    s = ' '.join(str(x) for x in a); out.append(s); print(s)

pdf = pdfplumber.open(WEEK / 'week-21-bonus.pdf')
U = 72 / 25.4 * 20  # 20 mm grid unit in pt

def grid(page):
    g = [l for l in page.lines if l.get('linewidth', 0) <= 0.5]
    xs = sorted({round(l['x0'], 2) for l in g if abs(l['x0'] - l['x1']) < 0.01})
    ys = sorted({round(792 - l['top'], 2) for l in g if abs(l['top'] - l['bottom']) < 0.01 and l['x1'] - l['x0'] > 400})
    # the board grid: 9 equally spaced vertical lines; horizontal ones spaced by the same step
    step = (xs[-1] - xs[0]) / 8
    run = [y for y in ys if any(abs(y - (ys[k] + step * j)) < 0.05 for k in range(len(ys)) for j in range(9))]
    y0 = min(y for y in ys if sum(1 for j in range(9) if any(abs(z - (y + step * j)) < 0.05 for z in ys)) == 9)
    return xs[0], y0, step

def tog(page, x, y):
    x0, y0, s = grid(page)
    return (round((x - x0) / s, 3), round((y - y0) / s, 3))

for i, page in enumerate(pdf.pages):
    x0, y0, s = grid(page)
    say(f'bonus p{i+1}: grid step {s:.3f} pt = {s / 72 * 25.4:.2f} mm, board {8 * s / 72 * 25.4:.1f} mm wide; lower-left at ({x0},{y0}) pt')
    dots = [((c['x0'] + c['x1']) / 2, 792 - (c['top'] + c['bottom']) / 2) for c in page.curves if c['x1'] - c['x0'] < 8]
    big = [d for d in dots if d[1] < 600 or i > 0]
    say('   dots (grid units): ' + ', '.join(str(tog(page, *d)) for d in big))
    for l in page.lines:
        if l.get('linewidth', 0) > 0.5:
            a = tog(page, l['x0'], 792 - l['top']); b = tog(page, l['x1'], 792 - l['bottom'])
            say(f'   heavy line {a} - {b} width {l["linewidth"]:.2f}')
    for r in page.rects:
        if r.get('non_stroking_color') not in [(1.0,), 1.0, [1.0], (1,)] and r['x1'] - r['x0'] > 100:
            say(f'   rectangle {tog(page, r["x0"], 792 - r["bottom"])} to {tog(page, r["x1"], 792 - r["top"])}')
    thin = [l for l in page.lines if l.get('linewidth', 0) <= 0.5 and abs(l['top'] - l['bottom']) < 0.01 and l['x1'] - l['x0'] > 400]

# ---------------- P1 / P2
A = (F(1), F(3)); B = (F(7), F(5)); LO, UP = F(1), F(7)
def L2(m, n, order):
    """length of A -> (m, wall1) -> (n, wall2) -> B"""
    w1, w2 = (LO, UP) if order == 'LU' else (UP, LO)
    p1 = (m, w1); p2 = (n, w2)
    return math.dist(A, p1) + math.dist(p1, p2) + math.dist(p2, B)

def brute(order):
    best = None
    N = 400
    for i in range(N + 1):
        m = 8 * i / N
        for j in range(N + 1):
            n = 8 * j / N
            v = L2(m, n, order)
            if best is None or v < best[0]:
                best = (v, m, n)
    # local refinement
    v, m, n = best; h = 8 / N
    for _ in range(40):
        cand = [(L2(m + dm, n + dn, order), m + dm, n + dn) for dm in (-h, 0, h) for dn in (-h, 0, h) if 0 <= m + dm <= 8 and 0 <= n + dn <= 8]
        v, m, n = min(cand); h /= 2
    return v, m, n

def unfold(order):
    w1, w2 = (LO, UP) if order == 'LU' else (UP, LO)
    b1 = (B[0], 2 * w2 - B[1])          # reflect finish across the last wall
    b2 = (b1[0], 2 * w1 - b1[1])        # then across the first
    w2c = 2 * w1 - w2                   # copy of the second wall
    def cross(y):
        t = (y - A[1]) / (b2[1] - A[1]); return A[0] + t * (b2[0] - A[0])
    m = cross(w1); n = cross(w2c)
    return b1, b2, m, n, (b2[0] - A[0]) ** 2 + (b2[1] - A[1]) ** 2

for order, name in [('LU', 'P1 lower then upper'), ('UL', 'P2 upper then lower')]:
    b1, b2, m, n, sq = unfold(order)
    bv, bm, bn = brute(order)
    say(f'{name}: images {b1}, {b2}; contacts first wall x = {m}, second wall x = {n}; min^2 = {sq} (min {math.sqrt(sq):.5f})')
    say(f'   brute force over both contacts: min {bv:.5f} at ({bm:.4f}, {bn:.4f})')
    assert abs(bv - math.sqrt(sq)) < 1e-6 and abs(bm - m) < 1e-3 and abs(bn - n) < 1e-3
    assert 0 < m < 8 and 0 < n < 8
assert unfold('LU')[4] == 136 and unfold('UL')[4] == 232
assert unfold('LU')[2:4] == (F(11, 5), F(29, 5)) and unfold('UL')[2:4] == (F(19, 7), F(37, 7))
say('   136 < 232: lower-then-upper is shorter (guide and overview agree)')
# height formula in the guide: vertical 2H + hA - hB (LU), 2H + hB - hA (UL)
H = UP - LO; hA = A[1] - LO; hB = B[1] - LO
assert unfold('LU')[1][1] - A[1] == -(2 * H + hA - hB) and unfold('UL')[1][1] - A[1] == 2 * H + hB - hA
say(f'   guide height formula: H = {H}, hA = {hA}, hB = {hB}: LU vertical {2*H+hA-hB}, UL vertical {2*H+hB-hA} (matches)')

# practice visual
Ap, Mp, Np, Bp = (F('0.4'), F(1)), (F(1), F(0)), (F(3), F(2)), (F(4), F('1.2'))
B1 = (Bp[0], 2 * 2 - Bp[1]); N2 = (Np[0], -Np[1]); B2 = (B1[0], -B1[1])
say(f'practice visual: B\' = {B1} (printed (4, 2.8)), N\' = {N2} (printed (3, -2)), B\'\' = {B2} (printed (4, -2.8))')
assert B1 == (4, F('2.8')) and N2 == (3, -2) and B2 == (4, F('-2.8'))
seg = lambda p, q: math.dist(p, q)
assert abs(seg(Ap, Mp) + seg(Mp, Np) + seg(Np, Bp) - (seg(Ap, Mp) + seg(Mp, N2) + seg(N2, B2))) < 1e-12
say('   lengths preserved; the unfolded path is bent (not a task answer), as the guide says')

# practice visual as printed: three panels drawn at 6 mm per unit, panel 2 shifted 6.5 units, panel 3 shifted (13.3, 2.1)
pg = pdf.pages[0]
pd = sorted([((c['x0'] + c['x1']) / 2, 792 - (c['top'] + c['bottom']) / 2) for c in pg.curves if c['x1'] - c['x0'] < 4 and 792 - c['bottom'] > 600])
u6 = 72 / 25.4 * 6
a0 = min(pd)  # panel 1 A at local (0.4, 1)
ox, oy = a0[0] - 0.4 * u6, a0[1] - u6
local = [(round((x - ox) / u6, 2), round((y - oy) / u6, 2)) for x, y in pd]
say('practice visual dots in panel-1 units (panel 2 adds 6.5 to x; panel 3 adds (13.3, 2.1)):', local)
want = [(0.4, 1), (1, 0), (3, 2), (4, 1.2), (6.9, 1), (7.5, 0), (9.5, 2), (10.5, 2.8), (13.7, 3.1), (14.3, 2.1), (16.3, 0.1), (17.3, -0.7)]
missing = [w for w in want if not any(abs(w[0] - l[0]) < 0.02 and abs(w[1] - l[1]) < 0.02 for l in local)]
say('   expected A, M, N, B / A, M, N, B\' / A, M, N\', B\'\' all found:', not missing, missing)
assert not missing

# ---------------- P3
def f3(x):
    return math.dist(A, (x, 1)) + math.dist((x, 1), B)
wins = [(F(1, 2), F(2)), (F(5), F(15, 2))]
res = []
for lo, hi in wins:
    best = min((f3(float(lo) + (float(hi) - float(lo)) * k / 100000), float(lo) + (float(hi) - float(lo)) * k / 100000) for k in range(100001))
    res.append(best); say(f'P3 window [{lo}, {hi}]: best contact x = {best[1]:.5f}, length {best[0]:.5f}')
say(f'   unrestricted best contact x = {float(A[0] + (B[0]-A[0]) * (A[1]-1) / ((A[1]-1) + (B[1]-1))):.5f}')
# exact: left = sqrt5 + sqrt41, right = 4 sqrt5; sqrt41 < 3 sqrt5 iff 41 < 45
assert abs(res[0][1] - 2) < 1e-9 and abs(res[1][1] - 5) < 1e-9 and 41 < 45
say(f'   left winner sqrt5+sqrt41 = {math.sqrt(5)+math.sqrt(41):.4f} < right winner 4 sqrt5 = {4*math.sqrt(5):.4f}: unique optimum (2, 1)')

# ---------------- P4 / P5
RX0, RX1, RY0, RY1 = F(2), F(6), F(2), F(5)
corners = [(RX0, RY0), (RX1, RY0), (RX1, RY1), (RX0, RY1)]
def hits_interior(p, q):
    t0, t1 = F(0), F(1)
    for (a, d, lo, hi) in [(p[0], q[0] - p[0], RX0, RX1), (p[1], q[1] - p[1], RY0, RY1)]:
        if d == 0:
            if not (lo < a < hi): return False
        else:
            ta, tb = (lo - a) / d, (hi - a) / d
            if ta > tb: ta, tb = tb, ta
            t0, t1 = max(t0, ta), min(t1, tb)
    return t0 < t1
def plen(path):
    return sum(math.dist(path[k], path[k + 1]) for k in range(len(path) - 1))
for name, y in [('P4', F(3)), ('P5', F(7, 2))]:
    a, b = (F(0), y), (F(8), y)
    legal = []
    for r in range(0, 5):
        for seq in itertools.permutations(corners, r):
            path = [a, *seq, b]
            if all(not hits_interior(path[k], path[k + 1]) for k in range(len(path) - 1)):
                legal.append((plen(path), seq))
    legal.sort(key=lambda t: t[0])
    best = legal[0][0]
    ties = [s for L, s in legal if abs(L - best) < 1e-9]
    say(f'{name} (A = {a}, B = {b}): {len(legal)} legal corner sequences; shortest {best:.5f} via {[tuple(map(str, c)) for c in ties[0]]}; number of shortest: {len(ties)}')
    for L, s in legal[:4]:
        say(f'     {L:.5f}  ' + ' '.join(f'({c[0]},{c[1]})' for c in s))
    say(f'   direct segment legal? {not hits_interior(a, b)}')
assert abs(4 + 2 * math.sqrt(5) - 8.47214) < 1e-5 and abs(4 + 2 * math.sqrt(8) - 9.65685) < 1e-5

# mid-height rule (guide P4-5 depth): endpoints at height h, both 2 units outside the rectangle
for k in range(0, 31):
    h = RY0 + (RY1 - RY0) * F(k, 30)
    lower = 4 + 2 * math.hypot(2, float(h - RY0)); upper = 4 + 2 * math.hypot(2, float(RY1 - h))
    mid = (RY0 + RY1) / 2
    assert (abs(lower - upper) < 1e-12) == (h == mid) and ((lower < upper) == (h < mid) or h == mid)
say('guide rule "tie exactly at mid-height, lower wins below, upper above" holds for 31 heights from 2 to 5')
(HERE / 'check_bonus.out').write_text('\n'.join(out) + '\n')
