"""General claims in the pages and the adult guide, checked by brute force over every connected
loopless multigraph with up to 5 islands and up to 7 bridges (labelled), using walk search only:
  - the start/end rule (guide overview and section 5; 2-3 P6, 4-5 P4 and P9),
  - start sets are all islands, two islands or none, never one (2-3 P9),
  - the number of odd islands is even (4-5 P6),
  - a closed walk needs exactly k new bridges for 2k odd islands (guide section 5, 2-3 P5),
  - fewest strokes = max(1, k) for 2k odd points (guide section 5, 4-5 P7),
  - fewest extra counters = minimum matching of odd islands by distance; open route leaves the best
    pair unmatched (guide section 5, 4-5 P10),
plus the 2-3 Problem 8 build targets and the guide's statements about them.
Run: python3 check_theory.py > check_theory.out
"""
import os
import sys
import itertools
from functools import lru_cache
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import Town, additions, extra_counters, fewest

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def multigraphs(n, m):
    V = 'ABCDE'[:n]
    pairs = list(itertools.combinations(V, 2))
    for combo in itertools.combinations_with_replacement(pairs, m):
        t = Town(V, combo)
        if t.connected():
            yield t


def min_trails(t):
    """Fewest edge-disjoint trails covering every edge, by search over trails."""
    m = len(t.E)
    full = (1 << m) - 1

    def trails_from(mask):
        out = set()

        def rec(v, used):
            if used:
                out.add(used)
            for i, w in t.inc[v]:
                if not (mask | used) >> i & 1:
                    rec(w, used | 1 << i)
        for v in t.V:
            rec(v, 0)
        return out

    @lru_cache(maxsize=None)
    def best(mask):
        if mask == full:
            return 0
        # the trail containing the lowest unused edge
        low = next(i for i in range(m) if not mask >> i & 1)
        return min(1 + best(mask | tr) for tr in trails_from(mask) if tr >> low & 1)
    return best(0)


def dist(t):
    D = {}
    for s in t.V:
        d = {s: 0}
        q = deque([s])
        while q:
            x = q.popleft()
            for _, y in t.inc[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        D[s] = d
    return D


def matching(nodes, D):
    if not nodes:
        return 0
    a = nodes[0]
    return min(D[a][b] + matching(nodes[1:j] + nodes[j + 1:], D) for j, b in enumerate(nodes[1:], 1))


counts = {'graphs': 0}
bad_rule, bad_one, bad_hand, bad_k, bad_strokes, bad_cpp = [], [], [], [], [], []
for n in range(2, 6):
    for m in range(n - 1, 8):
        for t in multigraphs(n, m):
            counts['graphs'] += 1
            se = t.start_end()
            odd = t.odd()
            # rule
            if len(odd) == 0:
                ok = se == {v: {v} for v in t.V}
            elif len(odd) == 2:
                ok = se == {odd[0]: {odd[1]}, odd[1]: {odd[0]}}
            else:
                ok = se == {}
            if not ok:
                bad_rule.append((t.E, se))
            if len(se) == 1:
                bad_one.append(t.E)
            if len(odd) % 2:
                bad_hand.append(t.E)
            # new bridges for a closed walk
            if m <= 6 and n <= 5 and len(odd) <= 4:
                k, _ = fewest(lambda k: additions(t, k, closed=True), 3)
                if k != len(odd) // 2:
                    bad_k.append((t.E, k))
            # strokes
            if m <= 6:
                s = min_trails(t)
                if s != max(1, len(odd) // 2):
                    bad_strokes.append((t.E, s))
            # delivery routes
            if m <= 5:
                D = dist(t)
                kc, _ = fewest(lambda k: extra_counters(t, k, True), 6)
                ko, _ = fewest(lambda k: extra_counters(t, k, False), 6)
                fc = matching(odd, D)
                fo = 0 if len(odd) <= 2 else min(matching([o for o in odd if o not in pr], D) for pr in itertools.combinations(odd, 2))
                if (kc, ko) != (fc, fo):
                    bad_cpp.append((t.E, (kc, ko), (fc, fo)))
print(f'  connected loopless multigraphs checked: {counts["graphs"]} (2-5 islands, up to 7 bridges)')
check('start/end rule: 0 odd -> every start, closed; 2 odd -> start at one, end at other; else none', not bad_rule, bad_rule[:3])
check('2-3 P9: no town with a bridge has exactly one possible start', not bad_one, bad_one[:3])
check('4-5 P6: the number of odd islands is always even', not bad_hand, bad_hand[:3])
check('closed walk needs exactly (odd islands)/2 new bridges (up to 6 bridges)', not bad_k, bad_k[:3])
check('fewest strokes = max(1, odd/2), by search over trails (up to 6 bridges)', not bad_strokes, bad_strokes[:3])
check('fewest extra counters = min matching of odd islands; open: leave best pair (up to 5 bridges)', not bad_cpp, bad_cpp[:3])

print('---- 2-3 Problem 8 targets')
# (a) 4 islands, 6 bridges, start on any island
sols = [t for t in multigraphs(4, 6) if t.start_end() and set(t.start_end()) == set(t.V)]
simple = [t for t in sols if len(set(frozenset(e) for e in t.E)) == len(t.E)]
check('(a) 4 islands, 6 bridges, any start: possible, and only with two bridges between some pair', sols and not simple,
      f'{len(sols)} labelled solutions, {len(simple)} without a repeated pair')
k4 = Town('ABCD', list(itertools.combinations('ABCD', 2)))
check('(a) guide: single bridges on 4 islands with 6 bridges join every pair once and every island is odd',
      len(k4.odd()) == 4 and len([t for t in multigraphs(4, 6) if len(set(frozenset(e) for e in t.E)) == 6]) == 1)
ex1 = Town('ABCD', [('A', 'B'), ('A', 'B'), ('B', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'D')])
check('(a) guide example: A B C D in a row, every bridge doubled', set(ex1.start_end()) == set('ABCD') and len(ex1.E) == 6)
# (b) 5 islands, 5 bridges, no walk
ex2 = Town('ABCDE', [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('B', 'E')])
check('(b) guide example: triangle A B C with tails A-D and B-E has no walk', not ex2.has_walk() and ex2.connected())
check('(b) such towns exist without double bridges', any(not t.has_walk() and len(set(frozenset(e) for e in t.E)) == 5 for t in multigraphs(5, 5)))
# (c) 6 islands, 8 bridges, starts only A or F
ex3 = Town('ABCDEF', [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A'), ('A', 'C'), ('C', 'F')])
check('(c) guide example: ring A..F plus A-C and C-F: starts exactly A and F', set(ex3.start_end()) == {'A', 'F'} and len(ex3.E) == 8)
# (d) 3 islands, 5 bridges, starts only A or B
sols = [t for t in multigraphs(3, 5) if set(t.start_end()) == {'A', 'B'}]
mult = []
for t in sols:
    c = {}
    for e in t.E:
        c[frozenset(e)] = c.get(frozenset(e), 0) + 1
    mult.append((max(c.values()), sorted((''.join(sorted(k)), v) for k, v in c.items())))
check('(d) 3 islands, 5 bridges, starts only A or B: the only way with at most 2 bridges per pair is A-B once, A-C twice, B-C twice',
      [m for m in mult if m[0] <= 2] == [(2, [('AB', 1), ('AC', 2), ('BC', 2)])], mult)
print()
print('FAILURES:', FAILS if FAILS else 'none')
