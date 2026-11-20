"""Reviewer's extra checks behind specific findings (not answers printed in the guide).

1. Problem 2, middle-row board: how many counters each empty square touches along
   a side and at a corner (the guide says "several counters diagonally").
2. A possible non-task removal demonstration for the return visit: the launch
   2x3 start plus a seed at (1,3) fills; taking (1,3) off returns to the launch
   start, stuck at four.
3. Seed-counter cap: smallest number of seeds a child could not place with six
   seed-colour counters, versus the board sizes in Problems 3-5.
4. The strip minimum from the guide's own two facts (ends seeded, no two
   adjacent empty squares): s seeds cover at most 2s - 1 squares.
5. Finishes under the 'exactly two' misreading for Problem 8, Problem 9 and the
   guide's Problem 7 examples.
6. The 14 three-seed filling starts on 3x3, grouped by turning and flipping.

Usage: python3 -I check_extras.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_answers import closure, fills, nbrs  # noqa: E402


def main():
    # 1
    R = C = 3
    row = {(2, 1), (2, 2), (2, 3)}
    for r in range(1, 4):
        for c in range(1, 4):
            if (r, c) in row:
                continue
            side = sum(n in row for n in nbrs(r, c, R, C))
            diag = sum((r + dr, c + dc) in row for dr in (-1, 1) for dc in (-1, 1))
            print(f"P2 middle row: empty ({r},{c}) side={side} corner={diag}")

    # 2
    launch = {(1, 1), (2, 1), (2, 2)}
    four = launch | {(1, 3)}
    print("demo: launch+(1,3) fills 2x3:", fills(four, 2, 3))
    print("demo: remove (1,3) ->", len(closure(four - {(1, 3)}, 2, 3)), "of 6 (the launch finish)")

    # 3
    print("six seed counters: max trial size 6; boards 3x3, 4x4, 5x5 minima 3, 4, 5")

    # 4
    for L in (3, 4, 5, 6):
        s = next(s for s in range(1, L + 1) if 2 * s - 1 >= L)
        print(f"strip 1x{L}: smallest s with 2s-1 >= L is {s}")



def exact_two_finishes(seeds, R, C):
    """All finishes over all orders under the 'exactly two' misreading."""
    seen, fins = set(), set()
    stack = [frozenset(seeds)]
    while stack:
        s = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        moves = [(r, c) for r in range(1, R + 1) for c in range(1, C + 1)
                 if (r, c) not in s and sum(n in s for n in nbrs(r, c, R, C)) == 2]
        if not moves:
            fins.add(len(s))
        for m in moves:
            stack.append(s | {m})
    return sorted(fins)


def misreading():
    print("5. 'exactly two' misreading, finish sizes over all orders:")
    for name, seeds in [("P8 2x2 L", {(1, 1), (1, 2), (2, 1)}),
                        ("P8 four corners", {(1, 1), (1, 3), (3, 1), (3, 3)}),
                        ("P8 three corners + centre", {(1, 1), (1, 3), (2, 2), (3, 1)}),
                        ("P8 middle of each side", {(1, 2), (2, 1), (2, 3), (3, 2)}),
                        ("P9 top row + left column", {(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)})]:
        R = C = 2 if "2x2" in name else 3
        print(f"    {name}: {exact_two_finishes(seeds, R, C)} of {R*C}")
    for name, R, seeds in [("guide P7 3x2 example", 3, {(1, 1), (2, 2), (3, 1)}),
                           ("guide P7 4x2 example", 4, {(1, 1), (2, 2), (4, 1)}),
                           ("guide P7 5x2 example", 5, {(1, 1), (2, 2), (4, 1), (5, 2)})]:
        print(f"    {name}: {exact_two_finishes(seeds, R, 2)} of {R*2}")



def three_by_three_fillers():
    """Group the 3x3 three-seed filling starts by turning and flipping."""
    import itertools
    cells = [(r, c) for r in range(1, 4) for c in range(1, 4)]
    def syms(s):
        out = []
        for k in range(4):
            t = set(s)
            for _ in range(k):
                t = {(c, 4 - r) for r, c in t}
            out.append(frozenset(t))
            out.append(frozenset((r, 4 - c) for r, c in t))
        return out
    groups = {}
    for s in itertools.combinations(cells, 3):
        if fills(set(s), 3, 3):
            key = min(tuple(sorted(x)) for x in syms(s))
            groups.setdefault(key, set()).add(frozenset(s))
    print("6. 3x3 three-seed filling starts:", sum(len(v) for v in groups.values()))
    for k, v in sorted(groups.items()):
        print(f"    family {k}: {len(v)} placements")


if __name__ == "__main__":
    main()
    misreading()
    three_by_three_fillers()
