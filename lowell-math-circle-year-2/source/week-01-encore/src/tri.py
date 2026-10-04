"""Triangle-grid geometry for pattern-block boards.

Lattice point (x, y) -> Cartesian (x + y/2, y*sqrt(3)/2), unit = one small edge (1 inch).
Up triangle   ('U', x, y): vertices (x,y), (x+1,y), (x,y+1)
Down triangle ('D', x, y): vertices (x+1,y), (x,y+1), (x+1,y+1)
"""
from math import sqrt
from functools import lru_cache
import itertools

S3 = sqrt(3) / 2


def cart(p):
    x, y = p
    return (x + y / 2.0, y * S3)


def verts(t):
    k, x, y = t
    if k == 'U':
        return [(x, y), (x + 1, y), (x, y + 1)]
    return [(x + 1, y), (x, y + 1), (x + 1, y + 1)]


def centroid(t):
    vs = [cart(v) for v in verts(t)]
    return (sum(v[0] for v in vs) / 3, sum(v[1] for v in vs) / 3)


def neighbors(t):
    k, x, y = t
    if k == 'U':
        return [('D', x, y), ('D', x - 1, y), ('D', x, y - 1)]
    return [('U', x, y), ('U', x + 1, y), ('U', x, y + 1)]


def edges_of(t):
    v = verts(t)
    return [frozenset((v[i], v[(i + 1) % 3])) for i in range(3)]


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


DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]  # 0,60,...,300 degrees


def path_poly(start, steps):
    """steps: list of (dir_index, length). Returns lattice vertices."""
    pts = [start]
    x, y = start
    for d, n in steps:
        dx, dy = DIRS[d]
        x, y = x + dx * n, y + dy * n
        pts.append((x, y))
    assert pts[-1] == pts[0], pts
    return pts[:-1]


def region_from_poly(lpoly):
    cpoly = [cart(p) for p in lpoly]
    xs = [p[0] for p in lpoly]
    ys = [p[1] for p in lpoly]
    R = set()
    for x in range(min(xs) - max(ys) - 2, max(xs) + 3):
        for y in range(min(ys) - 1, max(ys) + 2):
            for k in 'UD':
                t = (k, x, y)
                if point_in_poly(centroid(t), cpoly):
                    R.add(t)
    return R


def hexagon(a, b, c, start=(0, 0)):
    return path_poly(start, [(0, a), (1, b), (2, c), (3, a), (4, b), (5, c)])


def parallelogram(a, b, start=(0, 0)):
    return path_poly(start, [(0, a), (1, b), (3, a), (4, b)])


def triangle(n, start=(0, 0)):
    return path_poly(start, [(0, n), (2, n), (4, n)])


# ---------------------------------------------------------------- pieces

def rhombi(R):
    out = []
    for t in R:
        if t[0] == 'U':
            for u in neighbors(t):
                if u in R:
                    out.append(frozenset((t, u)))
    return out


def rhombus_dir(p):
    """Direction class of a rhombus = which edge it straddles: 0,1,2."""
    t, u = sorted(p)
    if t[0] == 'D':
        t, u = u, t
    _, x, y = t
    nb = neighbors(t)
    return nb.index(u)  # 0: D(x,y) slanted edge, 1: D(x-1,y) left edge, 2: D(x,y-1) bottom edge


def trapezoids(R):
    out = []
    for t in R:
        nb = [u for u in neighbors(t) if u in R]
        for a, b in itertools.combinations(nb, 2):
            out.append(frozenset((t, a, b)))
    return out


def trap_kind(p):
    ups = sum(1 for t in p if t[0] == 'U')
    return 'two-up' if ups == 2 else 'two-down'


def hexes(R):
    out = []
    pts = set()
    for t in R:
        pts.update(verts(t))
    for (x, y) in pts:
        h = frozenset([('U', x, y), ('D', x - 1, y), ('U', x - 1, y), ('D', x - 1, y - 1),
                       ('U', x, y - 1), ('D', x, y - 1)])
        if h <= R:
            out.append(h)
    return out


def greens(R):
    return [frozenset([t]) for t in R]


# ---------------------------------------------------------------- tiling enumeration

def tilings(R, pieces):
    R = frozenset(R)
    cover = {}
    for p in pieces:
        for t in p:
            cover.setdefault(t, []).append(p)
    order = sorted(R, key=lambda t: (centroid(t)[1], centroid(t)[0]))
    res = []

    def rec(i, used, chosen):
        while i < len(order) and order[i] in used:
            i += 1
        if i == len(order):
            res.append(list(chosen))
            return
        t = order[i]
        for p in cover.get(t, []):
            if not (p & used):
                chosen.append(p)
                rec(i + 1, used | p, chosen)
                chosen.pop()
    rec(0, frozenset(), [])
    return res


def count_tilings(R, pieces):
    R = frozenset(R)
    cover = {}
    for p in pieces:
        for t in p:
            cover.setdefault(t, []).append(p)
    order = sorted(R, key=lambda t: (centroid(t)[1], centroid(t)[0]))
    idx = {t: i for i, t in enumerate(order)}
    pmask = {}
    for p in pieces:
        m = 0
        for t in p:
            m |= 1 << idx[t]
        pmask[p] = m
    covl = [[pmask[p] for p in cover.get(t, [])] for t in order]
    full = (1 << len(order)) - 1

    @lru_cache(maxsize=None)
    def rec(used):
        if used == full:
            return 1
        i = (~used & (used + 1)).bit_length() - 1
        tot = 0
        for m in covl[i]:
            if not (m & used):
                tot += rec(used | m)
        return tot
    return rec(0)


# ---------------------------------------------------------------- placement game

def game_winner(R):
    """Return 'first' or 'second' for the rhombus placement game on region R."""
    order = sorted(R)
    idx = {t: i for i, t in enumerate(order)}
    moves = []
    for p in rhombi(R):
        m = 0
        for t in p:
            m |= 1 << idx[t]
        moves.append(m)

    @lru_cache(maxsize=None)
    def win(used):  # player to move wins?
        for m in moves:
            if not (m & used):
                if not win(used | m):
                    return True
        return False
    w = win(0)
    # also report winning first moves
    good = [m for m in moves if not win(m)]
    win.cache_clear()
    return ('first' if w else 'second'), len(good), len(moves)


def updown(R):
    u = sum(1 for t in R if t[0] == 'U')
    return u, len(R) - u


def from_ascii(lines):
    """Rows top to bottom; column h of row y is a triangle slot: U if (h-y) odd, D if even.
    Any non-space, non-'.' character marks a triangle."""
    R = set()
    n = len(lines)
    for i, line in enumerate(lines):
        y = n - 1 - i
        for h, ch in enumerate(line):
            if ch in ' .':
                continue
            if ch in '^v':
                assert (ch == '^') == bool((h - y) % 2), (i, h, ch)
            if (h - y) % 2:
                R.add(('U', (h - y - 1) // 2, y))
            else:
                R.add(('D', (h - y - 2) // 2, y))
    return R


def to_ascii(R):
    ys = [t[2] for t in R]
    hs = []
    rows = {}
    for t in R:
        k, x, y = t
        h = 2 * x + y + (1 if k == 'U' else 2)
        rows.setdefault(y, []).append(h)
        hs.append(h)
    mh = min(hs)
    mh -= mh % 2
    out = []
    for y in range(max(ys), min(ys) - 1, -1):
        s = [' '] * (max(hs) - mh + 1)
        for h in rows.get(y, []):
            s[h - mh] = '^' if (h - y) % 2 else 'v'
        out.append(''.join(s))
    return out
