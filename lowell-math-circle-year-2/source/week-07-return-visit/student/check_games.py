"""Exact finite-state checks for the three student investigations."""
from functools import cache
import json


@cache
def pass_moves(n, available):
    if n == 0:
        return ()
    moves = []
    for k in (1, 2):
        if k <= n and not pass_win(n-k, available):
            moves.append(str(k))
    if available and not pass_win(n, False):
        moves.append("PASS")
    return tuple(moves)


@cache
def pass_win(n, available):
    return bool(pass_moves(n, available))


@cache
def last_moves(n, last):
    return tuple(k for k in (1, 2, 3)
                 if k <= n and k != last and not last_win(n-k, k))


@cache
def last_win(n, last):
    return bool(last_moves(n, last))


def canonical(runs):
    # Isolated counters can never participate in a legal move.
    return tuple(sorted(n for n in runs if n >= 2))


def pair_options(runs):
    for row, n in enumerate(runs):
        for left in range(n-1):
            right = n-left-2
            after = canonical(runs[:row] + runs[row+1:] + (left, right))
            yield row, left+1, after


@cache
def pair_win(runs):
    return any(not pair_win(after) for _, _, after in pair_options(runs))


def pair_moves(runs):
    return [(row+1, start, after) for row, start, after in pair_options(runs)
            if not pair_win(after)]


assert [n for n in range(1, 13) if not pass_win(n, False)] == [3, 6, 9, 12]
assert [n for n in range(1, 13) if not pass_win(n, True)] == [4, 7, 10]
for n in range(1, 101):
    assert (not pass_win(n, False)) == (n % 3 == 0)
    assert (not pass_win(n, True)) == (n >= 4 and n % 3 == 1)
    for last, losing_residues in [(0, {0}), (1, {0, 1}), (2, {0}), (3, {0, 3})]:
        assert (not last_win(n, last)) == (n % 4 in losing_residues)
assert [n for n in range(1, 13) if not pair_win(canonical((n,)))] == [1, 5, 9]
for n in range(1, 13):
    assert not pair_win(canonical((n, n)))
for n in range(2, 13, 2):
    assert pair_win((n,))

cases = {"A": (4,), "B": (2, 2), "C": (5,), "D": (3,), "E": (6,), "F": (9,)}
report = {
    "pass": [{"pile": n, "available": pass_win(n, True),
              "available_winning_moves": pass_moves(n, True),
              "used": pass_win(n, False),
              "used_winning_moves": pass_moves(n, False)} for n in range(1, 13)],
    "last": {str(last): [{"pile": n, "winning": last_win(n, last),
                          "winning_moves": last_moves(n, last)} for n in range(1, 9)]
             for last in range(4)},
    "pairs": {name: {"rows": runs, "winning": pair_win(canonical(runs)),
                     "winning_moves_row_and_left_square": pair_moves(canonical(runs))}
              for name, runs in cases.items()}
}
print(json.dumps(report, indent=2))
