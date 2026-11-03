# Checks the opener puzzles in who-sat-where.tex: each must have exactly one answer.
# "without X: n" shows how many answers remain if clue X is dropped (n > 1 means the clue is needed).
# Chairs are numbered 1 green, 2 blue, 3 red, 4 yellow, 5 purple, left to right. Run: python3 check.py
from itertools import permutations

def answers(names, clues):
    out = []
    for p in permutations(range(1, len(names) + 1)):
        s = dict(zip(names, p))
        if all(c(s) for _, c in clues):
            out.append(s)
    return out

def run(names, clues, label):
    sols = answers(names, clues)
    print(f"{label}: {len(sols)} answer(s)")
    for s in sols:
        print("   ", ", ".join(sorted(s, key=s.get)))
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        print(f"    without '{text}': {len(answers(names, rest))}")
    return len(sols)

nb = lambda a, b: abs(a - b) == 1
FIVE = ["Bear", "Fox", "Owl", "Rabbit", "Turtle"]
main = [
    ("Fox sat in the red chair.", lambda s: s["Fox"] == 3),
    ("Owl sat on an end chair.", lambda s: s["Owl"] in (1, 5)),
    ("Rabbit sat right next to Owl.", lambda s: nb(s["Rabbit"], s["Owl"])),
    ("Bear sat somewhere to the left of Fox.", lambda s: s["Bear"] < s["Fox"]),
    ("Turtle sat right next to Fox.", lambda s: nb(s["Turtle"], s["Fox"])),
]
easy = [
    ("Owl sat in the green chair.", lambda s: s["Owl"] == 1),
    ("Fox did not sit next to Owl.", lambda s: not nb(s["Fox"], s["Owl"])),
]
hard = [
    ("Owl sat on an end chair.", lambda s: s["Owl"] in (1, 5)),
    ("Rabbit sat right next to Owl.", lambda s: nb(s["Rabbit"], s["Owl"])),
    ("Fox had exactly one animal between it and Owl.", lambda s: abs(s["Fox"] - s["Owl"]) == 2),
    ("Bear sat somewhere to the left of Rabbit.", lambda s: s["Bear"] < s["Rabbit"]),
    ("Turtle did not sit on an end chair.", lambda s: s["Turtle"] not in (1, 5)),
]
# early-finisher: clue 5 crossed out gives 2 answers; one new clue that restores exactly one
finisher = main[:4] + [("Bear sat on an end chair.", lambda s: s["Bear"] in (1, 5))]

counts = [run(FIVE, main, "main"), run(["Bear", "Fox", "Owl"], easy, "easier"),
          run(FIVE, hard, "harder"), run(FIVE, finisher, "early-finisher fix")]
print("without clue 5:", len(answers(FIVE, main[:4])), "answers")
assert counts == [1, 1, 1, 1]
print("all checks passed")
