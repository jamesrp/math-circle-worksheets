"""Independent triangular-lattice tools for the Week 1 encore math check.

Lattice point (i, j) sits at  origin + unit * (i*e1 + j*e2),  e1 at angle theta,
e2 at theta + 60 degrees.  A cell is a frozenset of its three lattice vertices.
Up cell  U(i,j) = {(i,j), (i+1,j), (i,j+1)}; down cell D(i,j) = {(i+1,j), (i,j+1), (i+1,j+1)}.
When theta = 0 (horizontal grid lines) "up" cells point up on the page.

Pieces are frozensets of cells.  Everything here is my own code; nothing is imported
from the packet's sources.
"""
from math import sqrt, atan2, degrees, cos, sin, radians, hypot
from functools import lru_cache
from itertools import combinations
from collections import Counter

R3 = sqrt(3) / 2


def U(i, j):
    return frozenset([(i, j), (i + 1, j), (i, j + 1)])


def D(i, j):
    return frozenset([(i + 1, j), (i, j + 1), (i + 1, j + 1)])


def is_up(c):
    # an up cell has two vertices with the smallest j
    js = sorted(v[1] for v in c)
    return js[0] == js[1]


def lcart(p):
    i, j = p
    return (i + j / 2.0, j * R3)


def centroid(c):
    pts = [lcart(v) for v in c]
    return (sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3)


def edges(c):
    v = sorted(c)
    return [frozenset(e) for e in combinations(v, 2)]


def adjacent(a, b):
    return len(a & b) == 2


# ----------------------------------------------------------------- frames (page <-> lattice)

class Frame:
    """Maps page inches <-> lattice coordinates."""

    def __init__(self, unit, theta, origin):
        self.unit, self.theta, self.origin = unit, theta, origin
        t = radians(theta)
        self.e1 = (cos(t), sin(t))
        self.e2 = (cos(t + radians(60)), sin(t + radians(60)))

    def to_lat(self, p, tol=0.03):
        x, y = p[0] - self.origin[0], p[1] - self.origin[1]
        x, y = x / self.unit, y / self.unit
        # solve x = i*e1 + j*e2
        a, b = self.e1
        c, d = self.e2
        det = a * d - b * c
        i = (x * d - y * c) / det
        j = (a * y - b * x) / det
        ri, rj = round(i), round(j)
        err = max(abs(i - ri), abs(j - rj))
        return (ri, rj), err

    def to_page(self, q):
        i, j = q
        return (self.origin[0] + self.unit * (i * self.e1[0] + j * self.e2[0]),
                self.origin[1] + self.unit * (i * self.e1[1] + j * self.e2[1]))


def seg_angle(a, b):
    return degrees(atan2(b[1] - a[1], b[0] - a[0])) % 180


def infer_theta(segs):
    """Grid orientation mod 60 degrees from a list of segments (pairs of points)."""
    angs = [seg_angle(a, b) % 60 for a, b in segs if hypot(b[0] - a[0], b[1] - a[1]) > 1e-3]
    # cluster near 0/60
    vals = [a if a < 59 else a - 60 for a in angs]
    t = sorted(vals)[len(vals) // 2]
    spread = max(abs(v - t) for v in vals)
    return t, spread


def poly_sides(poly):
    n = len(poly)
    return [(poly[k], poly[(k + 1) % n]) for k in range(n)]


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for k in range(n):
        x1, y1 = poly[k]
        x2, y2 = poly[(k + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                inside = not inside
    return inside


def cells_in_lattice_polys(lpolys):
    """Cells whose centroid is inside an odd number of the given lattice polygons."""
    cpolys = [[lcart(p) for p in L] for L in lpolys]
    allp = [p for L in lpolys for p in L]
    imin = min(p[0] for p in allp) - max(abs(p[1]) for p in allp) - 3
    imax = max(p[0] for p in allp) + max(abs(p[1]) for p in allp) + 3
    jmin = min(p[1] for p in allp) - 1
    jmax = max(p[1] for p in allp) + 1
    out = set()
    for i in range(imin, imax + 1):
        for j in range(jmin, jmax + 1):
            for c in (U(i, j), D(i, j)):
                cc = centroid(c)
                k = sum(1 for P in cpolys if point_in_poly(cc, P))
                if k % 2:
                    out.add(c)
    return frozenset(out)


def interior_edges(R):
    cnt = Counter(e for c in R for e in edges(c))
    return {e for e, k in cnt.items() if k == 2}


def boundary_edges(R):
    cnt = Counter(e for c in R for e in edges(c))
    return {e for e, k in cnt.items() if k == 1}


def lattice_poly_sides(lpoly):
    """Side lengths (in units) and exterior turning angles of a lattice polygon."""
    pts = [lcart(p) for p in lpoly]
    n = len(pts)
    sides, turns = [], []
    for k in range(n):
        a, b, c = pts[k - 1], pts[k], pts[(k + 1) % n]
        sides.append(round(hypot(c[0] - b[0], c[1] - b[1]), 6))
        a1 = atan2(b[1] - a[1], b[0] - a[0])
        a2 = atan2(c[1] - b[1], c[0] - b[0])
        turns.append(round((degrees(a2 - a1) + 180) % 360 - 180))
    return sides, turns


def simplify(poly, tol=1e-6):
    """Drop collinear vertices."""
    out = []
    n = len(poly)
    for k in range(n):
        a, b, c = poly[k - 1], poly[k], poly[(k + 1) % n]
        cr = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        if abs(cr) > tol:
            out.append(b)
    return out


# ----------------------------------------------------------------- symmetries of the lattice

def rot60(p):
    i, j = p
    return (-j, i + j)


def refl(p):
    i, j = p
    return (j, i)


def sym_maps():
    maps = []
    for r in range(6):
        for s in range(2):
            def f(p, r=r, s=s):
                if s:
                    p = refl(p)
                for _ in range(r):
                    p = rot60(p)
                return p
            maps.append(f)
    return maps


SYMS = sym_maps()


def map_cells(f, cells):
    return frozenset(frozenset(f(v) for v in c) for c in cells)


def normalize(cells):
    pts = [v for c in cells for v in c]
    mi = min(p[0] for p in pts)
    mj = min(p[1] for p in pts)
    return tuple(sorted(tuple(sorted((v[0] - mi, v[1] - mj) for v in c)) for c in cells))


def canon(cells):
    return min(normalize(map_cells(f, cells)) for f in SYMS)


def half_turn_centre(R):
    """Return (centre in doubled lattice coords, kind) if R has half-turn symmetry, else None.
    kind is 'vertex' (lattice point) or 'edge' (midpoint of a lattice edge)."""
    pts = [v for c in R for v in c]
    for c0 in [c for c in R]:
        pass
    # candidate centre = (min+max)/2 of the vertex set in lattice coords (point reflection keeps bbox)
    si = min(p[0] for p in pts) + max(p[0] for p in pts)
    sj = min(p[1] for p in pts) + max(p[1] for p in pts)
    img = frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in R)
    if img != frozenset(R):
        return None
    kind = 'vertex' if si % 2 == 0 and sj % 2 == 0 else 'edge'
    return (si, sj), kind


# ----------------------------------------------------------------- pieces

def nbrs(R, c):
    return [d for d in R if adjacent(c, d)]


def blues(R):
    R = set(R)
    out = set()
    for c in R:
        for d in nbrs(R, c):
            out.add(frozenset([c, d]))
    return sorted(out, key=lambda p: sorted(sorted(c) for c in p))


def reds(R):
    R = set(R)
    out = set()
    for c in R:
        for a, b in combinations(nbrs(R, c), 2):
            out.add(frozenset([c, a, b]))
    return sorted(out, key=lambda p: sorted(sorted(c) for c in p))


def unit_hex(p):
    i, j = p
    return frozenset([U(i, j), D(i - 1, j), U(i - 1, j), D(i - 1, j - 1), U(i, j - 1), D(i, j - 1)])


def yellows(R):
    R = set(R)
    pts = {v for c in R for v in c}
    out = []
    for p in sorted(pts):
        h = unit_hex(p)
        if h <= R:
            out.append(h)
    return out


def greens(R):
    return [frozenset([c]) for c in sorted(R, key=sorted)]


def kind_of(p):
    return {1: 'green', 2: 'blue', 3: 'red', 6: 'yellow'}[len(p)]


def check_unit_hex(h):
    """A 6-cell piece is a yellow only if its cells surround one lattice point."""
    common = frozenset.intersection(*h)
    return len(common) == 1


# ----------------------------------------------------------------- exact cover

def cell_order(R):
    return sorted(R, key=lambda c: (centroid(c)[1], centroid(c)[0]))


def _prep(R, pieces):
    order = cell_order(R)
    idx = {c: k for k, c in enumerate(order)}
    masks = []
    for p in pieces:
        m = 0
        for c in p:
            m |= 1 << idx[c]
        masks.append(m)
    by_first = [[] for _ in order]
    for k, m in enumerate(masks):
        low = (m & -m).bit_length() - 1
        by_first[low].append(k)
    return order, idx, masks, by_first


def count_tilings(R, pieces):
    order, idx, masks, by_first = _prep(R, pieces)
    full = (1 << len(order)) - 1

    @lru_cache(maxsize=None)
    def rec(used):
        if used == full:
            return 1
        i = (~used & (used + 1)).bit_length() - 1
        tot = 0
        for k in by_first[i]:
            if not masks[k] & used:
                tot += rec(used | masks[k])
        return tot
    return rec(0)


def all_tilings(R, pieces, limit=10 ** 6):
    order, idx, masks, by_first = _prep(R, pieces)
    full = (1 << len(order)) - 1
    res = []

    def rec(used, chosen):
        if len(res) >= limit:
            return
        if used == full:
            res.append(frozenset(pieces[k] for k in chosen))
            return
        i = (~used & (used + 1)).bit_length() - 1
        for k in by_first[i]:
            if not masks[k] & used:
                chosen.append(k)
                rec(used | masks[k], chosen)
                chosen.pop()
    rec(0, [])
    return res


def fewest(R, pieces):
    """Minimum number of pieces in a tiling, the number of minimum tilings, and a Counter
    of the colour mixes (yellow, red, blue, green) of the minimum tilings.  Also the
    minimum for each number of yellows."""
    order, idx, masks, by_first = _prep(R, pieces)
    full = (1 << len(order)) - 1
    kinds = [kind_of(p) for p in pieces]
    INF = 10 ** 9

    @lru_cache(maxsize=None)
    def rec(used):
        # returns dict: nyellow -> (min pieces, count, frozenset of mixes)
        if used == full:
            return {0: (0, 1, frozenset([(0, 0, 0, 0)]))}
        i = (~used & (used + 1)).bit_length() - 1
        best = {}
        for k in by_first[i]:
            if masks[k] & used:
                continue
            sub = rec(used | masks[k])
            kd = kinds[k]
            for ny, (mn, cnt, mixes) in sub.items():
                ny2 = ny + (kd == 'yellow')
                add = {'yellow': (1, 0, 0, 0), 'red': (0, 1, 0, 0), 'blue': (0, 0, 1, 0), 'green': (0, 0, 0, 1)}[kd]
                mixes2 = frozenset(tuple(a + b for a, b in zip(m, add)) for m in mixes)
                cur = best.get(ny2)
                if cur is None or mn + 1 < cur[0]:
                    best[ny2] = (mn + 1, cnt, mixes2)
                elif mn + 1 == cur[0]:
                    best[ny2] = (cur[0], cur[1] + cnt, cur[2] | mixes2)
        return best
    r = rec(0)
    rec.cache_clear()
    if not r:
        return None
    mn = min(v[0] for v in r.values())
    cnt = sum(v[1] for v in r.values() if v[0] == mn)
    mixes = frozenset().union(*[v[2] for v in r.values() if v[0] == mn])
    return mn, cnt, mixes, r


def min_tilings(R, pieces, target):
    """All tilings with exactly `target` pieces (enumerated with pruning)."""
    order, idx, masks, by_first = _prep(R, pieces)
    full = (1 << len(order)) - 1
    res = []
    maxsize = max(len(p) for p in pieces)

    def rec(used, chosen):
        left = len(order) - bin(used).count('1')
        if len(chosen) + (left + maxsize - 1) // maxsize > target:
            return
        if used == full:
            if len(chosen) == target:
                res.append(frozenset(pieces[k] for k in chosen))
            return
        i = (~used & (used + 1)).bit_length() - 1
        for k in by_first[i]:
            if not masks[k] & used:
                chosen.append(k)
                rec(used | masks[k], chosen)
                chosen.pop()
    rec(0, [])
    return res


def max_packing(R, pieces):
    """Maximum number of disjoint pieces and all maximum packings (small cases)."""
    best = [0, []]
    n = len(pieces)

    def rec(k, used, chosen):
        if len(chosen) + (n - k) < best[0]:
            return
        if k == n:
            if len(chosen) > best[0]:
                best[0], best[1] = len(chosen), [frozenset(chosen)]
            elif len(chosen) == best[0]:
                best[1].append(frozenset(chosen))
            return
        p = pieces[k]
        if not (p & used):
            chosen.append(p)
            rec(k + 1, used | p, chosen)
            chosen.pop()
        rec(k + 1, used, chosen)
    rec(0, frozenset(), [])
    return best[0], best[1]


# ----------------------------------------------------------------- the placement game

def components(cells):
    cells = set(cells)
    out = []
    while cells:
        c = cells.pop()
        comp = {c}
        stack = [c]
        while stack:
            x = stack.pop()
            for y in list(cells):
                if adjacent(x, y):
                    cells.discard(y)
                    comp.add(y)
                    stack.append(y)
        out.append(frozenset(comp))
    return out


_G = {}


def grundy(cells):
    """Sprague-Grundy value of the rhombus-placement game on the free cells `cells`
    (normal play: a player who cannot place loses).  Independent components add (XOR)."""
    g = 0
    for comp in components(cells):
        g ^= grundy_comp(comp)
    return g


def grundy_comp(comp):
    key = canon(comp)
    if key in _G:
        return _G[key]
    opts = set()
    for m in blues(comp):
        opts.add(grundy(comp - m))
    v = 0
    while v in opts:
        v += 1
    _G[key] = v
    return v


def winner(R):
    """('1st' or '2nd', winning first moves, all first moves)."""
    R = frozenset(R)
    moves = blues(R)
    good = [m for m in moves if grundy(R - m) == 0]
    return ('1st' if good else '2nd'), good, moves


def game_lengths(R):
    """Set of possible game lengths (all maximal play sequences)."""
    R = frozenset(R)

    @lru_cache(maxsize=None)
    def rec(free):
        ms = blues(free)
        if not ms:
            return frozenset([0])
        out = set()
        for m in ms:
            out |= {k + 1 for k in rec(free - m)}
        return frozenset(out)
    return rec(R)


# ----------------------------------------------------------------- descriptions

def describe(R):
    u = sum(1 for c in R if is_up(c))
    return f'{len(R)} cells ({u} up, {len(R) - u} down)'
