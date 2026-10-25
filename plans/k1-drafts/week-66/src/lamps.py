"""Lamplighter street on places -3..3 (and an endless check).
State: (frozenset of lit places, walker place). Start: (empty, 0).
Moves: L, R, F (flip lamp under walker)."""
from collections import deque
from itertools import product

LO, HI = -3, 3

def moves(state, lo=LO, hi=HI):
    lit, w = state
    if w - 1 >= lo:
        yield 'L', (lit, w - 1)
    if w + 1 <= hi:
        yield 'R', (lit, w + 1)
    yield 'F', (lit ^ frozenset([w]), w)

START = (frozenset(), 0)

def bfs(lo=LO, hi=HI):
    dist = {START: 0}
    q = deque([START])
    while q:
        s = q.popleft()
        for _, t in moves(s, lo, hi):
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist

DIST = bfs()
DIST_BIG = bfs(-6, 6)

def T(lit, w):
    return (frozenset(lit), w)

def fewest(lit, w):
    d = DIST[T(lit, w)]
    assert d == DIST_BIG[T(lit, w)]
    return d

def formula(lit, w):
    lit = set(lit)
    if not lit:
        return abs(w)
    a, b = min(lit | {0}), max(lit | {0})
    walk = min((0 - a) + (b - a) + abs(w - b), (b - 0) + (b - a) + abs(w - a))
    return len(lit) + walk

def words_exact(lit, w, n):
    """All move words of length exactly n reaching the target (seven-lamp street)."""
    target = T(lit, w)
    out = []
    def rec(state, word):
        if len(word) == n:
            if state == target:
                out.append(word)
            return
        # prune: remaining moves must be >= distance from state to target? use parity/size crude prune
        for m, t in moves(state):
            rec(t, word + m)
    rec(START, '')
    return out

def wrong_order(lit, w):
    """fewest moves among words whose walker reaches the far end lamps in the other order"""
    # brute: search states augmented by which end reached first
    lit = set(lit)
    a, b = min(lit), max(lit)
    best = {}
    # BFS over (state, first) where first in {None,'a','b'}
    start = (START, None)
    dist = {start: 0}
    q = deque([start])
    while q:
        (s, first) = q.popleft()
        for _, t in moves(s):
            f = first
            if f is None:
                if t[1] == a and a < 0:
                    f = 'a'
                elif t[1] == b and b > 0:
                    f = 'b'
            key = (t, f)
            if key not in dist:
                dist[key] = dist[(s, first)] + 1
                q.append(key)
    tgt = T(lit, w)
    return {f: dist.get((tgt, f)) for f in ('a', 'b')}

def neighbours(lit, w):
    s = T(lit, w)
    return [(m, sorted(t[0]), t[1], DIST[t]) for m, t in moves(s)]

def show(name, lit, w):
    f = fewest(lit, w)
    assert f == formula(lit, w), (lit, w)
    ws = words_exact(lit, w, f)
    print(f"{name}: lit={sorted(lit)} walker={w}: fewest {f}; {len(ws)} shortest word(s): {ws[:6]}")
    return f

if __name__ == '__main__':
    # formula check over all targets; the printed pictures are checked in check.py
    for (lit, w), d in DIST.items():
        assert d == formula(lit, w)
        assert d == DIST_BIG[(lit, w)]
    print("formula agrees on all", len(DIST), "targets")
