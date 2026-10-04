"""
Core library for the triangular grid used by all design checks.

Coordinates
-----------
Lattice points are (i, j) meaning the point i*e1 + j*e2, where
e1 = (1, 0) and e2 = (1/2, sqrt(3)/2) in inches (small-triangle edge = 1 inch).
So the Cartesian position of lattice point (i, j) is x = i + j/2, y = j*sqrt(3)/2.

Small triangles:
  U(i,j) = up-pointing   triangle with corners (i,j), (i+1,j), (i,j+1)
  D(i,j) = down-pointing triangle with corners (i+1,j), (i,j+1), (i+1,j+1)
A triangle is stored as a tuple (i, j, o) with o = 0 for up, 1 for down.

"Row j" is the horizontal strip between heights j*0.866 and (j+1)*0.866 inches.
"""
from math import sqrt
from functools import lru_cache
import itertools

S3 = sqrt(3) / 2

UP, DN = 0, 1


def corners(t):
    i, j, o = t
    if o == UP:
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i + 1, j + 1), (i, j + 1)]


def cart(p):
    i, j = p
    return (i + j / 2.0, j * S3)


def centroid3(t):
    """3 x centroid in lattice coords (integers)."""
    i, j, o = t
    return (3 * i + 1, 3 * j + 1) if o == UP else (3 * i + 2, 3 * j + 2)


def from_centroid3(c):
    u, v = c
    if u % 3 == 1:
        assert v % 3 == 1
        return ((u - 1) // 3, (v - 1) // 3, UP)
    assert u % 3 == 2 and v % 3 == 2
    return ((u - 2) // 3, (v - 2) // 3, DN)


def rot60(t):
    u, v = centroid3(t)
    return from_centroid3((-v, u + v))


def reflect(t):
    u, v = centroid3(t)
    return from_centroid3((u + v, -v))


def neighbors(t):
    i, j, o = t
    if o == UP:
        return [(i, j, DN), (i - 1, j, DN), (i, j - 1, DN)]
    return [(i, j, UP), (i + 1, j, UP), (i, j + 1, UP)]


def around_point(p):
    """The six small triangles that have lattice point p as a corner, in counterclockwise order."""
    i, j = p
    ts = [(i, j, UP), (i - 1, j, DN), (i - 1, j, UP), (i - 1, j - 1, DN), (i, j - 1, UP), (i, j - 1, DN)]
    # sort by angle of centroid around p
    import math
    px, py = cart(p)

    def ang(t):
        cs = [cart(c) for c in corners(t)]
        cx = sum(c[0] for c in cs) / 3
        cy = sum(c[1] for c in cs) / 3
        return math.atan2(cy - py, cx - px) % (2 * math.pi)

    return sorted(ts, key=ang)


def normalize(cells):
    cells = sorted(cells)
    i0, j0, _ = cells[0]
    return tuple(sorted((i - i0, j - j0, o) for i, j, o in cells))


def orientations(cells, mirror=True):
    out = set()
    cur = list(cells)
    for _ in range(6):
        out.add(normalize(cur))
        if mirror:
            out.add(normalize([reflect(t) for t in cur]))
        cur = [rot60(t) for t in cur]
    return sorted(out)


# ---- pieces (as sets of small triangles) ----
GREEN = [(0, 0, UP)]
BLUE = [(0, 0, UP), (0, 0, DN)]
RED = [(0, 0, UP), (0, 0, DN), (1, 0, UP)]
YELLOW = around_point((1, 1))
_ar = around_point((1, 1))
PURPLE = _ar[0:4]  # four consecutive triangles around a point = chevron

PIECES = {"G": GREEN, "B": BLUE, "R": RED, "Y": YELLOW, "P": PURPLE}
AREA = {k: len(v) for k, v in PIECES.items()}


def placements(region, piece):
    """All placements (frozensets of cells) of the piece (any rotation/reflection) inside region."""
    region = set(region)
    out = set()
    for orient in orientations(PIECES[piece] if isinstance(piece, str) else piece):
        a = orient[0]
        for c in region:
            if c[2] != a[2]:
                continue
            di, dj = c[0] - a[0], c[1] - a[1]
            pl = frozenset((i + di, j + dj, o) for i, j, o in orient)
            if pl <= region:
                out.add(pl)
    return sorted(out, key=lambda s: sorted(s))


# ---- regions ----

def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    for k in range(n):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % n]
        if (y1 > y) != (y2 > y):
            xin = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xin:
                inside = not inside
    return inside


def region_from_lattice_polygon(verts):
    """verts: list of lattice points (i,j) going around the outline. Returns set of triangles inside."""
    poly = [cart(v) for v in verts]
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    cells = set()
    for j in range(min(ys) - 1, max(ys) + 1):
        for i in range(min(xs) - max(ys) - 2, max(xs) + abs(min(ys)) + 2):
            for o in (UP, DN):
                t = (i, j, o)
                cs = [cart(c) for c in corners(t)]
                cx = sum(c[0] for c in cs) / 3
                cy = sum(c[1] for c in cs) / 3
                if point_in_poly(cx, cy, poly):
                    cells.add(t)
    return cells


def triangle_region(n):
    """Up-pointing triangle with side n, bottom-left corner at lattice (0,0)."""
    return region_from_lattice_polygon([(0, 0), (n, 0), (0, n)])


def down_triangle_region(n, bottom=(0, 0)):
    bi, bj = bottom
    return region_from_lattice_polygon([(bi, bj), (bi, bj + n), (bi - n, bj + n)])


def hex_vertices(a, b, c, start=(0, 0)):
    """Hexagon with sides a (bottom, along e1), b (along e2), c (along e3=e2-e1), a, b, c."""
    e1, e2, e3 = (1, 0), (0, 1), (-1, 1)
    p = start
    vs = [p]
    for (d, L) in [(e1, a), (e2, b), (e3, c), ((-1, 0), a), ((0, -1), b), ((1, -1), c)]:
        p = (p[0] + d[0] * L, p[1] + d[1] * L)
        vs.append(p)
    assert vs[-1] == vs[0]
    return vs[:-1]


def hexagon_region(a, b, c, start=(0, 0)):
    return region_from_lattice_polygon(hex_vertices(a, b, c, start))


def counts(region):
    up = sum(1 for t in region if t[2] == UP)
    return up, len(region) - up


def bbox_inches(region):
    pts = [cart(c) for t in region for c in corners(t)]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (max(xs) - min(xs), max(ys) - min(ys))


def boundary_vertices(region):
    """Outline(s) of the region as lists of lattice points (collinear points removed)."""
    # collect directed boundary edges (ccw orientation of each triangle)
    edges = {}
    for t in region:
        cs = corners(t)
        # make ccw
        (x1, y1), (x2, y2), (x3, y3) = [cart(c) for c in cs]
        if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) < 0:
            cs = [cs[0], cs[2], cs[1]]
        for k in range(3):
            a, b = cs[k], cs[(k + 1) % 3]
            if (b, a) in edges:
                del edges[(b, a)]
            else:
                edges[(a, b)] = True
    nxt = {}
    for (a, b) in edges:
        nxt.setdefault(a, []).append(b)
    loops = []
    used = set()
    for (a, b) in list(edges):
        if (a, b) in used:
            continue
        loop = [a]
        cur = (a, b)
        while cur not in used:
            used.add(cur)
            u, v = cur
            loop.append(v)
            cands = [w for w in nxt[v] if (v, w) not in used]
            if not cands:
                break
            cur = (v, cands[0])
        loop = loop[:-1]
        # remove collinear points
        def is_coll(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) == 0
        changed = True
        while changed and len(loop) > 3:
            changed = False
            for k in range(len(loop)):
                p, q, r = loop[k - 1], loop[k], loop[(k + 1) % len(loop)]
                if is_coll(p, q, r):
                    loop.pop(k)
                    changed = True
                    break
        loops.append(loop)
    return loops


# ---- matching (blue rhombi) ----

def max_matching(region):
    region = set(region)
    ups = [t for t in region if t[2] == UP]
    match_d = {}

    def try_aug(u, seen):
        for d in neighbors(u):
            if d in region and d not in seen:
                seen.add(d)
                if d not in match_d or try_aug(match_d[d], seen):
                    match_d[d] = u
                    return True
        return False

    size = 0
    for u in ups:
        if try_aug(u, set()):
            size += 1
    return size, {(v, k) for k, v in match_d.items()}


# ---- exact cover search ----

def order_key(t):
    i, j, o = t
    return (j, i + j * 0.5, o)


def count_tilings(region, piece_names, limit=None, collect=False):
    """Count tilings of region by the given pieces (each piece unlimited supply)."""
    region = frozenset(region)
    cells = sorted(region, key=order_key)
    pls = []
    for p in piece_names:
        for pl in placements(region, p):
            pls.append((p, pl))
    by_cell = {c: [] for c in cells}
    for p, pl in pls:
        for c in pl:
            by_cell[c].append((p, pl))
    results = []
    count = [0]

    def rec(covered, chosen):
        if limit and count[0] >= limit:
            return
        first = None
        for c in cells:
            if c not in covered:
                first = c
                break
        if first is None:
            count[0] += 1
            if collect:
                results.append(list(chosen))
            return
        for p, pl in by_cell[first]:
            if pl.isdisjoint(covered):
                chosen.append((p, pl))
                rec(covered | pl, chosen)
                chosen.pop()

    rec(frozenset(), [])
    return (count[0], results) if collect else count[0]


def min_pieces(region, piece_names):
    """Fewest pieces covering region exactly (pieces from piece_names). Returns (k, example)."""
    region = frozenset(region)
    cells = sorted(region, key=order_key)
    by_cell = {c: [] for c in cells}
    for p in piece_names:
        for pl in placements(region, p):
            for c in pl:
                by_cell[c].append((p, pl))
    # try larger first
    for c in by_cell:
        by_cell[c].sort(key=lambda x: -len(x[1]))
    maxa = max(AREA[p] for p in piece_names)
    best = [len(region) + 1, None]

    def rec(covered, chosen, rem):
        lb = len(chosen) + -(-rem // maxa)
        if lb >= best[0]:
            return
        first = None
        for c in cells:
            if c not in covered:
                first = c
                break
        if first is None:
            best[0] = len(chosen)
            best[1] = list(chosen)
            return
        for p, pl in by_cell[first]:
            if pl.isdisjoint(covered):
                chosen.append((p, pl))
                rec(covered | pl, chosen, rem - len(pl))
                chosen.pop()

    rec(frozenset(), [], len(region))
    return best[0], best[1]


def min_greens(region, big_pieces, want_example=True):
    """Fewest green triangles in an exact cover of region by big_pieces plus greens."""
    region = frozenset(region)
    cells = sorted(region, key=order_key)
    by_cell = {c: [] for c in cells}
    for p in big_pieces:
        for pl in placements(region, p):
            for c in pl:
                by_cell[c].append((p, pl))
    best = [len(region) + 1, None]

    def lower_bound(covered):
        rem = [c for c in region if c not in covered]
        up = sum(1 for c in rem if c[2] == UP)
        dn = len(rem) - up
        return abs(up - dn)

    def rec(covered, chosen, greens):
        if greens + lower_bound(covered) >= best[0]:
            return
        first = None
        for c in cells:
            if c not in covered:
                first = c
                break
        if first is None:
            best[0] = greens
            best[1] = list(chosen)
            return
        for p, pl in by_cell[first]:
            if pl.isdisjoint(covered):
                chosen.append((p, pl))
                rec(covered | pl, chosen, greens)
                chosen.pop()
        chosen.append(("G", frozenset([first])))
        rec(covered | {first}, chosen, greens + 1)
        chosen.pop()

    rec(frozenset(), [], 0)
    return best[0], best[1]


def piece_vertices(cells):
    """Outline of a piece as Cartesian vertices (inches)."""
    loops = boundary_vertices(cells)
    assert len(loops) == 1
    return [cart(p) for p in loops[0]]


def fmt_pt(p):
    return "(%s, %s)" % (fmt_num(p[0]), fmt_num(p[1]))


def fmt_num(x):
    r = round(x, 3)
    if abs(r - round(r)) < 1e-9:
        return str(int(round(r)))
    return ("%.3f" % r).rstrip("0").rstrip(".")


def fmt_lattice_outline(region):
    loops = boundary_vertices(region)
    return [" -> ".join("(%d,%d)" % p for p in loop) for loop in loops]


def fmt_cart_outline(region, shift=(0, 0)):
    loops = boundary_vertices(region)
    out = []
    for loop in loops:
        pts = [cart(p) for p in loop]
        out.append(" ".join(fmt_pt((x - shift[0], y - shift[1])) for x, y in pts))
    return out


def min_corner(region):
    pts = [cart(c) for t in region for c in corners(t)]
    return (min(p[0] for p in pts), min(p[1] for p in pts))
