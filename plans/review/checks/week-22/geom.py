"""Exact planar convex-hull predicates for the Week 22 math check.

Written independently for this review; it imports nothing from the packet's own
checkers. All arithmetic is exact (fractions.Fraction).

A group's region is the convex hull of its point locations (closed):
  one location -> a point, two -> a closed segment, three or more -> the
  filled polygon (or a segment/point if they are collinear/coincident).
"""
import os
from fractions import Fraction as Fr
from itertools import combinations


def find_root():
    """Repository root: four folders up from plans/review/checks/week-NN/,
    or (while still in the tmp run folder) the nearest ancestor holding the
    lowell-math-circle-year-2 folder."""
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.normpath(os.path.join(here, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(root, 'lowell-math-circle-year-2')):
        return root
    root = here
    while not os.path.isdir(os.path.join(root, 'lowell-math-circle-year-2')):
        parent = os.path.dirname(root)
        if parent == root:
            raise SystemExit('repository root not found')
        root = parent
    return root


def P(x, y):
    return (Fr(str(x)), Fr(str(y)))


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    """Extreme points of the closed convex hull, counter-clockwise, collinear
    points removed. Length 1 = point, 2 = segment, >=3 = polygon."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and orient(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and orient(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    h = lo[:-1] + hi[:-1]
    return h if len(h) >= 2 else pts[:1] + pts[-1:]


def on_segment(p, a, b):
    if orient(a, b, p) != 0:
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def contains(h, p):
    if len(h) == 1:
        return h[0] == p
    if len(h) == 2:
        return on_segment(p, h[0], h[1])
    return all(orient(h[i], h[(i + 1) % len(h)], p) >= 0 for i in range(len(h)))


def clip_segment(h, a, b):
    """Parameter interval [t0, t1] of the points a + t(b - a), 0 <= t <= 1,
    that lie in hull h; None if empty. a == b is treated as a point."""
    if a == b:
        return (Fr(0), Fr(0)) if contains(h, a) else None
    d = (b[0] - a[0], b[1] - a[1])
    if len(h) >= 3:
        lo, hi = Fr(0), Fr(1)
        for i in range(len(h)):
            u, v = h[i], h[(i + 1) % len(h)]
            fa = orient(u, v, a)
            fb = orient(u, v, b)
            # need fa + t (fb - fa) >= 0
            k = fb - fa
            if k == 0:
                if fa < 0:
                    return None
            elif k > 0:
                lo = max(lo, -fa / k)
            else:
                hi = min(hi, -fa / k)
            if lo > hi:
                return None
        return (lo, hi)
    # h is a point or a segment: candidate points are where the line of h meets ab
    def tpar(p):
        if d[0] != 0:
            return (p[0] - a[0]) / d[0]
        return (p[1] - a[1]) / d[1]
    if len(h) == 1:
        return (tpar(h[0]),) * 2 if on_segment(h[0], a, b) else None
    u, v = h
    if orient(a, b, u) == 0 and orient(a, b, v) == 0:      # collinear
        tu, tv = tpar(u), tpar(v)
        lo, hi = max(Fr(0), min(tu, tv)), min(Fr(1), max(tu, tv))
        return (lo, hi) if lo <= hi else None
    e = (v[0] - u[0], v[1] - u[1])
    den = d[0] * e[1] - d[1] * e[0]
    if den == 0:
        return None                                       # parallel, distinct lines
    w = (u[0] - a[0], u[1] - a[1])
    t = (w[0] * e[1] - w[1] * e[0]) / den
    s = (w[0] * d[1] - w[1] * d[0]) / den
    if 0 <= t <= 1 and 0 <= s <= 1:
        return (t, t)
    return None


def shared_set(h, k):
    """Return a description of hull(h) ∩ hull(k): None, ('point', p),
    ('segment', p, q) or ('area',) when both are polygons that meet."""
    if len(h) > len(k):
        h, k = k, h
    if len(h) == 1:
        return ('point', h[0]) if contains(k, h[0]) else None
    if len(h) == 2:
        iv = clip_segment(k, h[0], h[1])
        if iv is None:
            return None
        a, b = h
        p = (a[0] + iv[0] * (b[0] - a[0]), a[1] + iv[0] * (b[1] - a[1]))
        q = (a[0] + iv[1] * (b[0] - a[0]), a[1] + iv[1] * (b[1] - a[1]))
        return ('point', p) if p == q else ('segment', p, q)
    # two polygons
    for i in range(len(h)):
        if clip_segment(k, h[i], h[(i + 1) % len(h)]) is not None:
            return ('area',)
    if contains(h, k[0]):
        return ('area',)
    return None


def meet(groups_pts):
    """True if the hulls of all given groups (lists of points) share one point.
    Implemented for any number of groups provided some group has <= 2
    distinct locations (always true for the partitions checked here)."""
    hs = [hull(g) for g in groups_pts]
    hs.sort(key=len)
    h0 = hs[0]
    if len(h0) == 1:
        return all(contains(h, h0[0]) for h in hs[1:])
    if len(h0) == 2:
        lo, hi = Fr(0), Fr(1)
        for h in hs[1:]:
            iv = clip_segment(h, h0[0], h0[1])
            if iv is None:
                return False
            lo, hi = max(lo, iv[0]), min(hi, iv[1])
            if lo > hi:
                return False
        return True
    if len(hs) == 2:
        return shared_set(hs[0], hs[1]) is not None
    raise NotImplementedError('three or more polygonal groups')


def two_splits(labels):
    """Unordered splits into two nonempty groups; first label always in group 1."""
    labels = list(labels)
    first, rest = labels[0], labels[1:]
    out = []
    for r in range(0, len(rest) + 1):
        for comb in combinations(rest, r):
            g1 = [first] + list(comb)
            g2 = [x for x in labels if x not in g1]
            if g2:
                out.append((''.join(g1), ''.join(g2)))
    return out


def set_partitions(labels, k):
    """All partitions of labels into exactly k nonempty unordered blocks."""
    labels = list(labels)
    def rec(i, blocks):
        if i == len(labels):
            if len(blocks) == k:
                yield [''.join(b) for b in blocks]
            return
        for b in blocks:
            b.append(labels[i])
            yield from rec(i + 1, blocks)
            b.pop()
        if len(blocks) < k:
            blocks.append([labels[i]])
            yield from rec(i + 1, blocks)
            blocks.pop()
    return list(rec(0, []))


def successes(pts):
    """pts: dict label -> point. Returns {split string: shared description}."""
    out = {}
    for g1, g2 in two_splits(sorted(pts)):
        s = shared_set(hull([pts[x] for x in g1]), hull([pts[x] for x in g2]))
        if s is not None:
            out[g1 + '|' + g2] = s
    return out


def fmt(x):
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'


def fmt_shared(s):
    if s[0] == 'point':
        return f'point ({fmt(s[1][0])}, {fmt(s[1][1])})'
    if s[0] == 'segment':
        return f'segment ({fmt(s[1][0])}, {fmt(s[1][1])})-({fmt(s[2][0])}, {fmt(s[2][1])})'
    return 'positive area'


def dist_to_line(p, a, b):
    """Float distance from p to the infinite line ab."""
    import math
    num = abs(float(orient(a, b, p)))
    return num / math.hypot(float(b[0] - a[0]), float(b[1] - a[1]))


def dist_to_segment(p, a, b):
    import math
    ax, ay, bx, by, px, py = map(float, (a[0], a[1], b[0], b[1], p[0], p[1]))
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)
