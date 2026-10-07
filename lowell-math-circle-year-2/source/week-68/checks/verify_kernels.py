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

def tree(depth=3):
    graph = {(): set()}
    for level in range(depth):
        for v in [x for x in graph if len(x) == level]:
            for i in range(3 if not v else 2):
                w = v + (i,)
                graph[v].add(w)
                graph[w] = {v}
    return graph

def components(graph, blocked):
    unseen = set(graph) - set(blocked)
    out = []
    while unseen:
        start = next(iter(unseen))
        comp = {start}
        unseen.remove(start)
        q = [start]
        for v in q:
            for w in graph[v]:
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    q.append(w)
        out.append(comp)
    return out

def check68():
    g = tree(6)
    counts = []
    for radius in range(5):
        cs = components(g, {v for v in g if len(v) <= radius})
        assert all((any((len(v) == 6 for v in c)) for c in cs))
        assert len(cs) == 3 * 2 ** radius
        counts.append(len(cs))
    grid = {p: {q for q in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)) if max(abs(q[0]), abs(q[1])) <= 5} for p in product(range(-5, 6), repeat=2)}
    assert len(components(grid, set(product(range(-2, 3), repeat=2)))) == 1
    cs = components(grid, {(-1, 0), (1, 0), (0, -1), (0, 1)})
    assert sorted((len(c) for c in cs)) == [1, 116]
    ladder = {(x, y): {q for q in ((x - 1, y), (x + 1, y), (x, 1 - y)) if -8 <= q[0] <= 8} for x, y in product(range(-8, 9), range(2))}
    assert len(components(ladder, {(0, 0), (0, 1)})) == 2
    assert len(components(ladder, {(0, 0)})) == 1
    return {'finite_tree_outward_component_counts': counts, 'grid_pocket_component_sizes': [1, 116], 'ladder_whole_rung_deletion': 2, 'ladder_one_vertex_deletion': 1, 'scope': 'Finite windows only; infinite-end conclusions use the proof.'}
