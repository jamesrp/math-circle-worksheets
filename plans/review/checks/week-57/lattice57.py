"""Exact lattice-polygon tools for the Week 57 math check (standard library only).

Written for this review; nothing here is imported from the packet's own
verifiers.  Points are integer pairs; areas are Fractions.

- classify(poly, p): 'boundary' / 'inside' / 'outside' by exact on-segment
  tests plus a crossing-number ray cast.
- counts(poly, holes): (I, B) by visiting every lattice point of the
  bounding box (holes: dots on hole outlines are boundary, dots strictly in a
  hole are removed).
- area_shoelace(poly) and area_cells(poly): two different exact area
  computations.  area_cells clips the polygon against every unit cell
  (Sutherland-Hodgman, Fractions) and adds the pieces, so it does not use the
  shoelace formula on the whole outline.
- is_simple(poly): straight-sided, non-self-touching closed outline.
- seg_intersection(a,b,c,d): exact description of two segments' intersection.
"""
from fractions import Fraction as F
from math import gcd
import os
import sys


def repo_root():
    """Find the repository from this file's location.

    The committed copy lives in plans/review/checks/week-NN/ (four folders
    below the root); the working copy lived in tmp/review-runs/week-NN/.  Walk
    upward until the folder holding lowell-math-circle-year-2 is found.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    cand = os.path.abspath(os.path.join(here, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    d = here
    while True:
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            sys.exit('repository root not found above ' + here)
        d = nd


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def on_segment(p, a, b):
    if cross(a, b, p) != 0:
        return False
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def edges(poly):
    n = len(poly)
    return [(poly[i], poly[(i + 1) % n]) for i in range(n)]


def classify(poly, p):
    for a, b in edges(poly):
        if on_segment(p, a, b):
            return 'boundary'
    inside = False
    x, y = p
    for a, b in edges(poly):
        (x1, y1), (x2, y2) = a, b
        if (y1 > y) != (y2 > y):
            # x-coordinate of crossing compared exactly
            # crossing x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            num = (y - y1) * (x2 - x1)
            den = (y2 - y1)
            xc = F(x1) + F(num, den)
            if xc > x:
                inside = not inside
    return 'inside' if inside else 'outside'


def area2_signed(poly):
    s = 0
    for a, b in edges(poly):
        s += a[0] * b[1] - a[1] * b[0]
    return s


def area_shoelace(poly):
    return F(abs(area2_signed(poly)), 2)


def _clip(subject, inside_fn, intersect_fn):
    out = []
    n = len(subject)
    if n == 0:
        return out
    for i in range(n):
        cur = subject[i]
        prev = subject[i - 1]
        ci, pi = inside_fn(cur), inside_fn(prev)
        if ci:
            if not pi:
                out.append(intersect_fn(prev, cur))
            out.append(cur)
        elif pi:
            out.append(intersect_fn(prev, cur))
    return out


def _clip_cell(poly, x0, y0):
    pts = [(F(p[0]), F(p[1])) for p in poly]
    for axis, val, keep_ge in ((0, x0, True), (0, x0 + 1, False),
                               (1, y0, True), (1, y0 + 1, False)):
        def inside(p, axis=axis, val=val, keep_ge=keep_ge):
            return p[axis] >= val if keep_ge else p[axis] <= val

        def inter(p, q, axis=axis, val=val):
            t = (val - p[axis]) / (q[axis] - p[axis])
            return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        pts = _clip(pts, inside, inter)
        if not pts:
            return []
    return pts


def _area_frac(pts):
    s = F(0)
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        s += a[0] * b[1] - a[1] * b[0]
    return abs(s) / 2


def area_cells(poly, holes=()):
    """Exact area as a sum over unit cells of the clipped polygon."""
    def one(pg):
        xs = [p[0] for p in pg]
        ys = [p[1] for p in pg]
        tot = F(0)
        for x0 in range(min(xs), max(xs)):
            for y0 in range(min(ys), max(ys)):
                tot += _area_frac(_clip_cell(pg, x0, y0))
        return tot
    return one(poly) - sum(one(h) for h in holes)


def counts(poly, holes=()):
    """(I, B) for the region inside poly, with optional holes."""
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    I = B = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            c = classify(poly, (x, y))
            if c == 'outside':
                continue
            hc = [classify(h, (x, y)) for h in holes]
            if c == 'boundary' or 'boundary' in hc:
                B += 1
            elif 'inside' in hc:
                continue
            else:
                I += 1
    return I, B


def dot_sets(poly, holes=()):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    ins, bd = [], []
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            c = classify(poly, (x, y))
            if c == 'outside':
                continue
            hc = [classify(h, (x, y)) for h in holes]
            if c == 'boundary' or 'boundary' in hc:
                bd.append((x, y))
            elif 'inside' in hc:
                continue
            else:
                ins.append((x, y))
    return sorted(ins), sorted(bd)


def boundary_gcd(poly):
    return sum(gcd(abs(b[0] - a[0]), abs(b[1] - a[1])) for a, b in edges(poly))


def seg_intersection(a, b, c, d):
    """Return None, ('point', p) or ('segment', p, q) exactly (Fractions)."""
    d1 = cross(a, b, c)
    d2 = cross(a, b, d)
    if d1 == 0 and d2 == 0:
        # collinear: project on the dominant axis
        ax = 0 if a[0] != b[0] else 1
        if a[ax] == b[ax] and c[ax] == d[ax]:
            ax = 1 - ax
        lo1, hi1 = sorted([a, b], key=lambda p: (p[ax], p[1 - ax]))
        lo2, hi2 = sorted([c, d], key=lambda p: (p[ax], p[1 - ax]))
        lo = max(lo1, lo2, key=lambda p: (p[ax], p[1 - ax]))
        hi = min(hi1, hi2, key=lambda p: (p[ax], p[1 - ax]))
        if (lo[ax], lo[1 - ax]) > (hi[ax], hi[1 - ax]):
            return None
        if lo == hi:
            return ('point', (F(lo[0]), F(lo[1])))
        return ('segment', (F(lo[0]), F(lo[1])), (F(hi[0]), F(hi[1])))
    d3 = cross(c, d, a)
    d4 = cross(c, d, b)
    if ((d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0) or
            (d3 > 0 and d4 > 0) or (d3 < 0 and d4 < 0)):
        return None
    # proper or touching intersection at one point
    den = (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])
    t = F((c[0] - a[0]) * (d[1] - c[1]) - (c[1] - a[1]) * (d[0] - c[0]), den)
    return ('point', (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))


def is_simple(poly):
    n = len(poly)
    if n < 3 or len(set(poly)) != n or area2_signed(poly) == 0:
        return False
    es = edges(poly)
    for i in range(n):
        for j in range(i + 1, n):
            r = seg_intersection(*es[i], *es[j])
            if r is None:
                continue
            adjacent = (j == i + 1) or (i == 0 and j == n - 1)
            if not adjacent:
                return False
            if r[0] == 'segment':
                return False  # overlapping (back-tracking) adjacent sides
            shared = es[i][1] if j == i + 1 else es[i][0]
            if r[1] != (F(shared[0]), F(shared[1])):
                return False
    return True


def Q2(I, B):
    """2 * (I + B/2 - 1), an integer."""
    return 2 * I + B - 2


def segment_dots(a, b):
    g = gcd(abs(b[0] - a[0]), abs(b[1] - a[1]))
    dx, dy = (b[0] - a[0]) // g, (b[1] - a[1]) // g
    return [(a[0] + k * dx, a[1] + k * dy) for k in range(g + 1)]


def meet_exactly(p1, p2, a, b):
    """True when closed regions p1, p2 meet exactly in segment ab (a != b):
    every boundary contact lies on ab, ab lies on both boundaries, and the two
    regions lie on opposite sides of ab (so interiors are disjoint)."""
    def on_ab(p):
        return (cross(a, b, p) == 0 and
                min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))
    for e in edges(p1):
        for f in edges(p2):
            r = seg_intersection(*e, *f)
            if r is None:
                continue
            pts = [r[1]] if r[0] == 'point' else [r[1], r[2]]
            if not all(on_ab(p) for p in pts):
                return False
    # ab covered by both boundaries: test every dot and every half-step point
    dots = segment_dots(a, b)
    probes = [(F(p[0]), F(p[1])) for p in dots]
    probes += [(F(p[0] + q[0], 2), F(p[1] + q[1], 2)) for p, q in zip(dots, dots[1:])]
    for pg in (p1, p2):
        for pr in probes:
            if not any(on_segment(pr, e[0], e[1]) for e in edges(pg)):
                return False
    # opposite sides of ab near its midpoint
    m = (F(a[0] + b[0], 2), F(a[1] + b[1], 2))
    nx, ny = -(b[1] - a[1]), (b[0] - a[0])
    eps = F(1, 10007)
    plus = (m[0] + eps * nx, m[1] + eps * ny)
    minus = (m[0] - eps * nx, m[1] - eps * ny)
    c1 = (classify(p1, plus), classify(p1, minus))
    c2 = (classify(p2, plus), classify(p2, minus))
    return (c1 == ('inside', 'outside') and c2 == ('outside', 'inside')) or \
           (c1 == ('outside', 'inside') and c2 == ('inside', 'outside'))
