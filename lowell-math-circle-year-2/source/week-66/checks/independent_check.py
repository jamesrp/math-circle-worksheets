"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def lamp_checks():
    d = k.bfs((0, frozenset()), k.lamp_neighbors, 12)
    data = [('1A', 1, {1}, 2), ('1B', 1, {-1, 1}, 5), ('1C', 0, {0, 2}, 6), ('2A', -2, {-2, 0, 2}, 9), ('2B', 0, {-2, 0, 2}, 11), ('2C', 2, {-2, 0, 2}, 9), ('3', 0, {-1, 0, 1}, 7), ('4L', -1, {-1, 0, 1}, 6), ('4R', 1, {-1, 0, 1}, 6), ('4F', 0, {-1, 1}, 6)]
    out = {}
    for problem, p, lamps, expected in data:
        assert d[p, frozenset(lamps)] == expected
        out[problem] = expected
    return out

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check66(), "instances": lamp_checks()}, indent=2))
