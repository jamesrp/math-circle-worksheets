"""Triangular-grid geometry, tiling solver, and TikZ output for the pattern-block worksheets.

Lattice point (i, j) sits at x = i + j/2, y = j*H (H = sqrt(3)/2), so the grid has
horizontal lines and every small triangle points up or down.

  U(i,j): vertices (i,j), (i+1,j), (i,j+1)        -- points up
  D(i,j): vertices (i+1,j), (i,j+1), (i+1,j+1)    -- points down
"""
import math
from functools import lru_cache

H = math.sqrt(3) / 2


def xy(p):
    i, j = p
    return (i + j / 2.0, j * H)


def tri_verts(t):
    k, i, j = t
    if k == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i, j + 1), (i + 1, j + 1)]


def centroid(t):
    vs = [xy(v) for v in tri_verts(t)]
    return (sum(v[0] for v in vs) / 3, sum(v[1] for v in vs) / 3)


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for a in range(n):
        x1, y1 = xy(poly[a])
        x2, y2 = xy(poly[(a + 1) % n])
        if (y1 > y) != (y2 > y):
            xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xc > x:
                inside = not inside
    return inside


def region(polys, holes=()):
    """Set of triangles whose centroid lies in any of polys and not in holes (holes: triangles)."""
    allp = [v for p in polys for v in p]
    imin = min(v[0] for v in allp) - 2
    imax = max(v[0] for v in allp) + 2
    jmin = min(v[1] for v in allp) - 2
    jmax = max(v[1] for v in allp) + 2
    out = set()
    for i in range(imin - (jmax - jmin), imax + (jmax - jmin)):
        for j in range(jmin, jmax):
            for k in 'UD':
                t = (k, i, j)
                c = centroid(t)
                if any(point_in_poly(c, p) for p in polys):
                    out.add(t)
    return out - set(holes)


# ---------- shapes (lattice polygons) ----------

def hexagon(a, p, q, origin=(0, 0)):
    """Hexagon with bottom/top edges a, lower-right/upper-left p, upper-right/lower-left q."""
    ox, oy = origin
    vs = [(0, 0), (a, 0), (a, p), (a - q, p + q), (-q, p + q), (-q, q)]
    return [(ox + x, oy + y) for x, y in vs]


def big_up(n, origin=(0, 0)):
    ox, oy = origin
    return [(ox, oy), (ox + n, oy), (ox, oy + n)]


def big_down(n, origin=(0, 0)):
    ox, oy = origin
    return [(ox + n, oy), (ox + n, oy + n), (ox, oy + n)]


# ---------- adjacency, counts, solver ----------

def neighbors(t):
    k, i, j = t
    if k == 'U':
        return [('D', i, j), ('D', i - 1, j), ('D', i, j - 1)]
    return [('U', i, j), ('U', i + 1, j), ('U', i, j + 1)]


def rhombus_type(u, d):
    """Type of rhombus made of up-triangle u and adjacent down-triangle d.
    'L': leans like '/', going down the ribbon steps left.
    'R': leans like '\\', going down steps right.
    'S': standing diamond (no horizontal edges)."""
    _, i, j = u
    if d == ('D', i, j):
        return 'L'
    if d == ('D', i - 1, j):
        return 'R'
    if d == ('D', i, j - 1):
        return 'S'
    raise ValueError((u, d))


def counts(reg):
    up = sum(1 for t in reg if t[0] == 'U')
    return up, len(reg) - up


def all_tilings(reg, limit=10 ** 6):
    """All perfect matchings (rhombus tilings). Each tiling is a frozenset of (u, d) pairs."""
    reg = frozenset(reg)
    order = sorted(reg, key=lambda t: (-centroid(t)[1], centroid(t)[0]))
    res = []

    def rec(remaining, acc):
        if len(res) >= limit:
            return
        if not remaining:
            res.append(frozenset(acc))
            return
        # first uncovered triangle in reading order (top to bottom, left to right)
        for t in order:
            if t in remaining:
                break
        for n in neighbors(t):
            if n in remaining:
                pair = (t, n) if t[0] == 'U' else (n, t)
                rec(remaining - {t, n}, acc + [pair])

    rec(reg, [])
    return res


def max_matching(reg):
    """Size of a maximum matching (bipartite, simple augmenting paths)."""
    ups = [t for t in reg if t[0] == 'U']
    match_d = {}

    def try_aug(u, seen):
        for d in neighbors(u):
            if d in reg and d not in seen:
                seen.add(d)
                if d not in match_d or try_aug(match_d[d], seen):
                    match_d[d] = u
                    return True
        return False

    m = 0
    for u in ups:
        if try_aug(u, set()):
            m += 1
    return m


# ---------- edges ----------

def tri_edges(t):
    v = tri_verts(t)
    es = []
    for a in range(3):
        p, q = v[a], v[(a + 1) % 3]
        es.append(tuple(sorted([p, q])))
    return es


def edge_census(reg):
    cnt = {}
    for t in reg:
        for e in tri_edges(t):
            cnt[e] = cnt.get(e, 0) + 1
    interior = [e for e, c in cnt.items() if c == 2]
    boundary = [e for e, c in cnt.items() if c == 1]
    return interior, boundary


def boundary_loops(reg):
    """Chain boundary edges into closed loops of lattice points."""
    _, bnd = edge_census(reg)
    adj = {}
    for p, q in bnd:
        adj.setdefault(p, []).append(q)
        adj.setdefault(q, []).append(p)
    used = set()
    loops = []
    for e in bnd:
        if e in used:
            continue
        p, q = e
        loop = [p]
        used.add(e)
        prev, cur = p, q
        while cur != p:
            loop.append(cur)
            nxts = [n for n in adj[cur] if tuple(sorted([cur, n])) not in used]
            # prefer going straight when several choices (pinch points)
            if not nxts:
                break
            n = nxts[0]
            used.add(tuple(sorted([cur, n])))
            prev, cur = cur, n
        loops.append(loop)
    return loops


def simplify_loop(loop):
    """Drop collinear intermediate points."""
    out = []
    n = len(loop)
    for k in range(n):
        a, b, c = loop[k - 1], loop[k], loop[(k + 1) % n]
        d1 = (b[0] - a[0], b[1] - a[1])
        d2 = (c[0] - b[0], c[1] - b[1])
        if d1 != d2:
            out.append(b)
    return out


# ---------- TikZ helpers ----------

def fmt(v):
    s = f"{v:.4f}".rstrip('0').rstrip('.')
    return s if s not in ('-0', '') else '0'


def P(p, s=1.0, off=(0, 0)):
    x, y = xy(p)
    return f"({fmt(x * s + off[0])},{fmt(y * s + off[1])})"


def poly_path(pts, s=1.0, off=(0, 0)):
    return ' -- '.join(P(p, s, off) for p in pts) + ' -- cycle'


def bbox(reg):
    pts = [xy(v) for t in reg for v in tri_verts(t)]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def rhombus_pts(u, d):
    """Polygon of the rhombus (lattice points, in order)."""
    vs = set(tri_verts(u)) | set(tri_verts(d))
    shared = set(tri_verts(u)) & set(tri_verts(d))
    (a,) = set(tri_verts(u)) - shared
    (b,) = set(tri_verts(d)) - shared
    s1, s2 = sorted(shared)
    return [a, s1, b, s2]


# ---------- ribbons ----------

def tiling_map(tiling):
    """triangle -> (u, d, type)"""
    m = {}
    for u, d in tiling:
        typ = rhombus_type(u, d)
        m[u] = (u, d, typ)
        m[d] = (u, d, typ)
    return m


def ribbons_from_top(tiling, top_level, top_edges_i):
    """For each top horizontal edge ((i,top),(i+1,top)) follow the ribbon down.
    Returns list of (word, [rhombi]) ."""
    m = tiling_map(tiling)
    out = []
    for i0 in top_edges_i:
        i, j = i0, top_level
        word = []
        rh = []
        while j > 0:
            d = ('D', i, j - 1)
            if d not in m:
                break
            u, dd, typ = m[d]
            rh.append((u, dd))
            if typ == 'L':
                word.append('L')
                i = u[1]  # base of U(i,j-1) is ((i,j-1),(i+1,j-1))
            elif typ == 'R':
                word.append('R')
                i = u[1]
            else:
                raise ValueError('standing rhombus on a ribbon?')
            j -= 1
        out.append((''.join(word), rh))
    return out
