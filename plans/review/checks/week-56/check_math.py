"""Independent mathematical check of Week 56 (Euler's formula, angular defect).

Written for this review; imports nothing from the writer's or guide's
checkers.  Recomputes, from 3D coordinates and brute-force convex hulls:
  P1  V, E, F of cube, tetrahedron, right equilateral prism, octahedron;
  P2  separate sides/corners and the two incidence questions;
  P3  the six corner fans: angle used, gap, and whether a convex pointed
      corner / flat closure exists (explicit symmetric cone construction);
  P4  gap per vertex and total for the four models (measured on the hulls);
  P5  the square pyramid with equilateral sides (two vertex types);
  P6  the three cube redrawings (V, E, F, V-E+F, every vertex defect);
  P7  the opened cube drawing (bounded regions by face tracing), the
      tetrahedron example, the guide's deletion route, spanning trees;
  P8  total defect 720 and V-E+F=2 on many random and named convex solids;
  P9  the two reverse inventories, by the page's own deduction and by hulls;
  guide: the regular-face restriction (n-2)(q-2)<4, the Problem 2 side
      claims, and the preparation arithmetic.
Every guide table value is compared with the delivered facilitator PDF.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import math
import os
import random
import re
from collections import Counter, defaultdict

import sys
sys.dont_write_bytecode = True  # keep the check folder free of __pycache__
from common56 import (HERE, GUIDE_PDF, STUDENT_PDF, Report, convex_hull, face_angles, solid,
                      pdftext, sub, cross, norm, dot, angle_deg, mul, add)

R = Report(os.path.join(HERE, 'out_check_math.txt'))
RND = random.Random(56)


def inventory(points):
    f, e = convex_hull(points)
    return len(points), len(e), len(f), f, e


def defects(points, faces):
    fa = face_angles(points, faces)
    return {v: 360 - sum(a) for v, a in fa.items()}, fa


# ------------------------------------------------------------------ P1, P2, P4
R.out('== Problems 1, 2, 4: the four closed models ==')
expected_p1 = {'cube': (8, 12, 6), 'tetrahedron': (4, 6, 4), 'triangular prism': (6, 9, 5), 'octahedron': (6, 12, 8)}
p2_guide = {'cube': (24, 12, 24, 8), 'tetrahedron': (12, 6, 12, 4), 'triangular prism': (18, 9, 18, 6),
            'octahedron': (24, 12, 24, 6)}
p4_guide = {'cube': (8, 90, 720), 'tetrahedron': (4, 180, 720), 'triangular prism': (6, 120, 720),
            'octahedron': (6, 120, 720)}
corner_counts = {}
for name in ['cube', 'tetrahedron', 'triangular prism', 'octahedron']:
    P = solid(name)
    V, E, F, faces, edges = inventory(P)
    # regular faces?
    side = set(round(norm(sub(P[a], P[b])), 6) for a, b in (tuple(x) for x in edges))
    R.check((V, E, F) == expected_p1[name], f'P1 {name}: (V,E,F)=({V},{E},{F}); guide {expected_p1[name]}; V-E+F={V-E+F}')
    R.check(len(side) == 1, f'   {name}: all edges equal length (regular faces)')
    sides = sum(len(f) for f in faces)
    corners = sides  # an n-gon has n sides and n corners
    corner_counts[name] = corners
    R.check((sides, E, corners, V) == p2_guide[name] and sides == 2 * E,
            f'P2 {name}: separate sides {sides}, edges {E} (= sides/2), separate corners {corners}, vertices {V}')
    d, fa = defects(P, faces)
    conf = Counter(tuple(sorted(round(a) for a in fa[v])) for v in fa)
    gaps = sorted(set(round(x, 6) for x in d.values()))
    total = sum(d.values())
    R.check(len(gaps) == 1 and (V, gaps[0], round(total, 6)) == p4_guide[name],
            f'P4 {name}: one vertex type {dict(conf)}, gap {gaps}, {V} vertices, total {total:.6f} = {total/360:.0f} turns')
R.check(corner_counts['cube'] == corner_counts['octahedron'] == 24,
        'P2 second question: cube and octahedron both have 24 separate corners but 8 vs 6 vertices -> corner count alone does not give V')
R.out('   (corners/3 = V holds for cube 24/3, tetrahedron 12/3, prism 18/3; fails for octahedron 24/3=8 != 6)')

# ------------------------------------------------------------------ P3 fans
R.out('')
R.out('== Problem 3: corner fans ==')


def symmetric_cone(k, alpha_deg):
    """k equal face angles alpha around an apex.  Returns the half-angle
    theta of the edge rays from the axis (90 = flat), or None if impossible."""
    a = math.radians(alpha_deg)
    c = math.cos(2 * math.pi / k)
    s2 = (1 - math.cos(a)) / (1 - c)
    if s2 > 1 + 1e-12:
        return None
    return math.degrees(math.asin(min(1.0, math.sqrt(s2))))


fans = [('3 triangles', [60] * 3, 180, 'Pointed'), ('4 triangles', [60] * 4, 120, 'Pointed'),
        ('5 triangles', [60] * 5, 60, 'Pointed'), ('6 triangles', [60] * 6, 0, 'Flat'),
        ('3 squares', [90] * 3, 90, 'Pointed'), ('4 squares', [90] * 4, 0, 'Flat')]
for label, angs, g_guide, closure_guide in fans:
    used = sum(angs)
    gap = 360 - used
    th = symmetric_cone(len(angs), angs[0])
    if gap > 0:
        # build the cone explicitly and check convexity and face angles
        k = len(angs)
        rays = [(math.sin(math.radians(th)) * math.cos(2 * math.pi * i / k),
                 math.sin(math.radians(th)) * math.sin(2 * math.pi * i / k),
                 math.cos(math.radians(th))) for i in range(k)]
        fa = [angle_deg(rays[i], rays[(i + 1) % k]) for i in range(k)]
        convex = True
        for i in range(k):
            nrm = cross(rays[i], rays[(i + 1) % k])
            sides = [dot(nrm, rays[j]) for j in range(k) if j not in (i, (i + 1) % k)]
            convex &= all(s > 1e-9 for s in sides) or all(s < -1e-9 for s in sides)
        closure = 'Pointed' if convex and all(abs(x - angs[0]) < 1e-9 for x in fa) and th < 90 else '??'
    else:
        closure = 'Flat' if th is not None and abs(th - 90) < 1e-9 else '??'
    R.check(gap == g_guide and closure == closure_guide,
            f'P3 {label}: used {used}, gap {gap}, symmetric cone half-angle {th:.3f} deg -> {closure} (guide: {g_guide}, {closure_guide})')
R.out('   A convex pointed cone needs face angles summing to less than 360 (classical); the two 360-degree')
R.out('   fans can only lie flat or fold with an inward (reflex) crease.  Random check below.')
# random convex cones: angle sum < 360 always
mx = 0
accepted = 0
for _ in range(3000):
    k = RND.randint(3, 7)
    # random convex cone: rays = random points on a small cap, convex position, ordered by angle
    phis = sorted(RND.uniform(0, 2 * math.pi) for _ in range(k))
    hs = [RND.uniform(0.05, 1.0) * 10 ** RND.uniform(0, 1.5) for _ in range(k)]
    rays = [(h * math.cos(p), h * math.sin(p), 1.0) for h, p in zip(hs, phis)]
    # keep only if the polygon of rays (in z=1 plane) is convex and contains the axis
    poly = [(r[0], r[1]) for r in rays]
    cr = [(poly[(i + 1) % k][0] - poly[i][0]) * (poly[(i + 2) % k][1] - poly[i][1]) -
          (poly[(i + 1) % k][1] - poly[i][1]) * (poly[(i + 2) % k][0] - poly[i][0]) for i in range(k)]
    if not all(c > 1e-6 for c in cr):
        continue
    s = sum(angle_deg(rays[i], rays[(i + 1) % k]) for i in range(k))
    accepted += 1
    mx = max(mx, s)
R.check(mx < 360, f'P3 support: {accepted} random convex cones (of 3000 draws) all have face-angle sum < 360 (max {mx:.2f})')

# ------------------------------------------------------------------ P5 pyramid
R.out('')
R.out('== Problem 5: square pyramid with equilateral sides ==')
P = solid('square pyramid')
V, E, F, faces, edges = inventory(P)
lens = sorted(set(round(norm(sub(P[a], P[b])), 9) for a, b in (tuple(x) for x in edges)))
R.check(lens == [1.0], f'apex height 1/sqrt2 makes all 8 edges length 1 (equilateral triangles): {lens}')
d, fa = defects(P, faces)
top = 4
R.check(abs(sum(fa[top]) - 240) < 1e-9 and abs(d[top] - 120) < 1e-9, f'top: corners {[round(a) for a in fa[top]]} use 240, gap {d[top]:.3f}')
base = [v for v in d if v != top]
R.check(all(abs(sum(fa[v]) - 210) < 1e-9 and abs(d[v] - 150) < 1e-9 for v in base),
        f'4 base corners: corners {sorted(round(a) for a in fa[base[0]])} use 210, gap 150 each')
R.check((V, E, F) == (5, 8, 5) and abs(sum(d.values()) - 720) < 1e-9,
        f'(V,E,F)=({V},{E},{F}); total gap {sum(d.values()):.6f} = 120 + 4*150')

# ------------------------------------------------------------------ P6 cube redrawings
R.out('')
R.out('== Problem 6: cube surface redrawings (each starting from the original cube) ==')
cube = solid('cube')
cf, ce = convex_hull(cube)


def cell_stats(pts, faces):
    edges = set()
    for f in faces:
        for a, b in zip(f, f[1:] + f[:1]):
            edges.add(frozenset((a, b)))
    inc = Counter()
    for f in faces:
        for a, b in zip(f, f[1:] + f[:1]):
            inc[frozenset((a, b))] += 1
    assert all(c == 2 for c in inc.values()), 'every edge must lie in two faces'
    fa = {}
    for f in faces:
        L = len(f)
        for t, v in enumerate(f):
            u, w = f[t - 1], f[(t + 1) % L]
            fa.setdefault(v, []).append(angle_deg(sub(pts[u], pts[v]), sub(pts[w], pts[v])))
    d = {v: 360 - sum(a) for v, a in fa.items()}
    used = {v for f in faces for v in f}
    return len(used), len(edges), len(faces), d


def redraw(kind):
    pts = list(cube)
    faces = [list(f) for f in cf]
    f0 = faces[0]
    if kind == 'diagonal':
        a, b, c, e = f0
        faces[0:1] = [[a, b, c], [a, c, e]]
    elif kind == 'center':
        cen = mul(tuple(sum(pts[v][k] for v in f0) for k in range(3)), 0.25)
        pts.append(cen)
        m = len(pts) - 1
        faces[0:1] = [[f0[i], f0[(i + 1) % 4], m] for i in range(4)]
    elif kind == 'edge point':
        a, b = f0[0], f0[1]
        mid = mul(add(pts[a], pts[b]), 0.5)
        pts.append(mid)
        m = len(pts) - 1
        new = []
        for f in faces:
            g = []
            L = len(f)
            for t, v in enumerate(f):
                g.append(v)
                w = f[(t + 1) % L]
                if {v, w} == {a, b}:
                    g.append(m)
            new.append(g)
        faces = new
    return pts, faces


guide6 = {'original': (8, 12, 6), 'diagonal': (8, 13, 7), 'center': (9, 16, 9), 'edge point': (9, 13, 6)}
for kind in ['original', 'diagonal', 'center', 'edge point']:
    pts, faces = redraw(kind)
    V, E, F, d = cell_stats(pts, faces)
    newv = [v for v in d if v >= 8]
    R.check((V, E, F) == guide6[kind] and V - E + F == 2 and abs(sum(d.values()) - 720) < 1e-9
            and all(abs(d[v] - 90) < 1e-9 for v in range(8)) and all(abs(d[v]) < 1e-9 for v in newv),
            f'{kind}: (V,E,F)=({V},{E},{F}), V-E+F={V-E+F}, total gap {sum(d.values()):.6f}, '
            f'old corners 90 each, new-vertex gaps {[round(d[v], 9) for v in newv]} (guide {guide6[kind]})')
# cumulative reading (all three changes kept, on three different faces; and on one face)
pts = list(cube); faces = [list(f) for f in cf]
R.out('   other reading -- changes accumulated on one cube:')
# diagonal on cube face 0, centre on cube face 1, then an edge point on an edge of a third face
q0, q1 = [list(f) for f in cf[0:2]]
rest = [list(f) for f in cf[2:]]
a, b, c, e = q0
cenp = mul(tuple(sum(pts[v][k] for v in q1) for k in range(3)), 0.25); pts.append(cenp); m = len(pts) - 1
faces = [[a, b, c], [a, c, e]] + rest
s = cell_stats(pts, faces + [[q1[i], q1[(i + 1) % 4], m] for i in range(4)])
s_diag_only = cell_stats(pts[:8], [[a, b, c], [a, c, e]] + [q1] + rest)
R.out(f'     diagonal only: V,E,F = {s_diag_only[:3]}')
faces = faces + [[q1[i], q1[(i + 1) % 4], m] for i in range(4)]
R.out(f'     diagonal then centre (different faces): V,E,F = {s[:3]}, V-E+F = {s[0]-s[1]+s[2]}, total {sum(s[3].values()):.3f}')
q0e = {frozenset(x) for x in zip(q0, q0[1:] + q0[:1])}
q1e = {frozenset(x) for x in zip(q1, q1[1:] + q1[:1])}
cand = None
for f in rest:
    for x, y in zip(f, f[1:] + f[:1]):
        if frozenset((x, y)) not in q0e | q1e:
            cand = (x, y); break
    if cand:
        break
x, y = cand
pts.append(mul(add(pts[x], pts[y]), 0.5)); m2 = len(pts) - 1
nf = []
for f in faces:
    g = []
    for t, v in enumerate(f):
        g.append(v)
        if {v, f[(t + 1) % len(f)]} == {x, y}:
            g.append(m2)
    nf.append(g)
s = cell_stats(pts, nf)
R.out(f'     ... then an edge point: V,E,F = {s[:3]}, V-E+F = {s[0]-s[1]+s[2]}, total {sum(s[3].values()):.3f}')
# same face: centre lines drawn on the face that already has the diagonal
pts2 = list(cube); cen0 = mul(tuple(sum(pts2[v][k] for v in q0) for k in range(3)), 0.25); pts2.append(cen0)
s2 = cell_stats(pts2, [[q0[i], q0[(i + 1) % 4], 8] for i in range(4)] + [q1] + rest)
R.out(f'     diagonal then centre on the SAME face: V,E,F = {s2[:3]} (same as the guide row)')
R.out('     (rows 3-4 of the table would differ from the guide key; the conclusions do not)')

# ------------------------------------------------------------------ P7 opened drawings
R.out('')
R.out('== Problem 7: opened drawings and trees ==')


def plane_faces(pos, edges):
    """Faces of a plane straight-line graph by half-edge tracing.
    Returns list of faces (lists of vertices) and signed areas."""
    nb = defaultdict(list)
    for a, b in edges:
        nb[a].append(b); nb[b].append(a)
    for v in nb:
        nb[v].sort(key=lambda w: math.atan2(pos[w][1] - pos[v][1], pos[w][0] - pos[v][0]))
    seen = set(); faces = []
    for a, b in edges:
        for h in ((a, b), (b, a)):
            if h in seen:
                continue
            cyc = []; cur = h
            while cur not in seen:
                seen.add(cur); cyc.append(cur[0])
                u, v = cur
                lst = nb[v]; i = lst.index(u)
                w = lst[(i - 1) % len(lst)]  # next edge clockwise from (v->u): keeps face on the left
                cur = (v, w)
            area = sum(pos[cyc[i]][0] * pos[cyc[(i + 1) % len(cyc)]][1] - pos[cyc[(i + 1) % len(cyc)]][0] * pos[cyc[i]][1]
                       for i in range(len(cyc))) / 2
            faces.append((cyc, area))
    return faces


def components(vs, edges):
    par = {v: v for v in vs}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for a, b in edges:
        par[f(a)] = f(b)
    return len({f(v) for v in vs})


def bounded(pos, edges):
    fs = plane_faces(pos, edges)
    # one unbounded face per connected component; bounded faces have positive area (CCW)
    return sum(1 for c, a in fs if a > 1e-9)


# exact student p.7 drawing (source coordinates)
pos = {'A': (0, 0), 'B': (4.5, 0), 'C': (4.5, 4.5), 'D': (0, 4.5),
       'a': (1.4, 1.4), 'b': (3.1, 1.4), 'c': (3.1, 3.1), 'd': (1.4, 3.1)}
cube_edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'),
              ('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]
nb = bounded(pos, cube_edges)
R.check(nb == 5 and len(pos) - len(cube_edges) + nb == 1,
        f'opened cube (p.7): V=8, E=12, bounded regions {nb} ("five bounded faces"), V-E+F_bounded = {8-12+nb}')
# guide route
route = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('a', 'b')]
cur = list(cube_edges); ok = True; trace = []
for e in route:
    before = bounded(pos, cur)
    cur = [x for x in cur if x != e]
    after = bounded(pos, cur)
    conn = components(pos, cur) == 1
    trace.append((e, len(cur), after, conn))
    ok &= conn and after == before - 1
R.out('   guide route (edge erased, edges left, bounded regions, connected): ' + str(trace))
is_tree = len(cur) == 7 and components(pos, cur) == 1 and bounded(pos, cur) == 0
R.check(ok and is_tree, 'guide route AB,BC,CD,DA,ab: each step keeps 8 dots connected and removes one bounded region; ends in a tree (8 dots, 7 edges)')
# check that each outer deletion merges with the outside: the erased edge borders the unbounded face
cur = list(cube_edges); outside_merge = []
for e in route:
    fs = plane_faces(pos, cur)
    unb = [c for c, a in fs if a <= 1e-9]
    border = any(any({c[i], c[(i + 1) % len(c)]} == set(e) for i in range(len(c))) for c in unb)
    outside_merge.append(border)
    cur = [x for x in cur if x != e]
R.check(all(outside_merge), f'every deletion on the guide route borders the outside region: {outside_merge}')
# spanning trees of the cube graph (Kirchhoff) -- any opened drawing reduces to a tree
idx = {v: i for i, v in enumerate(pos)}
n = len(idx)
L = [[0] * n for _ in range(n)]
for a, b in cube_edges:
    i, j = idx[a], idx[b]
    L[i][i] += 1; L[j][j] += 1; L[i][j] -= 1; L[j][i] -= 1
M = [row[1:] for row in L[1:]]
from fractions import Fraction
Mf = [[Fraction(x) for x in row] for row in M]
det = Fraction(1)
for c in range(n - 1):
    p = next(r for r in range(c, n - 1) if Mf[r][c] != 0)
    if p != c:
        Mf[c], Mf[p] = Mf[p], Mf[c]; det = -det
    det *= Mf[c][c]
    for r in range(c + 1, n - 1):
        fct = Mf[r][c] / Mf[c][c]
        for k in range(c, n - 1):
            Mf[r][k] -= fct * Mf[c][k]
R.check(det == 384, f'the cube graph has {det} spanning trees (so "yes": many trees keep all 8 vertices connected)')
# exhaustive: every 5-edge deletion set leaving a connected graph gives a tree with 0 bounded regions
cnt = 0; good = 0
for rem in itertools.combinations(cube_edges, 5):
    keep = [e for e in cube_edges if e not in rem]
    if components(pos, keep) == 1:
        cnt += 1
        good += bounded(pos, keep) == 0
R.check(cnt == 384 and good == 384, f'all {cnt} connected 7-edge subgraphs are trees with no bounded region')
# tetrahedron example on p.7: triangle (3.9,0),(6.2,0),(5.05,2) with interior (5.05,.67)
tp = {'p': (3.9, 0), 'q': (6.2, 0), 'r': (5.05, 2), 's': (5.05, .67)}
te = [('p', 'q'), ('q', 'r'), ('r', 'p'), ('s', 'p'), ('s', 'q'), ('s', 'r')]
nbt = bounded(tp, te)
tree_e = te[3:]
R.check(nbt == 3 and bounded(tp, tree_e) == 0 and components(tp, tree_e) == 1,
        f'p.7 tetrahedron view: 4 dots, 6 edges, {nbt} bounded regions (three faces); erasing the 3 boundary edges leaves a 3-edge tree')

# ------------------------------------------------------------------ P8 general theorem
R.out('')
R.out('== Problem 8: total gap 720 and V-E+F = 2 on many convex solids ==')
named = ['cube', 'tetrahedron', 'octahedron', 'triangular prism', 'square pyramid', 'icosahedron', 'dodecahedron']
extra = {}
for k in range(3, 9):  # prisms and antiprisms, bipyramids
    ring = [(math.cos(2 * math.pi * i / k), math.sin(2 * math.pi * i / k)) for i in range(k)]
    extra[f'{k}-prism'] = [(x, y, 0.0) for x, y in ring] + [(x, y, 1.3) for x, y in ring]
    extra[f'{k}-antiprism'] = [(x, y, 0.0) for x, y in ring] + [
        (math.cos(2 * math.pi * (i + .5) / k), math.sin(2 * math.pi * (i + .5) / k), 0.8) for i in range(k)]
    extra[f'{k}-bipyramid'] = [(x, y, 0.0) for x, y in ring] + [(0, 0, 1.1), (0, 0, -0.7)]
# truncated cube corner and a house shape (mixed faces)
extra['house'] = solid('cube') + [(0.5, 0.0, 1.6), (0.5, 1.0, 1.6)]
extra['cut-corner cube'] = [p for p in solid('cube') if p != (1.0, 1.0, 1.0)] + [(0.6, 1, 1), (1, 0.6, 1), (1, 1, 0.6)]
bad = []
count = 0
for name in named:
    P = solid(name)
    V, E, F, faces, edges = inventory(P)
    d, _ = defects(P, faces)
    count += 1
    if V - E + F != 2 or abs(sum(d.values()) - 720) > 1e-6 or min(d.values()) <= 0:
        bad.append(name)
for name, P in extra.items():
    V, E, F, faces, edges = inventory(P)
    d, _ = defects(P, faces)
    count += 1
    if V - E + F != 2 or abs(sum(d.values()) - 720) > 1e-6 or min(d.values()) <= 0:
        bad.append(name)
for t in range(60):
    k = RND.randint(5, 16)
    P = []
    for _ in range(k):
        z = RND.uniform(-1, 1); ph = RND.uniform(0, 2 * math.pi); r = math.sqrt(1 - z * z)
        P.append((r * math.cos(ph), r * math.sin(ph), z * RND.uniform(0.6, 1.4)))
    V, E, F, faces, edges = inventory(P)
    used = {v for f in faces for v in f}
    Pv = [P[i] for i in sorted(used)]
    V, E, F, faces, edges = inventory(Pv)
    d, _ = defects(Pv, faces)
    count += 1
    if V - E + F != 2 or abs(sum(d.values()) - 720) > 1e-6 or min(d.values()) <= 0:
        bad.append(f'random {t}')
R.check(not bad, f'{count} convex solids (7 named, {len(extra)} prisms/antiprisms/bipyramids/mixed, 60 random): '
                 f'all have V-E+F=2, every vertex gap > 0, total gap 720' + (f' FAILED {bad}' if bad else ''))
# the guide's face-angle identity on the mixed 'house'
P = extra['house']; V, E, F, faces, edges = inventory(P)
fsum = sum(180 * (len(f) - 2) for f in faces)
R.check(fsum == 360 * (E - F) and 360 * V - fsum == 720,
        f'house solid (faces {sorted(len(f) for f in faces)}): sum 180(n_f-2) = {fsum} = 360(E-F); 360V - that = {360*V - fsum}')
# pentagon triangulation example
R.check(3 * 180 == 540 == 180 * (5 - 2), 'p.8 example: pentagon -> 3 triangles -> 540 degrees')

# ------------------------------------------------------------------ P9 reverse inventory
R.out('')
R.out('== Problem 9: reverse inventories ==')
for name, n, q, guide in [('icosahedron', 3, 5, (12, 30, 20)), ('dodecahedron', 5, 3, (20, 30, 12))]:
    ang = 180 * (n - 2) / n
    gap = 360 - q * ang
    V = 720 / gap
    F = q * V / n
    E = n * F / 2
    P = solid(name)
    Vh, Eh, Fh, faces, edges = inventory(P)
    d, fa = defects(P, faces)
    conf = Counter(tuple(sorted(round(a, 6) for a in fa[v])) for v in fa)
    R.check((V, E, F) == guide == (Vh, Eh, Fh) and len(conf) == 1 and all(len(f) == n for f in faces),
            f'{q} regular {n}-gons per vertex: gap {gap:g}, V=720/{gap:g}={V:g}, F={q}V/{n}={F:g}, E={n}F/2={E:g}; '
            f'hull of the {name}: ({Vh},{Eh},{Fh}), vertex type {dict(conf)}')
R.out('   uniqueness: V is forced by 720/gap once every vertex is alike, then F and E by incidence counting.')
# p.9 diagrams: five triangles fill 0..300, pentagons three 108-degree corners
R.check(5 * 60 == 300 and 3 * 108 == 324, 'fan pictures: 5x60=300 (gap 60), 3x108=324 (gap 36)')

# ------------------------------------------------------------------ guide extras
R.out('')
R.out('== Guide: regular-face restriction and arithmetic ==')
cands = [(n, q) for n in range(3, 50) for q in range(3, 50) if q * 180 * (n - 2) / n < 360 - 1e-9]
alt = [(n, q) for n in range(3, 50) for q in range(3, 50) if (n - 2) * (q - 2) < 4]
R.check(cands == alt == [(3, 3), (3, 4), (3, 5), (4, 3), (5, 3)],
        f'q*180(n-2)/n < 360 <=> (n-2)(q-2) < 4; candidates {cands}')
for (n, q), name in zip(cands, ['tetrahedron', 'octahedron', 'icosahedron', 'cube', 'dodecahedron']):
    P = solid(name); V, E, F, faces, edges = inventory(P)
    R.check(all(len(f) == n for f in faces) and n * F == q * V == 2 * E,
            f'   ({n},{q}) realised by the {name}: nF = qV = 2E = {2*E}')
# preparation arithmetic quoted in the guide
R.check(3 * (6 + 4 + 8 + 5 + 5) == 84, '84 polygon faces across 15 models')
R.check(3 * sum(E - (F - 1) for E, F in [(12, 6), (6, 4), (12, 8), (9, 5), (8, 5)]) == 72,
        '72 tabbed closing seams = 3 x sum(E - (F-1))')
R.check(3 * 2 + 6 * 2 == 18 and 2 + 6 * 2 + 9 * 2 == 32, '18 cardstock sheets; 32 student sheets (2 + 2x6 + 2x9)')
R.check(6 * (5 + 3) == 48 and 5 * 8 == 40 and 5 * 2 == 10, '48 hinge strips (6 sets x (5+3)); 40 triangles, 40 squares, 10 circles')
R.check(30 * math.sqrt(2) > 40 and 30 < 40, f'square far corner {30*math.sqrt(2):.1f} mm > 40 mm circle radius; triangle far corner 30 mm < 40')

# ------------------------------------------------------------------ guide PDF tables
R.out('')
R.out('== Delivered guide PDF: printed table values ==')
# pdftotext renders the TeX degree sign as U+25E6; normalise it
g = re.sub(r'[ \t]+', ' ', pdftext(GUIDE_PDF, layout=True)).replace('\u25e6', '\u00b0')
rows = [
    r'Cube 8 12 6 2', r'Regular tetrahedron 4 6 4 2', r'Right triangular prism 6 9 5 2', r'Regular octahedron 6 12 8 2',
    r'6 squares: cube 24 12 24 8', r'4 triangles: tetrahedron 12 6 12 4', r'2 triangles, 3 squares: prism 18 9 18 6',
    r'8 triangles: octahedron 24 12 24 6',
    r'3 equilateral triangles 180° 180° Pointed', r'4 equilateral triangles 240° 120° Pointed',
    r'5 equilateral triangles 300° 60° Pointed', r'6 equilateral triangles 360° 0° Flat',
    r'3 squares 270° 90° Pointed', r'4 squares 360° 0° Flat',
    r'Cube 8 3 squares: 270° 90° 720°', r'Tetrahedron 4 3 triangles: 180° 180° 720°',
    r'Triangular prism 6 1 triangle, 2 squares: 240° 120° 720°', r'Octahedron 6 4 triangles: 240° 120° 720°',
    r'Top 1 4 triangles: 240° 120° 120°', r'Base corner 4 1 square, 2 triangles: 210° 150° 600°',
    r'Original 8 12 6 2 720°', r'One face diagonal 8 13 7 2 720°', r'Face center and 4 lines 9 16 9 2 720°',
    r'One point along an edge 9 13 6 2 720°',
]
for row in rows:
    R.check(row in g, f'guide PDF prints "{row}"')
R.check(bool(re.search(r'V\s*=\s*720/60\s*=\s*12', g)) and bool(re.search(r'V\s*=\s*720/36\s*=\s*20', g)),
        'guide P9: V = 720/60 = 12 and V = 720/36 = 20 printed')
R.check('(12, 30, 20)' in g and '(20, 30, 12)' in g, 'guide P9: (12, 30, 20) and (20, 30, 12) printed')
R.finish()
