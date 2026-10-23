"""Independent mathematical checks for this week and required helpers."""
from collections import deque

from fractions import Fraction as F

from itertools import combinations, combinations_with_replacement, product

import json

from pathlib import Path

def check75():
    checked = 0
    counts = {}
    for a, b in product(range(-8, 9), repeat=2):
        difference = a - b
        if difference:
            times_set = {F(k, difference) for k in range(-abs(difference), abs(difference) + 1) if 0 < F(k, difference) < 1}
            points = {(F(a) * t % 1, t) for t in times_set}
            assert len(points) == max(abs(difference) - 1, 0)
        else:
            points = set()
        if a == 0:
            counts[str(b)] = len(points)
        checked += 1
    for n, m in product(range(-8, 9), repeat=2):
        for theta, t in product((F(0), F(1, 7), F(3, 5)), (F(0), F(1, 3), F(1))):
            twist = lambda k, x: ((x[0] + k * x[1]) % 1, x[1])
            assert twist(n, twist(m, (theta, t))) == twist(n + m, (theta, t))
            if t in (0, 1):
                assert twist(n, (theta, t)) == (theta, t)
    return {'winding_pairs_checked': checked, 'counts_against_zero_winding': counts, 'scope': 'Proper simple joining arcs; identical fixed endpoints; minimum interior crossings.'}
