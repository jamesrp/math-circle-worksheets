"""Independent triangular-lattice tools for the Week 1 math check.

Lattice point (u,v) sits at xy = (u + v/2, v*H). Cells:
  ('U',i,j): up triangle   (i,j),(i+1,j),(i,j+1)
  ('D',i,j): down triangle (i+1,j),(i,j+1),(i+1,j+1)
"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re
from math import sqrt
from fractions import Fraction
from itertools import combinations

H = sqrt(3) / 2
SRC = _os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-01/')

NUM = r'(-?\d+(?:\.\d+)?)'
PT = re.compile(r'\(\s*' + NUM + r'\s*,\s*' + NUM + r'\s*\)')


def to_lattice(x, y):
    v = y / H
    u = x - v / 2
    ru, rv = round(u * 2) / 2, round(v * 2) / 2
    assert abs(u - ru) < 1e-6 and abs(v - rv) < 1e-6, (x, y, u, v)
    return (Fraction(ru).limit_denominator(4), Fraction(rv).limit_denominator(4))


def parse_points(text):
    return [(float(a), float(b)) for a, b in PT.findall(text)]


def parse_paths(text):
    """Split a TikZ drawing string into a list of closed polygons (lists of xy)."""
    polys = []
    for seg in re.findall(r'\\draw\[[^\]]*\]\s*([^;]*);', text):
        pts = parse_points(seg)
        if pts:
            polys.append((seg, pts))
    return polys


def cell_vertices(c):
    t, i, j = c
    if t == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i, j + 1), (i + 1, j + 1)]


def xy(p):
    u, v = p
    return (float(u) + float(v) / 2, float(v) * H)


def centroid(c):
    pts = [xy(p) for p in cell_vertices(c)]
    return (sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3)


def cell_from_vertices(vs):
    """Identify the lattice cell from three lattice vertices (any order)."""
    vs = sorted((int(u), int(v)) for u, v in vs)
    s = set(vs)
    for (i, j) in vs:
        if {(i, j), (i + 1, j), (i, j + 1)} == s:
            return ('U', i, j)
        if {(i + 1, j), (i, j + 1), (i + 1, j + 1)} == s:
            return ('D', i, j)
        if {(i, j), (i - 1, j + 1), (i, j + 1)} == s:
            return ('D', i - 1, j)
        if {(i, j), (i + 1, j - 1), (i + 1, j)} == s:
            return ('D', i, j - 1)
    raise ValueError(vs)


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for k in range(n):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % n]
        if (y1 > y) != (y2 > y):
            xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xc > x:
                inside = not inside
    return inside


def cells_in_poly(poly_xy):
    lat = [to_lattice(*p) for p in poly_xy]
    us = [p[0] for p in lat]; vs = [p[1] for p in lat]
    out = set()
    for i in range(int(min(us)) - 4, int(max(us)) + 5):
        for j in range(int(min(vs)) - 1, int(max(vs)) + 2):
            for t in 'UD':
                c = (t, i, j)
                if point_in_poly(centroid(c), poly_xy):
                    out.add(c)
    return out


def poly_area_triangles(poly_xy):
    a = 0
    n = len(poly_xy)
    for k in range(n):
        x1, y1 = poly_xy[k]; x2, y2 = poly_xy[(k + 1) % n]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2 / (sqrt(3) / 4)


def neighbors(c):
    t, i, j = c
    if t == 'U':
        return [('D', i, j), ('D', i - 1, j), ('D', i, j - 1)]
    return [('U', i, j), ('U', i + 1, j), ('U', i, j + 1)]


# ---- lattice symmetries on points ----
def rot60(p):
    u, v = p
    return (-v, u + v)


def refl(p):
    u, v = p
    return (v, u)


def transform_cells(cells, f):
    return frozenset(cell_from_vertices([f(p) for p in cell_vertices(c)]) for c in cells)


def all_orientations(shape):
    shapes = set()
    cur = frozenset(shape)
    for r in range(2):
        for k in range(6):
            shapes.add(normalize(cur))
            cur = transform_cells(cur, rot60)
        cur = transform_cells(cur, refl)
    return shapes


def normalize(cells):
    # translate so that min vertex is near origin; translation by lattice vector (a,b)
    mi = min((i, j) for _, i, j in cells)
    return frozenset((t, i - mi[0], j - mi[1]) for t, i, j in cells)


def placements(shape, region):
    region = set(region)
    out = set()
    for o in all_orientations(shape):
        base = min((i, j) for _, i, j in o)
        for (_, ri, rj) in region:
            for dt in [(0, 0)]:
                pass
        # anchor: translate so each cell of o maps onto each region cell of same type
        anchor = next(iter(o))
        for rc in region:
            if rc[0] != anchor[0]:
                continue
            di, dj = rc[1] - anchor[1], rc[2] - anchor[2]
            pl = frozenset((t, i + di, j + dj) for t, i, j in o)
            if pl <= region:
                out.add(pl)
    return sorted(out, key=lambda s: sorted(s))


GREEN = {('U', 0, 0)}
BLUE = {('U', 0, 0), ('D', 0, 0)}
RED = {('U', 0, 0), ('D', 0, 0), ('U', 1, 0)}  # trapezoid
def hex_around(i, j):
    return {('U', i, j), ('U', i - 1, j), ('U', i, j - 1), ('D', i - 1, j), ('D', i, j - 1), ('D', i - 1, j - 1)}


YELLOW = hex_around(1, 1)
# chevron (0,0),(1,0),(1.5,h),(1,2h),(0,2h),(.5,h) = R-rhombus U(0,0)+D(0,0) and L-rhombus U(0,1)+D(-1,1)
PURPLE = {('U', 0, 0), ('D', 0, 0), ('U', 0, 1), ('D', -1, 1)}


def check_yellow():
    # hexagon around lattice point (1,1)? verify YELLOW is the six triangles around point (0,1)
    pts = set()
    for c in YELLOW:
        pts |= set(cell_vertices(c))
    return pts


def max_packing(region, pls):
    """Exact maximum number of disjoint placements (cells may stay empty)."""
    region = sorted(region)
    by_cell = {c: [p for p in pls if c in p] for c in region}
    best = [0, []]
    n = len(region)
    size = min(len(p) for p in pls) if pls else 1

    def rec(k, used, chosen):
        while k < n and region[k] in used:
            k += 1
        remaining = sum(1 for c in region[k:] if c not in used)
        if k < n and len(chosen) + remaining // size <= best[0]:
            return
        if k == n:
            if len(chosen) > best[0]:
                best[0] = len(chosen); best[1] = list(chosen)
            return
        c = region[k]
        for p in by_cell[c]:
            if p & used:
                continue
            chosen.append(p)
            rec(k + 1, used | p, chosen)
            chosen.pop()
        rec(k + 1, used | {c}, chosen)

    rec(0, frozenset(), [])
    return best[0], best[1]


def count_tilings(region, pls):
    region = sorted(region)
    by_cell = {c: [] for c in region}
    for p in pls:
        by_cell[min(p)].append(p)
    sols = []

    def rec(used, chosen):
        free = [c for c in region if c not in used]
        if not free:
            sols.append(list(chosen)); return
        c = free[0]
        for p in pls:
            if c in p and not (p & used):
                chosen.append(p); rec(used | p, chosen); chosen.pop()

    rec(frozenset(), [])
    return sols


def tilings_multi(region, piece_pls):
    """All exact tilings using any mix of pieces; piece_pls: dict name -> placements."""
    region = sorted(region)
    allp = [(n, p) for n, ps in piece_pls.items() for p in ps]
    sols = []

    def rec(used, chosen):
        free = [c for c in region if c not in used]
        if not free:
            sols.append(list(chosen)); return
        c = free[0]
        for n, p in allp:
            if c in p and not (p & used):
                chosen.append((n, p)); rec(used | p, chosen); chosen.pop()

    rec(frozenset(), [])
    return sols
