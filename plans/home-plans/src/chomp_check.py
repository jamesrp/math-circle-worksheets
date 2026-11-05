#!/usr/bin/env python3
"""Check every factual claim in plans/home-plans/2026-11-08-poisoned-cookie.md.

    python3 plans/home-plans/src/chomp_check.py

Conventions (the plan's). The poison is the bottom-left cookie, row 1, column 1.
A bite at (row r, column c) eats that cookie and every cookie above it, to its
right, or both. Whoever has to eat the poison loses. A board is written by its
row lengths, bottom row first: (4, 2, 2) is a bottom row of 4 with rows of 2 and
2 above. "R by C" means R rows and C columns.

Two independent solvers are used: one on row-length tuples, one on arbitrary
sets of cells. They are compared on every board inside the big printed board
(4 rows by 6 columns). Exits non-zero if any claim fails.
"""
from functools import lru_cache
from itertools import product
import sys

FAILS = []


def check(ok, text):
    print(("PASS  " if ok else "FAIL  ") + text)
    if not ok:
        FAILS.append(text)


# ---------------------------------------------------------------- solver A
def norm(rows):
    rows = list(rows)
    while rows and rows[-1] == 0:
        rows.pop()
    return tuple(rows)


def bites(pos):
    """All legal bites except eating the poison: ((r, c), board left)."""
    out = []
    for r in range(len(pos)):
        for c in range(pos[r]):
            if (r, c) == (0, 0):
                continue
            new = list(pos)
            for i in range(r, len(pos)):
                new[i] = min(new[i], c)
            out.append(((r + 1, c + 1), norm(new)))
    return out


@lru_cache(maxsize=None)
def win(pos):
    """True if the player to move can make sure the other player eats the poison.
    The poison alone, (1,), has no bites here: the mover must eat it and loses."""
    return any(not win(q) for _, q in bites(pos))


def winning_bites(pos):
    return [m for m, q in bites(pos) if not win(q)]


def rect(rows, cols):
    return (cols,) * rows


def after(pos, bite):
    return dict(bites(pos))[bite]


def L(right, up):
    """L shape: the poison, an arm of `right` cookies to its right, `up` above."""
    return norm((right + 1,) + (1,) * up)


def boards_in_box(rows, cols):
    res = set()
    for t in product(range(cols + 1), repeat=rows):
        if all(t[i] >= t[i + 1] for i in range(rows - 1)) and t[0] >= 1:
            res.add(norm(t))
    return sorted(res)


# ---------------------------------------------------------------- solver B
def cells_of(pos):
    return frozenset((r, c) for r, n in enumerate(pos, 1) for c in range(1, n + 1))


@lru_cache(maxsize=None)
def win_cells(cells):
    if cells == frozenset({(1, 1)}):
        return False
    for (r, c) in cells:
        if (r, c) == (1, 1):
            continue
        rest = frozenset((a, b) for (a, b) in cells if not (a >= r and b >= c))
        if not win_cells(rest):
            return True
    return False


def transpose(pos):
    return norm(tuple(sum(1 for n in pos if n > j) for j in range(pos[0])))


# ================================================================= claims
print("Solver cross-check")
box = boards_in_box(4, 6)
check(all(win(p) == win_cells(cells_of(p)) for p in box),
      f"the two solvers agree on all {len(box)} boards inside 4 by 6")
check(all(win(p) == win(transpose(p)) for p in boards_in_box(6, 6)),
      "a board and its flip across the poison's diagonal win or lose together (all boards inside 6 by 6)")

print("\nFact 1: every rectangle bigger than one cookie is a first-player win")
check(not win((1,)), "1 by 1 (the poison alone) loses for the player to move")
rects = [(r, c) for r in range(1, 9) for c in range(1, 9) if (r, c) != (1, 1)]
check(all(win(rect(r, c)) for r, c in rects),
      "every rectangle from 1 by 2 up to 8 by 8 is a first-player win")
used = [(1, 5), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5),
        (3, 6), (4, 4), (4, 5), (4, 6)]
check(all(win(rect(r, c)) for r, c in used),
      "every rectangle the plan uses (1 by 5; 2 by 2 to 2 by 6; 3 by 3 to 3 by 6; 4 by 4 to 4 by 6) is a first-player win")

print("\nStrategy stealing, seen on real boards")
for r, c in [(3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6)]:
    full = rect(r, c)
    a = after(full, (r, c))
    replies = winning_bites(a)
    left_by_reply = {after(a, m) for m in replies}
    left_by_first = {after(full, m) for m in winning_bites(full)}
    check(win(a) and left_by_reply == left_by_first and len(replies) == 1,
          f"{r} by {c}: after the top-right bite the only winning answer is {replies[0]}, "
          f"which leaves {sorted(left_by_reply)[0]}, the same board as the first player's own winning bite")
for c in range(2, 9):
    check(winning_bites(rect(2, c)) == [(2, c)],
          f"2 by {c}: the top-right bite itself is the winning first bite (nothing to steal)")
# The argument needs one cookie inside every bite; only rectangles have one.
for p in boards_in_box(4, 6):
    if len(cells_of(p)) < 2:
        continue
    common = set(cells_of(p)) - {(1, 1)}
    for (r, c) in cells_of(p) - {(1, 1)}:
        common &= {(a, b) for (a, b) in cells_of(p) if a >= r and b >= c}
    is_rect = len(set(p)) == 1
    if is_rect != bool(common):
        check(False, f"one cookie lies in every bite exactly on rectangles: fails at {p}")
        break
else:
    check(True, "inside 4 by 6, one cookie lies in every bite exactly when the board is a rectangle")
check(not win(L(2, 2)) and not win((2, 1)),
      "non-rectangles can lose for the mover: the little corner (2, 1) and the L with arms 2 and 2")

print("\nFact 2: one row, two rows, squares, L shapes")
for n in range(2, 9):
    check(winning_bites(rect(1, n)) == [(1, 2)],
          f"1 by {n}: the only winning bite eats everything but the poison")
ok = True
for a in range(1, 31):
    for b in range(0, a + 1):
        p = norm((a, b))
        if win(p) == (b == a - 1):
            ok = False
check(ok, "two rows (bottom row up to 30, top row 0 to bottom): the mover loses exactly when the top row is one shorter")
ok = True
for a in range(2, 31):
    for b in range(0, a + 1):
        p = norm((a, b))
        if b == a - 1:
            continue
        if b == a:
            reply, target = (2, a), norm((a, a - 1))
        else:
            reply, target = (1, b + 2), norm((b + 1, b))
        q = after(p, reply)
        if q != target or win(q):
            ok = False
check(ok, "two-row reply rule: from equal rows eat the top-right cookie; from a top row two or more shorter, "
          "cut the bottom row to one longer than the top; both leave a step, which loses for the mover")
ok = True
for a in range(1, 13):
    for b in range(1, 13):
        if win(L(a, b)) == (a == b):
            ok = False
check(ok, "L shapes with arms 1 to 12: the mover loses exactly when the arms are equal")
ok = True
for k in range(1, 13):
    for m, q in bites(L(k, k)):
        r, c = m
        mirror = (c, r)
        q2 = after(q, mirror)
        j = (c - 2) if r == 1 else (r - 2)
        if q2 != L(j, j):
            ok = False
check(ok, "copy-cat on an equal L (arms 1 to 12): copying any bite on the other arm gives equal arms again")
for n in range(2, 9):
    check(winning_bites(rect(n, n)) == [(2, 2)] and after(rect(n, n), (2, 2)) == L(n - 1, n - 1),
          f"{n} by {n}: the only winning bite is next to the poison diagonally, leaving an L with arms {n-1} and {n-1}")

print("\nFact 3: winning first bites the adult can use (each is the only one)")
table = {(2, 3): (2, 3), (2, 4): (2, 4), (2, 5): (2, 5), (2, 6): (2, 6),
         (3, 3): (2, 2), (3, 4): (2, 3), (3, 5): (3, 4), (3, 6): (2, 4),
         (4, 4): (2, 2), (4, 5): (3, 3), (4, 6): (2, 3)}
leaves = {(3, 4): (4, 2, 2), (3, 5): (5, 5, 3), (3, 6): (6, 3, 3), (4, 5): (5, 5, 2, 2),
          (4, 6): (6, 2, 2, 2)}
for (r, c), m in table.items():
    wb = winning_bites(rect(r, c))
    extra = f", leaving {leaves[(r, c)]}" if (r, c) in leaves else ""
    check(wb == [m], f"{r} by {c}: only winning first bite is row {m[0]}, column {m[1]}{extra}")
    if (r, c) in leaves:
        check(after(rect(r, c), m) == leaves[(r, c)], f"{r} by {c}: that bite leaves {leaves[(r, c)]}")
uniq = all(len(winning_bites(rect(r, c))) == 1 for r in range(2, 7) for c in range(2, 7))
check(uniq, "every rectangle with both sides 2 to 6 has exactly one winning first bite (a computation, not a theorem)")

print("\nRefutations the adult may want on 3 by 4 (every other first bite loses)")
full = rect(3, 4)
plan_answers = {(1, 2): (2, 1), (1, 3): (3, 2), (1, 4): (2, 2), (2, 1): (1, 2), (2, 2): (1, 4),
                (2, 4): (2, 3), (3, 1): (2, 4), (3, 2): (1, 3), (3, 3): (2, 3), (3, 4): (2, 3)}
check(set(plan_answers) == {m for m, _ in bites(full)} - {(2, 3)},
      "the plan lists an answer for every first bite on 3 by 4 except the winning one")
for m, ans in plan_answers.items():
    q = after(full, m)
    check(ans in winning_bites(q),
          f"3 by 4, first bite {m} leaves {q}; the plan's answer {ans} leaves {after(q, ans)}, a loss for the mover")

print("\nFact 4: three rows, the tempting pattern")
def pattern(n):
    return (2, n // 2 + 1) if n % 2 == 0 else (3, (n + 3) // 2)
for n in range(4, 9):
    check(winning_bites(rect(3, n)) == [pattern(n)], f"3 by {n}: pattern bite {pattern(n)} is the only winning bite")
check(winning_bites(rect(3, 9)) == [(3, 7)] and pattern(9) != (3, 7),
      "3 by 9: the pattern says (3, 6) but the only winning bite is (3, 7)")

print("\nLaunch")
q = after(rect(2, 5), (1, 3))
check(q == (2, 2) and len(cells_of(rect(2, 5))) - len(cells_of(q)) == 6,
      "launch: on 2 by 5, the bite at row 1, column 3 eats six cookies and leaves a 2 by 2")
q = after(rect(2, 5), (2, 2))
check(q == (5, 1) and len(cells_of(rect(2, 5))) - len(cells_of(q)) == 4,
      "launch: on 2 by 5, the bite at row 2, column 2 eats only the four top-row cookies from column 2 on")

print("\nRose's boards")
check(winning_bites(rect(2, 2)) == [(2, 2)] and after(rect(2, 2), (2, 2)) == (2, 1),
      "2 by 2: the only winning bite is the top-right cookie, which leaves the little corner (2, 1)")
check(not win((2, 1)) and all(q == (1,) for _, q in [(m, after(after((2, 1), m), m2))
                                                       for m in [(1, 2), (2, 1)]
                                                       for m2 in winning_bites(after((2, 1), m))]),
      "the little corner loses for the mover: whichever cookie is eaten, the other player eats the other one")
p = after(rect(2, 3), (2, 3))
ok = p == (3, 2)
for m, q in bites(p):
    if not any(after(q, m2) in {(2, 1), (1,)} for m2, _ in bites(q)):
        ok = False
check(ok, "2 by 3: after the top-right bite, every answer lets Rose make the little corner or leave only the poison")
check(winning_bites(rect(2, 3)) == [(2, 3)], "2 by 3: the top-right bite is the only winning first bite")
p = after(rect(2, 4), (2, 4))
needs_step = [q for m, q in bites(p)
              if not any(after(q, m2) in {(2, 1), (1,)} and not win(after(q, m2)) for m2, _ in bites(q))]
check(len(needs_step) > 0, f"2 by 4 is where the little corner stops being enough: after {needs_step[0]} Rose needs a longer step")
check(not win(L(3, 3)) and win(L(3, 2)), "copy-cat board: an L with arms 3 and 3 is a second-player win; arms 3 and 2 a first-player win")

print("\nTrap boards inside the big board (lose for the player to move)")
traps = [p for p in boards_in_box(4, 6) if not win(p)]
for p in traps:
    print("      ", p)
named = [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), L(2, 2), L(3, 3), (2, 2, 1), (4, 2, 2), (3, 1, 1)]
check(all(not win(p) for p in named),
      "named trap boards lose for the mover: steps (2,1) to (6,5), equal Ls, (2,2,1), (4,2,2)")
check(len(cells_of(rect(4, 6))) == 24, "the big 4 by 6 board holds 24 cookies, poison included")

print()
if FAILS:
    print(f"{len(FAILS)} claim(s) FAILED")
    sys.exit(1)
print("All claims pass.")
