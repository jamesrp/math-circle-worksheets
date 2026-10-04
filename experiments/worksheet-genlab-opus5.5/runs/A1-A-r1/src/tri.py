"""Triangular-grid geometry, piece placement, solvers, and TikZ output.

Lattice point (i, j) sits at Cartesian (i + j/2, j*S) in units of one triangle edge.
Up triangle U(i,j) has corners (i,j), (i+1,j), (i,j+1).
Down triangle D(i,j) has corners (i+1,j), (i+1,j+1), (i,j+1).
"""
import math
from collections import defaultdict

S = math.sqrt(3) / 2


def cart(v):
    i, j = v
    return (i + j / 2.0, j * S)


def verts(t):
    k, i, j = t
    if k == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i + 1, j + 1), (i, j + 1)]


def tedges(t):
    v = verts(t)
    return [frozenset((v[a], v[(a + 1) % 3])) for a in range(3)]


def centroid(t):
    xs = [cart(v) for v in verts(t)]
    return (sum(p[0] for p in xs) / 3, sum(p[1] for p in xs) / 3)


def identify(vset):
    vset = set(vset)
    for (i, j) in vset:
        for (a, b) in [(i, j), (i - 1, j), (i, j - 1), (i - 1, j - 1)]:
            if {(a, b), (a + 1, b), (a, b + 1)} == vset:
                return ('U', a, b)
            if {(a + 1, b), (a + 1, b + 1), (a, b + 1)} == vset:
                return ('D', a, b)
    raise ValueError(vset)


def rot60(v):
    i, j = v
    return (-j, i + j)


def refl(v):
    i, j = v
    return (i + j, -j)


def transform(tris, f):
    return frozenset(identify([f(v) for v in verts(t)]) for t in tris)


def normalize(tris):
    # translate so that the minimal triangle (in a fixed order) has i=j=0
    # translation must keep types; use min over (j, i, k)
    m = min(tris, key=lambda t: (t[2], t[1], t[0]))
    return frozenset((k, i - m[1], j - m[2]) for k, i, j in tris)


def images(base):
    out = set()
    cur = frozenset(base)
    for r in range(2):
        for _ in range(6):
            out.add(normalize(cur))
            cur = transform(cur, rot60)
        cur = transform(cur, refl)
    return list(out)


U = lambda i, j: ('U', i, j)
D = lambda i, j: ('D', i, j)

PIECES = {
    'G': [U(0, 0)],
    'B': [U(0, 0), D(0, 0)],
    'R': [U(0, 0), D(0, 0), U(1, 0)],
    'P': [U(0, 0), D(0, 0), U(1, 0), D(1, -1)],
    'Y': [U(1, 1), U(0, 1), U(1, 0), D(0, 1), D(0, 0), D(1, 0)],
}


def hex_around(i, j):
    return frozenset([U(i, j), U(i - 1, j), U(i, j - 1), D(i - 1, j), D(i - 1, j - 1), D(i, j - 1)])


def placements(piece, region):
    region = frozenset(region)
    res = set()
    for img in images(PIECES[piece]):
        t0 = min(img)
        for t in region:
            if t[0] != t0[0]:
                continue
            di, dj = t[1] - t0[1], t[2] - t0[2]
            moved = frozenset((k, i + di, j + dj) for k, i, j in img)
            if moved <= region:
                res.add(moved)
    return sorted(res, key=lambda s: sorted(s))


# ---------------------------------------------------------------- regions

def big_triangle(n, i0=0, j0=0):
    r = set()
    for j in range(n):
        for i in range(n - j):
            r.add(U(i0 + i, j0 + j))
        for i in range(n - j - 1):
            r.add(D(i0 + i, j0 + j))
    return frozenset(r)


def point_in_poly(p, poly):
    x, y = p
    inside = False
    n = len(poly)
    for a in range(n):
        x1, y1 = poly[a]
        x2, y2 = poly[(a + 1) % n]
        if (y1 > y) != (y2 > y):
            xin = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xin:
                inside = not inside
    return inside


def region_from_lattice_poly(lpoly):
    """lpoly: list of lattice vertices of a closed polygon along grid lines."""
    poly = [cart(v) for v in lpoly]
    imin = min(v[0] for v in lpoly) - 2 - max(abs(v[1]) for v in lpoly)
    imax = max(v[0] for v in lpoly) + 2 + max(abs(v[1]) for v in lpoly)
    jmin = min(v[1] for v in lpoly) - 1
    jmax = max(v[1] for v in lpoly) + 1
    r = set()
    for j in range(jmin, jmax + 1):
        for i in range(imin, imax + 1):
            for k in 'UD':
                t = (k, i, j)
                if point_in_poly(centroid(t), poly):
                    r.add(t)
    return frozenset(r)


def hexagon(a, b, c, start=(0, 0)):
    """Hexagon with horizontal top side a, then clockwise sides b, c, a, b, c.
    start is the lattice position of the top-left corner."""
    steps = [((1, 0), a), ((1, -1), b), ((0, -1), c), ((-1, 0), a), ((-1, 1), b), ((0, 1), c)]
    v = start
    poly = [v]
    for (d, n) in steps:
        v = (v[0] + d[0] * n, v[1] + d[1] * n)
        poly.append(v)
    assert poly[-1] == start
    return region_from_lattice_poly(poly[:-1]), poly[:-1]


def counts(region):
    u = sum(1 for t in region if t[0] == 'U')
    return u, len(region) - u


# ---------------------------------------------------------------- solvers

def tilings(region, pieces=('B',), limit=None):
    region = frozenset(region)
    pl = []
    for p in pieces:
        for s in placements(p, region):
            pl.append((p, s))
    cover = defaultdict(list)
    for idx, (p, s) in enumerate(pl):
        for t in s:
            cover[t].append(idx)
    out = []

    def rec(free, chosen):
        if limit is not None and len(out) >= limit:
            return
        if not free:
            out.append(list(chosen))
            return
        best = None
        bestopts = None
        for t in free:
            opts = [ix for ix in cover[t] if pl[ix][1] <= free]
            if best is None or len(opts) < len(bestopts):
                best, bestopts = t, opts
                if len(opts) == 0:
                    return
        for ix in bestopts:
            chosen.append(pl[ix])
            rec(free - pl[ix][1], chosen)
            chosen.pop()

    rec(region, [])
    return out


def max_pack(region, pieces=('B',), forbid_count=None):
    """Return (min uncovered, one optimal packing)."""
    region = frozenset(region)
    order = sorted(region, key=lambda t: (t[2], t[1], t[0]))
    pl = []
    for p in pieces:
        for s in placements(p, region):
            pl.append((p, s))
    cover = defaultdict(list)
    for idx, (p, s) in enumerate(pl):
        for t in s:
            cover[t].append(idx)
    best = [len(region) + 1, None]

    def lb(free):
        u = sum(1 for t in free if t[0] == 'U')
        d = len(free) - u
        return abs(u - d)

    def rec(pos, free, empty, chosen):
        if empty + lb(free) >= best[0]:
            return
        while pos < len(order) and order[pos] not in free:
            pos += 1
        if pos == len(order):
            best[0] = empty
            best[1] = list(chosen)
            return
        t = order[pos]
        for ix in cover[t]:
            if pl[ix][1] <= free:
                chosen.append(pl[ix])
                rec(pos + 1, free - pl[ix][1], empty, chosen)
                chosen.pop()
        rec(pos + 1, free - {t}, empty + 1, chosen)

    rec(0, region, 0, [])
    return best[0], best[1]


def min_pieces(region, pieces=('G', 'B', 'R', 'P', 'Y')):
    region = frozenset(region)
    order = sorted(region, key=lambda t: (t[2], t[1], t[0]))
    pl = []
    for p in pieces:
        for s in placements(p, region):
            pl.append((p, s))
    cover = defaultdict(list)
    for idx, (p, s) in enumerate(pl):
        for t in s:
            cover[t].append(idx)
    maxsize = max(len(s) for _, s in pl)
    best = [10 ** 9, None]

    def rec(pos, free, chosen):
        if len(chosen) + math.ceil(len(free) / maxsize) >= best[0]:
            return
        while pos < len(order) and order[pos] not in free:
            pos += 1
        if pos == len(order):
            best[0] = len(chosen)
            best[1] = list(chosen)
            return
        t = order[pos]
        for ix in sorted(cover[t], key=lambda ix: -len(pl[ix][1])):
            if pl[ix][1] <= free:
                chosen.append(pl[ix])
                rec(pos + 1, free - pl[ix][1], chosen)
                chosen.pop()

    rec(0, region, [])
    return best


# ---------------------------------------------------------------- drawing

def boundary_edges(tris):
    cnt = defaultdict(int)
    for t in tris:
        for e in tedges(t):
            cnt[e] += 1
    return [e for e, c in cnt.items() if c == 1]


def all_edges(tris):
    s = set()
    for t in tris:
        s.update(tedges(t))
    return s


def cycles(edges):
    """Chain boundary edges into closed cycles (lists of lattice vertices)."""
    adj = defaultdict(list)
    for e in edges:
        a, b = tuple(e)
        adj[a].append(b)
        adj[b].append(a)
    used = set()
    out = []
    for e in edges:
        if e in used:
            continue
        a, b = tuple(e)
        cyc = [a, b]
        used.add(e)
        prev, cur = a, b
        while True:
            nxt = None
            for c in adj[cur]:
                f = frozenset((cur, c))
                if f not in used:
                    nxt = c
                    break
            if nxt is None:
                break
            used.add(frozenset((cur, nxt)))
            if nxt == cyc[0]:
                break
            cyc.append(nxt)
            prev, cur = cur, nxt
        out.append(cyc)
    return out


def merge_collinear(cyc):
    """Drop vertices where the polygon goes straight on."""
    pts = [cart(v) for v in cyc]
    n = len(pts)
    keep = []
    for a in range(n):
        p0, p1, p2 = pts[a - 1], pts[a], pts[(a + 1) % n]
        cross = (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0])
        if abs(cross) > 1e-9:
            keep.append(cyc[a])
    return keep


def fmt(p):
    return "(%.4f,%.4f)" % (p[0], p[1])


def path_of(tris):
    """TikZ path (possibly several closed cycles) for the outline of a set of triangles."""
    parts = []
    for cyc in cycles(boundary_edges(tris)):
        cyc = merge_collinear(cyc)
        parts.append(" -- ".join(fmt(cart(v)) for v in cyc) + " -- cycle")
    return " ".join(parts)


def seg(e):
    a, b = tuple(e)
    return fmt(cart(a)) + " -- " + fmt(cart(b))


def tikz_region(region, grid='grid', outline='outline', fill=None, holes=(), hole_style='hole',
                extra=''):
    """Return tikz commands (no environment) drawing a board."""
    L = []
    allr = frozenset(region) | frozenset(holes)
    if fill:
        L.append("\\fill[%s,even odd rule] %s;" % (fill, path_of(allr)))
    if holes:
        L.append("\\fill[%s,even odd rule] %s;" % (hole_style, path_of(frozenset(holes))))
    inner = all_edges(allr) - set(boundary_edges(allr))
    if grid and inner:
        L.append("\\draw[%s] %s;" % (grid, " ".join(seg(e) for e in sorted(inner, key=sorted))))
    if holes:
        L.append("\\draw[%s] %s;" % (outline, path_of(frozenset(holes))))
    L.append("\\draw[%s] %s;" % (outline, path_of(allr)))
    if extra:
        L.append(extra)
    return "\n".join(L)


def tikz_tiling(pieces, fills=None, outline='piece', default_fill=None):
    """pieces: list of (name, frozenset). fills: dict name->style or callable."""
    L = []
    for name, s in pieces:
        st = None
        if callable(fills):
            st = fills(name, s)
        elif fills:
            st = fills.get(name)
        if st is None:
            st = default_fill
        if st:
            L.append("\\fill[%s] %s;" % (st, path_of(s)))
    for name, s in pieces:
        L.append("\\draw[%s] %s;" % (outline, path_of(s)))
    return "\n".join(L)


def bbox(tris):
    pts = [cart(v) for t in tris for v in verts(t)]
    return (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))


def shift_region(region, di, dj):
    return frozenset((k, i + di, j + dj) for k, i, j in region)
