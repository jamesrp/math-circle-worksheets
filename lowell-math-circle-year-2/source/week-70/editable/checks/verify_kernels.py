"""Independent mathematical checks for this week and required helpers."""
from collections import deque

from fractions import Fraction as F

from math import gcd

from itertools import combinations, combinations_with_replacement, product

import json

from pathlib import Path

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def minus(u, v):
    return (u[0] - v[0], u[1] - v[1])

def open_segment_intersection(p, v, q, w):
    """p+t*v and q+s*w; 0<t,s<1. Handles collinear overlaps."""
    determinant = cross(v, w)
    difference = minus(q, p)
    if determinant:
        t = F(cross(difference, w), determinant)
        s = F(cross(difference, v), determinant)
        return 0 < t < 1 and 0 < s < 1
    if cross(difference, v):
        return False
    index = 0 if v[0] else 1
    qa = F(q[index] - p[index], v[index])
    qb = F(q[index] + w[index] - p[index], v[index])
    return max(F(0), min(qa, qb)) < min(F(1), max(qa, qb))

def check70():
    shields = {(1, 1), (1, 3), (3, 1), (3, 3)}
    checked = 0
    earlier = 0
    for m, n in product(range(-30, 31), repeat=2):
        aimed = (2 + 4 * m, 2 + 4 * n)
        # A shot stops at its first T copy: divide the aimed lift by the (odd) gcd of
        # its half-coordinates, then test the midpoint of that first-hit segment.
        d = gcd(abs(aimed[0] // 2), abs(aimed[1] // 2))
        endpoint = (aimed[0] // d, aimed[1] // d)
        assert endpoint[0] % 4 == 2 and endpoint[1] % 4 == 2
        midpoint = tuple((F(t, 2) % 4 for t in endpoint))
        assert midpoint in shields
        assert midpoint not in {(0, 0), (2, 2)}
        checked += 1
        earlier += d > 1
    diagonals = list(product((-2, 2), repeat=2))
    pairs = 0
    for a, b in combinations(diagonals, 2):
        for tx, ty in product(range(-1, 2), repeat=2):
            assert not open_segment_intersection((0, 0), a, (4 * tx, 4 * ty), b)
        pairs += 1
    return {'first_hit_midpoints_checked': checked, 'aimed_lifts_with_an_earlier_first_hit': earlier, 'disjoint_diagonal_pairs_checked': pairs, 'blocking_minimum': 4, 'shields': sorted(shields)}
