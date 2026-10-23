#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 86 (plans/review/week-86.md).

Standard library only. Exact game values under the printed rules: C places, then R
(placing on C is capture); C moves first; each player stays or crosses one road;
sharing a dot is capture.

1. Shared Problem 2's new T1 (branch c-f-g-h, C starts at h): walking toward R catches
   every robber, the guaranteed capture takes 5 cop turns, and R can now switch from the
   branch to a side of the row ahead of C (the card's reason for the change).
2. Guide p. 3, shared Problem 4: "stay on or move to a dot across from C" (a farthest
   dot) is never caught on rings of 4 to 14 dots, whatever C does and however R breaks
   ties; on the pentagon the dots across from C are exactly those outside C's reach.
3. Guide p. 4, upper Problem 2: of the ten two-chord pentagons exactly the five whose
   chords share an endpoint are cop-win; with a-c and b-d, b and c reach the same places
   and folding b leaves the square a-c-d-e.
4. Guide p. 2, K-1 route: the five-dot path from c (2 cop turns), the triangle (caught on
   C's first move) and the square (R escapes forever).
"""
from collections import deque
from itertools import combinations


def graph(edges, verts=None):
    g = {}
    for a, b in edges:
        g.setdefault(a, {a}).add(b)
        g.setdefault(b, {b}).add(a)
    for v in verts or ():
        g.setdefault(v, {v})
    return g


def values(g):
    """Least number of cop turns that guarantees capture from (cop, robber) with C to move."""
    V = list(g)
    INF = float('inf')
    val = {(c, r): (0 if c == r else INF) for c in V for r in V}
    changed = True
    while changed:
        changed = False
        for c in V:
            for r in V:
                if c == r:
                    continue
                best = INF
                for c2 in g[c]:
                    if c2 == r:
                        best = 1
                        break
                    worst = max(1 + (0 if r2 == c2 else val[(c2, r2)]) for r2 in g[r])
                    best = min(best, worst)
                if best < val[(c, r)]:
                    val[(c, r)] = best
                    changed = True
    return val


def start_value(g, c):
    val = values(g)
    return max(val[(c, r)] for r in g)


def dist(g, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for w in g[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


def ring(n):
    v = [chr(97 + i) for i in range(n)]
    return graph([(v[i], v[(i + 1) % n]) for i in range(n)]), v


FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# 1. New T1
T1 = graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('c', 'f'), ('f', 'g'), ('g', 'h')])
D = {v: dist(T1, v) for v in T1}
check(start_value(T1, 'h') == 5, 'T1 (c-f-g-h): C starting at h guarantees capture in 5 cop turns, no fewer')
check(start_value(T1, 'c') == 3, 'T1: the best start is still c, now 3 cop turns (C must start at h on the page)')


def toward(c, r):
    return min((w for w in T1[c] if w != c), key=lambda w: D[w][r])


def walk_catches(c0):
    """Walking toward R from c0 catches R against every robber start and every reply: the
    positions R can reach against this cop form no cycle, so every play ends in capture."""
    nxt = {}
    stack = [(c0, r) for r in T1 if r != c0]
    while stack:
        c, r = stack.pop()
        if (c, r) in nxt:
            continue
        c2 = toward(c, r)
        nxt[(c, r)] = [] if c2 == r else [(c2, r2) for r2 in T1[r] if r2 != c2]
        stack += nxt[(c, r)]
    state = {}

    def acyclic(u):
        state[u] = 1
        for w in nxt[u]:
            if state.get(w) == 1 or (w not in state and not acyclic(w)):
                return False
        state[u] = 2
        return True
    return all(acyclic(u) for u in list(nxt) if u not in state)


check(walk_catches('h'), 'T1: walking toward R from h catches R from every start, whatever R does')
check(D['h']['c'] == 3 and D['f']['c'] == 1, 'T1: a robber on f reaches the row (c) in one move while C at h needs three; from c it can choose either side')

# 2. Farthest-dot escape on rings
for n in range(4, 15):
    g, v = ring(n)
    far = lambda c: {x for x in v if dist(g, c)[x] == n // 2}
    # states (c, r) before a cop turn with r a farthest dot; R policy: any reachable farthest dot
    ok = True
    for c0 in v:
        frontier = [(c0, r0) for r0 in far(c0)]
        seen = set()
        while frontier:
            c, r = frontier.pop()
            if (c, r) in seen:
                continue
            seen.add((c, r))
            for c2 in g[c]:
                if c2 == r:
                    ok = False
                    continue
                choices = [r2 for r2 in g[r] if r2 in far(c2)]
                if not choices:
                    ok = False
                for r2 in choices:  # every tie-break
                    frontier.append((c2, r2))
    check(ok, f'ring of {n}: staying on or moving to a dot across from C is never caught')
g5, v5 = ring(5)
for c in v5:
    across = {x for x in v5 if dist(g5, c)[x] == 2}
    check(across == set(v5) - g5[c], f'pentagon, C at {c}: the dots across from C are exactly those outside its reach')

# 3. Two chords on the pentagon
chords = [p for p in combinations(v5, 2) if p[1] not in g5[p[0]]]
for pair in combinations(chords, 2):
    g = graph([(x, y) for x in v5 for y in g5[x] if x < y] + list(pair))
    share = bool(set(pair[0]) & set(pair[1]))
    cop_win = min(start_value(g, c) for c in g) < float('inf')
    check(cop_win == share, f'pentagon + {pair[0][0]}-{pair[0][1]}, {pair[1][0]}-{pair[1][1]}: '
          f'{"cop-win" if cop_win else "robber-win"}; chords {"share" if share else "do not share"} an endpoint')
g = graph([(x, y) for x in v5 for y in g5[x] if x < y] + [('a', 'c'), ('b', 'd')])
check(g['b'] == g['c'] == {'a', 'b', 'c', 'd'}, 'a-c with b-d: b and c reach exactly a, b, c, d')
rest = {x: g[x] - {'b'} for x in g if x != 'b'}
check({frozenset((x, y)) for x in rest for y in rest[x] if x != y} == {frozenset(p) for p in ('ac', 'cd', 'de', 'ea')},
      'folding b leaves the square a-c-d-e')

# 4. K-1 route
P5 = graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')])
check(start_value(P5, 'c') == 2, 'K-1 route: five-dot path from c, capture within 2 cop turns')
g3, _ = ring(3)
check(all(start_value(g3, c) == 1 for c in g3), 'K-1 route: triangle, C catches R on its first move from any start')
g4, _ = ring(4)
check(all(start_value(g4, c) == float('inf') for c in g4), 'K-1 route: square, R escapes forever from every C start')

print(f'{"FAIL" if FAILS else "PASS"}: {len(FAILS)} failures')
raise SystemExit(1 if FAILS else 0)
