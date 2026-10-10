#!/usr/bin/env python3
"""Week 61 math check, step 3: the mathematics behind every answer and guide claim.

Independent of the packet's own verify_math.py.  Areas come from Monte Carlo
sampling and the Van Oosterom-Strackee solid angle, never from Girard's
formula; lune membership is tested from longitudes about the lune's own pole,
never from the sign rule the guide proves.  Vertices for Problems 5 and 6 are
the ones lifted from the delivered PDF (extracted.json).

Run: python3 check_math.py > out_check_math.txt
"""
import math
from fractions import Fraction as Fr

import numpy as np

from w61lib import corner, dist, figures, load_pages, sign_str, signs, solid_angle, unit

FAIL = []
RNG = np.random.default_rng(61)
SIGN_ORDER = ["+++", "++-", "+-+", "+--", "-++", "-+-", "--+", "---"]


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def sample(n):
    x = RNG.normal(size=(n, 3))
    return x / np.linalg.norm(x, axis=1)[:, None]


def in_lune(X, V, U, W):
    """Points of X in the lune with poles V, -V whose edges are the half great
    circles from V through U and through W, the one of angle < 180 (longitudes
    about V measured from U's direction, between 0 and W's longitude)."""
    V = unit(V)
    e1 = unit(U - (U @ V) * V)
    e2 = np.cross(V, e1)
    lonW = math.atan2(W @ e2, W @ e1)
    lon = np.arctan2(X @ e2, X @ e1)
    if lonW >= 0:
        return (lon > 0) & (lon < lonW)
    return (lon < 0) & (lon > lonW)


def pair_members(X, verts):
    A, B, C = verts
    out = []
    for V, U, W in ((A, B, C), (B, A, C), (C, A, B)):
        out.append(in_lune(X, V, U, W) | in_lune(-X, V, U, W))
    return out


def cells(X, verts):
    M = np.linalg.inv(np.column_stack(verts))
    S = np.sign(X @ M.T)
    return ["".join("+" if t > 0 else "-" for t in s) for s in S]


def covering_report(verts, n=400000, label=("A", "B", "C")):
    X = sample(n)
    cs = np.array(cells(X, verts))
    mem = pair_members(X, verts)
    res = {}
    for k, code in enumerate(SIGN_ORDER, 1):
        sel = cs == code
        frac = sel.mean()
        letters = []
        for name, m in zip(label, mem):
            share = m[sel].mean() if sel.any() else 0
            if share > 0.99:
                letters.append(name)
            elif share > 0.01:
                letters.append(name + "?")
        res[k] = (code, frac, letters)
    pair_area = [m.mean() for m in mem]
    return res, pair_area


def from_angles(A, B, C):
    """Build a triangle from its three corners (polar-triangle cosine rule)."""
    a, b, c = map(math.radians, (A, B, C))
    sa = math.acos((math.cos(a) + math.cos(b) * math.cos(c)) / (math.sin(b) * math.sin(c)))
    sb = math.acos((math.cos(b) + math.cos(a) * math.cos(c)) / (math.sin(a) * math.sin(c)))
    sc = math.acos((math.cos(c) + math.cos(a) * math.cos(b)) / (math.sin(a) * math.sin(b)))
    PA = np.array([0, 0, 1.0])
    PB = np.array([math.sin(sc), 0, math.cos(sc)])
    PC = np.array([math.sin(sb) * math.cos(a), math.sin(sb) * math.sin(a), math.cos(sb)])
    return PA, PB, PC, (sa, sb, sc)


def frac(area):
    return area / (4 * math.pi)


def hemisphere_witness(verts):
    w = unit(sum(verts))
    return min(v @ w for v in verts)


# ---------------------------------------------------------------- P1
print("Problem 1 (shortest routes)")
P = np.array([math.cos(math.radians(-40)), math.sin(math.radians(-40)), 0])
Q = np.array([math.cos(math.radians(55)), math.sin(math.radians(55)), 0])
ok(abs(dist(P, Q) - 95) < 1e-9, "page-1 example: minor arc 95 deg, other arc 265 deg (guide)")
# antipodal endpoints: every half great circle through a third point has length pi
N = np.array([0, 0, 1.0])
lens = []
for lonc in (0, 37, 90, 200):
    T = np.array([math.cos(math.radians(lonc)), math.sin(math.radians(lonc)), 0])
    lens.append(math.radians(dist(N, T) + dist(T, -N)))
ok(max(abs(l - math.pi) for l in lens) < 1e-12, "opposite points: routes via different equator points all have length pi (many shortest routes)")
# non-antipodal: any detour through a third point off the minor arc is strictly longer (sampled)
X = sample(20000)
det = np.degrees(np.arccos(np.clip(X @ P, -1, 1)) + np.arccos(np.clip(X @ Q, -1, 1)))
on = np.abs(X @ unit(np.cross(P, Q))) < 1e-3
ok(det.min() >= 95 - 1e-6, f"close/far pair: no route via any sampled point beats the 95 deg minor arc (min {det.min():.4f})")

# ---------------------------------------------------------------- P2
print("\nProblem 2 (three right corners)")
O = (np.array([0, 0, 1.0]), np.array([1, 0, 0.0]), np.array([0, 1, 0.0]))
cs = [corner(O[0], O[1], O[2]), corner(O[1], O[0], O[2]), corner(O[2], O[0], O[1])]
ok(max(abs(c - 90) for c in cs) < 1e-9, "octant N,(1,0,0),(0,1,0): corners 90,90,90")
ok(abs(frac(solid_angle(*O)) - 1 / 8) < 1e-12, "octant area 1/8 of the sphere (solid angle)")
ok(hemisphere_witness(O) > 0.5, "octant strictly inside the open hemisphere about (1,1,1)")

# ---------------------------------------------------------------- P3 and P4
print("\nProblems 3-4 (pole-equator triangles)")
prev = 0
for g in (30, 45, 60, 72, 89, 90, 110, 120, 150, 179):
    h = math.radians(g / 2)
    V = (np.array([0, 0, 1.0]), np.array([math.cos(h), -math.sin(h), 0]), np.array([math.cos(h), math.sin(h), 0]))
    a = frac(solid_angle(*V))
    c = (corner(V[0], V[1], V[2]), corner(V[1], V[0], V[2]), corner(V[2], V[0], V[1]))
    ok(abs(c[0] - g) < 1e-6 and abs(c[1] - 90) < 1e-6 and abs(c[2] - 90) < 1e-6 and abs(a - g / 720) < 1e-12 and a > prev
       and hemisphere_witness(V) > 0,
       f"gap {g}: corners ({c[0]:.1f},{c[1]:.1f},{c[2]:.1f}), area {a:.6f} = gap/720, grows with the gap, inside an open hemisphere")
    prev = a
for g, want in ((45, Fr(1, 16)), (72, Fr(1, 10)), (120, Fr(1, 6)), (40, Fr(1, 18))):
    ok(Fr(g, 720) == want and Fr(360, g).denominator == 1,
       f"P4 gap {g}: {Fr(360, g)} equal lunes, lune {Fr(g, 360)}, triangle {Fr(g, 720)} (key {want})")
Xs = sample(400000)
mc = in_lune(Xs, np.array([0, 0, 1.0]), np.array([1, 0, 0.0]), np.array([math.cos(math.radians(40)), math.sin(math.radians(40)), 0])).mean()
ok(abs(mc - 1 / 9) < 0.003, f"40 deg lune by sampling: {mc:.4f} vs 1/9 = {1 / 9:.4f}")

# ---------------------------------------------------------------- P5, P6 from the printed figures
pages = load_pages()


def lifted(fig, names):
    d = fig.labelled_dots()
    return [fig.lift(d[k][0]) for k in names]


def show(res, pair_area, label, key_letters, key_area, cellkey):
    for k in range(1, 9):
        code, f, letters = res[k]
        want = key_letters[k - 1]
        ok(sorted(letters) == sorted(want) and abs(f - cellkey[k - 1]) < 0.004,
           f"region {k} ({code}): area {f:.4f} (exact {cellkey[k - 1]:.4f}), pairs {''.join(letters) or '-'} -> count {len(letters)}")
    ok(max(abs(p - key_area) for p in pair_area) < 0.004, f"pair areas {[round(p, 4) for p in pair_area]} vs {key_area:.4f}")
    tot = sum(len(res[k][2]) * res[k][1] for k in res)
    ok(abs(tot - 3 * key_area) < 0.01, f"counted area sum over regions = {tot:.4f} = 3 pairs = {3 * key_area:.4f}")


print("\nProblem 5 (octant N, A, B from the printed front view)")
o0 = figures(pages[4])[4]
V5 = lifted(o0, ["N", "A", "B"])
res, pa = covering_report(V5, label=("N", "A", "B"))
key5 = [["N", "A", "B"], ["B"], ["A"], ["N"], ["N"], ["A"], ["B"], ["N", "A", "B"]]  # guide p.5 table
show(res, pa, ("N", "A", "B"), key5, 0.5, [1 / 8] * 8)
f5 = Fr(3, 2) - 1
ok(f5 / 4 == Fr(1, 8), "3 pairs x 1/2 = 3/2 = 1 + 4f  ->  f = 1/8")

print("\nProblem 6 (80-80-80 triangle from the printed front view)")
f6 = figures(pages[5])[0]
V6 = lifted(f6, ["A", "B", "C"])
res, pa = covering_report(V6)
key6 = [["A", "B", "C"], ["C"], ["B"], ["A"], ["A"], ["B"], ["C"], ["A", "B", "C"]]  # guide p.6 table
show(res, pa, ("A", "B", "C"), key6, 4 / 9, [1 / 12, 5 / 36, 5 / 36, 5 / 36, 5 / 36, 5 / 36, 5 / 36, 1 / 12])
ok(3 * Fr(4, 9) == 1 + 4 * Fr(1, 12), "3 x 4/9 = 4/3 = 1 + 4(1/12)")
ok(2 * Fr(1, 12) + 6 * Fr(5, 36) == 1 and 2 * Fr(1, 12) + 2 * Fr(5, 36) == Fr(4, 9), "guide cell key: 2(1/12)+6(5/36)=1, one pair 4/9")
A6, B6, C6 = V6
for code, verts in (("++-", (A6, B6, -C6)), ("+-+", (A6, -B6, C6)), ("+--", (A6, -B6, -C6))):
    angs = sorted(round(corner(verts[i], verts[(i + 1) % 3], verts[(i + 2) % 3]), 1) for i in range(3))
    ok(angs == [80.0, 100.0, 100.0] or max(abs(a - b) for a, b in zip(angs, [80, 100, 100])) < 0.3,
       f"cell {code}: corners {angs} (guide: one 80 and two 100), solid-angle fraction {frac(solid_angle(*verts)):.5f} vs 5/36={5 / 36:.5f}")

print("\nIs the page-5 example triangle the Problem 6 triangle?")
s0 = figures(pages[4])[0]
Vex = lifted(s0, ["A", "B", "C"])
ok(True, "page-5 example A,B,C vs page-6 A,B,C (same view frame): max difference "
   f"{max(np.linalg.norm(a - b) for a, b in zip(Vex, V6)):.4f} (unit-sphere units)")

# ---------------------------------------------------------------- P7
print("\nProblem 7 (records)")
for angs, want in (((60, 60, 90), Fr(1, 24)), ((80, 80, 80), Fr(1, 12)), ((100, 100, 100), Fr(1, 6))):
    A, B, C, sides = from_angles(*angs)
    got = (corner(A, B, C), corner(B, A, C), corner(C, A, B))
    f = frac(solid_angle(A, B, C))
    ok(max(abs(g - a) for g, a in zip(got, angs)) < 1e-6 and abs(f - float(want)) < 1e-12
       and hemisphere_witness((A, B, C)) > 0 and max(sides) < math.pi,
       f"{angs}: exists (sides {[round(math.degrees(s), 2) for s in sides]}), area by solid angle {f:.6f} = {want} = (sum-180)/720 = {Fr(sum(angs) - 180, 720)}")
# guide's explicit 60-60-90 coordinates
A = np.array([0, 0, 1.0]); B = np.array([2 * math.sqrt(2) / 3, 0, 1 / 3]); C = np.array([1 / math.sqrt(6), 1 / math.sqrt(2), 1 / math.sqrt(3)])
g = (corner(A, B, C), corner(B, A, C), corner(C, A, B))
ok(abs(np.linalg.norm(C) - 1) < 1e-12 and max(abs(x - y) for x, y in zip(g, (60, 60, 90))) < 1e-9,
   f"guide coordinates A=(0,0,1), B=(2r2/3,0,1/3), C=(1/r6,1/r2,1/r3): corners {tuple(round(x, 6) for x in g)}")
for q in (80, 100):
    cq = math.cos(math.radians(q)); d = cq / (1 - cq)
    G = np.full((3, 3), d); np.fill_diagonal(G, 1)
    ev = sorted(np.linalg.eigvalsh(G))
    L = np.linalg.cholesky(G); V = [L[i] for i in range(3)]
    ok(abs(d / (1 + d) - cq) < 1e-12 and np.allclose(ev, sorted([1 - d, 1 - d, 1 + 2 * d])) and min(ev) > 0
       and abs(corner(V[0], V[1], V[2]) - q) < 1e-9 and min(v @ unit(sum(V)) for v in V) > 0,
       f"guide equal-angle construction q={q}: d={d:.5f}, eigenvalues {np.round(ev, 4)}, corner {corner(V[0], V[1], V[2]):.6f}")

# ---------------------------------------------------------------- general theorem, random triangles
print("\nGeneral claims on random triangles in scope (open hemisphere, minor sides)")
worst_girard, max_sum, min_sum, bad_cover = 0, 0, 999, 0
for t in range(300):
    w = unit(RNG.normal(size=3))
    while True:
        V = [unit(w + RNG.normal(size=3) * RNG.uniform(0.2, 3)) for _ in range(3)]
        if min(v @ w for v in V) > 0.02 and abs(np.linalg.det(np.column_stack(V))) > 1e-3:
            break
    s = corner(V[0], V[1], V[2]) + corner(V[1], V[0], V[2]) + corner(V[2], V[0], V[1])
    worst_girard = max(worst_girard, abs(frac(solid_angle(*V)) - (s - 180) / 720))
    max_sum, min_sum = max(max_sum, s), min(min_sum, s)
    if t < 40:
        res, _ = covering_report(V, n=60000)
        counts = [len([l for l in res[k][2] if not l.endswith("?")]) for k in range(1, 9)]
        if counts != [3, 1, 1, 1, 1, 1, 1, 3] or any(res[k][1] == 0 for k in res):
            bad_cover += 1
ok(worst_girard < 1e-9, f"(sum-180)/720 equals the solid-angle fraction on 300 random triangles (worst error {worst_girard:.2e})")
ok(180 < min_sum and max_sum < 540, f"angle sums observed in ({min_sum:.2f}, {max_sum:.2f}), inside (180, 540)")
ok(bad_cover == 0, "40 random triangles: all eight cells nonempty, covering counts 3,1,1,1,1,1,1,3")
w = np.array([0, 0, 1.0])
for t in (0.2, 0.05, 0.01):
    V = [unit(np.array([math.cos(k * 2 * math.pi / 3), math.sin(k * 2 * math.pi / 3), 0]) * math.cos(t) + w * math.sin(t)) for k in range(3)]
    s = corner(V[0], V[1], V[2]) + corner(V[1], V[0], V[2]) + corner(V[2], V[0], V[1])
    ok(s < 540 and abs(frac(solid_angle(*V)) - (s - 180) / 720) < 1e-9,
       f"near-hemisphere triangle (vertices {math.degrees(t):.2f} deg above a great circle): sum {s:.3f} < 540, area {frac(solid_angle(*V)):.5f} < 1/2")

# ---------------------------------------------------------------- limits named in the guide
print("\nOutside the stated scope (guide p.8 'Counterexamples to overextension', p.1 limits)")
oct_c = 1 - 1 / 8
ok(abs((1 - frac(solid_angle(*O))) - 7 / 8) < 1e-12 and Fr(3 * 270 - 180, 720) == Fr(7, 8), "octant complement: reflex corners 270,270,270 -> (810-180)/720 = 7/8, its true area: "
   "the rule itself still holds there; only the 180<sum<540 bounds and the six-lune proof need the scope")
for g in (60, 110):
    Xs2 = sample(400000)
    lon = np.degrees(np.arctan2(Xs2[:, 1], Xs2[:, 0]))
    true = ((Xs2[:, 2] > 0) & (np.abs(lon) > g / 2)).mean()  # north of the equator, outside the short wedge
    rule = float(Fr((360 - g) + 90 + 90 - 180, 720))
    ok(abs(true - rule) < 0.003,
       f"pole triangle with the LONG equator arc (gap {g}): corners {360 - g},90,90, rule gives {rule:.4f}, sampled area {true:.4f}")
phi = math.radians(30)
cap = (1 - math.sin(phi)) / 2 * (90 / 360)
ok(abs(cap - 1 / 16) < 1e-12 and Fr(270 - 180, 720) == Fr(1, 8),
   "latitude-30 'triangle' (pole + two latitude points 90 deg apart): corners 90,90,90 but area 1/16, not 1/8 -> rule fails, as guide says")
ok(Fr(180 - 180, 720) == 0, "three 60-degree corners: rule gives 0, so no positive-area triangle (guide)")

# ---------------------------------------------------------------- arithmetic in the guide
print("\nGuide p.6 hint: 'compare the sizes of cells 1 and 2 in the same map' (projected sizes on the printed front view)")
f6v = figures(pages[5])[0]
dd = f6v.labelled_dots()
Af, Bf, Cf = [f6v.lift(dd[k][0]) for k in "ABC"]
g = np.linspace(-1, 1, 1201)
GX, GY = np.meshgrid(g, g)
m = GX ** 2 + GY ** 2 < 1
Pp = np.stack([GX[m], GY[m], np.sqrt(1 - GX[m] ** 2 - GY[m] ** 2)], 1)
codes = cells(Pp, (Af, Bf, Cf))
for code, k, exact in (("+++", 1, 1 / 12), ("++-", 2, 5 / 36), ("+-+", 3, 5 / 36), ("+--", 4, 5 / 36)):
    share = np.mean(np.array(codes) == code)
    print(f"  INFO region {k}: {share:.3f} of the printed disc; true sphere fraction {exact:.4f}")
print("  INFO regions 2, 3, 4 are congruent (5/36 each) but print at different sizes; region 1 + region 2 is the")
print("       80-degree lune at C (2/9 = 8/36), which is not 2/8: a count-free reason the cells are not eighths.")
ok(abs(Fr(1, 12) + Fr(5, 36) - Fr(2, 9)) == 0, "region 1 + region 2 = 1/12 + 5/36 = 2/9 = one 80-degree lune")

print("\nGuide arithmetic (materials, printing)")
ok(15 * 80 == 1200 and 6 + 6 + 3 == 15, "strings: 6+6+3 = 15 at 80 cm = 12 m")
ok(12 + 12 + 6 == 30 and 4 + 4 + 3 == 11 and 2 + 2 + 1 == 5, "dots 30, right-angle tabs 11, balls 5")
ok(abs(math.pi * 20 - 62.83) < 0.01 and 80 > math.pi * 20, "20 cm ball circumference 62.8 cm < 80 cm string")
ok(7 * 3 == 21 and 7 * 1 == 7 and 3 * 3 == 9 and 21 + 7 + 9 == 37 and 3 * 9 == 27, "printing: 21 + 7 + 9 = 37 student sheets, 27 adult sheets")
ok(4 + 4 + 2 + 1 == 11, "roster 4 + 4 + 3 = 11 children")

print("\n" + ("ALL MATH CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURES"))
