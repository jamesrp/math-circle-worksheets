"""Checks every answer in the grades 4-5 design (Week 7, take-away games),
plus the general claims from the activity outline that the 4-5 pages rely on."""
from itertools import combinations
from games import (losing_piles, losing_table, winning_takes, grundy_table, eventual_period,
                   multi_pile_lose, multi_pile_winning_moves)

ok = True


def check(cond, msg):
    global ok
    print(("  ok   " if cond else "  FAIL ") + msg)
    ok = ok and cond


A = (1, 3, 4)
BIG = 600

print("4-5 Problem 1: take 1 or 2, and take 1, 2, or 3; piles 1..20")
check(losing_piles((1, 2), 1, 20) == [3, 6, 9, 12, 15, 18], "1 or 2: 3, 6, 9, 12, 15, 18")
check(losing_piles((1, 2, 3), 1, 20) == [4, 8, 12, 16, 20], "1, 2, or 3: 4, 8, 12, 16, 20")
check(all(losing_table((1, 2), BIG)[n] == (n % 3 == 0) for n in range(BIG + 1)),
      f"1 or 2: losing exactly at multiples of 3 for every pile up to {BIG}")
check(all(losing_table((1, 2, 3), BIG)[n] == (n % 4 == 0) for n in range(BIG + 1)),
      f"1, 2, or 3: losing exactly at multiples of 4 for every pile up to {BIG}")
check(all(winning_takes((1, 2, 3), n) == [n % 4] for n in range(1, 101) if n % 4),
      "1, 2, or 3: from a non-multiple of 4 the ONLY winning take is the remainder (n mod 4)")

print("4-5 Problem 2: take 1, 3, or 4; piles 1..30")
lp = losing_piles(A, 1, 30)
check(lp == [2, 7, 9, 14, 16, 21, 23, 28, 30], f"losing piles 1..30: {lp}")
check(all(losing_table(A, BIG)[n] == (n % 7 in (0, 2)) for n in range(BIG + 1)),
      f"losing exactly when n mod 7 is 0 or 2, checked to {BIG}")

print("4-5 Problem 3: take 1, 3, or 4; piles 50, 53, 54, 56, 100 and why the pattern lasts")
for n, exp in [(50, [1]), (53, [4]), (54, [3]), (56, []), (100, [])]:
    got = winning_takes(A, n)
    check(got == exp, f"pile {n} (remainder {n % 7}): " +
          (f"go 1st, take {got}" if got else "go 2nd"))
# The remainder argument, checked residue by residue (valid for every pile size):
Lres = {0, 2}
arg = True
for r in range(7):
    after = {(r - s) % 7 for s in A}
    if r in Lres:
        arg &= not (after & Lres)          # every move leaves a non-losing remainder
    else:
        good = [s for s in A if (r - s) % 7 in Lres and s <= (r if r else 7)]
        arg &= bool(good)                   # some move, always available since pile >= r >= s
        print(f"    remainder {r}: take {good} to reach remainder {[(r - s) % 7 for s in good]}")
check(arg, "remainder argument: from remainders 0, 2 every move leaves 1,3,4,5,6; from each of "
      "1,3,4,5,6 some legal move reaches remainder 0 or 2 -> the pattern holds for ALL piles")

print("4-5 Problem 4: four more rules; piles 1..20")
cases = [((1, 4), [2, 5, 7, 10, 12, 15, 17, 20], (0, 5)),
         ((1, 4, 5), [2, 8, 10, 16, 18], (0, 8)),
         ((1, 2, 4), [3, 6, 9, 12, 15, 18], (0, 3)),
         ((1, 3, 5), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], (0, 2))]
for S, exp, per in cases:
    lp = losing_piles(S, 1, 20)
    ep = eventual_period(losing_table(S, BIG))
    check(lp == exp and ep == per, f"rule {S}: {lp}; repeats every {ep[1]} from the start")
add = {x: losing_piles((1, 2, x), 1, 200) == list(range(3, 201, 3)) for x in range(3, 31)}
check(all(add[x] == (x % 3 != 0) for x in add),
      "adding one move x (3..30) to 'take 1 or 2' keeps the multiples of 3 exactly when x is "
      "not a multiple of 3")
check(all(losing_table((1, 3, 5), BIG)[n] == (n % 2 == 0) for n in range(BIG + 1)),
      "1, 3, or 5: losing exactly at even piles (odd moves always change odd/even)")

print("4-5 Problem 5: find a rule (1 allowed) for each list, or show none exists")
N = 300
MAXMOVE = 14
targets = {
    "a: 2, 4, 6, 8, ... (every even pile)": lambda n: n % 2 == 0,
    "b: 5, 10, 15, 20, ...": lambda n: n % 5 == 0,
    "c: 3, 5, 8, 10, 13, 15, ...": lambda n: n % 5 in (0, 3),
    "d: 3, 7, 10, 14, 17, 21, 24, ...": lambda n: n % 7 in (0, 3),
}
sols = {k: [] for k in targets}
for k in range(0, MAXMOVE):
    for rest in combinations(range(2, MAXMOVE + 1), k):
        S = (1,) + rest
        t = losing_table(S, N)
        for name, f in targets.items():
            if all(t[n] == f(n) for n in range(N + 1)):
                sols[name].append(S)
for name in targets:
    s = sols[name]
    smallest = min(s, key=len) if s else None
    print(f"    {name}: {len(s)} rules with moves <= {MAXMOVE} work; smallest: {smallest}")
check(all(all(x % 2 == 1 for x in S) for S in sols["a: 2, 4, 6, 8, ... (every even pile)"])
      and len(sols["a: 2, 4, 6, 8, ... (every even pile)"]) == 2 ** 6,
      "a: a rule works exactly when every allowed move is odd (e.g. take 1 only, or 1 or 3)")
check(all({1, 2, 3, 4} <= set(S) and all(x % 5 for x in S) for S in sols["b: 5, 10, 15, 20, ..."])
      and (1, 2, 3, 4) in sols["b: 5, 10, 15, 20, ..."],
      "b: every working rule contains 1, 2, 3, 4 and no multiple of 5; 1,2,3,4 itself works")
check(sols["c: 3, 5, 8, 10, 13, 15, ..."] == [], "c: NO rule works (moves up to 14 all tried)")
check(all({1, 2, 6} <= set(S) and all(x % 7 not in (0, 3, 4) for x in S)
          for S in sols["d: 3, 7, 10, 14, 17, 21, 24, ..."])
      and (1, 2, 6) in sols["d: 3, 7, 10, 14, 17, 21, 24, ..."],
      "d: every working rule contains 1, 2, 6 and avoids remainders 0, 3, 4 (mod 7); "
      "1, 2, 6 itself works")
# the impossibility argument for c, step by step
check(5 - 3 == 2, "c: 3 and 5 are both on the list, so taking 2 cannot be allowed "
      "(it would lead from one losing pile to another)")
check(all(losing_table(S, 2)[2] for S in [(1,), (1, 3), (1, 4), (1, 3, 4, 7)]),
      "c: without the move 2, pile 2's only move is to 1, so 2 would be losing - but 2 is "
      "not on the list. Contradiction, for every rule.")
# a common wrong guess for d
check(losing_piles((1, 2, 3), 1, 20) != [n for n in range(1, 21) if n % 7 in (0, 3)]
      and losing_piles((1, 2, 6), 1, 40) == [n for n in range(1, 41) if n % 7 in (0, 3)],
      "d: 1,2,6 gives 3, 7, 10, 14, 17, 21, 24, 28, 31, 35, 38")

print("4-5 Problem 6: take 1, 6, or 9; piles 1..35")
lp = losing_piles((1, 6, 9), 1, 35)
check(lp == [2, 4, 7, 12, 14, 17, 19, 22, 24, 27, 29, 32, 34], f"losing piles 1..35: {lp}")
t = losing_table((1, 6, 9), 2000)
check(all(t[n] == (n % 5 in (2, 4) and n != 9) for n in range(1, 2001)),
      "for every pile 1..2000: losing exactly when the last digit is 2, 4, 7, or 9 - except 9")
check(eventual_period(t) == (10, 5), "pattern of losing piles settles to period 5 starting at pile 10")
check(winning_takes((1, 6, 9), 9) == [9], "9 is winning only because you can take all 9 at once")

print("4-5 Problem 7: can a rule's pattern never repeat?  (outline: always eventually periodic)")
worst = (0, None)
for k in range(1, 10):
    for rest in combinations(range(2, 11), k):
        S = (1,) + rest
        m = max(S)
        t = losing_table(S, 3000)
        # window argument: labels of n depend only on the m labels before n (n >= m),
        # so the first repeated m-window (within 2**m + 1 windows) forces periodicity.
        seen = {}
        rep = None
        for i in range(m, m + 2 ** m + 1):
            w = tuple(t[i - m:i])
            if w in seen:
                rep = (seen[w], i)
                break
            seen[w] = i
        assert rep is not None
        a, b = rep
        assert all(t[n] == t[n + (b - a)] for n in range(a, 3000 - (b - a))), S
        ep = eventual_period(t, 400)
        if ep[0] + ep[1] > worst[0]:
            worst = (ep[0] + ep[1], (S, ep))
check(True, "all 511 rules with 1 and moves up to 10: a window of the last (largest move) "
      "labels repeats within 2^(largest move)+1 steps, and from there the labels repeat forever")
print(f"    longest preperiod+period seen among them: {worst[1]}")
pre_examples = []
for k in range(1, 3):
    for rest in combinations(range(2, 13), k):
        S = (1,) + rest
        ep = eventual_period(losing_table(S, 1500), 500)
        if ep[0] > 0:
            pre_examples.append((S, ep))
print(f"    rules with 2 or 3 moves (<= 12) whose losing piles do NOT repeat from the start: "
      f"{pre_examples}")

print("4-5 Problem 8: two piles, take 1 or 2 from one pile; both piles 0..6")
R = ((1, 2), (1, 2))
cells = [(a, b) for a in range(7) for b in range(7) if multi_pile_lose(R, (a, b))]
check(all(multi_pile_lose(R, (a, b)) == (a % 3 == b % 3) for a in range(25) for b in range(25)),
      "losing exactly when both piles leave the same remainder on division by 3 (checked to 24)")
check(len(cells) == 17, f"17 losing squares in the 7x7 grid: {cells}")
print("  second player's answers from piles 2 and 5:")
allrep = True
for i in range(2):
    for s in (1, 2):
        pos = [2, 5]
        if s <= pos[i]:
            pos[i] -= s
            rep = multi_pile_winning_moves(R, tuple(pos))
            allrep &= bool(rep)
            print(f"    they take {s} from the pile of {[2, 5][i]} -> {tuple(pos)}; "
                  f"reply {[(f'take {t} from the pile of {pos[j]}') for j, t in rep]}")
check(allrep, "every first move from 2 and 5 has a reply that makes the remainders equal again")

print("4-5 Problem 9: two piles, take 1, 3, or 4 from one pile; both piles 0..7")
R = (A, A)
cells = [(a, b) for a in range(8) for b in range(8) if multi_pile_lose(R, (a, b))]
fam = {0: {0, 2, 7}, 1: {1, 3}, 2: {4, 6}, 3: {5}}
famof = {n: f for f, s in fam.items() for n in s}
check(all(multi_pile_lose(R, (a, b)) == (famof[a] == famof[b]) for a in range(8) for b in range(8)),
      "in the 8x8 grid, losing exactly when both piles are in the same family "
      "{0,2,7}, {1,3}, {4,6}, {5}")
check(len(cells) == 18, f"18 losing squares (13 up to swapping): {sorted({tuple(sorted(c)) for c in cells})}")
g = grundy_table(A, 40)
check(all(multi_pile_lose(R, (a, b)) == (g[a] == g[b]) for a in range(41) for b in range(41)),
      "brute force agrees with Sprague-Grundy: losing iff g(a) == g(b), checked to 40x40; "
      f"g(0..13) = {g[:14]}")
check(multi_pile_winning_moves(R, (4, 6)) == [], "piles 4 and 6: second player wins")
check(all(famof[n] == g[n] for n in range(8)),
      "the four families are exactly the piles with Grundy value 0, 1, 2, 3")
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

print("Outline claims")
check(eventual_period(losing_table((1, 3, 4), BIG)) == (0, 7), "{1,3,4}: period 7, losing at 0 and 2 mod 7")
gA = grundy_table((1, 2), 30)
gB = grundy_table((1, 3, 4), 30)
check(all(multi_pile_lose(((1, 2), (1, 3, 4)), (a, b)) == (gA[a] == gB[b])
          for a in range(31) for b in range(31)),
      "mixed sum (a pile under 1,2 and a pile under 1,3,4): losing iff the two Grundy values match")

print("\nALL 4-5 CHECKS PASSED" if ok else "\nSOME 4-5 CHECK FAILED")
raise SystemExit(0 if ok else 1)
