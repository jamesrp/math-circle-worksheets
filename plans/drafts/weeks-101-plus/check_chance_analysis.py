#!/usr/bin/env python3
"""Checks for the draft plans of weeks 130-133 and 141-142 (chance and analysis group).

Standard library only. Each check_week_1NN() asserts the small numbers quoted
in plans/drafts/weeks-101-plus/week-1NN-*.md. Simulations use fixed seeds.
Run: python3 plans/drafts/weeks-101-plus/check_chance_analysis.py
"""

import math
import random
from fractions import Fraction as F
from itertools import product


def harmonic(n):
    return sum(F(1, k) for k in range(1, n + 1))


# ---------------------------------------------------------------- week 130
def buffon_probability_numeric(L, d, steps=20000):
    """Needle of length L <= d on lines spaced d. Centre distance x to the
    nearest line is uniform on [0, d/2], angle t uniform on [0, pi/2]; the
    needle crosses when x <= (L/2) sin t. Midpoint rule over t."""
    total = 0.0
    for i in range(steps):
        t = (i + 0.5) * (math.pi / 2) / steps
        total += min(1.0, (L / 2) * math.sin(t) / (d / 2))
    return total / steps


def expected_crossings_numeric(L, d, steps=20000):
    """Any needle length: for angle t the projection across the lines is
    L sin t, and a uniformly placed interval of that length contains on
    average (L sin t)/d lines. Average over t."""
    total = 0.0
    for i in range(steps):
        t = (i + 0.5) * (math.pi / 2) / steps
        total += L * math.sin(t) / d
    return total / steps


def drop_polyline(points, d, rng):
    """Drop a rigid polyline (list of (x, y)) at a random angle and random
    vertical offset on horizontal lines y = k d. Return number of crossings."""
    a = rng.uniform(0, 2 * math.pi)
    off = rng.uniform(0, d)
    ys = [x * math.sin(a) + y * math.cos(a) + off for x, y in points]
    count = 0
    for y0, y1 in zip(ys, ys[1:]):
        lo, hi = min(y0, y1), max(y0, y1)
        count += math.floor(hi / d) - math.floor(lo / d)
    return count


def check_week_130():
    d = 1.0
    # Buffon: P = 2L/(pi d) for L <= d.
    for L in (0.25, 0.5, 1.0):
        assert abs(buffon_probability_numeric(L, d) - 2 * L / (math.pi * d)) < 1e-6
    assert abs(2 / math.pi - 0.6366) < 1e-4          # toothpick = line spacing
    assert abs(1 / math.pi - 0.3183) < 1e-4          # toothpick = half spacing
    # Barbier: expected crossings 2L/(pi d) for any length, e.g. L = 2d, 3d.
    for L in (2.0, 3.0):
        assert abs(expected_crossings_numeric(L, d) - 2 * L / (math.pi * d)) < 1e-6
    # A circle of diameter d always meets exactly one line, twice:
    # its vertical span [y - d/2, y + d/2) contains exactly one multiple of d.
    rng = random.Random(130)
    for _ in range(1000):
        y = rng.uniform(0, 10)
        lo, hi = y - d / 2, y + d / 2
        assert math.floor(hi / d) - math.floor(lo / d) == 1
    # Circle argument: 2 crossings = c * (pi d) gives c = 2/(pi d).
    # Seeded simulations: straight toothpick, bent "V" noodle, zigzag noodle,
    # all of total length d, average about 2/pi crossings.
    straight = [(0, 0), (1, 0)]
    vee = [(0, 0), (0.5, 0), (0.5, 0.5)]
    zig = [(0, 0), (0.25, 0.2), (0.5, 0)]          # two segments, then fix length
    seg = math.hypot(0.25, 0.2)
    zig = [(x / (2 * seg), y / (2 * seg)) for x, y in zig]  # total length 1
    n = 40000
    for shape in (straight, vee, zig):
        length = sum(math.dist(p, q) for p, q in zip(shape, shape[1:]))
        assert abs(length - 1.0) < 1e-12
        mean = sum(drop_polyline(shape, d, rng) for _ in range(n)) / n
        assert abs(mean - 2 / math.pi) < 0.015, mean
    # A 2d pipe cleaner on lines d apart: 4/pi = 1.27 crossings per drop.
    long_wire = [(0, 0), (1, 0), (1.6, 0.8)]           # lengths 1 and 1
    assert abs(sum(math.dist(p, q) for p, q in zip(long_wire, long_wire[1:])) - 2) < 1e-12
    mean = sum(drop_polyline(long_wire, d, rng) for _ in range(n)) / n
    assert abs(mean - 4 / math.pi) < 0.03 and abs(4 / math.pi - 1.273) < 1e-3
    # A wire of length pi d: bent into a ring of diameter d it always crosses
    # twice; dropped straight it crosses 0 to 4 times but 2 on average.
    ring_wire = [(0, 0), (math.pi, 0)]
    counts = [drop_polyline(ring_wire, d, rng) for _ in range(n)]
    assert set(counts) <= {0, 1, 2, 3, 4} and abs(sum(counts) / n - 2) < 0.03
    # Class-sized experiment: 500 drops of L = d toothpicks.
    p = 2 / math.pi
    assert round(500 * p) == 318
    sd = math.sqrt(500 * p * (1 - p))
    assert 10.7 < sd < 10.8
    # pi estimate 2 * drops / crossings at +-1 sd: about 3.04 to 3.25
    lo_est, hi_est = 2 * 500 / (500 * p + sd), 2 * 500 / (500 * p - sd)
    assert 3.03 < lo_est < 3.05 and 3.24 < hi_est < 3.26


# ---------------------------------------------------------------- week 131
def coupon_distribution(n, max_rolls):
    """Exact P(T = k) for the number of draws T to see all n equally likely kinds."""
    dist = [F(0)] * (n + 1)
    dist[0] = F(1)
    probs = {}
    for k in range(1, max_rolls + 1):
        new = [F(0)] * (n + 1)
        for seen in range(n):
            if dist[seen]:
                new[seen] += dist[seen] * F(seen, n)
                new[seen + 1] += dist[seen] * F(n - seen, n)
        new[n] = F(0)  # absorbed mass recorded below
        probs[k] = dist[n - 1] * F(1, n)
        dist = new
    return probs


def coupon_expected_unequal(ps):
    """Expected draws to see every kind, probabilities ps (inclusion-exclusion)."""
    total = F(0)
    m = len(ps)
    for mask in range(1, 2 ** m):
        sub = [ps[i] for i in range(m) if mask >> i & 1]
        total += (-1) ** (len(sub) + 1) / sum(sub)
    return total


def check_week_131():
    E6 = 6 * harmonic(6)
    assert E6 == F(147, 10)                                    # 14.7 rolls
    stages = [F(6, 6 - j) for j in range(6)]                   # 1, 6/5, 3/2, 2, 3, 6
    assert stages == [1, F(6, 5), F(3, 2), 2, 3, 6]
    running = [sum(stages[:k]) for k in range(1, 7)]
    assert [float(x) for x in running] == [1.0, 2.2, 3.7, 5.7, 8.7, 14.7]
    # The last face alone (6) takes longer on average than the first four (5.7).
    assert stages[5] > sum(stages[:4])
    # Other set sizes.
    assert 2 * harmonic(2) == 3
    assert 3 * harmonic(3) == F(11, 2)                         # 5.5
    assert 4 * harmonic(4) == F(25, 3)                         # 8.33
    assert abs(float(10 * harmonic(10)) - 29.29) < 0.01
    # Exact distribution for a die.
    probs = coupon_distribution(6, 200)
    assert probs[6] == F(720, 6 ** 6)                          # about 1.5%
    assert abs(float(probs[6]) - 0.0154) < 1e-4
    assert all(probs[k] == 0 for k in range(1, 6))
    cum, median = F(0), None
    for k in range(1, 201):
        cum += probs[k]
        if median is None and cum >= F(1, 2):
            median = k
    assert median == 13                                        # median 13 < mean 14.7
    p_le_10 = sum(probs[k] for k in range(1, 11))
    p_gt_20 = 1 - sum(probs[k] for k in range(1, 21))
    p_gt_25 = 1 - sum(probs[k] for k in range(1, 26))
    assert abs(float(p_le_10) - 0.272) < 0.001
    assert abs(float(p_gt_20) - 0.152) < 0.001
    assert abs(float(p_gt_25) - 0.062) < 0.001
    # Variance n^2 sum 1/k^2 - n H_n; sd about 6.2.
    var = 36 * sum(F(1, k * k) for k in range(1, 7)) - E6
    assert abs(float(var) - 38.99) < 0.01 and abs(math.sqrt(var) - 6.24) < 0.01
    # Seeded class experiment: average of 2000 die runs near 14.7.
    rng = random.Random(131)
    runs = []
    for _ in range(2000):
        seen, k = set(), 0
        while len(seen) < 6:
            seen.add(rng.randint(1, 6))
            k += 1
        runs.append(k)
    assert abs(sum(runs) / len(runs) - 14.7) < 0.4
    # Lopsided die stickered 1,1,2,3,4,5: five kinds, collecting is slower than
    # five equally likely kinds (a five-sided spinner).
    lop = coupon_expected_unequal([F(2, 6)] + [F(1, 6)] * 4)
    eq5 = 5 * harmonic(5)
    assert lop == F(127, 10) and eq5 == F(137, 12)             # 12.7 vs 11.42
    assert lop > eq5 and lop < E6                              # still faster than 6 kinds
    # Two-kinds-only lopsided coin (1/3, 2/3): 1/(1/3)+1/(2/3)-1 = 3.5 > 3.
    assert coupon_expected_unequal([F(1, 3), F(2, 3)]) == F(7, 2)


# ---------------------------------------------------------------- week 132
def conway(X, Y):
    """Conway correlation XY as an integer: bit i set when the suffix of X
    starting at position i equals the prefix of Y of the same length."""
    v = 0
    for i in range(len(X)):
        s = X[i:]
        v = 2 * v + (1 if len(s) <= len(Y) and Y.startswith(s) else 0)
    return v


def conway_pB(A, B):
    """Probability that B appears before A (odds B:A = (AA - AB):(BB - BA))."""
    a = conway(A, A) - conway(A, B)
    b = conway(B, B) - conway(B, A)
    return F(a, a + b)


def solve(mat, rhs):
    n = len(rhs)
    m = [row[:] + [rhs[i]] for i, row in enumerate(mat)]
    for c in range(n):
        piv = next(r for r in range(c, n) if m[r][c] != 0)
        m[c], m[piv] = m[piv], m[c]
        for r in range(n):
            if r != c and m[r][c] != 0:
                f = m[r][c] / m[c][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [m[i][n] / m[i][i] for i in range(n)]


def chain_race(A, B):
    """Exact P(B first) by a Markov chain on the last few flips (fractions)."""
    L = max(len(A), len(B))
    states = [''.join(p) for k in range(L) for p in product('HT', repeat=k)]
    idx = {s: i for i, s in enumerate(states)}
    n = len(states)
    mat = [[F(0)] * n for _ in range(n)]
    rhs = [F(0)] * n
    for s in states:
        i = idx[s]
        mat[i][i] += 1
        for c in 'HT':
            t = s + c
            if t.endswith(B):
                rhs[i] += F(1, 2)
            elif t.endswith(A):
                pass
            else:
                t = t[-(L - 1):] if L > 1 else ''
                mat[i][idx[t]] -= F(1, 2)
    return solve(mat, rhs)[idx['']]


def chain_wait(A):
    L = len(A)
    states = [''.join(p) for k in range(L) for p in product('HT', repeat=k)]
    idx = {s: i for i, s in enumerate(states)}
    n = len(states)
    mat = [[F(0)] * n for _ in range(n)]
    rhs = [F(1)] * n
    for s in states:
        i = idx[s]
        mat[i][i] += 1
        for c in 'HT':
            t = s + c
            if not t.endswith(A):
                t = t[-(L - 1):] if L > 1 else ''
                mat[i][idx[t]] -= F(1, 2)
    return solve(mat, rhs)[idx['']]


def check_week_132():
    pats3 = [''.join(p) for p in product('HT', repeat=3)]
    # Conway's leading numbers agree with an exact Markov chain on all 56 pairs.
    for A in pats3:
        for B in pats3:
            if A != B:
                assert conway_pB(A, B) == chain_race(A, B), (A, B)
    # Waiting times: 2 * AA.
    waits = {A: chain_wait(A) for A in pats3}
    for A in pats3:
        assert waits[A] == 2 * conway(A, A)
    assert waits['HHH'] == 14 and waits['HHT'] == 8 and waits['HTH'] == 10
    assert sorted(set(waits.values())) == [8, 10, 14]
    # Best replies: flip A's middle letter, put it in front, drop A's last.
    flip = {'H': 'T', 'T': 'H'}
    best = {}
    for A in pats3:
        reply = flip[A[1]] + A[:2]
        pr = conway_pB(A, reply)
        assert pr == max(conway_pB(A, B) for B in pats3 if B != A)
        assert pr > F(1, 2)
        best[A] = (reply, pr)
    assert best['HHH'] == ('THH', F(7, 8))
    assert best['HHT'] == ('THH', F(3, 4))
    assert best['HTH'] == ('HHT', F(2, 3))
    assert best['HTT'] == ('HHT', F(2, 3))
    # A cycle of four: THH > HHT > HTT > TTH > THH.
    assert conway_pB('HHT', 'THH') == F(3, 4)
    assert conway_pB('HTT', 'HHT') == F(2, 3)
    assert conway_pB('TTH', 'HTT') == F(3, 4)
    assert conway_pB('THH', 'TTH') == F(2, 3)
    # Two-flip races for K-1: TH beats HH 3/4 of the time; HT vs HH is even.
    assert conway_pB('HH', 'TH') == chain_race('HH', 'TH') == F(3, 4)
    assert conway_pB('HH', 'HT') == F(1, 2)
    assert chain_wait('HH') == 6 and chain_wait('HT') == 4
    # Length 3: the pattern with the shorter average wait never loses a race.
    for A in pats3:
        for B in pats3:
            if A != B and waits[B] > waits[A]:
                assert conway_pB(A, B) <= F(1, 2)
    # Length 4: THTH (wait 20) beats HTHH (wait 18) with chance 9/14.
    assert chain_wait('THTH') == 20 and chain_wait('HTHH') == 18
    assert conway_pB('HTHH', 'THTH') == chain_race('HTHH', 'THTH') == F(9, 14)
    # Seeded race: THH vs HHH.
    rng = random.Random(132)
    wins, n = 0, 20000
    for _ in range(n):
        s = ''
        while True:
            s = (s + rng.choice('HT'))[-3:]
            if s == 'THH':
                wins += 1
                break
            if s == 'HHH':
                break
    assert abs(wins / n - 0.875) < 0.01


# ---------------------------------------------------------------- week 133
def rate(r, b):
    return F(r, r + b)


def check_week_133():
    # Main bag set (red counters win). Pair 1: A1 = 1R; B1 = 8R 1B.
    # Pair 2: A2 = 1R 8B; B2 = 1B. Twenty counters in all.
    A1, B1, A2, B2 = (1, 0), (8, 1), (1, 8), (0, 1)
    assert rate(*A1) > rate(*B1) and rate(*A2) > rate(*B2)
    A = (A1[0] + A2[0], A1[1] + A2[1])
    B = (B1[0] + B2[0], B1[1] + B2[1])
    assert A == (2, 8) and B == (8, 2)
    assert rate(*A) == F(1, 5) and rate(*B) == F(4, 5)
    assert sum(A1 + B1 + A2 + B2) == 20
    # A gentler set for 4-5, every bag holding both colours (19 counters):
    # A1 2R1B (2/3) > B1 3R2B (3/5); A2 2R5B (2/7) > B2 1R3B (1/4);
    # merged A 4R6B (2/5) < merged B 4R5B (4/9).
    g = [(2, 1), (3, 2), (2, 5), (1, 3)]
    assert rate(*g[0]) > rate(*g[1]) and rate(*g[2]) > rate(*g[3])
    assert rate(4, 6) == F(2, 5) and rate(4, 5) == F(4, 9) and F(2, 5) < F(4, 9)
    assert sum(sum(x) for x in g) == 19
    # Exhaustive over bags of 1..5 counters each: 19 is the fewest counters for
    # a reversal with both colours in every bag.
    R = range(0, 6)
    fewest = None
    reversals = 0
    for a1r, a1b, b1r, b1b, a2r, a2b, b2r, b2b in product(R, repeat=8):
        sizes = (a1r + a1b, b1r + b1b, a2r + a2b, b2r + b2b)
        if min(sizes) == 0:
            continue
        x1, y1 = rate(a1r, a1b), rate(b1r, b1b)
        x2, y2 = rate(a2r, a2b), rate(b2r, b2b)
        mA = rate(a1r + a2r, a1b + a2b)
        mB = rate(b1r + b2r, b1b + b2b)
        # Mediant: a merged bag's chance lies between its two parts.
        assert min(x1, x2) <= mA <= max(x1, x2)
        if x1 > y1 and x2 > y2 and mA < mB:
            reversals += 1
            # Reversal needs unequal sizes: never with |A1| = |B1| and |A2| = |B2|.
            assert not (sizes[0] == sizes[1] and sizes[2] == sizes[3])
            # ... nor with the same split, |A1|/|A| = |B1|/|B|.
            assert F(sizes[0], sizes[0] + sizes[2]) != F(sizes[1], sizes[1] + sizes[3])
            if min(a1r, a1b, b1r, b1b, a2r, a2b, b2r, b2b) > 0:
                t = sum(sizes)
                fewest = t if fewest is None else min(fewest, t)
    assert reversals > 0 and fewest == 19
    # Kidney stones (Charig et al., BMJ 1986): totals 273/350 open surgery,
    # 289/350 PCNL, as read on the BMJ page. The often-quoted split by stone
    # size (not read in the paper) is consistent with those totals and reverses.
    small_open, large_open = (81, 87), (192, 263)
    small_pcnl, large_pcnl = (234, 270), (55, 80)
    assert small_open[0] + large_open[0] == 273 and small_open[1] + large_open[1] == 350
    assert small_pcnl[0] + large_pcnl[0] == 289 and small_pcnl[1] + large_pcnl[1] == 350
    assert F(*small_open) > F(*small_pcnl) and F(*large_open) > F(*large_pcnl)
    assert F(273, 350) < F(289, 350)
    assert round(100 * 273 / 350) == 78 and round(100 * 289 / 350) == 83


# ---------------------------------------------------------------- week 141
def check_week_141():
    # Harmonic stack: overhang (1/2) H_n block lengths.
    over = {n: harmonic(n) / 2 for n in range(1, 300)}
    assert over[1] == F(1, 2) and over[2] == F(3, 4) and over[3] == F(11, 12)
    assert over[4] == F(25, 24) and over[4] > 1 and over[3] < 1   # 4 blocks pass one length
    assert over[5] == F(137, 120)
    assert min(n for n in over if over[n] >= 2) == 31
    assert min(n for n in over if over[n] >= 3) == 227
    assert abs(float(harmonic(52) / 2) - 2.27) < 0.01             # a deck of cards
    # Balance check with exact fractions. Blocks have length 1; block k
    # (k = 1 at the top) has its right end at x_k; the table edge is at 0.
    # Harmonic stack: x_k = (1/2)(H_n - H_{k-1}). For each k, the centre of mass
    # of blocks 1..k sits exactly over the right end of block k+1 (or the table
    # edge for k = n): a knife-edge balance.
    for n in range(1, 12):
        x = {k: (harmonic(n) - harmonic(k - 1)) / 2 for k in range(1, n + 1)}
        for k in range(1, n + 1):
            com = sum(x[j] - F(1, 2) for j in range(1, k + 1)) / k
            support = x[k + 1] if k < n else F(0)
            assert com == support
        assert x[1] == harmonic(n) / 2
    # Three blocks, two on one level: bottom block centred on the edge
    # [-1/2, 1/2], on top [-1, 0] and [0, 1]. Each top block's centre is over
    # an end of the bottom block, and the whole stack's centre is at 0.
    # Overhang 1 > 11/12.
    bottom, left, right = F(0), F(-1, 2), F(1, 2)                 # centres
    assert (bottom + left + right) / 3 == 0
    assert right == bottom + F(1, 2) and left == bottom - F(1, 2)
    assert right + F(1, 2) == 1 and 1 > over[3]
    # Ainley's four-block optimum (cited): (15 - 4 sqrt 2)/8, about 1.16789.
    assert abs((15 - 4 * math.sqrt(2)) / 8 - 1.16789) < 1e-5
    assert (15 - 4 * math.sqrt(2)) / 8 > float(over[4])
    # Growth: (1/2) H_n - (1/2) ln n tends to gamma/2 (about 0.289).
    assert abs(float(harmonic(1000) / 2) - 0.5 * math.log(1000) - 0.2888) < 0.001
    # Oresme grouping: 1/3 + 1/4 > 1/2, 1/5 + ... + 1/8 > 1/2, etc.
    for m in range(1, 8):
        assert sum(F(1, k) for k in range(2 ** m + 1, 2 ** (m + 1) + 1)) >= F(1, 2)


# ---------------------------------------------------------------- week 142
def d2xy(order, i):
    """Standard Hilbert index-to-cell map on a 2^order grid."""
    x = y = 0
    s, t = 1, i
    n = 2 ** order
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1:
                x, y = s - 1 - x, s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


def hilbert_by_copies(order):
    """Build the order-n path from four copies of the order-(n-1) path:
    bottom-left copy reflected in the diagonal, two upper copies shifted,
    bottom-right copy reflected in the other diagonal, joined by 3 steps."""
    if order == 0:
        return [(0, 0)]
    prev = hilbert_by_copies(order - 1)
    h = 2 ** (order - 1)
    bl = [(y, x) for x, y in prev]
    tl = [(x, y + h) for x, y in prev]
    tr = [(x + h, y + h) for x, y in prev]
    br = [(2 * h - 1 - y, h - 1 - x) for x, y in prev]
    return bl + tl + tr + br


def hilbert_by_turns(order):
    """Turtle drawing from the L-system A -> +BF-AFA-FB+, B -> -AF+BFB+FA-."""
    rules = {'A': '+BF-AFA-FB+', 'B': '-AF+BFB+FA-'}
    s = 'A'
    for _ in range(order):
        s = ''.join(rules.get(c, c) for c in s)
    x, y, dx, dy = 0, 0, 1, 0
    pts = [(0, 0)]
    for c in s:
        if c == 'F':
            x, y = x + dx, y + dy
            pts.append((x, y))
        elif c == '+':
            dx, dy = -dy, dx
        elif c == '-':
            dx, dy = dy, -dx
    return pts


def normalize(pts):
    mx, my = min(p[0] for p in pts), min(p[1] for p in pts)
    return [(x - mx, y - my) for x, y in pts]


def symmetries(pts, side):
    out = []
    for sw in (False, True):
        for fx in (False, True):
            for fy in (False, True):
                q = []
                for x, y in pts:
                    if sw:
                        x, y = y, x
                    if fx:
                        x = side - 1 - x
                    if fy:
                        y = side - 1 - y
                    q.append((x, y))
                out.append(q)
    return out


def check_week_142():
    steps = {}
    for n in range(1, 7):
        side = 2 ** n
        path = [d2xy(n, i) for i in range(4 ** n)]
        assert len(set(path)) == 4 ** n                               # every cell once
        assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(path, path[1:]))
        assert path[0] == (0, 0) and path[-1] == (side - 1, 0)
        steps[n] = len(path) - 1
        # Four copies plus three bridges gives the same path.
        assert hilbert_by_copies(n) == path
        # The turning rule draws the same path up to a symmetry of the square.
        turtle = normalize(hilbert_by_turns(n))
        assert any(t == path for t in symmetries(turtle, side))
        # Nesting: the cell at step i of order n lies in the cell at step i // 4
        # of order n - 1 (each parent cell is split into its 2 x 2 children).
        if n > 1:
            for i, (x, y) in enumerate(path):
                assert (x // 2, y // 2) == d2xy(n - 1, i // 4)
    assert [steps[n] for n in (1, 2, 3)] == [3, 15, 63]
    # Path length in a unit square: (4^n - 1) / 2^n grows without bound.
    assert [F(4 ** n - 1, 2 ** n) for n in (1, 2, 3)] == [F(3, 2), F(15, 4), F(63, 8)]
    # Nearby times stay nearby: in order 5, cells k steps apart are at squared
    # distance at most 6k (a discrete form of Hoelder-1/2 continuity).
    n = 5
    path = [d2xy(n, i) for i in range(4 ** n)]
    worst_num, worst_den = 0, 1
    for i in range(len(path)):
        xi, yi = path[i]
        for j in range(i + 1, len(path)):
            xj, yj = path[j]
            d2 = (xi - xj) ** 2 + (yi - yj) ** 2
            if d2 * worst_den > worst_num * (j - i):
                worst_num, worst_den = d2, j - i
    assert F(worst_num, worst_den) == F(225, 43) and F(225, 43) <= 6
    # Nearby places need not be nearby times: on the 8 x 8 grid the two bottom
    # cells touching the middle line are visited at steps 5 and 58.
    p3 = [d2xy(3, i) for i in range(64)]
    assert p3.index((3, 0)) == 5 and p3.index((4, 0)) == 58
    # Quarters: steps 0-15 bottom-left, 16-31 top-left, 32-47 top-right,
    # 48-63 bottom-right (so the bottom-middle point lies in the first and last
    # quarters of time, the basis of the non-one-to-one argument).
    quads = [(x // 4, y // 4) for x, y in p3]
    assert quads[:16] == [(0, 0)] * 16 and quads[16:32] == [(0, 1)] * 16
    assert quads[32:48] == [(1, 1)] * 16 and quads[48:] == [(1, 0)] * 16


def main():
    for name in ('130', '131', '132', '133', '141', '142'):
        globals()['check_week_' + name]()
        print(f'week {name}: ok')


if __name__ == '__main__':
    main()
