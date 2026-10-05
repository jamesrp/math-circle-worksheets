"""Check the general claims of the guide and 4-5 Problem 7 on many small boards.

For every directed graph on {s,a,b,t} (all 4096) and on random graphs with 5 and 6
dots, and for EVERY collection of edge-disjoint simple routes on each graph:
  (1) largest collection size = fewest blocking arrows = min out-count of a split;
  (2) no change-walk from s reaches t  <=>  the collection is largest   (4-5 P7);
  (3) toggling any s-t change-walk and discarding cycles gives |C|+1 edge-disjoint
      simple routes;
  (4) when no change-walk exists, the reachable set S has every arrow leaving S
      reserved, every arrow entering S unreserved, and exactly |C| arrows leaving S.
Also counts collections that are stuck (no route fits beside them) but not largest.
Writes theorem_check.out.
"""
import os, sys, random
from itertools import combinations, permutations
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from routes import *


def all_collections(E):
    P = simple_paths(E)
    out = []

    def rec(i, used, chosen):
        out.append(tuple(chosen))
        for j in range(i, len(P)):
            if not (set(P[j]) & used):
                rec(j + 1, used | set(P[j]), chosen + [P[j]])
    rec(0, frozenset(), [])
    return out


def check_graph(V, E, stats):
    k, _ = packings(E)
    c, _ = min_cuts(E)
    sp = min(len(o) for S, o, i in splits(E, V))
    assert k == c == sp, (E, k, c, sp)
    for C in all_collections(E):
        R = {e for p in C for e in p}
        W = change_walks(E, R)
        if W:
            assert len(C) < k, ('walk but already largest', E, C)
            for w in W:
                rts, rest = decompose(toggle(R, w))
                assert len(rts) == len(C) + 1 and edge_disjoint(rts) and all(r in simple_paths(E) for r in rts), (E, C, w)
                if rest:
                    stats['cycles_left_after_toggle'] += 1
            stats['walk'] += 1
        else:
            assert len(C) == k, ('no walk but not largest', E, C)
            S = residual_reach(E, R)
            out = [e for e in E if e[0] in S and e[1] not in S]
            inn = [e for e in E if e[1] in S and e[0] not in S]
            assert all(e in R for e in out) and not any(e in R for e in inn) and len(out) == len(C)
            stats['nowalk'] += 1
        stuck = not simple_paths(E, closed=frozenset(R))
        if stuck and len(C) < k:
            stats['stuck_not_largest'] += 1
    stats['graphs'] += 1


stats = {'graphs': 0, 'walk': 0, 'nowalk': 0, 'stuck_not_largest': 0, 'cycles_left_after_toggle': 0}
V = ['s', 'a', 'b', 't']
arcs = [(u, v) for u in V for v in V if u != v]
for mask in range(1 << len(arcs)):
    E = [arcs[i] for i in range(len(arcs)) if mask >> i & 1]
    check_graph(V, E, stats)
lines = [f'all 4096 graphs on 4 dots: {stats}']
random.seed(13)
for n, trials, p in [(5, 20000, 0.45), (6, 8000, 0.35)]:
    stats = {'graphs': 0, 'walk': 0, 'nowalk': 0, 'stuck_not_largest': 0, 'cycles_left_after_toggle': 0}
    V = ['s'] + [chr(97 + i) for i in range(n - 2)] + ['t']
    arcs = [(u, v) for u in V for v in V if u != v]
    for _ in range(trials):
        E = [a for a in arcs if random.random() < p]
        check_graph(V, E, stats)
    lines.append(f'{trials} random graphs on {n} dots (arc probability {p}): {stats}')
lines.append('all assertions passed')
print('\n'.join(lines))
open(os.path.join(HERE, 'theorem_check.out'), 'w').write('\n'.join(lines) + '\n')
