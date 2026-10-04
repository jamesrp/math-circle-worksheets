"""Triangular-grid geometry, solvers and TikZ output for the Week 1 tiling pages.

Lattice point (a, b) sits at Cartesian (a + b/2, b*S), S = sqrt(3)/2, unit = 1 inch.
Cells: ('U', a, b) has corners (a,b), (a+1,b), (a,b+1);
       ('D', a, b) has corners (a+1,b), (a+1,b+1), (a,b+1).
"""
import math
from itertools import combinations

S = math.sqrt(3) / 2


def cart(p):
    a, b = p
    return (a + b / 2.0, b * S)


def corners(c):
    t, a, b = c
    if t == 'U':
        return [(a, b), (a + 1, b), (a, b + 1)]
    return [(a + 1, b), (a + 1, b + 1), (a, b + 1)]


def centroid(c):
    pts = [cart(p) for p in corners(c)]
    return (sum(x for x, _ in pts) / 3, sum(y for _, y in pts) / 3)


def edges(c):
    p = corners(c)
    return [frozenset((p[0], p[1])), frozenset((p[1], p[2])), frozenset((p[2], p[0]))]


def neighbors(c):
    t, a, b = c
    if t == 'U':
        return [('D', a, b), ('D', a - 1, b), ('D', a, b - 1)]
    return [('U', a, b), ('U', a + 1, b), ('U', a, b + 1)]


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                inside = not inside
    return inside


def region_from_poly(lat_poly):
    poly = [cart(p) for p in lat_poly]
    xs = [p[0] for p in lat_poly] + [p[1] for p in lat_poly]
    lo, hi = min(xs) - 2 * max(abs(v) for v in xs) - 3, max(xs) + 2 * max(abs(v) for v in xs) + 3
    cells = set()
    for a in range(int(lo), int(hi) + 1):
        for b in range(int(lo), int(hi) + 1):
            for t in 'UD':
                c = (t, a, b)
                if point_in_poly(centroid(c), poly):
                    cells.add(c)
    return cells


def hexagon_poly(a, b, c):
    pts = [(0, 0)]
    for (dx, dy), n in [((1, 0), a), ((0, 1), b), ((-1, 1), c), ((-1, 0), a), ((0, -1), b), ((1, -1), c)]:
        x, y = pts[-1]
        pts.append((x + dx * n, y + dy * n))
    return pts[:-1]


def triangle_poly(n):
    return [(0, 0), (n, 0), (0, n)]


def counts(cells):
    u = sum(1 for c in cells if c[0] == 'U')
    return u, len(cells) - u


def rhombi(cells):
    out = []
    for c in cells:
        if c[0] == 'U':
            for d in neighbors(c):
                if d in cells:
                    out.append(frozenset((c, d)))
    return out


def rhomb_kind(r):
    u = [c for c in r if c[0] == 'U'][0]
    d = [c for c in r if c[0] == 'D'][0]
    _, a, b = u
    if d == ('D', a, b):
        return 'R'
    if d == ('D', a - 1, b):
        return 'L'
    return 'V'


def around(v):
    """The six cells around lattice point v, in cyclic order."""
    a, b = v
    # cyclic order counterclockwise starting with the up-triangle to the upper right
    return [('U', a, b), ('D', a - 1, b), ('U', a - 1, b), ('D', a - 1, b - 1), ('U', a, b - 1), ('D', a, b - 1)]


def check_around():
    # every consecutive pair around a vertex must be edge-adjacent
    ring = around((0, 0))
    for i in range(6):
        c, d = ring[i], ring[(i + 1) % 6]
        assert d in neighbors(c), (c, d)
        assert (0, 0) in corners(c)


def chevrons(cells):
    out = set()
    vs = set(p for c in cells for p in corners(c))
    for v in vs:
        ring = around(v)
        for i in range(6):
            piece = frozenset(ring[(i + k) % 6] for k in range(4))
            if piece <= cells:
                out.add(piece)
    return list(out)


def all_tilings(cells, pieces=None, limit=None):
    cells = set(cells)
    if pieces is None:
        pieces = rhombi(cells)
    by_cell = {c: [] for c in cells}
    for p in pieces:
        for c in p:
            by_cell[c].append(p)
    order = sorted(cells, key=lambda c: (c[2], c[1] + c[2] / 2.0, c[0]))
    res = []

    def rec(covered, chosen):
        if limit and len(res) >= limit:
            return
        for c in order:
            if c not in covered:
                break
        else:
            res.append(list(chosen))
            return
        for p in by_cell[c]:
            if not (p & covered):
                chosen.append(p)
                rec(covered | p, chosen)
                chosen.pop()

    rec(frozenset(), [])
    return res


def max_matching(cells):
    us = [c for c in cells if c[0] == 'U']
    match = {}

    def try_aug(u, seen):
        for d in neighbors(u):
            if d in cells and d not in seen:
                seen.add(d)
                if d not in match or try_aug(match[d], seen):
                    match[d] = u
                    return True
        return False

    for u in us:
        try_aug(u, set())
    return [frozenset((u, d)) for d, u in match.items()]


def max_packing(cells, pieces):
    """Maximum number of disjoint pieces (branch and bound)."""
    cells = frozenset(cells)
    pieces = [p for p in pieces if p <= cells]
    order = sorted(cells, key=lambda c: (c[2], c[1] + c[2] / 2.0, c[0]))
    by_cell = {c: [p for p in pieces if c in p] for c in cells}
    size = len(pieces[0]) if pieces else 1
    best = [0, []]

    def rec(i, covered, chosen):
        remaining = len(cells) - len(covered)
        if len(chosen) + remaining // size <= best[0]:
            return
        if len(chosen) > best[0]:
            best[0] = len(chosen)
            best[1] = list(chosen)
        # find next uncovered cell
        while i < len(order) and order[i] in covered:
            i += 1
        if i >= len(order):
            return
        c = order[i]
        for p in by_cell[c]:
            if not (p & covered):
                chosen.append(p)
                rec(i + 1, covered | p, chosen)
                chosen.pop()
        # leave c uncovered
        rec(i + 1, covered | {c}, chosen)

    rec(0, frozenset(), [])
    return best[1]


def flip_neighbors(tiling, cells):
    tset = set(tiling)
    out = []
    vs = set(p for c in cells for p in corners(c))
    for v in vs:
        ring = around(v)
        if not all(c in cells for c in ring):
            continue
        A = [frozenset((ring[0], ring[1])), frozenset((ring[2], ring[3])), frozenset((ring[4], ring[5]))]
        B = [frozenset((ring[1], ring[2])), frozenset((ring[3], ring[4])), frozenset((ring[5], ring[0]))]
        if all(r in tset for r in A):
            out.append(frozenset((tset - set(A)) | set(B)))
        elif all(r in tset for r in B):
            out.append(frozenset((tset - set(B)) | set(A)))
    return out


def chains(tiling, cells):
    """Chains of L/R rhombi from the bottom horizontal boundary edges up to the top."""
    piece_of = {}
    for r in tiling:
        for c in r:
            piece_of[c] = r
    bottoms = sorted([c for c in cells if c[0] == 'U' and ('D', c[1], c[2] - 1) not in cells
                      and c[2] == min(x[2] for x in cells)], key=lambda c: c[1])
    out = []
    for u in bottoms:
        word = []
        shaded = []
        cur = u
        while cur in cells:
            r = piece_of[cur]
            k = rhomb_kind(r)
            assert k in 'LR', (cur, r)
            word.append(k)
            shaded.append(r)
            d = [c for c in r if c[0] == 'D'][0]
            cur = ('U', d[1], d[2] + 1)
        out.append((''.join(word), shaded))
    return out


# ---------------------------------------------------------------- TikZ output

def fmt(v):
    s = '%.4f' % v
    s = s.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def pt(p):
    x, y = cart(p)
    return '(%s,%s)' % (fmt(x), fmt(y))


def boundary_edges(cells):
    cnt = {}
    for c in cells:
        for e in edges(c):
            cnt[e] = cnt.get(e, 0) + 1
    return [e for e, k in cnt.items() if k == 1]


def interior_edges(cells):
    cnt = {}
    for c in cells:
        for e in edges(c):
            cnt[e] = cnt.get(e, 0) + 1
    return [e for e, k in cnt.items() if k == 2]


def piece_edges(cells, tiling):
    """Interior edges that separate two different pieces."""
    piece_of = {}
    for i, r in enumerate(tiling):
        for c in r:
            piece_of[c] = i
    e2c = {}
    for c in cells:
        for e in edges(c):
            e2c.setdefault(e, []).append(c)
    out = []
    for e, cs in e2c.items():
        if len(cs) == 2:
            a, b = cs
            if piece_of.get(a, ('x', a)) != piece_of.get(b, ('y', b)):
                out.append(e)
    return out


def seg(e):
    p, q = sorted(e)
    return '%s--%s' % (pt(p), pt(q))


def tikz(cells, scale=1.0, tiling=None, grid=True, fills=None, outline_w=1.6,
         grid_color='black!30', grid_w=0.5, tile_w=1.1, label=None, extra='',
         origin=None, unit_note=None):
    """Return a tikzpicture drawing the region `cells`.

    scale: inches per small edge (1.0 = actual size).
    fills: list of (set_of_cells, tikz_fill_spec).
    tiling: list of pieces (frozensets of cells) whose separating edges are drawn.
    """
    lines = ['\\begin{tikzpicture}[x=%sin,y=%sin,line cap=round,line join=round]' % (fmt(scale), fmt(scale))]
    if fills:
        for cs, spec in fills:
            for c in sorted(cs):
                p = corners(c)
                lines.append('\\fill[%s] %s--%s--%s--cycle;' % (spec, pt(p[0]), pt(p[1]), pt(p[2])))
    if grid:
        ie = interior_edges(cells)
        if ie:
            lines.append('\\draw[%s,line width=%spt] %s;' % (grid_color, fmt(grid_w), ' '.join(seg(e) for e in sorted(ie, key=sorted))))
    if tiling:
        pe = piece_edges(cells, tiling)
        if pe:
            lines.append('\\draw[black,line width=%spt] %s;' % (fmt(tile_w), ' '.join(seg(e) for e in sorted(pe, key=sorted))))
    be = boundary_edges(cells)
    lines.append('\\draw[black,line width=%spt] %s;' % (fmt(outline_w), ' '.join(seg(e) for e in sorted(be, key=sorted))))
    if extra:
        lines.append(extra)
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)


def bbox(cells):
    pts = [cart(p) for c in cells for p in corners(c)]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


check_around()
