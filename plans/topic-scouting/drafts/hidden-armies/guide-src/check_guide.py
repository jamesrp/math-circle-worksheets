"""Recompute every answer printed in the Hidden armies facilitator guide.

Independent of the pages' check_answers.py.  Keyed to the FINAL student PDFs:
K-1 (6 pp., P1-P7), grades 2-3 (5 pp., P1-P7), grades 4-5 (6 pp., P1-P8).

Game: a plan is an ordered triple (hill 1, hill 2, hill 3) of whole numbers.
A hill goes to the larger number, an equal hill to nobody; more hills wins.
Run: python3 check_guide.py   (prints values used in the guide; exits 1 on any failure)
"""
import itertools
import sys
from math import comb

FAIL = []


def ok(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def plans(n):
    return [(a, b, n - a - b) for a in range(n, -1, -1) for b in range(n - a, -1, -1)]


def res(p, q):
    w = sum(x > y for x, y in zip(p, q))
    l = sum(x < y for x, y in zip(p, q))
    return (w > l) - (w < l)


def beats(p, q):
    return res(p, q) == 1


def beaters(q, n=None):
    n = sum(q) if n is None else n
    return [p for p in plans(n) if beats(p, q)]


def s(p):
    return "-".join(map(str, p))


def ls(L):
    return ", ".join(s(p) for p in L)


def fewest(q):
    m = 0
    while not any(beats(p, q) for p in plans(m)):
        m += 1
    return m


def formula(q):
    a, b, c = sorted(q, reverse=True)
    return b + c + 2


def counter(q):
    """One more than q on each of the two smaller hills, the rest on the biggest."""
    big = max(range(3), key=lambda i: (q[i], -i))
    p = [q[i] + 1 for i in range(3)]
    p[big] = sum(q) - sum(p[i] for i in range(3) if i != big)
    return tuple(p)


def typ(p):
    return tuple(sorted(p, reverse=True))


print("=== Overview facts ===")
ok(len(plans(5)) == 21 == comb(7, 2) and len(plans(6)) == 28 == comb(8, 2), "21 plans with 5 cubes, 28 with 6")
# equal armies: a game is a tie exactly when some hill is equal; 3-0 never happens
for n in range(0, 13):
    P = plans(n)
    good = all((res(p, q) == 0) == any(x == y for x, y in zip(p, q)) for p in P for q in P)
    no30 = all(not all(x > y for x, y in zip(p, q)) for p in P for q in P)
    if not (good and no30):
        ok(False, f"N={n}: tie iff some equal hill / no 3-0")
ok(True, "N=0..12: with equal armies a game ties exactly when some hill is equal; no 3-0 wins")
# Theorem 1: fewest cubes = b + c + 2 for every plan with at least one cube
allgood = all(fewest(q) == formula(q) for n in range(1, 13) for q in plans(n))
ok(allgood, "fewest cubes that beat q = (two smaller hills) + 2, every q with 1..12 cubes")
ok(fewest((0, 0, 0)) == 1, "exception: 0-0-0 is beaten by 1 cube")
# extra cubes never hurt: if p beats q, adding a cube anywhere to p still beats q
ok(all(beats(tuple(p[j] + (j == i) for j in range(3)), q)
       for n in range(0, 9) for q in plans(n) for m in range(0, 10) for p in plans(m) if beats(p, q)
       for i in range(3)), "adding a cube to a winning plan never spoils the win (checked to 9 vs 8)")
# Corollary: beatable with equal army iff biggest hill >= 2; unbeaten plans by N
for n in range(0, 16):
    unb = [p for p in plans(n) if not beaters(p)]
    ok(set(unb) == {p for p in plans(n) if max(p) <= 1}, f"N={n}: unbeaten = plans with no hill above 1: {ls(unb) or 'none'}")
ok(all(beats(counter(q), q) and sum(counter(q)) == sum(q) for n in range(4, 31) for q in plans(n)),
   "counter-plan rule beats every plan, N=4..30")
# 6-cube landscape
P6 = plans(6)
B = {p: sum(beats(p, q) for q in P6) for p in P6}
L = {p: sum(beats(q, p) for q in P6) for p in P6}
T = {p: sum(res(p, q) == 0 for q in P6) for p in P6}
ok(all(T[p] == 13 for p in P6), "every 6-cube plan ties exactly 13 of the 28 (itself included)")
ok(all(B[p] + L[p] == 15 for p in P6), "beats + beaten-by = 15 for every 6-cube plan")
types6 = [(6, 0, 0), (5, 1, 0), (4, 2, 0), (4, 1, 1), (3, 3, 0), (3, 2, 1), (2, 2, 2)]
for t in types6:
    arr = sorted(set(itertools.permutations(t)), reverse=True)
    ok(len({B[p] for p in arr}) == 1, f"type {s(t)}: {len(arr)} arrangements, each beats {B[t]}, beaten by {L[t]}")
ok(sum(B.values()) == 210, f"sum of all 28 counts = {sum(B.values())}")
ok([B[t] for t in types6] == [0, 5, 8, 9, 9, 11, 12], "counts 0,5,8,9,9,11,12")
ok(all(res(tuple(p[i] for i in perm), tuple(q[i] for i in perm)) == res(p, q)
       for p in P6 for q in P6 for perm in itertools.permutations(range(3))),
   "rearranging the hills of both plans never changes a result")
# circles
cyc = set()
for a, b, c in itertools.permutations(P6, 3):
    if beats(a, b) and beats(b, c) and beats(c, a):
        cyc.add(min((a, b, c), (b, c, a), (c, a, b)))
on = {x for cy in cyc for x in cy}
ok(len(cyc) == 180, f"{len(cyc)} circles of three plans with 6 cubes")
ok(on == set(P6) - {(6, 0, 0), (0, 6, 0), (0, 0, 6)}, "every 6-cube plan except 6-0-0, 0-6-0, 0-0-6 lies on a circle")
w222 = [cy for cy in cyc if (2, 2, 2) in cy]
ok(len(w222) == 12, f"{len(w222)} circles contain 2-2-2")
# in each, the plan before 2-2-2 (the one that beats it) is an arrangement of 3-3-0
pre = set()
for cy in w222:
    i = cy.index((2, 2, 2))
    pre.add(typ(cy[(i - 1) % 3]))
ok(pre == {(3, 3, 0)}, "in every circle through 2-2-2 the plan that beats 2-2-2 is an arrangement of 3-3-0")
ok(beats((0, 1, 5), (2, 0, 4)) and beats((2, 0, 4), (1, 2, 3)) and beats((1, 2, 3), (0, 1, 5)),
   "outline circle 0-1-5 -> 2-0-4 -> 1-2-3 -> 0-1-5")
c1 = [(0, 2, 4), (3, 1, 2), (1, 5, 0)]
c2 = [(2, 2, 2), (4, 1, 1), (3, 3, 0)]
for cy in (c1, c2):
    ok(all(beats(cy[i], cy[(i + 1) % 3]) for i in range(3)), f"circle {' -> '.join(s(p) for p in cy)}")
ok({typ(p) for p in c1 + c2} == set(types6) - {(6, 0, 0)}, "these two circles meet all six other types")
# rearranging hills of a whole circle gives a circle
ok(all(all(beats(tuple(cy[k][i] for i in perm), tuple(cy[(k + 1) % 3][i] for i in perm)) for k in range(3))
       for cy in cyc for perm in itertools.permutations(range(3))), "relabelling the hills of a circle gives a circle")
# 6-0-0 beats nothing; 15 plans beat it
ok(B[(6, 0, 0)] == 0 and L[(6, 0, 0)] == 15, "6-0-0 beats none and is beaten by 15")
# mixed plans (4-5 P8)
ben = [(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]
mia = [(4, 2, 0), (4, 0, 2), (2, 4, 0), (2, 0, 4), (0, 4, 2), (0, 2, 4)]


def wl(q, Lst):
    return sum(beats(q, x) for x in Lst), sum(beats(x, q) for x in Lst)


print("     vs Ben (wins, losses) by type:", {s(t): wl(t, ben) for t in types6})
print("     vs Mia (wins, losses) by type:", {s(t): wl(t, mia) for t in types6})
ok(all(len({wl(p, ben) for p in set(itertools.permutations(t))}) == 1 and
       len({wl(p, mia) for p in set(itertools.permutations(t))}) == 1 for t in types6),
   "a plan's score against Ben or Mia depends only on its type (so 7 tests suffice)")
exb = [q for q in P6 if wl(q, ben)[0] > wl(q, ben)[1]]
ok(sorted(exb) == sorted([(3, 3, 0), (3, 0, 3), (0, 3, 3)]) and all(wl(q, ben) == (2, 0) for q in exb),
   f"plans that beat more of Ben's than they lose to: {ls(exb)} (2 wins, 0 losses each)")
ok(all(wl(q, mia)[0] <= wl(q, mia)[1] for q in P6), "no 6-cube plan beats more of Mia's plans than it loses to")
evenmia = sorted({typ(q) for q in P6 if wl(q, mia)[0] == wl(q, mia)[1]}, reverse=True)
print("     types that break even against Mia:", ls(evenmia))
ok(all(res(p, q) == -res(q, p) for p in P6 for q in P6), "the game is symmetric (antisymmetric score)")

print("\n=== Launch (7 cubes each, so no launch plan, even rearranged, appears on any page) ===")
# Every plan printed on a page, as a type.  7-cube plans appear only as 3-2-2 and 1-1-5 (2-3 P3, 4-5 P2).
page_plans = [(5, 0, 0), (0, 4, 1), (0, 3, 2), (2, 1, 2), (1, 4, 0), (1, 3, 1), (2, 2, 1), (1, 1, 1), (3, 1, 1),
              (4, 0, 1), (4, 1, 0), (0, 0, 5), (0, 1, 4), (2, 0, 3), (1, 2, 2), (1, 0, 4), (2, 3, 0),
              (2, 2, 2), (1, 4, 1), (3, 0, 3), (0, 1, 5), (3, 2, 2), (1, 1, 5), (4, 4, 2), (2, 5, 3), (7, 7, 6),
              (6, 0, 0), (4, 1, 1), (3, 2, 1), (3, 3, 0), (8, 1, 1), (5, 3, 2), (3, 3, 3), (1, 8, 1),
              (34, 33, 33), (50, 0, 50), (40, 30, 30), (3, 0, 2)] + plans(6) + ben + mia
page_types = {typ(p) for p in page_plans}
k1_task_types = {typ(p) for p in [(5, 0, 0), (0, 4, 1), (0, 3, 2), (2, 1, 2), (1, 4, 0), (1, 3, 1), (2, 2, 1),
                                  (3, 1, 1), (4, 0, 1)]}
ok(k1_task_types == {typ(p) for p in plans(5)}, "all five 5-cube types are plans K-1 is asked to beat (so the launch avoids 5)")
A1, B1 = (5, 0, 2), (4, 3, 0)
A2, B2 = (2, 5, 0), (2, 0, 5)
for p in (A1, B1, A2, B2):
    ok(sum(p) == 7 and typ(p) not in page_types, f"launch plan {s(p)}: 7 cubes, type {s(typ(p))} on no page")
ok(res(A1, B1) == 1, "game 1: 5-0-2 beats 4-3-0 (A wins hills 1 and 3, B wins hill 2)")
ok([i + 1 for i in range(3) if A1[i] > B1[i]] == [1, 3] and [i + 1 for i in range(3) if B1[i] > A1[i]] == [2],
   "game 1 tokens: A on hills 1 and 3, B on hill 2")
ok(A1 != counter(B1) and B2 != counter(A1), "launch plans are not the counter-plan pattern")
ok(max(range(3), key=lambda i: B1[i]) == 0 and A1[0] > B1[0], "game 1 winner takes the loser's biggest hill, unlike the counter-plan")
ok(res(B2, A1) == 0, "game 2: B's 2-0-5 would only have tied A's old 5-0-2 (it shows no way to win)")
ok(res(A2, B2) == 0 and A2[0] == B2[0] and A2[1] > B2[1] and B2[2] > A2[2],
   "game 2: 2-5-0 vs 2-0-5 ties; hill 1 equal, A wins hill 2, B wins hill 3")
# reviewer's alternative 2-3-2 is a type a page asks to beat (3-2-2), so 2-0-5 is used
ok(typ((2, 3, 2)) in page_types, "2-3-2 (type 3-2-2) is on a page, so the launch does not use it")

print("\n=== K-1 ===")
for t in [(5, 0, 0), (4, 1, 0), (3, 2, 0), (3, 1, 1), (2, 2, 1)]:
    print(f"     5 cubes, type {s(t)}: beaten by {len(beaters(t))} of 21")
ok(len(beaters((2, 2, 1))) == 2 and ls(beaters((2, 2, 1))) == "3-0-2, 0-3-2", "2-2-1 beaten only by 3-0-2, 0-3-2")
ok([p for p in plans(5) if not beaters(p)] == [], "P2: no 5-cube plan is unbeatable")
for q in [(5, 0, 0), (0, 4, 1), (0, 3, 2), (2, 1, 2)]:
    b = beaters(q)
    print(f"     P3 {s(q)}: {len(b)} beaters: {ls(b)}; counter rule gives {s(counter(q))}")
    ok(beats(counter(q), q), f"P3 counter for {s(q)}")
ok(len(beaters((5, 0, 0))) == 10 and len(beaters((0, 4, 1))) == 6 and len(beaters((0, 3, 2))) == 4
   and ls(beaters((2, 1, 2))) == "3-2-0, 0-2-3", "P3 counts 10, 6, 4, 2")
ok(set(p for p in plans(2) if not beaters(p)) == {(1, 1, 0), (1, 0, 1), (0, 1, 1)}, "P4 2 cubes: 1-1-0, 1-0-1, 0-1-1")
ok([p for p in plans(3) if not beaters(p)] == [(1, 1, 1)], "P4 3 cubes: 1-1-1 only")
ok([p for p in plans(4) if not beaters(p)] == [], "P4 4 cubes: none")
ok(ls(beaters((2, 1, 1))) == "0-2-2" and ls(beaters((1, 1, 2))) == "2-2-0", "P4 2-1-1 beaten only by 0-2-2; 1-1-2 only by 2-2-0")
for t in [(4, 0, 0), (3, 1, 0), (2, 2, 0), (2, 1, 1)]:
    print(f"     4 cubes, type {s(t)}: beaten by {len(beaters(t))} of 15")
# P5 as printed: box 1 columns 4-1-0 | 2-2-1 | 0-0-5, box 2 columns 0-1-4 | 2-0-3 | 1-2-2; rows (L,M), (M,R), (L,R)
for A, Bm, C in [((4, 1, 0), (2, 2, 1), (0, 0, 5)), ((0, 1, 4), (2, 0, 3), (1, 2, 2))]:
    rows = [(A, Bm), (Bm, C), (A, C)]
    win = [s(x) if res(x, y) == 1 else s(y) if res(x, y) == -1 else "tie" for x, y in rows]
    print(f"     P5 box {s(A)}/{s(Bm)}/{s(C)}: row winners {win}")
ok(beats((2, 2, 1), (4, 1, 0)) and beats((2, 2, 1), (0, 0, 5)) and beats((4, 1, 0), (0, 0, 5)), "P5 box 1: 2-2-1 best")
ok(beats((0, 1, 4), (2, 0, 3)) and beats((2, 0, 3), (1, 2, 2)) and beats((1, 2, 2), (0, 1, 4)), "P5 box 2: circle")
for q, m in [((5, 0, 0), 2), ((1, 4, 0), 3), ((1, 3, 1), 4), ((2, 2, 1), 5), ((1, 1, 1), 4)]:
    best = [p for p in plans(m) if beats(p, q)]
    ok(fewest(q) == m, f"P6 {s(q)}: fewest {m}; all {m}-cube winners: {ls(best)}")
for q, n, boards in [((3, 1, 1), 3, 4), ((4, 0, 1), 6, 8)]:
    b = beaters(q)
    ok(len(b) == n, f"P7 {s(q)}: exactly {n} beaters ({boards} boards printed): {ls(b)}")

print("\n=== Grades 2-3 ===")
for q in [(2, 2, 2), (1, 4, 1), (3, 0, 3), (0, 1, 5), (3, 2, 2), (1, 1, 5), (4, 4, 2), (2, 5, 3), (7, 7, 6)]:
    c = counter(q)
    ok(beats(c, q) and sum(c) == sum(q), f"P3 {s(q)} ({sum(q)} cubes): counter {s(c)}")
ok([p for p in plans(3) if not beaters(p)] == [(1, 1, 1)] and not [p for p in plans(4) if not beaters(p)],
   "P4: 1-1-1; none with 4 cubes")
ok(all(res(p, (1, 1, 1)) <= 0 for p in plans(3)), "P4: no 3-cube plan beats 1-1-1")
print("     P4 1-1-1 vs each 3-cube plan:", {s(p): res((1, 1, 1), p) for p in plans(3)})
ok(beats((2, 2, 2), (4, 1, 1)) and beats((4, 1, 1), (3, 3, 0)) and beats((3, 3, 0), (2, 2, 2)),
   "P5 printed order top->right->left: 2-2-2 -> 4-1-1 -> 3-3-0")
ok(not any((6, 0, 0) in cy for cy in cyc), "P5 no circle through 6-0-0")
ok(sorted(beaters((2, 2, 2))) == sorted([(3, 3, 0), (3, 0, 3), (0, 3, 3)]), "P6 beaters of 2-2-2: 3-3-0, 3-0-3, 0-3-3")
b600 = beaters((6, 0, 0))
ok(len(b600) == 15 and set(b600) == {p for p in P6 if p[1] >= 1 and p[2] >= 1}, f"P6 beaters of 6-0-0 (15): {ls(b600)}")
for q, m in [((6, 0, 0), 2), ((4, 1, 1), 4), ((3, 2, 1), 5), ((2, 2, 2), 6), ((3, 3, 0), 5), ((1, 1, 1), 4),
             ((8, 1, 1), 4), ((5, 3, 2), 7)]:
    ex = counter(q) if False else None
    a, b, c = sorted(q, reverse=True)
    ok(fewest(q) == m == formula(q), f"P7 {s(q)}: fewest {m}")
examples = {(6, 0, 0): (0, 1, 1), (4, 1, 1): (0, 2, 2), (3, 2, 1): (0, 3, 2), (2, 2, 2): (3, 3, 0), (3, 3, 0): (4, 0, 1),
            (1, 1, 1): (2, 2, 0), (8, 1, 1): (0, 2, 2), (5, 3, 2): (0, 4, 3)}
for q, p in examples.items():
    ok(beats(p, q) and sum(p) == fewest(q), f"P7 example: {s(p)} beats {s(q)} with {sum(p)} cubes")

print("\n=== Grades 4-5 ===")
for q in [(2, 2, 2), (1, 4, 1), (3, 2, 2), (1, 1, 5), (3, 3, 3), (1, 8, 1), (7, 7, 6), (34, 33, 33), (50, 0, 50)]:
    c = counter(q)
    ok(beats(c, q) and sum(c) == sum(q), f"P2 {s(q)} ({sum(q)} cubes): counter {s(c)}")
ok(beats((48, 1, 51), (50, 0, 50)) and beats((32, 34, 34), (34, 33, 33)), "P2 48-1-51 and 32-34-34")
ok(beats((0, 1, 99), (50, 0, 50)), "P2 0-1-99 also beats 50-0-50")
ok([q for q in P6 if fewest(q) == 6] == [(2, 2, 2)] and max(fewest(q) for q in P6) == 6, "2-2-2 is the 6-cube plan that needs the most cubes to beat (6)")
# P6
for q, m in [((6, 0, 0), 2), ((4, 1, 1), 4), ((3, 2, 1), 5), ((2, 2, 2), 6), ((1, 1, 1), 4)]:
    ok(fewest(q) == m, f"P6 {s(q)}: fewest {m}")
ok(beats((0, 31, 31), (40, 30, 30)), "P6 0-31-31 beats 40-30-30")
ok(not any(beats(p, (40, 30, 30)) for p in plans(61)), "P6 no 61-cube plan beats 40-30-30")
# P7: partner has 6 cubes


def safe(p):
    return not any(beats(q, p) for q in P6)


def always(p):
    return all(beats(p, q) for q in P6)


ms = min(m for m in range(15) if any(safe(p) for p in plans(m)))
ma = min(m for m in range(15) if any(always(p) for p in plans(m)))
ok(ms == 8 and sorted(p for p in plans(8) if safe(p)) == sorted(set(itertools.permutations((3, 3, 2)))),
   "P7 fewest for a plan no 6-cube plan beats: 8, exactly the arrangements of 3-3-2")
ok(ma == 9 and [p for p in plans(9) if always(p)] == [(3, 3, 3)], "P7 fewest for a plan beating every 6-cube plan: 9, only 3-3-3")
# the attack on any 8-cube plan: one more than its smallest hill, the rest on its middle hill
for p in plans(8):
    x = sorted(range(3), key=lambda i: p[i])
    q = [0, 0, 0]
    q[x[0]] = p[x[0]] + 1
    q[x[1]] = 6 - q[x[0]]
    ok_q = q[x[1]] >= 0 and res(tuple(p), tuple(q)) <= 0
    if not ok_q:
        ok(False, f"P7 attack fails on {s(p)}")
ok(True, "P7 every 8-cube plan is held to a tie or loss by: smallest hill + 1, the rest on its middle hill")
# P7 also holds if the partner may use fewer than 6
ok(all(not any(beats(q, p) for m in range(7) for q in plans(m)) for p in set(itertools.permutations((3, 3, 2)))),
   "P7 3-3-2 also safe against partners with fewer than 6")
# P4 summary already above; P5 example cycle for each type
for t in types6[1:]:
    cy = next(cy for cy in sorted(cyc) if t in cy)
    print(f"     P5 a circle through {s(t)}: {' -> '.join(s(p) for p in cy)}")

print("\n=== Extra facts cited in the guide ===")
ok(ls(beaters((2, 1, 2))) == "3-2-0, 0-2-3" and ls(beaters((1, 2, 2))) == "2-3-0, 2-0-3",
   "2-1-2 loses only to 3-2-0, 0-2-3; 1-2-2 only to 2-3-0, 2-0-3")
ties6 = sum(res(p, q) == 0 for p in P6 for q in P6)
ok(ties6 == 364, f"6 cubes: {ties6} of 784 ordered pairings tie ({ties6 / 784:.0%})")
tied_distinct = sum(res(p, q) == 0 for p, q in itertools.combinations(P6, 2))
ok(tied_distinct == 168 and comb(28, 2) == 378, f"{tied_distinct} of 378 pairs of different 6-cube plans tie")
ok(all(res((2, 0, 0), q) <= 0 and res((0, 2, 0), q) <= 0 for q in [(1, 1, 0)]), "2-0-0 / 0-2-0 cannot beat 1-1-0")
# the 4-5 P7 attack defeats every plan with at most 9 cubes except 3-3-3
bad = []
for m in range(0, 10):
    for p in plans(m):
        if p == (3, 3, 3):
            continue
        x = sorted(range(3), key=lambda i: p[i])
        q = [0, 0, 0]
        q[x[0]] = p[x[0]] + 1
        q[x[1]] = 6 - q[x[0]]
        if q[x[1]] < 0 or res(p, tuple(q)) == 1:
            bad.append(p)
ok(not bad, "P7 attack (one more than the smallest hill, rest on the middle hill) stops every plan of <= 9 cubes but 3-3-3")
ok(all(beats((3, 3, 3), q) for q in P6), "3-3-3 beats every 6-cube plan")
ok(all(res((2, 2, 2), x) == 0 for x in ben + mia), "2-2-2 ties all of Ben's and all of Mia's plans")
ok(len(set(itertools.permutations((3, 3, 0)))) == 3 and min(L.values()) == 3 and
   [p for p in P6 if L[p] == 3] == [(2, 2, 2)], "2-2-2 is the 6-cube plan beaten by fewest (3)")
print("     6-cube plans beaten by 4:", ls([p for p in P6 if L[p] == 4]))


print("\n=== Added at revision (GUIDE-REVISE) ===")
# Theorem 3 tie count: every plan with N cubes ties exactly 2N+1 plans (itself included), proved by inclusion-exclusion
for n in range(0, 13):
    P = plans(n)
    for p in P:
        t_ = sum(res(p, q) == 0 for q in P)
        singles = [sum(q[i] == p[i] for q in P) for i in range(3)]
        if not (t_ == 2 * n + 1 and singles == [n + 1 - p[i] for i in range(3)] and sum(singles) == 2 * n + 3
                and all(sum(q[i] == p[i] and q[j] == p[j] for q in P) == 1 for i in range(3) for j in range(i + 1, 3))):
            ok(False, f"tie count for {s(p)}")
    nb = {p: sum(beats(p, q) for q in P) + sum(beats(q, p) for q in P) for p in P}
    if any(v != n * (n - 1) // 2 for v in nb.values()):
        ok(False, f"N={n}: beats + beaten-by = N(N-1)/2")
ok(True, "N=0..12: every plan ties exactly 2N+1 plans (13 of 28 for N=6); N+1-p_i plans match it on hill i; "
         "beats + beaten-by = N(N-1)/2 (15 for N=6)")
# circles counted once each
ordered = sum(1 for a, b, c in itertools.permutations(P6, 3) if beats(a, b) and beats(b, c) and beats(c, a))
ok(ordered == 540 == 3 * len(cyc), f"{len(cyc)} circles counted once each ({ordered} if counted once per starting plan)")
# Mia's die: at least an even score on average against every plan, and better than even against 6-0-0
mia_avg = {q: sum(res(m, q) for m in mia) for q in P6}
ok(all(v >= 0 for v in mia_avg.values()), "Mia's die: average score >= 0 against every 6-cube plan")
ok(mia_avg[(6, 0, 0)] == 2 and [s(q) for q in P6 if mia_avg[q] > 0] == ["6-0-0", "0-6-0", "0-0-6"],
   "Mia's die wins on average only against 6-0-0, 0-6-0, 0-0-6 (2 wins, 0 losses in six)")
ben_vs330 = [res((3, 3, 0), b) for b in ben]
ok(sorted(ben_vs330) == [0, 0, 0, 0, 1, 1], "3-3-0 beats two of Ben's six plans and ties four")
# 4-5 P7, proof for 9: in any plan of at most 9 cubes except 3-3-3 the two smaller hills total at most 5,
# because a total of 6 or more forces the biggest hill to be at least 3, hence 9 cubes as 3-3-3
ok(all(sum(sorted(p)[:2]) <= 5 for m in range(10) for p in plans(m) if p != (3, 3, 3)),
   "4-5 P7: every plan of <= 9 cubes other than 3-3-3 has its two smaller hills totalling <= 5")
ok([p for m in range(10) for p in plans(m) if sum(sorted(p)[:2]) >= 6] == [(3, 3, 3)],
   "4-5 P7: 3-3-3 is the only plan of <= 9 cubes whose two smaller hills total 6 or more")
# K-1 P7, reason for 3-1-1: winning hill 1 costs 4 and leaves 1 cube; winning one hill and tying two costs 6
P5 = plans(5)
ok(not any(beats(p, (3, 1, 1)) for p in P5 if p[0] >= 4), "K-1 P7: no 5-cube plan that wins hill 1 of 3-1-1 beats it")
ok(3 + 1 + 1 + 1 == 6 > 5, "K-1 P7: winning one hill of 3-1-1 and tying two costs at least 6")
ok(all(p[1] >= 2 and p[2] >= 2 for p in beaters((3, 1, 1))) and
   sorted(beaters((3, 1, 1))) == sorted(p for p in P5 if p[1] >= 2 and p[2] >= 2),
   "K-1 P7: the beaters of 3-1-1 are exactly the 5-cube plans with >= 2 on hills 2 and 3")
ok(not any(beats(p, (4, 0, 1)) for p in P5 if p[0] >= 5) and
   sorted(beaters((4, 0, 1))) == sorted(p for p in P5 if p[1] >= 1 and p[2] >= 2),
   "K-1 P7: the beaters of 4-0-1 are exactly the 5-cube plans with >= 1 on hill 2 and >= 2 on hill 3")
# Grades 4-5 continuation: with h hills (same rules), a plan nobody can beat exists exactly when N <= h


def plans_h(n, h):
    if h == 1:
        return [(n,)]
    return [(a,) + r for a in range(n, -1, -1) for r in plans_h(n - a, h - 1)]


def res_h(p, q):
    w = sum(x > y for x, y in zip(p, q))
    l = sum(x < y for x, y in zip(p, q))
    return (w > l) - (w < l)


def counter_h(q):
    """Give up the biggest hill; one more on two other hills; match the rest; spare cubes on the biggest hill."""
    h = len(q)
    big = max(range(h), key=lambda i: (q[i], -i))
    others = [i for i in range(h) if i != big]
    p = list(q)
    p[others[0]] += 1
    p[others[1]] += 1
    p[big] = sum(q) - sum(p[i] for i in others)
    return tuple(p)


for h, top in [(3, 15), (4, 12), (5, 10)]:
    for n in range(0, top + 1):
        P = plans_h(n, h)
        unb = [p for p in P if not any(res_h(q, p) == 1 for q in P)]
        if bool(unb) != (n <= h) or set(unb) != {p for p in P if max(p, default=0) <= 1}:
            ok(False, f"{h} hills, {n} cubes: unbeatable plans")
        for q in P:
            if max(q) >= 2:
                c = counter_h(q)
                if not (min(c) >= 0 and sum(c) == n and res_h(c, q) == 1 and sum(c) - c[q.index(max(q))] == n - max(q) + 2):
                    ok(False, f"{h} hills: counter fails on {q}")
    ok(True, f"{h} hills, 0..{top} cubes: a plan nobody can beat exists exactly when cubes <= hills "
             f"(the plans with no hill above 1); the counter-plan costs N - a + 2 and beats every plan with a hill of 2+")
# Materials counts for the current group (4 K-1, 4 Grades 2-3, 3 Grades 4-5; two launch adults)
mats = 4 + 4 + 3 + 2
sheets = sum(-(-k // 2) for k in (4, 4, 3)) + 1
ok(mats == 13 and sheets == 7 and 2 * sheets - mats == 1, "13 hill mats from 7 materials sheets, one mat spare")
ok(4 * 6 + 7 * 10 == 94 and 2 * 7 == 14, "cubes: 94 for children (about 100) plus 14 for the launch")
# older children build at most 10 each; the 10-cube rows and their counter-plans fit in a pair's 20
for q in [(4, 4, 2), (2, 5, 3), (1, 8, 1), (8, 1, 1), (5, 3, 2)]:
    ok(sum(q) == 10 and sum(counter(q)) <= 10, f"10-cube row {s(q)}: a pair builds it and {s(counter(q))} with 10 cubes each")
ok(max(sum(p) for p in [(3, 3, 3), (3, 3, 2)]) == 9 and 9 + 6 <= 20, "4-5 P7: 3-3-3 and a 6-cube partner fit in 20 cubes")
k1p6 = [(5, 0, 0), (1, 4, 0), (1, 3, 1), (2, 2, 1), (1, 1, 1)]
ok(max(sum(q) + fewest(q) for q in k1p6) == 10 <= 12, "K-1 P6: the shown plan and a fewest-cubes winner fit in a pair's 12 cubes")

print("\nALL OK" if not FAIL else f"\n{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
