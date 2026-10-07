"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def shortest_words(neighbors, depth=13):
    start = (0, 0)
    words = {start: ''}
    q = deque([start])
    while q:
        s = q.popleft()
        w = words[s]
        if len(w) == depth:
            continue
        for move, n in neighbors(s):
            if n not in words:
                words[n] = w + move
                q.append(n)
    return words

def elevator_checks():

    def neighbors(s, left=True):
        x, h = s
        return [('R', (x + 2 ** h, h)), ('U', (x, h + 1))] + ([('D', (x, h - 1))] if h else []) + ([('L', (x - 2 ** h, h))] if left else [])
    allwords = shortest_words(neighbors)
    rightwords = shortest_words(lambda s: neighbors(s, False))
    expected = {3: 3, 7: 6, 9: 7, 15: 9, 16: 8, 17: 9, 23: 10}
    result = {}
    for x, d in expected.items():
        assert len(allwords[x, 0]) == d
        result[str(x)] = {'moves': d, 'witness': allwords[x, 0], 'no_left_moves': len(rightwords[x, 0]), 'no_left_witness': rightwords[x, 0]}
    assert len(rightwords[23, 0]) == 11
    maxima = {str(b): max((x for (x, h), w in allwords.items() if h == 0 and len(w) <= b)) for b in range(4, 9)}
    assert list(maxima.values()) == [4, 6, 8, 12, 16]
    return {'destinations': result, 'budget_maxima': maxima}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check74(), "instances": elevator_checks()}, indent=2))
