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

def tree(depth=3):
    graph = {(): set()}
    for level in range(depth):
        for v in [x for x in graph if len(x) == level]:
            for i in range(3 if not v else 2):
                w = v + (i,)
                graph[v].add(w)
                graph[w] = {v}
    return graph

def check69():
    records = []
    for n in range(1, 13):
        ab = {(x, 0) for x in range(n + 1)}
        bc = {(n, y) for y in range(n + 1)}
        ac = {(0, y) for y in range(n + 1)} | {(x, n) for x in range(n + 1)}
        assert min((l1((0, n), p) for p in ab | bc)) == n
        delta = max((min((l1(p, q) for q in t | u)) for s, t, u in ((ab, bc, ac), (bc, ab, ac), (ac, ab, bc)) for p in s))
        assert delta == n
        records.append(delta)
    g = tree(3)
    d = {v: bfs(v, g.__getitem__, 10) for v in g}
    count = 0
    for a, b, c in combinations(g, 3):
        sides = [{p for p in g if d[x][p] + d[p][y] == d[x][y]} for x, y in ((a, b), (b, c), (a, c))]
        assert all((sides[i] <= sides[(i + 1) % 3] | sides[(i + 2) % 3] for i in range(3)))
        count += 1
    return {'grid_triangle_thinness_n_1_to_12': records, 'tree_triangles_checked': count}
