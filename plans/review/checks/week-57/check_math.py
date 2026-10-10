"""Independent mathematical check of Week 57 (Area from dots / Pick's theorem).

Uses only lattice57 (written for this review); the packet's verify_math.py,
verify_pdf.py and guide verify.py are not imported or run.  Coordinates are the
guide's adult keys, which check_diagrams.py confirms against the delivered
student PDF.  The guide's printed numbers are read back from the delivered
facilitator PDF with pdftotext and compared.

Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import os
import random
import re
import subprocess
import sys
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
import lattice57 as L  # noqa: E402

ROOT = L.repo_root()
GUIDE = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-57', 'week-57-facilitator.pdf')
STUDENT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-57', 'week-57-students.pdf')
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def rec(poly, holes=()):
    I, B = L.counts(poly, holes)
    A1 = L.area_cells(poly, holes)
    A2 = L.area_shoelace(poly) - sum(L.area_shoelace(h) for h in holes)
    assert A1 == A2, (poly, A1, A2)
    return I, B, A1


def pick(I, B, h=0):
    return I + F(B, 2) - 1 + h


def fits(poly, w, h):
    return all(0 <= x <= w and 0 <= y <= h for x, y in poly)


def pdftext(path):
    return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True,
                          text=True).stdout


GT = pdftext(GUIDE)
GT1 = re.sub(r'\s+', ' ', GT)
ST = re.sub(r'\s+', ' ', pdftext(STUDENT))


def in_guide(s):
    return re.sub(r'\s+', ' ', s) in GT1


# ---------------------------------------------------------------- panels
say('== Shared panels (student pp. 1-2)')
tri = [(0, 0), (2, 0), (0, 1)]
tri2 = [(2, 0), (2, 1), (0, 1)]
rect21 = [(0, 0), (2, 0), (2, 1), (0, 1)]
check(rec(tri) == (0, 4, 1) and rec(tri2) == (0, 4, 1) and rec(rect21) == (0, 6, 2),
      'p.1 panel: each copy (0,4,1), rectangle (0,6,2); page prints "Rectangle area: 2", "One copy\'s area: 1"')
check(L.meet_exactly(tri, tri2, (2, 0), (0, 1)), 'p.1 panel: the two copies meet exactly along the dashed diagonal')
check(rec([(0, 0), (2, 0), (2, 2), (0, 2)]) == (1, 8, 4) and L.dot_sets([(0, 0), (2, 0), (2, 2), (0, 2)])[0] == [(1, 1)],
      'p.2 panel: 2x2 square has I=1, B=8, area 4 as printed')
check('Rectangle area: 2' in ST and ("One copy’s area: 1" in ST or "One copy's area: 1" in ST)
      and 'I=1 B=8 area= 4' in ST,
      'p.1 and p.2 panel outputs read from the student PDF text')

# ---------------------------------------------------------------- P1
say('== Problem 1')
P1R = [(0, 1), (3, 1), (3, 3), (0, 3)]
P1S = [(0, 0), (2, 0), (3, 3), (1, 3)]
check(rec(P1R)[2] == 6 and rec(P1S)[2] == 6, 'P1: both areas are 6')
# guide's dissection: wedge (0,0),(1,0),(1,3) cut along x=1 and moved 2 right
wedge = [(0, 0), (1, 0), (1, 3)]
rest = [(1, 0), (2, 0), (3, 3), (1, 3)]
moved = [(x + 2, y) for x, y in wedge]
target = [(1, 0), (3, 0), (3, 3), (1, 3)]
ok = True
N = 37
for i in range(N * 3):
    for j in range(N * 3):
        p = (F(2 * i + 1, 2 * N), F(2 * j + 1, 2 * N))
        inP = L.classify(P1S, p)
        inW, inR = L.classify(wedge, p), L.classify(rest, p)
        if 'boundary' in (inP, inW, inR):
            continue
        if (inP == 'inside') != ((inW == 'inside') + (inR == 'inside') == 1) or (inW == inR == 'inside'):
            ok = False
        inT = L.classify(target, p)
        inM, inR2 = L.classify(moved, p), L.classify(rest, p)
        if 'boundary' in (inT, inM, inR2):
            continue
        if (inT == 'inside') != ((inM == 'inside') + (inR2 == 'inside') == 1) or (inM == inR2 == 'inside'):
            ok = False
check(ok, 'P1 guide: wedge (0,0),(1,0),(1,3) + rest tile the parallelogram; moved 2 right they tile [1,3]x[0,3]')

# ---------------------------------------------------------------- P2
say('== Problem 2')
Lsh = [(0, 0), (3, 0), (3, 1), (1, 1), (1, 3), (0, 3)]
T2 = [(0, 0), (3, 0), (1, 3)]
check(rec(Lsh) == (0, 12, 5), 'P2: L-shape (0,12,5)')
check(L.dot_sets(Lsh)[0] == [], 'P2: L-shape has no inside dot (guide)')
check(rec(T2) == (3, 5, F(9, 2)), 'P2: triangle (3,5,9/2)')
ins, bd = L.dot_sets(T2)
check(ins == [(1, 1), (1, 2), (2, 1)] and bd == [(0, 0), (1, 0), (1, 3), (2, 0), (3, 0)],
      'P2 guide: inside (1,1),(1,2),(2,1); boundary four base dots and (1,3)')
for a, b in (((0, 0), (1, 3)), ((3, 0), (1, 3))):
    c = [p for p in T2 if p not in (a, b)][0]
    img = (a[0] + b[0] - c[0], a[1] + b[1] - c[1])
    par = [c, a, img, b] if L.is_simple([c, a, img, b]) else [a, c, b, img]
    A = L.area_shoelace(par)
    ys = [p[1] for p in par]
    hz = [(p, q) for p, q in L.edges(par) if p[1] == q[1]]
    check(A == 9 and max(ys) - min(ys) == 3 and all(abs(p[0] - q[0]) == 3 for p, q in hz) and len(hz) == 2,
          'P2 guide: two copies joined on side %s-%s give parallelogram %s, base 3, height 3, area 9' % (a, b, par))

# ---------------------------------------------------------------- P3
say('== Problem 3 (5x5-dot boards, 0..4)')
G4 = [(x, y) for x in range(5) for y in range(5)]


def simple_quads(points):
    for c in itertools.combinations(points, 4):
        a = c[0]
        for perm in ((c[1], c[2], c[3]), (c[1], c[3], c[2]), (c[2], c[1], c[3])):
            q = [a, *perm]
            if L.area2_signed(q) != 0 and L.is_simple(q):
                yield q


tris3 = [list(t) for t in itertools.combinations(G4, 3) if L.area2_signed(list(t)) != 0]
t26 = [t for t in tris3 if L.boundary_gcd(t) == 6 and L.counts(t) == (2, 6)]
q26 = [q for q in simple_quads(G4) if L.boundary_gcd(q) == 6 and L.counts(q) == (2, 6)]
check(len(t26) > 0 and len(q26) > 0, 'P3: triangles with (I,B)=(2,6) on the board: %d; four-sided shapes: %d'
      % (len(t26), len(q26)))
check(all(L.area_cells(p) == 4 for p in t26 + q26), 'P3: every one of them has area 4')
conv = sum(1 for q in q26 if all(L.cross(q[i], q[(i + 1) % 4], q[(i + 2) % 4]) * L.area2_signed(q) > 0 for i in range(4)))
say('     P3: of the %d four-sided shapes, %d convex and %d with an inward corner' % (len(q26), conv, len(q26) - conv))
W3T = [(0, 0), (4, 0), (1, 2)]
W3Q = [(0, 0), (2, 0), (3, 2), (1, 2)]
check(rec(W3T) == (2, 6, 4) and L.dot_sets(W3T)[0] == [(1, 1), (2, 1)],
      'P3 guide triangle (0,0),(4,0),(1,2): (2,6,4), inside (1,1),(2,1)')
check(rec(W3Q) == (2, 6, 4) and L.dot_sets(W3Q)[0] == [(1, 1), (2, 1)] and
      sorted(L.dot_sets(W3Q)[1]) == sorted(W3Q + [(1, 0), (2, 2)]),
      'P3 guide quadrilateral (0,0),(2,0),(3,2),(1,2): (2,6,4), inside (1,1),(2,1), boundary = corners + (1,0),(2,2)')
check(fits(W3T, 4, 4) and fits(W3Q, 4, 4), 'P3 guide witnesses fit 0..4')
apex = [p for p in G4 if p[1] > 0 and L.counts([(0, 0), (4, 0), p]) == (2, 6)]
check(len(apex) > 0, 'P3 hint 3: horizontal base of four intervals at y=0 admits apexes %s' % apex)
par2 = [s for s in range(-3, 4) for h in range(1, 5)
        if fits([(0, 0), (2, 0), (2 + s, h), (s, h)], 4, 4) and L.counts([(0, 0), (2, 0), (2 + s, h), (s, h)]) == (2, 6)]
check(len(par2) > 0, 'P3 hint 3: base of two intervals at (0,0)-(2,0) admits a parallelogram')

# ---------------------------------------------------------------- P4
say('== Problem 4')
records = [(1, 8, F(4)), (0, 12, F(5)), (3, 5, F(9, 2)), (2, 6, F(4))]
# solve area = a I + b B + c from the first three, test the fourth
import itertools as _it  # noqa: E402,F811
sol = None
for r1, r2, r3 in _it.combinations(records, 3):
    M = [[F(r[0]), F(r[1]), F(1), r[2]] for r in (r1, r2, r3)]
    # Gaussian elimination
    try:
        for c in range(3):
            piv = next(i for i in range(c, 3) if M[i][c] != 0)
            M[c], M[piv] = M[piv], M[c]
            for i in range(3):
                if i != c and M[i][c] != 0:
                    f = M[i][c] / M[c][c]
                    M[i] = [x - f * y for x, y in zip(M[i], M[c])]
        s = tuple(M[i][3] / M[i][i] for i in range(3))
        sol = sol or s
        check(s == (1, F(1, 2), -1), 'P4: records %s determine area = I + B/2 - 1 uniquely among linear rules'
              % ([r[:2] for r in (r1, r2, r3)],))
    except StopIteration:
        say('     P4: records %s are linearly dependent' % ([r[:2] for r in (r1, r2, r3)],))
check(F(4, 2) != 1 and F(12, 2) != 5, 'P4 guide: "area is half of B" predicts 2 for the unit square (area 1) and 6 for the L (area 5)')
check(rec([(0, 0), (1, 0), (1, 1), (0, 1)]) == (0, 4, 1), 'P4 guide: unit square (0,4,1)')

# ---------------------------------------------------------------- P5
say('== Problem 5 (7x7-dot board, 0..6)')
G6 = [(x, y) for x in range(7) for y in range(7)]
seen = {}
seenB = set()
for t in itertools.combinations(G6, 3):
    t = list(t)
    if abs(L.area2_signed(t)) == 12:
        seen.setdefault(L.counts(t), t)
for c in itertools.combinations(G6, 4):
    a = c[0]
    for perm in ((c[1], c[2], c[3]), (c[1], c[3], c[2]), (c[2], c[1], c[3])):
        q = [a, *perm]
        if abs(L.area2_signed(q)) == 12 and L.is_simple(q):
            r = L.boundary_gcd(q)
            if r not in seenB:
                seenB.add(r)
                seen.setdefault(L.counts(q), q)
want = [(0, 14), (1, 12), (2, 10), (3, 8), (4, 6), (5, 4)]
check(sorted(seen) == want, 'P5: (I,B) records realised by area-6 triangles/quadrilaterals on the board: %s' % sorted(seen))
for k in want:
    check(pick(*k) == 6, 'P5: Pick gives 6 for %s' % (k,))
W5 = {(0, 14): [(0, 0), (6, 0), (6, 1), (0, 1)],
      (1, 12): [(0, 0), (5, 0), (5, 1), (4, 1), (3, 2), (2, 1), (0, 1)],
      (2, 10): [(0, 0), (3, 0), (3, 2), (0, 2)],
      (3, 8): [(0, 0), (3, 0), (4, 2), (1, 2)],
      (4, 6): [(0, 0), (2, 0), (3, 3), (1, 3)],
      (5, 4): [(0, 0), (2, 1), (6, 6), (4, 5)]}
for k, poly in W5.items():
    r = rec(poly)
    check(L.is_simple(poly) and fits(poly, 6, 6) and r == (k[0], k[1], 6),
          'P5 guide witness %s: simple, fits 0..6, record %s' % (poly, r))
# strip-width certificate for the slender parallelogram


def width_at(poly, y):
    xs = []
    for a, b in L.edges(poly):
        if a[1] != b[1] and min(a[1], b[1]) <= y <= max(a[1], b[1]):
            xs.append(a[0] + F(y - a[1]) * (b[0] - a[0]) / (b[1] - a[1]))
    return max(xs) - min(xs)


par = W5[(5, 4)]
ok = all(width_at(par, F(k, 10)) == F(6, 5) for k in range(10, 51))
ok &= all(width_at(par, F(k, 10)) == F(6, 5) * F(k, 10) for k in range(0, 11))
ok &= all(width_at(par, F(k, 10)) == F(6, 5) * (6 - F(k, 10)) for k in range(50, 61))
check(ok, 'P5 guide: cross-section width 6y/5 on 0<=y<=1, 6/5 on 1<=y<=5, 6(6-y)/5 on 5<=y<=6')
check(F(24, 5) + F(3, 5) + F(3, 5) == 6, 'P5 guide: 24/5 + 3/5 + 3/5 = 6')
check(L.boundary_gcd(par) == 4 and len(par) == 4, 'P5 guide: its four sides have no intermediate dots')
tB4 = [list(t) for t in itertools.combinations(G6, 3) if abs(L.area2_signed(list(t))) == 12 and L.boundary_gcd(list(t)) == 4]
say('     P5 note: (5,4) is also realised by %d area-6 triangles on the board, e.g. %s' % (len(tB4), tB4[0] if tB4 else None))

# ---------------------------------------------------------------- P6
say('== Problem 6')
R6 = [(0, 0), (4, 0), (4, 2), (0, 2)]
R6l, R6r = [(0, 0), (2, 0), (2, 2), (0, 2)], [(2, 0), (4, 0), (4, 2), (2, 2)]
S6 = [(0, 0), (2, 0), (3, 3), (1, 3)]
S6lo, S6up = [(0, 0), (2, 0), (3, 3)], [(0, 0), (3, 3), (1, 3)]
check((rec(R6l), rec(R6r), rec(R6)) == ((1, 8, 4), (1, 8, 4), (3, 12, 8)), 'P6 rectangle: left (1,8,4), right (1,8,4), whole (3,12,8)')
check((rec(S6lo), rec(S6up), rec(S6)) == ((1, 6, 3), (1, 6, 3), (4, 6, 6)), 'P6 slanted: lower (1,6,3), upper (1,6,3), whole (4,6,6)')
check(sorted((3 - x, 3 - y) for x, y in S6lo) == sorted(S6up), 'P6 guide: upper piece is the lower piece by a half-turn')
check(L.meet_exactly(R6l, R6r, (2, 0), (2, 2)) and L.meet_exactly(S6lo, S6up, (0, 0), (3, 3)), 'P6: each pair meets exactly along its seam')
check(len(L.segment_dots((2, 0), (2, 2))) == 3 and len(L.segment_dots((0, 0), (3, 3))) == 4, 'P6 guide: k=3 and k=4')
check(L.dot_sets(R6)[0] == [(1, 1), (2, 1), (3, 1)], 'P6 guide: only (2,1) becomes inside in the rectangle')

# ---------------------------------------------------------------- P7 join
say('== Problem 7: joining along one segment')
rng = random.Random(57)


def random_simple(n, size):
    for _ in range(200):
        pts = list({(rng.randint(0, size), rng.randint(0, size)) for _ in range(n)})
        if len(pts) < 3:
            continue
        cx = F(sum(p[0] for p in pts), len(pts))
        cy = F(sum(p[1] for p in pts), len(pts))
        import math
        pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
        if L.is_simple(pts):
            return pts
    return None


def split_along(poly, p, q):
    """Insert boundary lattice points p, q as vertices and return the two arcs."""
    pts = list(poly)
    for z in (p, q):
        if z in pts:
            continue
        for i, (a, b) in enumerate(L.edges(pts)):
            if L.on_segment(z, a, b):
                pts.insert(i + 1, z)
                break
        else:
            return None
    i, j = pts.index(p), pts.index(q)
    if i > j:
        i, j = j, i
    A = pts[i:j + 1]
    Bp = pts[j:] + pts[:i + 1]
    return A, Bp


def drop_straight(poly):
    out = []
    n = len(poly)
    for k in range(n):
        if L.cross(poly[k - 1], poly[k], poly[(k + 1) % n]) != 0:
            out.append(poly[k])
    return out


tested = 0
bad = []
endpoints_boundary = True
for trial in range(3000):
    U = random_simple(rng.randint(3, 8), rng.choice([4, 5, 6]))
    if U is None:
        continue
    ins, bd = L.dot_sets(U)
    if len(bd) < 3:
        continue
    p, q = rng.sample(bd, 2)
    chord = L.segment_dots(p, q)
    mids = [(F(a[0] + b[0], 2), F(a[1] + b[1], 2)) for a, b in zip(chord, chord[1:])]
    if not all(L.classify(U, z) == 'inside' for z in chord[1:-1] + mids):
        continue
    parts = split_along(U, p, q)
    if parts is None:
        continue
    P1, P2 = parts
    if len(P1) < 3 or len(P2) < 3:
        continue
    P1, P2 = drop_straight(P1), drop_straight(P2)
    if len(P1) < 3 or len(P2) < 3 or not L.is_simple(P1) or not L.is_simple(P2):
        continue
    if not L.meet_exactly(P1, P2, p, q):
        continue
    tested += 1
    k = len(L.segment_dots(p, q))
    I1, B1 = L.counts(P1)
    I2, B2 = L.counts(P2)
    I, B = L.counts(U)
    if not (I == I1 + I2 + k - 2 and B == B1 + B2 - 2 * k + 2 and
            L.Q2(I, B) == L.Q2(I1, B1) + L.Q2(I2, B2) and
            L.area_cells(U) == L.area_cells(P1) + L.area_cells(P2)):
        bad.append((U, p, q))
    if L.classify(U, p) != 'boundary' or L.classify(U, q) != 'boundary':
        endpoints_boundary = False
check(tested > 500 and not bad, 'P7: %d random legal joins; I=I1+I2+k-2, B=B1+B2-2k+2, Q and area add in all' % tested)
check(endpoints_boundary, 'P7 guide: both seam endpoints are boundary dots of the union in every test')
# Joins where the shared segment is a whole side of one piece only (triangle on part of a rectangle side)
ok = True
cnt = 0
for w in range(2, 7):
    for h in range(1, 4):
        Rr = [(0, 0), (w, 0), (w, h), (0, h)]
        for x1 in range(0, w):
            for x2 in range(x1 + 1, w + 1):
                if (x1, x2) == (0, w):
                    continue
                for ax in range(-2, w + 3):
                    for ay in range(h + 1, h + 4):
                        Tt = [(x1, h), (x2, h), (ax, ay)]
                        if not L.meet_exactly(Rr, Tt, (x1, h), (x2, h)):
                            continue
                        U = [(0, 0), (w, 0), (w, h)] + ([(x2, h)] if x2 != w else []) + [(ax, ay)] + \
                            ([(x1, h)] if x1 != 0 else []) + [(0, h)]
                        U = drop_straight(U)
                        if not L.is_simple(U):
                            continue
                        cnt += 1
                        k = len(L.segment_dots((x1, h), (x2, h)))
                        (I1, B1), (I2, B2), (I, B) = L.counts(Rr), L.counts(Tt), L.counts(U)
                        if not (I == I1 + I2 + k - 2 and B == B1 + B2 - 2 * k + 2):
                            ok = False
check(ok and cnt > 50, 'P7 other reading: a triangle joined on part of a rectangle side (%d cases) still obeys the formulas' % cnt)
check(rec([(0, 0), (2, 0), (0, 1)]) == (0, 4, 1) and rec([(2, 0), (2, 1), (0, 1)]) == (0, 4, 1)
      and len(L.segment_dots((2, 0), (0, 1))) == 2 and rec(rect21) == (0, 6, 2),
      'P7 guide k=2 edge case: two (0,4,1) triangles, diagonal with only its endpoints, rectangle (0,6,2)')
# Guide p.1 lists "several shared sides" among joins that "do not satisfy this claim".
# Test joins whose seam is a connected bent path of two sides.
NOTCH = [(0, 3), (4, 3), (2, 2)]
PENT = [(0, 0), (4, 0), (4, 3), (2, 2), (0, 3)]
RECT43 = [(0, 0), (4, 0), (4, 3), (0, 3)]
(I1, B1), (I2, B2), (I, B) = L.counts(PENT), L.counts(NOTCH), L.counts(RECT43)
k = 3  # seam path (0,3)-(2,2)-(4,3): dots (0,3), (2,2), (4,3)
check((I1, B1, I2, B2, I, B) == (5, 12, 0, 6, 6, 14) and I == I1 + I2 + k - 2 and B == B1 + B2 - 2 * k + 2
      and L.Q2(I, B) == L.Q2(I1, B1) + L.Q2(I2, B2),
      'bent seam: P8 pentagon (5,12) + notch (0,6) across the two-side seam (0,3)-(2,2)-(4,3) give the 4x3 '
      'rectangle (6,14); I=I1+I2+k-2, B=B1+B2-2k+2 with k=3, and Q: 10 + 2 = 12')


def path_meets_only(p1, p2, path):
    segs = list(zip(path, path[1:]))
    def on_path(z):
        return any(L.on_segment(z, a, b) for a, b in segs)
    for e in L.edges(p1):
        for f in L.edges(p2):
            r = L.seg_intersection(*e, *f)
            if r is None:
                continue
            pts = [r[1]] if r[0] == 'point' else [r[1], r[2]]
            if not all(on_path(z) for z in pts):
                return False
    return True


nb = 0
bent_ok = True
for trial in range(4000):
    U = random_simple(rng.randint(3, 8), rng.choice([5, 6, 7]))
    if U is None:
        continue
    ins, bd = L.dot_sets(U)
    if len(bd) < 2 or not ins:
        continue
    p, q = rng.sample(bd, 2)
    v = rng.choice(ins)
    if L.cross(p, v, q) == 0:
        continue
    # the seam must run through the inside of U except at its two ends
    dots_path = L.segment_dots(p, v) + L.segment_dots(v, q)[1:]
    mids = [(F(a[0] + b[0], 2), F(a[1] + b[1], 2)) for a, b in zip(dots_path, dots_path[1:])]
    if not all(L.classify(U, z) == 'inside' for z in dots_path[1:-1] + mids):
        continue
    parts = split_along(U, p, q)
    if parts is None:
        continue
    A1, A2 = parts
    P1 = drop_straight(A1 + [v])
    P2 = drop_straight(A2 + [v])
    if len(P1) < 3 or len(P2) < 3 or not L.is_simple(P1) or not L.is_simple(P2):
        continue
    if L.area_cells(P1) + L.area_cells(P2) != L.area_cells(U):
        continue
    path = [p, v, q]
    if not path_meets_only(P1, P2, path):
        continue
    nb += 1
    k = len(L.segment_dots(p, v)) + len(L.segment_dots(v, q)) - 1
    (I1, B1), (I2, B2), (I, B) = L.counts(P1), L.counts(P2), L.counts(U)
    if not (I == I1 + I2 + k - 2 and B == B1 + B2 - 2 * k + 2 and L.Q2(I, B) == L.Q2(I1, B1) + L.Q2(I2, B2)):
        if bent_ok:
            say('     bent-seam counterexample?', U, p, v, q, P1, P2, k, (I1, B1), (I2, B2), (I, B))
        bent_ok = False
check(bent_ok and nb > 200, 'bent seam: %d random joins along a connected two-side seam all obey I=I1+I2+k-2, '
      'B=B1+B2-2k+2 and Q=Q1+Q2 (k = dots on the whole seam), contrary to guide p.1' % nb)
# genuine limits: point contact and two separate shared pieces
Ta, Tb = [(0, 0), (2, 0), (1, 1)], [(1, 1), (2, 2), (0, 2)]
Ia, Ba = L.counts(Ta)
Ib, Bb = L.counts(Tb)
check(F(L.Q2(Ia + Ib, Ba + Bb - 1), 2) != L.area_cells(Ta) + L.area_cells(Tb),
      'guide limit: two triangles touching at one point: counting the pinched union gives Q = %s, area %s'
      % (F(L.Q2(Ia + Ib, Ba + Bb - 1), 2), L.area_cells(Ta) + L.area_cells(Tb)))

# ---------------------------------------------------------------- P8
say('== Problem 8')
T8 = [(0, 0), (4, 1), (1, 3)]
P8 = [(0, 0), (4, 0), (4, 3), (2, 2), (0, 3)]
check(rec(T8) == (5, 3, F(11, 2)) and L.dot_sets(T8)[0] == [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]
      and sorted(L.dot_sets(T8)[1]) == sorted(T8),
      'P8 triangle: (5,3,11/2), inside (1,1),(1,2),(2,1),(2,2),(3,1), boundary = the 3 corners')
comps = [[(0, 0), (4, 0), (4, 1)], [(4, 1), (4, 3), (1, 3)], [(1, 3), (0, 3), (0, 0)]]
check([L.area_shoelace(c) for c in comps] == [2, 3, F(3, 2)] and 12 - 2 - 3 - F(3, 2) == F(11, 2),
      'P8 guide: complements in the 4x3 box have areas 2, 3, 3/2; 12-2-3-3/2 = 11/2')
check(rec(P8) == (5, 12, 10) and L.dot_sets(P8)[0] == [(1, 1), (1, 2), (2, 1), (3, 1), (3, 2)]
      and (2, 2) in L.dot_sets(P8)[1] and L.is_simple(P8) and len(P8) == 5,
      'P8 pentagon: (5,12,10), inside (1,1),(1,2),(2,1),(3,1),(3,2); (2,2) boundary; 5 sides')
check(L.area_shoelace([(0, 3), (4, 3), (2, 2)]) == 2, 'P8 guide: notch area 2, 12 - 2 = 10')
# Step 1
ok = all(L.counts([(0, 0), (a, 0), (a, b), (0, b)]) == ((a - 1) * (b - 1), 2 * a + 2 * b) and
         (a - 1) * (b - 1) + a + b - 1 == a * b for a in range(1, 9) for b in range(1, 9))
check(ok, 'Step 1: a x b rectangles (a,b<=8): I=(a-1)(b-1), B=2a+2b, Q=ab')
# Step 2
ok = True
for a in range(1, 9):
    for b in range(1, 9):
        t1, t2 = [(0, 0), (a, 0), (0, b)], [(a, 0), (a, b), (0, b)]
        c1, c2 = L.counts(t1), L.counts(t2)
        if c1 != c2 or L.Q2(*c1) != a * b or sorted((a - x, b - y) for x, y in t1) != sorted(t2):
            ok = False
        if not L.meet_exactly(t1, t2, (a, 0), (0, b)):
            ok = False
check(ok, 'Step 2: both diagonal halves have equal counts, swap under (x,y)->(a-x,b-y), meet exactly on the diagonal; 2Q=ab')


# Step 3
def axis_right(t):
    if len(t) != 3 or L.area2_signed(t) == 0:
        return False
    for i in range(3):
        o, p, q = t[i], t[(i + 1) % 3], t[(i + 2) % 3]
        v1, v2 = (p[0] - o[0], p[1] - o[1]), (q[0] - o[0], q[1] - o[1])
        if v1[0] * v2[0] + v1[1] * v2[1] == 0 and (v1[0] == 0 or v1[1] == 0) and (v2[0] == 0 or v2[1] == 0):
            return True
    return False


def step3_pieces(x1, x2, y0, px, py):
    """Guide's complement pieces and attachment order for base (x1,y0)-(x2,y0), apex (px,py), py>y0."""
    lo, hi = min(x1, px), max(x2, px)
    if x1 <= px <= x2:
        pieces = []
        if px > x1:
            pieces.append(([(x1, y0), (px, py), (x1, py)], ((x1, y0), (px, py))))
        if px < x2:
            pieces.append(([(x2, y0), (x2, py), (px, py)], ((x2, y0), (px, py))))
    elif px > x2:
        pieces = [([(x2, y0), (px, y0), (px, py)], ((x2, y0), (px, py))),      # small wedge, shorter slope
                  ([(x1, y0), (px, py), (x1, py)], ((x1, y0), (px, py)))]
    else:  # px < x1: mirror image of the px > x2 case
        pieces = [([(px, y0), (x1, y0), (px, py)], ((x1, y0), (px, py))),      # small wedge, shorter slope
                  ([(x2, y0), (x2, py), (px, py)], ((x2, y0), (px, py)))]
    return pieces, [(lo, y0), (hi, y0), (hi, py), (lo, py)]


def union_poly(P, piece, seam):
    """Splice piece into P along seam (a full side of both)."""
    a, b = seam
    n = len(P)
    for i in range(n):
        if {P[i], P[(i + 1) % n]} == {a, b}:
            extra = [v for v in piece if v not in (a, b)][0]
            return drop_straight(P[:i + 1] + [extra] + P[i + 1:])
    return None


def step3_ok(x1, x2, y0, px, py, reverse=False):
    T = [(x1, y0), (x2, y0), (px, py)]
    pieces, R = step3_pieces(x1, x2, y0, px, py)
    if reverse:
        pieces = pieces[::-1]
    if len(pieces) > 2 or not all(axis_right(p) for p, _ in pieces):
        return False
    cur = T
    for piece, seam in pieces:
        if not L.meet_exactly(cur, piece, *seam):
            return False
        nxt = union_poly(cur, piece, seam)
        if nxt is None or not L.is_simple(nxt):
            return False
        if L.area_shoelace(nxt) != L.area_shoelace(cur) + L.area_shoelace(piece):
            return False
        cur = nxt
    return sorted(drop_straight(cur)) == sorted(R)


ok = rev_ok = True
n3 = 0
for x1 in range(0, 7):
    for x2 in range(x1 + 1, 8):
        for px in range(-1, 9):
            for py in range(1, 6):
                n3 += 1
                ok &= step3_ok(x1, x2, 0, px, py)
                rev_ok &= step3_ok(x1, x2, 0, px, py, reverse=True)
check(ok, 'Step 3: %d horizontal-base triangles: at most two axis-right complement pieces, each attachment meets exactly in one full side, unions simple, final union = bounding rectangle' % n3)
say('     Step 3 note: the opposite attachment order is %s' % ('also legal in every case' if rev_ok else 'illegal in some case'))


# Step 4
def step4(A, Bv, C):
    xs = sorted([A, Bv, C])
    A, Bv, C = xs
    if len({A[0], Bv[0], C[0]}) < 3 or A[1] == C[1]:
        return 'axis'
    # height of AC at Bx
    h = A[1] + F(Bv[0] - A[0]) * (C[1] - A[1]) / (C[0] - A[0])
    assert min(A[1], C[1]) < h < max(A[1], C[1])
    D1, D2 = (Bv[0], A[1]), (Bv[0], C[1])
    s1, s2, sB = L.cross(A, C, D1), L.cross(A, C, D2), L.cross(A, C, Bv)
    assert s1 * s2 < 0 and sB != 0
    D = D1 if s1 * sB < 0 else D2
    Q = [A, Bv, C, D]
    sg = [L.cross(Q[i], Q[(i + 1) % 4], Q[(i + 2) % 4]) for i in range(4)]
    convex = all(s > 0 for s in sg) or all(s < 0 for s in sg)
    ABD, BCD, ACD, ABC = [A, Bv, D], [Bv, C, D], [A, C, D], [A, Bv, C]
    vert = lambda t: any(p[0] == q[0] for p, q in L.edges(t))  # noqa: E731
    horiz = lambda t: any(p[1] == q[1] for p, q in L.edges(t))  # noqa: E731
    legal = L.meet_exactly(ABC, ACD, A, C) and L.meet_exactly(ABD, BCD, Bv, D)
    q_ok = all(F(L.Q2(*L.counts(t)), 2) == L.area_cells(t) for t in (ABC, ACD, ABD, BCD, Q))
    return convex and vert(ABD) and vert(BCD) and horiz(ACD) and legal and q_ok and \
        L.Q2(*L.counts(ABC)) + L.Q2(*L.counts(ACD)) == L.Q2(*L.counts(Q)) == L.Q2(*L.counts(ABD)) + L.Q2(*L.counts(BCD))


for size in (5, 6):
    pts = [(x, y) for x in range(size) for y in range(size)]
    tri_all = [t for t in itertools.combinations(pts, 3) if L.area2_signed(list(t)) != 0]
    res = [step4(*t) for t in tri_all]
    n_axis = sum(1 for r in res if r == 'axis')
    n_bridge = sum(1 for r in res if r is True)
    n_fail = sum(1 for r in res if r is False)
    check(n_fail == 0, 'Step 4 on %dx%d dots: %d noncollinear triangles, %d sent to Step 3 by the guide\'s two tests, %d through the bridge, %d failures'
          % (size, size, len(tri_all), n_axis, n_bridge, n_fail))
    if size == 5:
        n_any_axis = sum(1 for t in tri_all if any(p[0] == q[0] or p[1] == q[1] for p, q in itertools.combinations(t, 2)))
        check(len(tri_all) == 2148, 'guide p.8: 2,148 noncollinear triangles on a 5x5-dot board')
        check((n_any_axis, len(tri_all) - n_any_axis) == (1600, 548),
              'source README split: %d have some axis side, %d have none (the guide routes %d through the bridge, '
              'since Step 4 sends a triangle with a horizontal side AB or BC to the bridge; it still works)'
              % (n_any_axis, len(tri_all) - n_any_axis, n_bridge))
ex = {'ABC': [(0, 0), (2, 1), (6, 6)], 'ACD': [(0, 0), (6, 6), (2, 6)], 'ABD': [(0, 0), (2, 1), (2, 6)],
      'BCD': [(2, 1), (6, 6), (2, 6)], 'ABCD': [(0, 0), (2, 1), (6, 6), (2, 6)]}
table = {'ABC': (0, 8, 3), 'ACD': (7, 12, 12), 'ABD': (2, 8, 5), 'BCD': (6, 10, 10), 'ABCD': (12, 8, 15)}
for k, poly in ex.items():
    check(rec(poly) == table[k], 'Step 4 example %s: %s (guide table %s)' % (k, rec(poly), table[k]))
check(L.cross((0, 0), (6, 6), (2, 1)) * L.cross((0, 0), (6, 6), (2, 6)) < 0 and step4((0, 0), (2, 1), (6, 6)) is True,
      'Step 4 example: D=(2,6) is the choice opposite B, and the bridge works')
# complement of ABC in its bounding box contains a quadrilateral
check(L.classify([(0, 0), (6, 0), (6, 6), (0, 6)], (2, 1)) == 'inside',
      'Step 4 example: B=(2,1) is interior to the bounding square, so the complement of ABC is a right triangle and the quadrilateral (0,0),(6,0),(6,6),(2,1)')


# Step 5: ears
def find_ear(P):
    n = len(P)
    for i in range(n):
        a, v, b = P[i - 1], P[i], P[(i + 1) % n]
        if L.cross(a, v, b) == 0:
            continue
        rest = [P[j] for j in range(n) if j != i]
        ear = [a, v, b]
        if L.is_simple(rest) and L.area2_signed(ear) != 0 and L.meet_exactly(ear, rest, a, b) \
                and L.area_shoelace(rest) + L.area_shoelace(ear) == L.area_shoelace(P):
            return ear, rest
    return None


ok = True
npoly = 0
for trial in range(1500):
    P = random_simple(rng.randint(4, 9), rng.choice([4, 5, 6, 7]))
    if P is None:
        continue
    P = drop_straight(P)
    if len(P) < 4 or not L.is_simple(P):
        continue
    npoly += 1
    I, B = L.counts(P)
    if pick(I, B) != L.area_cells(P):
        ok = False
    e = find_ear(P)
    if e is None:
        ok = False
        continue
    ear, rest = e
    k = len(L.segment_dots(ear[0], ear[2]))
    (I1, B1), (I2, B2) = L.counts(ear), L.counts(rest)
    if not (I == I1 + I2 + k - 2 and B == B1 + B2 - 2 * k + 2):
        ok = False
check(ok and npoly > 500, 'Step 5: %d random simple polygons: an ear whose diagonal is a legal join always exists; Pick holds' % npoly)
# all simple quadrilaterals and pentagon sample on 5x5: Pick
ok = all(pick(*L.counts(q)) == L.area_cells(q) for q in simple_quads(G4))
check(ok, 'Pick holds for every simple quadrilateral on the 5x5-dot board')
check(all(F(abs(L.area2_signed(list(t))), 2).denominator in (1, 2) for t in itertools.combinations(G4, 3)) and
      all(L.area_shoelace([(0, 0), (n, 0), (0, 1)]) == F(n, 2) for n in range(1, 20)),
      'guide p.1: lattice areas are multiples of 1/2 and every positive multiple occurs')

# ---------------------------------------------------------------- holes
say('== Problems 9-10: holes')
O9, H9 = [(0, 0), (4, 0), (4, 4), (0, 4)], [(1, 1), (3, 1), (3, 3), (1, 3)]
r9 = rec(O9, [H9])
check(r9 == (0, 24, 12), 'P9 ring: (I,B,A) = %s, guide (0,24,12)' % (r9,))
check(pick(0, 24) == 11 and pick(0, 24, 1) == 12, 'P9 guide: old expression 11, one-hole rule gives 12 (A = I + B/2)')
check(L.classify(H9, (2, 2)) == 'inside' and sorted(L.dot_sets(H9)[1]) == sorted(set(L.dot_sets(H9)[1])) and len(L.dot_sets(H9)[1]) == 8,
      'P9 guide: centre (2,2) removed, 8 hole-side dots')
O9b, H9b = [(0, 0), (6, 0), (6, 3), (0, 3)], [(1, 1), (2, 1), (2, 2), (1, 2)]
check(rec(O9b, [H9b]) == (6, 22, 17) and L.counts(O9b) == (10, 18) and L.counts(H9b) == (0, 4) and fits(O9b, 6, 3),
      'P9 guide second test: region (6,22,17); filled outer (10,18); hole (0,4); fits the 6x3 board')
O10 = [(0, 0), (6, 0), (6, 4), (0, 4)]
H10 = [[(1, 1), (2, 1), (2, 2), (1, 2)], [(4, 1), (5, 1), (5, 2), (4, 2)]]
check(rec(O10, H10) == (7, 28, 22) and L.counts(O10) == (15, 20) and pick(7, 28) == 20 and pick(7, 28, 2) == 22,
      'P10 guide witness: (7,28,22); filled (15,20); old expression 20, +2 = 22')
# random h-hole tests, with pairwise disjoint closures strictly inside
ok = True
nh = 0
for trial in range(400):
    W, Hh = rng.randint(5, 9), rng.randint(4, 8)
    outer = [(0, 0), (W, 0), (W, Hh), (0, Hh)]
    holes = []
    for _ in range(rng.randint(1, 3)):
        for _ in range(30):
            hp = random_simple(rng.randint(3, 5), 3)
            if hp is None:
                continue
            dx, dy = rng.randint(1, W - 4), rng.randint(1, Hh - 4) if Hh > 4 else 1
            hp = [(x + dx, y + dy) for x, y in hp]
            if not all(L.classify(outer, p) == 'inside' for p in hp) or max(x for x, _ in hp) >= W or max(y for _, y in hp) >= Hh:
                continue
            clash = False
            for h0 in holes:
                for e in L.edges(hp):
                    for f in L.edges(h0):
                        if L.seg_intersection(*e, *f):
                            clash = True
                if any(L.classify(h0, p) != 'outside' for p in hp) or any(L.classify(hp, p) != 'outside' for p in h0):
                    clash = True
            if not clash:
                holes.append(hp)
                break
    if not holes:
        continue
    nh += 1
    I, B = L.counts(outer, holes)
    Io, Bo = L.counts(outer)
    sub_I = Io - sum(sum(L.counts(h)) for h in holes)
    sub_B = Bo + sum(L.counts(h)[1] for h in holes)
    if not (I == sub_I and B == sub_B and pick(I, B, len(holes)) == L.area_cells(outer, holes)):
        ok = False
check(ok and nh > 300, 'h-hole rule: %d random regions with 1-3 separate holes: I = Io - sum(Ij+Bj), B = Bo + sum Bj, A = I + B/2 - 1 + h' % nh)
# guide's stated limit: touching holes break the rule
Ot = [(0, 0), (4, 0), (4, 4), (0, 4)]
Ht = [[(1, 1), (2, 1), (2, 2), (1, 2)], [(2, 2), (3, 2), (3, 3), (2, 3)]]
It, Bt = L.counts(Ot, Ht)
say('     limit check: holes touching at (2,2): I=%d, B=%d, area %s, rule gives %s (so separation is needed)'
    % (It, Bt, L.area_cells(Ot, Ht), pick(It, Bt, 2)))
check(pick(It, Bt, 2) != L.area_cells(Ot, Ht), 'guide limit: holes whose closures touch are correctly excluded')

# ---------------------------------------------------------------- preparation arithmetic (guide p. 2)
say('== Guide p. 2 arithmetic')
check(12 + 10 + 10 + 10 + 6 + 3 == 51, '51 student sheets: 12+10+10+10+6+3')
check(6 + 3 + 3 + 6 + 7 == 25 and 5 + 2 == 7, '25-sheet option: 6+3+3+6+7, and 7 = 5 kits + 2 younger pairs')
check(5 * 10 + 10 == 60 and 5 * 20 + 20 == 120 and 60 * 2 == 120 and 60 + 60 == 120, 'pieces: 60 squares, 120 halves, 120 raw squares')
check((5 * 1 + 1, 5 * 2 + 2, 5 * 1 + 1, 5 * 2 + 2) == (6, 12, 6, 12), 'drawing kit totals 6, 12, 6, 12')
check(2 * 2 + 4 + 3 == 11, 'tables KK11, 3333, 445: 11 children')
check(abs(2 * 215.9 / 10 - 43.2) < 0.1 and 279.4 / 10 < 30, 'two letter sheets side by side: 43.2 x 27.9 cm (about 45 x 30)')

# ---------------------------------------------------------------- guide text read-back
say('== Guide text read back from the delivered PDF')
for s in ['(0, 12, 5)', '(3, 5, 9/2)', '(1, 8, 4)', '(2, 6, 4)', '(0, 14), (1, 12), (2, 10), (3, 8), (4, 6), (5, 4)',
          '24/5 + 3/5 + 3/5 = 6', 'I = 1 + 1 + 1 = 3, B = 8 + 8 − 6 + 2 = 12', 'I = 1 + 1 + 2 = 4,',
          'B = 6 + 6 − 8 + 2 = 6', '(I, B, A) = (5, 3, 11/2)', '(I, B, A) = (5, 12, 10)',
          'Area 16 − 4 = 12, I = 0, B = 16 + 8 = 24', 'Independent area 18 − 1 = 17', 'I_o = 10', 'Independent area is 24 − 1 − 1 = 22',
          '3 + 12 = 5 + 10 = 15', '51 Week 57 student sheets', '25 sheets', '2,148']:
    s2 = s.replace('I_o = 10', 'Io = 10')
    check(in_guide(s2) or in_guide(s), 'guide PDF prints "%s"' % s)

say('')
say('%d checks, %d failures' % (sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))), len(FAIL)))
open(os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
