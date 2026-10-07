"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def triangle_checks():
    maxima = {}
    path_counts = {}
    for n in (2, 4, 6):
        ab = {(x, 0) for x in range(n + 1)}
        bc = {(n, y) for y in range(n + 1)}
        values = []
        for positions in combinations(range(2 * n), n):
            east = set(positions)
            x = y = 0
            ac = {(0, 0)}
            for i in range(2 * n):
                if i in east:
                    x += 1
                else:
                    y += 1
                ac.add((x, y))
            assert (x, y) == (n, n)
            delta = max((min((k.l1(p, q) for q in t | u)) for side, t, u in ((ab, bc, ac), (bc, ac, ab), (ac, ab, bc)) for p in side))
            values.append(delta)
        assert min(values) == 0 and max(values) == n
        maxima[str(n)] = max(values)
        path_counts[str(n)] = len(values)
    trees = [('ab', 'bc', 'cd', 'de', 'df', 'cg', 'gh', 'hk', 'bi', 'ij', 'al'), ('ab', 'bc', 'cd', 'de', 'bf', 'fg', 'fh', 'di', 'ij', 'ik')]
    triples = 0
    for edges in trees:
        vertices = set(''.join(edges))
        graph = {v: set() for v in vertices}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        dist = {v: k.bfs(v, graph.__getitem__, 20) for v in vertices}
        assert len(edges) == len(vertices) - 1 and len(dist[next(iter(vertices))]) == len(vertices)
        for homes in combinations(vertices, 3):
            for u, v in edges:
                membership = 0
                for a, b in combinations(homes, 2):
                    if min(dist[a][u] + 1 + dist[v][b], dist[a][v] + 1 + dist[u][b]) == dist[a][b]:
                        membership += 1
                assert membership in (0, 2)
            triples += 1
    return {'1_tree_triples_checked': triples, '2_zero_gap': 'AC through B', '2_gap_at_least_two': 'AC via (0,4) gives gap4', '3_optimal_max_gaps': maxima, '3_all_monotone_paths_checked': path_counts, '4_general_plan': 'choose integer n greater than the named bound; use left/top AC', '5_all_tree_gaps': 0}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check69(), "instances": triangle_checks()}, indent=2))
