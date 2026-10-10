"""Independent chip-firing solver for the Week 11 math check.

Written for this review; it does not import or reuse the packet's own
build_packets.py / verify.py / independent_checks.py.

A board is a dict  vertex -> list of neighbours  (undirected, loopless,
multi-edges allowed by repetition).  The sink, when present, is the vertex
'S'; it never fires and its chips are not part of the state.  A state is a
tuple of chip counts in the order of BOARD_ORDER[board].
"""
import os
import sys
from functools import lru_cache
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-11')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-11')
SRC_RV = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-11-return-visit')


def edges_to_board(edges):
    nb = {}
    for a, b in edges:
        nb.setdefault(a, []).append(b)
        nb.setdefault(b, []).append(a)
    return nb


# My own transcription of the boards (checked against the PDFs in extract_pdf.py).
EDGES = {
    'triangle': [('A', 'B'), ('A', 'S'), ('B', 'S')],
    'fourcycle': [('S', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'S')],
    'extraline': [('S', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'S'), ('A', 'C')],
    'closedtriangle': [('A', 'B'), ('B', 'C'), ('C', 'A')],
}
ORDER = {'triangle': 'AB', 'fourcycle': 'ABC', 'extraline': 'ABC', 'closedtriangle': 'ABC'}


class Board:
    def __init__(self, name, edges=None, order=None):
        self.name = name
        self.edges = edges or EDGES[name]
        self.order = order or ORDER[name]
        nb = edges_to_board(self.edges)
        self.nb = {v: nb[v] for v in self.order}
        self.deg = tuple(len(self.nb[v]) for v in self.order)
        self.idx = {v: i for i, v in enumerate(self.order)}
        self.has_sink = any('S' in e for e in self.edges)

    def legal(self, state):
        return [v for v in self.order if state[self.idx[v]] >= len(self.nb[v])]

    def fire(self, state, v):
        """Return (new_state, chips_to_sink) or None if v cannot fire."""
        i = self.idx[v]
        if state[i] < len(self.nb[v]):
            return None
        s = list(state)
        s[i] -= len(self.nb[v])
        sink = 0
        for w in self.nb[v]:
            if w == 'S':
                sink += 1
            else:
                s[self.idx[w]] += 1
        return tuple(s), sink

    def run_word(self, state, word):
        """Play a word; return (final_state, sink_chips) or raise ValueError at the first illegal letter."""
        state = tuple(state)
        sink = 0
        for k, v in enumerate(word):
            r = self.fire(state, v)
            if r is None:
                raise ValueError(f'{word}: letter {k+1} ({v}) illegal at {state}')
            state, s = r
            sink += s
        return state, sink

    def is_stable(self, state):
        return not self.legal(state)

    def stable_states(self):
        return [s for s in product(*[range(d) for d in self.deg])]

    def all_complete_words(self, state, limit=10**6):
        """Every complete legal firing word from state (DFS over words)."""
        out = []

        def rec(st, w):
            if len(out) > limit:
                raise RuntimeError('too many words')
            act = self.legal(st)
            if not act:
                out.append(w)
                return
            for v in act:
                rec(self.fire(st, v)[0], w + v)
        rec(tuple(state), '')
        return out

    def outcome_set(self, state):
        """Set of (finish, counts, sink) over ALL complete legal runs, by memoised search over states,
        plus the number of distinct complete words.  Only for boards with a sink (finite)."""
        n = len(self.order)

        @lru_cache(None)
        def rec(st):
            act = self.legal(st)
            if not act:
                return frozenset([(st, (0,) * n, 0)]), 1
            res = set()
            nwords = 0
            for v in act:
                nst, s = self.fire(st, v)
                sub, k = rec(nst)
                nwords += k
                for fin, cnt, sk in sub:
                    c = list(cnt)
                    c[self.idx[v]] += 1
                    res.add((fin, tuple(c), sk + s))
            return frozenset(res), nwords
        return rec(tuple(state))

    def stabilize(self, state):
        """Unique outcome (asserts uniqueness over all legal orders)."""
        res, nwords = self.outcome_set(state)
        assert len(res) == 1, (self.name, state, res)
        fin, cnt, sk = next(iter(res))
        return {'finish': fin, 'counts': cnt, 'sink': sk, 'nwords': nwords}

    def S(self, state):
        """Fast stabilisation by one order (used for big random tests; uniqueness is tested elsewhere)."""
        st = list(state)
        cnt = [0] * len(st)
        while True:
            act = [i for i, v in enumerate(self.order) if st[i] >= self.deg[i]]
            if not act:
                return tuple(st), tuple(cnt)
            i = act[-1]
            v = self.order[i]
            st[i] -= self.deg[i]
            cnt[i] += 1
            for w in self.nb[v]:
                if w != 'S':
                    st[self.idx[w]] += 1

    def laplacian(self):
        n = len(self.order)
        L = [[0] * n for _ in range(n)]
        for i, v in enumerate(self.order):
            L[i][i] = len(self.nb[v])
            for w in self.nb[v]:
                if w != 'S':
                    L[i][self.idx[w]] -= 1
        return L

    def formal(self, c, f):
        """c - L f."""
        L = self.laplacian()
        return tuple(c[i] - sum(L[i][j] * f[j] for j in range(len(c))) for i in range(len(c)))

    def addition_interleavings(self, adds):
        """All final states reachable by adding the chips of `adds` (a vector) one at a time in any
        order, firing any legal vertex at any time, and stopping only when all chips are added and
        no vertex can fire.  Returns set of (finish, counts)."""
        n = len(self.order)

        @lru_cache(None)
        def rec(st, rem):
            res = set()
            act = self.legal(st)
            if not act and not any(rem):
                return frozenset([(st, (0,) * n)])
            for i in range(n):
                if rem[i]:
                    s2 = list(st); s2[i] += 1
                    r2 = list(rem); r2[i] -= 1
                    res |= rec(tuple(s2), tuple(r2))
            for v in act:
                nst, _ = self.fire(st, v)
                for fin, cnt in rec(nst, rem):
                    c = list(cnt); c[self.idx[v]] += 1
                    res.add((fin, tuple(c)))
            return frozenset(res)
        return rec((0,) * n, tuple(adds))

    def closed_explore(self, start, max_states=10**5):
        """For a sink-free board: explore every state reachable by legal firing.
        Returns (reachable states, stable reachable states, whether a legal cycle is reachable,
        whether every run is infinite)."""
        seen = {tuple(start)}
        stack = [tuple(start)]
        succ = {}
        while stack:
            st = stack.pop()
            succ[st] = [self.fire(st, v)[0] for v in self.legal(st)]
            for t in succ[st]:
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
            assert len(seen) < max_states
        stable = [s for s in seen if not succ[s]]
        # cycle detection in the reachable digraph
        colour = {}
        has_cycle = False

        def dfs(u):
            nonlocal has_cycle
            colour[u] = 1
            for w in succ[u]:
                if colour.get(w) == 1:
                    has_cycle = True
                elif w not in colour:
                    dfs(w)
            colour[u] = 2
        sys.setrecursionlimit(10000)
        dfs(tuple(start))
        return seen, stable, has_cycle


def fmt(t):
    return '(' + ', '.join(str(x) for x in t) + ')'


TRI = Board('triangle')
FOUR = Board('fourcycle')
EXTRA = Board('extraline')
CLOSED = Board('closedtriangle')
