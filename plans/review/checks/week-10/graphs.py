"""Exhaustive walk search on small multigraphs, written for this review.

A town is a list of vertex names and a list of edges (u, v); parallel edges are allowed.
Nothing here uses parity theory: every answer comes from searching actual walks.
"""
from functools import lru_cache
import itertools


class Town:
    def __init__(self, verts, edges, directed=False):
        self.V = list(verts)
        self.E = [tuple(e) for e in edges]
        self.directed = directed
        self.inc = {v: [] for v in self.V}
        for i, (a, b) in enumerate(self.E):
            self.inc[a].append((i, b))
            if not directed:
                self.inc[b].append((i, a))
        self.full = (1 << len(self.E)) - 1
        self._ends = lru_cache(maxsize=None)(self._ends_raw)

    def _ends_raw(self, v, mask):
        """frozenset of vertices where a walk from v using exactly the unused edges can end."""
        if mask == self.full:
            return frozenset([v])
        out = set()
        for i, w in self.inc[v]:
            if not mask >> i & 1:
                out |= self._ends(w, mask | 1 << i)
        return frozenset(out)

    def ends_from(self, s, mask=0):
        return self._ends(s, mask)

    def start_end(self):
        """dict start -> set of ends of walks using every edge exactly once."""
        return {s: set(self.ends_from(s)) for s in self.V if self.ends_from(s)}

    def has_walk(self):
        return bool(self.start_end())

    def has_closed(self):
        return any(s in es for s, es in self.start_end().items())

    def closed_starts(self):
        return {s for s, es in self.start_end().items() if s in es}

    def is_walk(self, word, closed=None):
        """Is the island word a walk using every edge exactly once (as a multiset)?"""
        used = [False] * len(self.E)
        for a, b in zip(word, word[1:]):
            ok = False
            for i, w in self.inc[a]:
                if w == b and not used[i]:
                    used[i] = True
                    ok = True
                    break
            if not ok:
                return False
        if not all(used):
            return False
        if closed is True and word[0] != word[-1]:
            return False
        return True

    def degrees(self):
        d = {v: 0 for v in self.V}
        for a, b in self.E:
            d[a] += 1
            d[b] += 1
        return d

    def odd(self):
        return sorted(v for v, k in self.degrees().items() if k % 2)

    def connected(self):
        if not self.V:
            return True
        seen = {self.V[0]}
        stack = [self.V[0]]
        while stack:
            x = stack.pop()
            for _, y in self.inc[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
            if self.directed:
                for i, (a, b) in enumerate(self.E):
                    if b == x and a not in seen:
                        seen.add(a)
                        stack.append(a)
        return len(seen) == len(self.V)

    def count_trails(self, s, mask=0, closed=False):
        """Number of edge sequences (walks using every edge once) from s; closed=True counts those ending at s."""
        @lru_cache(maxsize=None)
        def rec(v, m):
            if m == self.full:
                return 1 if (not closed or v == s) else 0
            tot = 0
            for i, w in self.inc[v]:
                if not m >> i & 1:
                    tot += rec(w, m | 1 << i)
            return tot
        return rec(s, mask)

    def plus(self, extra):
        return Town(self.V, self.E + [tuple(e) for e in extra], self.directed)

    def doubled(self, idxs):
        return Town(self.V, self.E + [self.E[i] for i in idxs], self.directed)


def edge_game(town, start):
    """Token game: players alternately move the token over an unused edge; a player who cannot move loses.
    Returns True if the player to move first wins."""
    @lru_cache(maxsize=None)
    def win(v, m):
        for i, w in town.inc[v]:
            if not m >> i & 1 and not win(w, m | 1 << i):
                return True
        return False
    return win(start, 0)


def additions(town, k, pairs=None, closed=False):
    """All multisets of k new edges (from candidate vertex pairs) after which a walk exists
    (closed=True: a closed walk)."""
    if pairs is None:
        pairs = list(itertools.combinations(town.V, 2))
    out = []
    for combo in itertools.combinations_with_replacement(pairs, k):
        t = town.plus(combo)
        if (t.has_closed() if closed else t.has_walk()):
            out.append(combo)
    return out


def extra_counters(town, k, closed):
    """All multisets of k extra crossings on existing edges (indices) after which a walk exists."""
    out = []
    for combo in itertools.combinations_with_replacement(range(len(town.E)), k):
        t = town.doubled(combo)
        if (t.has_closed() if closed else t.has_walk()):
            out.append(combo)
    return out


def fewest(fn, kmax=6):
    for k in range(kmax + 1):
        sols = fn(k)
        if sols:
            return k, sols
    return None, []
