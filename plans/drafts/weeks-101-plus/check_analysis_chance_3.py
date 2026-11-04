#!/usr/bin/env python3
"""Checks for the draft plans of weeks 202-208 (analysis and chance, third group).

Standard library only. Each check_week_2NN() asserts the small numbers quoted
in plans/drafts/weeks-101-plus/week-2NN-*.md. Simulations use fixed seeds.
Run: python3 plans/drafts/weeks-101-plus/check_analysis_chance_3.py
"""

import math
import random
from fractions import Fraction as F
from math import comb, isqrt


# ---------------------------------------------------------------- week 202
def check_week_202():
    # Halving: after n steps the walker has covered 1 - 1/2^n of the way.
    s = F(0)
    for n in range(1, 21):
        s += F(1, 2 ** n)
        assert s == 1 - F(1, 2 ** n)
    # A 4 m (400 cm) walk: 8 halvings leave 1.5625 cm, 9 leave under 1 cm.
    assert F(400, 2 ** 8) == F(25, 16) and F(400, 2 ** 9) < 1
    assert min(n for n in range(30) if F(400, 2 ** n) < 1) == 9
    # 1/4 + 1/16 + ... : partial sums are (1 - 1/4^n)/3, always below 1/3.
    s = F(0)
    for n in range(1, 21):
        s += F(1, 4 ** n)
        assert s == (1 - F(1, 4 ** n)) / 3 and s < F(1, 3)
    # Square picture: at each level the L-shaped band of area 3/4^n is three
    # equal squares, one shaded, so the shaded part is exactly a third of
    # everything removed so far, at every level.
    removed = F(0)
    shaded = F(0)
    for n in range(1, 15):
        band = 3 * F(1, 4 ** n)
        removed += band
        shaded += band / 3
        assert shaded * 3 == removed == 1 - F(1, 4 ** n)
    # General geometric series: partial sums (1 - r^(n+1))/(1 - r).
    for r in (F(1, 2), F(1, 3), F(1, 4), F(1, 10), F(2, 3)):
        s = sum(r ** k for k in range(31))
        assert s == (1 - r ** 31) / (1 - r)
        assert abs(float(s) - float(1 / (1 - r))) < 1e-4
    # 9/10 + 9/100 + ... = 1 (0.999... = 1) and 1/2 + 1/8 + 1/32 + ... = 2/3.
    assert sum(F(9, 10 ** k) for k in range(1, 11)) == 1 - F(1, 10 ** 10)
    s = sum(F(1, 2) * F(1, 4) ** k for k in range(20))
    assert abs(float(s) - 2 / 3) < 1e-11 and s < F(2, 3)
    # Achilles (Underground Mathematics numbers): 100 m head start, speeds
    # 100 m/min and 1 m/min. Catch-up stages 100, 1, 1/100, ... sum to
    # 10000/99 m, about 101.01 m, reached at 100/99 min, about 60.6 s.
    total = F(10000, 99)
    assert abs(float(sum(F(100, 100 ** k) for k in range(12))) - float(total)) < 1e-12
    assert abs(float(total) - 101.0101) < 1e-4
    assert abs(float(F(100, 99)) * 60 - 60.606) < 1e-3
    # Direct check: positions after t minutes meet at t = 100/99.
    t = F(100, 99)
    assert 100 * t == 100 + 1 * t
    # Contrast with the harmonic series (draft 141): the halving sum starting
    # at 1 never reaches 2, but 1 + 1/2 + 1/3 + 1/4 = 25/12 already passes 2.
    assert sum(F(1, 2 ** k) for k in range(40)) < 2
    assert sum(F(1, k) for k in range(1, 5)) == F(25, 12) > 2
    # 1/3 in binary is 0.010101...: digits from repeated doubling.
    x, bits = F(1, 3), []
    for _ in range(8):
        x *= 2
        bits.append(int(x >= 1))
        x -= int(x >= 1)
    assert bits == [0, 1, 0, 1, 0, 1, 0, 1]


# ---------------------------------------------------------------- week 203
DOTTIE = 0.7390851332151607


def presses(f, x, target, tol=5e-7, limit=10 ** 6):
    n = 0
    while abs(x - target) > tol:
        x = f(x)
        n += 1
        assert n < limit
    return n


def check_week_203():
    # Dottie number: cos p = p, and pressing cos converges from 0 or 1.
    assert abs(math.cos(DOTTIE) - DOTTIE) < 1e-15
    assert presses(math.cos, 0.0, DOTTIE) == 35
    assert presses(math.cos, 1.0, DOTTIE) == 34
    # Each press multiplies the error by about sin p = 0.6736 (|cos'(p)|),
    # so roughly 6 presses per new correct digit.
    assert abs(math.sin(DOTTIE) - 0.6736) < 1e-4
    assert 5.5 < math.log(10) / -math.log(math.sin(DOTTIE)) < 6
    # Any real start lands in [cos 1, 1], inside [0, 1], after two presses;
    # on [0, 1], |cos x - cos y| <= sin(1)|x - y| with sin 1 = 0.8415.
    rng = random.Random(203)
    for _ in range(2000):
        x = rng.uniform(-1000, 1000)
        y = math.cos(math.cos(x))
        assert math.cos(1) - 1e-12 <= y <= 1
    assert abs(math.sin(1) - 0.8415) < 1e-4
    # Square-root key: settles at 1 from 5, 100, a million or 0.01.
    assert presses(math.sqrt, 5.0, 1.0) == 22
    assert presses(math.sqrt, 100.0, 1.0) == 24
    assert presses(math.sqrt, 1e6, 1.0) == 25
    assert presses(math.sqrt, 0.01, 1.0) == 24
    # Near 1 the distance to 1 roughly halves each press (sqrt(1+s) ~ 1+s/2).
    x = 1.01
    for _ in range(5):
        y = math.sqrt(x)
        assert abs((y - 1) / (x - 1) - 0.5) < 0.003
        x = y
    # On [1, infinity) the square-root key is a contraction with factor 1/2:
    # |sqrt x - sqrt y| = |x - y| / (sqrt x + sqrt y) <= |x - y| / 2.
    for _ in range(2000):
        a, b = rng.uniform(1, 1e4), rng.uniform(1, 1e4)
        assert abs(math.sqrt(a) - math.sqrt(b)) <= abs(a - b) / 2 + 1e-12
    # Golden key 1 + 1/x: 15 presses from 1 to six decimals of 1.618034.
    phi = (1 + 5 ** 0.5) / 2
    assert presses(lambda x: 1 + 1 / x, 1.0, phi) == 15
    # Keys that do not settle: 1/x swaps 2 and 1/2; x*x from 1.1 runs away
    # and from 0.9 falls to 0, so its fixed point 1 repels.
    assert 1 / (1 / 2.0) == 2.0
    x = 1.1
    for _ in range(6):
        x = x * x
    assert x > 400
    x = 0.9
    for _ in range(6):
        x = x * x
    assert x < 0.002
    # Sine key creeps to 0 slowly: after n presses from 1, about sqrt(3/n).
    x = 1.0
    for k in range(1, 1001):
        x = math.sin(x)
        if k in (100, 1000):
            assert abs(x / math.sqrt(3 / k) - 1) < 0.03
    # Averaging a guess (Heron): x -> (x + 2/x)/2 from 1 gives 3/2, 17/12,
    # 577/408, 665857/470832; errors 0.086, 0.0025, 2.1e-6, 1.6e-12,
    # so correct decimals roughly double (0, 2, 5, 11).
    x = F(1)
    seq = []
    for _ in range(4):
        x = (x + 2 / x) / 2
        seq.append(x)
    assert seq == [F(3, 2), F(17, 12), F(577, 408), F(665857, 470832)]
    errs = [float(v) - 2 ** 0.5 for v in seq]
    assert abs(errs[0] - 0.0858) < 1e-4 and abs(errs[1] - 0.00245) < 1e-5
    assert 2.0e-6 < errs[2] < 2.2e-6 and 1.5e-12 < errs[3] < 1.7e-12
    assert all(e > 0 for e in errs)
    # Error rule: e_new = e^2 / (2x) exactly, the reason digits double.
    r2 = 2 ** 0.5
    for v in seq[:3]:
        e = float(v) - r2
        e_next = float((v + 2 / v) / 2) - r2
        assert abs(e_next - e * e / (2 * float(v))) < 1e-15
    # Physical K-1 rule (Tanton's alternating folds): on a 90 cm ribbon,
    # "halfway to the left end" then "halfway to the right end" settles into
    # the 30 cm and 60 cm marks from any start.
    for start in (0.0, 13.0, 45.0, 77.0, 90.0):
        x = start
        for _ in range(30):
            x = x / 2          # fold left end to the clip
            left = x
            x = (x + 90) / 2   # fold right end to the clip
        assert abs(left - 30) < 1e-6 and abs(x - 60) < 1e-6
    # The two-fold round is x -> x/4 + 45: a contraction by 1/4 with fixed 60.
    x = 0.0
    gaps = []
    for _ in range(5):
        gaps.append(60 - x)
        x = x / 4 + 45
    assert gaps == [60.0, 15.0, 3.75, 0.9375, 0.234375]


# ---------------------------------------------------------------- week 204
G = 9.81


def t_straight(D, H):
    L = math.hypot(D, H)
    return math.sqrt(2 * L * L / (G * H))


def cycloid_params(D, H):
    """Cycloid x = a(t - sin t), y = a(1 - cos t) (y measured down) through
    (0, 0) and (D, H): solve (t - sin t)/(1 - cos t) = D/H by bisection."""
    lo, hi = 1e-9, 2 * math.pi - 1e-9
    for _ in range(200):
        mid = (lo + hi) / 2
        if (mid - math.sin(mid)) / (1 - math.cos(mid)) > D / H:
            hi = mid
        else:
            lo = mid
    t = (lo + hi) / 2
    return H / (1 - math.cos(t)), t


def t_cycloid(D, H):
    a, t = cycloid_params(D, H)
    return t * math.sqrt(a / G)


def t_arc(D, H, N=100000):
    """Circle arc from (0, 0) to (D, H), horizontal at the finish: centre
    (D, H - R) with R = (D^2 + H^2)/(2H). Time = integral of ds/sqrt(2 g y);
    the substitution b = b0 (1 - u^2) removes the start singularity."""
    R = (D * D + H * H) / (2 * H)
    b0 = math.asin(D / R) if H <= R else None
    assert b0 is not None
    tot = 0.0
    for i in range(N):
        u = (i + 0.5) / N
        b = b0 * (1 - u * u)
        db = b0 * 2 * u / N
        y = H - 2 * R * math.sin(b / 2) ** 2
        tot += R * db / math.sqrt(2 * G * y)
    return tot


def t_cycloid_from(a, t0, N=100000):
    """Time from rest at parameter t0 to the bottom t = pi of the cycloid."""
    tot = 0.0
    for i in range(N):
        u = (i + 0.5) / N
        t = t0 + (math.pi - t0) * u * u
        dt = (math.pi - t0) * 2 * u / N
        ds = 2 * a * math.sin(t / 2) * dt
        dy = 2 * a * math.sin((t + t0) / 2) * math.sin((t - t0) / 2)
        tot += ds / math.sqrt(2 * G * dy)
    return tot


def check_week_204():
    # Classroom race A: drop 30 cm over 47.1 cm (= pi/2 x 30), where the
    # cycloid reaches the finish at its lowest point (a = 15 cm).
    D, H = math.pi / 2 * 0.3, 0.3
    a, t = cycloid_params(D, H)
    assert abs(a - 0.15) < 1e-9 and abs(t - math.pi) < 1e-9
    ts, tc, ta = t_straight(D, H), t_cycloid(D, H), t_arc(D, H)
    assert abs(ts - 0.4605) < 1e-4
    assert abs(tc - 0.3885) < 1e-4
    assert abs(ta - 0.3931) < 1e-4
    assert tc < ta < ts
    assert abs(tc - math.pi * math.sqrt(0.15 / G)) < 1e-9
    # Closed forms: straight sqrt(pi^2 + 4) sqrt(a/g), cycloid pi sqrt(a/g).
    assert abs(ts - math.sqrt(math.pi ** 2 + 4) * math.sqrt(a / G)) < 1e-9
    assert abs(ts / tc - 1.1854) < 1e-4
    # Galileo's square case, D = H = 30 cm: quarter circle vs cycloid.
    ts2, ta2, tc2 = t_straight(0.3, 0.3), t_arc(0.3, 0.3), t_cycloid(0.3, 0.3)
    assert abs(ts2 - 0.3497) < 1e-4 and abs(ta2 - 0.3242) < 1e-4
    assert abs(tc2 - 0.3193) < 1e-4 and tc2 < ta2 < ts2
    # Long shallow race, 1 m across, 30 cm drop: the cycloid dips about
    # 9.7 cm below the finish and still wins clearly.
    ts3, ta3, tc3 = t_straight(1.0, 0.3), t_arc(1.0, 0.3), t_cycloid(1.0, 0.3)
    a3, t3 = cycloid_params(1.0, 0.3)
    assert t3 > math.pi and abs(2 * a3 - 0.3 - 0.097) < 0.001
    assert abs(ts3 - 0.861) < 1e-3 and abs(ta3 - 0.691) < 1e-3
    assert abs(tc3 - 0.594) < 1e-3
    # Tautochrone: from rest anywhere on the cycloid, the time to the bottom
    # is the same, pi sqrt(a/g) (0.3885 s for a = 15 cm).
    target = math.pi * math.sqrt(0.15 / G)
    for t0 in (0.0, 0.5, 1.5, 2.5, 3.0):
        assert abs(t_cycloid_from(0.15, t0) - target) < 1e-7
    # Straight ramps from the same start to the same floor: time grows with
    # length, so a steeper ramp to a nearer point arrives sooner.
    assert t_straight(0.2, 0.3) < t_straight(0.47, 0.3) < t_straight(1.0, 0.3)
    # A rolling solid ball has v^2 = (10/7) g y, which stretches every time
    # by sqrt(7/5), about 1.183, so the ranking is unchanged.
    assert abs(math.sqrt(7 / 5) - 1.1832) < 1e-4


# ---------------------------------------------------------------- week 205
def grid_cells(r):
    """Unit cells of a grid centred on a circle of radius r: count cells
    wholly inside and cells meeting the open disc."""
    inner = outer = 0
    for i in range(-r, r):
        for j in range(-r, r):
            far = max(i * i, (i + 1) ** 2) + max(j * j, (j + 1) ** 2)
            nx = 0 if i <= 0 <= i + 1 else min(abs(i), abs(i + 1))
            ny = 0 if j <= 0 <= j + 1 else min(abs(j), abs(j + 1))
            if far <= r * r:
                inner += 1
            if nx * nx + ny * ny < r * r:
                outer += 1
    return inner, outer


def check_week_205():
    # Archimedes' doubling from the hexagon: perimeter / diameter for
    # inscribed (n sin(pi/n)) and circumscribed (n tan(pi/n)) n-gons.
    table = {6: (3.0000, 3.4641), 12: (3.1058, 3.2154), 24: (3.1326, 3.1597),
             48: (3.1394, 3.1461), 96: (3.1410, 3.1427)}
    for n, (lo, hi) in table.items():
        assert abs(n * math.sin(math.pi / n) - lo) < 1e-4
        assert abs(n * math.tan(math.pi / n) - hi) < 1e-4
        assert n * math.sin(math.pi / n) < math.pi < n * math.tan(math.pi / n)
    # 223/71 < inner 96-gon < pi < outer 96-gon < 22/7.
    assert 223 / 71 < 96 * math.sin(math.pi / 96)
    assert 96 * math.tan(math.pi / 96) < 22 / 7
    assert abs(223 / 71 - 3.140845) < 1e-6 and abs(22 / 7 - 3.142857) < 1e-6
    # Doubling the sides cuts the gap between the bounds by about 4.
    gaps = [n * (math.tan(math.pi / n) - math.sin(math.pi / n)) for n in (6, 12, 24, 48, 96)]
    for g1, g2 in zip(gaps, gaps[1:]):
        assert 4.0 < g1 / g2 < 4.25
    # Archimedes' rational bounds for sqrt 3: 265/153 < sqrt 3 < 1351/780.
    assert F(265, 153) ** 2 < 3 < F(1351, 780) ** 2
    # Hexagon: perimeter exactly 3 diameters, so the circle is longer than 3.
    # Wedges: m wedges rearranged give an area between the inscribed m-gon's
    # (m/2) r^2 sin(2 pi/m) and pi r^2: 2.83, 3.06, 3.12, 3.14 r^2 for m = 8..64.
    for m, v in ((8, 2.8284), (16, 3.0615), (32, 3.1214), (64, 3.1365)):
        assert abs(m / 2 * math.sin(2 * math.pi / m) - v) < 1e-4
    # The rearranged strip: base half the circumference (pi r), height r.
    # Squares on a 1 cm grid in a 10 cm circle: 276 wholly inside, 344 touched,
    # with 100 pi = 314.16 between; radius 5: 60 and 88 around 78.54.
    assert grid_cells(10) == (276, 344) and 276 < 100 * math.pi < 344
    assert grid_cells(5) == (60, 88) and 60 < 25 * math.pi < 88
    # String measurement: a 10 cm can has circumference 31.4 cm; a 1 mm
    # error in the diameter of a 7 cm lid moves the ratio by about 1.4%.
    assert abs(10 * math.pi - 31.42) < 0.01
    assert abs(0.1 / 7 - 0.0143) < 1e-4
    # Circumference also 2 pi r: string around a 15 cm plate is 47.1 cm.
    assert abs(15 * math.pi - 47.12) < 0.01


# ---------------------------------------------------------------- week 206
def euclid_quotients(a, b):
    q = []
    while b:
        q.append(a // b)
        a, b = b, a % b
    return q, a


def check_week_206():
    # Theon's side and diagonal numbers: (s, d) -> (s + d, 2s + d).
    pairs = [(1, 1)]
    for _ in range(7):
        s, d = pairs[-1]
        pairs.append((s + d, 2 * s + d))
    assert pairs[:7] == [(1, 1), (2, 3), (5, 7), (12, 17), (29, 41), (70, 99), (169, 239)]
    # d^2 - 2 s^2 alternates -1, +1, -1, ...
    assert [d * d - 2 * s * s for s, d in pairs] == [(-1) ** (k + 1) for k in range(8)]
    # So d/s is within 1/(s (d + s sqrt 2)) of sqrt 2: 17/12 is off by 0.0025,
    # 41/29 by 0.0004, 99/70 by 0.00007.
    r2 = 2 ** 0.5
    for s, d in pairs:
        assert abs(abs(d / s - r2) - 1 / (s * (d + s * r2))) < 1e-12
    assert abs(17 / 12 - r2 - 0.00245) < 1e-5
    assert abs(r2 - 41 / 29 - 0.00042) < 1e-5
    assert abs(99 / 70 - r2 - 0.0000721) < 1e-7
    # Two equal tile squares never make one square: 1+1, 4+4, ..., but the
    # side numbers come within one tile: 25+25 = 50 = 49+1, 144+144 = 289-1.
    for b in range(1, 20001):
        a = isqrt(2 * b * b)
        assert a * a != 2 * b * b
    assert 2 * 5 ** 2 == 7 ** 2 + 1 and 2 * 12 ** 2 == 17 ** 2 - 1
    assert 2 * 2 ** 2 == 3 ** 2 - 1 and 2 * 29 ** 2 == 41 ** 2 + 1
    # Tennenbaum's overlap: (a, b) -> (2b - a, a - b) flips the sign of
    # a^2 - 2b^2 and keeps its size, so an exact square pair would give a
    # smaller exact pair; it is also the folding step (17, 12) -> (7, 5).
    for b in range(1, 300):
        for a in range(b + 1, 2 * b):
            a2, b2 = 2 * b - a, a - b
            assert a2 * a2 - 2 * b2 * b2 == -(a * a - 2 * b * b)
            assert 0 < b2 < b
    chain = [(17, 12)]
    while chain[-1][1] > 0:
        a, b = chain[-1]
        chain.append((2 * b - a, a - b))
    assert chain == [(17, 12), (7, 5), (3, 2), (1, 1), (1, 0)]
    # The descent is Theon's rule run backwards.
    for s, d in pairs[1:]:
        s0, d0 = d - s, 2 * s - d
        assert (s0 + d0, 2 * s0 + d0) == (s, d)
    # Cutting biggest squares (Week 32's move): A4 (297 by 210 mm) gives
    # 1, 2, 2, 2, 2, 2 squares and ends with a 3 mm square, because 297/210
    # is a fraction; US letter (11 by 8.5 in, i.e. 22 by 17 half-inches)
    # gives 1, 3, 2, 2, so it differs at the second cut.
    assert euclid_quotients(297, 210) == ([1, 2, 2, 2, 2, 2], 3)
    assert euclid_quotients(22, 17) == ([1, 3, 2, 2], 1)
    # Leftover strips for A4: 87, 36, 15, 6, 3 mm.
    a, b, rems = 297, 210, []
    while b:
        a, b = b, a % b
        if b:
            rems.append(b)
    assert rems == [87, 36, 15, 6, 3]
    # A true 1 : sqrt 2 rectangle gives 1, 2, 2, 2, ... forever: the first
    # 30 quotients of sqrt 2 (from a 60-digit integer approximation).
    N = 10 ** 60
    q, _ = euclid_quotients(isqrt(2 * N * N), N)
    assert q[:30] == [1] + [2] * 29
    # Each round shrinks the leftover strip by sqrt 2 - 1, about 0.414.
    assert abs((r2 - 1) - 0.4142) < 1e-4
    assert abs(1 / (r2 - 1) - (r2 + 1)) < 1e-12
    # A-paper: 297/210 = 1.41429 versus sqrt 2 = 1.41421; letter is 1.294.
    assert abs(297 / 210 - 1.41429) < 1e-5 and abs(11 / 8.5 - 1.2941) < 1e-4
    # Cutting letter paper down to 1 : sqrt 2 keeps 11 in and trims the
    # width to 11/sqrt 2, about 7.78 in.
    assert abs(11 / r2 - 7.778) < 1e-3


# ---------------------------------------------------------------- week 207
def check_week_207():
    # One-coin walk on a line. u(n) = P(at 0 after 2n flips) = C(2n,n)/4^n.
    def u(n):
        return F(comb(2 * n, n), 4 ** n)
    # First return exactly at flip 2n: C(2n,n)/((2n-1) 4^n) = 1/2, 1/8,
    # 1/16, 5/128, 7/256; and P(no return by 2n) = u(n).
    f = [F(comb(2 * n, n), (2 * n - 1) * 4 ** n) for n in range(1, 40)]
    assert f[:5] == [F(1, 2), F(1, 8), F(1, 16), F(5, 128), F(7, 256)]
    for n in range(1, 40):
        assert 1 - sum(f[:n]) == u(n)
    # Back home within 20 flips: 1 - 184756/1048576, about 82%;
    # within 100 flips about 92%.
    assert 1 - u(10) == 1 - F(184756, 1048576)
    assert abs(float(1 - u(10)) - 0.8238) < 1e-4
    assert abs(float(1 - u(50)) - 0.9204) < 1e-4
    # First-return paths of length 2n: 2 x Catalan(n-1) = 2, 2, 4, 10, 28.
    assert [2 * comb(2 * n - 2, n - 1) // n for n in range(1, 6)] == [2, 2, 4, 10, 28]
    for n in range(1, 12):
        assert F(2 * comb(2 * n - 2, n - 1) // n, 2 ** (2 * n)) == f[n - 1]
    # Infinite average: the capped average E[min(T, 2N)] = 2 sum_{k<N} u(k)
    # grows like 4 sqrt(N/pi): about 7.0, 22.5, 71.4, 225.7.
    vals = {}
    s, un = 0.0, 1.0
    for k in range(10000):
        s += 2 * un
        un *= (2 * k + 1) / (2 * k + 2)
        if k + 1 in (10, 100, 1000, 10000):
            vals[k + 1] = s
    for N, v in ((10, 7.05), (100, 22.54), (1000, 71.36), (10000, 225.67)):
        assert abs(vals[N] - v) < 0.01
        assert abs(vals[N] / (4 * math.sqrt(N / math.pi)) - 1) < 0.013
    # Week 91 / AP-01 road 0..m: from s the walk reaches m first with chance
    # s/m and lasts s(m - s) flips on average (exact linear solve).
    for m in range(2, 11):
        # chance: harmonic, h(0)=0, h(m)=1 -> h(s)=s/m; duration: d(s)=1+avg.
        for s0 in range(m + 1):
            h = F(s0, m)
            d = s0 * (m - s0)
            if 0 < s0 < m:
                assert h == (F(s0 - 1, m) + F(s0 + 1, m)) / 2
                assert d == 1 + F((s0 - 1) * (m - s0 + 1) + (s0 + 1) * (m - s0 - 1), 2)
    # So after one step right, home comes before m with chance 1 - 1/m (-> 1)
    # but the trip lasts at least m - 1 flips on average (-> infinity).
    assert [1 - F(1, m) for m in (10, 100)] == [F(9, 10), F(99, 100)]
    # Two coins (diagonal grid steps): P(home at 2n) = u(n)^2, whose sum
    # diverges like log; three coins: u(n)^3, whose sum converges.
    # Three-coin (body-centred) walk returns with chance about 0.2822.
    N = 2_000_000
    s1, un = 0.0, 1.0
    for k in range(N):
        s1 += un ** 3
        un *= (2 * k + 1) / (2 * k + 2)
    s1 += 2 / (math.pi ** 1.5 * math.sqrt(N))      # tail estimate
    assert abs((1 - 1 / s1) - 0.28223) < 2e-5
    # Two-coin partial sums keep growing: about (1/pi) ln n.
    s2, un, marks = 0.0, 1.0, {}
    for k in range(1, 100001):
        s2 += un * un
        un *= (2 * k - 1) / (2 * k)
        if k in (1000, 100000):
            marks[k] = s2
    assert marks[100000] - marks[1000] > 1.4
    assert abs((marks[100000] - marks[1000]) - math.log(100) / math.pi) < 0.01
    # Simple cubic lattice (one axis per step, six choices): return chance
    # 0.3405 (MathWorld), recomputed from P(home at 2n) with a tail estimate.
    lf = [math.lgamma(i + 1) for i in range(402)]
    Gsum = 1.0
    Nn = 200
    for n in range(1, Nn + 1):
        base = lf[2 * n] - 2 * n * math.log(6)
        tot = 0.0
        for i in range(n + 1):
            for j in range(n + 1 - i):
                k = n - i - j
                tot += math.exp(base - 2 * (lf[i] + lf[j] + lf[k]))
        Gsum += tot
    Gsum += 2 * (3 / (4 * math.pi)) ** 1.5 * 2 / math.sqrt(Nn + 0.5)
    assert abs((1 - 1 / Gsum) - 0.3405) < 2e-4
    # Seeded classroom simulation: 2000 walks of 20 flips, about 82% home.
    rng = random.Random(207)
    home = 0
    for _ in range(2000):
        pos = 0
        for _ in range(20):
            pos += 1 if rng.random() < 0.5 else -1
            if pos == 0:
                home += 1
                break
    assert abs(home / 2000 - 0.8238) < 0.03


# ---------------------------------------------------------------- week 208
def p_longest_at_most(n, k, either=True):
    """P(longest run <= k) in n fair flips; either=True counts runs of the
    same face (heads or tails), else runs of heads only."""
    if either:
        c = [0] * (n + 1)
        c[0] = 1
        for m in range(1, n + 1):
            c[m] = sum(c[m - j] for j in range(1, min(k, m) + 1))
        return F(2 * c[n], 2 ** n) if k >= 1 else F(0)
    dp = [1] + [0] * k
    for _ in range(n):
        nd = [0] * (k + 1)
        nd[0] = sum(dp)
        for r in range(k):
            nd[r + 1] += dp[r]
        dp = nd
    return F(sum(dp), 2 ** n)


def run_dist(n, either):
    cdf = [p_longest_at_most(n, k, either) for k in range(n + 1)]
    pmf = [cdf[0]] + [cdf[k] - cdf[k - 1] for k in range(1, n + 1)]
    mean = sum(k * p for k, p in enumerate(pmf))
    return cdf, pmf, mean


def check_week_208():
    # 100 flips, longest run of one face (heads or tails).
    cdf, pmf, mean = run_dist(100, True)
    assert abs(float(cdf[7] - cdf[4]) - 0.657) < 1e-3     # 5 to 7
    assert abs(float(cdf[4]) - 0.0283) < 1e-4             # 4 or less
    assert abs(float(1 - cdf[5]) - 0.807) < 1e-3          # 6 or more
    assert abs(float(1 - cdf[7]) - 0.315) < 1e-3          # 8 or more
    assert abs(float(mean) - 6.98) < 0.01
    assert max(range(101), key=lambda k: pmf[k]) == 6
    assert abs(math.log2(100) - 6.64) < 0.01
    # Heads only in 100 flips: average about 6.0.
    _, _, mh = run_dist(100, False)
    assert abs(float(mh) - 5.99) < 0.01
    # Schilling (1990), 200 flips: head runs average about 7, runs of either
    # face about 8, and 4 to 10 heads contains the longest head run with
    # chance 95.3%.
    c200, _, m200 = run_dist(200, False)
    _, _, m200e = run_dist(200, True)
    assert abs(float(m200) - 6.98) < 0.01 and abs(float(m200e) - 7.98) < 0.01
    assert abs(float(c200[10] - c200[3]) - 0.953) < 1e-3
    # 20 flips (NRICH strips): a run of 4 or more of one face 77% of the
    # time, 5 or more 46%.
    c20, _, _ = run_dist(20, True)
    assert abs(float(1 - c20[3]) - 0.768) < 1e-3
    assert abs(float(1 - c20[4]) - 0.458) < 1e-3
    # 10 flips (K-1 towers): a run of 3 or more 82%, 4 or more 46%.
    c10, _, _ = run_dist(10, True)
    assert 1 - c10[2] == F(1 - F(178, 1024))
    assert abs(float(1 - c10[2]) - 0.826) < 1e-3
    assert abs(float(1 - c10[3]) - 0.465) < 1e-3
    # Switches: in 100 flips the face changes 49.5 times on average
    # (99 gaps, each a change with chance 1/2), so 50.5 runs.
    switches = sum(F(1, 2) for _ in range(99))
    assert switches == F(99, 2) and 1 + switches == F(101, 2)
    # Seeded simulation agrees with the exact 5-to-7 chance.
    rng = random.Random(208)
    hits = 0
    for _ in range(4000):
        best = cur = 1
        prev = rng.random() < 0.5
        for _ in range(99):
            x = rng.random() < 0.5
            cur = cur + 1 if x == prev else 1
            best = max(best, cur)
            prev = x
        hits += 5 <= best <= 7
    assert abs(hits / 4000 - 0.657) < 0.03


def main():
    for name in ('202', '203', '204', '205', '206', '207', '208'):
        globals()['check_week_' + name]()
        print(f'week {name}: ok')


if __name__ == '__main__':
    main()
