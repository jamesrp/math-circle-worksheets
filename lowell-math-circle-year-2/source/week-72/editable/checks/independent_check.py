"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def robot_at(word, start=(0, 0, 0)):
    x, y, z = start
    for move in word:
        if move == 'E':
            x += 1
        if move == 'W':
            x -= 1
        if move == 'N':
            y += 1
            z += x
        if move == 'S':
            y -= 1
            z -= x
    return (x, y, z)

def robot_checks():
    values = {''.join(w): robot_at(w)[2] for w in permutations('ENWS')}
    assert set(values.values()) == {-1, 0, 1}
    distribution = {str(i): list(values.values()).count(i) for i in (-1, 0, 1)}
    outlines = [((0, 0), 'EENWWS', 2), ((2, 0), 'EENWWS', 2), ((-3, 0), 'EENWWS', 2), ((0, 0), 'EENWNWSS', 3)]
    for (x, y), w, area in outlines:
        assert robot_at(w, (x, y, 0)) == (x, y, area)
        opposite = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
        reverse = ''.join((opposite[c] for c in w[::-1]))
        assert robot_at(reverse, (x, y, 0)) == (x, y, -area)
    plus = 'ENWS' * 3 + 'EENN'
    minus = 'NESW' * 7 + 'EENN'
    assert robot_at(plus) == (2, 2, 7)
    assert robot_at(minus) == (2, 2, -3)
    for z in range(-20, 21):
        loops = 'ENWS' * (z - 4) if z >= 4 else 'NESW' * (4 - z)
        assert robot_at(loops + 'EENN') == (2, 2, z)
    return {'2_distribution_among_24_words': distribution, '3_signed_areas': [[-2, 2], [-2, 2], [-2, 2], [-3, 3]], '4_memory7_witness': plus, '4_memory_minus3_witness': minus, '4_general_rule': 'repeat +/-1 unit loops, then EENN'}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check72(), "instances": robot_checks()}, indent=2))
