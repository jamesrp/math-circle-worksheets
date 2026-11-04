#!/usr/bin/env python3
"""Checks for the draft plans of weeks 157-163 (number and symmetry, second set).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_number_symmetry_2.py
Every small number quoted in the week-157 ... week-163 drafts is asserted here.
"""

from itertools import permutations, product
import cmath
import math


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# ---------------------------------------------------------------- week 157
def long_division(num, den, steps):
    """Digits and remainders of num/den after the decimal point (0 < num < den)."""
    digits, rems = [], []
    r = num
    for _ in range(steps):
        rems.append(r)
        r *= 10
        digits.append(r // den)
        r %= den
    return digits, rems


def period(den):
    """Length of the repeating block of 1/den, for den coprime to 10."""
    r, k = 10 % den, 1
    while r != 1:
        r = r * 10 % den
        k += 1
    return k


def check_week_157():
    # 1/7 = 0.142857 142857 ..., remainders 1, 3, 2, 6, 4, 5 then back to 1.
    digits, rems = long_division(1, 7, 12)
    assert digits == [1, 4, 2, 8, 5, 7] * 2
    assert rems[:7] == [1, 3, 2, 6, 4, 5, 1]
    # Every remainder 1..6 appears once in a cycle, so 2/7 starts at remainder 2, etc.
    for k in range(1, 7):
        d, _ = long_division(k, 7, 6)
        start = rems.index(k)
        assert d == (digits[start:] + digits[:start])[:6]
    # 142857 times 1..6 rotates its digits; times 7 gives 999999.
    c = 142857
    rotations = {str(c)[i:] + str(c)[:i] for i in range(6)}
    for m in range(1, 7):
        assert str(c * m) in rotations
    assert c * 7 == 999999
    # Periods for small primes; the period always divides p - 1.
    expected = {3: 1, 7: 6, 11: 2, 13: 6, 17: 16, 19: 18, 23: 22, 29: 28,
                31: 15, 37: 3, 41: 5, 43: 21, 47: 46, 53: 13, 59: 58, 61: 60,
                67: 33, 71: 35, 73: 8, 79: 13, 83: 41, 89: 44, 97: 96}
    for p, k in expected.items():
        assert period(p) == k
    for p in range(3, 2000):
        if is_prime(p) and p != 5:
            assert (p - 1) % period(p) == 0
    # Full-period primes below 100 (OEIS A001913).
    full = [p for p in range(3, 100) if is_prime(p) and p != 5 and period(p) == p - 1]
    assert full == [7, 17, 19, 23, 29, 47, 59, 61, 97]
    # 1/13 has period 6, so its 12 remainders split into two wheels of 6.
    _, r13 = long_division(1, 13, 6)
    _, r13b = long_division(2, 13, 6)
    assert sorted(r13) == [1, 3, 4, 9, 10, 12]
    assert sorted(r13b) == [2, 5, 6, 7, 8, 11]
    # 1/41 repeats 02439 (period 5): 40 / 5 = 8 wheels.
    d41, _ = long_division(1, 41, 5)
    assert d41 == [0, 2, 4, 3, 9] and period(41) == 5
    # The 1/17 cyclic number times 1..16 rotates digits.
    c17 = (10 ** 16 - 1) // 17
    s17 = f"{c17:016d}"
    assert s17 == "0588235294117647"
    rot17 = {s17[i:] + s17[:i] for i in range(16)}
    for m in range(1, 17):
        assert f"{c17 * m:016d}" in rot17
    # A remainder wheel for 7: the rule "times 10, keep the remainder" is "times 3".
    assert all(10 * r % 7 == 3 * r % 7 for r in range(7))
    # Sharing 1 cookie among 7 takes 6 rounds before the leftover is 1 again, and the
    # most counters ever dealt in one round is 60 (leftover 6, traded for 60).
    assert rems.index(1, 1) == 6
    assert max(10 * r for r in rems[:6]) == 60
    # 10 counters onto 3 plates: 3 each, 1 left (period 1).
    assert divmod(10, 3) == (3, 1) and period(3) == 1
    # Plate counts up to 30 (no factor 2 or 5) that repeat after exactly 2 rounds: 11.
    assert [n for n in range(3, 31) if math.gcd(n, 10) == 1 and period(n) == 2] == [11]
    # Starting the 7-wheel at remainder 2 reads 285714.
    assert long_division(2, 7, 6)[0] == [2, 8, 5, 7, 1, 4]


# ---------------------------------------------------------------- week 158
def two_square_ways(n):
    """Pairs (a, b) with 0 <= a <= b and a^2 + b^2 = n."""
    out = []
    a = 0
    while 2 * a * a <= n:
        b2 = n - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            out.append((a, b))
        a += 1
    return out


def zagier_set(p):
    return [(x, y, z) for x in range(1, math.isqrt(p) + 1)
            for y in range(1, p) for z in range(1, p)
            if x * x + 4 * y * z == p]


def zagier_map(t):
    x, y, z = t
    if x < y - z:
        return (x + 2 * z, z, y - x - z)
    if x < 2 * y:
        return (2 * y - x, y, x - y + z)
    return (x - 2 * y, x - y + z, y)


def check_week_158():
    # Totals up to 50 that are a sum of two squares (0 allowed), OEIS A001481.
    yes = [n for n in range(0, 51) if two_square_ways(n)]
    assert yes == [0, 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25, 26, 29, 32,
                   34, 36, 37, 40, 41, 45, 49, 50]
    # Using two non-empty squares (both at least 1) up to 50.
    pos = [n for n in range(1, 51) if any(a >= 1 for a, b in two_square_ways(n))]
    assert pos == [2, 5, 8, 10, 13, 17, 18, 20, 25, 26, 29, 32, 34, 37, 40, 41,
                   45, 50]
    # 1 to 20: 3, 6, 7, 11, 12, 14, 15, 19 never work (with 0 allowed).
    assert [n for n in range(1, 21) if not two_square_ways(n)] == \
        [3, 6, 7, 11, 12, 14, 15, 19]
    # A square number is 0 or 1 mod 4, so a sum of two is 0, 1 or 2 mod 4: never 3.
    assert {a * a % 4 for a in range(100)} == {0, 1}
    assert all(not two_square_ways(n) for n in range(3, 2000, 4))
    # Fermat: an odd prime is a sum of two squares iff it is 1 mod 4, in exactly one way.
    for p in range(3, 3000):
        if is_prime(p):
            w = two_square_ways(p)
            assert (len(w) == 1) == (p % 4 == 1)
            assert len(w) <= 1
    # Examples quoted.
    assert two_square_ways(25) == [(0, 5), (3, 4)]
    assert two_square_ways(50) == [(1, 7), (5, 5)]
    assert two_square_ways(65) == [(1, 8), (4, 7)]
    assert two_square_ways(29) == [(2, 5)] and two_square_ways(13) == [(2, 3)]
    # Up to 50, the totals with two different builds (0 allowed) are 25 and 50.
    assert [n for n in range(1, 51) if len(two_square_ways(n)) >= 2] == [25, 50]
    # The general rule: 45 = 9 x 5 = 36 + 9 works, 21 = 3 x 7 does not; 43, 47 fail.
    assert two_square_ways(45) == [(3, 6)] and not two_square_ways(21)
    assert not two_square_ways(43) and not two_square_ways(47)
    assert all(not two_square_ways(p) for p in [3, 7, 11, 19, 23])
    assert all(len(two_square_ways(p)) == 1 for p in [5, 13, 17, 29, 37, 41])
    # First total that is a sum of two non-zero squares in two ways: 50.
    first_two = min(n for n in range(1, 200)
                    if sum(1 for a, b in two_square_ways(n) if a >= 1) >= 2)
    assert first_two == 50
    # Zagier's involution: windmills x^2 + 4yz = p, one fixed point, odd count.
    for p in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]:
        S = zagier_set(p)
        Sset = set(S)
        assert all(zagier_map(t) in Sset for t in S)
        assert all(zagier_map(zagier_map(t)) == t for t in S)
        fixed = [t for t in S if zagier_map(t) == t]
        k = (p - 1) // 4
        assert fixed == [(1, 1, k)]
        assert len(S) % 2 == 1
        # The obvious swap (x, y, z) -> (x, z, y) then has a fixed point y = z.
        sym = [t for t in S if t[1] == t[2]]
        assert len(sym) == 1
        x, y, _ = sym[0]
        assert x * x + (2 * y) ** 2 == p
    # Windmill counts for 13 and 29 quoted in the plan.
    assert len(zagier_set(13)) == 3 and len(zagier_set(29)) == 5
    # The identity behind combining: (a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2.
    assert (1 + 4) * (4 + 9) == 65 == (2 - 6) ** 2 + (3 + 4) ** 2 == 1 + 64


# ---------------------------------------------------------------- week 159
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def rectangles(n):
    """Rectangles a x b with a <= b and a * b = n (a turned rectangle counts once)."""
    return [(a, n // a) for a in range(1, math.isqrt(n) + 1) if n % a == 0]


def proper_sum(n):
    return sum(divisors(n)) - n


def check_week_159():
    assert rectangles(12) == [(1, 12), (2, 6), (3, 4)]
    assert rectangles(24) == [(1, 24), (2, 12), (3, 8), (4, 6)]
    assert rectangles(36) == [(1, 36), (2, 18), (3, 12), (4, 9), (6, 6)]
    # Up to 50, the most rectangles: 5, for 36 and 48.
    best = max(len(rectangles(n)) for n in range(1, 51))
    assert best == 5
    assert [n for n in range(1, 51) if len(rectangles(n)) == 5] == [36, 48]
    # Only one rectangle (a single row) exactly for 1 and the primes.
    assert all((len(rectangles(n)) == 1) == (n == 1 or is_prime(n))
               for n in range(1, 200))
    # A square number of tiles is the only way to get an odd number of divisors.
    assert all((len(divisors(n)) % 2 == 1) == (math.isqrt(n) ** 2 == n)
               for n in range(1, 500))
    # Perfect numbers below 10000.
    perfect = [n for n in range(2, 10000) if proper_sum(n) == n]
    assert perfect == [6, 28, 496, 8128]
    # Up to 30: abundant 12, 18, 20, 24, 30; perfect 6, 28; the rest deficient.
    ab = [n for n in range(1, 31) if proper_sum(n) > n]
    assert ab == [12, 18, 20, 24, 30]
    assert proper_sum(12) == 16 and proper_sum(28) == 28 and proper_sum(15) == 9
    # Up to 100: 22 abundant, 2 perfect, 76 deficient; the smallest odd abundant is 945.
    cnt = {"a": 0, "p": 0, "d": 0}
    for n in range(1, 101):
        s = proper_sum(n)
        cnt["a" if s > n else "p" if s == n else "d"] += 1
    assert cnt == {"a": 22, "p": 2, "d": 76}
    assert min(n for n in range(1, 1000, 2) if proper_sum(n) > n) == 945
    # Only a line and a square: p x p for a prime p (below 100: 4, 9, 25, 49).
    assert [n for n in range(2, 100) if len(rectangles(n)) == 2
            and math.isqrt(n) ** 2 == n] == [4, 9, 25, 49]
    # Below 30 the largest excess of the divisor tower is 24's: 36, 12 above itself.
    assert max(range(1, 30), key=lambda n: proper_sum(n) - n) == 24
    assert proper_sum(24) == 36
    # Every prime is deficient (proper divisor sum 1), every power of 2 just misses.
    assert all(proper_sum(2 ** k) == 2 ** k - 1 for k in range(1, 15))
    # Euclid: 2^(p-1)(2^p - 1) with 2^p - 1 prime gives 6, 28, 496, 8128, 33550336.
    euclid = [2 ** (p - 1) * (2 ** p - 1) for p in range(2, 14) if is_prime(2 ** p - 1)]
    assert euclid == [6, 28, 496, 8128, 33550336]
    # 2^11 - 1 = 2047 = 23 * 89 is not prime, so p prime is not enough.
    assert 2 ** 11 - 1 == 23 * 89
    # 1 + 2 + 4 + 8 = 15 is not prime, and 15 x 8 = 120 is abundant, not perfect.
    assert 15 * 8 == 120 and proper_sum(120) == 240
    # 1 + 2 + 4 + 8 + 16 = 31 is prime, and 31 x 16 = 496 is perfect.
    assert 31 * 16 == 496 and proper_sum(496) == 496
    # Doubling picture: 28 = 1+2+4+7+14 and 1+2+4 = 7.
    assert divisors(28)[:-1] == [1, 2, 4, 7, 14] and 1 + 2 + 4 == 7
    # Every multiple of 6 above 6 is abundant (6 is perfect), checked to 3000.
    assert all(proper_sum(n) > n for n in range(12, 3000, 6))
    # 1 + 2 + 3 = 6 and 1 + 2 + 3 + ... + 7 = 28 (both triangular).
    assert sum(range(1, 4)) == 6 and sum(range(1, 8)) == 28 and sum(range(1, 32)) == 496


# ---------------------------------------------------------------- week 160
def chords(n, k):
    """Distinct chords {i, k*i mod n} with i != k*i mod n."""
    return {frozenset((i, k * i % n)) for i in range(n) if i != k * i % n}


def orbit_of_one(n, k):
    seen, x = [], 1 % n
    while x not in seen:
        seen.append(x)
        x = k * x % n
    return seen, x


def check_week_160():
    # Ten nails, times 2: 0 stays, 5 goes to 0, two strings land on each even nail.
    assert [2 * i % 10 for i in range(10)] == [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]
    assert len(chords(10, 2)) == 9
    # 24 nails, times 2: 23 strings but 8-16 is drawn twice, so 22 distinct chords.
    assert len(chords(24, 2)) == 22
    # Times 3 on 24 nails: fixed nails 0 and 12, so 22 strings, but 3-9, 6-18
    # and 15-21 are each drawn twice, leaving 19 distinct chords.
    assert [i for i in range(24) if 3 * i % 24 == i] == [0, 12]
    assert [i for i in range(24) if 9 * i % 24 == i and 3 * i % 24 != i] == \
        [3, 6, 9, 15, 18, 21]
    assert len(chords(24, 3)) == 19
    # Following one string after another from 1 on 10 nails.
    assert orbit_of_one(10, 3) == ([1, 3, 9, 7], 1)
    assert orbit_of_one(10, 9) == ([1, 9], 1)
    assert orbit_of_one(10, 2) == ([1, 2, 4, 8, 6], 2)
    assert [k for k in range(1, 10) if orbit_of_one(10, k) == (orbit_of_one(10, k)[0], 1)
            and len(orbit_of_one(10, k)[0]) == 4] == [3, 7]
    # Even notches 2, 4, 6, 8 each receive two strings; 60 dots times 2: 59 strings.
    ends = [2 * i % 10 for i in range(1, 10)]
    assert all(ends.count(e) == 2 for e in (2, 4, 6, 8)) and all(e % 2 == 0 for e in ends)
    assert sum(1 for i in range(60) if 2 * i % 60 != i) == 59
    # On 24 nails every multiplier sharing no factor with 24 closes up after 2 steps.
    units = [k for k in range(1, 24) if math.gcd(k, 24) == 1]
    assert units == [1, 5, 7, 11, 13, 17, 19, 23]
    assert all(k * k % 24 == 1 for k in units)
    # 24 is the largest n with that property (checked to 2000).
    good = [n for n in range(2, 2000)
            if all(k * k % n == 1 for k in range(1, n) if math.gcd(k, n) == 1)]
    assert good == [2, 3, 4, 6, 8, 12, 24]
    # Times (n - 1) gives parallel chords: i and n - i are mirror images across nail 0.
    n = 24
    for i in range(1, n):
        a = cmath.exp(2j * math.pi * i / n)
        b = cmath.exp(2j * math.pi * ((n - 1) * i % n) / n)
        assert abs((a - b).real) < 1e-9          # every chord is vertical
    # Times (n + 1) draws nothing: every nail goes to itself.
    assert chords(24, 25) == set()
    # Envelope: the chord from angle t to angle k t touches the curve
    # P(t) = (k e^{it} + e^{ikt}) / (k + 1), an epicycloid with k - 1 cusps.
    for k in [2, 3, 4, 5]:
        for step in range(1, 200):
            t = 2 * math.pi * step / 200 + 0.001
            A, B = cmath.exp(1j * t), cmath.exp(1j * k * t)
            P = (k * A + B) / (k + 1)
            d = B - A
            # P lies on the chord: (P - A) is a real multiple of d.
            assert abs(((P - A) / d).imag) < 1e-9
            # P'(t) is parallel to the chord, so the chord is tangent there.
            dP = 1j * k * (A + B) / (k + 1)
            if abs(dP) > 1e-6:
                assert abs((dP / d).imag) < 1e-6
        # Cusps where P'(t) = 0, that is e^{i(k-1)t} = -1: t = (pi + 2 pi j)/(k - 1),
        # which gives k - 1 values in one turn; P' is non-zero at every other sample.
        cusp_ts = [(math.pi + 2 * math.pi * j) / (k - 1) for j in range(k - 1)]
        assert len(cusp_ts) == k - 1 and all(0 < t < 2 * math.pi for t in cusp_ts)
        for t in cusp_ts:
            assert abs(cmath.exp(1j * t) + cmath.exp(1j * k * t)) < 1e-9
        for m in range(1000):
            t = 2 * math.pi * m / 1000
            if min(abs(t - c) for c in cusp_ts) > 0.01:
                assert abs(cmath.exp(1j * t) + cmath.exp(1j * k * t)) > 1e-4
    # Times 2: 1 cusp (cardioid); times 3: 2 cusps (nephroid).


# ---------------------------------------------------------------- week 161
def check_week_161():
    # Trihexaflexagon: 3 faces x 6 triangles = 18 triangle sides = 9 triangles x 2,
    # folded from a strip of 10 triangles (one is a glue tab).
    assert 3 * 6 == 9 * 2 and 9 + 1 == 10
    # Hexahexaflexagon: 6 faces x 6 = 36 = 18 triangles x 2; strip of 19 with the tab.
    assert 6 * 6 == 18 * 2 and 18 + 1 == 19
    # Anderson et al. (2010): with pinch flexes an order-3n flexagon has 6n - 3
    # mathematical faces: 3 for the trihexa (n = 1), 9 for the hexahexa (n = 2).
    assert [6 * n - 3 for n in (1, 2)] == [3, 9]
    # Tuckerman-diagram model of the hexahexaflexagon: a central triangle 1-2-3 with
    # a triangle on each side bringing in faces 4, 5, 6.  States (top and bottom
    # colours) are the diagram's edges, and a pinch flex moves within a triangle.
    tris = [(1, 2, 3), (1, 2, 4), (2, 3, 5), (3, 1, 6)]
    edges = {frozenset(e) for t in tris for e in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0]))}
    assert len(edges) == 9            # matches 6n - 3 = 9
    count = {f: sum(f in t for t in tris) for f in range(1, 7)}
    assert count == {1: 3, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1}   # Gardner's 3-to-1 ratio
    # Faces 4, 5, 6 never show together with each other (no edge joins them).
    assert not any(e <= {4, 5, 6} for e in edges)
    # Trihexaflexagon model: one triangle 1-2-3, three states, each face in two.
    tri_edges = {frozenset(e) for e in ((1, 2), (2, 3), (3, 1))}
    assert len(tri_edges) == 3
    assert all(sum(f in e for e in tri_edges) == 2 for f in (1, 2, 3))


# ---------------------------------------------------------------- week 162
# Faces: 0 up, 1 down, 2 front, 3 back, 4 left, 5 right.  A colouring is a tuple
# giving the colour on each face; a rotation is a permutation of face positions.
def compose(p, q):
    return tuple(p[q[i]] for i in range(6))


def rotation_group():
    # Quarter turn about the vertical axis: front -> right -> back -> left -> front.
    turn_v = (0, 1, 4, 5, 3, 2)      # new face i shows the old face turn_v[i]
    # Quarter turn about the front-back axis: up -> right -> down -> left -> up.
    turn_f = (4, 5, 2, 3, 1, 0)
    group = {tuple(range(6))}
    frontier = [tuple(range(6))]
    while frontier:
        g = frontier.pop()
        for h in (turn_v, turn_f):
            gh = compose(g, h)
            if gh not in group:
                group.add(gh)
                frontier.append(gh)
    return group


def orbits(colourings, group):
    seen, reps = set(), []
    for c in colourings:
        if c in seen:
            continue
        orb = {tuple(c[g[i]] for i in range(6)) for g in group}
        seen |= orb
        reps.append(c)
    return reps, seen


def canon(c, group):
    return min(tuple(c[g[i]] for i in range(6)) for g in group)


def check_week_162():
    G = rotation_group()
    assert len(G) == 24
    # The 24 rotations shuffle the 4 long diagonals in all 4! = 24 ways (a copy of S4).
    verts = [frozenset(v) for v in product((0, 1), (2, 3), (4, 5))]
    opp = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    diags = []
    for v in verts:
        d = frozenset([v, frozenset(opp[f] for f in v)])
        if d not in diags:
            diags.append(d)
    assert len(diags) == 4
    perms = set()
    for g in G:
        move = {g[i]: i for i in range(6)}          # old face -> new position
        img = []
        for d in diags:
            v = next(iter(d))
            nv = frozenset(move[f] for f in v)
            img.append(next(k for k, e in enumerate(diags) if nv in e))
        perms.add(tuple(img))
    assert len(perms) == 24
    # Six different colours: 720 paintings, 30 different cubes, each seen 24 ways.
    allc = list(permutations(range(6)))
    assert len(allc) == 720
    reps, _ = orbits(allc, G)
    assert len(reps) == 30
    # Fix colour 0 on top: 5 choices below, then 6 ways round the sides: 30.
    assert math.factorial(4) // 4 == 6 and 5 * 6 == 30
    # No six-colour cube is its own mirror image: 30 cubes = 15 mirror pairs.
    mirror = (0, 1, 2, 3, 5, 4)      # swap left and right
    canon_set = {canon(c, G) for c in reps}
    for c in reps:
        m = tuple(c[mirror[i]] for i in range(6))
        assert canon(m, G) != canon(c, G)
        assert canon(m, G) in canon_set
    assert len(canon_set) == 30
    # Two colours, any number of each: 64 paintings, 10 different cubes.
    two, _ = orbits(list(product(range(2), repeat=6)), G)
    assert len(two) == 10
    by_red = [sum(1 for c in two if sum(c) == r) for r in range(7)]
    assert by_red == [1, 1, 2, 2, 2, 1, 1]
    # Three colours, each on exactly two faces: 90 paintings, 6 different cubes.
    three = [c for c in product(range(3), repeat=6) if all(c.count(x) == 2 for x in range(3))]
    assert len(three) == 90
    reps3, _ = orbits(three, G)
    assert len(reps3) == 6
    # MacMahon's puzzle: for each target cube T, build a 2x2x2 copy from eight of
    # the other 29 cubes, outside matching T, touching inner faces equal colours.
    # Corner (x, y, z) in {0,1}^3; outer faces are those on the big cube's surface.
    corners = list(product(range(2), repeat=3))
    # face index for each axis direction: x: 4 left (0) / 5 right (1);
    # y: 3 back (0) / 2 front (1); z: 1 down (0) / 0 up (1)
    face = {("x", 0): 4, ("x", 1): 5, ("y", 0): 3, ("y", 1): 2, ("z", 0): 1, ("z", 1): 0}
    axes = ("x", "y", "z")
    set_counts = []
    for T in reps:
        tcanon = canon(T, G)
        options = []
        for pos in corners:
            outer = {face[(a, pos[i])] for i, a in enumerate(axes)}
            opts = [c for c in allc if all(c[f] == T[f] for f in outer)
                    and canon(c, G) != tcanon]
            options.append(opts)
        sols = []

        def ok(assign, idx):
            pos = corners[idx]
            c = assign[idx]
            for j in range(idx):
                q = corners[j]
                diff = [i for i in range(3) if pos[i] != q[i]]
                if len(diff) == 1:
                    i = diff[0]
                    a = axes[i]
                    # c's inner face towards q, and q's inner face towards c.
                    if c[face[(a, q[i])]] != assign[j][face[(a, pos[i])]]:
                        return False
            return True

        def search(assign):
            idx = len(assign)
            if idx == 8:
                cs = [canon(c, G) for c in assign]
                if len(set(cs)) == 8:
                    sols.append(frozenset(cs))
                return
            for c in options[idx]:
                assign.append(c)
                if ok(assign, idx):
                    search(assign)
                assign.pop()

        search([])
        assert len(sols) == 2            # two arrangements with T held still
        assert len(set(sols)) == 1       # always the same set of eight cubes
        set_counts.append(len(sols))
    assert set_counts == [2] * 30


# ---------------------------------------------------------------- week 163
def check_week_163():
    i = 1j
    assert i ** 2 == -1 and i ** 4 == 1
    # (-1) x (-1) = 1: two half turns make a whole turn.
    assert (-1) * (-1) == 1 and abs(cmath.exp(1j * math.pi) ** 2 - 1) < 1e-12
    # Quarter turn on the grid: (a, b) -> (-b, a).
    for a in range(-3, 4):
        for b in range(-3, 4):
            z = complex(a, b) * i
            assert (z.real, z.imag) == (-b, a)
    # Products quoted in the plan.
    assert (2 + 1j) * (2 - 1j) == 5
    assert (2 + 1j) ** 2 == 3 + 4j and abs(3 + 4j) == 5
    assert (1 + 1j) ** 2 == 2j and (1 + 1j) * (1 - 1j) == 2
    assert (3 + 2j) * (3 - 2j) == 13 and (4 + 1j) * (4 - 1j) == 17
    assert (1 + 2j) * (2 + 1j) == 5j
    assert (2 + 1j) * (3 + 1j) == 5 + 5j
    assert (1 + 1j) ** 4 == -4 and (1 + 1j) ** 8 == 16
    # Times (1 + i): (a, b) -> (a - b, a + b), a 45 degree turn with stretch sqrt 2.
    for a in range(-3, 4):
        for b in range(-3, 4):
            z = complex(a, b) * (1 + 1j)
            assert (z.real, z.imag) == (a - b, a + b)
    # Nose-to-tail rule: z x (a + bi) is a copies of z followed by b copies of z
    # turned a quarter left (negative counts point backwards), on the grid.
    def nose_to_tail(z, a, b):
        x, y = z
        return (a * x - b * y, a * y + b * x)
    for (x, y) in [(2, 1), (1, 3), (-2, 1), (3, -1)]:
        for a in range(-3, 4):
            for b in range(-3, 4):
                w = complex(x, y) * complex(a, b)
                assert nose_to_tail((x, y), a, b) == (w.real, w.imag)
    assert nose_to_tail((2, 1), 2, -1) == (5, 0)
    assert nose_to_tail((2, 1), 2, 1) == (3, 4)
    # Powers of 1 + i spiral out: 1, 1+i, 2i, -2+2i, -4, -4-4i, -8i, 8-8i, 16.
    pw = [(1 + 1j) ** k for k in range(9)]
    assert pw == [1, 1 + 1j, 2j, -2 + 2j, -4, -4 - 4j, -8j, 8 - 8j, 16]
    # Lengths multiply: squared lengths (a^2 + b^2) multiply exactly on the grid.
    pts = [complex(a, b) for a in range(-4, 5) for b in range(-4, 5)]
    for z in pts:
        for w in pts:
            n = lambda u: int(u.real) ** 2 + int(u.imag) ** 2
            assert n(z * w) == n(z) * n(w)
    # Angles add: checked with floating point on a few arrows.
    for z, w in [(2 + 1j, 1 + 3j), (1 + 1j, -2 + 1j), (3 - 1j, 2 + 2j)]:
        lhs = cmath.phase(z * w)
        rhs = cmath.phase(z) + cmath.phase(w)
        assert abs(cmath.exp(1j * lhs) - cmath.exp(1j * rhs)) < 1e-12
    # Squared lengths of grid arrows up to 25 are the two-square totals of week 158.
    sq = sorted({a * a + b * b for a in range(6) for b in range(6)} & set(range(1, 26)))
    assert sq == [1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25]
    # 3 has no grid arrow of squared length 3; 7 neither.
    assert 3 not in sq and 7 not in sq
    # The arrows of squared length 5: eight of them, (+-1, +-2) and (+-2, +-1).
    five = [(a, b) for a in range(-3, 4) for b in range(-3, 4) if a * a + b * b == 5]
    assert len(five) == 8
    # The four turns 1, i, -1, -i are the only grid arrows of length 1.
    one = [(a, b) for a in range(-2, 3) for b in range(-2, 3) if a * a + b * b == 1]
    assert len(one) == 4


def main():
    for name in ["157", "158", "159", "160", "161", "162", "163"]:
        globals()[f"check_week_{name}"]()
        print(f"week {name}: ok")


if __name__ == "__main__":
    main()
