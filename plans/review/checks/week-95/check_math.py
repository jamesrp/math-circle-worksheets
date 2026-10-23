#!/usr/bin/env python3
"""Independent mathematical checks for Week 95 (Count the unseen).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py or student/verify.py. Standard library only.

Model: a bag is the set {0, ..., N-1}. A round is a first catch (a set of M
distinct objects, all marked and returned) and a second catch (a set of n
distinct objects). Overlap R = size of the intersection. "Possible" means some
pair of sets realises the record; "average" means the exact mean over all
equally likely pairs of subsets (uniform first and second catch, independent).

Everything that can be enumerated directly (sets of subsets) is enumerated;
where full enumeration is too large (e.g. pairs of 12-subsets of 24) the exact
distribution is obtained by enumerating second catches against a fixed first
catch, which is equivalent by symmetry (checked by full enumeration for small N).

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
OUT = []
FAILS = []


def log(s=""):
    OUT.append(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------- primitives
def overlap_dist_fixed_first(N, M, n):
    """Exact distribution of R by enumerating every n-subset against first={0..M-1}."""
    first = set(range(M))
    counts = {}
    total = 0
    for S in combinations(range(N), n):
        r = sum(1 for x in S if x in first)
        counts[r] = counts.get(r, 0) + 1
        total += 1
    return {r: F(c, total) for r, c in sorted(counts.items())}


def overlap_dist_full(N, M, n):
    """Exact distribution of R by enumerating every (first, second) pair."""
    counts = {}
    total = 0
    seconds = [set(S) for S in combinations(range(N), n)]
    for A in combinations(range(N), M):
        A = set(A)
        for S in seconds:
            r = len(A & S)
            counts[r] = counts.get(r, 0) + 1
            total += 1
    return {r: F(c, total) for r, c in sorted(counts.items())}


def possible_overlaps(N, M, n):
    """Set of overlaps realisable by some pair of sets (direct search)."""
    if M > N or n > N:
        return set()
    return set(overlap_dist_fixed_first(N, M, n))


def mean(d):
    return sum(r * p for r, p in d.items())


def smallest_bag(M, n, R, cap=60):
    for N in range(1, cap):
        if R in possible_overlaps_fast(N, M, n):
            return N
    return None


def possible_overlaps_fast(N, M, n):
    """Constructive search: try to build first={0..M-1}, second with r marked + n-r unmarked."""
    out = set()
    if M > N or n > N:
        return out
    for r in range(0, n + 1):
        if r <= M and n - r <= N - M:
            out.add(r)
    return out


# ------------------------------------------------- 0. the set facts (overview)
log("== Overview: overlap support and lower bound (direct enumeration) ==")
ok = True
for N in range(1, 11):
    for M in range(0, N + 1):
        for n in range(0, N + 1):
            direct = possible_overlaps(N, M, n)
            formula = set(range(max(0, M + n - N), min(M, n) + 1))
            if direct != formula or direct != possible_overlaps_fast(N, M, n):
                ok = False
                log(f"  mismatch N={N} M={M} n={n}: {direct} vs {formula}")
check(ok, "for every N<=10, M,n<=N: realisable overlaps = max(0,M+n-N)..min(M,n)")

ok = True
for M in range(0, 8):
    for n in range(0, 8):
        for R in range(0, min(M, n) + 1):
            Ns = [N for N in range(1, 20) if R in possible_overlaps(N, M, n)]
            lo = max(1, M + n - R)  # bags are nonempty in this search
            if not Ns or Ns != list(range(lo, 20)):
                ok = False
check(ok, "a record (M,n,R) fits exactly the bags N >= M+n-R (checked N<20, M,n<8)")

ok = True
for N in range(1, 8):
    for M in range(0, N + 1):
        for n in range(0, N + 1):
            if overlap_dist_full(N, M, n) != overlap_dist_fixed_first(N, M, n):
                ok = False
check(ok, "fixing the first catch gives the same overlap distribution as random first catch (N<8)")

ok = True
for N in range(1, 13):
    for M in range(0, N + 1):
        for n in range(0, N + 1):
            if mean(overlap_dist_fixed_first(N, M, n)) != F(M * n, N):
                ok = False
check(ok, "exact mean overlap equals M*n/N for every N<=12 (enumerated, not assumed)")

ok = True
for N in range(1, 15):
    for n in range(1, N + 1):
        cnt = sum(1 for S in combinations(range(N), n) if 0 in S)
        ok &= F(cnt, comb(N, n)) == F(n, N) and cnt == comb(N - 1, n - 1)
check(ok, "one object lies in C(N-1,n-1) of the C(N,n) second catches, fraction n/N")

# ------------------------------------------------------------- Grades 2-3
log("")
log("== Grades 2-3 ==")
# P1
ok = all(possible_overlaps(N, 4, 4) == set(range(5)) for N in range(8, 21))
check(ok, "G23 P1: for every N in 8..20 with catches 4,4 every overlap 0..4 is possible")
check(all(mean(overlap_dist_fixed_first(N, 4, 4)) == F(16, N) for N in range(8, 21)),
      "G23 P1: guide's mean overlap 16/N")

# P2 identity records
first, second = set("ABCDE"), set("BDEFG")
union = first | second
check(sorted(first & second) == list("BDE"), "G23 P2: shared objects are B, D, E")
check(len(union) == 7, "G23 P2: seven different objects seen, so smallest bag 7")
poss = [t for t in (6, 7, 8, 12, 20) if t >= len(union)]
check(poss == [7, 8, 12, 20], f"G23 P2: of 6,7,8,12,20 the possible totals are {poss}")

# P3
first, second = set("ABCDE"), set("FGHIJ")
check(not (first & second) and len(first | second) == 10,
      "G23 P3: disjoint catches, smallest bag 10; any N>=10 also fits (unseen objects)")

# P4 likelihoods
seq = [2, 1, 3, 1, 2, 0]
d8 = overlap_dist_full(8, 4, 4)
d16 = overlap_dist_fixed_first(16, 4, 4)
log(f"  P(R|N=8)  = {dict((r, str(p)) for r, p in d8.items())}")
log(f"  P(R|N=16) = {dict((r, str(p)) for r, p in d16.items())}")
check(all(r in d8 and r in d16 for r in seq), "G23 P4: every printed overlap is possible for both 8 and 16")
per_round = [8 if d8[r] > d16[r] else 16 for r in seq]
log(f"  per-round likelihood choice: {per_round}")
check(per_round == [8, 16, 8, 16, 8, 16], "G23 P4: guide's per-round choices 8,16,8,16,8,16")
fm = []
for r in seq:
    if r == 0:
        fm.append("none")
    else:
        g = F(16, r)
        fm.append(str(g))
log(f"  fraction-matching guesses 16/R: {fm}")
L8 = L16 = F(1)
for r in seq:
    L8 *= d8[r]
    L16 *= d16[r]
lr = L16 / L8
log(f"  L(16)/L(8) = {lr} = {float(lr):.4f}")
check(abs(float(lr) - 1.76) < 0.005, "G23 P4: guide's 'likelihood about 1.76 times that at 8' for 16")
check(F(sum(seq), 6) == F(3, 2), "G23 P4: mean overlap 1.5; model means 16/8=2, 16/16=1")
log(f"  note: pooled fraction matching 16/1.5 = {float(F(16, 1) / F(3, 2)):.3f} (nearer 8); "
    f"votes per round 3 for 8, 3 for 16 -- the printed data are deliberately balanced")

# P5
for N in (8, 16):
    A = set(range(4))
    S0 = set(range(4, 8))
    S3 = {0, 1, 2, 4}
    check(len(A & S0) == 0 and len(A & S3) == 3 and max(S0 | S3) < N,
          f"G23 P5: N={N}: first {{A..D}}, second {{E..H}} gives 0; {{A,B,C,E}} gives 3")
check(d8[0] == F(1, 70), "G23 P5: random zero overlap at N=8 has chance 1/70")

# P6, P7
expect = {6: {3, 4}, 7: {2, 3, 4}, 8: {1, 2, 3, 4}, 12: {0, 1, 2, 3, 4}}
for N, s in expect.items():
    got = possible_overlaps(N, 5, 4)
    check(got == s, f"G23 P6/P7: N={N}, catches 5 and 4: possible overlaps {sorted(got)}")
check(all(4 in possible_overlaps(N, 5, 4) and 0 not in possible_overlaps(N, 5, 4) for N in (6, 7, 8)),
      "G23 P7: 'overlap 4 possible, 0 impossible' works for bags 6, 7 and 8")
# guide's next-visit remark: min overlap as N grows
mins = [min(possible_overlaps(N, 5, 4)) for N in range(5, 13)]
check(mins == [max(0, 9 - N) for N in range(5, 13)], f"G23 P7 guide: smallest overlap 9-N until 0: {mins}")

# ------------------------------------------------------------- Grades 4-5
log("")
log("== Grades 4-5 ==")
ok = all(possible_overlaps_fast(N, 6, 6) == set(range(7)) for N in range(12, 25))
ok &= all(possible_overlaps(N, 6, 6) == set(range(7)) for N in (12, 13, 14))
check(ok, "G45 P1: every overlap 0..6 is possible for every N in 12..24")
check(mean(overlap_dist_fixed_first(12, 6, 6)) == 3 and mean(overlap_dist_fixed_first(24, 6, 6)) == F(3, 2),
      "G45 P1: expected overlap 36/N runs from 3 (N=12) to 1.5 (N=24)")

# P2
check(smallest_bag(6, 6, 2) == 10, "G45 P2: record A (6,6,2): smallest bag 10")
check(smallest_bag(6, 6, 0) == 12, "G45 P2: record B (6,6,0): smallest bag 12")
A, S = set(range(1, 7)), {1, 2, 7, 8, 9, 10}
check(len(A & S) == 2 and len(A | S) == 10, "G45 P2: guide construction first 1-6, second 1,2,7-10")

# P3
check(F(2 * 3, 1) == 6, "G45 P3 example: 2 marked, sample 1 of 3 -> rule's guess 6 (2/6 = 1/3)")
check(F(6 * 6, 2) == 18 and F(6, 18) == F(2, 6), "G45 P3: record A rule's guess 18 (6/18 = 2/6)")
check(2 in possible_overlaps(10, 6, 6), "G45 P3: a 10-object bag also gives record A, so 18 is not forced")
check(F(2, 6) != F(6, 10), "G45 P3 guide: sample fraction 1/3 differs from population fraction 6/10")
log(f"  P(R=2 | N=10, 6, 6) = {overlap_dist_fixed_first(10, 6, 6)[2]}")

# P4
seq = [1, 2, 3, 2, 0]
guesses = [F(36, r) if r else None for r in seq]
check(guesses == [36, 18, 12, 18, None], "G45 P4: printed rule's guesses 36, 18, 12, 18, no matching total")
check(all(r in possible_overlaps_fast(18, 6, 6) for r in seq), "G45 P4: an 18-object bag can produce every record")
seq_min = max(6 + 6 - r for r in seq)
check(seq_min == 12, "G45 P4: smallest bag fitting all five records is 12; every N>=12 fits")
ok = True
for r in seq:
    sec = set(range(1, r + 1)) | set(range(7, 12 - r + 1))
    ok &= len(sec) == 6 and len(sec & set(range(1, 7))) == r and max(sec) <= 18
check(ok, "G45 P4 guide construction: second = 1..r plus 7..12-r has 6 objects and overlap r")
check(F(36) / F(sum(seq), 5) == F(45, 2), "G45 P4 guide: mean overlap 8/5, matched guess 22.5")
check(sum(g for g in guesses if g) / 4 == 21, "G45 P4 guide: average of the four finite guesses 21")

# P5
check(0 in possible_overlaps_fast(12, 6, 6) and 0 in possible_overlaps_fast(18, 6, 6),
      "G45 P5: bags 12 and 18 both give overlap 0")
ok = all(F(M * 6, 18) < F((M + 1) * 6, 18) for M in range(0, 18))
check(ok, "G45 P5 guide: with N fixed and other catch positive, enlarging a catch raises the mean")

# P6, P7: exact expectation for N=24 by a subset-counting DP (object by object), which
# counts the same subsets as direct enumeration; it is cross-checked against brute force.
def overlap_dist_dp(N, M, n):
    # state: (objects chosen, marked objects chosen) -> number of ways
    st = {(0, 0): 1}
    for i in range(N):
        marked = i < M
        nxt = dict(st)
        for (c, r), w in st.items():
            if c < n:
                key = (c + 1, r + (1 if marked else 0))
                nxt[key] = nxt.get(key, 0) + w
        st = nxt
    tot = sum(w for (c, r), w in st.items() if c == n)
    return {r: F(w, tot) for (c, r), w in sorted(st.items()) if c == n}


ok = all(overlap_dist_dp(N, M, n) == overlap_dist_fixed_first(N, M, n)
         for N in range(1, 13) for M in range(N + 1) for n in range(N + 1))
check(ok, "subset-counting DP equals brute-force enumeration for every N<=12")


def exact_mean_24(M, n):
    return mean(overlap_dist_dp(24, M, n))


best = {}
for s in range(2, 25):
    vals = {(M, s - M): exact_mean_24(M, s - M) for M in range(0, s + 1)}
    top = max(vals.values())
    best[s] = sorted(k for k, v in vals.items() if v == top)
log(f"  best splits: { {s: best[s] for s in (12, 13, 20)} }")
check(best[12] == [(6, 6)], "G45 P6: budget 12, the unique best split is 6+6")
check(exact_mean_24(6, 6) == F(3, 2), "G45 P6: its average overlap 36/24 = 3/2")
prods = [M * (12 - M) for M in range(1, 7)]
check(prods == [11, 20, 27, 32, 35, 36], "G45 P6 guide: products 11,20,27,32,35,36")
check([exact_mean_24(M, 12 - M) * 24 for M in range(1, 7)] == prods,
      "G45 P6 guide: those products are 24 x the exact average overlaps")
check(best[13] == [(6, 7), (7, 6)] and exact_mean_24(6, 7) == F(7, 4), "G45 P7: budget 13 -> 6+7 or 7+6, 7/4")
check(best[20] == [(10, 10)] and exact_mean_24(10, 10) == F(25, 6), "G45 P7: budget 20 -> 10+10, 25/6")
check(all(best[s] == sorted({(s // 2, s - s // 2), (s - s // 2, s // 2)}) for s in range(2, 25)),
      "G45 P7: for every budget 2..24 the best splits are floor/ceil of s/2")
ok = all(exact_mean_24(M, n) == F(M * n, 24) for M in range(25) for n in range(25))
check(ok, "G45 P6: supplied formula first*second/total is exact for every pair of catch sizes, N=24")
ok = all(mean(overlap_dist_fixed_first(N, M, n)) == mean(overlap_dist_fixed_first(N, n, M))
         for N in range(1, 11) for M in range(N + 1) for n in range(N + 1))
check(ok, "mean overlap is symmetric in the two catch sizes (N<=10)")
# design theorem on page 1, for all N<=24 and s<=N, via exact means (formula verified above for N<=12)
ok = True
for N in range(2, 25):
    for s in range(2, N + 1):
        vals = {(M, s - M): mean(overlap_dist_dp(N, M, s - M)) for M in range(1, s)}
        top = max(vals.values())
        arg = sorted(k for k, v in vals.items() if v == top)
        ok &= arg == sorted({(s // 2, s - s // 2), (s - s // 2, s // 2)})
check(ok, "Overview design theorem: balanced split maximises exact mean overlap (all N<=24, s<=N)")
ok = all((M + 1) * (n - 1) - M * n == n - M - 1 for M in range(30) for n in range(30))
check(ok, "Overview: moving one unit from n to M changes Mn by n-M-1")
ok = all(4 * M * n == (M + n) ** 2 - (M - n) ** 2 for M in range(30) for n in range(30))
check(ok, "Guide p5: Mn = (s^2 - (M-n)^2)/4")

# P8 and limits
ok = True
N = 6
for A in combinations(range(N), 3):
    for S in combinations(range(N), 3):
        true_r = len(set(A) & set(S))
        for k in range(0, 4):
            for lost in combinations(A, k):
                detected = len((set(A) - set(lost)) & set(S))
                ok &= detected <= true_r
                if detected and true_r:
                    ok &= F(3 * 3, detected) >= F(3 * 3, true_r)
check(ok, "G45 P8 guide: lost marks never raise detected overlap; positive ratio guess can only rise")
check(6 + 6 - 0 == 12 and 6 > 0, "Guide limits: N=M=n=6 with all dots lost shows R=0 -> false bound 12 > 6")
d = overlap_dist_fixed_first(6, 4, 3)
check(d == {1: F(1, 5), 2: F(3, 5), 3: F(1, 5)}, f"Guide limits: N=6,M=4,n=3 overlaps 1,2,3 w.p. 1/5,3/5,1/5")
eg = sum(F(12, r) * p for r, p in d.items())
check(eg == F(34, 5), f"Guide limits: mean ratio guess = {eg} (not 6)")

# ----------------------------------------- live-game shortcut via identity letters
log("")
log("== Live games (P1 both bands) with permanent letters A-X on the objects ==")
log("If the keeper's hidden bag is letters A.. in order, the highest letter ever caught is a")
log("lower bound that equals N whenever the last object turns up in any of the six catches.")
for band, k, Ns in (("G23", 4, (8, 12, 16, 20)), ("G45", 6, (12, 16, 20, 24))):
    for N in Ns:
        miss_one = F(sum(1 for S in combinations(range(N), k) if N - 1 not in S), comb(N, k))
        p_seen = 1 - miss_one ** 6  # six independent uniform catches over three rounds
        exp_union = N * (1 - miss_one ** 6)
        log(f"  {band} N={N:2d}: P(last letter caught in 3 rounds) = {float(p_seen):.3f}; "
            f"expected distinct letters seen = {float(exp_union):.2f}")
log("  (exact: P(an object misses one uniform k-catch) by enumeration, raised to the 6 independent catches)")

log("")
log(f"{len(FAILS)} failures")
(HERE / "check_math.py.out").write_text("\n".join(OUT) + "\n")
print("\n".join(OUT))
sys.exit(1 if FAILS else 0)
