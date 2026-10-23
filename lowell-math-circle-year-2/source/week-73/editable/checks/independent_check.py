"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def stretch_checks():
    old = [(F(0), F(0)), (F(4), F(0)), (F(4), F(1)), (F(0), F(1)), (F(2), F(1, 2))]
    corners = [(F(0), F(0)), (F(2), F(0)), (F(2), F(2)), (F(0), F(2))]
    offcenter = 0
    tested = 0
    for u, v in product((F(i, 8) for i in range(1, 16)), repeat=2):
        new = corners + [(u, v)]
        squared = []
        for i, j in combinations(range(5), 2):
            a = k.minus(old[i], old[j])
            b = k.minus(new[i], new[j])
            squared.append((b[0] ** 2 + b[1] ** 2) / (a[0] ** 2 + a[1] ** 2))
        assert max(squared) == 4
        probes = [4 * ((u - 1) ** 2 + v * v), 4 * ((u - 1) ** 2 + (v - 2) ** 2)]
        if (u, v) == (1, 1):
            assert max(probes) == 4
        else:
            assert max(probes) > 4
            offcenter += 1
        for i in range(4):
            a, b = (corners[i], corners[(i + 1) % 4])
            assert k.cross(k.minus(b, a), k.minus((u, v), a)) > 0
        tested += 1
    assert max(F(6, 4), F(2)) == 2
    assert max(F(2, 4), F(3)) == 3
    examples = [(F(6), F(1)), (F(3), F(3, 2))]
    for w, h in examples:
        assert max(w / 4, h) == F(3, 2)
    return {'fan_center_placements_checked': tested, 'offcenter_midpoint_failures': offcenter, '1_five_pin_score_everywhere': 2, '2_unique_survivor': [1, 1], '5_6_by_2': 2, '5_2_by_3': 3, '6_examples': ['6 by 1', '3 by 1.5'], '6_general_condition': 'max(width/4,height)=1.5'}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check73(), "instances": stretch_checks()}, indent=2))
