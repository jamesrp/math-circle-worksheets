"""Shared helpers for the Week 1 encore math check: page outlines, drawn tilings,
and an independent 3-D model of cube piles in a box corner."""
import os
import sys
from math import hypot, cos, sin, radians, sqrt
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfpaths as PP
import boards as BD
from lat import *

_PAGES = {}


def page(band, n):
    """Painted paths of page n (1-based)."""
    if band not in _PAGES:
        _PAGES[band] = PP.pages(band)
    return _PAGES[band][n - 1]


def outlines(band, n):
    return BD.page_outlines(page(band, n))


def stroked_boards(band, n, min_lw=0.0, max_lw=99):
    """Stroked (unfilled) outlines on a page, top-to-bottom then left-to-right."""
    outs = [o for o in outlines(band, n) if o.path['op'] == 'S' and min_lw <= o.lw <= max_lw and o.ok]
    return sorted(outs, key=lambda o: (-round(o.centre[1], 1), o.centre[0]))


def drawn_pieces(band, n):
    """Filled-and-stroked closed polygons (pieces in pictures)."""
    return [o for o in outlines(band, n) if o.path['op'] in ('B', 'B*', 'b', 'b*') and min(o.fill) < 0.97]


def cluster(outs, gap=0.02):
    """Group polygons that touch (share a point within `gap`)."""
    n = len(outs)
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a in range(n):
        for b in range(a + 1, n):
            pa, pb = outs[a].page_poly, outs[b].page_poly
            if any(hypot(p[0] - q[0], p[1] - q[1]) < gap for p in pa for q in pb):
                parent[find(a)] = find(b)
    groups = {}
    for a in range(n):
        groups.setdefault(find(a), []).append(outs[a])
    return sorted(groups.values(), key=lambda g: (-round(sum(o.centre[1] for o in g) / len(g), 1),
                                                  sum(o.centre[0] for o in g) / len(g)))


def tiling_from_pieces(group):
    """Snap a picture made of piece polygons to one lattice.  Returns
    (frame, region, tiling, colours) where tiling is a set of pieces (frozensets of cells)
    and colours maps piece -> fill rgb."""
    sides = []
    for o in group:
        P = o.page_poly
        sides += [(P[k], P[(k + 1) % len(P)]) for k in range(len(P))]
    unit = min(hypot(b[0] - a[0], b[1] - a[1]) for a, b in sides)
    theta, spread = infer_theta(sides)
    origin = group[0].page_poly[0]
    fr = Frame(unit, theta, origin)
    T = set()
    colours = {}
    maxerr = 0
    for o in group:
        lp = []
        for q in o.page_poly:
            l, e = fr.to_lat(q)
            maxerr = max(maxerr, e)
            lp.append(l)
        cells = cells_in_lattice_polys([lp])
        T.add(cells)
        colours[cells] = o.fill
    region = frozenset().union(*T)
    disjoint = sum(len(p) for p in T) == len(region)
    return {'frame': fr, 'region': region, 'tiling': frozenset(T), 'colours': colours,
            'snap_err': maxerr, 'disjoint': disjoint, 'unit': unit, 'theta': theta,
            'centre': (sum(o.centre[0] for o in group) / len(group), sum(o.centre[1] for o in group) / len(group))}


def colour_name(rgb):
    r, g, b = rgb
    if abs(r - g) < 0.03 and abs(g - b) < 0.03:
        return 'gray%.2f' % r
    if r > g and r > b and g > 0.7 * r and b < 0.75 * r:
        return 'yellow'
    if r > g and r > b:
        return 'red'
    if b > r and b > g:
        return 'blue'
    if g > r and g > b:
        return 'green'
    return 'other%s' % (tuple(round(v, 2) for v in rgb),)


def same_shape(R1, R2):
    """Regions equal up to translation only."""
    return normalize(R1) == normalize(R2)


def translate_to(R_src, R_dst):
    """Translation (di,dj) carrying R_src onto R_dst, or None."""
    a = min(v for c in R_src for v in c)
    b = min(v for c in R_dst for v in c)
    d = (b[0] - a[0], b[1] - a[1])
    img = frozenset(frozenset((v[0] + d[0], v[1] + d[1]) for v in c) for c in R_src)
    return d if img == frozenset(R_dst) else None


def shift(T, d):
    return frozenset(frozenset(frozenset((v[0] + d[0], v[1] + d[1]) for v in c) for c in p) for p in T)


# ----------------------------------------------------------------- 3-D model of a pile of cubes

# Isometric view from direction (1,1,1): x to the lower left, y to the lower right, z up.
UX = (-cos(radians(30)), -0.5)
UY = (cos(radians(30)), -0.5)
UZ = (0.0, 1.0)


def proj(p):
    x, y, z = p
    return (x * UX[0] + y * UY[0] + z * UZ[0], x * UX[1] + y * UY[1] + z * UZ[1])


def plane_partitions(a, b, c):
    """Stack heights h[i][j] (i < a along x, j < b along y, 0..c), non-increasing in i and j."""
    out = []
    for hs in product(range(c + 1), repeat=a * b):
        h = [list(hs[i * b:(i + 1) * b]) for i in range(a)]
        ok = all(h[i][j] >= h[i + 1][j] for i in range(a - 1) for j in range(b)) and \
            all(h[i][j] >= h[i][j + 1] for i in range(a) for j in range(b - 1))
        if ok:
            out.append(tuple(map(tuple, h)))
    return out


def visible_faces(h, a, b, c):
    """The faces seen from (1,1,1): floor/tops ('top'), faces parallel to the wall x=0 ('xwall'),
    faces parallel to the wall y=0 ('ywall').  Returns list of (type, 4 corner points in 3-D)."""
    F = []
    for i in range(a):
        for j in range(b):
            z = h[i][j]
            F.append(('top', [(i, j, z), (i + 1, j, z), (i + 1, j + 1, z), (i, j + 1, z)]))
    for j in range(b):
        for k in range(c):
            X = sum(1 for i in range(a) if h[i][j] > k)
            F.append(('xwall', [(X, j, k), (X, j + 1, k), (X, j + 1, k + 1), (X, j, k + 1)]))
    for i in range(a):
        for k in range(c):
            Y = sum(1 for j in range(b) if h[i][j] > k)
            F.append(('ywall', [(i, Y, k), (i + 1, Y, k), (i + 1, Y, k + 1), (i, Y, k + 1)]))
    return F


def box_outline(a, b, c):
    pts3 = [(a, 0, 0), (a, b, 0), (0, b, 0), (0, b, c), (0, 0, c), (a, 0, c)]
    return [proj(p) for p in pts3]


def key2(pts, nd=3):
    return frozenset((round(x, nd) + 0.0, round(y, nd) + 0.0) for x, y in pts)


def model_pictures(a, b, c):
    """{frozenset of face keys (centred at the hexagon centre): (heights, cubes, {facekey: type})}"""
    out = {}
    O = box_outline(a, b, c)
    cx = sum(p[0] for p in O) / 6
    cy = sum(p[1] for p in O) / 6
    for h in plane_partitions(a, b, c):
        faces = {}
        for typ, pts in visible_faces(h, a, b, c):
            q = [proj(p) for p in pts]
            faces[key2([(x - cx, y - cy) for x, y in q])] = typ
        out[frozenset(faces)] = (h, sum(map(sum, h)), faces)
    return out, [(x - cx, y - cy) for x, y in O]


def tiling_face_keys(T, frame):
    """Drawn or enumerated rhombus tiling -> centred, unit-scaled face keys in page orientation."""
    cells = frozenset().union(*T)
    pts = [frame.to_page(v) for c in cells for v in c]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    keys = {}
    for p in T:
        corners = {v for c in p for v in c}
        q = [frame.to_page(v) for v in corners]
        keys[key2([((x - cx) / frame.unit, (y - cy) / frame.unit) for x, y in q])] = p
    return keys


def region_outline_key(R, frame):
    pts = [frame.to_page(v) for c in R for v in c]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    bnd = boundary_edges(R)
    corner_pts = {v for e in bnd for v in e}
    return key2([((frame.to_page(v)[0] - cx) / frame.unit, (frame.to_page(v)[1] - cy) / frame.unit) for v in corner_pts])


def model_boundary_key(a, b, c):
    """All lattice points on the boundary of the projected box hexagon, centred."""
    O = box_outline(a, b, c)
    cx = sum(p[0] for p in O) / 6
    cy = sum(p[1] for p in O) / 6
    pts = set()
    for k in range(6):
        p, q = O[k], O[(k + 1) % 6]
        L = round(hypot(q[0] - p[0], q[1] - p[1]))
        for t in range(L + 1):
            pts.add((p[0] + (q[0] - p[0]) * t / L - cx, p[1] + (q[1] - p[1]) * t / L - cy))
    return key2(list(pts))


class Log:
    def __init__(self, path):
        self.path = path
        self.lines = []

    def __call__(self, *a):
        s = ' '.join(str(x) for x in a)
        print(s)
        self.lines.append(s)

    def save(self):
        with open(self.path, 'w') as fh:
            fh.write('\n'.join(self.lines) + '\n')
