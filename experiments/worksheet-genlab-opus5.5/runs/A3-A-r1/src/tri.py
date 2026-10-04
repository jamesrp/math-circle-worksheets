"""Triangular-grid geometry, solvers, and TikZ drawing for the Week 1 tiling pages.

Lattice point (i, j) has Cartesian position (i + j/2, j*sqrt(3)/2), in inches when
drawn at actual size (small triangle edge = 1 inch).
A triangle is (i, j, 'U') or (i, j, 'D').
  U(i,j): (i,j), (i+1,j), (i,j+1)
  D(i,j): (i+1,j), (i,j+1), (i+1,j+1)
"""
import math
from functools import lru_cache

S3 = math.sqrt(3) / 2
DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]  # 0,60,...,300 degrees


def cart(p):
    i, j = p
    return (i + j / 2.0, j * S3)


def verts(t):
    i, j, k = t
    if k == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i, j + 1), (i + 1, j + 1)]


def centroid(t):
    vs = [cart(v) for v in verts(t)]
    return (sum(v[0] for v in vs) / 3, sum(v[1] for v in vs) / 3)


def edges(t):
    v = verts(t)
    return [tuple(sorted((v[a], v[b]))) for a, b in ((0, 1), (1, 2), (0, 2))]


def neighbors(t):
    i, j, k = t
    if k == 'U':
        return [(i, j, 'D'), (i - 1, j, 'D'), (i, j - 1, 'D')]
    return [(i, j, 'U'), (i + 1, j, 'U'), (i, j + 1, 'U')]


def sector(v, k):
    """Triangle in sector k (k*60..(k+1)*60 degrees) around lattice vertex v."""
    i, j = v
    k %= 6
    return [(i, j, 'U'), (i - 1, j, 'D'), (i - 1, j, 'U'),
            (i - 1, j - 1, 'D'), (i, j - 1, 'U'), (i, j - 1, 'D')][k]


# ---------------------------------------------------------------- regions

def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for a in range(n):
        x1, y1 = poly[a]
        x2, y2 = poly[(a + 1) % n]
        if (y1 > y) != (y2 > y):
            xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xc > x:
                inside = not inside
    return inside


def turtle(steps, start=(0, 0)):
    """steps: list of (direction index, length). Returns lattice polygon vertices."""
    pts = [start]
    i, j = start
    for d, n in steps:
        di, dj = DIRS[d % 6]
        i += di * n
        j += dj * n
        pts.append((i, j))
    assert pts[-1] == start, ("not closed", pts[-1])
    return pts[:-1]


def region_from_poly(lattice_poly):
    poly = [cart(p) for p in lattice_poly]
    ii = [p[0] for p in lattice_poly]
    jj = [p[1] for p in lattice_poly]
    out = set()
    for i in range(min(ii) - min(jj) - max(jj) - 2, max(ii) + max(jj) - min(jj) + 3):
        for j in range(min(jj) - 1, max(jj) + 1):
            for k in 'UD':
                t = (i, j, k)
                if point_in_poly(centroid(t), poly):
                    out.add(t)
    return frozenset(out)


def big_triangle(n, origin=(0, 0)):
    oi, oj = origin
    s = set()
    for i in range(n):
        for j in range(n - i):
            s.add((oi + i, oj + j, 'U'))
            if i + j <= n - 2:
                s.add((oi + i, oj + j, 'D'))
    return frozenset(s)


def hexagon(a, b, c, start=(0, 0)):
    """Bottom side a (horizontal), then b at 60deg, c at 120deg, a, b, c."""
    return region_from_poly(turtle([(0, a), (1, b), (2, c), (3, a), (4, b), (5, c)], start))


def counts(R):
    u = sum(1 for t in R if t[2] == 'U')
    return u, len(R) - u


# ---------------------------------------------------------------- pieces

PIECE_SECTORS = {'G': [1], 'B': [2], 'R': [3], 'P': [4], 'Y': [6]}


def placements(R, kind):
    """All placements of a piece kind inside region R, as frozensets of triangles."""
    n = {'G': 1, 'B': 2, 'R': 3, 'P': 4, 'Y': 6}[kind]
    if n == 1:
        return [frozenset([t]) for t in R]
    vs = set()
    for t in R:
        vs.update(verts(t))
    out = set()
    for v in vs:
        rots = range(1) if n == 6 else range(6)
        for r in rots:
            tri = frozenset(sector(v, r + k) for k in range(n))
            if tri <= R:
                out.add(tri)
    return sorted(out, key=lambda p: sorted(p))


def count_tilings(R, kinds=('B',), limit=None, collect=False):
    R = frozenset(R)
    pl = []
    for k in kinds:
        pl += [(k, p) for p in placements(R, k)]
    by_tri = {}
    for k, p in pl:
        for t in p:
            by_tri.setdefault(t, []).append((k, p))
    order = sorted(R)
    sols = []
    cnt = [0]

    def rec(covered, chosen):
        if limit and cnt[0] >= limit:
            return
        first = None
        for t in order:
            if t not in covered:
                first = t
                break
        if first is None:
            cnt[0] += 1
            if collect:
                sols.append(list(chosen))
            return
        for k, p in by_tri.get(first, []):
            if not (p & covered):
                chosen.append((k, p))
                rec(covered | p, chosen)
                chosen.pop()

    rec(frozenset(), [])
    return (cnt[0], sols) if collect else cnt[0]


def max_matching(R):
    """Max number of blue rhombi that fit (bipartite matching U-D)."""
    R = set(R)
    ups = [t for t in R if t[2] == 'U']
    match_d = {}

    def aug(u, seen):
        for d in neighbors(u):
            if d in R and d not in seen:
                seen.add(d)
                if d not in match_d or aug(match_d[d], seen):
                    match_d[d] = u
                    return True
        return False

    m = 0
    for u in ups:
        if aug(u, set()):
            m += 1
    return m


def min_pieces(R, kinds, weight=None, best_known=None):
    """Minimum total weight to cover R exactly with pieces of the given kinds.
    weight: dict kind->cost (default 1 each). Returns (cost, solution)."""
    R = frozenset(R)
    weight = weight or {k: 1 for k in kinds}
    pl = []
    for k in kinds:
        pl += [(k, p) for p in placements(R, k)]
    by_tri = {}
    for k, p in pl:
        for t in p:
            by_tri.setdefault(t, []).append((k, p))
    for t in by_tri:
        by_tri[t].sort(key=lambda kp: -len(kp[1]))
    order = sorted(R)
    best = [best_known if best_known is not None else 10 ** 9, None]
    maxsize = max(len(p) for k, p in pl)
    minw_per_tri = min(weight[k] / {'G': 1, 'B': 2, 'R': 3, 'P': 4, 'Y': 6}[k] for k in kinds)

    def rec(covered, cost, chosen):
        remaining = len(R) - len(covered)
        if cost + remaining * minw_per_tri >= best[0] - 1e-9 and remaining > 0:
            return
        first = None
        for t in order:
            if t not in covered:
                first = t
                break
        if first is None:
            if cost < best[0]:
                best[0] = cost
                best[1] = list(chosen)
            return
        for k, p in by_tri.get(first, []):
            if not (p & covered):
                chosen.append((k, p))
                rec(covered | p, cost + weight[k], chosen)
                chosen.pop()

    rec(frozenset(), 0, [])
    return best[0], best[1]


# ---------------------------------------------------------------- games

def game_outcome(R, kinds=('B',)):
    """Normal play (last placement wins). Returns True if first player wins,
    plus the list of winning first moves."""
    R = frozenset(R)
    pl = []
    for k in kinds:
        pl += placements(R, k)

    @lru_cache(maxsize=None)
    def win(covered):
        for p in pl:
            if not (p & covered):
                if not win(covered | p):
                    return True
        return False

    first = win(frozenset())
    good = [p for p in pl if not win(frozenset(p))]
    return first, good


# ---------------------------------------------------------------- lozenge tilings

def lozenge_type(p):
    """'L', 'R' (have horizontal edges) or 'V'."""
    a, b = sorted(p, key=lambda t: t[2])  # D before U
    d, u = a, b
    if d[2] != 'D':
        d, u = b, a
    di, dj, _ = d
    ui, uj, _ = u
    if (ui, uj) == (di, dj):
        return 'R'   # looks like '/': top edge to the right of bottom edge
    if (ui, uj) == (di + 1, dj):
        return 'L'   # looks like '\\'
    return 'V'


def ribbons(R, tiling):
    """For a hexagon region with horizontal top side, follow chains from each top edge."""
    tri_to_tile = {}
    for p in tiling:
        for t in p:
            tri_to_tile[t] = p
    topj = max(t[1] for t in R if t[2] == 'D') + 1
    tops = sorted(t for t in R if t[2] == 'D' and t[1] == topj - 1)
    words = []
    for d in tops:
        w = ''
        cur = d
        while cur in tri_to_tile:
            p = tri_to_tile[cur]
            typ = lozenge_type(p)
            assert typ in 'LR', (cur, p)
            w += typ
            u = [t for t in p if t[2] == 'U'][0]
            nxt = (u[0], u[1] - 1, 'D')
            if nxt not in R:
                break
            cur = nxt
        words.append(w)
    return words


def flip_neighbors(R, tiling):
    """Tilings reachable by one flip (tiling given as frozenset of frozensets)."""
    tset = set(tiling)
    vs = set()
    for t in R:
        vs.update(verts(t))
    out = []
    for v in vs:
        secs = [sector(v, k) for k in range(6)]
        if not all(s in R for s in secs):
            continue
        A = [frozenset((secs[0], secs[1])), frozenset((secs[2], secs[3])), frozenset((secs[4], secs[5]))]
        B = [frozenset((secs[1], secs[2])), frozenset((secs[3], secs[4])), frozenset((secs[5], secs[0]))]
        if all(x in tset for x in A):
            out.append(frozenset((tset - set(A)) | set(B)))
        elif all(x in tset for x in B):
            out.append(frozenset((tset - set(B)) | set(A)))
    return out


def all_lozenge_tilings(R):
    n, sols = count_tilings(R, ('B',), collect=True)
    res = [frozenset(p for k, p in s) for s in sols]
    return sorted(res, key=lambda t: sorted(sorted(p) for p in t))


def flip_graph(R):
    tl = all_lozenge_tilings(R)
    idx = {t: n for n, t in enumerate(tl)}
    adj = {n: set() for n in range(len(tl))}
    for t in tl:
        for u in flip_neighbors(R, t):
            adj[idx[t]].add(idx[u])
    return tl, adj


def bfs(adj, s):
    dist = {s: 0}
    q = [s]
    for x in q:
        for y in adj[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist


# ---------------------------------------------------------------- drawing

COL = {'G': 'pbgreen', 'B': 'pbblue', 'R': 'pbred', 'Y': 'pbyellow', 'P': 'pbpurple'}


def fmt(x):
    s = f"{x:.4f}".rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def cxy(p, off=(0, 0)):
    x, y = cart(p)
    return f"({fmt(x + off[0])},{fmt(y + off[1])})"


def boundary_edges(R):
    cnt = {}
    for t in R:
        for e in edges(t):
            cnt[e] = cnt.get(e, 0) + 1
    return [e for e, c in cnt.items() if c == 1]


def tile_polygon(p):
    """Ordered outline vertices of a simply connected set of triangles."""
    adj = {}
    for a, b in boundary_edges(p):
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    start = min(adj)
    poly = [start]
    prev, cur = None, start
    while True:
        nxts = [x for x in adj[cur] if x != prev]
        nxt = nxts[0]
        if nxt == start:
            break
        poly.append(nxt)
        prev, cur = cur, nxt
        if len(poly) > len(adj):
            raise ValueError('not a simple outline')
    return poly


def bbox(R):
    pts = [cart(v) for t in R for v in verts(t)]
    return (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))


def tikz_region(R, scale=1.0, grid=True, holes=(), tiles=(), tile_fill=True, outline_w='1.6pt',
                grid_color='black!35', grid_w='0.5pt', label=None, label_pos='below', extra='',
                normalize=True, fill_board=None, hole_fill='black!55', tile_w=None, dots=False):
    """Return a tikzpicture drawing region R. Units: scale inches per small-triangle edge."""
    R = frozenset(R)
    allR = R | frozenset(holes)
    x0, y0, x1, y1 = bbox(allR)
    off = (-x0, -y0) if normalize else (0, 0)
    L = []
    L.append(f"\\begin{{tikzpicture}}[x={scale}in,y={scale}in,line join=round,line cap=round,baseline=(current bounding box.south)]")
    if fill_board:
        for t in R:
            v = verts(t)
            L.append(f"\\fill[{fill_board}] {cxy(v[0], off)}--{cxy(v[1], off)}--{cxy(v[2], off)}--cycle;")
    for t in holes:
        v = verts(t)
        L.append(f"\\fill[{hole_fill}] {cxy(v[0], off)}--{cxy(v[1], off)}--{cxy(v[2], off)}--cycle;")
    for k, p in tiles:
        if tile_fill:
            col = COL.get(k, k)
            poly = tile_polygon(p)
            L.append(f"\\fill[{col}] " + "--".join(cxy(v, off) for v in poly) + "--cycle;")
    if grid:
        es = set()
        for t in R:
            es.update(edges(t))
        bset = set(boundary_edges(allR))
        inner = [e for e in es if e not in bset]
        for a, b in sorted(inner):
            L.append(f"\\draw[{grid_color},line width={grid_w}] {cxy(a, off)}--{cxy(b, off)};")
    if dots:
        vs = set()
        for t in R:
            vs.update(verts(t))
        for v in sorted(vs):
            L.append(f"\\fill[black!60] {cxy(v, off)} circle (0.9pt);")
    for k, p in tiles:
        tw = tile_w or outline_w
        for a, b in boundary_edges(p):
            L.append(f"\\draw[black,line width={tw}] {cxy(a, off)}--{cxy(b, off)};")
    for a, b in boundary_edges(allR):
        L.append(f"\\draw[black,line width={outline_w}] {cxy(a, off)}--{cxy(b, off)};")
    if holes:
        for a, b in boundary_edges(frozenset(holes)):
            L.append(f"\\draw[black,line width={outline_w}] {cxy(a, off)}--{cxy(b, off)};")
    if extra:
        L.append(extra)
    L.append("\\end{tikzpicture}")
    return "\n".join(L)


def tikz_piece(kind, scale=0.35, rot=0):
    """Small colored picture of one block."""
    n = {'G': 1, 'B': 2, 'R': 3, 'P': 4, 'Y': 6}[kind]
    tri = frozenset(sector((0, 0), rot + k) for k in range(n))
    return tikz_region(tri, scale=scale, grid=False, tiles=[(kind, tri)], outline_w='0.8pt')
