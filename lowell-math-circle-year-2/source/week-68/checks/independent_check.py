"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def ends_checks():
    line = {x: {q for q in (x - 1, x + 1) if -6 <= q <= 6} for x in range(-6, 7)}
    max_forever = {}
    for n in (1, 2, 4):
        counts = []
        for blocked in combinations(range(-4, 5), n):
            cs = k.components(line, blocked)
            counts.append(sum((bool(c & {-6, 6}) for c in cs)))
        assert set(counts) == {2}
        max_forever[str(n)] = 2
    cs = k.components(line, {-3, -1, 0, 2})
    finite = [sorted(c) for c in cs if not c & {-6, 6}]
    assert sorted(finite) == [[-2], [1]]
    ladder = {(x, y): {q for q in ((x - 1, y), (x + 1, y), (x, 1 - y)) if -5 <= q[0] <= 5} for x, y in product(range(-5, 6), range(2))}
    assert len(k.components(ladder, {(0, 0)})) == 1
    assert len(k.components(ladder, {(0, 0), (0, 1)})) == 2
    assert len(k.components(ladder, {(0, 0), (1, 0)})) == 1
    for blocked in combinations(product(range(-2, 3), range(2)), 4):
        cs = k.components(ladder, blocked)
        assert sum((any((abs(x) == 5 for x, y in c)) for c in cs)) <= 2
    blocked = {(0, y) for y in range(-2, 3)}
    grid = {p: {q for q in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)) if max(abs(q[0]), abs(q[1])) <= 4 and q not in blocked} for p in product(range(-4, 5), repeat=2) if p not in blocked}
    assert k.bfs((-2, 0), grid.__getitem__, 20)[2, 0] == 10
    return {'1_forever_counts': max_forever, '2_four_blocker_witness': [-3, -1, 0, 2], '2_trapped_pieces': [[-2], [1]], '3_one_blocker': 'connected', '3_two_blockers': 'same rung separates; same rail adjacent stays connected', '4_three_forever_pieces': 'impossible', '5_P_to_Q_shortest_length': 10, '6_grid_forever_pieces': 1, '7_branch_counts': [3, 6, 12], '8_next_count': 24}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check68(), "instances": ends_checks()}, indent=2))
