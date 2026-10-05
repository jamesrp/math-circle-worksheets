"""My own route/cut/game/residual routines for the Week 13 check (no packet code used)."""
from itertools import combinations
from functools import lru_cache


def simple_paths(edges, s='s', t='t', closed=frozenset()):
    """All simple directed s-t paths, each as a tuple of edges (a, b)."""
    out = {}
    adj = {}
    for e in edges:
        if e not in closed:
            adj.setdefault(e[0], []).append(e)
    res = []

    def dfs(v, seen, path):
        if v == t:
            res.append(tuple(path)); return
        for e in adj.get(v, []):
            if e[1] not in seen:
                seen.add(e[1]); path.append(e)
                dfs(e[1], seen, path)
                path.pop(); seen.remove(e[1])
    dfs(s, {s}, [])
    return res


def blocks(edges, closed, s='s', t='t'):
    """True if closing `closed` leaves no s-t route (reachability)."""
    reach = {s}; changed = True
    while changed:
        changed = False
        for a, b in edges:
            if (a, b) not in closed and a in reach and b not in reach:
                reach.add(b); changed = True
    return t not in reach


def packings(edges, s='s', t='t'):
    """All collections of pairwise edge-disjoint routes; returns (max size, list of maximum collections)."""
    P = simple_paths(edges, s, t)
    best = [0, []]

    def rec(i, used, chosen):
        if len(chosen) > best[0]:
            best[0] = len(chosen); best[1] = [tuple(chosen)]
        elif len(chosen) == best[0] and chosen:
            best[1].append(tuple(chosen))
        for j in range(i, len(P)):
            if not (set(P[j]) & used):
                rec(j + 1, used | set(P[j]), chosen + [P[j]])
    rec(0, frozenset(), [])
    return best[0], best[1]


def min_cuts(edges, s='s', t='t'):
    for k in range(len(edges) + 1):
        cuts = [c for c in combinations(edges, k) if blocks(edges, set(c), s, t)]
        if cuts:
            return k, cuts


def splits(edges, verts, s='s', t='t'):
    """Every start side S (s in S, t not in S): (S, out-arrows, in-arrows)."""
    inner = [v for v in verts if v not in (s, t)]
    out = []
    for k in range(len(inner) + 1):
        for c in combinations(inner, k):
            S = {s, *c}
            o = [e for e in edges if e[0] in S and e[1] not in S]
            i = [e for e in edges if e[0] not in S and e[1] in S]
            out.append((sorted(S), o, i))
    return out


def game(edges, s='s', t='t'):
    """Closing game: players alternately close one open arrow; the move that leaves no route wins.
    Returns (first player wins?, list of winning first moves)."""
    E = list(edges)
    routes = [frozenset(E.index(e) for e in p) for p in simple_paths(E, s, t)]
    masks = [sum(1 << i for i in r) for r in routes]

    @lru_cache(None)
    def win(closed):  # player to move, routes still exist
        for i in range(len(E)):
            if not closed >> i & 1:
                c = closed | 1 << i
                if all(c & m for m in masks) or not win(c):
                    return True
        return False
    first = win(0)
    good = [E[i] for i in range(len(E)) if all((1 << i) & m for m in masks) or not win(1 << i)]
    return first, good


def residual_arcs(edges, R):
    """Change-walk steps: unused arrow forward, reserved arrow backward. (tail, head, original edge, kind)"""
    arcs = []
    for e in edges:
        if e in R:
            arcs.append((e[1], e[0], e, 'cancel'))
        else:
            arcs.append((e[0], e[1], e, 'reserve'))
    return arcs


def change_walks(edges, R, s='s', t='t'):
    """All change-walks from s to t that visit each dot at most once."""
    arcs = residual_arcs(edges, R)
    res = []

    def dfs(v, seen, path):
        if v == t:
            res.append(list(path)); return
        for a in arcs:
            if a[0] == v and a[1] not in seen:
                seen.add(a[1]); path.append(a)
                dfs(a[1], seen, path)
                path.pop(); seen.remove(a[1])
    dfs(s, {s}, [])
    return res


def residual_reach(edges, R, s='s'):
    arcs = residual_arcs(edges, R)
    reach = {s}; changed = True
    while changed:
        changed = False
        for a in arcs:
            if a[0] in reach and a[1] not in reach:
                reach.add(a[1]); changed = True
    return reach


def toggle(R, walk):
    R = set(R)
    for _, _, e, kind in walk:
        if kind == 'reserve':
            R.add(e)
        else:
            R.remove(e)
    return R


def decompose(R, s='s', t='t'):
    """Split a balanced reservation into simple s-t routes (cycles discarded). Returns list of routes."""
    R = set(R)
    routes = []
    while any(e[0] == s for e in R):
        v = s; path = []; seen = [s]
        while v != t:
            e = sorted(x for x in R if x[0] == v)[0]
            R.remove(e); path.append(e); v = e[1]
            if v in seen:  # remove the cycle just closed
                k = seen.index(v)
                cyc = path[k:]; path = path[:k]; seen = seen[:k + 1]
                continue
            seen.append(v)
        routes.append(tuple(path))
    return routes, R


def balanced(R, s='s', t='t'):
    verts = {v for e in R for v in e}
    for v in verts - {s, t}:
        if sum(e[1] == v for e in R) != sum(e[0] == v for e in R):
            return False
    return True


def fmt_path(p):
    return '-'.join([p[0][0]] + [e[1] for e in p]) if p else '(empty)'


def fmt_edges(es):
    return '{' + ', '.join(a + b for a, b in es) + '}'


def edge_disjoint(routes):
    allE = [e for r in routes for e in r]
    return len(allE) == len(set(allE))
