#!/usr/bin/env python3
"""Independent math-stage check of Week 71 "Can you hear the room?".

Written from scratch for the review; it does not import or trust the packet's
own checkers.  Run from anywhere:  python3 check_week71.py
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, sqrt, atan2, degrees, hypot
import itertools, random

REPO = Path(__file__).resolve().parents[4]
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-71'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-71'
STUDENT_PDF = WEEK / 'week-71-students.pdf'

out = []
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)

# ---------------------------------------------------------------- rectangles
def rect_fold(W, H, p, d, n):
    """Folded billiard in [0,W]x[0,H]; A bottom, B left, C top, D right.
    Returns (word, list of unfolded hit points) or None on a corner hit."""
    x, y = map(F, p); u, v = map(F, d)
    sx = sy = 1                      # unfolding signs
    ox, oy = F(0), F(0)              # unfolded position of the current point
    X, Y = F(p[0]), F(p[1])
    word, pts = [], []
    while len(word) < n:
        ts = []
        if u > 0: ts.append(((W - x) / u, 'D'))
        if u < 0: ts.append((-x / u, 'B'))
        if v > 0: ts.append(((H - y) / v, 'C'))
        if v < 0: ts.append((-y / v, 'A'))
        t = min(tt for tt, _ in ts)
        hits = [l for tt, l in ts if tt == t]
        if len(hits) > 1:
            return None
        x += t * u; y += t * v
        X += t * u * sx; Y += t * v * sy
        word.append(hits[0]); pts.append((X, Y))
        if hits[0] in 'BD': u = -u; sx = -sx
        else: v = -v; sy = -sy
    return ''.join(word), pts

def unfolded_label(X, Y, W, H):
    """Label of the grid line through an unfolded crossing point."""
    on_v = X % W == 0; on_h = Y % H == 0
    if on_v and on_h: return None
    if on_v: return 'B' if (X // W) % 2 == 0 else 'D'
    return 'A' if (Y // H) % 2 == 0 else 'C'

def rect_valid(w):
    """Necessary condition for a rectangle word: wall letters of each
    direction alternate (H: A/C, V: B/D)."""
    h = [c for c in w if c in 'AC']; v = [c for c in w if c in 'BD']
    return all(a != b for a, b in zip(h, h[1:])) and all(a != b for a, b in zip(v, v[1:]))

def dirs(N):
    for u in range(-N, N + 1):
        for v in range(-N, N + 1):
            if (u or v) and gcd(abs(u), abs(v)) == 1:
                yield u, v

say('== Page 1 worked AD example (side-4 square, start (1,2) toward (3,0)) ==')
w, pts = rect_fold(4, 4, (1, 2), (1, -1), 2)
say('word', w, 'unfolded hits', [(str(a), str(b)) for a, b in pts])
assert w == 'AD' and pts == [(3, 0), (4, -1)]
# folded second hit is (4,1): the guide's "then to (4,1) on D"
assert (F(3) + 1, F(0) + 1) == (4, 1)

say('\n== Problem 1: three-letter words from the dot (1,1) in the 5x5-cell window [-4,6]^2 ==')
words1 = {}
for d in dirs(14):
    r = rect_fold(2, 2, (1, 1), d, 3)
    if not r: continue
    w, pts = r
    if all(-4 <= a <= 6 and -4 <= b <= 6 for a, b in pts):
        for (a, b), c in zip(pts, w):
            assert unfolded_label(a, b, 2, 2) == c
        words1.setdefault(w, d)
valid3 = [''.join(p) for p in itertools.product('ABCD', repeat=3)
          if all(a != b for a, b in zip(p, p[1:])) and rect_valid(''.join(p))]
say('distinct words reachable in window:', len(words1), '; alternation-valid 3-words:', len(valid3))
say('missing from window:', sorted(set(valid3) - set(words1)))
assert set(words1) <= set(valid3)

say('\nGuide Problem 1 table:')
table = [((3, 2), 'DCB', (4, 3)), ((2, 3), 'CDA', (3, 4)), ((-3, 2), 'BCD', (-2, 3)),
         ((-2, 3), 'CBA', (-1, 4)), ((-3, -2), 'BAD', (-2, -1)), ((-2, -3), 'ABC', (-1, -2))]
for d, w, third in table:
    r = rect_fold(2, 2, (1, 1), d, 3)
    ok = r is not None and r[0] == w and r[1][2] == third and all(-4 <= a <= 6 and -4 <= b <= 6 for a, b in r[1])
    say(' ', d, w, third, 'OK' if ok else 'MISMATCH', r and [(str(a), str(b)) for a, b in r[1]])
    assert ok

say('\n== PDF label check: page-1 and page-4 tracing windows vs true unfolding labels ==')
import pymupdf
doc = pymupdf.open(STUDENT_PDF)
def check_window(page, origin, xunit, yunit, lo, hi, name):
    """origin = PDF point of unfolded (0,0); units = PDF points per room-side/2."""
    bad = n = 0
    for x0, y0, x1, y1, word, *_ in doc[page].get_text('words'):
        if word not in 'ABCD' or len(word) != 1: continue
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        X = (cx - origin[0]) / xunit; Y = (origin[1] - cy) / yunit
        if not (lo - .3 <= X <= hi + .3 and lo - .3 <= Y <= hi + .3): continue
        # snap to the nearest grid line (even coordinate) on the label's axis
        ex, ey = abs(X - 2 * round(X / 2)), abs(Y - 2 * round(Y / 2))
        if ex < .2 and ey > .5:
            truth = 'B' if round(X / 2) % 2 == 0 else 'D'
        elif ey < .2 and ex > .5:
            truth = 'A' if round(Y / 2) % 2 == 0 else 'C'
        else:
            continue
        n += 1
        if truth != word:
            bad += 1; say('  WRONG label', word, 'at', round(X, 2), round(Y, 2), 'should be', truth)
    say(f'  {name}: {n} wall labels checked, {bad} wrong')
    assert bad == 0 and n > 0
cell = 56.6929                       # 2 cm in PDF points
check_window(0, (277.54, 485.85), cell / 2, cell / 2, -4, 6, 'page 1 window')
check_window(3, (277.77, 238.86), cell / 2, cell / 2, -2, 4, 'page 4 square window')
check_window(3, (249.42, 440.28), cell, cell / 2, -2, 4, 'page 4 wide window (x stretched 2x)')

say('\n== Problem 4: guide examples and availability in page-4 windows ==')
for d, w, third in table[:3]:
    r = rect_fold(2, 2, (1, 1), d, 3)
    sq_ok = all(-2 <= a <= 4 and -2 <= b <= 4 for a, b in r[1])
    r2 = rect_fold(4, 2, (2, 1), (2 * d[0], d[1]), 3)
    re_ok = r2[0] == w and all(-4 <= a <= 8 and -2 <= b <= 4 for a, b in r2[1])
    mixed = set(w) & set('AC') and set(w) & set('BD')
    say(' ', w, 'square hits', [(str(a), str(b)) for a, b in r[1]], 'rect hits',
        [(str(a), str(b)) for a, b in r2[1]], 'in windows' if sq_ok and re_ok else 'OUTSIDE', 'mixed' if mixed else 'NOT MIXED')
    assert sq_ok and re_ok and mixed and r2[1][2] == (2 * third[0], third[1])
words4 = set()
starts = [(F(i, 7), F(j, 7)) for i in range(1, 14) for j in range(1, 14)]
for s in starts:
    for d in dirs(7):
        r = rect_fold(2, 2, s, d, 4)
        if not r: continue
        w, pts = r
        for k in (3, 4):
            if all(-2 <= a <= 4 and -2 <= b <= 4 for a, b in pts[:k]):
                ww = w[:k]
                if set(ww) & set('AC') and set(ww) & set('BD'):
                    words4.add(ww)
say('  distinct mixed words (length 3-4) drawable in the page-4 square window:', len(words4))

say('\n== Problem 4 / overview: stretch transfer, exact, 12 bounces ==')
rng = random.Random(71)
agree = tried = 0
for _ in range(3000):
    s = (F(rng.randint(1, 199), 100), F(rng.randint(1, 199), 100))
    d = (rng.randint(-40, 40), rng.randint(-40, 40))
    if d == (0, 0): continue
    a = rect_fold(2, 2, s, d, 12)
    al, be = F(rng.randint(1, 9), rng.randint(1, 9)), F(rng.randint(1, 9), rng.randint(1, 9))
    b = rect_fold(2 * al, 2 * be, (s[0] * al, s[1] * be), (d[0] * al, d[1] * be), 12)
    tried += 1
    if (a is None) == (b is None) and (a is None or a[0] == b[0]):
        agree += 1
say(f'  {agree}/{tried} random rays give identical words (or both corner) after an (alpha,beta) stretch')
assert agree == tried

say('\n== Problem 2 square: ABA as a subword in rectangles ==')
cnt = 0
for _ in range(3000):
    W, H = F(rng.randint(1, 30), 7), F(rng.randint(1, 30), 7)
    s = (W * F(rng.randint(1, 99), 100), H * F(rng.randint(1, 99), 100))
    d = (rng.randint(-30, 30), rng.randint(-30, 30))
    if d == (0, 0): continue
    r = rect_fold(W, H, s, d, 15)
    if r:
        cnt += 1
        assert rect_valid(r[0]), r
say(f'  {cnt} random rectangle rays of 15 bounces: none breaks A/C and B/D alternation (so no ABA)')

# ------------------------------------------------------------ Q(sqrt3) exact
class Q3:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = F(a); s.b = F(b)
    def __add__(s, o): o = q(o); return Q3(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = q(o); return Q3(s.a - o.a, s.b - o.b)
    def __rsub__(s, o): return q(o) - s
    def __neg__(s): return Q3(-s.a, -s.b)
    def __mul__(s, o): o = q(o); return Q3(s.a * o.a + 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = q(o); n = o.a * o.a - 3 * o.b * o.b
        return s * Q3(o.a / n, -o.b / n)
    def sign(s):
        a, b = s.a, s.b
        if a >= 0 and b >= 0: return 0 if a == 0 and b == 0 else 1
        if a <= 0 and b <= 0: return -1
        c = a * a - 3 * b * b
        return (1 if a > 0 else -1) if c > 0 else ((1 if b > 0 else -1) if c < 0 else 0)
    def __eq__(s, o): o = q(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __float__(s): return float(s.a) + float(s.b) * sqrt(3)
    def __repr__(s): return f'{s.a}+{s.b}r3' if s.b else f'{s.a}'
def q(x): return x if isinstance(x, Q3) else Q3(x)
R3 = Q3(0, 1)

def reflect_pt(p, a, b):
    ex, ey = b[0] - a[0], b[1] - a[1]
    qx, qy = p[0] - a[0], p[1] - a[1]
    t = (qx * ex + qy * ey) / (ex * ex + ey * ey)
    return (a[0] + 2 * t * ex - qx, a[1] + 2 * t * ey - qy)

def reflect_vec(d, e):
    t = (d[0] * e[0] + d[1] * e[1]) / (e[0] * e[0] + e[1] * e[1])
    return (2 * t * e[0] - d[0], 2 * t * e[1] - d[1])

def cross(a, b): return a[0] * b[1] - a[1] * b[0]

def poly_fold(P, labels, p, d, n):
    """Exact folded billiard in convex polygon P (vertices CCW).
    Returns list of (label, point) or None on a corner hit."""
    res = []
    for _ in range(n):
        best = None
        for i in range(len(P)):
            a, b = P[i], P[(i + 1) % len(P)]
            e = (b[0] - a[0], b[1] - a[1])
            den = cross(d, e)
            if den.sign() == 0: continue
            w = (a[0] - p[0], a[1] - p[1])
            t = cross(w, e) / den; s = cross(w, d) / den
            if t.sign() <= 0: continue
            if s.sign() < 0 or (s - 1).sign() > 0: continue
            if best is None or (t - best[0]).sign() < 0: best = (t, s, i, e)
        t, s, i, e = best
        if s.sign() == 0 or (s - 1).sign() == 0: return None
        p = (p[0] + t * d[0], p[1] + t * d[1])
        res.append((labels[i], p))
        d = reflect_vec(d, e)
    return res

say('\n== Problem 2 rhombus: exact Q(sqrt3) checks ==')
RH = [(Q3(0), Q3(0)), (Q3(4), Q3(0)), (Q3(6), 2 * R3), (Q3(2), 2 * R3)]
LAB = ['A', 'D', 'C', 'B']          # edges 0..3: bottom, right, top, left
for i in range(4):
    a, b = RH[i], RH[(i + 1) % 4]
    L2 = (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])
    assert L2 == 16
start = (F(11, 4) * Q3(1), R3 * F(1, 4))
d0 = ((Q3(2) - start[0]), (Q3(0) - start[1]))
hits = poly_fold(RH, LAB, start, d0, 3)
say('  folded hits from (11/4, sqrt3/4):', [(l, (repr(x), repr(y))) for l, (x, y) in hits])
assert [h[0] for h in hits] == ['A', 'B', 'A']
assert hits[0][1] == (Q3(2), Q3(0)) and hits[1][1] == (Q3(F(1, 2)), R3 * F(1, 2)) and hits[2][1] == (Q3(2), Q3(0))
# start strictly inside
for i in range(4):
    a, b = RH[i], RH[(i + 1) % 4]
    assert cross((b[0] - a[0], b[1] - a[1]), (start[0] - a[0], start[1] - a[1])).sign() > 0

# unfolded chain exactly as windows.tex builds it: reflect across edge 0, then 3, then 0
faces = [RH]
for j in (0, 3, 0):
    old = faces[-1]
    faces.append([reflect_pt(p, old[j], old[(j + 1) % 4]) for p in old])
say('  unfolded faces:', [[(repr(x), repr(y)) for x, y in f] for f in faces])
# compare with windows.tex coordinates
import re
tex = (SRC / 'student' / 'windows.tex').read_text()
rh_block = tex[tex.index('rhombusABA'):]
fills = re.findall(r'\\fill\[gray!\d+\] (.*?)--cycle;', rh_block)[:4]
for f, face in zip(fills, faces):
    nums = [tuple(map(float, m)) for m in re.findall(r'\(([-\d.]+),([-\d.]+)\)', f)]
    assert all(abs(x - float(X)) < 1e-6 and abs(y - float(Y)) < 1e-6 for (x, y), (X, Y) in zip(nums, face)), (nums, face)
say('  windows.tex rhombus faces match exact reflections')
# straight unfolded line from start through (2,0)
seq = [(faces[0][0], faces[0][1]), (faces[1][3], faces[1][0]), (faces[2][0], faces[2][1])]
p, d = start, d0
for (a, b), want in zip(seq, [(Q3(2), Q3(0)), (Q3(F(1, 2)), -R3 * F(1, 2)), (Q3(-1), -R3)]):
    e = (b[0] - a[0], b[1] - a[1]); w = (a[0] - p[0], a[1] - p[1]); den = cross(d, e)
    t = cross(w, e) / den; s = cross(w, d) / den
    pt = (p[0] + t * d[0], p[1] + t * d[1])
    assert pt == want and s.sign() > 0 and (s - 1).sign() < 0, (pt, s)
say('  unfolded straight line meets (2,0), (1/2,-sqrt3/2), (-1,-sqrt3), each strictly inside its segment')

# ---------------------------------------------------------------- float sampling
def fl(P): return [(float(x), float(y)) for x, y in P]
def float_fold(P, labels, p, d, n, eps=1e-7):
    res = []
    for _ in range(n):
        best = None
        for i in range(len(P)):
            a, b = P[i], P[(i + 1) % len(P)]
            e = (b[0] - a[0], b[1] - a[1]); den = d[0] * e[1] - d[1] * e[0]
            if abs(den) < 1e-14: continue
            w = (a[0] - p[0], a[1] - p[1])
            t = (w[0] * e[1] - w[1] * e[0]) / den; s = (w[0] * d[1] - w[1] * d[0]) / den
            if t <= 1e-12 or s < -1e-9 or s > 1 + 1e-9: continue
            if best is None or t < best[0]: best = (t, s, i, e)
        if best is None: return None
        t, s, i, e = best
        if s < 1e-4 or s > 1 - 1e-4: return None       # near a corner: discard
        p = (p[0] + t * d[0], p[1] + t * d[1])
        res.append(labels[i])
        L = e[0] ** 2 + e[1] ** 2; k = (d[0] * e[0] + d[1] * e[1]) / L
        d = (2 * k * e[0] - d[0], 2 * k * e[1] - d[1])
    return ''.join(res)

def inside(P, x, y):
    return all((P[(i + 1) % 4][0] - P[i][0]) * (y - P[i][1]) - (P[(i + 1) % 4][1] - P[i][1]) * (x - P[i][0]) > 0 for i in range(4))

def sample_words(P, labels, n, trials, seed):
    r = random.Random(seed); xs = [p[0] for p in P]; ys = [p[1] for p in P]
    found = set()
    for _ in range(trials):
        while True:
            x = r.uniform(min(xs), max(xs)); y = r.uniform(min(ys), max(ys))
            if inside(P, x, y): break
        th = r.uniform(0, 6.283185307179586)
        w = float_fold(P, labels, (x, y), (__import__('math').cos(th), __import__('math').sin(th)), n)
        if w: found.add(w)
    return found

say('\n== Problem 3 context: sampled word sets (evidence only, not proofs) ==')
SQ = [(0, 0), (4, 0), (4, 4), (0, 4)]
RHf = fl(RH)
for n in (3, 4):
    sq = sample_words(SQ, LAB, n, 200000, 1)
    rh = sample_words(RHf, LAB, n, 200000, 2)
    say(f'  length {n}: square {len(sq)} words, rhombus {len(rh)} words')
    say('    rhombus-only:', sorted(rh - sq))
    say('    square-only (not found in rhombus sample):', sorted(sq - rh))
    if n == 3:
        assert len(sq) == len(valid3) and sq == set(valid3)

say('\n== Problem 3: rectangle words that the 60-degree rhombus cannot make ==')
# Square witnesses from the page-1 dot for the four HHV/VVH members of the ACB orbit
for w, d in (('ACB', (-1, -4)), ('CAD', (1, 4)), ('BDA', (-4, -1)), ('DBC', (4, 1))):
    r = rect_fold(2, 2, (1, 1), d, 3)
    assert r and r[0] == w and all(-4 <= a <= 6 and -4 <= b <= 6 for a, b in r[1])
    say(f'  square {w}: from the dot, direction {d}, unfolded hits', [(str(a), str(b)) for a, b in r[1]])
# Rhombus: unfold across C.  The copy's image of B is the segment (2,2r3)-(0,4r3).
# A line from (x0,0), 0<x0<4, through (x1,2r3), 2<x1<6, meets it at height y in (2r3,4r3)
# iff x1-2 = lam*(x0-x1-2) with lam=(y-2r3)/(2r3) in (0,1)  =>  x1 < x0/2 < 2: impossible.
r3 = sqrt(3); viol = 0
for i in range(1, 400):
    x0 = 4 * i / 400
    for j in range(1, 400):
        x1 = 2 + 4 * j / 400
        dx = x1 - x0                      # direction (dx, 2r3)
        # intersect with line through (2,2r3) direction (-1, r3)
        den = dx * r3 - 2 * r3 * (-1)
        if abs(den) < 1e-12: continue
        # solve (x0,0)+t(dx,2r3) = (2,2r3)+u(-1,r3)
        t = ((2 - x0) * r3 - (2 * r3) * (-1)) / den
        u = ((2 - x0) * 2 * r3 - (2 * r3) * dx) / den
        if t > 1 and 0 < u < 2: viol += 1
say(f'  ACB in rhombus: grid of 399x399 A-to-C segments, continuations meeting the B image: {viol}')
assert viol == 0
say('\n== Problem 2 unfolded chains: fraction of random straight lines doing A,B,A ==')
def chain_hits(faces_f, seq_idx, trials, seed):
    r = random.Random(seed); P0 = faces_f[0]; good = 0
    xs = [p[0] for p in P0]; ys = [p[1] for p in P0]
    for _ in range(trials):
        while True:
            x = r.uniform(min(xs), max(xs)); y = r.uniform(min(ys), max(ys))
            if inside(P0, x, y): break
        th = r.uniform(0, 6.283185307179586)
        import math
        d = (math.cos(th), math.sin(th)); p = (x, y); ok = True
        for k, (fi, j) in enumerate(seq_idx):
            # the straight line must leave face k through its edge j (the labelled seam)
            F_ = faces_f[fi]; best = None
            for i in range(4):
                a, b = F_[i], F_[(i + 1) % 4]; e = (b[0] - a[0], b[1] - a[1])
                den = d[0] * e[1] - d[1] * e[0]
                if abs(den) < 1e-14: continue
                w = (a[0] - p[0], a[1] - p[1])
                t = (w[0] * e[1] - w[1] * e[0]) / den; s = (w[0] * d[1] - w[1] * d[0]) / den
                if t > 1e-12 and -1e-12 <= s <= 1 + 1e-12 and (best is None or t < best[0]): best = (t, s, i)
            if best is None or best[2] != j or not (1e-6 < best[1] < 1 - 1e-6): ok = False; break
            p = (p[0] + best[0] * d[0], p[1] + best[0] * d[1])
        good += ok
    return good / trials
sq_faces = [SQ]
for j in (0, 3, 0):
    old = sq_faces[-1]; sq_faces.append([reflect_pt(p, old[j], old[(j + 1) % 4]) for p in old])
sq_faces = [[(float(x), float(y)) for x, y in f] for f in sq_faces]
rh_faces = [fl(f) for f in faces]
say('  square chain:', chain_hits(sq_faces, [(0, 0), (1, 3), (2, 0)], 200000, 3))
say('  rhombus chain:', chain_hits(rh_faces, [(0, 0), (1, 3), (2, 0)], 200000, 4))

say('\n== Printed polygon geometry (student PDF) ==')
for pno in range(5):
    for dr in doc[pno].get_drawings():
        it = dr['items']
        if len(it) == 4 and all(x[0] == 'l' for x in it) and dr.get('fill') is None:
            P = [(x[1].x, x[1].y) for x in it]
            sides = [hypot(P[(i + 1) % 4][0] - P[i][0], P[(i + 1) % 4][1] - P[i][1]) for i in range(4)]
            angs = []
            for i in range(4):
                a, b, c = P[i - 1], P[i], P[(i + 1) % 4]
                v1 = (a[0] - b[0], a[1] - b[1]); v2 = (c[0] - b[0], c[1] - b[1])
                ang = abs(degrees(atan2(v1[0] * v2[1] - v1[1] * v2[0], v1[0] * v2[0] + v1[1] * v2[1])))
                angs.append(round(ang, 2))
            xs = [p[0] for p in P]; ys = [p[1] for p in P]
            say(f'  p{pno + 1}: sides(cm)={[round(s / 72 * 2.54, 3) for s in sides]} angles={angs} '
                f'bbox {round((max(xs) - min(xs)) / 72 * 2.54, 2)} x {round((max(ys) - min(ys)) / 72 * 2.54, 2)} cm')
Path(__file__).with_suffix('.py.out').write_text('\n'.join(out) + '\n')
