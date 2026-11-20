# Checks the opener puzzles in paint-the-island.tex: each must have exactly one answer,
# and every clue must be needed ("without X: n" with n > 1).
# Rule on every puzzle: each country is red, blue or yellow, and two countries that share
# a border (a stretch of line, not only a corner point) have different colors.
# Main map, on a 3-by-4 grid of squares (rows top to bottom):
#   Ant Ant Bear Bear / Cat Dog Eel Bear / Cat Dog Dog Fox
# Eel and Fox meet only at a corner, so they are not neighbors.
# Small map (easier): a 2-by-2 grid, Ant Bear / Cat Dog.
# Run: python3 paint-the-island_check.py
from itertools import product

COLORS = ["red", "blue", "yellow"]


def neighbors(rows):
    cells = {(r, c): x for r, row in enumerate(rows) for c, x in enumerate(row)}
    pairs = set()
    for (r, c), x in cells.items():
        for q in ((r + 1, c), (r, c + 1)):
            y = cells.get(q)
            if y and y != x:
                pairs.add(frozenset((x, y)))
    return sorted(set(cells.values())), pairs


def colorings(rows):
    names, pairs = neighbors(rows)
    out = []
    for cs in product(COLORS, repeat=len(names)):
        s = dict(zip(names, cs))
        if all(s[a] != s[b] for a, b in map(tuple, pairs)):
            out.append(s)
    return names, pairs, out


def run(label, rows, clues):
    names, pairs, cols = colorings(rows)
    sols = [s for s in cols if all(f(s) for _, f in clues)]
    print(f"{label}: neighbors {sorted('-'.join(sorted(p)) for p in pairs)}")
    print(f"  {len(cols)} colorings follow the rule; {len(sols)} fit every clue")
    for s in sols:
        print("   ", ", ".join(f"{n} {s[n]}" for n in names))
    ok = len(sols) == 1
    for i, (text, _) in enumerate(clues):
        rest = clues[:i] + clues[i + 1:]
        n = len([s for s in cols if all(f(s) for _, f in rest)])
        print(f"    without '{text}': {n}")
        ok = ok and n > 1
    print("  OK" if ok else "  PROBLEM")
    return ok


MAIN = [["Ant", "Ant", "Bear", "Bear"], ["Cat", "Dog", "Eel", "Bear"], ["Cat", "Dog", "Dog", "Fox"]]
SMALL = [["Ant", "Bear"], ["Cat", "Dog"]]
count = lambda s, c: list(s.values()).count(c)

main = [
    ("Ant Land is red.", lambda s: s["Ant"] == "red"),
    ("Ant Land and Fox Land are different colors.", lambda s: s["Ant"] != s["Fox"]),
    ("Cat Land and Eel Land are the same color.", lambda s: s["Cat"] == s["Eel"]),
    ("Exactly two countries are blue.", lambda s: count(s, "blue") == 2),
]
harder = [  # no country is told its color
    ("Ant Land and Fox Land are different colors.", lambda s: s["Ant"] != s["Fox"]),
    ("Exactly one country is red.", lambda s: count(s, "red") == 1),
    ("Exactly two countries are blue.", lambda s: count(s, "blue") == 2),
]
easier = [
    ("Ant Land is red.", lambda s: s["Ant"] == "red"),
    ("Bear Land is blue.", lambda s: s["Bear"] == "blue"),
    ("Dog Land is not red.", lambda s: s["Dog"] != "red"),
]
results = [run("Main puzzle", MAIN, main), run("Harder (same map)", MAIN, harder), run("Easier (four countries)", SMALL, easier)]

# Early finisher: cross out clue 4 of the main puzzle; how many answers now?
names, pairs, cols = colorings(MAIN)
left = [s for s in cols if all(f(s) for _, f in main[:3])]
print("Main without clue 4:", len(left), "answers")
for s in left:
    print("   ", ", ".join(f"{n} {s[n]}" for n in names))
# Can the main map be colored with only two colors? (Ant, Cat and Dog all touch each other.)
names, pairs = neighbors(MAIN)
two = [cs for cs in product(["red", "blue"], repeat=6) if all(dict(zip(names, cs))[a] != dict(zip(names, cs))[b] for a, b in map(tuple, pairs))]
print("Main map with two colors:", len(two), "ways")
assert all(results)
