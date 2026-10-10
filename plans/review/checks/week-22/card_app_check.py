# Card-stage check for the app-fit paragraph: with A, B, C fixed and
# noncollinear, how many splits can a placed D make work?
# Run with: python3 -I card_app_check.py  (from the run folder)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from geom import successes
from collections import Counter

A, B, C = (F(2), F(2)), (F(10), F(3)), (F(4), F(10))   # K-1 P1/P4 board
counts = Counter()
where = {}
for xi in range(0, 127):
    for yi in range(0, 127):
        D = (F(xi, 10), F(yi, 10))
        n = len(successes({'A': A, 'B': B, 'C': C, 'D': D}))
        counts[n] += 1
        where.setdefault(n, D)
print("successes with A, B, C fixed and D on a 0.1 cm lattice:", dict(sorted(counts.items())))
print("example D for each count:", {k: (str(v[0]), str(v[1])) for k, v in sorted(where.items())})
