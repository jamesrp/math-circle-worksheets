#!/usr/bin/env python3
"""Checks carried over from the old student builder (make.py, archived in the
repository's source/week-49/archive-before-problem-files-2026-10-23/). checks.txt,
which make.py wrote, records what they establish."""
from itertools import product


def D(s):
    return tuple(abs(s[i]-s[(i+1) % len(s)]) for i in range(len(s)))


def rounds(s):
    seen = set(); n = 0
    while any(s) and s not in seen:
        seen.add(s); s = D(s); n += 1
    return n, not any(s)


assert D((1, 4, 2, 0)) == (3, 2, 2, 1)
assert rounds((0, 1, 2, 4)) == (7, True)
assert all(rounds(s)[1] for s in product(range(6), repeat=4))
assert not rounds((1, 0, 0))[1]
for s in product(range(2), repeat=4):
    for _ in range(4):
        s = D(s)
    assert all(x % 2 == 0 for x in s)
print('PASS student checks: all 1296 starts in 0..5 terminate; (0,1,2,4) needs 7 moves; three-station (1,0,0) '
      'repeats; all 16 parity patterns are even after four rounds.')

# Added with the review card's fixes, October 23, 2026: every changed claim, key and count.
from itertools import permutations


def run(s):
    out = [tuple(s)]
    while any(out[-1]):
        out.append(D(out[-1]))
    return out


orders = {p: rounds(p)[0] for p in permutations((0, 1, 2, 4))}
assert sorted(orders.values()).count(7) == 8 and sorted(orders.values()).count(4) == 16
assert orders[(0, 2, 1, 4)] == 4 and orders[(0, 1, 4, 2)] == 4 and orders[(0, 1, 2, 4)] == 7
assert run((0, 2, 1, 4)) == [(0, 2, 1, 4), (2, 1, 3, 4), (1, 2, 1, 2), (1, 1, 1, 1), (0, 0, 0, 0)]
print('PASS orders: of the 24 orders of 0, 1, 2, 4, eight last 7 moves and sixteen 4; the printed (0,2,1,4) and '
      '(0,1,4,2) both last 4, so the pages no longer show a longest order.')

a, b = run((2, 5, 1, 0)), run((4, 10, 2, 0))
assert len(a) - 1 == 6 == len(b) - 1 and all(tuple(2*x for x in s) == t for s, t in zip(a, b))
assert a == [(2, 5, 1, 0), (3, 4, 1, 2), (1, 3, 1, 1), (2, 2, 0, 0), (0, 2, 0, 2), (2, 2, 2, 2), (0, 0, 0, 0)]
assert len(run((6, 15, 3, 0))) - 1 == 6
assert (1, 4, 2, 0) not in a and (1, 4, 2, 0) not in b   # no longer the page-1 example
print('PASS 4-5 scaling: (2,5,1,0) and (4,10,2,0) take 6 moves each, every state of the second is double the '
      'first, and tripling also takes 6.')

# Cubes: 40 per pair holds an old and a new ring on the mats for every start used.
starts = [s for s in product(range(6), repeat=4)]
assert max(sum(s) + sum(D(s)) for s in starts) <= 40
for s in [(2, 5, 1, 0), (4, 10, 2, 0), (1, 0, 0, 0)]:
    r = run(s)
    assert max(sum(x) + sum(y) for x, y in zip(r, r[1:])) <= 40
assert max(sum(x) + sum(y) for x, y in zip(b, b[1:])) == 36
print('PASS cubes: every start from 0 to 5 and the 4-5 doubled run fit 40 cubes for an old and a new ring at once '
      '(at most 36 for (4,10,2,0)); no number cards are needed.')

# The three-station run needs a repeat within six recorded moves.
r3 = [(1, 0, 0)]
for _ in range(6):
    r3.append(D(r3[-1]))
first_repeat = next(i for i in range(1, 7) if r3[i] in r3[1:i])
assert r3[1:5] == [(1, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)] and first_repeat == 4
print('PASS three stations: (1,0,0) gives (1,0,1), (1,1,0), (0,1,1) and (1,0,1) again at move 4, within the six '
      'numbered record rows; (1,0,0,0) reaches zero in', rounds((1, 0, 0, 0))[0], 'moves.')
assert rounds((1, 0, 0, 0)) == (4, True)

# Predecessors (older Problem 3): complete search, since 2(max - min) <= sum of the gaps.
def preds(t, top=8):
    return [s for s in product(range(top + 1), repeat=4) if min(s) == 0 and D(s) == t]


assert preds((2, 0, 2, 0)) and preds((1, 1, 1, 1)) and not preds((1, 1, 1, 0)) and not preds((0, 0, 0, 2))
assert all(sum(D(s)) % 2 == 0 for s in product(range(6), repeat=4))
print('PASS predecessors: (2,0,2,0) and (1,1,1,1) have old rings, (1,1,1,0) (odd total) and (0,0,0,2) (three zero '
      'gaps) do not.')

# One-move and two-move starts (K-1 Problems 3-4), with the all-zero start taking 0 moves.
one = [s for s in product(range(6), repeat=4) if rounds(s) == (1, True)]
assert one == [(c,) * 4 for c in range(1, 6)] and rounds((0, 0, 0, 0)) == (0, True)
assert rounds((0, 1, 0, 1)) == (2, True) and rounds((0, 1, 2, 1)) == (2, True)
print('PASS K-1: exactly the positive constant rings become all zeros in one move; the all-zero start takes 0 moves.')

# The tallest height can stay (guide example) and never grows.
assert D((0, 1, 2, 4)) == (1, 1, 2, 4)
assert all(max(D(s)) <= max(s) for s in product(range(9), repeat=4))
print('PASS bound: no new height exceeds the old maximum, and (0,1,2,4) -> (1,1,2,4) keeps it at 4.')
