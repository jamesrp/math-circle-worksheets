#!/usr/bin/env python3
"""Check every factual claim in plans/home-plans/2026-11-21-hackenbush.md.

    python3 plans/home-plans/src/hackenbush_check.py

Red-blue Hackenbush, normal play: Blue cuts one blue segment, Red one red
segment; every segment no longer joined to the ground (through segments) is
removed; a player with no move loses. Stalks are written bottom to top, so BR
is a blue segment on the ground with a red one on top.

Two independent methods. (1) Game search: who wins with each starter, and which
cuts win. (2) Values: the simplest number strictly between Blue's best option
and Red's best option. A value v is confirmed by method (1) alone by adding a
stalk worth -v and checking that the sum is a second-player win with either
starter. The printed boards are read from src/hackenbush_positions.py, so the
boards checked are the boards printed. Exits non-zero if any claim fails.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hackenbush_positions import GROUND, POSITIONS  # noqa: E402

FAILS = []


def check(ok, text):
    print(("PASS  " if ok else "FAIL  ") + text)
    if not ok:
        FAILS.append(text)


# ---------------------------------------------------------------- boards
def stalk(s, tag):
    """Stalk s (bottom to top) as edges; ground is node 'G'."""
    out, prev = [], "G"
    for k, colour in enumerate(s):
        node = f"{tag}{k}"
        out.append((prev, node, colour))
        prev = node
    return out


def total(*stalks):
    edges = []
    for k, s in enumerate(stalks):
        edges += stalk(s, f"s{k}_")
    return edges


def printed(num):
    """Board number num from the positions page, as edges."""
    segs = next(s for n, _, s in POSITIONS if n == num)

    def node(x, y):
        return "G" if y == GROUND else (x, y)
    return [(node(x1, y1), node(x2, y2), c) for (x1, y1, x2, y2, c) in segs]


def plus(*boards):
    """Disjoint sum: rename non-ground nodes apart."""
    out = []
    for k, b in enumerate(boards):
        ren = lambda v: v if v == "G" else (k, v)  # noqa: E731
        out += [(ren(u), ren(v), c) for (u, v, c) in b]
    return out


# ---------------------------------------------------------------- method 1: game search
class Game:
    def __init__(self, edges):
        self.E = tuple(edges)
        self.start = self.grounded(frozenset(range(len(self.E))))

    def grounded(self, alive):
        adj = {}
        for i in alive:
            u, v, _ = self.E[i]
            adj.setdefault(u, []).append((v, i))
            adj.setdefault(v, []).append((u, i))
        seen, stack, keep = {"G"}, ["G"], set()
        while stack:
            x = stack.pop()
            for y, i in adj.get(x, []):
                keep.add(i)
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        return frozenset(keep)

    def cuts(self, pos, who):
        return [(i, self.grounded(pos - {i})) for i in sorted(pos) if self.E[i][2] == who]

    @lru_cache(maxsize=None)
    def wins(self, pos, who):
        """True if `who`, about to move on pos, can force the win."""
        other = "R" if who == "B" else "B"
        return any(not self.wins(q, other) for _, q in self.cuts(pos, who))

    def winner(self, starter, pos=None):
        pos = self.start if pos is None else pos
        other = "R" if starter == "B" else "B"
        return starter if self.wins(pos, starter) else other

    def winning_cuts(self, who, pos=None):
        pos = self.start if pos is None else pos
        other = "R" if who == "B" else "B"
        return [self.E[i] for i, q in self.cuts(pos, who) if not self.wins(q, other)]

    def outcome(self):
        """'B' (Blue wins whoever starts), 'R', or 'second' (whoever moves second)."""
        b, r = self.winner("B"), self.winner("R")
        if b == r:
            return b
        assert (b, r) == ("R", "B"), "first-player wins cannot happen with numbers"
        return "second"


# ---------------------------------------------------------------- method 2: values
def simplest(lo, hi):
    """Simplest number strictly between lo and hi (None means no bound)."""
    if lo is not None and hi is not None:
        assert lo < hi
    def ok(x):
        return (lo is None or x > lo) and (hi is None or x < hi)
    if ok(F(0)):
        return F(0)
    if lo is not None and lo >= 0:            # positive: smallest integer above lo, if it fits
        n = F(math.floor(lo) + 1)
        if ok(n):
            return n
    if hi is not None and hi <= 0:
        n = F(math.ceil(hi) - 1)
        if ok(n):
            return n
    d = 2
    while True:                               # otherwise the smallest denominator 2^k
        a, b = math.floor(lo * d), math.ceil(hi * d)
        fits = [F(k, d) for k in range(a, b + 1) if ok(F(k, d))]
        if fits:
            return min(fits, key=abs)
        d *= 2


def value(edges):
    g = Game(edges)

    @lru_cache(maxsize=None)
    def val(pos):
        left = [val(q) for _, q in g.cuts(pos, "B")]
        right = [val(q) for _, q in g.cuts(pos, "R")]
        return simplest(max(left) if left else None, min(right) if right else None)
    return val(g.start)


def stalk_rule(s):
    """Berlekamp's rule for a stalk: the first run of one colour counts 1 each;
    after the first change of colour each segment counts half the one before,
    plus for blue and minus for red."""
    if not s:
        return F(0)
    sign = {"B": 1, "R": -1}
    k = 0
    while k < len(s) and s[k] == s[0]:
        k += 1
    v, w = F(sign[s[0]] * k), F(1)
    for c in s[k:]:
        w /= 2
        v += sign[c] * w
    return v


def swap(s):
    return s.translate(str.maketrans("BR", "RB"))


def confirm_value(edges, v, balancer, text):
    """Confirm value v by game search alone: edges + balancer must be a
    second-player win, where balancer is a stalk worth -v by Berlekamp's rule."""
    check(stalk_rule(balancer) == -v, f"{balancer} is worth {-v} by the stalk rule")
    g = Game(plus(edges, stalk(balancer, "z")))
    check(g.outcome() == "second", f"{text} + {balancer}: whoever moves first loses")
    check(value(edges) == v, f"{text} has value {v}")


# ---------------------------------------------------------------- the printed page
print("== Positions page")
t, tree, house, sticks, more = (printed(n) for n in (1, 2, 3, 4, 5))
check(next(s for n, _, s in POSITIONS if n == 6) == [], "board 6 is blank")

g = Game(t)
check(g.outcome() == "B", "1 Two towers (BBB + RR): Blue wins whoever starts")
blue_top = ((30, 48), (30, 66), "B")
check(g.winning_cuts("B") == [blue_top], "1: Blue starting wins only by chopping the top blue segment")
after_bottom = g.grounded(g.start - {g.E.index(("G", (30, 30), "B"))})
check(g.wins(after_bottom, "R"), "1: if Blue chops the bottom blue, the whole tower falls and Red wins")
confirm_value(t, F(1), "R", "Two towers")

g = Game(tree)
trunk = ("G", (47, 36), "B")
check(g.outcome() == "B", "2 The tree (blue trunk, 3 red leaves): Blue wins whoever starts")
check(g.winning_cuts("B") == [trunk], "2: Blue starting wins only by chopping the trunk")
ok = all(Game(tree).winning_cuts("B", q) == [trunk] for _, q in g.cuts(g.start, "R"))
check(ok, "2: after any red cut, chopping the trunk wins (and is the only win)")
confirm_value(tree, F(1, 8), "RBBB", "The tree")

g = Game(house)
walls = [("G", (30, 38), "B"), ("G", (64, 38), "B")]
check(g.outcome() == "B", "3 The house (blue walls; red ceiling and roof): Blue wins whoever starts")
check(sorted(g.winning_cuts("B")) == sorted(walls), "3: Blue starting wins by chopping either wall")
ok = all(sorted(g.winning_cuts("B", q)) == sorted(walls) for _, q in g.cuts(g.start, "R"))
check(ok, "3: after any red cut, chopping either wall wins")
one_wall = g.grounded(g.start - {g.E.index(walls[0])})
check(len(one_wall) == 4, "3: with one wall chopped, nothing falls (the other wall holds the house up)")
check(g.winner("B") == "B" and not g.wins(one_wall, "R"), "3: Blue chops one wall, then the other, and wins")
confirm_value(house, F(1, 4), "RBB", "The house")

g = Game(sticks)
check(g.outcome() == "R", "4 Sticks (BR + R): Red wins whoever starts")
check(g.winning_cuts("R") == [((34, 30), (34, 48), "R")], "4: Red starting wins only by chopping the red top of BR")
confirm_value(sticks, F(-1, 2), "BR", "Sticks")

g = Game(more)
check(g.outcome() == "second", "5 More sticks (BR + BR + R): whoever moves first loses")
check(value(more) == 0, "5 has value 0")
# the reply proof in the plan
B1, B2, R1 = ("G", (24, 30), "B"), ("G", (47, 30), "B"), ("G", (70, 30), "R")
T1, T2 = ((24, 30), (24, 48), "R"), ((47, 30), (47, 48), "R")
E = g.E
idx = {e: i for i, e in enumerate(E)}
def after(pos, *cut):
    for e in cut:
        pos = g.grounded(pos - {idx[e]})
    return pos
check(not g.wins(after(g.start, B1, T2), "B"), "5: Blue chops a BR at the ground; Red chops the other red top; Blue loses")
check(not g.wins(after(g.start, R1, B1), "R"), "5: Red chops the lone R; Blue chops a whole BR; Red loses")
check(not g.wins(after(g.start, T1, B2), "R"), "5: Red chops a red top; Blue chops the other BR at the ground; Red loses")

print("== Jay's strand")
for s, v in [("B", 1), ("R", -1), ("BR", F(1, 2)), ("BRR", F(1, 4)), ("RB", F(-1, 2)),
             ("RBB", F(-1, 4)), ("BRB", F(3, 4)), ("BBR", F(3, 2)), ("BBRB", F(7, 4))]:
    check(value(stalk(s, "a")) == v, f"stalk {s} is worth {v}")
for k in range(1, 6):
    b = [("G", "t", "B")] + [("t", f"l{i}", "R") for i in range(k)]
    check(value(b) == F(1, 2 ** k), f"blue trunk with {k} red leaves is worth 1/{2 ** k}")
check(Game(total("BR", "R")).outcome() == "R" and Game(total("BR", "BR", "R")).outcome() == "second",
      "one BR loses to an R; two BR balance an R")
check(Game(total("BRR", "BRR", "RB")).outcome() == "second", "BRR + BRR + RB: whoever moves first loses")
check(Game(total("BR", "BR", "RB")).outcome() == "B", "BR + BR + RB: Blue wins (RB is not R)")
check(Game(plus(house, stalk("RBB", "z"))).outcome() == "second", "house + RBB: whoever moves first loses")
check(Game(plus(tree, stalk("RBBB", "z"))).outcome() == "second", "tree + RBBB: whoever moves first loses")
check(Game(plus(tree, tree, stalk("RBB", "z"))).outcome() == "second", "tree + tree + RBB: whoever moves first loses")

# Berlekamp's rule against the solver, every stalk up to 6 segments
bad = [s for n in range(1, 7) for s in map("".join, product("BR", repeat=n))
       if value(stalk(s, "a")) != stalk_rule(s)]
check(not bad, "the stalk rule matches the solver on all 126 stalks of 1 to 6 segments")

# one-colour towers: whoever has more segments wins; equal means whoever moves second
ok = True
for m in range(0, 5):
    for n in range(0, 5):
        if m == n == 0:
            continue
        want = "B" if m > n else "R" if n > m else "second"
        ok &= Game(total("B" * m, "R" * n)).outcome() == want
check(ok, "a blue tower of m and a red tower of n (up to 4): more wins; equal, whoever moves second wins")

# a board beside its colour swap balances (mirror strategy), stalks up to 4
ok = all(Game(total(s, swap(s))).outcome() == "second"
         for n in range(1, 5) for s in map("".join, product("BR", repeat=n)))
check(ok, "every stalk of 1 to 4 segments beside its colour swap: whoever moves first loses")
ok = Game(plus(house, [(u, v, "R" if c == "B" else "B") for (u, v, c) in house])).outcome() == "second"
check(ok, "the house beside a colour-swapped house: whoever moves first loses")

# values add, and the sign of the value gives the winner, on all pairs of printed boards
boards = {1: t, 2: tree, 3: house, 4: sticks, 5: more}
ok = True
for a in boards:
    for b in boards:
        if a <= b:
            s = plus(boards[a], boards[b])
            v = value(s)
            ok &= v == value(boards[a]) + value(boards[b])
            want = "B" if v > 0 else "R" if v < 0 else "second"
            ok &= Game(s).outcome() == want
check(ok, "on every pair of printed boards, values add and the sign names the winner")

print()
if FAILS:
    print(f"{len(FAILS)} claim(s) FAILED")
    sys.exit(1)
print("all claims checked")
