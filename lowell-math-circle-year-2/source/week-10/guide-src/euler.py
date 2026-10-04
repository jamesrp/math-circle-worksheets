"""Walks that cross every bridge exactly once, by exhaustive search (no parity theory used)."""

import itertools
from functools import lru_cache


def connected(n, edges):
    adj = {i: set() for i in range(n)}
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    seen = {0}
    st = [0]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); st.append(y)
    return len(seen) == n


def degrees(n, edges):
    d = [0] * n
    for u, v in edges:
        d[u] += 1; d[v] += 1
    return d


def start_end(n, edges):
    """dict start -> frozenset of possible ends, over all walks using every edge exactly once."""
    m = len(edges)
    inc = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        inc[u].append((i, v))
        if u != v:
            inc[v].append((i, u))
    full = (1 << m) - 1

    @lru_cache(maxsize=None)
    def ends(x, mask):
        if mask == full:
            return frozenset([x])
        out = set()
        for i, y in inc[x]:
            if not mask >> i & 1:
                out |= ends(y, mask | 1 << i)
        return frozenset(out)

    res = {}
    for s in range(n):
        e = ends(s, 0)
        if e:
            res[s] = e
    ends.cache_clear()
    return res


def one_walk(n, edges, start, end=None):
    m = len(edges)
    inc = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        inc[u].append((i, v))
        if u != v:
            inc[v].append((i, u))
    used = [False] * m
    path = [start]

    def dfs(x, k):
        if k == m:
            return end is None or x == end
        for i, y in inc[x]:
            if not used[i]:
                used[i] = True; path.append(y)
                if dfs(y, k + 1):
                    return True
                used[i] = False; path.pop()
        return False

    return list(path) if dfs(start, 0) else None


def count_walks(n, edges, start, end=None, limit=None):
    m = len(edges)
    inc = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        inc[u].append((i, v))
        if u != v:
            inc[v].append((i, u))
    full = (1 << m) - 1

    @lru_cache(maxsize=None)
    def cnt(x, mask):
        if mask == full:
            return 1 if (end is None or x == end) else 0
        return sum(cnt(y, mask | 1 << i) for i, y in inc[x] if not mask >> i & 1)

    r = cnt(start, 0)
    cnt.cache_clear()
    return r


def has_walk(n, edges, closed=False):
    se = start_end(n, edges)
    if closed:
        return any(s in e for s, e in se.items())
    return bool(se)


def fewest_extra(n, edges, pool, closed, kmax=5):
    """Fewest bridges to add (chosen with repetition from pool, a list of island pairs) so that a
    walk crossing every bridge once exists (closed: ending where it started).
    Returns (k, list of solutions as sorted tuples of pairs)."""
    for k in range(0, kmax + 1):
        sols = []
        for extra in itertools.combinations_with_replacement(range(len(pool)), k):
            E = list(edges) + [pool[i] for i in extra]
            if not connected(n, E):
                continue
            if has_walk(n, E, closed):
                sols.append(tuple(pool[i] for i in extra))
        if sols:
            return k, sols
    return None, []
