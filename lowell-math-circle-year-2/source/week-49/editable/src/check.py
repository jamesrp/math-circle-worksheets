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
