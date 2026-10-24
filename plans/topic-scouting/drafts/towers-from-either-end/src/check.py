"""Game analysis for 'Towers from either end'.

Two players alternately remove one whole tower from either end of a row.
Whoever collects more cubes wins; equal hauls tie.
"""
from functools import lru_cache
from itertools import product


@lru_cache(maxsize=None)
def margin(row):
    """Best (own - other) for the player to move on this row."""
    if not row:
        return 0
    if len(row) == 1:
        return row[0]
    return max(row[0] - margin(row[1:]), row[-1] - margin(row[:-1]))


def best(row):
    """Most cubes the player to move can be sure of collecting."""
    return (sum(row) + margin(row)) // 2


def first_haul(row):
    t = sum(row)
    m = margin(row)
    return ((t + m) // 2, (t - m) // 2)


def result(row):
    m = margin(row)
    return "W" if m > 0 else ("T" if m == 0 else "L")


def winning_first_moves(row):
    """Moves ('L' or 'R') that achieve the best margin for the mover."""
    m = margin(row)
    out = []
    if row[0] - margin(row[1:]) == m:
        out.append("L")
    if len(row) > 1 and row[-1] - margin(row[:-1]) == m:
        out.append("R")
    return out


def colours(row):
    red = sum(row[0::2])   # slots 1, 3, 5, ...
    blue = sum(row[1::2])  # slots 2, 4, 6, ...
    return red, blue


def greedy_vs_best(row):
    """First player takes the taller end each time (left on ties);
    second plays best. Returns first player's margin."""
    @lru_cache(maxsize=None)
    def g(r, greedy_turn):
        if not r:
            return 0
        if greedy_turn:
            if r[0] >= r[-1]:
                return r[0] + g(r[1:], False)
            return r[-1] + g(r[:-1], False)
        # best-playing opponent minimises greedy player's margin
        return min(-r[0] + g(r[1:], True), -r[-1] + g(r[:-1], True))
    return g(tuple(row), True)


def plan_games(row):
    """First player uses colour plan (take ends in the slot class of the
    colour with more cubes; red if equal). Enumerate every opponent reply.
    Returns list of (move sequence of slot numbers, planner haul, other haul)."""
    n = len(row)
    assert n % 2 == 0
    red, blue = colours(row)
    want = 0 if red >= blue else 1  # parity class (0-based index parity)
    games = []

    def rec(lo, hi, turn, seq, a, b):
        if lo > hi:
            games.append((seq, a, b))
            return
        if turn == 0:
            choices = [i for i in (lo, hi) if i % 2 == want]
            assert len(choices) >= 1, (row, lo, hi)
            i = choices[0]
            nlo, nhi = (lo + 1, hi) if i == lo else (lo, hi - 1)
            rec(nlo, nhi, 1, seq + [i + 1], a + row[i], b)
        else:
            for i in sorted(set((lo, hi))):
                nlo, nhi = (lo + 1, hi) if i == lo else (lo, hi - 1)
                rec(nlo, nhi, 0, seq + [i + 1], a, b + row[i])

    rec(0, n - 1, 0, [], 0, 0)
    return games


def lines(row):
    """All complete games (sequence of slot numbers taken)."""
    out = []

    def rec(lo, hi, seq):
        if lo > hi:
            out.append(seq)
            return
        rec(lo + 1, hi, seq + [lo + 1])
        if hi != lo:
            rec(lo, hi - 1, seq + [hi + 1])
    rec(0, len(row) - 1, [])
    return out


def describe(row):
    row = tuple(row)
    f, s = first_haul(row)
    r, b = colours(row)
    return (f"{row}: total {sum(row)}, best play {f}-{s} ({result(row)}), "
            f"margin {margin(row)}, first moves {winning_first_moves(row)}, "
            f"red {r} blue {b}, greedy margin {greedy_vs_best(row)}")


if __name__ == "__main__":
    # Outline claims
    # 1. even rows never a loss (2,4,6 towers, heights 1..4)
    for n in (2, 4, 6):
        bad = [r for r in product(range(1, 5), repeat=n) if margin(r) < 0]
        assert not bad
        # colour plan guarantees max(red, blue) against every reply
        for r in product(range(1, 5), repeat=n):
            red, blue = colours(r)
            for seq, a, b in plan_games(r):
                assert a == max(red, blue), (r, seq, a)
    print("even rows 2,4,6 heights 1-4: never lose; plan collects its colour")
    for n in (2, 4, 6, 8):
        bad = [r for r in product(range(1, 7), repeat=n) if margin(r) < 0] if n <= 6 else []
        assert not bad
    print("even rows 2,4,6 heights 1-6: never lose")
    print(describe((2, 1, 2, 3)))
    print(describe((1, 5, 1)), describe((5, 1, 5)))
    rows5 = list(product(range(1, 5), repeat=5))
    L = sum(1 for r in rows5 if margin(r) < 0)
    T = sum(1 for r in rows5 if margin(r) == 0)
    print("rows of five heights 1-4:", len(rows5), "losses", L, "ties", T)
    # Odd rows: blue > red implies loss; blue == red implies not a win
    for n in (1, 3, 5, 7):
        for r in product(range(1, 7), repeat=n) if n <= 5 else product(range(1, 4), repeat=n):
            red, blue = colours(r)
            if blue > red:
                assert margin(r) < 0, r
            if blue == red:
                assert margin(r) <= 0, r
    print("odd rows: blue>red => first loses; blue==red => first does not win (checked)")
    # Rows of three: exact rule
    for r in product(range(1, 7), repeat=3):
        a, b, c = r
        assert (margin(r) < 0) == (b > a + c)
        assert (margin(r) == 0) == (b == a + c)
    print("rows of three: lose iff middle > ends, tie iff equal")
    # Rows of five: how many losses have red >= blue?
    rows5_6 = list(product(range(1, 7), repeat=5))
    loss = [r for r in rows5_6 if margin(r) < 0]
    loss_rb = [r for r in loss if colours(r)[0] >= colours(r)[1]]
    print("rows of five heights 1-6: losses", len(loss), "of which red>=blue", len(loss_rb))
    print("examples:", loss_rb[:10])
    worst = min(rows5_6, key=margin)
    print("worst row of five (1-6):", describe(worst))
