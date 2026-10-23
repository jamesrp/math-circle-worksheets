"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def shield_checks():
    first_hits = []
    for x, y in product((-2, 2, 6, 10), repeat=2):
        g = math.gcd(abs(x // 2), abs(y // 2))
        first = (x // g, y // g)
        midpoint = (F(first[0], 2) % 4, F(first[1], 2) % 4)
        assert midpoint in {(1, 1), (1, 3), (3, 1), (3, 3)}
        first_hits.append({'lift': [x, y], 'first_lift': list(first), 'blocking_midpoint': list(map(int, midpoint))})
    return {'map_targets': 16, 'first_hits': first_hits, 'minimum_for_problems_1_and_4': 4}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check70(), "instances": shield_checks()}, indent=2))
