"""Triangular-grid tiling checks for Week01++ ideas.
Cells: ('U',i,j) up triangle with vertices (i,j),(i+1,j),(i,j+1);
       ('D',i,j) down triangle with vertices (i+1,j),(i,j+1),(i+1,j+1).
Lattice coords -> cartesian: (x + y/2, y*sqrt3/2).
"""
import math, itertools, sys
from functools import lru_cache
from collections import deque, Counter
S3 = math.sqrt(3)

def cart(p):
    x, y = p
    return (x + y / 2, y * S3 / 2)

def verts(c):
    t, i, j = c
    if t == 'U':
        return [(i, j), (i + 1, j), (i, j + 1)]
    return [(i + 1, j), (i, j + 1), (i + 1, j + 1)]

def centroid(c):
    vs = [cart(v) for v in verts(c)]
    return (sum(v[0] for v in vs) / 3, sum(v[1] for v in vs) / 3)

def neighbors(c):
    t, i, j = c
    if t == 'U':
        return [('D', i, j), ('D', i - 1, j), ('D', i, j - 1)]
    return [('U', i, j), ('U', i + 1, j), ('U', i, j + 1)]

DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

def polygon(steps):
    """steps: list of (dir_index, length). returns lattice vertices."""
    p = (0, 0)
    pts = [p]
    for d, n in steps:
        dx, dy = DIRS[d]
        p = (p[0] + dx * n, p[1] + dy * n)
        pts.append(p)
    assert pts[-1] == (0, 0), pts
    return pts[:-1]

def inside(poly, q):
    # winding / ray casting on cartesian
    P = [cart(v) for v in poly]
    x, y = q
    inside = False
    n = len(P)
    for k in range(n):
        x1, y1 = P[k]; x2, y2 = P[(k + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                inside = not inside
    return inside

def region(steps):
    poly = polygon(steps)
    xs = [v[0] for v in poly]; ys = [v[1] for v in poly]
    cells = []
    for i in range(min(xs) - 2 - max(ys), max(xs) + 3 + max(ys)):
        for j in range(min(ys) - 1, max(ys) + 2):
            for t in 'UD':
                c = (t, i, j)
                if inside(poly, centroid(c)):
                    cells.append(c)
    return cells

def hexagon(a, b, c):
    return region([(0, a), (1, b), (2, c), (3, a), (4, b), (5, c)])

def tri(n):
    return region([(0, n), (2, n), (4, n)])

def para(a, b):
    return region([(0, a), (1, b), (3, a), (4, b)])

# ---------- placements ----------
def rhombi(cells):
    S = set(cells)
    out = set()
    for c in cells:
        for d in neighbors(c):
            if d in S:
                out.add(frozenset([c, d]))
    return list(out)

def trapezoids(cells):
    S = set(cells)
    out = set()
    for c in cells:
        nb = [d for d in neighbors(c) if d in S]
        for a, b in itertools.combinations(nb, 2):
            out.add(frozenset([a, c, b]))
    return list(out)

def hexes(cells):
    S = set(cells)
    out = []
    vs = set(v for c in cells for v in verts(c))
    for (x, y) in vs:
        around = [('U', x, y), ('D', x - 1, y), ('U', x - 1, y), ('D', x - 1, y - 1), ('U', x, y - 1), ('D', x, y - 1)]
        if all(a in S for a in around):
            out.append(frozenset(around))
    return out

def singles(cells):
    return [frozenset([c]) for c in cells]

def tilings(cells, pieces):
    order = sorted(cells)
    idx = {c: k for k, c in enumerate(order)}
    by_cell = {c: [] for c in cells}
    for p in pieces:
        for c in p:
            by_cell[c].append(p)
    res = []
    covered = set()
    cur = []
    def rec():
        # first uncovered
        for c in order:
            if c not in covered:
                break
        else:
            res.append(frozenset(cur)); return
        for p in by_cell[c]:
            if not (p & covered):
                covered.update(p); cur.append(p)
                rec()
                cur.pop(); covered.difference_update(p)
    rec()
    return res

def rh_orient(p):
    a, b = sorted(p)
    # orientation determined by the shared edge direction
    u = a if a[0] == 'U' else b
    d = b if u is a else a
    if (d[1], d[2]) == (u[1], u[2]):
        return 'slant1'
    if (d[1], d[2]) == (u[1] - 1, u[2]):
        return 'slant2'
    return 'flat'

def updown(cells):
    return sum(1 for c in cells if c[0] == 'U'), sum(1 for c in cells if c[0] == 'D')


# ---------------------------------------------------------------------------
# Week 1++ checks (October 3, 2026). Run: python3 plans/week-01-plus-checks.py
# ---------------------------------------------------------------------------
def flip_graph(T, k):
    """Two tilings are adjacent when they differ only inside the union of k pieces."""
    from collections import defaultdict
    buckets = defaultdict(list)
    for n, t in enumerate(T):
        for sub in itertools.combinations(t, k):
            buckets[t - frozenset(sub)].append(n)
    adj = {n: set() for n in range(len(T))}
    for ns in buckets.values():
        for a in ns:
            for b in ns:
                if a != b:
                    adj[a].add(b)
    return adj

def components(adj):
    seen, comps = set(), []
    for s in adj:
        if s in seen:
            continue
        stack, comp = [s], 0
        seen.add(s)
        while stack:
            u = stack.pop(); comp += 1
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        comps.append(comp)
    return comps

def diameter_and_bipartite(adj):
    def bfs(s):
        d = {s: 0}; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1; q.append(v)
        return d
    diam = max(max(bfs(s).values()) for s in adj)
    col, bip = {}, True
    for s in adj:
        if s in col:
            continue
        col[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]; q.append(v)
                elif col[v] == col[u]:
                    bip = False
    return diam, bip

def trap_kind(p):
    return '2up' if sum(1 for c in p if c[0] == 'U') == 2 else '2down'

def placement_game(cells):
    """Normal play: players alternately place a blue rhombus; a player with no legal placement loses."""
    cells = sorted(cells); idx = {c: k for k, c in enumerate(cells)}
    masks = [sum(1 << idx[c] for c in p) for p in rhombi(cells)]
    memo = {}
    def win(occ):
        if occ not in memo:
            memo[occ] = any(not (m & occ) and not win(occ | m) for m in masks)
        return memo[occ]
    first = win(0)
    return ('first' if first else 'second'), sum(1 for m in masks if not win(m)), len(masks)

def min_pieces(cells):
    pieces = [(p, 'hexagon') for p in hexes(cells)] + [(p, 'trapezoid') for p in trapezoids(cells)] \
        + [(p, 'rhombus') for p in rhombi(cells)] + [(p, 'triangle') for p in singles(cells)]
    order = sorted(cells); by = {c: [] for c in cells}
    for p in pieces:
        for c in p[0]:
            by[c].append(p)
    for c in by:
        by[c].sort(key=lambda p: -len(p[0]))
    best = [10 ** 9, None]; cov = set(); cur = []
    def rec():
        rem = len(cells) - len(cov)
        if len(cur) + -(-rem // 6) >= best[0]:
            return
        for c in order:
            if c not in cov:
                break
        else:
            best[0], best[1] = len(cur), list(cur); return
        for p in by[c]:
            if not (p[0] & cov):
                cov.update(p[0]); cur.append(p); rec(); cur.pop(); cov.difference_update(p[0])
    rec()
    return best[0], dict(Counter(k for _, k in best[1]))

def max_hexagons(cells):
    H = hexes(cells); best = 0
    def rec(i, used, n):
        nonlocal best
        if n + len(H) - i <= best:
            return
        if i == len(H):
            best = n; return
        if not (H[i] & used):
            rec(i + 1, used | H[i], n + 1)
        rec(i + 1, used, n)
    rec(0, frozenset(), 0)
    return best

if __name__ == '__main__':
    print('1. Blue-rhombus tilings of (a,b,c) hexagons: count, orientation counts, flip graph')
    for abc in [(1, 2, 2), (2, 2, 2), (1, 3, 3), (2, 2, 3)]:
        cells = hexagon(*abc); T = tilings(cells, rhombi(cells))
        orient = {tuple(sorted(Counter(rh_orient(p) for p in t).values())) for t in T}
        diam, bip = diameter_and_bipartite(flip_graph(T, 3))
        print(f'   {abc}: {len(T)} tilings; orientation counts {orient}; flip diameter {diam} (abc={abc[0]*abc[1]*abc[2]}); bipartite {bip}')
    print('2. Red-trapezoid tilings: 2up/2down counts are forced by up-minus-down cells')
    for name, cells in [('side-3 triangle', tri(3)), ('side-6 triangle', tri(6)), ('2x hexagon', hexagon(2, 2, 2))]:
        T = tilings(cells, trapezoids(cells)); u, d = updown(cells)
        kinds = {tuple(sorted(Counter(trap_kind(p) for p in t).items())) for t in T}
        print(f'   {name}: up/down cells {u}/{d}; {len(T)} tilings; kinds {kinds}')
    cells = hexagon(2, 2, 2); T = tilings(cells, trapezoids(cells))
    for k in (2, 4, 5, 6):
        print(f'   2x hexagon, re-tile up to {k} trapezoids at once: components {components(flip_graph(T, k))}')
    print('3. Rhombus placement game (last player able to place wins)')
    for name, cells in [('hex(1,1,1)', hexagon(1, 1, 1)), ('hex(1,1,2)', hexagon(1, 1, 2)), ('hex(1,2,2)', hexagon(1, 2, 2)),
                        ('hex(2,2,2)', hexagon(2, 2, 2)), ('para 2x2', para(2, 2)), ('para 3x2', para(3, 2)),
                        ('para 4x2', para(4, 2)), ('para 3x3', para(3, 3)), ('side-3 triangle', tri(3)), ('side-4 triangle', tri(4))]:
        w, good, tot = placement_game(cells)
        print(f'   {name}: {w} player wins; winning first placements {good}/{tot}')
    print('4. Fewest blocks (hexagon/trapezoid/rhombus/triangle) and most yellow hexagons')
    for name, cells in [('2x hexagon', hexagon(2, 2, 2)), ('3x hexagon', hexagon(3, 3, 3)), ('side-4 triangle', tri(4)),
                        ('side-5 triangle', tri(5)), ('side-6 triangle', tri(6))]:
        print(f'   {name}: fewest {min_pieces(cells)}; most hexagons {max_hexagons(cells)}')
    print('5. Bigger copies made from the same block')
    print('   2x trapezoid from 4 trapezoids:', len(tilings(region([(0, 4), (2, 2), (3, 2), (4, 2)]), trapezoids(region([(0, 4), (2, 2), (3, 2), (4, 2)])))), 'way(s)')
    print('   2x hexagon from small hexagons only:', len(tilings(hexagon(2, 2, 2), hexes(hexagon(2, 2, 2)))), 'ways')
