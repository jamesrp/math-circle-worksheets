#!/usr/bin/env python3
"""Checks for the number-strand draft plans, weeks 108-114.

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_number.py
Every small number quoted in week-108 ... week-114 drafts is asserted here.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
import math


# ---------------------------------------------------------------- week 108
def collatz_next(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_orbit(n):
    orbit = [n]
    while n != 1:
        n = collatz_next(n)
        orbit.append(n)
    return orbit


def kaprekar_step(n):
    digits = sorted(f"{n:04d}")
    small = int("".join(digits))
    big = int("".join(reversed(digits)))
    return big - small


def check_week_108():
    # 27 takes 111 steps and peaks at 9232.
    o27 = collatz_orbit(27)
    assert len(o27) - 1 == 111
    assert max(o27) == 9232
    # Small examples quoted in the plan.
    assert collatz_orbit(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert len(collatz_orbit(7)) - 1 == 16 and max(collatz_orbit(7)) == 52
    assert len(collatz_orbit(9)) - 1 == 19
    # Under 30, 27 is the slowest; under 100, 97 is the slowest (118 steps).
    steps = {n: len(collatz_orbit(n)) - 1 for n in range(1, 100)}
    assert max(range(1, 30), key=lambda n: steps[n]) == 27
    assert max(range(1, 100), key=lambda n: steps[n]) == 97 and steps[97] == 118
    # Starts 1..20: the slowest is 18 and 19 (20 steps each).
    assert max(steps[n] for n in range(1, 21)) == 20
    assert [n for n in range(1, 21) if steps[n] == 20] == [18, 19]
    # Every start below 100000 reaches 1 (a tiny version of the computer checks).
    # Each start drops below itself in finitely many steps, so by induction all reach 1.
    for n in range(2, 100000):
        m, k = n, 0
        while m >= n:
            m = collatz_next(m)
            k += 1
        assert k < 400
    # Backward tree from 1: levels of numbers exactly k steps from 1.
    level = {1}
    seen = {1}
    levels = [sorted(level)]
    for _ in range(9):
        new = set()
        for m in level:
            for p in (2 * m, (m - 1) // 3 if (m - 1) % 3 == 0 else None):
                if p and p > 0 and p not in seen and collatz_next(p) == m:
                    new.add(p)
        seen |= new
        level = new
        levels.append(sorted(level))
    assert levels[:6] == [[1], [2], [4], [8], [16], [5, 32]]
    assert levels[6] == [10, 64]
    assert levels[7] == [3, 20, 21, 128]
    assert levels[8] == [6, 40, 42, 256]
    # A number m has an odd parent exactly when m leaves remainder 4 on division by 6.
    for m in range(2, 2000):
        odd_parent = (m - 1) % 3 == 0 and ((m - 1) // 3) % 2 == 1 and (m - 1) // 3 > 1
        assert odd_parent == (m % 6 == 4 and m != 4)
    # Kaprekar: every 4-digit string with two different digits reaches 6174 in at most 7 steps.
    worst = 0
    for n in range(10000):
        if len(set(f"{n:04d}")) == 1:
            continue
        k, m = 0, n
        while m != 6174:
            m = kaprekar_step(m)
            k += 1
            assert k <= 7
        worst = max(worst, k)
    assert worst == 7
    assert kaprekar_step(3524) == 3087 and kaprekar_step(3087) == 8352
    assert kaprekar_step(8352) == 6174 and kaprekar_step(6174) == 6174


# ---------------------------------------------------------------- week 109
def greedy_egyptian(fr):
    out = []
    while fr > 0:
        d = -(-fr.denominator // fr.numerator)
        out.append(d)
        fr -= Fraction(1, d)
    return out


def check_week_109():
    F = Fraction
    # Greedy examples.
    assert greedy_egyptian(F(3, 4)) == [2, 4]
    assert greedy_egyptian(F(4, 5)) == [2, 4, 20]
    assert greedy_egyptian(F(5, 8)) == [2, 8]
    assert greedy_egyptian(F(2, 5)) == [3, 15]
    assert greedy_egyptian(F(3, 7)) == [3, 11, 231]
    assert greedy_egyptian(F(9, 10)) == [2, 3, 15]
    assert greedy_egyptian(F(521, 1050)) == [3, 7, 50]
    assert greedy_egyptian(F(5, 121)) == [25, 757, 763309, 873960180913,
                                          1527612795642093418846225]
    # 5/121 has a three-term representation, so greedy's five terms are not shortest.
    assert F(5, 121) == F(1, 33) + F(1, 121) + F(1, 363)
    # Loaf-sharing identities.
    assert F(2, 3) == F(1, 2) + F(1, 6)
    assert F(3, 5) == F(1, 2) + F(1, 10)
    assert F(5, 6) == F(1, 2) + F(1, 3)
    assert F(9, 10) == F(2, 3) + F(1, 5) + F(1, 30)
    assert F(2, 7) == F(1, 4) + F(1, 28)
    # Splitting identity 1/n = 1/(n+1) + 1/(n(n+1)) and odd 2/n in two pieces.
    for n in range(2, 200):
        assert F(1, n) == F(1, n + 1) + F(1, n * (n + 1))
    for m in range(1, 100):
        n = 2 * m + 1
        assert F(2, n) == F(1, m + 1) + F(1, n * (m + 1))
    # Monovariant: each greedy step strictly lowers the numerator (in lowest terms).
    for b in range(2, 60):
        for a in range(1, b):
            fr = F(a, b)
            while fr > 0:
                d = -(-fr.denominator // fr.numerator)
                nxt = fr - F(1, d)
                assert nxt == 0 or nxt.numerator < fr.numerator
                fr = nxt
            assert len(greedy_egyptian(F(a, b))) <= F(a, b).numerator
    # Fraction strips: halves, thirds, quarters, sixths, twelfths, one of each.
    strips = [2, 3, 4, 6, 12]
    made = set()
    for r in range(1, 6):
        for c in combinations(strips, r):
            made.add(sum(F(1, d) for d in c))
    twelfths = [k for k in range(1, 12) if F(k, 12) in made]
    assert twelfths == list(range(1, 12))
    # Erdos-Straus for small n: 4/n = 1/a + 1/b + 1/c with a <= b <= c.
    def es(n):
        target = F(4, n)
        for a in range(n // 4 + 1, 3 * n // 4 + 2):
            r1 = target - F(1, a)
            if r1 <= 0:
                continue
            for b in range(max(a, -(-r1.denominator // r1.numerator)),
                           int(2 / r1) + 2):
                r2 = r1 - F(1, b)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= b:
                    return (a, b, r2.denominator)
        return None
    for n in range(2, 121):
        assert es(n) is not None, n
    assert F(4, 5) == F(1, 2) + F(1, 4) + F(1, 20)
    assert F(4, 7) == F(1, 2) + F(1, 15) + F(1, 210)


# ---------------------------------------------------------------- week 110
FIBS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


def zeck_reps(n, allow_neighbours=False):
    """All sets of distinct Fibonacci numbers (1,2,3,5,...) summing to n."""
    fibs = [f for f in FIBS if f <= n]
    reps = []
    for r in range(1, len(fibs) + 1):
        for idx in combinations(range(len(fibs)), r):
            if sum(fibs[i] for i in idx) != n:
                continue
            if not allow_neighbours and any(idx[j + 1] - idx[j] == 1 for j in range(r - 1)):
                continue
            reps.append(tuple(fibs[i] for i in idx))
    return reps


def zeck_greedy(n):
    out = []
    for f in reversed(FIBS):
        if f <= n:
            out.append(f)
            n -= f
    return out


def check_week_110():
    for n in range(1, 144):
        reps = zeck_reps(n)
        assert len(reps) == 1, n
        assert sorted(reps[0], reverse=True) == zeck_greedy(n)
    assert zeck_reps(20) == [(2, 5, 13)]
    assert zeck_reps(12) == [(1, 3, 8)]
    # Without the neighbour rule, 8 and 13 have three ways and 16 has four.
    assert zeck_reps(8, True) == [(8,), (3, 5), (1, 2, 5)]
    assert len(zeck_reps(13, True)) == 3
    assert zeck_reps(16, True) == [(3, 13), (1, 2, 13), (3, 5, 8), (1, 2, 5, 8)]
    assert zeck_reps(16) == [(3, 13)]
    # Coins 1,2,3,5,8,13 with the no-neighbour rule make exactly 1..20.
    coins = [1, 2, 3, 5, 8, 13]
    amounts = set()
    for r in range(1, 7):
        for idx in combinations(range(6), r):
            if any(idx[j + 1] - idx[j] == 1 for j in range(r - 1)):
                continue
            amounts.add(sum(coins[i] for i in idx))
    assert amounts == set(range(1, 21))

    # Fibonacci Nim: pile n, first move takes 1..n-1, later moves at most twice the last.
    @lru_cache(maxsize=None)
    def win(n, quota):
        return any(not win(n - t, 2 * t) for t in range(1, min(quota, n) + 1))

    losing_starts = [n for n in range(2, 60) if not win(n, n - 1)]
    assert losing_starts == [f for f in FIBS if 2 <= f < 60]
    # The Zeckendorf move (take the smallest part) wins whenever the quota allows it.
    for n in range(2, 60):
        for quota in range(1, n + 1):
            small = min(zeck_greedy(n))
            if small <= quota:
                assert win(n, quota)
                assert small == n or not win(n - small, 2 * small)
            else:
                assert not win(n, quota)
    # Example game from 20: Zeckendorf 13+5+2, so the first player takes 2.
    assert zeck_greedy(20) == [13, 5, 2] and not win(18, 4)

    # Zeckendorf game (Baird-Smith, Epstein, Flint, Miller): start with n ones.
    def moves(state):
        # state: tuple of counts c[i] of F_(i+1), index 0 is value 1.
        c = list(state)
        L = len(c)
        res = []
        for i in range(L):
            if c[i] >= 2:
                d = c[:]
                d[i] -= 2
                if i == 0:
                    d[1] += 1                      # 1+1 -> 2
                elif i == 1:
                    d[0] += 1; d[2] += 1           # 2+2 -> 1+3
                else:
                    d[i - 2] += 1; d[i + 1] += 1   # 2F_i -> F_(i-2) + F_(i+1)
                res.append(tuple(d))
            if i + 1 < L - 1 and c[i] >= 1 and c[i + 1] >= 1:
                d = c[:]
                d[i] -= 1; d[i + 1] -= 1; d[i + 2] += 1
                res.append(tuple(d))
        return res

    def solve(n):
        L = len([f for f in FIBS if f <= n]) + 2
        vals = FIBS[:L]

        @lru_cache(maxsize=None)
        def mover_wins(state):
            ms = moves(state)
            return any(not mover_wins(s) for s in ms)

        @lru_cache(maxsize=None)
        def terminal(state):
            ms = moves(state)
            if not ms:
                return {state}
            out = set()
            for s in ms:
                out |= terminal(s)
            return out

        start = tuple([n] + [0] * (L - 1))
        ends = terminal(start)
        assert len(ends) == 1
        end = next(iter(ends))
        assert sorted((vals[i] for i in range(L) for _ in range(end[i])), reverse=True) == zeck_greedy(n)
        return mover_wins(start)

    for n in range(3, 13):
        assert solve(n) is False, n   # the second player wins


# ---------------------------------------------------------------- week 111
def consecutive_ways(n):
    """Runs of two or more consecutive positive whole numbers adding to n."""
    ways = []
    for start in range(1, n):
        s, k = 0, start
        while s < n:
            s += k
            k += 1
        if s == n and k - start >= 2:
            ways.append(list(range(start, k)))
    return ways


def odd_divisors_above_one(n):
    return [d for d in range(3, n + 1, 2) if n % d == 0]


def check_week_111():
    for n in range(1, 513):
        w = consecutive_ways(n)
        assert len(w) == len(odd_divisors_above_one(n)), n
        assert (len(w) == 0) == (n & (n - 1) == 0)
    assert [n for n in range(1, 65) if not consecutive_ways(n)] == [1, 2, 4, 8, 16, 32, 64]
    assert consecutive_ways(15) == [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
    assert consecutive_ways(9) == [[2, 3, 4], [4, 5]]
    assert len(consecutive_ways(30)) == 3
    counts = {n: len(consecutive_ways(n)) for n in range(1, 101)}
    assert max(counts.values()) == 5
    assert [n for n in counts if counts[n] == 5] == [45, 63, 75, 90, 99]
    assert counts[45] == 5
    # Numbers 1..20 that cannot be built: 1, 2, 4, 8, 16.
    assert [n for n in range(1, 21) if not consecutive_ways(n)] == [1, 2, 4, 8, 16]
    # Odd numbers 2m+1 are always m + (m+1); 3 consecutive give the multiples of 3 from 6.
    for m in range(1, 50):
        assert [m, m + 1] in consecutive_ways(2 * m + 1)
    assert sorted(sum(range(a, a + 3)) for a in range(1, 10)) == list(range(6, 33, 3))
    # Pairing: a run of length k with odd k is centred on n/k; with even k, its
    # middle pair adds to the odd number 2n/k. Each odd divisor > 1 gives exactly one run.
    for n in range(3, 300):
        runs = consecutive_ways(n)
        tags = set()
        for r in runs:
            k = len(r)
            tags.add(k if k % 2 == 1 else (2 * n) // k)
        assert tags == set(odd_divisors_above_one(n)), n


# ---------------------------------------------------------------- week 112
def euclid_rhythm(k, n):
    """Onsets at floor(i*n/k), i = 0..k-1, as a string of x and dots."""
    on = {(i * n) // k for i in range(k)}
    return "".join("x" if j in on else "." for j in range(n))


def rotations(s):
    return {s[i:] + s[:i] for i in range(len(s))}


def gaps(s):
    idx = [i for i, ch in enumerate(s) if ch == "x"]
    n = len(s)
    return [(idx[(j + 1) % len(idx)] - idx[j]) % n or n for j in range(len(idx))]


def spread_ok(s, k):
    n = len(s)
    idx = [i for i, ch in enumerate(s) if ch == "x"]
    for j in range(1, k):
        lo, hi = (j * n) // k, -(-(j * n) // k)
        for a in range(k):
            dist = (idx[(a + j) % k] - idx[a]) % n
            if dist not in (lo, hi):
                return False
    return True


def evenness(s):
    n = len(s)
    idx = [i for i, ch in enumerate(s) if ch == "x"]
    return sum(2 * math.sin(math.pi * abs(a - b) / n) for a, b in combinations(idx, 2))


def check_week_112():
    assert "x..x..x." in rotations(euclid_rhythm(3, 8))
    assert "x.xx.xx." in rotations(euclid_rhythm(5, 8))
    assert "x.x.." in rotations(euclid_rhythm(2, 5))
    assert "x.xx" in rotations(euclid_rhythm(3, 4))
    assert gaps("x..x..x.") == [3, 3, 2]
    assert gaps("x.xxx.") == [2, 1, 1, 2] and not spread_ok("x.xxx.", 4)
    assert spread_ok("xx.xx.", 4)
    # Uniqueness up to rotation: among all k-onset patterns on n spots, those whose
    # gaps are all floor(n/k) or ceil(n/k) form one rotation class, and the same
    # class maximises evenness (Demaine et al. 2009, Theorem 4.1), checked n <= 12.
    for n in range(2, 13):
        for k in range(1, n + 1):
            pats = []
            for c in combinations(range(n), k):
                pats.append("".join("x" if j in c else "." for j in range(n)))
            lo, hi = n // k, -(-n // k)
            e = euclid_rhythm(k, n)
            # Next-clap gaps alone do not decide it: x.xxx. and xx.xx. both use gaps 1, 2.
            gap_ok = {p for p in pats if all(g in (lo, hi) for g in gaps(p))}
            assert rotations(e) <= gap_ok
            # Every clap-to-jth-next-clap distance within floor/ceil of j*n/k does decide it.
            good = {p for p in pats if spread_ok(p, k)}
            assert good == rotations(e), (k, n)
            if k >= 2:
                best = max(evenness(p) for p in pats)
                winners = {p for p in pats if abs(evenness(p) - best) < 1e-9}
                assert winners == rotations(e), (k, n)
            # Swapping claps and rests gives the rhythm with n - k claps.
            comp = e.replace("x", "o").replace(".", "x").replace("o", ".")
            if 0 < k < n:
                assert comp in rotations(euclid_rhythm(n - k, n))
            # A common factor d repeats a smaller rhythm d times.
            d = math.gcd(k, n)
            small = euclid_rhythm(k // d, n // d)
            assert (small * d) in rotations(e)
    # 3 claps in 8 spots: 56 patterns, 7 rotation classes, 5 if flips also allowed.
    pats = ["".join("x" if j in c else "." for j in range(8)) for c in combinations(range(8), 3)]
    assert len(pats) == 56
    classes = {min(rotations(p)) for p in pats}
    assert len(classes) == 7
    bracelets = {min(rotations(p) | rotations(p[::-1])) for p in pats}
    assert len(bracelets) == 5
    # 4 claps in 12 spots spread evenly: x..x..x..x.. (gcd 4).
    assert euclid_rhythm(4, 12) == "x..x..x..x.."
    assert sorted(gaps(euclid_rhythm(5, 12))) == [2, 2, 2, 3, 3]
    assert "x..x.x..x.x." in rotations(euclid_rhythm(5, 12))
    assert sorted(gaps(euclid_rhythm(7, 12))) == [1, 1, 2, 2, 2, 2, 2]


# ---------------------------------------------------------------- week 113
SYMS = [
    lambda r, c, n: (r, c), lambda r, c, n: (c, n - 1 - r),
    lambda r, c, n: (n - 1 - r, n - 1 - c), lambda r, c, n: (n - 1 - c, r),
    lambda r, c, n: (r, n - 1 - c), lambda r, c, n: (n - 1 - r, c),
    lambda r, c, n: (c, r), lambda r, c, n: (n - 1 - c, n - 1 - r),
]


def is_magic(sq):
    n = len(sq)
    s = sum(sq[0])
    lines = [list(row) for row in sq] + [[sq[r][c] for r in range(n)] for c in range(n)]
    lines += [[sq[i][i] for i in range(n)], [sq[i][n - 1 - i] for i in range(n)]]
    return all(sum(line) == s for line in lines)


def check_week_113():
    for n, m in [(3, 15), (4, 34), (5, 65)]:
        assert n * (n * n + 1) // 2 == m
    squares = []
    for p in permutations(range(1, 10)):
        sq = [p[0:3], p[3:6], p[6:9]]
        if is_magic(sq):
            squares.append(tuple(p))
    assert len(squares) == 8
    assert all(s[4] == 5 for s in squares)
    lo_shu = (4, 9, 2, 3, 5, 7, 8, 1, 6)
    assert lo_shu in squares
    orbit = set()
    for f in SYMS:
        img = [0] * 9
        for r in range(3):
            for c in range(3):
                r2, c2 = f(r, c, 3)
                img[3 * r2 + c2] = lo_shu[3 * r + c]
        orbit.add(tuple(img))
    assert orbit == set(squares)
    # The eight triples from 1..9 adding to 15; how many contain each number.
    triples = [t for t in combinations(range(1, 10), 3) if sum(t) == 15]
    assert len(triples) == 8
    count = {k: sum(k in t for t in triples) for k in range(1, 10)}
    assert count == {1: 2, 2: 3, 3: 2, 4: 3, 5: 4, 6: 3, 7: 2, 8: 3, 9: 2}
    # The eight lines of the Lo Shu are exactly these triples (Pick-15 = tic-tac-toe).
    g = [lo_shu[0:3], lo_shu[3:6], lo_shu[6:9]]
    lines = [tuple(sorted(row)) for row in g]
    lines += [tuple(sorted(g[r][c] for r in range(3))) for c in range(3)]
    lines += [tuple(sorted(g[i][i] for i in range(3))), tuple(sorted(g[i][2 - i] for i in range(3)))]
    assert sorted(lines) == sorted(triples)
    # The 8 line positions of a 3x3 grid are 8 of the 12 lines of the plane mod 3.
    cells = [(r, c) for r in range(3) for c in range(3)]
    aff = set()
    for p0 in cells:
        for v in [(0, 1), (1, 0), (1, 1), (1, 2)]:
            aff.add(frozenset(((p0[0] + t * v[0]) % 3, (p0[1] + t * v[1]) % 3) for t in range(3)))
    assert len(aff) == 12
    grid_lines = [frozenset((r, c) for c in range(3)) for r in range(3)]
    grid_lines += [frozenset((r, c) for r in range(3)) for c in range(3)]
    grid_lines += [frozenset((i, i) for i in range(3)), frozenset((i, 2 - i) for i in range(3))]
    assert all(l in aff for l in grid_lines) and len(set(grid_lines)) == 8
    # Rows only (no diagonal or column rule): 1..9 into rows of 15 in many ways.
    row_only = sum(1 for p in permutations(range(1, 10))
                   if sum(p[0:3]) == sum(p[3:6]) == sum(p[6:9]) == 15)
    assert row_only == 2592
    # Duerer's square from Melencolia I.
    d = [(16, 3, 2, 13), (5, 10, 11, 8), (9, 6, 7, 12), (4, 15, 14, 1)]
    assert is_magic(d) and sum(d[0]) == 34
    assert (d[3][1], d[3][2]) == (15, 14)
    assert d[0][0] + d[0][3] + d[3][0] + d[3][3] == 34
    assert d[1][1] + d[1][2] + d[2][1] + d[2][2] == 34
    assert sorted(x for row in d for x in row) == list(range(1, 17))


# ---------------------------------------------------------------- week 114
def check_week_114():
    phi = (1 + 5 ** 0.5) / 2
    golden = 360 * (1 - 1 / phi)
    assert abs(golden - 137.5077640) < 1e-6
    assert abs(360 / phi ** 2 - golden) < 1e-9
    # Rational turns p/q (lowest terms) put seeds on exactly q spokes.
    for p, q in [(1, 4), (1, 3), (2, 5), (3, 8), (5, 13), (1, 2)]:
        spokes = {(i * p) % q for i in range(200)}
        assert len(spokes) == q
    # Fibonacci-ratio turns approach the golden turn.
    approx = [(1, 2), (1, 3), (2, 5), (3, 8), (5, 13), (8, 21), (13, 34)]
    angles = [360 * p / q for p, q in approx]
    assert [round(a, 1) for a in angles] == [180.0, 120.0, 144.0, 135.0, 138.5, 137.1, 137.6]
    errs = [abs(a - golden) for a in angles]
    assert all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    # Vogel model: seed i at radius sqrt(i), angle i * golden. The nearest
    # neighbour of an outer seed is i +/- a Fibonacci number.
    pts = [(math.sqrt(i) * math.cos(math.radians(i * golden)),
            math.sqrt(i) * math.sin(math.radians(i * golden))) for i in range(1, 1001)]
    fib = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}
    diffs = set()
    for i in range(10, 900):
        xi, yi = pts[i - 1]
        best = min((j for j in range(1, 1001) if j != i),
                   key=lambda j: (pts[j - 1][0] - xi) ** 2 + (pts[j - 1][1] - yi) ** 2)
        diffs.add(abs(best - i))
    assert diffs == {8, 13, 21, 34, 55, 89}
    # With a turn of 1/4 (90 degrees), 30 seeds sit on 4 spokes, 8 or 7 per spoke.
    per = [sum(1 for i in range(30) if i % 4 == s) for s in range(4)]
    assert per == [8, 8, 7, 7]
    # Swinton et al. 2016 counts (cited): 565 + 67 = 632 of 768, about 82%.
    assert 565 + 67 == 632 and round(100 * 632 / 768) == 82 and 768 - 632 == 136


def main():
    for name, fn in [("108", check_week_108), ("109", check_week_109),
                     ("110", check_week_110), ("111", check_week_111),
                     ("112", check_week_112), ("113", check_week_113),
                     ("114", check_week_114)]:
        fn()
        print(f"week {name}: ok")


if __name__ == "__main__":
    main()
