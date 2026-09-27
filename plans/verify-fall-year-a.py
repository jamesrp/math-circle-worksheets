"""Verify the concrete mathematical instances in fall-k-5-year-a-activities.md.

Run with Python 3; no external packages or input files are required.
Finite checks complement the general arguments in the guide.
"""

from itertools import combinations, permutations, product
from math import gcd


def check_shapes():
    window = frozenset(("AB", "BC", "AD", "BE", "CF", "DE", "EF"))
    left = frozenset(("AB", "AD", "BE", "DE"))
    right = frozenset(("BC", "BE", "CF", "EF"))
    subsets = [frozenset(c) for k in range(8) for c in combinations(window, k)]
    answers = [s for s in subsets if left | s == window]
    assert len(answers) == 16
    restricted = [s for s in answers if s <= right]
    assert set(restricted) == {right, right - {"BE"}}
    assert (left | right) - right == left - {"BE"}
    for a, b in product(subsets, repeat=2):
        assert (((a | b) - b) == a) == a.isdisjoint(b)
    print("Shape operations: restoration criterion and 16/2 solution counts passed.")


def shift(message, amount):
    return "".join(
        chr((ord(c) - ord("A") + amount) % 26 + ord("A"))
        if "A" <= c <= "Z" else c
        for c in message
    )


def pattern(word):
    indices = {}
    return tuple(indices.setdefault(c, len(indices)) for c in word)


def check_ciphers():
    key = {"A": "triangle", "E": "circle", "M": "square", "R": "star", "T": "plus"}
    encoded = " / ".join(" ".join(key[c] for c in word) for word in "MEET ME AT TREE".split())
    assert encoded == "square circle circle plus / square circle / triangle plus / plus star circle circle"
    candidates = ["BERRY", "MERRY", "FERRY", "HAPPY", "ROBOT", "LEVEL"]
    possible = [w for w in candidates if pattern(w) == pattern("ABCCD")]
    assert possible == ["BERRY", "MERRY", "FERRY", "HAPPY"]
    possible = [w for w in possible if w[1] == "E"]
    assert possible == ["BERRY", "MERRY", "FERRY"]
    assert [w for w in possible if w[0] == "B"] == ["BERRY"]
    for plain, amount, cipher in [
        ("GO TO TREE", 3, "JR WR WUHH"),
        ("FIND THE RED BOX", 4, "JMRH XLI VIH FSB"),
        ("BRING THE BLUE BLOCK", 7, "IYPUN AOL ISBL ISVJR"),
    ]:
        assert shift(plain, amount) == cipher
        assert shift(cipher, -amount) == plain
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert shift(shift(alphabet, 7), 5) == shift(alphabet, 12)
    assert shift(shift(alphabet, 12), 14) == alphabet
    assert [k for k in range(26) if shift(shift(alphabet, k), k) == alphabet] == [0, 13]
    print("Ciphers: all messages, candidate filters, composition, and inverses passed.")


def latin_squares(n):
    rows = list(permutations(range(1, n + 1)))
    results = []

    def append_row(grid):
        if len(grid) == n:
            results.append(tuple(grid))
            return
        for row in rows:
            if all(all(row[c] != old[c] for old in grid) for c in range(n)):
                append_row(grid + [row])

    append_row([])
    return results


def visible(row):
    count = highest = 0
    for height in row:
        if height > highest:
            count += 1
            highest = height
    return count


def sight_lines(grid):
    columns = list(zip(*grid))
    return {
        **{("T", i): visible(col) for i, col in enumerate(columns)},
        **{("B", i): visible(col[::-1]) for i, col in enumerate(columns)},
        **{("L", i): visible(row) for i, row in enumerate(grid)},
        **{("R", i): visible(row[::-1]) for i, row in enumerate(grid)},
    }


def check_towers():
    squares = {n: latin_squares(n) for n in (2, 3, 4)}
    assert {n: len(gs) for n, gs in squares.items()} == {2: 2, 3: 12, 4: 576}
    lines = {n: [(g, sight_lines(g)) for g in gs] for n, gs in squares.items()}
    # Zero-based row/column indices, unlike the prose's one-based labels.
    s4 = {("L", 2): 2, ("L", 3): 1, ("R", 1): 2, ("R", 2): 2, ("R", 3): 2}
    s3 = {**s4, ("T", 0): 4, ("L", 0): 4}
    s5 = {k: v for k, v in s4.items() if k != ("L", 2)}
    target4 = ((1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3))
    alternate4 = (target4[0], target4[2], target4[1], target4[3])

    def solutions(n, clues):
        return {g for g, values in lines[n] if all(values[k] == v for k, v in clues.items())}

    puzzles = [
        ("S0", 2, {("L", 0): 2}, {((1, 2), (2, 1))}),
        ("S1", 3, {("T", 0): 3, ("R", 1): 2}, {((1, 2, 3), (2, 3, 1), (3, 1, 2))}),
        ("S2", 3, {("L", 2): 1, ("R", 1): 1, ("R", 2): 2}, {((2, 3, 1), (1, 2, 3), (3, 1, 2))}),
        ("S3", 4, s3, {target4}),
        ("S4", 4, s4, {target4}),
        ("S5", 4, s5, {target4, alternate4}),
    ]
    for name, n, clues, expected in puzzles:
        assert solutions(n, clues) == expected, name
    for removed in s4:
        assert len(solutions(4, {k: v for k, v in s4.items() if k != removed})) > 1
    print("Towers: S0-S4 unique; S5 exactly two; each S4 clue necessary.")


def score(guess, secret):
    return sum(a == b for a, b in zip(guess, secret))


def check_color_codes():
    histories = [
        (2, [("RR", 1), ("BR", 0)], "RB"),
        (3, [("RRR", 1), ("BRR", 0), ("RBR", 2)], "RBB"),
        (4, [("RRRR", 2), ("BRRR", 3), ("RBRR", 1), ("RRBR", 1)], "BRRB"),
    ]
    for n, history, expected in histories:
        possibles = ["".join(s) for s in product("RB", repeat=n)
                     if all(score(g, s) == result for g, result in history)]
        assert possibles == [expected]
    checked = 0
    for n in range(2, 6):
        for secret in product("RB", repeat=n):
            baseline = score("R" * n, secret)
            recovered = []
            for i in range(n - 1):
                guess = "R" * i + "B" + "R" * (n - i - 1)
                delta = score(guess, secret) - baseline
                assert delta in (-1, 1)
                recovered.append("B" if delta == 1 else "R")
            remaining_reds = baseline - recovered.count("R")
            assert remaining_reds in (0, 1)
            recovered.append("R" if remaining_reds else "B")
            assert tuple(recovered) == secret
            checked += 1
    print(f"Color codes: three histories unique; baseline method passed all {checked} secrets of lengths 2-5.")


def take_away(moves, limit=140):
    winning = [False]
    for n in range(1, limit + 1):
        winning.append(any(not winning[n - move] for move in moves if move <= n))
    return winning


def check_games():
    for moves, losing_rule in [
        ((1, 2), lambda n: n % 3 == 0),
        ((1, 3, 4), lambda n: n % 7 in (0, 2)),
        ((1, 3, 5), lambda n: n % 2 == 0),
    ]:
        assert all(win == (not losing_rule(n)) for n, win in enumerate(take_away(moves)))
    w = take_away((1, 3, 4))
    assert [m for m in (1, 3, 4) if not w[8 - m]] == [1]
    assert [m for m in (1, 3, 4) if not w[10 - m]] == [1, 3]
    # Coordinates below are remaining horizontal and vertical distances.
    for piece in ("rook", "king"):
        winning = {}
        for x in range(13):
            for y in range(13):
                if piece == "rook":
                    destinations = [(i, y) for i in range(x)] + [(x, j) for j in range(y)]
                    expected_losing = x == y
                else:
                    destinations = [(x - dx, y - dy) for dx, dy in ((1, 0), (0, 1), (1, 1))
                                    if x >= dx and y >= dy]
                    expected_losing = x % 2 == 0 and y % 2 == 0
                winning[x, y] = any(not winning[p] for p in destinations)
                assert winning[x, y] == (not expected_losing), (piece, x, y)
    print("Games: take-away positions 0-140 and rook/king distances 0-12 passed.")


def trace_billiards(width, height):
    x = y = 0
    dx = dy = 1
    vertices = [(0, 0)]
    for _ in range(width * height + 1):
        x += dx
        y += dy
        assert 0 <= x <= width and 0 <= y <= height
        if x in (0, width) or y in (0, height):
            vertices.append((x, y))
        if x in (0, width) and y in (0, height):
            return vertices
        if x in (0, width):
            dx = -dx
        if y in (0, height):
            dy = -dy
    raise AssertionError("No corner reached")


def check_billiards():
    def corner(w, h):
        x, y = trace_billiards(w, h)[-1]
        return ("T" if y == h else "B") + ("R" if x == w else "L")

    for w in range(1, 28):
        for h in range(1, 28):
            a, b = w // gcd(w, h), h // gcd(w, h)
            expected = ("T" if a % 2 else "B") + ("R" if b % 2 else "L")
            assert corner(w, h) == expected
            assert expected != "BL"
            assert corner(2 * w, 2 * h) == expected
    for w, h, endpoint in [
        (3, 3, "TR"), (3, 6, "TL"), (6, 3, "BR"), (3, 9, "TR"),
        (6, 9, "BR"), (9, 6, "TL"), (6, 10, "TR"),
        (6, 12, "TL"), (9, 18, "TL"), (12, 6, "BR"), (18, 9, "BR"),
        (6, 18, "TR"), (9, 27, "TR"),
    ]:
        assert corner(w, h) == endpoint
    assert trace_billiards(3, 6) == [(0, 0), (3, 3), (0, 6)]
    assert trace_billiards(6, 3) == [(0, 0), (3, 3), (6, 0)]
    assert trace_billiards(6, 9) == [(0, 0), (6, 6), (3, 9), (0, 6), (6, 0)]
    assert len(trace_billiards(3, 9)) - 2 == 2
    print("Billiards: specified paths, endpoints, scaling, and all sizes 1-27 passed.")


if __name__ == "__main__":
    check_shapes()
    check_ciphers()
    check_towers()
    check_color_codes()
    check_games()
    check_billiards()
    print("All activity-instance checks passed.")
