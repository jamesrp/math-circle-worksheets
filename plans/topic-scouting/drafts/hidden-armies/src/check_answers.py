"""Check every answer the three Hidden armies packets rely on.

Game: each player splits N cubes over hills 1, 2, 3 (a hill may be empty).
A hill goes to the player with more cubes on it; an equal hill goes to nobody.
The player who wins more hills wins the game.
"""
import itertools


def plans(n, k=3):
    return [p for p in itertools.product(range(n + 1), repeat=k) if sum(p) == n]


def res(p, q):
    """+1 if p beats q, -1 if q beats p, 0 for a draw."""
    w = sum(a > b for a, b in zip(p, q))
    l = sum(a < b for a, b in zip(p, q))
    return (w > l) - (w < l)


def beaters(q, n=None):
    n = sum(q) if n is None else n
    return [p for p in plans(n) if res(p, q) == 1]


def unbeaten(n):
    return [p for p in plans(n) if not beaters(p)]


def fewest(q):
    # with unequal armies a win can also be one hill won and two hills tied
    m = 0
    while not any(res(p, q) == 1 for p in plans(m)):
        m += 1
    return m


def counter(q):
    """The counter-plan rule: one more on the two smaller hills, rest on the biggest."""
    order = sorted(range(3), key=lambda i: -q[i])
    big, s1, s2 = order
    p = [0, 0, 0]
    p[s1] = q[s1] + 1
    p[s2] = q[s2] + 1
    p[big] = sum(q) - p[s1] - p[s2]
    assert p[big] >= 0
    return tuple(p)


def three_cycles(n):
    P = plans(n)
    out = set()
    for a, b, c in itertools.permutations(P, 3):
        if res(a, b) == 1 and res(b, c) == 1 and res(c, a) == 1:
            out.add(min((a, b, c), (b, c, a), (c, a, b)))
    return out


ok = True


def check(cond, msg):
    global ok
    print(("ok   " if cond else "FAIL ") + msg)
    ok &= bool(cond)


# General facts
for n in range(1, 13):
    u = unbeaten(n)
    if n >= 4:
        check(u == [], f"N={n}: no unbeaten plan")
        check(all(res(counter(q), q) == 1 for q in plans(n)), f"N={n}: counter rule beats every plan")
    else:
        print(f"     N={n}: unbeaten {u}")
check(unbeaten(1) == plans(1), "N=1: every plan unbeaten (all games draw)")
check(sorted(unbeaten(2)) == sorted([(1, 1, 0), (1, 0, 1), (0, 1, 1)]), "N=2: unbeaten are arrangements of 1-1-0")
check(unbeaten(3) == [(1, 1, 1)], "N=3: only 1-1-1 unbeaten")
for n in range(1, 9):
    check(all(fewest(q) == sum(q) - max(q) + 2 for q in plans(n)), f"fewest-cubes rule (two smaller hills + 2) for N={n}")

print("\n--- K-1 ---")
check(res((2, 3, 0), (1, 0, 4)) == 1, "rules example: 2-3-0 beats 1-0-4")
check(unbeaten(5) == [], "P2: no 5-cube plan nobody can beat (open question; answer is no)")
for q in [(5, 0, 0), (0, 4, 1), (0, 3, 2), (2, 1, 2)]:
    b = beaters(q)
    check(len(b) > 0, f"P3 {q}: {len(b)} beaters with 5 cubes, e.g. {b[:4]}")
check(sorted(unbeaten(2)) == sorted([(1, 1, 0), (1, 0, 1), (0, 1, 1)]) and unbeaten(3) == [(1, 1, 1)]
      and unbeaten(4) == [], "P4: 2 cubes -> 1-1-0 and arrangements; 3 cubes -> 1-1-1; 4 cubes -> none")
# P5 boxes as printed: columns (A, B, C), rows A-B, B-C, A-C
for A, B, C in [((4, 1, 0), (2, 2, 1), (0, 0, 5)), ((0, 1, 4), (2, 0, 3), (1, 2, 2))]:
    print(f"     P5 box {A},{B},{C}: A-B {res(A, B)}, B-C {res(B, C)}, A-C {res(A, C)} (+1 = left wins)")
    check(all(res(x, y) != 0 for x, y in [(A, B), (B, C), (A, C)]), f"P5 box {A},{B},{C}: no row is a tie")
g1 = [((2, 2, 1), (4, 1, 0)), ((4, 1, 0), (0, 0, 5)), ((0, 0, 5), (2, 2, 1))]
g2 = [((0, 1, 4), (2, 0, 3)), ((2, 0, 3), (1, 2, 2)), ((1, 2, 2), (0, 1, 4))]
for a, b in g1 + g2:
    r = res(a, b)
    print(f"     P5 {a} vs {b}: {'first' if r == 1 else 'second' if r == -1 else 'draw'}")
check(res(*g1[0][::1]) == 1 and res(*g1[1]) == 1 and res(*g1[2]) == -1, "P5 group 1: 2-2-1 beats both, 4-1-0 beats 0-0-5")
check(all(res(a, b) == 1 for a, b in g2), "P5 group 2: a circle, no best plan")
for q, m in [((5, 0, 0), 2), ((1, 4, 0), 3), ((1, 3, 1), 4), ((2, 2, 1), 5), ((1, 1, 1), 4)]:
    check(fewest(q) == m, f"P6 fewest cubes to beat {q} = {m} (any number of cubes allowed)")
for q, m, boards in [((3, 1, 1), 3, 4), ((4, 0, 1), 6, 8)]:
    b = beaters(q)
    check(len(b) == m and boards > m, f"P7 every 5-cube plan beating {q}: {len(b)} {b}; {boards} boards")

print("\n--- Grades 2-3 ---")
for q in [(2, 2, 2), (1, 4, 1), (3, 0, 3), (0, 1, 5), (3, 2, 2), (1, 1, 5), (4, 4, 2), (2, 5, 3), (7, 7, 6)]:
    c = counter(q)
    check(res(c, q) == 1 and sum(c) == sum(q), f"P3 {q} ({sum(q)} cubes) beaten by {c}")
check(all(unbeaten(n) == [] for n in range(6, 13)), "P3 claim: every plan with 6 to 12 cubes can be beaten")
check(unbeaten(3) == [(1, 1, 1)] and unbeaten(4) == [], "P4: 1-1-1 with 3 cubes; none with 4")
cyc6 = three_cycles(6)
with222 = [c for c in cyc6 if (2, 2, 2) in c]
check(len(with222) > 0, f"P5 circle containing 2-2-2 exists, e.g. {with222[:3]}")
check(not any((6, 0, 0) in c for c in cyc6), "P5 no circle contains 6-0-0 (it beats nothing)")
check(not beaters((6, 0, 0)) == [] and [q for q in plans(6) if res((6, 0, 0), q) == 1] == [], "6-0-0 beats no plan")
b222 = beaters((2, 2, 2))
check(sorted(b222) == sorted([(3, 3, 0), (3, 0, 3), (0, 3, 3)]), f"P6 beaters of 2-2-2: {b222}")
b600 = beaters((6, 0, 0))
check(len(b600) == 15 and all(p[1] >= 1 and p[2] >= 1 for p in b600), f"P6 beaters of 6-0-0: {len(b600)}")
for q, m in [((6, 0, 0), 2), ((4, 1, 1), 4), ((3, 2, 1), 5), ((2, 2, 2), 6), ((3, 3, 0), 5), ((1, 1, 1), 4), ((8, 1, 1), 4), ((5, 3, 2), 7)]:
    check(fewest(q) == m, f"P7 fewest to beat {q} = {m}")
check(fewest((1, 1, 1)) == 4 > 3, "P7 1-1-1 needs more cubes than the partner (different numbers allowed)")

print("\n--- Grades 4-5 ---")
for q in [(2, 2, 2), (1, 4, 1), (3, 2, 2), (3, 3, 3), (1, 8, 1), (7, 7, 6), (34, 33, 33), (50, 0, 50)]:
    c = counter(q)
    check(res(c, q) == 1 and sum(c) == sum(q), f"P2 {q} ({sum(q)} cubes) beaten by {c}")
check(res((48, 1, 51), (50, 0, 50)) == 1, "P2 50-0-50 beaten by 48-1-51")
for n in range(1, 6):
    print(f"     P3 N={n}: unbeaten {unbeaten(n)}")
P6 = plans(6)
check(len(P6) == 28, "P4: 28 plans with 6 cubes")
table = {p: sum(res(p, q) == 1 for q in P6) for p in P6}
for t in [(2, 2, 2), (3, 2, 1), (4, 1, 1), (3, 3, 0), (4, 2, 0), (5, 1, 0), (6, 0, 0)]:
    vals = {table[p] for p in set(itertools.permutations(t))}
    print(f"     P4 arrangements of {t}: beat {vals}, beaten by {len(beaters(t))}")
check(max(table.values()) == table[(2, 2, 2)] == 12 and len(beaters((2, 2, 2))) == 3, "P4: 2-2-2 beats most (12), beaten by 3")
check(table[(6, 0, 0)] == 0 and len(beaters((6, 0, 0))) == 15, "P4: 6-0-0 beats 0, beaten by 15")
inc = set(x for c in cyc6 for x in c)
check(inc == set(P6) - {(6, 0, 0), (0, 6, 0), (0, 0, 6)}, "P5: every plan except 6-0-0, 0-6-0, 0-0-6 lies on a circle of three")
ben = [(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]
mia = [(4, 2, 0), (4, 0, 2), (2, 4, 0), (2, 0, 4), (0, 4, 2), (0, 2, 4)]


def vs_list(q, L):
    return sum(res(q, l) == 1 for l in L), sum(res(q, l) == -1 for l in L)


best_ben = [(q, vs_list(q, ben)) for q in P6 if vs_list(q, ben)[0] > vs_list(q, ben)[1]]
check(len(best_ben) > 0, f"P8 Ben's die can be exploited: {best_ben}")
check(all(vs_list(q, mia)[0] <= vs_list(q, mia)[1] for q in P6), "P8 Mia's die: no plan beats more of her plans than it loses to")
print("     P8 Mia: max wins-losses =", max(vs_list(q, mia)[0] - vs_list(q, mia)[1] for q in P6))
for q, m in [((6, 0, 0), 2), ((4, 1, 1), 4), ((3, 2, 1), 5), ((2, 2, 2), 6), ((1, 1, 1), 4), ((40, 30, 30), 62)]:
    got = sum(q) - max(q) + 2 if sum(q) > 12 else fewest(q)
    check(got == m, f"P6 fewest to beat {q} = {m}")
# 40-30-30 directly: a 62-cube plan beats it, no 61-cube plan does (only hills 2,3 or a pair incl. hill 1 matter)
check(res((0, 31, 31), (40, 30, 30)) == 1, "P6 0-31-31 beats 40-30-30")
check(not any(res(p, (40, 30, 30)) == 1 for p in plans(61)), "P6 no 61-cube plan beats 40-30-30")


def safe(p):  # no 6-cube plan beats p
    return not any(res(q, p) == 1 for q in P6)


def always(p):  # p beats every 6-cube plan
    return all(res(p, q) == 1 for q in P6)


ms = min(m for m in range(0, 15) if any(safe(p) for p in plans(m)))
ma = min(m for m in range(0, 15) if any(always(p) for p in plans(m)))
check(ms == 8, f"P7 fewest cubes for a plan no 6-cube plan beats: {ms}, e.g. {[p for p in plans(ms) if safe(p)][:3]}")
check(ma == 9, f"P7 fewest cubes for a plan that beats every 6-cube plan: {ma}, e.g. {[p for p in plans(ma) if always(p)][:3]}")
check(table[(3, 2, 1)] == 11 and table[(4, 1, 1)] == table[(3, 3, 0)] == 9 and table[(4, 2, 0)] == 8
      and table[(5, 1, 0)] == 5, "P4: other counts 11, 9, 9, 8, 5; largest count 12 fits the circles")
print("\nALL OK" if ok else "\nSOME CHECKS FAILED")
