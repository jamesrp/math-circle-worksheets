"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def median_checks():
    grid = list(product(range(5), repeat=2))
    assert k.median_candidates(grid, ((0, 0), (4, 1), (1, 4))) == [(1, 1)]
    assert k.median_candidates(grid, ((0, 3), (4, 0), (4, 4))) == [(4, 3)]
    edges = ('au', 'uv', 'vw', 'wb', 'vt', 'tc', 'ws', 'sr', 'uq')
    graph = {p: set() for p in 'auvwbtcsrq'}
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    dist = {p: k.bfs(p, graph.__getitem__, 12) for p in graph}
    assert k.median_candidates(graph, 'abc', lambda a, b: dist[a][b]) == ['v']
    cube = list(product(range(2), repeat=3))
    assert k.median_candidates(cube, ((0, 0, 1), (0, 1, 0), (1, 1, 1))) == [(0, 1, 1)]
    return {'1_left': [1, 1], '1_right': [4, 3], '2': 'unique for every placement', '3_tree': 'v=(2,0)', '3_triangle': 'none', '3_square': 'B', '4_left': '100', '4_right': '011', '5': 'coordinatewise majority'}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check67(), "instances": median_checks()}, indent=2))
