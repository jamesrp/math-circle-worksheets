"""Checks behind facts the week-97 card states that math.md does not cover."""
from itertools import combinations

def out(n, m):
    # remove complete bundles of m from n*n counters
    c = n * n
    while c >= m:
        c -= m
    return c

# K-1 route: squares 1..5 in groups of 3 and of 4
print("groups of 3:", [out(n, 3) for n in range(1, 6)])
print("groups of 4:", [out(n, 4) for n in range(1, 6)])

# L-shape: 5x5 minus 2x2 corner is a 3x7 rectangle
assert 5 * 5 - 2 * 2 == (5 - 2) * (5 + 2) == 3 * 7
print("5x5 - 2x2 = 21 = 3 x 7")

# p.1 bundles-of-4 table: output 0 hides 0 and 2
print("bundles of 4, inputs 0-3:", {r: [x for x in range(4) if out(x, 4) == r] for r in (0, 1)})

# App idea: bundle sizes from 2..12 whose square leftovers tell sides 0..15 apart
for k in (1, 2):
    sols = [ms for ms in combinations(range(2, 13), k)
            if len({tuple(out(x, m) for m in ms) for x in range(16)}) == 16]
    print(k, "size(s):", sols)
