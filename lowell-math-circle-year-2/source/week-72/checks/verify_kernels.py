"""Independent mathematical checks for this week and required helpers."""
from collections import deque

from fractions import Fraction as F

from itertools import combinations, combinations_with_replacement, product

import json

from pathlib import Path

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def robot(word):
    x = y = z = 0
    points = [(0, 0)]
    for move in word:
        if move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        elif move == 'N':
            y += 1
            z += x
        elif move == 'S':
            y -= 1
            z -= x
        else:
            raise ValueError(move)
        points.append((x, y))
    return ((x, y, z), points)

def multiply(p, q):
    x, y, z = p
    a, b, c = q
    return (x + a, y + b, z + c + x * b)

def check72():
    words = sorted(set((''.join(p) for p in __import__('itertools').permutations('EENN'))))
    values = {w: robot(w)[0][2] for w in words}
    assert values == {'EENN': 4, 'ENEN': 3, 'ENNE': 2, 'NEEN': 2, 'NENE': 1, 'NNEE': 0}
    assert robot('ENWS')[0] == (0, 0, 1)
    assert robot('NESW')[0] == (0, 0, -1)
    checked = 0
    closed = 0
    for length in range(8):
        for w in product('ENWS', repeat=length):
            (x, y, z), points = robot(w)
            twice_area = sum((cross(a, b) for a, b in zip(points, points[1:] + [(0, 0)])))
            assert 2 * z - x * y == twice_area
            if x == y == 0:
                assert 2 * z == twice_area
                closed += 1
            checked += 1
    states = list(product(range(-1, 2), repeat=3))
    for a, b, c in product(states, repeat=3):
        assert multiply(multiply(a, b), c) == multiply(a, multiply(b, c))
    for p in states:
        x, y, z = p
        assert multiply(p, (-x, -y, -z + x * y)) == (0, 0, 0)
    return {'monotone_counters': values, 'words_checked_through_length_7': checked, 'closed_words_checked': closed, 'associativity_triples_checked': len(states) ** 3}
