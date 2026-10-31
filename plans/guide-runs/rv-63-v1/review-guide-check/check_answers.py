"""Reviewer's independent re-derivation of every answer the guide prints.

Written before reading the guide writer's checker. Uses pages.json from
extract_pages.py (boards and grids read from the final student PDFs) and the rows
read from the rendered pages. Every claim transcribed from the guide is asserted.

Usage: python3 -I check_answers.py
"""
import itertools
import json
import math
import os
import random
from collections import Counter, deque

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = json.load(open(os.path.join(HERE, "pages.json")))
for _k in ("U_grids_p9", "U_grids_p10"):
    for _g in PAGES[_k]:
        _g["shaded"] = [tuple(x) for x in _g["shaded"]]
        _g["dots"] = [tuple(x) for x in _g["dots"]]
L = "ABCDEFG"
fails = []


def ok(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


# ---------- rows: string r, r[i] = card sitting in home L[i] ----------
def home(n):
    return L[:n]


def swap_cards(row, x, y):
    return row.translate(str.maketrans(x + y, y + x))


def loops(row):
    """Arrows card -> home where it sits. Returns list of loops as card strings."""
    n = len(row)
    where = {row[i]: L[i] for i in range(n)}  # card -> home letter
    seen, out = set(), []
    for c in L[:n]:
        if c in seen:
            continue
        cyc, x = [], c
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = where[x]
        out.append("".join(cyc))
    return out


def bfs_dist(start, n):
    """Fewest swaps from start to every row (any two cards)."""
    dist = {start: 0}
    q = deque([start])
    while q:
        r = q.popleft()
        for x, y in itertools.combinations(L[:n], 2):
            s = swap_cards(r, x, y)
            if s not in dist:
                dist[s] = dist[r] + 1
                q.append(s)
    return dist


DIST = {n: bfs_dist(home(n), n) for n in range(2, 7)}


def fewest(row):
    return DIST[len(row)][row]


def apply_word(row, word):
    for w in word:
        row = swap_cards(row, w[0], w[1])
    return row


def exact_reach(row, m):
    cur = {row}
    n = len(row)
    for _ in range(m):
        cur = {swap_cards(r, x, y) for r in cur for x, y in itertools.combinations(L[:n], 2)}
    return home(n) in cur


def perms(n):
    return ["".join(p) for p in itertools.permutations(L[:n])]


def matches(row):
    return sum(row[i] == L[i] for i in range(len(row)))


def deranged(row):
    return matches(row) == 0


def D(n):
    return sum(1 for r in perms(n) if deranged(r)) if n else 1


# ---------- 0. fewest = n - loops, n <= 6 ----------
for n in range(2, 7):
    ok(all(DIST[n][r] == n - len(loops(r)) for r in perms(n)), f"fewest swaps = n - loops for every row, n={n}")

# ---------- K-1 ----------
print("\n== K-1 ==")
for n, ends in [(3, {"BCA", "CAB"}), (4, {"BADC", "CDAB", "DCBA"})]:
    hf = [r for r in perms(n) if deranged(r)]
    m = min(DIST[n][r] for r in hf)
    got = {r for r in hf if DIST[n][r] == m}
    ok(m == 2 and got == ends, f"K-1 P{n-2}: fewest {m}, end rows {sorted(got)}")
ok(apply_word("ABC", ["AB", "AC"]) == "BCA", "guide: from ABC, AB then AC gives BCA")
hf5 = [r for r in perms(5) if deranged(r)]
ok(min(DIST[5][r] for r in hf5) == 3, "K-1 P3: five cards need 3; two cannot")
ok(apply_word("ABCDE", ["AB", "CD", "AE"]) == "BEDCA" and deranged("BEDCA"), "guide word AB, CD, AE gives BEDCA, home-free")
for row, f, word in [("CBA", 1, ["AC"]), ("BCA", 2, ["AB", "BC"]), ("BADC", 2, ["AB", "CD"]), ("BCDA", 3, ["AB", "BC", "CD"])]:
    ok(fewest(row) == f and apply_word(row, word) == home(len(row)) and len(word) == f, f"K-1 P4 {row}: fewest {fewest(row)}, guide word {word}")
# BCDA: every first swap splits the single loop into 1+3 or 2+2
outs = Counter(tuple(sorted(len(c) for c in loops(swap_cards("BCDA", x, y)))) for x, y in itertools.combinations("ABCD", 2))
ok(set(outs) == {(1, 3), (2, 2)}, f"K-1 P4 BCDA first swaps give loop shapes {dict(outs)}")
# P5
deck3 = perms(3)
ok(deck3 == ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"] and [matches(r) for r in deck3] == [3, 1, 1, 0, 0, 1], "K-1 P5 match counts 3,1,1,0,0,1 in printed order")
per = {c: [r for r in deck3 if r[L.index(c)] == c] for c in "ABC"}
ok(per == {"A": ["ABC", "ACB"], "B": ["ABC", "CBA"], "C": ["ABC", "BAC"]}, f"K-1 P5 per-letter {per}")


def obey(board, n):
    """board: home -> refused cards. Return obeying rows on the first n homes/cards."""
    out = []
    for r in perms(n):
        if all(r[i] not in board.get(L[i], []) for i in range(n)):
            out.append(r)
    return out


ok(obey(PAGES["K1_P6"], 3) == ["BCA"], f"K-1 P6 {obey(PAGES['K1_P6'], 3)}")
ok(obey(PAGES["K1_P7"], 4) == ["BCDA", "CDAB", "DCAB"], f"K-1 P7 {obey(PAGES['K1_P7'], 4)}")
ok(obey(PAGES["K1_P8"], 4) == ["CDAB"], f"K-1 P8 {obey(PAGES['K1_P8'], 4)}")

# ---------- Grades 2-3 ----------
print("\n== Grades 2-3 ==")
m23 = [("CBAD", 1, ["AC"]), ("BCAD", 2, ["AB", "BC"]), ("DCBA", 2, ["AD", "BC"]), ("ACDB", 2, ["BC", "CD"]),
       ("BCDA", 3, ["AB", "BC", "CD"]), ("CDBA", 3, ["AC", "BD", "CD"])]
for row, f, word in m23:
    ok(fewest(row) == f and apply_word(row, word) == "ABCD", f"2-3 P2 {row}: fewest {fewest(row)} loops {len(loops(row))}, guide word {word}")
ok([len(loops(r)) for r, _, _ in m23] == [3, 2, 2, 2, 1, 1], "2-3 P2 loop counts 3,2,2,2,1,1 in reading order")
hardest4 = sorted(r for r in perms(4) if DIST[4][r] == max(DIST[4].values()))
ok(max(DIST[4].values()) == 3 and hardest4 == ["BCDA", "BDAC", "CADB", "CDBA", "DABC", "DCAB"], f"2-3 P3 hardest {hardest4}")
ok(all(len(loops(r)) == 1 for r in hardest4), "2-3 P3 hardest rows are single four-card loops")
hf4 = [r for r in perms(4) if deranged(r)]
ok(sorted(set(hf4) - set(hardest4)) == ["BADC", "CDAB", "DCBA"], "child bridge: base week's 9 home-free rows minus the 3 double exchanges = the 6 hardest")
ok(all(DIST[4][r] <= 2 for r in perms(4) if not deranged(r)), "child bridge: any row with a card at home needs at most 2")


def two_home(row):
    n = len(row)
    return [x + y for x, y in itertools.combinations(L[:n], 2)
            if matches(swap_cards(row, x, y)) - matches(row) == 2]


p4 = {r: two_home(r) for r in ["BCDA", "CDAB", "BCAD", "DBCA", "DACB"]}
ok(p4 == {"BCDA": [], "CDAB": ["AC", "BD"], "BCAD": [], "DBCA": ["AD"], "DACB": []}, f"2-3 P4 {p4}")
deck4 = perms(4)
ok(sum(matches(r) for r in deck4) == 24 and all(sum(r[i] == L[i] for r in deck4) == 6 for i in range(4)), "2-3 P5 24 circles, 6 per letter")
ok(sum(matches(r) for r in perms(3)) == 6 and sum(matches(r) for r in perms(5)) == 120, "2-3 P6 6 and 120")
piles4 = [sum(1 for r in deck4 if matches(r) == k) for k in range(5)]
ok(piles4 == [9, 8, 6, 0, 1], f"2-3 P7 piles {piles4}")
m8 = [len(obey(b, 4)) for b in PAGES["M_P8"]]
ok(m8 == [9, 7, 4, 0], f"2-3 P8 counts {m8}")
ok(obey(PAGES["M_P8"][2], 4) == ["CDAB", "CDBA", "DCAB", "DCBA"], "2-3 P8 third board rows")

# P9: all 4-spot boards on four cards
spots = [(c, h) for c in "ABCD" for h in "ABCD"]


def count_spots(sp, n=4):
    return sum(1 for r in perms(n) if all(r[L.index(h)] != c for c, h in sp))


def rk(sp):
    """r_k: k spots, pairwise distinct cards and homes."""
    out = [0] * (len(sp) + 1)
    for k in range(len(sp) + 1):
        for sub in itertools.combinations(sp, k):
            if len({c for c, h in sub}) == k and len({h for c, h in sub}) == k:
                out[k] += 1
    return out


dist9 = Counter()
triples = {}
for sp in itertools.combinations(spots, 4):
    cnt = count_spots(sp)
    dist9[cnt] += 1
    r = rk(sp)
    triples.setdefault((r[2], r[3], r[4]), set()).add(cnt)
    assert cnt == sum((-1) ** k * r[k] * math.factorial(4 - k) for k in range(5))
ok(sum(dist9.values()) == 1820 and sorted(dist9) == [0, 4, 6, 7, 8, 9], f"2-3 P9 counts that occur {dict(sorted(dist9.items()))}")
ok(dist9[9] == 24 and all(count_spots(sp) == 9 for sp in itertools.combinations(spots, 4)
                          if len({c for c, h in sp}) == 4 and len({h for c, h in sp}) == 4), "2-3 P9 the 24 one-per-card-and-home boards give 9")
ok(count_spots([("A", "A"), ("B", "B"), ("D", "C"), ("D", "D")]) == 8, "2-3 P9 guide example for 8")
ok(count_spots([("A", "A"), ("B", "B"), ("D", "A"), ("D", "B")]) == 6, "2-3 P9 guide example for 6")
guide_tab = {(0, 0, 0): 0, (2, 0, 0): 4, (3, 0, 0): 6, (4, 0, 0): 8, (4, 1, 0): 7, (5, 2, 0): 8, (6, 4, 1): 9}
ok({k: v for k, v in triples.items()} == {k: {v} for k, v in guide_tab.items()}, f"guide p8 triple table = all triples occurring {sorted(triples.items())}")

# ---------- Grades 4-5 ----------
print("\n== Grades 4-5 ==")
ok([min(DIST[n][r] for r in perms(n) if deranged(r)) for n in (3, 4, 5)] == [2, 2, 3], "4-5 P1 minima 2,2,3")
u2 = [("EBCDA", "(AE)(B)(C)(D)", 1, ["AE"]), ("BCADE", "(ACB)(D)(E)", 2, ["AB", "BC"]),
      ("BADEC", "(AB)(CED)", 3, ["AB", "CD", "DE"]), ("BCAED", "(ACB)(DE)", 3, ["AB", "BC", "DE"]),
      ("BCDEA", "(AEDCB)", 4, ["AB", "BC", "CD", "DE"]), ("DEABC", "(ACEBD)", 4, ["AD", "BE", "CD", "DE"])]
for row, lp, f, word in u2:
    mine = "".join("(" + c + ")" for c in loops(row))
    ok(mine == lp and fewest(row) == f and apply_word(row, word) == "ABCDE", f"4-5 P2/P3 {row}: loops {mine} fewest {fewest(row)} guide word {word}")
# worked arrow example WUVXY in homes U V W X Y
UV = "UVWXY"
ex = "WUVXY"
arrows = {ex[i]: UV[i] for i in range(5)}
ok(arrows == {"W": "U", "U": "V", "V": "W", "X": "X", "Y": "Y"}, f"4-5 P3 worked visual arrows {arrows}")
ok(loops("BCADE")[0] == "ACB", "BCADE: A sits in C, so A -> C")
hard5 = sorted(r for r in perms(5) if DIST[5][r] == 4)
guide24 = sorted("BCDEA BCEAD BDAEC BDECA BEACD BEDAC CADEB CAEBD CDBEA CDEAB CEBAD CEDBA DABEC DAECB DCAEB DCEBA DEABC DEBCA EABCD EADBC ECABD ECDAB EDACB EDBAC".split())
ok(hard5 == guide24 and len(hard5) == 24, f"4-5 P4 hardest list of 24 matches guide")
ok(sum(1 for r in hf5 if DIST[5][r] == 3) == 20 and len(hf5) == 44, "4-5 P4 20 of 44 need 3")
ok(all(sorted(len(c) for c in loops(r)) == [2, 3] for r in hf5 if DIST[5][r] == 3), "4-5 P4 the 20 are a 2-loop + 3-loop")
for row, want in [("BACDE", [False, True, False, True]), ("BCADE", [True, False, True, False])]:
    got = [exact_reach(row, m) for m in (2, 3, 4, 5)]
    ok(got == want, f"4-5 P5 {row} exactly 2,3,4,5: {got}")
ok(sum(matches(r) for r in deck4) == 24 and sum(matches(r) for r in perms(5)) == 120, "4-5 P6 24 and 120")
pairs = lambda n: sum(math.comb(matches(r), 2) for r in perms(n))
ok(pairs(4) == 12 and pairs(5) == 60, f"4-5 P7 pairs {pairs(4)}, {pairs(5)}")
piles5 = [sum(1 for r in perms(5) if matches(r) == k) for k in range(6)]
ok(piles5 == [44, 45, 20, 10, 0, 1], f"4-5 P8 piles {piles5}")
ok([D(n) - n * D(n - 1) for n in (3, 4, 5)] == [-1, 1, -1] and [D(3), D(4), D(5)] == [2, 9, 44], "4-5 P9 2 v 3, 9 v 8, 44 v 45")
b10 = PAGES["U_P10"]
ok(obey(b10, 3) == ["BCA"] and obey(b10, 4) == ["BCDA", "CDAB", "DCAB"], "4-5 P10 three and four cards")
guide16 = "BCDEA BDAEC BDEAC BEDAC CDAEB CDEAB CDEBA CEDAB CEDBA DCAEB DCEAB DCEBA DEABC ECDAB ECDBA EDABC".split()
ok(obey(b10, 5) == guide16, f"4-5 P10 five cards {len(obey(b10, 5))} rows match guide list")
b11a, b11b = PAGES["U_P11"]
guide13 = "BCDEA BDAEC BDEAC BEDAC CDAEB CDEAB CDEBA CEDAB CEDBA DCAEB DCEAB DCEBA DEABC".split()
ok(obey(b11a, 4) == ["BCDA", "CDAB"], f"4-5 P11 four {obey(b11a, 4)}")
ok(obey(b11b, 5) == guide13, f"4-5 P11 five {len(obey(b11b, 5))} rows match guide list")


def grid_spots(g):
    return [(c, h) for c, h in g["shaded"]]


g9 = PAGES["U_grids_p9"]
g10 = PAGES["U_grids_p10"]
strip4, ring4 = [g for g in g9 if g["cell"] == 19.8]
strip5, ring5 = [g for g in g10 if g["cell"] == 19.8]
for name, g, n, want, board in [("P12 strip4", strip4, 4, 3, b10), ("P12 ring4", ring4, 4, 2, b11a),
                                ("P13 strip5", strip5, 5, 16, b10), ("P13 ring5", ring5, 5, 13, b11b)]:
    sp = grid_spots(g)
    bsp = sorted((c, h) for h, cs in board.items() for c in cs if L.index(h) < n and L.index(c) < n)
    cnt = sum(1 for r in perms(n) if all(r[L.index(h)] != c for c, h in sp))
    r = rk(sp)
    alt = sum((-1) ** k * r[k] * math.factorial(n - k) for k in range(n + 1))
    ok(cnt == want == alt and sorted(sp) == bsp, f"{name}: grid count {cnt}, r_k {r[:n+1]}, alternating {alt}, same spots as board")
guide_r = {"P12 strip4": [1, 7, 15, 10, 1], "P12 ring4": [1, 8, 20, 16, 2], "P13 strip5": [1, 9, 28, 35, 15, 1], "P13 ring5": [1, 10, 35, 50, 25, 2]}
for name, g, n in [("P12 strip4", strip4, 4), ("P12 ring4", ring4, 4), ("P13 strip5", strip5, 5), ("P13 ring5", ring5, 5)]:
    ok(rk(grid_spots(g))[:n + 1] == guide_r[name], f"guide coefficient table row {name}")
# worked grid example
exg = [g for g in g9 if g["cell"] == 17.0]
ok(len(exg) == 2 and all(sorted(g["shaded"]) == [("U", "V"), ("W", "W"), ("X", "U")] for g in exg), "P12 worked example shading U-V, W-W, X-U (non-task)")
full = exg[1]["dots"]
ok(sorted(full) == [("U", "W"), ("V", "U"), ("W", "X"), ("X", "V")], f"P12 worked example dots {full} = row VXUW")
ok(not set(full) & set(exg[1]["shaded"]), "P12 worked example row obeys its shading")

# ---------- Overview general claims (checked on small n) ----------
print("\n== Overview claims ==")
for n in range(2, 7):
    hf = [r for r in perms(n) if deranged(r)]
    ok(min(DIST[n][r] for r in hf) == math.ceil(n / 2), f"leaving every home needs ceil(n/2), n={n}")
for n in range(2, 6):
    good = True
    for r in perms(n):
        f = DIST[n][r]
        for m in range(0, 8):
            if exact_reach(r, m) != (m >= f and (m - f) % 2 == 0):
                good = False
    ok(good, f"exact m swaps iff m >= fewest and same parity, n={n}, m<=7")
for n in range(1, 8):
    P = perms(n)
    ok(sum(matches(r) for r in P) == math.factorial(n), f"marks = n!, n={n}")
    if n >= 2:
        ok(sum(math.comb(matches(r), 2) for r in P) == math.factorial(n) // 2, f"pairs = n!/2, n={n}")
    ok([sum(1 for r in P if matches(r) == k) for k in range(n + 1)] == [math.comb(n, k) * D(n - k) for k in range(n + 1)], f"piles C(n,k) D(n-k), n={n}")
    ok(D(n) - n * D(n - 1) == (-1) ** n, f"D_n - n D_(n-1) = (-1)^n, n={n}")
ok(D(0) == 1 and D(1) == 0, "D0=1, D1=0")
random.seed(63)
good = True
for _ in range(300):
    n = random.randint(2, 5)
    sp = random.sample([(c, h) for c in L[:n] for h in L[:n]], random.randint(0, n * n // 2))
    cnt = sum(1 for r in perms(n) if all(r[L.index(h)] != c for c, h in sp))
    r = rk(sp)
    if cnt != sum((-1) ** k * r[k] * math.factorial(n - k) for k in range(min(len(sp), n) + 1)):
        good = False
ok(good, "rook-number alternating sum on 300 random boards, n<=5")


# guide p8 chain/ring recursion F(L,k)
def F(Ln, k):
    if k == 0:
        return 1
    if Ln <= 0:
        return 0
    if Ln == 1:
        return 1 if k == 1 else 0
    return F(Ln - 1, k) + F(Ln - 2, k - 1)


for n in (3, 4, 5, 6):
    ok([F(2 * n - 1, k) for k in range(n + 1)] == [math.comb(2 * n - k, k) for k in range(n + 1)], f"strip r_k via F, n={n}")
    ring = [1] + [F(2 * n - 1, k) + F(2 * n - 3, k - 1) for k in range(1, n + 1)]
    kap = [1] + [round(2 * n / (2 * n - k) * math.comb(2 * n - k, k)) for k in range(1, n + 1)]
    ok(ring == kap, f"ring r_k via F matches Kaplansky, n={n}: {ring}")

print("\nFAILURES:", len(fails))
for f in fails:
    print("  ", f)
