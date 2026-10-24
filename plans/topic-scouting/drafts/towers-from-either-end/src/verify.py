"""Answer key and checks for every row printed in the three packets.

Run: python3 verify.py   (asserts the intended properties, prints the key)
"""
from check import (margin, first_haul, result, winning_first_moves, colours,
                   plan_games, greedy_vs_best)


def key(row):
    f, s = first_haul(row)
    r, b = colours(row)
    return (f"{', '.join(map(str, row)):<24} {result(row)} {f}-{s}  "
            f"best first move(s) {winning_first_moves(row)}  red {r} blue {b}")


def unique_winning_move(row):
    """Exactly one first move wins; the other does not."""
    left = row[0] - margin(row[1:])
    right = row[-1] - margin(row[:-1])
    return (left > 0) != (right > 0)


def show(title, rows, expect=None, check=None):
    print(f"\n{title}")
    for i, r in enumerate(rows):
        print("  " + key(r))
        if expect is not None:
            assert result(r) == expect[i], (title, r, result(r), expect[i])
        if check is not None:
            assert check(r), (title, r)


def heights_ok(rows, hi):
    for r in rows:
        assert all(1 <= h <= hi for h in r), r


# ---------------------------------------------------------------- K-1
K1 = {
    "P1": [(5, 2, 1, 4), (1, 5, 2, 3), (2, 4, 3, 1)],
    "P2": [(2, 1, 5, 3), (3, 5, 1, 2), (1, 1, 5, 2), (2, 5, 1, 1), (5, 1, 3, 2), (2, 3, 1, 4)],
    "P3": [(1, 5, 1), (5, 1, 5), (1, 4, 2), (3, 4, 2), (2, 5, 2)],
    "P6": [(1, 2, 5, 2), (3, 4, 1, 2), (4, 1, 5, 2), (1, 4, 2, 3)],
    "P7": [(3, 1, 2, 5), (2, 4, 1, 1), (1, 3, 2, 1, 3, 1), (2, 1, 1, 3, 2, 2)],
    "P8": [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5)],
}
# ---------------------------------------------------------------- 2-3
G23 = {
    "P1": [(5, 2, 1, 4), (2, 6, 3, 4), (2, 4, 3, 1)],
    "P2": [(2, 1, 5, 3), (3, 6, 1, 2), (2, 3, 1, 5), (1, 4, 6, 2)],
    "P3": [(1, 5, 1), (5, 1, 5), (2, 6, 3), (3, 4, 2), (2, 5, 3), (4, 6, 1)],
    "P5": [(1, 2, 5, 1, 3, 2), (3, 1, 1, 4, 2, 2), (1, 2, 3, 1, 2, 1, 3, 2)],
    "P6": [(2, 4, 1, 1, 3, 2)],
    "P7": [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5), (2, 4, 5, 3), (3, 2, 4, 5)],
    "P8": [(2, 1, 5, 1, 2), (4, 1, 1, 1, 4), (1, 4, 2, 4, 1), (1, 2, 4, 2, 1)],
}
# ---------------------------------------------------------------- 4-5
G45 = {
    "P1": [(2, 1, 5, 3), (1, 4, 6, 2), (2, 4, 3, 1), (6, 2, 1, 5)],
    "P2": [(1, 5, 1), (5, 1, 5), (2, 6, 3), (3, 4, 2), (2, 5, 3), (6, 1, 2)],
    "P4": [(1, 2, 5, 1, 3, 2), (3, 1, 1, 4, 2, 2), (1, 2, 3, 1, 2, 1, 3, 2)],
    "P6": [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5), (2, 4, 5, 3), (3, 1, 1, 3), (4, 2, 1, 3)],
    "P7": [(1, 4, 2, 4, 1), (2, 3, 1, 5, 2), (3, 5, 2, 4, 1), (1, 3, 3, 3, 1)],
    "P8": [(4, 1, 1, 1, 4), (1, 2, 4, 2, 1), (2, 1, 5, 1, 2), (4, 2, 1, 2, 4), (4, 1, 6, 2, 3)],
    "P10": [(3, 1, 4, 1, 5), (2, 1, 2, 5, 3), (5, 2, 6, 1, 3)],
    "P11": (2, 3, 6, 2, 1, 4),
}
# Worked example of a game record (2-3 P6): plain launch row, slots in order.
EXAMPLE_ROW, EXAMPLE_GAME = (3, 1, 4, 2), (4, 3, 1, 2)


def legal_game(row, seq):
    lo, hi = 1, len(row)
    for s in seq:
        if s not in (lo, hi):
            return False
        if s == lo:
            lo += 1
        else:
            hi -= 1
    return lo > hi


def taller_end(row):
    if row[0] == row[-1]:
        return None
    return "L" if row[0] > row[-1] else "R"


if __name__ == "__main__":
    print("=== K-1 ===")
    for k, v in K1.items():
        heights_ok(v, 5)
    show("P1 play", K1["P1"])
    show("P2 one winning first move", K1["P2"], ["W"] * 6, unique_winning_move)
    show("P3 rows of three", K1["P3"], ["L", "W", "L", "W", "L"])
    show("P6 grown-up uses colour plan (colours unequal)", K1["P6"],
         check=lambda r: colours(r)[0] != colours(r)[1])
    # two of the P6 rows: the plan's first move is the shorter end
    assert sum(1 for r in K1["P6"]
               if (("L" if colours(r)[0] > colours(r)[1] else "R") != taller_end(r))) == 2
    show("P7 child goes first (colours unequal)", K1["P7"],
         check=lambda r: colours(r)[0] != colours(r)[1])
    show("P8 equal colours", K1["P8"], ["W", "T", "W"],
         check=lambda r: colours(r)[0] == colours(r)[1])
    used = [r for k in ("P1", "P2", "P3", "P7", "P8") for r in K1[k]]
    assert not set(K1["P6"]) & set(used), "P6 rows must be fresh"

    print("\n=== 2-3 ===")
    for k, v in G23.items():
        heights_ok(v, 6)
    show("P1 play", G23["P1"])
    show("P2 one winning first move", G23["P2"], ["W"] * 4, unique_winning_move)
    ends = [winning_first_moves(r)[0] == taller_end(r) for r in G23["P2"]]
    print("    winning move is the taller end:", ends)
    assert any(ends) and not all(ends)
    show("P3 rows of three", G23["P3"], ["L", "W", "L", "W", "T", "L"])
    show("P5 grown-up uses plan (colours unequal)", G23["P5"],
         check=lambda r: colours(r)[0] != colours(r)[1])
    assert legal_game(EXAMPLE_ROW, EXAMPLE_GAME)
    show("P6 plan test", G23["P6"])
    for seq, a, b in plan_games(G23["P6"][0]):
        print("    plan game, slots in order:", seq, f"planner {a}, partner {b}")
    print("    number of games:", len(plan_games(G23["P6"][0])))
    assert len(plan_games(G23["P6"][0])) == 4
    show("P7 equal colours", G23["P7"], ["W", "T", "W", "T", "W"],
         check=lambda r: colours(r)[0] == colours(r)[1])
    assert all(len(r) == 4 for r in G23["P7"]), "no row of six to copy into P9"
    show("P8 rows of five", G23["P8"], ["L", "W", "L", "T"])

    print("\n=== 4-5 ===")
    for k, v in G45.items():
        if k != "P11":
            heights_ok(v, 6)
    show("P1 rows of four", G45["P1"], ["W", "W", "T", "W"])
    show("P2 rows of three", G45["P2"], ["L", "W", "L", "W", "T", "W"])
    show("P4 plan rows", G45["P4"], check=lambda r: colours(r)[0] != colours(r)[1])
    show("P6 equal colours", G45["P6"], ["W", "T", "W", "T", "T", "W"],
         check=lambda r: colours(r)[0] == colours(r)[1])
    assert not set(G45["P6"]) & set(G45["P1"]), "P6 must not repeat P1"
    show("P7 blue > red", G45["P7"], ["L"] * 4, check=lambda r: colours(r)[1] > colours(r)[0])
    show("P8 red > blue", G45["P8"], ["W", "T", "L", "W", "L"],
         check=lambda r: colours(r)[0] > colours(r)[1])
    show("P10 rows of five", G45["P10"], ["T", "W", "L"],
         check=lambda r: len(winning_first_moves(r)) == 1)
    assert any(winning_first_moves(r)[0] != taller_end(r) for r in G45["P10"])
    print("\nP11 table: most cubes the player to move can be sure of, per run")
    row = G45["P11"]
    n = len(row)
    for k in range(n, 0, -1):
        cells = []
        for i in range(n - k + 1):
            sub = row[i:i + k]
            cells.append(f"[{','.join(map(str, sub))}]={first_haul(sub)[0]}")
        print("  " + "  ".join(cells))
    print("  colours:", colours(row), "result:", key(row))
    print("\nall checks passed")
