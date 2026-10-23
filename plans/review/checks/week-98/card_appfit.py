"""Card-stage checks for Week 98 app notes: two-neighbour growth on a-by-b boards.
Counts filling starts of the minimum size, and the largest inclusion-minimal
filling starts (every seed needed), by exhaustive search on small boards."""
from itertools import combinations
import sys

def closure(a, b, seeds):
    filled = set(seeds)
    changed = True
    while changed:
        changed = False
        for r in range(a):
            for c in range(b):
                if (r, c) in filled:
                    continue
                k = sum((r + dr, c + dc) in filled for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
                if k >= 2:
                    filled.add((r, c)); changed = True
    return filled

def fills(a, b, seeds):
    return len(closure(a, b, seeds)) == a * b

def report(a, b, maxsize):
    cells = [(r, c) for r in range(a) for c in range(b)]
    out = {}
    for s in range(1, maxsize + 1):
        filling = [S for S in combinations(cells, s) if fills(a, b, S)]
        minimal = [S for S in filling if all(not fills(a, b, tuple(x for x in S if x != y)) for y in S)]
        out[s] = (len(filling), len(minimal))
        from math import comb
        print(f"{a}x{b} size {s}: {len(filling)} of {comb(a*b, s)} starts fill; {len(minimal)} are inclusion-minimal")
    return out

if __name__ == "__main__":
    report(3, 3, 5)
    report(4, 4, 6)
    report(5, 5, 6)
