#!/usr/bin/env python3
"""Check every answer in the Hackenbush puzzle key on the boards as printed.

    python3 plans/home-plans/src/hackenbush_puzzles_check.py

Reuses the game search and value code of src/hackenbush_check.py (which runs its
own checks on import) and reads the boards from src/hackenbush_puzzles.py.
Finite boards: a value v is confirmed twice, by the simplest-number recursion and
by game search alone (the board beside its colour swap, or beside a stalk worth
-v, is a loss for whoever moves first). Stalks that never end: every chop leaves
a finite stalk, so the value is the simplest number strictly above all of Blue's
chops and below all of Red's; we check the two sides squeeze to the claimed value.
Exits non-zero if any claim fails.
"""
import contextlib
import io
import pathlib
import sys
from fractions import Fraction as F
from itertools import product

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
with contextlib.redirect_stdout(io.StringIO()):
    import hackenbush_check as H  # noqa: E402  (exits if its own checks fail)
from hackenbush_puzzles import (BOARDS, P1, P3, alternating, red_forever,  # noqa: E402
                                third)

FAILS = []
Game, value, stalk, total, plus, swap, rule = (H.Game, H.value, H.stalk, H.total, H.plus,
                                               H.swap, H.stalk_rule)


def check(ok, text):
    print(("PASS  " if ok else "FAIL  ") + text)
    if not ok:
        FAILS.append(text)


def edges(pieces):
    """Printed pieces as edges; a point at height 0 is the ground."""
    out = []
    for k, p in enumerate(pieces):
        node = lambda x, y: "G" if y == 0 else (x, y)  # noqa: E731
        if p[0] == "seg":
            _, x1, y1, x2, y2, c = p
            out.append((node(x1, y1), node(x2, y2), c))
        elif p[0] == "loop":          # a loop hanging from a point plays like one segment there
            _, x, y, r, c = p
            out.append((node(x, y), ("loop", k), c))
        else:
            raise ValueError("finite boards only")
    return out


def swapped(e):
    return [(u, v, "R" if c == "B" else "B") for (u, v, c) in e]


def confirm(e, v, text):
    check(value(e) == v, f"{text} is worth {v}")
    check(Game(plus(e, swapped(e))).outcome() == "second",
          f"{text} beside its colour swap: whoever moves first loses")
    want = "B" if v > 0 else "R" if v < 0 else "second"
    check(Game(e).outcome() == want, f"{text}: the sign of its worth names the winner ({want})")


ALL = {n: list(map("".join, product("BR", repeat=n))) for n in range(1, 13)}


def stalks_worth(v, upto=10):
    return [s for n in range(1, upto + 1) for s in ALL[n] if rule(s) == v]


print("== Problem 1: reading stalks")
want1 = {"a": F(3, 4), "b": F(3, 8), "c": F(7, 8), "d": F(-3, 4)}
for k, s in P1.items():
    e = edges(BOARDS["P1"][k])
    confirm(e, want1[k], f"({k}) {s}")
    check(rule(s) == want1[k], f"({k}) {s}: the stalk rule agrees")
check(Game(total("BRB", "RB", "RBB")).outcome() == "second", "BRB + RB + RBB: whoever moves first loses (3/4 test)")

print("== Problem 2: building stalks (the answer is the only stalk up to 10 segments)")
for v, s in [(F(9, 16), "BRBRR"), (F(11, 16), "BRBRB"), (F(11, 4), "BBBRB")]:
    check(stalks_worth(v) == [s], f"the only stalk worth {v} is {s}")
    check(value(stalk(s, "a")) == v, f"{s} is worth {v} by the solver")
    check(Game(total(s, swap(s))).outcome() == "second", f"{s} beside {swap(s)}: whoever moves first loses")

print("== Problem 3: two blue, two red, in order")
want3 = {"E": F(5, 4), "C": F(5, 8), "A": F(3, 8), "D": F(-3, 8), "F": F(-5, 8), "B": F(-5, 4)}
check(sorted(P3.values()) == sorted(s for s in ALL[4] if s.count("B") == 2), "the six stalks are every order of BBRR")
for k, s in P3.items():
    check(value(edges(BOARDS["P3"][k])) == want3[k], f"{k} {s} is worth {want3[k]}")
order = sorted(P3, key=lambda k: -value(edges(BOARDS["P3"][k])))
check(order == list("ECADFB"), "best for Blue to best for Red: E C A D F B")
for a, b in zip(order, order[1:]):
    g = Game(plus(edges(BOARDS["P3"][a]), swapped(edges(BOARDS["P3"][b]))))
    check(g.outcome() == "B", f"{a} beside the colour swap of {b}: Blue wins whoever starts ({a} is better for Blue)")

print("== Problem 4: make it fair")
e4 = edges(BOARDS["P4"])
check(value(e4) == F(7, 8), "the board (BRB and BRRR) is worth 7/8")
check(stalks_worth(F(-7, 8)) == ["RBRR"], "the only stalk worth -7/8 is RBRR")
check(Game(plus(e4, stalk("RBRR", "z"))).outcome() == "second", "board + RBRR: whoever moves first loses")
check(all(Game(plus(e4, stalk(s, "z"))).outcome() != "second" for n in range(1, 7) for s in ALL[n] if s != "RBRR"),
      "no other stalk of 1 to 6 segments balances it")

print("== Problem 5: pictures")
want5 = {"The Y": F(1), "The bush": F(7, 8), "The flower": F(17, 16), "The person": F(3, 2)}
same = {"The Y": "B", "The bush": "BRBB", "The flower": "BBRRRR", "The person": "BBR"}
for k, pieces in BOARDS["P5"].items():
    e = edges(pieces)
    confirm(e, want5[k], k)
    s = same[k]
    check(Game(plus(e, stalk(swap(s), "z"))).outcome() == "second", f"{k} plays exactly like the stalk {s}")
y = edges(BOARDS["P5"]["The Y"])
gY = Game(y)
check(sorted(value([x for i, x in enumerate(y) if i in q]) for _, q in gY.cuts(gY.start, "B")) == [0, F(1, 2)]
      and [value([x for i, x in enumerate(y) if i in q]) for _, q in gY.cuts(gY.start, "R")] == [2],
      "the Y: Blue's chops leave 0 or 1/2, Red's chop leaves 2, and the simplest number between 1/2 and 2 is 1")
person = edges(BOARDS["P5"]["The person"])
check(sum(c == "R" for *_, c in person) == 2 and sum(c == "B" for *_, c in person) == 4,
      "the person: 4 blue (legs, arms), 2 red (body, head)")

print("== Problem 6: ten red, one blue")
check(rule("B" + "R" * 10) == F(1, 1024) and value(stalk("B" + "R" * 10, "a")) == F(1, 1024),
      "B with 10 red on top is worth 1/1024: Blue wins whoever starts")
tree10 = [("G", "t", "B")] + [("t", f"l{i}", "R") for i in range(10)]
check(value(tree10) == F(1, 1024) and Game(tree10).outcome() == "B",
      "a blue trunk with 10 red leaves is worth 1/1024: Blue wins whoever starts")


def squeeze(pattern, v, text, N=60):
    """Blue's chops leave the prefixes ending below a blue segment; Red's likewise."""
    s = "".join(pattern(i) for i in range(N))
    L = [rule(s[:i]) for i in range(N) if s[i] == "B"]
    R = [rule(s[:i]) for i in range(N) if s[i] == "R"]
    check(max(L) < v < min(R), f"{text}: every Blue chop leaves less than {v}, every Red chop more")
    check(min(R) - max(L) < F(1, 2 ** (N - 4)), f"{text}: the two sides close in on {v} (gap below 2^-{N - 4})")


print("== Problem 7: blue, red, blue, red, forever")
squeeze(alternating, F(2, 3), "BRBR... forever")
check([rule("BRBRBR"[:n]) for n in range(1, 7)] == [1, F(1, 2), F(3, 4), F(5, 8), F(11, 16), F(21, 32)],
      "its first stalks: 1, 1/2, 3/4, 5/8, 11/16, 21/32")

print("== Problem 8: worth 1/3")
check("".join(third(i) for i in range(9)) == "BRRBRBRBR", "the drawn answer is B R R, then B R forever")
squeeze(third, F(1, 3), "BRR then BRBR... forever")
check(F(1, 4) + F(1, 8) * F(2, 3) == F(1, 3), "1 - 1/2 - 1/4 = 1/4, plus 1/8 of the 2/3 pattern, is 1/3")

print("== Problem 9: no stalk that ends is worth 1/3")
ok = all((rule(s).denominator & (rule(s).denominator - 1)) == 0 for n in ALL for s in ALL[n])
check(ok, "every stalk of 1 to 12 segments is worth a fraction whose bottom is a power of 2")
check(all(rule(s) != F(1, 3) for n in ALL for s in ALL[n]), "none of them is worth 1/3")

print("== Problem 10: red forever on a blue trunk")
check(red_forever(0) == "B" and all(red_forever(i) == "R" for i in range(1, 50)), "the drawn stalk is B, then R forever")
check(not Game([]).wins(frozenset(), "R"), "Blue first: chop the trunk; everything falls and Red has no move")
ok = all(value(stalk("B" + "R" * k, "a")) > 0 for k in range(0, 9)) and all(rule("B" + "R" * k) > 0 for k in range(40))
check(ok, "Red first: every red chop leaves B with some red on top, worth more than 0, so Blue wins")
for k in range(0, 7):
    # the infinite stalk beside RB^k (worth -1/2^k): Red wins whoever starts
    red_first = not Game(total("B" + "R" * (k + 1), "R" + "B" * k)).wins(
        Game(total("B" + "R" * (k + 1), "R" + "B" * k)).start, "B")
    blue_trunk = Game(total("R" + "B" * k)).outcome() == "R" if k > 0 else True
    blue_other = all(not Game(total("B" + "R" * (j + 1), "R" + "B" * j)).wins(
        Game(total("B" + "R" * (j + 1), "R" + "B" * j)).start, "B") for j in range(k))
    check(red_first and blue_trunk and blue_other,
          f"beside RB^{k} (worth -1/{2 ** k}) Red wins whoever starts, so it is worth less than 1/{2 ** k}")

print()
if FAILS:
    print(f"{len(FAILS)} claim(s) FAILED")
    sys.exit(1)
print("all claims checked")
