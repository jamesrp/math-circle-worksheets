# Checks the opener puzzles in mail-route.tex: each must have exactly one answer.
# "without X: n" shows how many answers remain if clue X is dropped (n > 1 means the clue is needed).
# The five-house town is the floor town and the house town on page 1 of the Week 10 packets:
#   green = A (top), purple = B (upper left), yellow = C (upper right),
#   blue = D (bottom left), red = E (bottom right),
#   paths A-B, A-C, B-C, B-D, C-E, D-E.
# The main puzzle states no path rule, so it is checked as a pure order puzzle, and again with the
# path rule a child might assume (from each house straight to the next along one path).
# The harder puzzle states the path rule. Run: python3 mail-route_check.py
from itertools import permutations

FIVE = ["blue", "red", "yellow", "green", "purple"]
PLACE = {"green": "A", "purple": "B", "yellow": "C", "blue": "D", "red": "E"}
PATHS = {frozenset(p) for p in ["AB", "AC", "BC", "BD", "CE", "DE"]}
THREE = ["purple", "yellow", "green"]  # the roof triangle: every pair joined, so any order walks the paths


def on_paths(order):
    return all(frozenset((PLACE[a], PLACE[b])) in PATHS for a, b in zip(order, order[1:]))


def answers(houses, clues, paths=False):
    out = []
    for order in permutations(houses):
        s = {h: i + 1 for i, h in enumerate(order)}  # house -> visit number
        if all(c(s) for _, c in clues) and (not paths or on_paths(order)):
            out.append(order)
    return out


def run(houses, clues, label, paths=False):
    sols = answers(houses, clues, paths)
    print(f"{label}: {len(sols)} answer(s)")
    for o in sols:
        print("   ", ", ".join(o))
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        print(f"    without '{text}': {len(answers(houses, rest, paths))}")
    return len(sols)


first = lambda s: min(s, key=s.get)
last = lambda s: max(s, key=s.get)

main = [
    ("Pat went to the red house right after the blue house.", lambda s: s["red"] == s["blue"] + 1),
    ("Pat went to the green house right after the yellow house.", lambda s: s["green"] == s["yellow"] + 1),
    ("Pat went to the yellow house some time after the red house.", lambda s: s["yellow"] > s["red"]),
    ("The green house was not the last house.", lambda s: s["green"] != 5),
]
easy = [
    ("Pat went to the yellow house right after the purple house.", lambda s: s["yellow"] == s["purple"] + 1),
    ("Pat did not start at the green house.", lambda s: s["green"] != 1),
]
hard = [  # with the stated path rule
    ("Pat started at a bottom house.", lambda s: first(s) in ("blue", "red")),
    ("Pat went to the red house right after the blue house.", lambda s: s["red"] == s["blue"] + 1),
    ("The top house was not first and not last.", lambda s: s["green"] not in (1, 5)),
]
# early finisher: clue 4 crossed out; one new clue that restores exactly one answer
finisher = main[:3] + [("The purple house was the last house.", lambda s: s["purple"] == 5)]

ANSWER = ("blue", "red", "yellow", "green", "purple")
counts = [
    run(FIVE, main, "main"),
    run(FIVE, main, "main, if a child also keeps to the paths", paths=True),
    run(THREE, easy, "easier"),
    run(FIVE, hard, "harder (path rule stated)", paths=True),
    run(FIVE, finisher, "early-finisher fix"),
]
print("harder without its path rule:", len(answers(FIVE, hard)), "answers")
print("main without clue 4:", len(answers(FIVE, main[:3])), "answers:",
      ["/".join(o) for o in answers(FIVE, main[:3])])
print("main without clue 4, keeping to the paths:", len(answers(FIVE, main[:3], paths=True)))

# every main clue is needed, read either way
need = [len(answers(FIVE, main[:i] + main[i + 1:], p)) for p in (False, True) for i in range(4)]
assert min(need) > 1, need
assert answers(FIVE, main) == [ANSWER] and answers(FIVE, hard, True) == [ANSWER]
assert answers(FIVE, finisher) == [ANSWER] and answers(THREE, easy) == [("purple", "yellow", "green")]
assert on_paths(ANSWER)

# The floor walk: Pat's route crosses four of the six bridges and leaves B-C and B-D.
route = [PLACE[h] for h in ANSWER]
used = {frozenset(p) for p in zip(route, route[1:])}
left = sorted("".join(sorted(p)) for p in PATHS - used)
print("bridges left after Pat's route:", left, "; Pat ends at", route[-1])
assert left == ["BC", "BD"]
# From B (Pat's last house), any continuation gets stuck with one counter left.
for nxt in ("C", "D"):
    rest = PATHS - used - {frozenset(("B", nxt))}
    assert not any(nxt in p for p in rest) and len(rest) == 1

assert counts == [1, 1, 1, 1, 1]
print("all checks passed")
