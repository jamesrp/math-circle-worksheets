# Checks the opener puzzles in photo-line.tex (November 11, 2026): each must have exactly one answer.
# "without X: n" shows how many answers remain if clue X is dropped (n > 1 means the clue is needed).
# Places in the line are numbered 1 to 5 from the left end. Heights are in cubes:
# Mouse 1, Cat 2, Dog 3, Horse 4, Giraffe 5. Run: python3 photo-line_check.py (stdlib only).
# It also checks the tower facts the room plan prints (views of the answer row, the launch row,
# the floor finale and the early-finisher cards).
from itertools import permutations

H = {"Mouse": 1, "Cat": 2, "Dog": 3, "Horse": 4, "Giraffe": 5}


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
    return sols


def at(s, place):
    return next(k for k, v in s.items() if v == place)


def ends(s):
    return at(s, 1), at(s, len(s))


nb = lambda a, b: abs(a - b) == 1
FIVE = ["Mouse", "Cat", "Dog", "Horse", "Giraffe"]
THREE = ["Mouse", "Cat", "Dog"]

main = [
    ("Horse stands in the middle.", lambda s: s["Horse"] == 3),
    ("Dog stands at one end of the line.", lambda s: s["Dog"] in (1, 5)),
    ("Mouse stands between two taller animals.",
     lambda s: 1 < s["Mouse"] < 5 and all(H[at(s, s["Mouse"] + d)] > H["Mouse"] for d in (-1, 1))),
    ("Mouse stands right next to Cat.", lambda s: nb(s["Mouse"], s["Cat"])),
    ("The animal at the left end is shorter than the animal at the right end.",
     lambda s: H[ends(s)[0]] < H[ends(s)[1]]),
]
easy = [
    ("The tallest animal stands at the right end.", lambda s: at(s, len(s)) == max(s, key=H.get)),
    ("Mouse stands between two taller animals.",
     lambda s: 1 < s["Mouse"] < len(s) and all(H[at(s, s["Mouse"] + d)] > H["Mouse"] for d in (-1, 1))),
]
hard = [
    ("Every animal taller than Cat stands somewhere to the right of Cat.",
     lambda s: all(s[x] > s["Cat"] for x in s if H[x] > H["Cat"])),
    ("Cat stands right next to a shorter animal.",
     lambda s: any(nb(s["Cat"], s[x]) and H[x] < H["Cat"] for x in s)),
    ("Horse stands right next to Mouse.", lambda s: nb(s["Horse"], s["Mouse"])),
    ("The two tallest animals stand side by side.", lambda s: nb(s["Giraffe"], s["Horse"])),
]
# early finisher: clue 5 crossed out gives 2 answers; one new clue that restores exactly one
finisher = main[:4] + [("Giraffe stands somewhere to the right of Horse.",
                        lambda s: s["Giraffe"] > s["Horse"])]

sols = [run(FIVE, main, "main"), run(THREE, easy, "easier"),
        run(FIVE, hard, "harder"), run(FIVE, finisher, "early-finisher fix")]
print("without clue 5:", len(answers(FIVE, main[:4])), "answers")
assert [len(s) for s in sols] == [1, 1, 1, 1]
# every main-puzzle clue is needed
assert all(len(answers(FIVE, main[:i] + main[i + 1:])) > 1 for i in range(len(main)))
assert all(len(answers(FIVE, hard[:i] + hard[i + 1:])) > 1 for i in range(len(hard)))
assert all(len(answers(THREE, easy[:i] + easy[i + 1:])) > 1 for i in range(len(easy)))
assert len(answers(FIVE, main[:4])) == 2


def row(s):
    return [H[a] for a in sorted(s, key=s.get)]


def seen(r):
    top = count = 0
    for h in r:
        if h > top:
            top, count = h, count + 1
    return count


def views(r):
    return seen(r), seen(r[::-1])


answer = row(sols[0][0])
assert answer == [2, 1, 4, 5, 3]                        # Cat, Mouse, Horse, Giraffe, Dog
assert row(sols[2][0]) == answer and row(sols[3][0]) == answer
assert row(sols[1][0]) == [2, 1, 3]                     # Cat, Mouse, Dog: the guide's launch row
assert views(answer) == (3, 2)                          # floor at minute 6
launch = [h for h in answer if h <= 3]                  # take Horse and Giraffe away
assert launch == [2, 1, 3] and views(launch) == (2, 1)
assert views([1, 2, 3]) == (3, 1)                       # the launch's move
rows4 = list(permutations(range(1, 5)))
rows5 = list(permutations(range(1, 6)))
assert views([3, 1, 4, 2]) == (2, 2)                    # midpoint hidden row
assert sum(views(r) == (2, 2) for r in rows4) == 6      # six rows of four show 2 and 2
assert not any(views(r) == (1, 1) for r in rows5)       # finale: 1 and 1 never
assert views([1, 4, 5, 3, 2]) == (3, 3)                 # finale: 3 and 3 with five
assert sum(views(r) == (3, 3) for r in rows5) == 6      # 4-5 early-finisher card
assert not any(sum(views(r)) > 6 for r in rows5)        # L + R <= n + 1, so no 4 and 3
assert sorted(r for r in rows4 if views(r) == (3, 2)) == [(1, 2, 4, 3), (1, 3, 4, 2), (2, 3, 4, 1)]

# 2-3 early-finisher card: every 3-by-3 city has exactly two 3s around its edge
cities = [c for c in ((a, b, d) for a in permutations((1, 2, 3)) for b in permutations((1, 2, 3))
                      for d in permutations((1, 2, 3)))
          if all(len({c[0][j], c[1][j], c[2][j]}) == 3 for j in range(3))]
assert len(cities) == 12
for c in cities:
    lines = list(c) + [tuple(c[i][j] for i in range(3)) for j in range(3)]
    edge = [v for line in lines for v in views(list(line))]
    assert edge.count(3) == 2 and sum(edge) == 22
print("all checks passed")
