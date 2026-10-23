"""Independent mathematical checks for this week and required helpers."""
from collections import deque

from fractions import Fraction as F

from itertools import combinations, combinations_with_replacement, product

import json

from pathlib import Path

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def minus(u, v):
    return (u[0] - v[0], u[1] - v[1])

def check73():
    points = list(product((F(i, 2) for i in range(9)), (F(i, 2) for i in range(3))))
    pair_count = 0
    attained = False
    for a, b in combinations(points, 2):
        dx, dy = minus(a, b)
        before = dx * dx + dy * dy
        after = dx * dx / 4 + 4 * dy * dy
        assert after <= 4 * before
        if after == 4 * before:
            attained = True
        pair_count += 1
    assert attained
    return {'exact_sample_pairs': pair_count, 'squared_stretch_bound': 4, 'bound_attained': True, 'scope': 'All-pairs optimality uses the universal boundary proof.'}
