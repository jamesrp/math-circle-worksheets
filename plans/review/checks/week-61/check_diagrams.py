#!/usr/bin/env python3
"""Week 61 math check, step 2: every student-page sphere diagram, from the PDF.

Reads extracted.json (extract.py).  Each drawn ball is an orthographic disc, so
a visible point (x, y) in the disc lifts to (x, y, +sqrt(1-x^2-y^2)) and a
dashed (back) point to the negative root.  From the lifted dots, arcs, fills
and number labels this script recomputes the actual surface angles, arc
lengths, great-circle planes, lune angles and the sign cell of every region
label, and checks back views are rotations (not mirror images) of the front.

Run: python3 check_diagrams.py > out_check_diagrams.txt
"""
import math
import sys

import numpy as np

from w61lib import (BLUE, INK, corner, dist, figures, interior_point, kabsch, load_pages, plane_fit,
                    pts_of, sign_str, signs, unit, bbox)

FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


PAGES = load_pages()
SIGN_ORDER = ["+++", "++-", "+-+", "+--", "-++", "-+-", "--+", "---"]


def one(d, k):
    v = d.get(k)
    assert v and len(v) == 1, (k, d.keys())
    return v[0]


def lift_arc(fig, path):
    return [fig.lift(p, back=path["dashed"]) for p in pts_of(path)]


def arc_length_deg(P):
    return sum(dist(a, b) for a, b in zip(P, P[1:]))


# ------------------------------------------------------------------ page 1
print("Page 1: route example (Mark P and Q -> great circle -> shorter arc)")
f0, f1, f2 = figures(PAGES[0])
for k, f in enumerate((f0, f1, f2)):
    d = f.labelled_dots()
    P, Q = f.lift(one(d, "P")), f.lift(one(d, "Q"))
    print(f"  panel {k + 1}: P={np.round(P, 4)}, Q={np.round(Q, 4)}, angular distance PQ = {dist(P, Q):.3f} deg")
    ok(abs(dist(P, Q) - 95) < 0.1, f"panel {k + 1}: P,Q are 95 deg apart (minor arc 95, major 265)")
d1 = f1.labelled_dots()
centre = one(d1, "center")
ok(max(abs(t) for t in f1.xy(centre)) < 1e-3, "panel 2: 'center' dot is the projected ball centre")
pts = [p for a in f1.arcs for p in lift_arc(f1, a)]
n, res = plane_fit(pts)
P1, Q1 = f1.lift(one(d1, "P")), f1.lift(one(d1, "Q"))
ok(res < 0.01 and abs(n @ P1) < 0.01 and abs(n @ Q1) < 0.01,
   f"panel 2: drawn circle (solid front + dashed back) is one centre plane through P and Q (residual {res:.4f})")
blue = [a for a in f2.arcs if a["stroke"] == BLUE]
ok(len(blue) == 1, "panel 3: one thick blue route")
B = lift_arc(f2, blue[0])
d2 = f2.labelled_dots()
P2, Q2 = f2.lift(one(d2, "P")), f2.lift(one(d2, "Q"))
nb, rb = plane_fit(B)
ends = sorted([dist(B[0], P2), dist(B[-1], Q2)] + [dist(B[0], Q2), dist(B[-1], P2)])[:2]
ok(rb < 0.01 and max(ends) < 1.0, f"panel 3: blue route lies on the PQ great circle and ends at P and Q")
ok(abs(arc_length_deg(B) - 95) < 1, f"panel 3: blue route length {arc_length_deg(B):.2f} deg = the shorter arc")
ok(min(f2.lift(p)[2] for p in pts_of(blue[0])) >= -1e-9 and not blue[0]["dashed"], "panel 3: blue route entirely on the visible side, drawn solid")

# ------------------------------------------------------------------ page 2
print("\nPage 2: angle convention at P")
(g,) = figures(PAGES[1])
dP = g.labelled_dots()
Pp = g.lift(one(dP, "P"))
ok(max(abs(t) for t in g.xy(one(dP, "P"))) < 1e-3, "ball panel: P at the front centre")
dirs = []
for a in g.arcs:
    L = lift_arc(g, a)
    far = max(L, key=lambda q: dist(q, Pp))
    near = sorted(L, key=lambda q: dist(q, Pp))[1]
    dirs.append(unit(near - (near @ Pp) * Pp))
    n, r = plane_fit(L + [Pp])
    ok(r < 0.01, f"ball panel: side to {np.round(far, 3)} lies in a centre plane through P (res {r:.4f})")
ang = math.degrees(math.acos(np.clip(dirs[0] @ dirs[1], -1, 1)))
ok(abs(ang - 135) < 0.5, f"ball panel: surface angle between the two sides at P = {ang:.2f} deg (record says 135)")
flat = [p for p in PAGES[1]["paths"] if p["stroke"] == BLUE and len(pts_of(p)) == 2 and bbox(p)[0] > 250 and bbox(p)[2] < 380]
vecs = []
for p in flat:
    a, b = pts_of(p)
    o = (305.3, 203.0)
    far = b if math.hypot(b[0] - o[0], b[1] - o[1]) > math.hypot(a[0] - o[0], a[1] - o[1]) else a
    near = a if far is b else b
    vecs.append(np.array([far[0] - near[0], -(far[1] - near[1])]))
fa = math.degrees(math.acos(vecs[0] @ vecs[1] / np.linalg.norm(vecs[0]) / np.linalg.norm(vecs[1])))
ok(len(vecs) == 2 and abs(fa - 135) < 0.5, f"flat 'Directions close to P' panel: angle {fa:.2f} deg")

# ------------------------------------------------------------------ page 3
print("\nPage 3: Problem 3 printed triangle")
(h,) = figures(PAGES[2])
dd = h.labelled_dots()
N, A, Bv = (h.lift(one(dd, k)) for k in ("N", "A", "B"))
cN, cA, cB = corner(N, A, Bv), corner(A, N, Bv), corner(Bv, N, A)
print(f"  N={np.round(N, 4)} A={np.round(A, 4)} B={np.round(Bv, 4)}; corners N {cN:.2f}, A {cA:.2f}, B {cB:.2f}")
ok(abs(cA - 90) < 0.5 and abs(cB - 90) < 0.5, "A and B corners are right angles (A, B on the equator of N)")
ok(abs(N @ A) < 0.01 and abs(N @ Bv) < 0.01, "A and B lie on the equator (90 deg from N)")
ok(abs(cN - 110) < 0.5, "N corner = 110 deg = equatorial gap AB (guide: 'printed example is 110')")
for a in h.arcs:
    L = lift_arc(h, a)
    n, r = plane_fit(L)
    ends = [k for k, v in (("N", N), ("A", A), ("B", Bv)) if min(dist(L[0], v), dist(L[-1], v)) < 1.5]
    ok(r < 0.01 and len(ends) == 2, f"side {''.join(ends)} is a great-circle arc (res {r:.4f}), length {arc_length_deg(L):.1f} deg")
(fill,) = h.fills
s, _ = signs(h.lift(interior_point(fill)), (N, A, Bv))
ok(sign_str(s) == "+++", f"shading is the triangle NAB itself (cell {sign_str(s)})")

# ------------------------------------------------------------------ page 4
print("\nPage 4: 40-degree lune, nine-strip view")
(lu,) = figures(PAGES[3])
dd = lu.labelled_dots()
Nl = lu.lift(one(dd, "N"))
Sdot = [p for p in lu.paths if p["fill"] == [255, 255, 255] and p["stroke"] == INK]
Sxy = ((bbox(Sdot[0])[0] + bbox(Sdot[0])[2]) / 2, (bbox(Sdot[0])[1] + bbox(Sdot[0])[3]) / 2)
Sl = lu.lift(Sxy, back=True)
ok(dist(Nl, -Sl) < 0.5, f"open dot labelled 'S (back)' is the back point opposite N (off by {dist(Nl, -Sl):.3f} deg)")
bl = sorted([a for a in lu.arcs if a["stroke"] == BLUE], key=lambda a: bbox(a)[0])
left = [a for a in bl if np.mean([q[0] for q in pts_of(a)]) < lu.cx]
right = [a for a in bl if a not in left]
tang = []
for grp in (left, right):
    L = [p for a in grp for p in lift_arc(lu, a)]
    n, r = plane_fit(L)
    ok(r < 0.01 and abs(n @ Nl) < 0.01, f"lune edge ({len(grp)} pieces, front solid/back dashed) is a meridian: centre plane through N and S, res {r:.4f}")
    near = min([q for q in L if dist(q, Nl) > 2], key=lambda q: dist(q, Nl))
    tang.append(unit(near - (near @ Nl) * Nl))
lune_ang = math.degrees(math.acos(np.clip(tang[0] @ tang[1], -1, 1)))
ok(abs(lune_ang - 40) < 0.5, f"lune angle at N = {lune_ang:.2f} deg")
eq = [p for a in lu.arcs if a["stroke"] == INK for p in lift_arc(lu, a)]
n, r = plane_fit(eq)
ok(r < 0.01 and abs(abs(n @ Nl) - 1) < 0.01, f"thin ink circle is the equator of N (res {r:.4f})")
(lf,) = lu.fills
q = lu.lift(interior_point(lf))
ok(math.degrees(math.acos(np.clip(unit(q - (q @ Nl) * Nl) @ tang[0], -1, 1))) < 40 and
   math.degrees(math.acos(np.clip(unit(q - (q @ Nl) * Nl) @ tang[1], -1, 1))) < 40, "shading lies inside the 40 deg lune")
spokes = [p for p in PAGES[3]["paths"] if len(pts_of(p)) == 2 and 250 < bbox(p)[0] < 310 and bbox(p)[3] < 215 and p["stroke"] == [111, 115, 118]]
O = (307.9, 158.4)
angs = []
for p in spokes:
    a, b = pts_of(p)
    far = max((a, b), key=lambda t: math.hypot(t[0] - O[0], t[1] - O[1]))
    angs.append(math.degrees(math.atan2(-(far[1] - O[1]), far[0] - O[0])) % 360)
angs.sort()
gaps = [(angs[(i + 1) % len(angs)] - angs[i]) % 360 for i in range(len(angs))]
ok(len(angs) == 9 and max(abs(g - 40) for g in gaps) < 0.3, f"top view: {len(angs)} spokes, gaps {[round(g, 1) for g in gaps]}")

# ------------------------------------------------------------------ pages 5-6
def side_triangle(fig, names):
    d = fig.labelled_dots()
    return {k: fig.lift(one(d, k)) for k in names if k in d}, d


print("\nPage 5: lune-pair example (80-80-80 triangle ABC)")
s0, s1, s2, s3, o0, o1 = figures(PAGES[4])
V0, _ = side_triangle(s0, "ABC")
A, B, C = V0["A"], V0["B"], V0["C"]
angs = (corner(A, B, C), corner(B, A, C), corner(C, A, B))
ok(max(abs(t - 80) for t in angs) < 0.6, f"'Corner A': corners {tuple(round(t, 2) for t in angs)}; B, C on the limb (z={B[2]:.3f},{C[2]:.3f})")
(cf,) = s0.fills
sg, _ = signs(s0.lift(interior_point(cf)), (A, B, C))
ok(sign_str(sg) == "+++", f"'Corner A' shading is triangle ABC (cell {sign_str(sg)})")
V1, d1 = side_triangle(s1, ["A", "B", "C", "B*", "C*"])
for a in s1.arcs:
    if a["stroke"] != BLUE:
        continue
    L = lift_arc(s1, a)
    n, r = plane_fit(L)
    on = [k for k, v in V1.items() if abs(n @ v) < 0.01]
    ok(r < 0.01 and sorted(on) in (["A", "B", "B*"], ["A", "C", "C*"]), f"'Circles AB and AC': blue circle through {on} (res {r:.4f})")
V2, d2 = side_triangle(s2, ["A", "B", "C", "B*", "C*"])
A2, B2, C2 = V2["A"], V2["B"], V2["C"]
got = sorted(sign_str(signs(s2.lift(interior_point(f)), (A2, B2, C2))[0]) for f in s2.fills)
ok(got == ["+++", "+--"], f"'Pair at A: front' shades cells {got} (pair at A = cells whose B and C signs agree)")
(xd,) = s2.bluedots
xs = sign_str(signs(s2.lift(s2.dot_centre(xd)), (A2, B2, C2))[0])
xlabel = min(s2.words, key=lambda w: math.hypot((w['x0'] + w['x1']) / 2 - s2.dot_centre(xd)[0], (w['y0'] + w['y1']) / 2 - s2.dot_centre(xd)[1]))["text"]
pairs_x = [v for v, (i, j) in zip("ABC", ((1, 2), (0, 2), (0, 1))) if xs[i] == xs[j]]
ok(xlabel == "X" and xs == "+--" and pairs_x == ["A"], f"patch {xlabel} is in cell {xs}: covered by pairs {pairs_x} only -> count 1, as the table says")
V3, d3 = side_triangle(s3, ["A*", "B", "C", "B*", "C*"])
src = [V3[k] for k in ("B", "C", "B*", "C*", "A*")]
dst = [B2, C2, -B2, -C2, -A2]
R, det, res = kabsch(src, dst)
ok(det > 0 and res < 0.02, f"'Same pair: back' is a rotation of the front view (det {det:+.0f}, residual {res:.4f})")
got = sorted(sign_str(signs(R @ s3.lift(interior_point(f)), (A2, B2, C2))[0]) for f in s3.fills)
ok(got == sorted(["---", "-++"]), f"'Same pair: back' shades cells {got}")


def region_check(front, back, names, title):
    Vf, _ = side_triangle(front, names + [n + "*" for n in names])
    T = [Vf[k] for k in names]
    Vb, _ = side_triangle(back, list(Vf.keys()) + [names[0] + "*"])
    common = [k for k in Vb if (k in Vf) or (k.rstrip("*") in Vf)]
    src, dst = [], []
    for k in Vb:
        base = k.rstrip("*")
        v = Vf[base] if base in Vf else None
        if v is None:
            continue
        src.append(Vb[k])
        dst.append(-v if k.endswith("*") else v)
    R, det, res = kabsch(src, dst)
    ok(det > 0 and res < 0.02, f"{title}: back view is a rotation of the front view (det {det:+.0f}, residual {res:.4f}, {len(src)} labelled points)")
    found = {}
    for fig, rot in ((front, np.eye(3)), (back, R)):
        for j in range(1, 9):
            for c in fig.word_centre(str(j)):
                if fig is front and c[1] > fig.box[3]:
                    continue
                v = rot @ fig.lift(c)
                found[j] = sign_str(signs(v, T)[0])
    for j in range(1, 9):
        ok(found.get(j) == SIGN_ORDER[j - 1], f"{title}: region label {j} sits in cell {found.get(j)} (expected {SIGN_ORDER[j - 1]})")
    return T


print("\nPage 5: Problem 5 octant views")
T5 = region_check(o0, o1, ["N", "A", "B"], "P5")
N5, A5, B5 = T5
ok(max(abs(N5 @ A5), abs(N5 @ B5), abs(A5 @ B5)) < 0.01, "P5: N, A, B mutually perpendicular (three right angles)")
for f in (o0, o1):
    for a in f.arcs:
        L = lift_arc(f, a)
        n, r = plane_fit(L)
        ok(r < 0.01, f"P5 {'front' if f is o0 else 'back'}: straight line is an edge-on great circle (res {r:.4f})")

print("\nPage 6: Problem 6 views of the 80-80-80 triangle")
f6, b6 = figures(PAGES[5])
T6 = region_check(f6, b6, ["A", "B", "C"], "P6")
A6, B6, C6 = T6
ang6 = (corner(A6, B6, C6), corner(B6, A6, C6), corner(C6, A6, B6))
ok(max(abs(t - 80) for t in ang6) < 0.6, f"P6: printed triangle has corners {tuple(round(t, 2) for t in ang6)}")
V6, _ = side_triangle(f6, ["A", "B", "C", "B*", "C*"])
for f in (f6, b6):
    for a in f.arcs:
        L = lift_arc(f, a)
        n, r = plane_fit(L)
        on = [k for k, v in V6.items() if abs(n @ (v if f is f6 else v)) < 0.01] if f is f6 else []
        ok(r < 0.01, f"P6 {'front' if f is f6 else 'back'}: arc is a great circle (res {r:.4f}) {on}")
ok(np.allclose([dist(A6, B6), dist(B6, C6), dist(C6, A6)], [dist(A6, B6)] * 3, atol=0.5),
   f"P6: equal sides {dist(A6, B6):.2f} deg (equilateral, as three equal corners force)")

print("\nPage 7: Problem 7 records")
caps = [(60, 60, 90), (80, 80, 80), (100, 100, 100)]
for fig, cap in zip(figures(PAGES[6]), caps):
    d = fig.labelled_dots()
    A7, B7, C7 = (fig.lift(one(d, k)) for k in "ABC")
    got = (corner(A7, B7, C7), corner(B7, A7, C7), corner(C7, A7, B7))
    ok(max(abs(g - c) for g, c in zip(got, cap)) < 0.8,
       f"record {cap}: printed sketch has corners A,B,C = {tuple(round(t, 2) for t in got)}")
    for a in fig.arcs:
        L = lift_arc(fig, a)
        n, r = plane_fit(L)
        ok(r < 0.01 and arc_length_deg(L) < 180, f"  side is a minor great-circle arc ({arc_length_deg(L):.1f} deg, res {r:.4f})")

print("\nPage 5 example vs Problem 6 (guide calls the example a 'non-task 80 degree triangle')")
same_front = max(abs(a - b) for k in ("A", "B", "C", "B*", "C*")
                 for a, b in zip(s2.xy(s2.labelled_dots()[k][0]), f6.xy(f6.labelled_dots()[k][0])))
same_back = max(abs(a - b) for k in ("A*", "B", "C", "B*", "C*")
                for a, b in zip(s3.xy(s3.labelled_dots()[k][0]), b6.xy(b6.labelled_dots()[k][0])))
print(f"  INFO example front vs P6 front: max label-point offset {same_front:.4f} radii; back vs back {same_back:.4f} radii")
print("  INFO -> the page-5 example is the Problem 6 triangle in the Problem 6 views; its shaded pair at A")
print("       (front cells +++ and +--, back cells -++ and ---) is P6 regions 1, 4, 5, 8: P6's whole A column.")

print("\nVertex-label boxes that sit on a shaded region at its own vertex (white box drawn over the shape)")
from w61lib import point_in_poly
for pg in (2, 4, 5, 6):
    for fig in figures(PAGES[pg]):
        boxes = [p for p in fig.paths if p["fill"] == [255, 255, 255] and p["stroke"] is None and len(pts_of(p)) == 5]
        polys = [[tuple(q) for q in f["subpaths"][0] if q != "Z"] for f in fig.fills]
        for name, cs in fig.labelled_dots().items():
            for c in cs:
                bx = min(boxes, key=lambda b: math.hypot((bbox(b)[0] + bbox(b)[2]) / 2 - c[0], (bbox(b)[1] + bbox(b)[3]) / 2 - c[1]))
                x0, y0, x1, y1 = bbox(bx)
                probe = [(x0 + (x1 - x0) * i / 6, y0 + (y1 - y0) * j / 6) for i in range(1, 6) for j in range(1, 6)]
                covered = sum(any(point_in_poly(q, P) for P in polys) for q in probe)
                if covered >= 13:
                    print(f"  INFO page {pg + 1}, figure at ({fig.cx:.0f},{fig.cy:.0f}): label {name} box "
                          f"{c[1] - y1:.1f}-{c[1] - y0:.1f} pt above its dot lies over shading ({covered}/25 probe points)")

print("\n" + ("ALL DIAGRAM CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURES"))
