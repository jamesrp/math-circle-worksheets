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

def lamp_neighbors(s):
    x, lamps = s
    return ((x - 1, lamps), (x + 1, lamps), (x, lamps ^ frozenset([x])))

def lamp_formula(s):
    x, lamps = s
    low, high = (min([0, *lamps]), max([0, *lamps]))
    walking = min(-low + high - low + abs(x - high), high + high - low + abs(x - low))
    return len(lamps) + walking

def check66():
    distances = bfs((0, frozenset()), lamp_neighbors, 12)
    for s, d in distances.items():
        assert lamp_formula(s) == d, (s, d, lamp_formula(s))
    target = (0, frozenset([-1, 0, 1]))
    assert distances[target] == 7
    near = [distances[s] for s in lamp_neighbors(target)]
    assert near == [6, 6, 6]
    return {'states_checked_through_distance_12': len(distances), 'target_distance': 7, 'neighbor_distances': near}
