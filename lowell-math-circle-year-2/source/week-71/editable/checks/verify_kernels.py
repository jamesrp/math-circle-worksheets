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

def times(a, v):
    return (a * v[0], a * v[1])

def rectangle_bounces(width, height, start, velocity, steps=12):
    x, y = map(F, start)
    dx, dy = map(F, velocity)
    word = []
    for _ in range(steps):
        choices = []
        if dx > 0:
            choices.append(((F(width) - x) / dx, 'R'))
        if dx < 0:
            choices.append((-x / dx, 'L'))
        if dy > 0:
            choices.append(((F(height) - y) / dy, 'T'))
        if dy < 0:
            choices.append((-y / dy, 'B'))
        t = min((t for t, _ in choices))
        hits = [s for u, s in choices if u == t]
        if len(hits) != 1:
            return None
        assert t > 0
        x += t * dx
        y += t * dy
        word.append(hits[0])
        if hits[0] in 'RL':
            dx = -dx
        else:
            dy = -dy
    return ''.join(word)

def check71():
    checked = 0
    corner_excluded = 0
    for ix, iy in product(range(1, 6), repeat=2):
        for dx, dy in product(range(-3, 4), repeat=2):
            if not (dx or dy):
                continue
            start = (F(ix, 6), F(iy, 6))
            velocity = (F(dx), F(dy))
            w = rectangle_bounces(1, 1, start, velocity)
            v = rectangle_bounces(3, 2, (3 * start[0], 2 * start[1]), (3 * dx, 2 * dy))
            assert w == v
            if w is None:
                corner_excluded += 1
                continue
            for a, b, c in zip(w, w[1:], w[2:]):
                assert not (a == c and (a in 'LR') != (b in 'LR'))
            checked += 1
    start = (F(11, 16), F(1, 16))
    a = (F(1, 2), F(0))
    b = (F(1, 8), F(1, 8))
    incoming = minus(a, start)
    first = minus(b, a)
    second = minus(a, b)
    assert cross((incoming[0], -incoming[1]), first) == 0
    reflect_b = lambda v: ((-v[0] + 3 * v[1]) / 2, (v[0] + v[1]) / 2)
    assert reflect_b(first) == second
    for p in (start, a, b):
        assert 0 <= p[0] - p[1] <= 1 and 0 <= 2 * p[1] <= 1
    assert 0 < a[0] < 1 and 0 < b[1] < F(1, 2)
    return {'corner_free_rectangle_examples': checked, 'corner_examples_excluded': corner_excluded, 'stretch_factors': [3, 2], 'rhombus_ABA_witness_scaled_y': {'start': [str(t) for t in start], 'A': [str(t) for t in a], 'B': [str(t) for t in b], 'third_bounce': 'same A point'}}
