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

def elevator_neighbors(s):
    x, h = s
    out = [(x - 2 ** h, h), (x + 2 ** h, h), (x, h + 1)]
    if h:
        out.append((x, h - 1))
    return out

def check74():
    d = bfs((0, 0), elevator_neighbors, 12)
    assert d[16, 0] == 8
    bounds = [(7 - 2 * h) * 2 ** h for h in range(4)]
    assert bounds == [7, 10, 12, 8] and max(bounds) < 16
    for budget in range(1, 13):
        actual = max((abs(x) for (x, h), dist in d.items() if not h and dist <= budget))
        expected = max(((budget - 2 * H) * 2 ** H for H in range(budget // 2 + 1)))
        assert actual == expected, (budget, actual, expected)
    return {'states_checked_through_distance_12': len(d), 'target_16_distance': 8, 'seven_move_height_bounds': bounds, 'power_of_two_distances': {str(n): d[n, 0] for n in (1, 2, 4, 8, 16, 32, 64)}}
