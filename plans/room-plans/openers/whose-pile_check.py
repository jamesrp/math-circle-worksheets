# Checks the opener puzzles in whose-pile.tex: each must have exactly one answer.
# "without X: n" shows how many answers remain if clue X is dropped (n > 1 means the clue is needed).
# Each animal has one pile, and the piles have different sizes. Run: python3 whose-pile_check.py
# It also checks the game facts the November 18 room plan uses on the floor.
from itertools import permutations


def answers(names, sizes, clues):
    out = []
    for p in permutations(sizes):
        s = dict(zip(names, p))
        if all(c(s) for _, c in clues):
            out.append(s)
    return out


def run(names, sizes, clues, label):
    sols = answers(names, sizes, clues)
    print(f"{label}: {len(sols)} answer(s)")
    for s in sols:
        print("   ", ", ".join(f"{a} {s[a]}" for a in sorted(s, key=s.get)))
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        print(f"    without '{text}': {len(answers(names, sizes, rest))}")
    return len(sols)


odd = lambda n: n % 2 == 1
even = lambda n: n % 2 == 0

FOUR, FOUR_SIZES = ["Duck", "Frog", "Goat", "Mouse"], [3, 5, 6, 7]
main = [
    ("Frog has an odd number of counters.", lambda s: odd(s["Frog"])),
    ("Mouse has fewer counters than Frog.", lambda s: s["Mouse"] < s["Frog"]),
    ("Goat has more counters than Frog.", lambda s: s["Goat"] > s["Frog"]),
    ("Duck does not have the biggest pile.", lambda s: s["Duck"] != max(FOUR_SIZES)),
]
easy = [
    ("Goat has the most counters.", lambda s: s["Goat"] == 7),
    ("Mouse has fewer counters than Frog.", lambda s: s["Mouse"] < s["Frog"]),
]
FIVE, FIVE_SIZES = ["Duck", "Frog", "Goat", "Hen", "Mouse"], [3, 5, 6, 7, 8]
hard = [
    ("Duck has an even number of counters.", lambda s: even(s["Duck"])),
    ("Hen has an even number of counters.", lambda s: even(s["Hen"])),
    ("Hen has more counters than Duck.", lambda s: s["Hen"] > s["Duck"]),
    ("Frog has exactly two more counters than Mouse.", lambda s: s["Frog"] == s["Mouse"] + 2),
    ("Goat has more counters than Frog.", lambda s: s["Goat"] > s["Frog"]),
]
# early finisher: clue 4 crossed out gives 2 answers; one new clue that restores exactly one
finisher = main[:3] + [("Goat has more counters than Duck.", lambda s: s["Goat"] > s["Duck"])]

counts = [run(FOUR, FOUR_SIZES, main, "main"),
          run(["Frog", "Goat", "Mouse"], [3, 5, 7], easy, "easier"),
          run(FIVE, FIVE_SIZES, hard, "harder"),
          run(FOUR, FOUR_SIZES, finisher, "early-finisher fix")]
print("without clue 4:", len(answers(FOUR, FOUR_SIZES, main[:3])), "answers")

the_answer = {"Mouse": 3, "Frog": 5, "Duck": 6, "Goat": 7}
assert answers(FOUR, FOUR_SIZES, main) == [the_answer]
assert answers(["Frog", "Goat", "Mouse"], [3, 5, 7], easy) == [{"Frog": 5, "Goat": 7, "Mouse": 3}]
assert answers(FIVE, FIVE_SIZES, hard) == [dict(the_answer, Hen=8)]
# every main clue is needed
assert all(len(answers(FOUR, FOUR_SIZES, main[:i] + main[i + 1:])) > 1 for i in range(len(main)))
assert len(answers(FOUR, FOUR_SIZES, main[:3])) == 2


# Floor facts: one pile, take a number from the menu, whoever takes the last counter wins.
def first_player_wins(n, menu):
    win = [False] * (n + 1)  # win[k]: the player about to move from k can make sure they win
    for k in range(1, n + 1):
        win[k] = any(m <= k and not win[k - m] for m in menu)
    return win[n]


for menu in [(1, 2), (1, 3, 4), (1, 2, 3)]:
    hand_over = [k for k in range(0, 9) if not first_player_wins(k, menu)]
    print("moves", menu, "piles 0-8 to hand over:", hand_over)
# Launch: Goat's 7 with 1 or 2 is a first-player win (take 1, leave 6).
assert first_player_wins(7, (1, 2)) and not first_player_wins(6, (1, 2))
# Midpoint: the same 7 with 1, 3 or 4 is a second-player win.
assert not first_player_wins(7, (1, 3, 4))
# The opener piles 3, 5, 6, 7: which to hand over changes with the rule.
assert [k for k in (3, 5, 6, 7) if not first_player_wins(k, (1, 2))] == [3, 6]
assert [k for k in (3, 5, 6, 7) if not first_player_wins(k, (1, 3, 4))] == [7]
assert counts == [1, 1, 1, 1]
print("all checks passed")
