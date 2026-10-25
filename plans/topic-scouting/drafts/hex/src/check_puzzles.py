"""Check the specific positions printed in the packets.

Run:  python3 check_puzzles.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build import (PUZZLES, WALK_BOARDS, EXAMPLE_RED, EXAMPLE_BLUE,  # noqa: E402
                   OBSTACLE_RED, EXTRA_RED, EXTRA_BLUE)
from hexsolve import Board, show  # noqa: E402
from hexgeom import walk  # noqa: E402
from check_hex import has_chain  # noqa: E402


def main():
    # Example game in the shared rules (6 x 6): Red has won, Blue has not.
    cells = {p: 'R' for p in EXAMPLE_RED}
    cells.update({p: 'B' for p in EXAMPLE_BLUE})
    print("example: red chain", has_chain(6, cells, 'R'), "blue chain", has_chain(6, cells, 'B'),
          "red", len(EXAMPLE_RED), "blue", len(EXAMPLE_BLUE))

    # Grades 2-3, puzzles: Blue to move.  Which Blue moves win?
    b4 = Board(4)
    for i, (red, blue) in enumerate(PUZZLES, 1):
        R, B = b4.mask(red), b4.mask(blue)
        assert not b4.red_wins(R) and not b4.blue_wins(B)
        wm = b4.winning_moves(R, B, False)
        print(f"puzzle {i}: red {len(red)} blue {len(blue)}; Blue's winning moves: {wm or 'none (Red wins)'}")
        show(4, red, blue, wm)

    # Grades 4-5, boundary path boards.
    for i, rows in enumerate(WALK_BOARDS, 1):
        n = len(rows)
        cells = {(r, c): rows[r][c] for r in range(n) for c in range(n)}
        pts, end = walk(n, cells)
        print(f"walk board {i}: path from top-left corner ends at {end} after {len(pts) - 1} sides; "
              f"red chain {has_chain(n, cells, 'R')}, blue chain {has_chain(n, cells, 'B')}; "
              f"red {sum(v == 'R' for v in cells.values())}")

    # 3 x 3 openings (grades 2-3 Problem 6, grades 4-5 Problem 7).
    b3 = Board(3)
    wins = [(r, c) for r in range(3) for c in range(3) if not b3._wins(b3.mask([(r, c)]), 0, False)]
    print("3x3 winning first moves for Red:", wins)

    # Minimum blue blocking sets on 3x3, 4x4, 5x5: smallest k such that some k blue
    # cells leave Red without a chain when every other cell is red.
    import itertools
    for n in (3, 4, 5):
        allc = [(r, c) for r in range(n) for c in range(n)]
        found = None
        for k in range(1, n + 1):
            for blue in itertools.combinations(allc, k):
                cells = {p: ('B' if p in blue else 'R') for p in allc}
                if not has_chain(n, cells, 'R'):
                    found = k
                    break
            if found:
                break
        # every minimum blocking set contains a blue chain from left to right
        ok = all(
            has_chain(n, {p: ('B' if p in blue else 'R') for p in allc}, 'B')
            for blue in itertools.combinations(allc, found)
            if not has_chain(n, {p: ('B' if p in blue else 'R') for p in allc}, 'R'))
        print(f"{n}x{n}: fewest blue counters that stop Red = {found}; each such set is a blue chain: {ok}")


def fewest_blue(n, fixed_red=()):
    """Smallest number of blue counters that leave Red without a chain when
    every other hexagon (including fixed_red) is red."""
    import itertools
    allc = [(r, c) for r in range(n) for c in range(n)]
    free = [p for p in allc if p not in fixed_red]
    for k in range(1, len(free) + 1):
        sets = [blue for blue in itertools.combinations(free, k)
                if not has_chain(n, {p: ('B' if p in blue else 'R') for p in allc}, 'R')]
        if sets:
            return k, len(sets)


def extra_counter_check():
    """Grades 4-5 Problem 9: Red to move in the printed 4 x 4 position."""
    b4 = Board(4)
    R, B = b4.mask(EXTRA_RED), b4.mask(EXTRA_BLUE)
    assert len(EXTRA_RED) == len(EXTRA_BLUE)          # Red to move after Red went first
    assert not b4.red_wins(R) and not b4.blue_wins(B)
    wm = b4.winning_moves(R, B, True)
    print("4-5 extra-counter position: Red's winning moves", wm)
    show(4, EXTRA_RED, EXTRA_BLUE, wm)
    empty = [(r, c) for r in range(4) for c in range(4)
             if (r, c) not in EXTRA_RED and (r, c) not in EXTRA_BLUE]
    still = {}
    for e in empty:
        R2 = R | b4.mask([e])
        still[e] = b4.red_wins(R2) or bool(b4.winning_moves(R2, B, True))
    print("  with one extra red counter, Red (to move) still wins for every empty hexagon:",
          all(still.values()), still)
    # if it were Blue's turn instead, could Blue win?  (the position is not one-sided)
    print("  Blue to move in the printed position would win at:", b4.winning_moves(R, B, False))


def extra_main():
    print("2-3 Problem 4 (5x5 empty): fewest blue =", fewest_blue(5))
    print("2-3 Problem 5 (5x5, red at %s): fewest blue =" % (OBSTACLE_RED,), fewest_blue(5, OBSTACLE_RED))
    print("K-1 Problem 7: fewest blue 3x3 =", fewest_blue(3), " 4x4 =", fewest_blue(4))
    extra_counter_check()


if __name__ == "__main__":
    main()
    extra_main()
