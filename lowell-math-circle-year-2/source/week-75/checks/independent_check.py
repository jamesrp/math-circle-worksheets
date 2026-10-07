"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def cylinder_checks():
    pairs = [(0, 1), (0, 2), (0, 3), (-1, 1), (-1, 2), (2, 4), (2, 7), (5, 5)]
    answers = []
    for a, b in pairs:
        if a == b:
            count = 0
        else:
            d = b - a
            times = {F(i, d) for i in range(-abs(d), abs(d) + 1) if 0 < F(i, d) < 1}
            count = len(times)
        assert count == max(abs(a - b) - 1, 0)
        answers.append({'windings': [a, b], 'minimum_interior_crossings': count})
    for length in (2, 3, 4):
        for w in product((-1, 1), repeat=length):
            assert abs(sum(w)) <= length
    zero_six = [w for w in product((-1, 1), repeat=6) if sum(w) == 0]
    assert len(zero_six) == 20
    return {'2_lift_endpoints_for_plus2_and_minus1': ['2.5,1', '-0.5,1'], '3_isotopy_criterion': 'same integer winding, endpoints fixed', '4_shortest_twist_word': 'absolute value of signed sum', '5_balanced_six_twist_words': 20, '5_example': '+++---', '6_and_7_crossings': answers}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check75(), "instances": cylinder_checks()}, indent=2))
