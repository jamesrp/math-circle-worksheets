"""
Rhombus (lozenge) tilings of hexagons, flips, and ribbons, built on tri.py.

Hexagon (a,b,c): bottom side a (horizontal), lower-right side b, upper-right side c,
top side a, upper-left side b, lower-left side c.  Bottom-left corner at lattice (0,0).

Rhombus kinds in this flat-top orientation:
  'R'  = lying rhombus leaning right  = U(i,j) + D(i,j)      (flat top and bottom)
  'L'  = lying rhombus leaning left   = U(i,j) + D(i-1,j)    (flat top and bottom)
  'S'  = standing rhombus (diamond)   = D(i,j) + U(i,j+1)    (points at top and bottom)
"""
import tri
from collections import deque

UP, DN = tri.UP, tri.DN


def kind(rh):
    a, b = sorted(rh, key=lambda t: t[2])  # a is up, b is down
    (i, j, _), (k, l, _) = a, b
    if l == j and k == i:
        return 'R'
    if l == j and k == i - 1:
        return 'L'
    if l == j - 1 and k == i:
        return 'S'
    raise ValueError(rh)


def tilings(a, b, c):
    R = tri.hexagon_region(a, b, c)
    n, res = tri.count_tilings(R, ['B'], collect=True)
    return R, [frozenset(pl for _, pl in t) for t in res]


def partner_map(tiling):
    m = {}
    for rh in tiling:
        x, y = tuple(rh)
        m[x] = y
        m[y] = x
    return m


def ribbons(tiling, a, b, c):
    """Words (bottom to top) of the a chains that start at the bottom edges."""
    m = partner_map(tiling)
    words = []
    for k in range(a):
        cur = (k, 0, UP)
        w = ''
        for step in range(b + c):
            p = m[cur]
            if p == (cur[0], cur[1], DN):
                w += 'R'
                cur = (cur[0], cur[1] + 1, UP)
            elif p == (cur[0] - 1, cur[1], DN):
                w += 'L'
                cur = (cur[0] - 1, cur[1] + 1, UP)
            else:
                raise RuntimeError('chain broke')
        words.append(w)
    return tuple(words)


def interior_points(R):
    pts = set()
    for t in R:
        for p in tri.corners(t):
            pts.add(p)
    return [p for p in pts if all(t in R for t in tri.around_point(p))]


def flips(tiling, R):
    """All tilings reachable by one flip, with the lattice point flipped around."""
    m = partner_map(tiling)
    out = []
    for p in interior_points(R):
        six = tri.around_point(p)  # ccw order
        S = set(six)
        if all(m[t] in S for t in six):
            # the three rhombi pair six[k] with six[k+1] for k even or odd
            pairs_now = {frozenset((t, m[t])) for t in six}
            # alternatives: pairing (0,1),(2,3),(4,5) or (1,2),(3,4),(5,0)
            A = {frozenset((six[0], six[1])), frozenset((six[2], six[3])), frozenset((six[4], six[5]))}
            B = {frozenset((six[1], six[2])), frozenset((six[3], six[4])), frozenset((six[5], six[0]))}
            new = B if pairs_now == A else A
            assert pairs_now in (A, B)
            nt = frozenset((tiling - pairs_now) | new)
            out.append((p, nt))
    return out


def flip_graph(a, b, c):
    R, ts = tilings(a, b, c)
    idx = {t: k for k, t in enumerate(ts)}
    adj = {k: set() for k in range(len(ts))}
    for t in ts:
        for p, nt in flips(t, R):
            adj[idx[t]].add(idx[nt])
    return R, ts, idx, adj


def bfs(adj, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def inversions(word):
    """number of pairs (R before L)."""
    n = 0
    rs = 0
    for ch in word:
        if ch == 'R':
            rs += 1
        else:
            n += rs
    return n


def rhombus_cart(rh):
    return tri.piece_vertices(list(rh))
