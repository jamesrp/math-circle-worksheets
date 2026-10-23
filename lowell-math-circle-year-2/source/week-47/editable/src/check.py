#!/usr/bin/env python3
"""Checks carried over from the old student builder (make.py, archived in the
repository's source/week-47/archive-before-problem-files-2026-10-23/): an independent
enumeration of the seven-site instance of Problem 5. It writes checks.txt, as make.py did."""
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sol = [s for s in product(range(6), repeat=7) if s[0] == 1 and s[4] == 3 and s[6] == 1 and all(abs(a-b) <= 1 for a, b in zip(s, s[1:]))]
assert len(sol) == 10
assert tuple(min(s[i] for s in sol) for i in range(7)) == (1, 0, 1, 2, 3, 2, 1)
assert tuple(max(s[i] for s in sol) for i in range(7)) == (1, 2, 3, 4, 3, 2, 1)
(ROOT/'checks.txt').write_text('Seven-site instance: 10 completions; coordinatewise minima and maxima verified.\n')
print('PASS student checks (seven-site instance: 10 completions, minima 1,0,1,2,3,2,1, maxima 1,2,3,4,3,2,1).')
