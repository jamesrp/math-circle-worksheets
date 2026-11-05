# Checks the opener puzzles in round-table.tex: each must have exactly one answer, and every clue
# must be needed. "without X: n" shows how many answers remain if clue X is dropped (n > 1 means
# the clue is needed). Seats are numbered clockwise from the star seat: 0 is the star seat, then
# 1, 2, ... going the way the arrow points. "X sat 2 seats clockwise from Y" means X's seat is Y's
# seat plus 2, going round past the star seat (counting the next seat as one).
# It also checks the numbers the stars and wheels room plan uses: the note passes acted out on the
# chairs, the yarn-star finale table, and the early-finisher answers. Run: python3 round-table_check.py
from itertools import permutations
from math import gcd


def answers(names, n, clues):
    out = []
    for p in permutations(range(n)):
        s = dict(zip(names, p))
        if all(c(s) for _, c in clues):
            out.append(s)
    return out


def run(names, n, clues, label):
    sols = answers(names, n, clues)
    print(f"{label}: {len(sols)} answer(s)")
    for s in sols:
        print("    star seat, then clockwise:", ", ".join(sorted(s, key=s.get)))
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        print(f"    without '{text}': {len(answers(names, n, rest))}")
    needed = all(len(answers(names, n, clues[:i] + clues[i + 1:])) > 1 for i in range(len(clues)))
    return len(sols), needed


def cw(n, x, y, k):  # x sat k seats clockwise from y
    return lambda s: s[x] == (s[y] + k) % n


def nextto(n, x, y):
    return lambda s: (s[x] - s[y]) % n in (1, n - 1)


def note(s, n, start_seat, hop):
    """Seats the note visits, passed `hop` seats clockwise each time, until it is back."""
    seat, seen = start_seat, []
    while True:
        seen.append(seat)
        seat = (seat + hop) % n
        if seat == start_seat:
            return [a for q in seen for a in s if s[a] == q]


FIVE = ["Bear", "Fox", "Owl", "Rabbit", "Turtle"]
main = [
    ("Rabbit sat in the star seat.", lambda s: s["Rabbit"] == 0),
    ("Fox sat 2 seats clockwise from Owl.", cw(5, "Fox", "Owl", 2)),
    ("Bear sat 2 seats clockwise from Fox.", cw(5, "Bear", "Fox", 2)),
    ("Owl sat right next to Turtle.", nextto(5, "Owl", "Turtle")),
]
FOUR = ["Bear", "Fox", "Owl", "Turtle"]
easy = [
    ("Turtle sat in the star seat.", lambda s: s["Turtle"] == 0),
    ("Owl sat across the table from Turtle.", cw(4, "Owl", "Turtle", 2)),
    ("Fox sat 1 seat clockwise from Turtle.", cw(4, "Fox", "Turtle", 1)),
]
SIX = ["Bear", "Fox", "Owl", "Rabbit", "Turtle", "Mouse"]
hard = [
    ("Mouse sat in the star seat.", lambda s: s["Mouse"] == 0),
    ("Fox sat 2 seats clockwise from Owl.", cw(6, "Fox", "Owl", 2)),
    ("Bear sat 2 seats clockwise from Fox.", cw(6, "Bear", "Fox", 2)),
    ("Owl sat right next to the star seat.", lambda s: s["Owl"] in (1, 5)),
    ("Bear sat across the table from Rabbit.", cw(6, "Bear", "Rabbit", 3)),
]
# early finisher on the main sheet: cross out clue 4, then one new clue restores exactly one answer
finisher = main[:3] + [("Bear sat right next to Rabbit.", nextto(5, "Bear", "Rabbit"))]

results = [
    run(FIVE, 5, main, "main (5 seats)"),
    run(FOUR, 4, easy, "easier (4 seats)"),
    run(SIX, 6, hard, "harder (6 seats)"),
    run(FIVE, 5, finisher, "early-finisher fix"),
]
assert all(r == (1, True) for r in results), results

no4 = answers(FIVE, 5, main[:3])
print("main without clue 4:", len(no4), "answers:",
      ["/".join(sorted(s, key=s.get)) for s in no4])
assert len(no4) == 2

(m,), (e,), (h,) = answers(FIVE, 5, main), answers(FOUR, 4, easy), answers(SIX, 6, hard)
by_seat = lambda s: sorted(s, key=s.get)
assert by_seat(m) == ["Rabbit", "Bear", "Owl", "Turtle", "Fox"]
assert by_seat(e) == ["Turtle", "Fox", "Owl", "Bear"]
assert by_seat(h) == ["Mouse", "Owl", "Rabbit", "Fox", "Turtle", "Bear"]

# On the floor: Rabbit (star seat) passes the note 2 seats clockwise; it reaches every animal.
path = note(m, 5, 0, 2)
print("main, note passed by 2 from the star seat:", " -> ".join(path + [path[0]]))
assert path == ["Rabbit", "Owl", "Fox", "Bear", "Turtle"]
# Easier: Turtle's note by 2 reaches only Owl. Harder: Mouse's note by 2 misses Owl, Fox and Bear.
assert note(e, 4, 0, 2) == ["Turtle", "Owl"]
missed = sorted(set(SIX) - set(note(h, 6, 0, 2)))
print("harder, never get Mouse's note:", missed)
assert missed == ["Bear", "Fox", "Owl"]

# The launch and the midpoint: on 5 chairs pass 2 reaches everyone; on 6 chairs pass 2 needs
# 2 starts and pass 3 needs 3; passes 1 and 5 reach everyone.
starts = lambda n, k: gcd(n, k)
assert starts(5, 2) == 1 and starts(6, 2) == 2 and starts(6, 3) == 3
assert [k for k in range(1, 6) if starts(6, k) == 1] == [1, 5]

# Finale: the yarn star, everyone in one circle of N people passing the ball k people clockwise.
# For each circle size: a pass that needs restarts (and how many) and a pass that makes one star.
# The plan's table: N -> (restart pass, one-star pass), with the shape each restart loop makes.
TABLE = {8: (2, 3, "squares"), 9: (3, 2, "triangles"), 10: (4, 3, "five-pointed stars"),
         11: (None, 3, None), 12: (3, 5, "squares"), 13: (None, 5, None),
         14: (4, 3, "seven-pointed stars"), 15: (3, 4, "pentagons"), 16: (4, 5, "squares")}
POLY = {3: "triangles", 4: "squares", 5: "pentagons"}
for N, (r, one, shape) in TABLE.items():
    # one start, and a star rather than a plain polygon or lines through the middle
    assert gcd(N, one) == 1 and 1 < one < N - 1 and 2 * one != N
    if r is None:
        assert all(gcd(N, k) == 1 for k in range(1, N))  # prime: every pass reaches everyone
        print(f"finale {N}: every pass reaches everyone (prime); pass {one} makes one star")
        continue
    g = gcd(N, r)
    m, j = N // g, r // g  # each loop has m people and steps j of them
    got = POLY[m] if j % m in (1, m - 1) else {5: "five-pointed stars", 7: "seven-pointed stars"}[m]
    assert g > 1 and m >= 3 and got == shape, (N, r, got)
    print(f"finale {N}: pass {r} needs {g} starts, {got} of {m}; pass {one} makes one star")
assert gcd(12, 3) == 3 and gcd(12, 5) == 1

# Early-finisher cards.
assert [k for k in range(1, 8) if gcd(8, k) == 1] == [1, 3, 5, 7]          # K-1: ring of 8 counters
assert [k for k in range(1, 12) if gcd(12, k) == 1] == [1, 5, 7, 11]        # 2-3: clock of 12
# 4-5: 35 dots, hop 14 or 21: 7 pieces, each a five-pointed star {5/2}
for k in (14, 21):
    g = gcd(35, k)
    assert g == 7 and 35 // g == 5 and (k // g) % 5 in (2, 3)
assert [k for k in range(1, 35) if gcd(35, k) == 7] == [7, 14, 21, 28]  # 7 and 28 give pentagons
print("all checks passed")
