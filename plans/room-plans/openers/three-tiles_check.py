# Checks the opener puzzles in three-tiles.tex: each must have exactly one answer, and every clue is needed.
# "without X: n" shows how many answers remain if clue X is dropped (n > 1 means the clue is needed).
# Tiles are the Week 36 tiles: shape circle/triangle/square, fill open/striped/solid.
# Run: python3 three-tiles_check.py
from itertools import permutations

SHAPES = ["circle", "triangle", "square"]
FILLS = ["open", "striped", "solid"]


def worlds(names, shapes_differ=True, fills="different"):
    """Every way to give each friend one tile. fills: 'different' or 'same-or-different'."""
    n = len(names)
    out = []
    for sh in permutations(range(3), n):
        fill_choices = list(permutations(range(3), n))
        if fills == "same-or-different":
            fill_choices += [(f,) * n for f in range(3)]
        for fi in fill_choices:
            out.append({k: (SHAPES[s], FILLS[f]) for k, s, f in zip(names, sh, fi)})
    return out


def has(w, shape=None, fill=None):
    return [k for k, t in w.items() if (shape is None or t[0] == shape) and (fill is None or t[1] == fill)]


def run(label, all_worlds, clues):
    sols = [w for w in all_worlds if all(c(w) for _, c in clues)]
    print(f"{label}: {len(sols)} answer(s) among {len(all_worlds)}")
    for s in sols:
        print("   ", ", ".join(f"{k} {t[1]} {t[0]}" for k, t in s.items()))
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        print(f"    without '{text}': {sum(all(c(w) for _, c in rest) for w in all_worlds)}")
    assert len(sols) == 1
    assert all(sum(all(c(w) for _, c in clues[:i] + clues[i + 1:]) for w in all_worlds) > 1 for i in range(len(clues)))


THREE = ["Ana", "Ben", "Cy"]
main = [
    ("Ana has a circle", lambda w: w["Ana"][0] == "circle"),
    ("Ben does not have a square", lambda w: w["Ben"][0] != "square"),
    ("The solid tile is not a triangle", lambda w: ("triangle", "solid") not in w.values()),
    ("The striped tile is a square", lambda w: ("square", "striped") in w.values()),
]
run("Main (shapes all different, fills all different)", worlds(THREE), main)

harder = [main[0],
          ("Ben's tile is not striped", lambda w: w["Ben"][1] != "striped"),
          main[2],
          ("Someone has a striped square", lambda w: ("square", "striped") in w.values())]
run("Harder (shapes all different, fills all the same or all different)", worlds(THREE, fills="same-or-different"), harder)
# The main clues under the harder premise leave two answers (all three striped is the second):
print("    main clues, harder premise:", sum(all(c(w) for _, c in main) for w in worlds(THREE, fills="same-or-different")))

TWO = ["Ana", "Ben"]
two_worlds = [w for w in worlds(TWO) if all(t[0] in ("circle", "triangle") and t[1] in ("open", "solid") for t in w.values())]
easier = [
    ("Ana has the circle", lambda w: w["Ana"][0] == "circle"),
    ("The triangle is open", lambda w: all(t[1] == "open" for t in w.values() if t[0] == "triangle")),
]
run("Easier (two friends: a circle and a triangle, one open and one solid)", two_worlds, easier)

# Early finishers on the main puzzle: drop clue 2.
rest = [main[0], main[2], main[3]]
sols = [w for w in worlds(THREE) if all(c(w) for _, c in rest)]
print("Main without clue 2:", len(sols), "answers")
for s in sols:
    print("   ", ", ".join(f"{k} {t[1]} {t[0]}" for k, t in s.items()))
