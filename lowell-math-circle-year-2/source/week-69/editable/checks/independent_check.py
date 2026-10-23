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
    # Problem 3's middle board (v3): homes A=(0,0), B=(4,2), C=(2,4) on the 4-by-4 board
    def monotone(a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        sx, sy = (1 if dx > 0 else -1), (1 if dy > 0 else -1)
        for xs in combinations(range(abs(dx) + abs(dy)), abs(dx)):
            p = a
            route = {p}
            for i in range(abs(dx) + abs(dy)):
                p = (p[0] + sx, p[1]) if i in xs else (p[0], p[1] + sy)
                route.add(p)
            assert p == b
            yield route
    A, B, C = (0, 0), (4, 2), (2, 4)
    sides = [list(monotone(A, B)), list(monotone(B, C)), list(monotone(C, A))]
    middle, where = [], set()
    for ab in sides[0]:
        for bc in sides[1]:
            for ca in sides[2]:
                tri = (ab, bc, ca)
                best = max(min(k.l1(p, q) for j, t in enumerate(tri) if j != i for q in t) for i, s in enumerate(tri) for p in s)
                middle.append(best)
                if best == 3:
                    where |= {p for i, s in enumerate(tri) for p in s if min(k.l1(p, q) for j, t in enumerate(tri) if j != i for q in t) == 3}
    assert [len(s) for s in sides] == [15, 6, 15] and len(middle) == 1350
    assert max(middle) == 3 and where == {(0, 3), (3, 0)}
    assert max(min(k.l1(p, h) for h in (A, B, C)) for p in product(range(5), repeat=2)) == 3
    # Problem 2 key (v3): AB bottom, BC right, AC up 2, right 4, up 2 has biggest gap 2, at (0,2)
    ac = {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)}
    ab4, bc4 = {(x, 0) for x in range(5)}, {(4, y) for y in range(5)}
    tri = (ab4, bc4, ac)
    assert max(min(k.l1(p, q) for j, t in enumerate(tri) if j != i for q in t) for i, s in enumerate(tri) for p in s) == 2
    assert min(k.l1((0, 2), q) for q in ab4 | bc4) == 2
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
    return {'1_tree_triples_checked': triples, '2_zero_gap': 'AC through B', '2_gap_at_least_two': 'AC up 2, right 4, up 2 gives gap 2 at (0,2)', '3_optimal_max_gaps': maxima, '3_all_monotone_paths_checked': path_counts, '3_middle_board_A00_B42_C24': {'triangles': 1350, 'maximum_gap': 3, 'at': [[0, 3], [3, 0]]}, '4_general_plan': 'choose integer n greater than the named bound; use left/top AC', '5_all_tree_gaps': 0}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check69(), "instances": triangle_checks()}, indent=2))
