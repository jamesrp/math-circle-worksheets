"""Independent mathematical checks for this week and required helpers."""
from collections import deque

from fractions import Fraction as F

from itertools import combinations, combinations_with_replacement, product

import json

from pathlib import Path

def bfs(start, neighbors, depth):
    distances = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        if distances[u] == depth:
            continue
        for v in neighbors(u):
            if v not in distances:
                distances[v] = distances[u] + 1
                q.append(v)
    return distances

def l1(a, b):
    return sum((abs(x - y) for x, y in zip(a, b)))

def median_candidates(vertices, triple, distance=l1):
    return [p for p in vertices if all((distance(a, p) + distance(p, b) == distance(a, b) for a, b in combinations(triple, 2)))]

def tree(depth=3):
    graph = {(): set()}
    for level in range(depth):
        for v in [x for x in graph if len(x) == level]:
            for i in range(3 if not v else 2):
                w = v + (i,)
                graph[v].add(w)
                graph[w] = {v}
    return graph

def check67():
    grid = list(product(range(5), repeat=2))
    total = 0
    for triple in combinations_with_replacement(grid, 3):
        expected = tuple((sorted((v[i] for v in triple))[1] for i in range(2)))
        assert median_candidates(grid, triple) == [expected]
        total += 1
    assert median_candidates(grid, ((0, 0), (4, 1), (1, 4))) == [(1, 1)]
    cube = list(product(range(2), repeat=3))
    for triple in combinations_with_replacement(cube, 3):
        expected = tuple((sorted((v[i] for v in triple))[1] for i in range(3)))
        assert median_candidates(cube, triple) == [expected]
    assert median_candidates(cube, ((0, 0, 0), (1, 1, 0), (1, 0, 1))) == [(1, 0, 0)]
    cycle = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
    cd = {v: bfs(v, cycle.__getitem__, 3) for v in cycle}
    assert not median_candidates(cycle, (0, 1, 2), lambda a, b: cd[a][b])
    g = tree(3)
    td = {v: bfs(v, g.__getitem__, 10) for v in g}
    n = 0
    for triple in combinations(g, 3):
        assert len(median_candidates(g, triple, lambda a, b: td[a][b])) == 1
        n += 1
    return {'grid_triples_including_repetitions': total, 'cube_triples_including_repetitions': 120, 'tree_triples': n, 'triangle_cycle_medians': 0}
