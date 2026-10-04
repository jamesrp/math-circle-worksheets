"""Triangular-grid geometry, solvers, and TikZ output for the Week 1 tiling pages.

Lattice point (i, j) sits at Cartesian (i + j/2, j*H), H = sqrt(3)/2, in units of
one small-triangle edge (1 inch on actual-size boards).

Up-triangle   ('U', i, j): vertices (i,j), (i+1,j), (i,j+1)
Down-triangle ('D', i, j): vertices (i+1,j), (i+1,j+1), (i,j+1)
"""
import math
from functools import lru_cache

H = math.sqrt(3) / 2


def cart(p):
    i, j = p
    return (i + j / 2.0, j * H)


def verts(t):
    k, i, j = t
    if k == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i + 1, j + 1), (i, j + 1)]


def nbrs(t):
    k, i, j = t
    if k == 'U':
        return [('D', i, j), ('D', i - 1, j), ('D', i, j - 1)]
    return [('U', i, j), ('U', i + 1, j), ('U', i, j + 1)]


def centroid(t):
    vs = [cart(v) for v in verts(t)]
    return (sum(v[0] for v in vs) / 3, sum(v[1] for v in vs) / 3)


def edges(t):
    v = verts(t)
    return [frozenset((v[a], v[b])) for a, b in ((0, 1), (1, 2), (2, 0))]


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    for a in range(n):
        x1, y1 = poly[a]
        x2, y2 = poly[(a + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xi:
                inside = not inside
    return inside


def region_from_lattice_poly(lpts):
    """All triangles whose centroid lies inside the lattice polygon."""
    poly = [cart(p) for p in lpts]
    imin = min(p[0] for p in lpts) - 2 - max(p[1] for p in lpts)
    imax = max(p[0] for p in lpts) + 2 + max(p[1] for p in lpts)
    jmin = min(p[1] for p in lpts) - 1
    jmax = max(p[1] for p in lpts) + 1
    out = set()
    for i in range(imin, imax + 1):
        for j in range(jmin, jmax + 1):
            for k in 'UD':
                t = (k, i, j)
                if point_in_poly(*centroid(t), poly):
                    out.add(t)
    return frozenset(out)


DIRS = {  # lattice steps
    'E': (1, 0), 'W': (-1, 0),
    'NE': (0, 1), 'SW': (0, -1),
    'NW': (-1, 1), 'SE': (1, -1),
}


def walk(start, moves):
    """moves: list of (dir, length). Returns lattice polygon vertices."""
    p = start
    pts = [p]
    for d, n in moves:
        di, dj = DIRS[d]
        p = (p[0] + di * n, p[1] + dj * n)
        pts.append(p)
    assert pts[-1] == pts[0], ("polygon not closed", pts)
    return pts[:-1]


def hexagon(a, b, c, origin=(0, 0)):
    """Hexagon with horizontal top side a, then b down-right, c down-left, ...
    origin = bottom-left corner of the bottom side."""
    # start at bottom-left corner, go E a, NE b... choose: bottom side a (E),
    # then up-right side: going from bottom-right corner up to the right corner is
    # direction NE?  We want, clockwise from top-left: E a, SE b, SW c, W a, NW b, NE c.
    # Counter-clockwise from bottom-left: E a, NE c, NW b, W a, SW c, SE b.
    return region_from_lattice_poly(
        walk(origin, [('E', a), ('NE', c), ('NW', b), ('W', a), ('SW', c), ('SE', b)]))


def up_triangle(n, origin=(0, 0)):
    return region_from_lattice_poly(walk(origin, [('E', n), ('NW', n), ('SW', n)]))


def down_triangle(n, origin=(0, 0)):
    # origin = bottom vertex
    return region_from_lattice_poly(walk(origin, [('NE', n), ('W', n), ('SE', n)]))


def poly_region(origin, moves):
    return region_from_lattice_poly(walk(origin, moves))


def counts(region):
    u = sum(1 for t in region if t[0] == 'U')
    return u, len(region) - u


# ---------------------------------------------------------------- tilings

def rhombus_tilings(region, limit=None):
    """All tilings of region by rhombi; each tiling is a frozenset of frozenset pairs."""
    region = frozenset(region)
    order = sorted(region, key=lambda t: (-t[2], centroid(t)[0]))
    res = []

    def rec(covered, acc):
        if limit is not None and len(res) >= limit:
            return
        for t in order:
            if t not in covered:
                break
        else:
            res.append(frozenset(acc))
            return
        for n in nbrs(t):
            if n in region and n not in covered:
                acc.append(frozenset((t, n)))
                covered.add(t)
                covered.add(n)
                rec(covered, acc)
                covered.discard(t)
                covered.discard(n)
                acc.pop()
    rec(set(), [])
    return res


def tileable(region):
    return len(rhombus_tilings(region, limit=1)) > 0


def max_rhombi(region):
    """Maximum number of disjoint rhombi = maximum matching (up vs down)."""
    region = set(region)
    ups = [t for t in region if t[0] == 'U']
    match_d = {}

    def try_aug(u, seen):
        for d in nbrs(u):
            if d in region and d not in seen:
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


def min_greens(region):
    return len(region) - 2 * max_rhombi(region)


def best_packing(region):
    """Return (rhombi list, greens list) achieving the minimum number of greens."""
    region = set(region)
    ups = [t for t in region if t[0] == 'U']
    match_d = {}

    def try_aug(u, seen):
        for d in nbrs(u):
            if d in region and d not in seen:
                seen.add(d)
                if d not in match_d or try_aug(match_d[d], seen):
                    match_d[d] = u
                    return True
        return False
    for u in ups:
        try_aug(u, set())
    rh = [frozenset((u, d)) for d, u in match_d.items()]
    used = set().union(*rh) if rh else set()
    greens = [t for t in region if t not in used]
    return rh, greens


# ------------------------------------------------- pieces for fewest-blocks

def hex_around(p):
    i, j = p
    return frozenset([('U', i, j), ('D', i - 1, j), ('U', i - 1, j),
                      ('D', i - 1, j - 1), ('U', i, j - 1), ('D', i, j - 1)])


def placements(region, kinds='GBRY'):
    region = frozenset(region)
    pl = []
    if 'G' in kinds:
        pl += [('G', frozenset([t])) for t in region]
    if 'B' in kinds:
        s = set()
        for t in region:
            for n in nbrs(t):
                if n in region:
                    s.add(frozenset((t, n)))
        pl += [('B', x) for x in s]
    if 'R' in kinds:
        s = set()
        for t in region:
            ns = [n for n in nbrs(t) if n in region]
            for a in range(len(ns)):
                for b in range(a + 1, len(ns)):
                    s.add(frozenset((t, ns[a], ns[b])))
        pl += [('R', x) for x in s]
    if 'Y' in kinds:
        s = set()
        for t in region:
            for v in verts(t):
                h = hex_around(v)
                if h <= region:
                    s.add(h)
        pl += [('Y', x) for x in s]
    return pl


def min_pieces(region, kinds='GBRY'):
    """Minimum number of pieces in an exact cover; returns (n, solution)."""
    region = frozenset(region)
    pl = placements(region, kinds)
    by_tri = {t: [] for t in region}
    for p in pl:
        for t in p[1]:
            by_tri[t].append(p)
    for t in by_tri:
        by_tri[t].sort(key=lambda p: -len(p[1]))
    order = sorted(region, key=lambda t: (-t[2], centroid(t)[0]))
    best = [len(region) + 1, None]

    def rec(covered, acc, remaining):
        lb = len(acc) + math.ceil(remaining / 6)
        if lb >= best[0]:
            return
        for t in order:
            if t not in covered:
                break
        else:
            best[0] = len(acc)
            best[1] = list(acc)
            return
        for p in by_tri[t]:
            if not (p[1] & covered):
                acc.append(p)
                rec(covered | p[1], acc, remaining - len(p[1]))
                acc.pop()
    rec(frozenset(), [], len(region))
    return best[0], best[1]


def all_mixes(region, kinds='GBRY'):
    """Set of piece multisets (as sorted strings) that tile the region exactly."""
    region = frozenset(region)
    pl = placements(region, kinds)
    by_tri = {t: [p for p in pl if t in p[1]] for t in region}
    order = sorted(region, key=lambda t: (-t[2], centroid(t)[0]))
    mixes = {}

    def rec(covered, acc):
        for t in order:
            if t not in covered:
                break
        else:
            key = ''.join(sorted(p[0] for p in acc))
            mixes.setdefault(key, list(acc))
            return
        for p in by_tri[t]:
            if not (p[1] & covered):
                acc.append(p)
                rec(covered | p[1], acc)
                acc.pop()
    rec(frozenset(), [])
    return mixes


# ------------------------------------------------------------ flips/ribbons

def flip_neighbors(tiling):
    """Tilings reachable by one flip (three rhombi forming a unit hexagon)."""
    tiling = frozenset(tiling)
    tri_to_rh = {}
    for r in tiling:
        for t in r:
            tri_to_rh[t] = r
    out = []
    seen = set()
    pts = set(v for r in tiling for t in r for v in verts(t))
    for p in pts:
        h = hex_around(p)
        if not all(t in tri_to_rh for t in h):
            continue
        rs = set(tri_to_rh[t] for t in h)
        if len(rs) != 3:
            continue
        others = [x for x in [
            [frozenset((('U', p[0], p[1]), ('D', p[0] - 1, p[1]))),
             frozenset((('U', p[0] - 1, p[1]), ('D', p[0] - 1, p[1] - 1))),
             frozenset((('U', p[0], p[1] - 1), ('D', p[0], p[1] - 1)))],
            [frozenset((('U', p[0], p[1]), ('D', p[0], p[1] - 1))),
             frozenset((('D', p[0] - 1, p[1]), ('U', p[0] - 1, p[1]))),
             frozenset((('D', p[0] - 1, p[1] - 1), ('U', p[0], p[1] - 1)))],
        ]]
        for o in others:
            if set(o) != rs and all(all(t in h for t in r) for r in o):
                # check o is a valid set of rhombi (adjacent pairs)
                ok = all(any(n == b for n in nbrs(a)) for a, b in (tuple(r) for r in o))
                if ok:
                    new = (tiling - rs) | frozenset(o)
                    if new not in seen:
                        seen.add(new)
                        out.append(new)
    return out


def flip_graph(tilings):
    idx = {t: n for n, t in enumerate(tilings)}
    adj = {n: set() for n in range(len(tilings))}
    for t in tilings:
        for u in flip_neighbors(t):
            assert u in idx, "flip left the tiling set"
            adj[idx[t]].add(idx[u])
    return adj


def bfs(adj, s):
    dist = {s: 0}
    q = [s]
    while q:
        x = q.pop(0)
        for y in adj[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return dist


def rhombus_kind(r):
    """'V' vertical, 'R' leans right (/), 'L' leans left (\\)."""
    a, b = sorted(r)  # 'D' < 'U'
    d, u = a, b
    if d[0] != 'D':
        raise ValueError
    # U(i,j)+D(i,j): leans right; U(i,j)+D(i-1,j): leans left; U(i,j)+D(i,j-1): vertical
    if d[2] == u[2] - 1:
        return 'V'
    if d[1] == u[1]:
        return 'R'
    return 'L'


def ribbons(tiling, region):
    """Chains of tilted rhombi from each top horizontal edge down to the bottom.
    Returns list of (list of rhombi, word) from left to right."""
    tri_to_rh = {}
    for r in tiling:
        for t in r:
            tri_to_rh[t] = r
    jtop = max(t[2] for t in region)
    # top edges: top edge of a D triangle in top row whose upper neighbour not in region
    tops = sorted([t for t in region if t[0] == 'D' and t[2] == jtop], key=lambda t: t[1])
    out = []
    for t in tops:
        chain = []
        word = ''
        cur = t
        while True:
            r = tri_to_rh[cur]
            k = rhombus_kind(r)
            assert k in 'RL'
            chain.append(r)
            word += k
            u = [x for x in r if x[0] == 'U'][0]
            below = ('D', u[1], u[2] - 1)
            if below not in region:
                break
            cur = below
        out.append((chain, word))
    return out


# ------------------------------------------------------------------- TikZ

def fmt(x):
    s = '%.4f' % x
    s = s.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def boundary_edges(region):
    cnt = {}
    for t in region:
        for e in edges(t):
            cnt[e] = cnt.get(e, 0) + 1
    return [e for e, c in cnt.items() if c == 1], [e for e, c in cnt.items() if c == 2]


def chain_edges(edgelist):
    """Join undirected unit edges into polylines (for cleaner thick outlines)."""
    adj = {}
    for e in edgelist:
        a, b = tuple(e)
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    used = set()
    paths = []
    for e in edgelist:
        if e in used:
            continue
        a, b = tuple(e)
        used.add(e)
        path = [a, b]
        # extend forward
        while True:
            last = path[-1]
            nxt = [n for n in adj[last] if frozenset((last, n)) not in used]
            if not nxt or len(adj[last]) != 2:
                break
            used.add(frozenset((last, nxt[0])))
            path.append(nxt[0])
        while True:
            first = path[0]
            nxt = [n for n in adj[first] if frozenset((first, n)) not in used]
            if not nxt or len(adj[first]) != 2:
                break
            used.add(frozenset((first, nxt[0])))
            path.insert(0, nxt[0])
        paths.append(path)
    return paths


def pstr(p, off=(0, 0)):
    x, y = cart(p)
    return '(%s,%s)' % (fmt(x - off[0]), fmt(y - off[1]))


def tri_path(t, off):
    return ' -- '.join(pstr(v, off) for v in verts(t)) + ' -- cycle'


def piece_outline(tris):
    """Boundary polylines of a union of triangles."""
    b, _ = boundary_edges(tris)
    return chain_edges(b)


def offset_of(region):
    xs = [cart(v)[0] for t in region for v in verts(t)]
    ys = [cart(v)[1] for t in region for v in verts(t)]
    return (min(xs), min(ys)), (max(xs) - min(xs), max(ys) - min(ys))


def tikz_board(region, unit_in=1.0, black=(), pieces=(), grid=True, gridcolor='gridgray',
               boundary_w=1.6, grid_w=0.5, shade=None, extra='', piece_fill=True,
               label=None, label_pos='left', piece_w=None, off=None, wrap=True,
               chains=()):
    """Return TikZ code for a board.

    pieces: list of (kind, set of triangles). kind in G,B,R,Y,P or 'W' (outline only).
    black: triangles to fill black (holes).
    chains: list of sets of triangles to shade gray.
    """
    region = frozenset(region)
    if off is None:
        off, _ = offset_of(region)
    out = []
    if wrap:
        out.append('\\begin{tikzpicture}[x=%sin,y=%sin,line join=round,line cap=round]'
                   % (fmt(unit_in), fmt(unit_in)))
    for c in chains:
        for t in c:
            out.append('\\fill[chainfill] %s;' % tri_path(t, off))
    if piece_fill:
        for kind, tris in pieces:
            if kind in 'GBRYP':
                for t in tris:
                    out.append('\\fill[fill%s] %s;' % (kind, tri_path(t, off)))
    for t in black:
        out.append('\\fill[holefill] %s;' % tri_path(t, off))
    b, inner = boundary_edges(region)
    if grid:
        for e in inner:
            a, c = tuple(e)
            out.append('\\draw[%s,line width=%spt] %s -- %s;' % (gridcolor, fmt(grid_w), pstr(a, off), pstr(c, off)))
    pw = piece_w if piece_w is not None else boundary_w * 0.8
    for kind, tris in pieces:
        for path in piece_outline(tris):
            out.append('\\draw[line width=%spt] %s;' % (fmt(pw), ' -- '.join(pstr(p, off) for p in path)))
    for path in chain_edges(b):
        closed = path[0] == path[-1]
        s = ' -- '.join(pstr(p, off) for p in (path[:-1] if closed else path))
        if closed:
            s += ' -- cycle'
        out.append('\\draw[line width=%spt] %s;' % (fmt(boundary_w), s))
    out.append(extra)
    if wrap:
        out.append('\\end{tikzpicture}')
    return '\n'.join(x for x in out if x)


def bbox_in(region, unit_in=1.0):
    _, (w, h) = offset_of(region)
    return w * unit_in, h * unit_in
