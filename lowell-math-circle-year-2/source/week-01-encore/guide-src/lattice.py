"""Independent geometry and solvers for the adult guide's answer check.

Nothing here imports the student-page sources.  Boards are rebuilt from the
coordinates printed in the student figures (final/src/figs/*.tex): every closed
outline, grid segment and drawn piece is read back from the TikZ, mapped onto the
triangle lattice, and the small triangles inside it are recomputed.

Lattice point (x, y) sits at (x + y/2, y*sqrt(3)/2) in units of one small edge.
A triangle is a frozenset of its three lattice vertices.
"""
import math
import os
import re
from collections import deque
from functools import lru_cache
from itertools import combinations

S3 = math.sqrt(3) / 2
FIGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'figs')

# ------------------------------------------------------------------ reading the TikZ

NUM = r'-?\d+(?:\.\d+)?'
PT = re.compile(r'\((' + NUM + r'),(' + NUM + r')\)')
CMD = re.compile(r'^\\(draw|fill|filldraw|node|path)\[([^\]]*)\](.*);\s*$')


class Shape:
    def __init__(self, kind, style, pts):
        self.kind, self.style, self.pts = kind, style, pts

    @property
    def bbox(self):
        xs = [p[0] for p in self.pts]
        ys = [p[1] for p in self.pts]
        return min(xs), min(ys), max(xs), max(ys)


def read_fig(name):
    """Return (loops, segments, pieces, fills, texts) of figure `name`.
    loops: closed outlines drawn with \\draw; pieces: \\filldraw polygons with their fill;
    fills: \\fill polygons with their colour; segments: open grid segments; texts: nodes."""
    loops, segs, pieces, fills, texts = [], [], [], [], []
    with open(os.path.join(FIGS, name + '.tex')) as fh:
        for line in fh:
            m = CMD.match(line.strip())
            if not m:
                continue
            kind, style, rest = m.groups()
            if kind == 'node':
                p = PT.search(rest)
                t = rest[rest.index('{') + 1:rest.rindex('}')]
                texts.append((float(p.group(1)), float(p.group(2)), t))
                continue
            if 'rectangle' in rest:
                continue
            if 'cycle' in rest:
                for chunk in rest.split('cycle'):
                    pts = [(float(a), float(b)) for a, b in PT.findall(chunk)]
                    if len(pts) < 3:
                        continue
                    if kind == 'filldraw':
                        fill = re.search(r'fill=([^,]+)', style).group(1)
                        pieces.append(Shape(fill, style, pts))
                    elif kind == 'fill':
                        fills.append(Shape(style.split(',')[0], style, pts))
                    elif kind == 'draw':
                        loops.append(Shape('loop', style, pts))
            elif kind == 'draw':
                for a, b in re.findall(r'(\(' + NUM + ',' + NUM + r'\)) -- (\(' + NUM + ',' + NUM + r'\))', rest):
                    pa = tuple(float(v) for v in PT.match(a).groups())
                    pb = tuple(float(v) for v in PT.match(b).groups())
                    segs.append((pa, pb))
    return loops, segs, pieces, fills, texts


def reading_order(shapes):
    """Top to bottom, then left to right (rows grouped by vertical overlap)."""
    shapes = sorted(shapes, key=lambda s: -s.bbox[3])
    rows = []
    for s in shapes:
        for r in rows:
            top, bot = r[0].bbox[3], r[0].bbox[1]
            if s.bbox[1] < top and s.bbox[3] > bot and abs(s.bbox[3] - top) < 0.6 * (top - bot):
                r.append(s)
                break
        else:
            rows.append([s])
    out = []
    for r in rows:
        out += sorted(r, key=lambda s: s.bbox[0])
    return out


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            if x1 + (y - y1) * (x2 - x1) / (y2 - y1) > x:
                inside = not inside
    return inside


def seg_len(s):
    (a, b), (c, d) = s
    return math.hypot(c - a, d - b)


# ------------------------------------------------------------------ frames and regions

class Frame:
    """Maps page inches to lattice coordinates: origin at a page point, a rotation that
    makes the shape's edges point at multiples of 60 degrees, and the small-edge length."""

    def __init__(self, poly, unit):
        (x0, y0), (x1, y1) = poly[0], poly[1]
        th = math.degrees(math.atan2(y1 - y0, x1 - x0)) % 60
        if th > 59.9:
            th = 0.0
        self.rot = th
        self.o = (x0, y0)
        self.unit = unit

    def to_lat(self, p, tol=0.02):
        r = math.radians(-self.rot)
        dx, dy = (p[0] - self.o[0]) / self.unit, (p[1] - self.o[1]) / self.unit
        X = math.cos(r) * dx - math.sin(r) * dy
        Y = math.sin(r) * dx + math.cos(r) * dy
        ly = Y / S3
        lx = X - ly / 2
        rx, ry = round(lx), round(ly)
        assert abs(lx - rx) < tol and abs(ly - ry) < tol, (p, lx, ly)
        return (rx, ry)

    def to_page(self, q):
        X, Y = q[0] + q[1] / 2, q[1] * S3
        r = math.radians(self.rot)
        return (self.o[0] + self.unit * (math.cos(r) * X - math.sin(r) * Y),
                self.o[1] + self.unit * (math.sin(r) * X + math.cos(r) * Y))


def cart(q):
    return (q[0] + q[1] / 2, q[1] * S3)


def tri_up(x, y):
    return frozenset([(x, y), (x + 1, y), (x, y + 1)])


def tri_down(x, y):
    return frozenset([(x + 1, y), (x, y + 1), (x + 1, y + 1)])


def centroid(t):
    cs = [cart(v) for v in t]
    return (sum(c[0] for c in cs) / 3, sum(c[1] for c in cs) / 3)


def is_up(t):
    """Up in lattice terms: two vertices share the lowest lattice row."""
    ys = sorted(v[1] for v in t)
    return ys[0] == ys[1]


def region_of_lattice_poly(lpoly):
    cp = [cart(q) for q in lpoly]
    xs = [q[0] for q in lpoly]
    ys = [q[1] for q in lpoly]
    R = set()
    for y in range(min(ys) - 1, max(ys) + 1):
        for x in range(min(xs) - (max(ys) - min(ys)) - 2, max(xs) + (max(ys) - min(ys)) + 2):
            for t in (tri_up(x, y), tri_down(x, y)):
                if point_in_poly(centroid(t), cp):
                    R.add(t)
    return frozenset(R)


def simplify(lpoly):
    out = []
    n = len(lpoly)
    for i in range(n):
        a, b, c = cart(lpoly[i - 1]), cart(lpoly[i]), cart(lpoly[(i + 1) % n])
        if abs((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])) > 1e-9:
            out.append(lpoly[i])
    return out


def sides(lpoly):
    """Side lengths in small edges, starting from the lowest-leftmost corner going round."""
    lp = simplify(lpoly)
    n = len(lp)
    out = []
    for i in range(n):
        a, b = lp[i], lp[(i + 1) % n]
        dx, dy = b[0] - a[0], b[1] - a[1]
        out.append(max(abs(dx), abs(dy), abs(dx + dy)))
    return out


class Board:
    """A region read back from an outline on a student page."""

    def __init__(self, shape, unit):
        self.shape = shape
        self.frame = Frame(shape.pts, unit)
        self.lpoly = [self.frame.to_lat(p) for p in shape.pts]
        self.R = region_of_lattice_poly(self.lpoly)
        self.sides = sides(self.lpoly)

    def piece_of(self, poly):
        lp = [self.frame.to_lat(p) for p in poly]
        return region_of_lattice_poly(lp)

    @property
    def updown(self):
        u = sum(1 for t in self.R if is_up(t))
        return u, len(self.R) - u


def unit_from_grid(shape, segs):
    """Small-edge length from the grid segments drawn inside an outline (None if no grid)."""
    inside = [s for s in segs if point_in_poly(((s[0][0] + s[1][0]) / 2, (s[0][1] + s[1][1]) / 2), shape.pts)]
    if not inside:
        return None
    ls = sorted(seg_len(s) for s in inside)
    return ls[len(ls) // 2]


def boards_of(name, style_key=None, unit=None, skip_icons=False):
    """All outlines in figure `name` (optionally only those whose style contains style_key),
    in reading order, as Boards.  Unit from the grid if drawn, else `unit` (default 1 inch)."""
    loops, segs, pieces, fills, texts = read_fig(name)
    out = []
    for s in reading_order(loops):
        if style_key and style_key not in s.style:
            continue
        u = unit_from_grid(s, segs) or unit or 1.0
        try:
            out.append(Board(s, u))
        except AssertionError:
            if not skip_icons:      # only the small piece icons beside record boxes are skipped
                raise
    return out


# ------------------------------------------------------------------ pieces in a region

def adjacent(t, u):
    return len(t & u) == 2


def neighbours_in(R):
    R = list(R)
    nb = {t: [] for t in R}
    for i, t in enumerate(R):
        for u in R[i + 1:]:
            if adjacent(t, u):
                nb[t].append(u)
                nb[u].append(t)
    return nb


def greens(R):
    return [frozenset([t]) for t in R]


def blues(R):
    nb = neighbours_in(R)
    return list({frozenset([t, u]) for t in R for u in nb[t]})


def reds(R):
    nb = neighbours_in(R)
    out = set()
    for t in R:
        for a, b in combinations(nb[t], 2):
            out.add(frozenset([t, a, b]))
    return list(out)


def yellows(R):
    pts = set().union(*R)
    out = []
    for (x, y) in pts:
        h = frozenset([tri_up(x, y), tri_down(x - 1, y), tri_up(x - 1, y), tri_down(x - 1, y - 1),
                       tri_up(x, y - 1), tri_down(x, y - 1)])
        if h <= R:
            out.append(h)
    return out


def colour(p):
    return {1: 'green', 2: 'blue', 3: 'red', 6: 'yellow'}[len(p)]


# ------------------------------------------------------------------ tilings

class Tiler:
    def __init__(self, R, pieces):
        self.R = frozenset(R)
        self.order = sorted(R, key=lambda t: (centroid(t)[1], centroid(t)[0]))
        self.idx = {t: i for i, t in enumerate(self.order)}
        self.pieces = list(pieces)
        self.mask = [sum(1 << self.idx[t] for t in p) for p in self.pieces]
        self.cover = [[] for _ in self.order]
        for k, p in enumerate(self.pieces):
            for t in p:
                self.cover[self.idx[t]].append(k)
        self.full = (1 << len(self.order)) - 1

    def first_free(self, used):
        return (~used & (used + 1)).bit_length() - 1

    def count(self):
        @lru_cache(maxsize=None)
        def rec(used):
            if used == self.full:
                return 1
            i = self.first_free(used)
            return sum(rec(used | self.mask[k]) for k in self.cover[i] if not self.mask[k] & used)
        return rec(0)

    def all(self, limit=10 ** 6):
        out = []

        def rec(used, chosen):
            if len(out) >= limit:
                return
            if used == self.full:
                out.append(frozenset(self.pieces[k] for k in chosen))
                return
            i = self.first_free(used)
            for k in self.cover[i]:
                if not self.mask[k] & used:
                    chosen.append(k)
                    rec(used | self.mask[k], chosen)
                    chosen.pop()
        rec(0, [])
        return out

    def all_with(self, n):
        """All tilings with exactly n pieces (pruned by area: no piece covers more than 6)."""
        big = max(len(p) for p in self.pieces)
        out = []

        def rec(used, chosen, left):
            if used == self.full:
                if len(chosen) == n:
                    out.append(frozenset(self.pieces[k] for k in chosen))
                return
            if len(chosen) + -(-left // big) > n:
                return
            i = self.first_free(used)
            for k in self.cover[i]:
                if not self.mask[k] & used:
                    chosen.append(k)
                    rec(used | self.mask[k], chosen, left - len(self.pieces[k]))
                    chosen.pop()
        rec(0, [], len(self.order))
        return out

    def fewest(self):
        """(fewest pieces, one tiling with that many) or (None, None)."""
        @lru_cache(maxsize=None)
        def rec(used):
            if used == self.full:
                return 0
            i = self.first_free(used)
            best = None
            for k in self.cover[i]:
                if not self.mask[k] & used:
                    r = rec(used | self.mask[k])
                    if r is not None and (best is None or r + 1 < best):
                        best = r + 1
            return best
        n = rec(0)
        if n is None:
            return None, None
        used, chosen = 0, []
        while used != self.full:
            i = self.first_free(used)
            for k in self.cover[i]:
                if not self.mask[k] & used and rec(used | self.mask[k]) == rec(used) - 1:
                    chosen.append(self.pieces[k])
                    used |= self.mask[k]
                    break
        return n, chosen

    def most(self):
        @lru_cache(maxsize=None)
        def rec(used):
            if used == self.full:
                return 0
            i = self.first_free(used)
            best = None
            for k in self.cover[i]:
                if not self.mask[k] & used:
                    r = rec(used | self.mask[k])
                    if r is not None and (best is None or r + 1 > best):
                        best = r + 1
            return best
        return rec(0)


def components(cells, nb):
    cells = set(cells)
    out = []
    while cells:
        s = cells.pop()
        comp = {s}
        q = [s]
        while q:
            c = q.pop()
            for d in nb[c]:
                if d in cells:
                    cells.remove(d)
                    comp.add(d)
                    q.append(d)
        out.append(frozenset(comp))
    return out


# ------------------------------------------------------------------ the placement game

def _tri_key(t):
    """(kind, x, y) for a triangle given by its vertex set."""
    vs = sorted(t, key=lambda v: (v[1], v[0]))
    if vs[0][1] == vs[1][1]:
        return ('U', vs[0][0], vs[0][1])
    return ('D', vs[0][0] - 1, vs[0][1])


def _key_tri(k):
    return tri_up(k[1], k[2]) if k[0] == 'U' else tri_down(k[1], k[2])


SYMS = []
for _refl in (False, True):
    for _r in range(6):
        def _f(v, r=_r, refl=_refl):
            x, y = v
            if refl:
                x, y = y, x
            for _ in range(r):
                x, y = -y, x + y
            return (x, y)
        SYMS.append(_f)


def canon(comp):
    best = None
    for f in SYMS:
        ks = [_tri_key(frozenset(f(v) for v in t)) for t in comp]
        mx = min(k[1] for k in ks)
        my = min(k[2] for k in ks)
        c = tuple(sorted((k[0], k[1] - mx, k[2] - my) for k in ks))
        if best is None or c < best:
            best = c
    return best


@lru_cache(maxsize=None)
def grundy_c(c):
    """Grundy value of the rhombus-placement game on the free cells c (canonical tuple)."""
    cells = [_key_tri(k) for k in c]
    if len(cells) < 2:
        return 0
    if len(cells) == 2:
        return 1 if adjacent(cells[0], cells[1]) else 0
    S = frozenset(cells)
    nb = neighbours_in(S)
    seen = set()
    for t in cells:
        for u in nb[t]:
            if _tri_key(t) < _tri_key(u):
                seen.add(grundy_set(S - {t, u}))
    g = 0
    while g in seen:
        g += 1
    return g


def grundy_set(S):
    nb = neighbours_in(S)
    g = 0
    for comp in components(S, nb):
        g ^= grundy_c(canon(comp))
    return g


def game(R):
    """('first'|'second', winning first moves, all first moves)."""
    R = frozenset(R)
    moves = blues(R)
    win = [m for m in moves if grundy_set(R - m) == 0]
    return ('first' if win else 'second'), win, moves


def half_turn(R):
    """Centre of the half turn taking R to itself (lattice coords x2), or None;
    and the placements that are their own half-turn image."""
    pts = set().union(*R)
    # the centre is the average of all vertices (exact for a centrally symmetric region)
    n = len(pts)
    cx2 = sum(2 * p[0] for p in pts)
    cy2 = sum(2 * p[1] for p in pts)
    if cx2 % n or cy2 % n:
        return None, None, []
    cx2 //= n
    cy2 //= n

    def img(t):
        return frozenset((cx2 - v[0], cy2 - v[1]) for v in t)
    if any(img(t) not in R for t in R):
        return None, None, []
    kind = 'grid point' if cx2 % 2 == 0 and cy2 % 2 == 0 else 'edge midpoint'
    selfs = [m for m in blues(R) if frozenset(img(t) for t in m) == m]
    return (cx2 / 2, cy2 / 2), kind, selfs


# ------------------------------------------------------------------ flips and moves

def unit_hexes(R):
    return yellows(R)


def rhombus_flip_graph(R, Ts):
    Tset = set(Ts)
    G = {T: [] for T in Ts}
    H = unit_hexes(R)
    for T in Ts:
        for h in H:
            inside = [p for p in T if p <= h]
            if len(inside) == 3:
                for alt in Tiler(h, blues(h)).all():
                    if set(alt) != set(inside):
                        T2 = frozenset((set(T) - set(inside)) | set(alt))
                        assert T2 in Tset
                        G[T].append(T2)
    return G


def bfs(G, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def is_bipartite(G):
    col = {}
    for s in G:
        if s in col:
            continue
        col[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in G[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    q.append(v)
                elif col[v] == col[u]:
                    return False
    return True
