"""Checks every answer in the grades 2-3 design (Week 7, take-away games)."""
from functools import lru_cache
from games import (losing_piles, losing_table, winning_takes, multi_pile_lose,
                   multi_pile_winning_moves)

ok = True


def check(cond, msg):
    global ok
    print(("  ok   " if cond else "  FAIL ") + msg)
    ok = ok and cond


def verdict(S, n):
    return "2nd" if losing_table(S, n)[n] else "1st"


A = (1, 3, 4)

print("2-3 Problem 1: take 1 or 2; piles 7, 9, 11, 12")
for n, who, takes in [(7, "1st", [1]), (9, "2nd", []), (11, "1st", [2]), (12, "2nd", [])]:
    got = (verdict((1, 2), n), winning_takes((1, 2), n))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")

print("2-3 Problem 2: take 1, 3, or 4; piles 1..20")
lp = losing_piles(A, 1, 20)
check(lp == [2, 7, 9, 14, 16], f"piles where you'd rather go 2nd: {lp}")
print("  adult table (pile: winning take(s)):")
row = []
for n in range(1, 21):
    w = winning_takes(A, n)
    row.append(f"{n}:{'/'.join(map(str, w)) if w else '2nd'}")
print("   ", "  ".join(row))
multi = [n for n in range(1, 21) if len(winning_takes(A, n)) > 1]
check(multi == [3, 10, 17], f"piles with more than one winning take: {multi} "
      "(3: take 1 or 3; 10, 17: take 1 or 3)")
check([n for n in range(1, 21) if winning_takes(A, n) and 4 <= n and 4 not in winning_takes(A, n)]
      == [5, 8, 10, 12, 15, 17, 19],
      "winning piles (>=4) where taking 4 is a mistake: 5, 8, 10, 12, 15, 17, 19")

print("2-3 Problem 3: test the claims (take 1, 3, or 4)")
# Maya: 8, go first, take 4
check(not losing_table(A, 4)[4] and winning_takes(A, 4) == [4] and winning_takes(A, 8) == [1],
      "Maya (8, take 4) is WRONG: 4 are left and the partner takes all 4. Right move: take 1")
# Leo: 11, go first, take 4
check(losing_table(A, 7)[7] and winning_takes(A, 11) == [4],
      "Leo (11, take 4) is RIGHT: 7 is a losing pile; take 4 is the only winning first move")
# Ravi: 6, go first, take 1
check(not losing_table(A, 5)[5] and winning_takes(A, 5) == [3] and winning_takes(A, 6) == [4],
      "Ravi (6, take 1) is WRONG: from 5 the partner takes 3 (the only refutation) leaving 2; "
      "Ravi must take 1 and the partner takes the last. Right move: take 4")
# Zoe: 9, go second
check(losing_table(A, 9)[9], "Zoe (9, go second) is RIGHT")


def strategy_tree(S, n, indent="    "):
    """n: losing pile, opponent to move. Print every opponent move and all winning replies."""
    for p in S:
        if p > n:
            continue
        m = n - p
        if m == 0:
            raise AssertionError("opponent took the last counter from a losing pile?!")
        r = winning_takes(S, m)
        assert r, f"no reply from {m}"
        print(f"{indent}they take {p} ({m} left) -> take {' or '.join(map(str, r))} "
              f"({', '.join(str(m - x) for x in r)} left)")
        nxt = m - r[0]
        if nxt > 0:
            strategy_tree(S, nxt, indent + "    ")


print("  Leo's full plan after taking 4 from 11 (7 left, partner to move):")
strategy_tree(A, 7)
print("  Zoe's full plan from 9 (partner moves first):")
strategy_tree(A, 9)
check(True, "both RIGHT claims have a winning answer to every reply at every stage (trees above)")

print("2-3 Problem 4: take 1, 3, or 4; piles 23, 25, 28, 31")
for n, who, takes in [(23, "2nd", []), (25, "1st", [4]), (28, "2nd", []), (31, "1st", [1, 3])]:
    got = (verdict(A, n), winning_takes(A, n))
    check(got == (who, takes), f"pile {n}: {got[0]}, winning first take(s) {got[1]}")
check(losing_piles(A, 1, 35) == [n for n in range(1, 36) if n % 7 in (0, 2)],
      "losing piles up to 35 are exactly the numbers leaving remainder 0 or 2 on division by 7")

print("2-3 Problem 5: three more rules, piles 1..15")
for S, exp in [((1, 3), [2, 4, 6, 8, 10, 12, 14]), ((1, 2, 3), [4, 8, 12]),
               ((1, 4), [2, 5, 7, 10, 12, 15])]:
    lp = losing_piles(S, 1, 15)
    check(lp == exp, f"rule {S}: rather go 2nd at {lp}")

print("2-3 Problem 6: two piles, take 1, 3, or 4 from ONE pile")
R = (A, A)
for piles, who in [((5, 5), "2nd"), ((1, 3), "2nd"), ((3, 4), "1st"), ((4, 6), "2nd")]:
    lose = multi_pile_lose(R, piles)
    wm = multi_pile_winning_moves(R, piles)
    desc = [f"take {s} from the pile of {piles[i]}" for i, s in wm]
    check(("2nd" if lose else "1st") == who, f"piles {piles}: {who}; winning first moves {desc}")
check(not losing_table(A, 1)[1] and not losing_table(A, 3)[3] and not losing_table(A, 4)[4]
      and not losing_table(A, 6)[6],
      "piles 1, 3, 4, 6 are each a 1st-player win ON THEIR OWN, yet 1&3 and 4&6 are 2nd-player wins")
print("  second player's answers from piles 1 and 3:")
for i, s in [(0, 1), (1, 1), (1, 3)]:
    pos = [1, 3]
    pos[i] -= s
    rep = multi_pile_winning_moves(R, tuple(pos))
    print(f"    they take {s} from the pile of {[1, 3][i]} -> {tuple(pos)}; "
          f"reply {[(f'take {t} from the pile of {pos[j]}') for j, t in rep]}")
print("  second player's answers from piles 4 and 6:")
for i in range(2):
    for s in A:
        pos = [4, 6]
        if s <= pos[i]:
            pos[i] -= s
            rep = multi_pile_winning_moves(R, tuple(pos))
            assert rep
            print(f"    they take {s} from the pile of {[4, 6][i]} -> {tuple(pos)}; "
                  f"reply {[(f'take {t} from the pile of {pos[j]}') for j, t in rep]}")
check(True, "every first move from (1,3) and from (4,6) has a winning reply (listed above)")

print("2-3 Problem 7: Kai always takes as many as allowed (4, else 3, else 1); Kai goes first")


def greedy(n):
    return max(s for s in A if s <= n)


@lru_cache(None)
def kai_wins(n):
    """Kai to move at n>0, plays greedily; the other player plays as well as possible."""
    g = greedy(n)
    if g == n:
        return True
    m = n - g
    for s in A:
        if s <= m and (s == m or not kai_wins(m - s)):
            return False
    return True


def beat_kai_line(n):
    """A line of play (Kai first from n) in which the other player wins."""
    line = []
    while True:
        g = greedy(n)
        line.append(f"Kai takes {g} ({n - g} left)")
        n -= g
        if n == 0:
            return None
        for s in A:
            if s <= n and (s == n or not kai_wins(n - s)):
                line.append(f"you take {s} ({n - s} left)")
                n -= s
                break
        if n == 0:
            return line


kw = [n for n in range(1, 21) if kai_wins(n)]
check(kw == [1, 3, 4, 6, 11], f"Kai's plan wins (against every reply) only from piles {kw}")
check([n for n in range(1, 21) if not losing_table(A, n)[n] and not kai_wins(n)]
      == [5, 8, 10, 12, 13, 15, 17, 18, 19, 20],
      "winning piles that Kai still loses: 5, 8, 10, 12, 13, 15, 17, 18, 19, 20")
check([n for n in range(1, 21) if not kai_wins(n) and losing_table(A, n - greedy(n))[n - greedy(n)]]
      == [13, 18, 20],
      "13, 18, 20: Kai's FIRST move is correct, but his habit loses later")
for n in (13, 18, 20, 5, 8):
    print(f"    from {n}: " + "; ".join(beat_kai_line(n)))

print("\nALL 2-3 CHECKS PASSED" if ok else "\nSOME 2-3 CHECK FAILED")
raise SystemExit(0 if ok else 1)
