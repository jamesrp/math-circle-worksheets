#!/usr/bin/env python3
"""Check every answer behind the Week 63 return-visit pages by enumeration.

Rows are written as the cards in homes A, B, C, ... in order.
A forbidden spot (X, Y) means card X may not sit in home Y.
Run: python3 verify.py   (prints OK lines; any failure raises AssertionError)
"""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb, factorial

L = "ABCDEFG"


def rows(n):
    return ["".join(p) for p in permutations(L[:n])]


def loops(r):
    """Number of loops of the arrows card -> home where it sits."""
    seen, c = set(), 0
    for x in range(len(r)):
        if x in seen:
            continue
        c += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = L.index(r[y])
    return c


def bfs(n):
    """Fewest swaps (any two cards) from every row to home."""
    start = L[:n]
    d = {start: 0}
    q = deque([start])
    while q:
        r = q.popleft()
        for i, j in combinations(range(n), 2):
            s = list(r)
            s[i], s[j] = s[j], s[i]
            s = "".join(s)
            if s not in d:
                d[s] = d[r] + 1
                q.append(s)
    return d


def exact(r, m):
    """Can row r be brought home in exactly m swaps?"""
    n = len(r)
    cur = {r}
    for _ in range(m):
        nxt = set()
        for x in cur:
            for i, j in combinations(range(n), 2):
                s = list(x)
                s[i], s[j] = s[j], s[i]
                nxt.add("".join(s))
        cur = nxt
    return L[:n] in cur


def free(r):
    return all(r[i] != L[i] for i in range(len(r)))


def obey(n, forb):
    return [r for r in rows(n) if all((r[i], L[i]) not in forb for i in range(n))]


def own(n):
    return {(L[i], L[i]) for i in range(n)}


def strip(n):
    return own(n) | {(L[i], L[i + 1]) for i in range(n - 1)}


def ring(n):
    return strip(n) | {(L[n - 1], "A")}


def rook(F, n):
    res = [0] * (n + 1)
    for k in range(n + 1):
        for S in combinations(sorted(F), k):
            if len({c for c, _ in S}) == k and len({h for _, h in S}) == k:
                res[k] += 1
    return res


def from_refused(refused):
    """Board drawn as {home: refused cards} -> set of forbidden spots."""
    return {(c, h) for h, cs in refused.items() for c in cs}


D = {n: {r: v for r, v in bfs(n).items()} for n in range(3, 7)}

# Kernel 1: fewest swaps = cards - loops
for n in range(3, 7):
    assert all(D[n][r] == n - loops(r) for r in D[n])
print("OK fewest swaps = n - loops, n = 3..6")
assert [Counter(D[3].values())[k] for k in range(3)] == [1, 3, 2]
assert [Counter(D[4].values())[k] for k in range(4)] == [1, 6, 11, 6]
assert [Counter(D[5].values())[k] for k in range(5)] == [1, 10, 35, 50, 24]

# Swap printed rows (all bands)
answers = {"CBA": 1, "BCA": 2, "BADC": 2, "BCDA": 3,                      # K-1 P4
           "CBAD": 1, "BCAD": 2, "DCBA": 2, "ACDB": 2, "CDBA": 3,          # 2-3 P2
           "EBCDA": 1, "BCADE": 2, "BADEC": 3, "BCAED": 3, "BCDEA": 4,     # 4-5 P2
           "DEABC": 4}
for r, v in answers.items():
    assert D[len(r)][r] == v, r
print("OK printed rows:", answers)

# Fewest swaps from home to home-free: 2, 2, 3; end rows
for n, m in ((3, 2), (4, 2), (5, 3)):
    best = min(D[n][r] for r in D[n] if free(r))
    assert best == m
ends4 = sorted(r for r in D[4] if free(r) and D[4][r] == 2)
assert ends4 == ["BADC", "CDAB", "DCBA"]
assert sorted(r for r in D[3] if free(r) and D[3][r] == 2) == ["BCA", "CAB"]
assert free("BEDCA") and D[5]["BEDCA"] == 3
print("OK home to home-free: 2, 2, 3; four-card ends", ends4)

# 2-3 P3: every four-card row needing the most swaps
hard4 = sorted(r for r in D[4] if D[4][r] == 3)
assert hard4 == ["BCDA", "BDAC", "CADB", "CDBA", "DABC", "DCAB"]
assert max(D[4].values()) == 3
print("OK hardest four-card rows (3 swaps, never 4):", hard4)

# 2-3 P4: one swap brings two cards home at once
def two_home(r):
    n = len(r)
    return any(r[i] == L[j] and r[j] == L[i] for i, j in combinations(range(n), 2))
p4 = {r: two_home(r) for r in ["BCDA", "CDAB", "BCAD", "DBCA", "DACB"]}
assert p4 == {"BCDA": False, "CDAB": True, "BCAD": False, "DBCA": True, "DACB": False}
print("OK 2-3 P4:", p4)

# 4-5 P4: hardest five-card rows
hard5 = [r for r in D[5] if D[5][r] == 4]
assert len(hard5) == 24 and all(loops(r) == 1 for r in hard5)
assert Counter(D[5][r] for r in D[5] if free(r)) == Counter({3: 20, 4: 24})
print("OK 24 hardest five-card rows; 20 of 44 home-free need 3")

# 4-5 P5: parity
assert [exact("BACDE", m) for m in range(1, 6)] == [True, False, True, False, True]
assert [exact("BCADE", m) for m in range(1, 6)] == [False, True, False, True, False]
print("OK parity: BACDE 1,3,5; BCADE 2,4")

# Kernel 2: marks, pairs, piles
for n in range(1, 8):
    R = rows(n)
    marks = sum(sum(r[i] == L[i] for i in range(n)) for r in R)
    assert marks == factorial(n)
    per = Counter(L[i] for r in R for i in range(n) if r[i] == L[i])
    assert all(per[L[i]] == factorial(n - 1) for i in range(n))
    if n >= 2:
        pairs = sum(comb(sum(r[i] == L[i] for i in range(n)), 2) for r in R)
        assert pairs == factorial(n) // 2
piles4 = Counter(sum(r[i] == L[i] for i in range(4)) for r in rows(4))
piles5 = Counter(sum(r[i] == L[i] for i in range(5)) for r in rows(5))
assert [piles4[k] for k in range(5)] == [9, 8, 6, 0, 1]
assert [piles5[k] for k in range(6)] == [44, 45, 20, 10, 0, 1]
print("OK marks n!, per letter (n-1)!, pairs n!/2; piles 9,8,6,0,1 and 44,45,20,10,0,1")
marks3 = [sum(r[i] == L[i] for i in range(3)) for r in rows(3)]
assert sum(marks3) == 6
print("OK K-1 P5: 6 counters on 6 outcome cards, 2 per letter")

# Kernel 3: printed boards
k1 = [({"A": "A", "B": "AB", "C": "BC"}, 3, ["BCA"]),
      ({"A": "A", "B": "AB", "C": "BC", "D": "CD"}, 4, ["BCDA", "CDAB", "DCAB"]),
      ({"A": "AB", "B": "ABC", "C": "BCD", "D": "CD"}, 4, ["CDAB"])]
for ref, n, want in k1:
    assert sorted(obey(n, from_refused(ref))) == want
print("OK K-1 boards: BCA; BCDA CDAB DCAB; CDAB")

m8 = [({"A": "A", "B": "B", "C": "C", "D": "D"}, 9),
      ({"A": "A", "B": "AB", "C": "C"}, 7),
      ({"A": "AB", "B": "AB"}, 4),
      ({"A": "A", "B": "A", "C": "A", "D": "A"}, 0)]
for ref, want in m8:
    assert len(obey(4, from_refused(ref))) == want
print("OK 2-3 P8: 9, 7, 4, 0")

# 2-3 P9: all four-spot boards on four cards
cells = [(c, h) for c in "ABCD" for h in "ABCD"]
cnt = Counter(len(obey(4, set(F))) for F in combinations(cells, 4))
assert sorted(cnt) == [0, 4, 6, 7, 8, 9]
assert cnt[9] == 24
best = [F for F in combinations(cells, 4) if len(obey(4, set(F))) == 9]
assert all(len({c for c, _ in F}) == 4 and len({h for _, h in F}) == 4 for F in best)
assert len(obey(4, from_refused({"A": "AB", "B": "CD"}))) == 8
assert len(obey(4, from_refused({"A": "A", "B": "B", "C": "D", "D": "D"}))) == 8
assert len(obey(4, from_refused({"A": "ABC", "B": "D"}))) == 6
assert len(obey(4, from_refused({"A": "AD", "B": "BD"}))) == 6
print("OK 2-3 P9: max 9 (one cross per card and home), 8 and 6 reachable, 5 impossible;",
      dict(sorted(cnt.items())))

# 4-5 P10, P11 and grids (P12, P13)
for n, s_want, r_want in ((3, 1, None), (4, 3, 2), (5, 16, 13)):
    assert len(obey(n, strip(n))) == s_want
    if r_want:
        assert len(obey(n, ring(n))) == r_want
    for F, want in ((strip(n), s_want), (ring(n), r_want)):
        if want is None:
            continue
        rk = rook(F, n)
        assert sum((-1) ** k * rk[k] * factorial(n - k) for k in range(n + 1)) == want
print("OK strip 1, 3, 16; ring 2, 13; alternating sums agree")
print("   strip 4", rook(strip(4), 4), "strip 5", rook(strip(5), 5))
print("   ring 4", rook(ring(4), 4), "ring 5", rook(ring(5), 5))
assert sorted(set(obey(5, strip(5))) - set(obey(5, ring(5)))) == ["ECDAB", "ECDBA", "EDABC"]
assert sorted(obey(4, ring(4))) == ["BCDA", "CDAB"]

# 4-5 P12 worked example: VXUW obeys the example shading U-in-V, W-in-W, X-in-U
ex = "VXUW"
homes = "UVWX"
shade = {("U", "V"), ("W", "W"), ("X", "U")}
assert all((ex[i], homes[i]) not in shade for i in range(4))
print("OK grid worked example row obeys its shading")
print("ALL CHECKS PASSED")
