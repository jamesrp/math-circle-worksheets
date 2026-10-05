"""Triangulations of a convex n-gon, written for this review.

Corners are 0..n-1 in cyclic order (A=0, B=1, ...; on K-1 pages 1=0, 2=1, ...).
A triangulation is a frozenset of diagonals (i, j) with i < j.
Two independent generators are provided and cross-checked in solve.py:
  * by_subsets(n): every (n-3)-subset of diagonals with no crossing pair;
  * by_root(n): recursive decomposition on the triangle over side (0, n-1).
"""
import itertools
from collections import deque
from functools import lru_cache

LET = 'ABCDEFGHIJ'


def diagonals(n):
    return [(i, j) for i in range(n) for j in range(i + 2, n) if not (i == 0 and j == n - 1)]


def cross(e, f):
    a, b = e
    c, d = f
    return a < c < b < d or c < a < d < b


def noncrossing(ds):
    return all(not cross(e, f) for e, f in itertools.combinations(ds, 2))


def by_subsets(n):
    return [frozenset(c) for c in itertools.combinations(diagonals(n), n - 3) if noncrossing(c)]


def by_root(n):
    @lru_cache(None)
    def tri(vs):
        # vs: tuple of corners in cyclic order; the root side is (vs[0], vs[-1])
        if len(vs) < 3:
            return [frozenset()]
        out = []
        a, b = vs[0], vs[-1]
        for k in range(1, len(vs) - 1):
            c = vs[k]
            left = vs[:k + 1]
            right = vs[k:]
            extra = set()
            if k > 1:
                extra.add(tuple(sorted((a, c))))
            if k < len(vs) - 2:
                extra.add(tuple(sorted((c, b))))
            for L in tri(left):
                for R in tri(right):
                    out.append(frozenset(L | R | extra))
        return out
    return tri(tuple(range(n)))


def is_side(n, a, b):
    return (b - a) % n in (1, n - 1)


def edges_of(n, T):
    E = set(T)
    E |= {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
    return E


def triangles(n, T):
    E = edges_of(n, T)
    return [t for t in itertools.combinations(range(n), 3)
            if all(tuple(sorted(p)) in E for p in itertools.combinations(t, 2))]


def faces(n, D):
    """Faces of the convex n-gon cut by the noncrossing chord set D (any size)."""
    fs = [list(range(n))]
    for a, b in sorted(D):
        for i, f in enumerate(fs):
            if a in f and b in f:
                ia, ib = f.index(a), f.index(b)
                if ia > ib:
                    ia, ib = ib, ia
                f1 = f[ia:ib + 1]
                f2 = f[ib:] + f[:ia + 1]
                fs[i:i + 1] = [f1, f2]
                break
    return fs


def flip(n, T, d):
    """Flip diagonal d of T; return the new triangulation."""
    a, b = d
    tris = [t for t in triangles(n, T) if a in t and b in t]
    assert len(tris) == 2, (T, d, tris)
    c = [v for v in tris[0] if v not in d][0]
    e = [v for v in tris[1] if v not in d][0]
    return frozenset((T - {d}) | {tuple(sorted((c, e)))})


def neighbours(n, T):
    return [flip(n, T, d) for d in sorted(T)]


def graph(n, Ts):
    return {T: neighbours(n, T) for T in Ts}


def bfs(G, s):
    dist = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def fan(n, v):
    return frozenset(d for d in diagonals(n) if v in d)


def parse(s, labels=LET):
    """'AC AD' -> frozenset({(0,2),(0,3)}); also '13 14' with labels '123456789'."""
    out = set()
    for tok in s.split():
        a, b = labels.index(tok[0]), labels.index(tok[1])
        out.add(tuple(sorted((a, b))))
    return frozenset(out)


def name(T, labels=LET):
    return ' '.join(sorted(labels[a] + labels[b] for a, b in T))


def deg(T, v):
    return sum(v in d for d in T)
