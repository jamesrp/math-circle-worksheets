"""Checks every answer in the K-1 design (Week 7, take-away games)."""
from games import (losing_piles, losing_table, winning_takes, multi_pile_lose,
                   multi_pile_winning_moves)

ok = True


def check(cond, msg):
    global ok
    print(("  ok   " if cond else "  FAIL ") + msg)
    ok = ok and cond


def first_or_second(S, n, misere=False):
    t = losing_table(S, n, misere)
    return "2nd" if t[n] else "1st"


print("K-1 Problem 1: take 1 or 2, piles 3, 4, 5")
expect = {3: ("2nd", []), 4: ("1st", [1]), 5: ("1st", [2])}
for n, (who, takes) in expect.items():
    got = (first_or_second((1, 2), n), winning_takes((1, 2), n))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")
check(not losing_table((1, 2), 2)[2] and losing_table((1, 2), 2)[0],
      "pile 4: the greedy take of 2 leaves 2, which the partner takes -> greedy loses")

print("K-1 Problem 2: take 1 or 2, piles 6, 7, 8")
expect = {6: ("2nd", []), 7: ("1st", [1]), 8: ("1st", [2])}
for n, (who, takes) in expect.items():
    got = (first_or_second((1, 2), n), winning_takes((1, 2), n))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")

print("K-1 Problem 3: partner starts from 6 (take 1 or 2); every partner move and the reply")


def reply_tree(S, n, depth=0):
    """n is a losing pile with the PARTNER to move. Enumerate every partner move and
    every winning reply; return True if a winning reply exists every time."""
    good = True
    for p in S:
        if p > n:
            continue
        after_partner = n - p
        if after_partner == 0:
            print("    " * depth + f"partner takes {p} from {n}: partner took the last counter!")
            return False
        replies = winning_takes(S, after_partner)
        print("    " * depth + f"partner takes {p} from {n} -> {after_partner} left; "
              f"you take {replies} -> {after_partner - replies[0]} left")
        good = good and len(replies) == 1
        if after_partner - replies[0] > 0:
            good = reply_tree(S, after_partner - replies[0], depth + 1) and good
    return good


check(reply_tree((1, 2), 6), "from 6, each of the 4 possible partner lines has exactly one "
      "winning reply (5 -> take 2, 4 -> take 1, then 2 -> take 2, 1 -> take 1)")

print("K-1 Problem 4: take 1 or 2, piles 1..12, which piles you do not want on your turn")
lp = losing_piles((1, 2), 1, 12)
check(lp == [3, 6, 9, 12], f"trap piles = {lp}")

print("K-1 Problem 5: take 1, 2, or 3, piles 3, 4, 5, 8")
expect = {3: ("1st", [3]), 4: ("2nd", []), 5: ("1st", [1]), 8: ("2nd", [])}
for n, (who, takes) in expect.items():
    got = (first_or_second((1, 2, 3), n), winning_takes((1, 2, 3), n))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")
check(losing_piles((1, 2, 3), 1, 12) == [4, 8, 12], "traps 1..12 under 1,2,3 are 4, 8, 12")

print("K-1 Problem 6: take 1 or 3, piles 1..10")
lp = losing_piles((1, 3), 1, 10)
check(lp == [2, 4, 6, 8, 10], f"trap piles = {lp}")

print("K-1 Problem 7: two rows, take 1 or 2 from one row")
R = ((1, 2), (1, 2))
for rows, who in [((2, 2), "2nd"), ((4, 4), "2nd"), ((4, 5), "1st")]:
    lose = multi_pile_lose(R, rows)
    wm = multi_pile_winning_moves(R, rows)
    desc = [f"take {s} from the row of {rows[i]}" for i, s in wm]
    check(("2nd" if lose else "1st") == who, f"rows {rows}: {who}; winning moves {desc}")


def mirror_always_wins(n, S=(1, 2)):
    """Second player copies the first player's move in the other row.
    Brute force over every first-player line: does the copier always take the last counter?"""
    def go(a, b):  # first player to move, a == b
        if a == 0 and b == 0:
            return True  # copier took the last counter
        for s in S:
            for (x, y) in ((a, b), (b, a)):
                if s <= x:
                    # first player takes s from a row of x; copier takes s from the other row of y==x
                    if not go(x - s, y - s):
                        return False
        return True
    return go(n, n)


for n in range(1, 11):
    assert mirror_always_wins(n)
check(True, "copying the partner's move in the other row wins for the 2nd player for equal rows 1..10")
check(set(multi_pile_winning_moves(R, (4, 5))) == {(1, 1), (0, 2)},
      "rows 4 and 5: the two winning first moves are take 1 from the 5-row (-> 4,4) "
      "and take 2 from the 4-row (-> 2,5)")

print("K-1 Problem 8: poison game (whoever takes the last counter LOSES), take 1 or 2")
expect = {3: ("1st", [2]), 4: ("2nd", []), 5: ("1st", [1]), 7: ("2nd", [])}
for n, (who, takes) in expect.items():
    got = (first_or_second((1, 2), n, misere=True), winning_takes((1, 2), n, misere=True))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")
check(losing_piles((1, 2), 1, 12, misere=True) == [1, 4, 7, 10],
      "poison-game traps 1..12 are 1, 4, 7, 10")

print("K-1 Problem 9: three rows, take 1 or 2 from one row")
R3 = ((1, 2),) * 3
for rows, who in [((1, 1, 1), "1st"), ((2, 2, 2), "1st"), ((3, 3, 3), "2nd")]:
    lose = multi_pile_lose(R3, rows)
    wm = multi_pile_winning_moves(R3, rows)
    check(("2nd" if lose else "1st") == who, f"rows {rows}: {who}; winning moves {wm}")
check(set(multi_pile_winning_moves(R3, (2, 2, 2))) == {(0, 2), (1, 2), (2, 2)},
      "rows 2,2,2: the only winning first moves take a whole row of 2")
check(winning_takes((1, 2), 2) == [2] and winning_takes((1, 2), 1) == [1]
      and multi_pile_lose(R3, (0, 3, 3)),
      "rows 3,3,3: whatever the 1st player takes from a row, the 2nd player takes the rest of "
      "that row (2 -> take 2, 1 -> take 1), leaving rows 3,3 (+ empty), which is losing")

print("\nALL K-1 CHECKS PASSED" if ok else "\nSOME K-1 CHECK FAILED")
raise SystemExit(0 if ok else 1)
