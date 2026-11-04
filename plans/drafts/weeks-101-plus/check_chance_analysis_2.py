#!/usr/bin/env python3
"""Checks for the draft plans of weeks 171-175 (second chance and analysis group).

Standard library only. Each check_week_1NN() asserts the small numbers quoted
in plans/drafts/weeks-101-plus/week-1NN-*.md. Simulations use fixed seeds.
Run: python3 plans/drafts/weeks-101-plus/check_chance_analysis_2.py
"""

import math
import random
from decimal import Decimal, getcontext
from fractions import Fraction as F
from math import comb, factorial


# ---------------------------------------------------------------- week 171
def p_match(n, d):
    """Chance that some two of n people share a 'birthday' among d equally
    likely days."""
    distinct = F(1)
    for i in range(n):
        distinct *= F(d - i, d)
    return 1 - distinct


def p_no_triple(n, d):
    """Chance that no day is shared by three or more of n people (d days)."""
    total = 0
    for j in range(n // 2 + 1):          # j days used twice, n - 2j once
        singles = n - 2 * j
        if j + singles > d:
            continue
        ways_days = factorial(d) // (factorial(j) * factorial(singles)
                                     * factorial(d - j - singles))
        total += ways_days * factorial(n) // (2 ** j)
    return F(total, d ** n)


def p_no_near(n, d=365):
    """Circular calendar of d days: chance that no two of n people have
    birthdays on the same or adjacent days (k = 1):
    (d - n - 1)! / (d^(n-1) (d - 2n)!)."""
    return F(factorial(d - n - 1), d ** (n - 1) * factorial(d - 2 * n))


def check_week_171():
    # The classic numbers.
    assert abs(float(p_match(23, 365)) - 0.5073) < 1e-4
    assert abs(float(p_match(22, 365)) - 0.4757) < 1e-4
    assert p_match(22, 365) < F(1, 2) < p_match(23, 365)
    assert abs(float(p_match(11, 365)) - 0.1411) < 1e-4      # a class of 11
    assert abs(float(p_match(30, 365)) - 0.7063) < 1e-4
    assert abs(float(p_match(57, 365)) - 0.9901) < 1e-4
    # Pairs: 23 people make 253 pairs; the pair heuristic 1 - exp(-253/365).
    assert comb(23, 2) == 253
    assert abs((1 - math.exp(-253 / 365)) - 0.5000) < 1e-3
    # sqrt(2 d ln 2) for d = 365 is about 22.5.
    assert abs(math.sqrt(2 * 365 * math.log(2)) - 22.49) < 0.01
    # Someone shares YOUR birthday: 22 others give about 6%; 253 others
    # are needed for an even chance.
    assert abs(1 - (364 / 365) ** 22 - 0.0586) < 1e-4
    n = 1
    while 1 - (364 / 365) ** n < 0.5:
        n += 1
    assert n == 253
    # Small calendars for children.
    months = {k: p_match(k, 12) for k in range(2, 14)}
    assert abs(float(months[4]) - 0.4271) < 1e-4
    assert abs(float(months[5]) - 0.6181) < 1e-4          # over 60% with 5
    assert months[5] == 1 - F(95040, 248832)
    assert months[13] == 1                                 # pigeonhole
    assert months[12] == 1 - F(factorial(12), 12 ** 12)
    die = {k: p_match(k, 6) for k in range(2, 8)}
    assert die[2] == F(1, 6) and die[3] == F(4, 9)         # 44% with 3
    assert die[4] == F(13, 18)                             # 72% with 4
    assert die[7] == 1
    # Real month lengths (Feb 28.25 of 365.25 days) make a match a little
    # more likely than twelve equal months, for 5 people.
    lengths = [31, F(113, 4), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ps = [F(x) / sum(lengths) for x in lengths]
    e = [F(0)] * 6
    e[0] = F(1)
    for p in ps:                       # elementary symmetric polynomials
        for k in range(5, 0, -1):
            e[k] += e[k - 1] * p
    p_unequal = 1 - factorial(5) * e[5]
    assert months[5] < p_unequal < months[5] + F(1, 100)
    # Three sharing: 88 people (McKinney 1966, cited by Diaconis-Mosteller).
    assert 1 - p_no_triple(87, 365) < F(1, 2) < 1 - p_no_triple(88, 365)
    # Same or adjacent day: 14 people (Abramson-Moser, cited there).
    assert 1 - p_no_near(13) < F(1, 2) < 1 - p_no_near(14)
    # Rolls until the first repeat (the roll that repeats included):
    # sum over k of P(first k rolls all different); about 3.77 for a d6,
    # 5.04 for a d12 and 24.6 for 365 days, near sqrt(pi d / 2).
    def first_repeat(d):
        return sum(F(factorial(d), factorial(d - k) * d ** k)
                   for k in range(d + 1))
    assert abs(float(first_repeat(6)) - 3.775) < 0.001
    assert abs(float(first_repeat(12)) - 5.036) < 0.001
    assert abs(float(first_repeat(365)) - 24.617) < 0.001
    assert abs(math.sqrt(math.pi * 365 / 2) - 23.94) < 0.01
    # Contrast with draft 131: seeing all twelve faces takes 12 H_12 rolls.
    assert abs(float(12 * sum(F(1, k) for k in range(1, 13))) - 37.24) < 0.01
    # A class running 30 groups of 5 on a 12-box calendar sees matches in
    # a majority of groups with chance about 87%.
    p5 = float(months[5])
    maj = sum(comb(30, k) * p5 ** k * (1 - p5) ** (30 - k)
              for k in range(16, 31))
    assert abs(maj - 0.873) < 0.001
    # Seeded simulation of 5 children each rolling a 12-sided die.
    rng = random.Random(171)
    trials = 20000
    hits = sum(len(set(rng.randrange(12) for _ in range(5))) < 5
               for _ in range(trials))
    assert abs(hits / trials - 0.618) < 0.015


# ---------------------------------------------------------------- week 172
def first_digit(x):
    return int(str(x)[0])


def check_week_172():
    benford = [math.log10(1 + 1 / d) for d in range(1, 10)]
    assert abs(sum(benford) - 1) < 1e-12
    assert abs(benford[0] - 0.30103) < 1e-5
    assert abs(benford[1] - 0.17609) < 1e-5
    assert abs(benford[8] - 0.04576) < 1e-5
    # The first ten powers of 2.
    firsts = [first_digit(2 ** n) for n in range(10)]
    assert firsts == [1, 2, 4, 8, 1, 3, 6, 1, 2, 5]
    # Exactly one power of 2 with each number of digits starts with 1, and
    # each digit length holds 3 or 4 powers of 2.
    by_len = {}
    for n in range(0, 1200):
        s = str(2 ** n)
        by_len.setdefault(len(s), []).append(s[0])
    for k, digs in by_len.items():
        if k < len(str(2 ** 1199)):
            assert digs.count('1') == 1 and len(digs) in (3, 4)
    # Among 2^1, ..., 2^N the count starting with 1 is floor(N log10 2).
    count = 0
    for N in range(1, 3001):
        count += first_digit(2 ** N) == 1
        assert count == math.floor(N * math.log10(2))
    getcontext().prec = 40
    log2 = Decimal(2).log10()
    assert int(Decimal(10 ** 9) * log2) == 301029995       # Cai et al.
    # First 100 powers 2^0..2^99: 30 start with 1; Benford predicts 30.1.
    first100 = [first_digit(2 ** n) for n in range(100)]
    assert first100.count(1) == 30
    assert [first100.count(d) for d in range(1, 10)] == [30, 17, 13, 10, 7, 7, 6, 5, 5]
    assert first100.count(2) == 17
    # Powers of 3 and Fibonacci numbers behave the same way.
    p3 = [first_digit(3 ** n) for n in range(100)]
    assert p3.count(1) == 29
    fib = [1, 1]
    while len(fib) < 100:
        fib.append(fib[-1] + fib[-2])
    assert [first_digit(f) for f in fib].count(1) == 30
    # The whole numbers 1..N do not settle: the share starting with 1
    # swings between about 1/9 and 5/9.
    def share1(N):
        return F(sum(1 for k in range(1, N + 1) if str(k)[0] == '1'), N)
    assert share1(19) == F(11, 19)
    assert share1(99) == F(11, 99)
    assert share1(199) == F(111, 199)
    assert share1(999) == F(111, 999)
    assert abs(float(share1(1999)) - 0.5558) < 1e-4
    # Doubling 1..9: five of the nine answers start with 1 (scale change
    # breaks equal first digits).
    doubled = [first_digit(2 * k) for k in range(1, 10)]
    assert doubled.count(1) == 5
    # Doubling moves first digits along a small map: 1 -> 2 or 3,
    # 2 -> 4 or 5, 3 -> 6 or 7, 4 -> 8 or 9, and 5, 6, 7, 8, 9 -> 1.
    moves = {}
    for x in range(10, 100):
        moves.setdefault(x // 10, set()).add(first_digit(2 * x))
    assert moves == {1: {2, 3}, 2: {4, 5}, 3: {6, 7}, 4: {8, 9},
                     5: {1}, 6: {1}, 7: {1}, 8: {1}, 9: {1}}
    # A doubling chain from 7, as children would compute it.
    chain = [7 * 2 ** k for k in range(10)]
    assert chain == [7, 14, 28, 56, 112, 224, 448, 896, 1792, 3584]
    assert [first_digit(x) for x in chain].count(1) == 3


# ---------------------------------------------------------------- week 173
CLASSIC = {1: 38, 4: 14, 9: 31, 16: 6, 21: 42, 28: 84, 36: 44, 47: 26,
           49: 11, 51: 67, 56: 53, 62: 19, 64: 60, 71: 91, 80: 100, 87: 24,
           93: 73, 95: 75, 98: 78}


def expected_float(jumps, N=100, faces=6, rule='stay'):
    """Expected rolls from square 0 (value iteration). rule 'stay': a roll
    past N leaves the counter where it is; 'pass': reaching or passing N
    finishes."""
    E = [0.0] * (N + 1)
    for _ in range(100000):
        new = [0.0] * (N + 1)
        for s in range(N):
            tot = 0.0
            for r in range(1, faces + 1):
                t = s + r
                if t > N:
                    t = s if rule == 'stay' else N
                tot += E[jumps.get(t, t)]
            new[s] = 1 + tot / faces
        diff = max(abs(a - b) for a, b in zip(new, E))
        E = new
        if diff < 1e-12:
            break
    return E[0]


def expected_exact(jumps, N, faces):
    """Exact expected rolls from 0 under the 'pass' rule, by working back
    from the finish. Valid when every jump goes forward of its square or
    the system is solved by elimination (done here)."""
    n = N
    A = [[F(0)] * (n + 1) for _ in range(n)]
    for s in range(n):
        A[s][s] += 1
        A[s][n] = F(1)
        for r in faces:
            t = s + r
            if t >= N:
                continue
            t = jumps.get(t, t)
            if t >= N:
                continue
            A[s][t] -= F(1, len(faces))
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [A[s][n] for s in range(n)]


def length_distribution(jumps, N, rolls):
    """Exact chance that a 'pass'-rule game on squares 0..N with a d6 ends
    on each roll 1..rolls."""
    p = {0: F(1)}
    out = []
    for _ in range(rolls):
        q, fin = {}, F(0)
        for s, pr in p.items():
            for f in range(1, 7):
                t = s + f
                if t >= N:
                    fin += pr / 6
                    continue
                t = jumps.get(t, t)
                q[t] = q.get(t, 0) + pr / 6
        out.append(fin)
        p = q
    return out


def check_week_173():
    # Classic 1952 Milton Bradley board, overshoot = stay put: 39.225122.
    e = expected_float(CLASSIC)
    assert abs(e - 39.225122) < 1e-6
    # Without the 80->100 ladder the game averages about 59 rolls.
    j = dict(CLASSIC); del j[80]
    assert abs(expected_float(j) - 58.99) < 0.01
    # Removing the snake 56->53 makes the game LONGER (39.239): that snake
    # shortens the game, because from 53 the snake at 62 is out of reach.
    j = dict(CLASSIC); del j[56]
    assert expected_float(j) > e and abs(expected_float(j) - 39.239) < 0.001
    # Adding a ladder 74->81 makes the game LONGER (about 41.46): it carries
    # you past the 80->100 ladder.
    j = dict(CLASSIC); j[74] = 81
    assert abs(expected_float(j) - 41.458) < 0.001
    # Removing any one of the nine ladders lengthens the classic game.
    for a, b in CLASSIC.items():
        if b > a:
            j = dict(CLASSIC); del j[a]
            assert expected_float(j) > e
    # Children's 20-square board: ladders 3->11, 8->15, snakes 13->5, 18->2;
    # reaching or passing 20 finishes.
    kids = {3: 11, 8: 15, 13: 5, 18: 2}
    E = expected_exact(kids, 20, range(1, 7))
    assert abs(float(E[0]) - 7.009) < 0.001
    assert abs(float(expected_exact({}, 20, range(1, 7))[0]) - 6.190) < 0.001
    assert abs(float(expected_exact({3: 11, 8: 15}, 20, range(1, 7))[0])
               - 5.264) < 0.001
    dist = length_distribution(kids, 20, 60)
    assert dist[0] == 0 and dist[1] == 0 and dist[2] == F(1, 12)
    cum, median = F(0), None
    for i, x in enumerate(dist):
        cum += x
        if median is None and cum >= F(1, 2):
            median = i + 1
    assert median == 6
    assert abs(float(1 - sum(dist[:15])) - 0.0368) < 1e-4
    # Coin strip, squares 0..8, tails 1 step, heads 2 steps, reaching or
    # passing 8 finishes. Working back: 1, 3/2, 9/4, 23/8, 57/16, ...
    plain = expected_exact({}, 8, (1, 2))
    assert plain[7] == 1 and plain[6] == F(3, 2) and plain[5] == F(9, 4)
    assert plain[4] == F(23, 8) and plain[3] == F(57, 16)
    # Big ladder 2->8: from 0 the game averages 153/64 tosses.
    big = expected_exact({2: 8}, 8, (1, 2))
    assert big[0] == F(153, 64) and big[1] == F(89, 32)
    # Adding a small ladder 1->3 makes it longer: 89/32 tosses.
    both = expected_exact({2: 8, 1: 3}, 8, (1, 2))
    assert both[0] == F(89, 32) and both[0] > big[0]
    # Seeded simulation of the children's board.
    rng = random.Random(173)
    total, games = 0, 4000
    for _ in range(games):
        s, rolls = 0, 0
        while s < 20:
            s += rng.randint(1, 6)
            rolls += 1
            s = kids.get(s, s)
        total += rolls
    assert abs(total / games - 7.01) < 0.25


# ---------------------------------------------------------------- week 174
def rounds_to_empty(n_max):
    """E[n] = expected rounds until a pile of n fair coins is empty, when
    each round every coin is flipped and heads are removed."""
    E = [F(0)]
    for n in range(1, n_max + 1):
        s = sum(F(comb(n, k), 2 ** n) * E[k] for k in range(n))
        E.append((1 + s) / (1 - F(1, 2 ** n)))
    return E


def check_week_174():
    E = rounds_to_empty(128)
    assert E[1] == 2 and E[2] == F(8, 3) and E[3] == F(22, 7)
    assert E[4] == F(368, 105)
    # The sum formula E[n] = sum_{j>=0} (1 - (1 - 2^-j)^n).
    for n in (1, 2, 5, 10, 32):
        s = sum(1 - (1 - 2.0 ** -j) ** n for j in range(200))
        assert abs(s - float(E[n])) < 1e-9
    assert abs(float(E[10]) - 4.73) < 0.01
    assert abs(float(E[32]) - 6.36) < 0.01
    assert abs(float(E[100]) - 7.98) < 0.01
    # Asymptotics log2 n + 1/2 + gamma/ln 2 (Szpankowski-Rego, via Finch).
    gamma = 0.5772156649015329
    c = 0.5 + gamma / math.log(2)
    assert abs(c - 1.3327461772) < 1e-9
    # The gap shrinks slowly: 0.07 at n = 10, 0.02 at 32, under 0.01 at 100.
    gaps = {n: float(E[n]) - (math.log2(n) + c) for n in (10, 32, 100, 128)}
    assert 0.06 < gaps[10] < 0.08 and 0.015 < gaps[32] < 0.025
    assert 0 < gaps[100] < 0.01 and 0 < gaps[128] < 0.01
    # Doubling the pile adds about one round.
    assert abs(float(E[64] - E[32]) - 0.989) < 0.001
    assert abs(float(E[128] - E[64]) - 0.994) < 0.001
    # The spread stays about the same as the pile grows: variance about
    # 3.3 at 10 coins, 3.44 at 32, 3.49 at 100, 3.51 at 10,000.
    def var(n, q=0.5):
        m = sum(1 - (1 - q ** j) ** n for j in range(400))
        s2 = sum((2 * j + 1) * (1 - (1 - q ** j) ** n) for j in range(400))
        return s2 - m * m
    assert abs(var(10) - 3.31) < 0.01 and abs(var(32) - 3.44) < 0.01
    assert abs(var(100) - 3.49) < 0.01 and abs(var(10000) - 3.51) < 0.01
    # App puzzle: 64 beads at chance 1/2 (about 7.34 ticks) go dark sooner
    # than 32 beads at chance 1/3 per tick (about 10.51 ticks).
    slow = sum(1 - (1 - (2 / 3) ** j) ** 32 for j in range(600))
    assert abs(float(E[64]) - 7.344) < 0.001 and abs(slow - 10.51) < 0.01
    # Expected pile sizes: 32 -> 16 -> 8 -> 4 -> 2 -> 1.
    assert [32 / 2 ** r for r in range(6)] == [32, 16, 8, 4, 2, 1]
    # Chance a pile of 20 is empty after 5 rounds: (31/32)^20, about 53%.
    assert abs((31 / 32) ** 20 - 0.530) < 0.001
    # Dice version (remove sixes): half-life ln 2 / ln(6/5), about 3.8 rolls.
    assert abs(math.log(2) / math.log(6 / 5) - 3.80) < 0.01
    # Radiocarbon with half-life 5730 years: a quarter after 11460 years;
    # about 1/423 (0.24%) after 50,000 years.
    assert abs(2 ** (-11460 / 5730) - 0.25) < 1e-12
    left = 2 ** (-50000 / 5730)
    assert abs(left - 0.0024) < 0.0001 and 420 < 1 / left < 425
    # Seeded simulation: 32 coins.
    rng = random.Random(174)
    total, runs = 0, 5000
    for _ in range(runs):
        n, r = 32, 0
        while n:
            n = sum(rng.random() < 0.5 for _ in range(n))
            r += 1
        total += r
    assert abs(total / runs - float(E[32])) < 0.1


# ---------------------------------------------------------------- week 175
def check_week_175():
    # Triangle with corners (0,0), (1,0), (0,1); jump halfway to a corner.
    # Starting at the corner (0,0), after k jumps every point is (a,b)/2^k,
    # and the reachable points are exactly those with a AND b = 0 (no
    # common binary 1), i.e. C(a+b, a) odd: the odd entries of Pascal's
    # triangle (Lucas/Kummer).
    corners = [(0, 0), (1, 0), (0, 1)]
    for k in range(1, 9):
        size = 2 ** k
        pts = {(0, 0)}
        for _ in range(k):
            pts = {((x + cx * size) // 2, (y + cy * size) // 2)
                   for x, y in pts for cx, cy in corners}
        # (integer arithmetic on the 2^k grid; all halvings are exact
        # because each coordinate is built up from the corner.)
        expected = {(a, b) for a in range(size) for b in range(size)
                    if a & b == 0}
        assert pts == expected and len(pts) == 3 ** k
        assert all(comb(a + b, a) % 2 == 1 for a, b in pts)
    # Halving: any start ends within 1/2^k of the triangle's size after k
    # jumps; 8 jumps on a 25 cm triangle leave under 1 mm.
    assert 250 / 2 ** 8 < 1
    # Level-k counts: Sierpinski keeps 3^k of 4^k small triangles.
    assert [3 ** k for k in range(1, 5)] == [3, 9, 27, 81]
    assert abs(math.log(3) / math.log(2) - 1.585) < 0.001
    # Square, jump halfway: every one of the 4^k cells is reached (it fills
    # in). Square with "never the same corner twice in a row": 4*3^(k-1)
    # cells, so it thins out like Sierpinski.
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    for k in range(1, 7):
        cells_all, cells_rule = set(), set()

        def walk(seq):
            # point after the jumps seq[0], seq[1], ... (last jump outermost)
            # lies in the cell addressed by the reversed sequence.
            x = y = 0
            for i, v in enumerate(reversed(seq)):
                x += sq[v][0] * 2 ** (k - 1 - i)
                y += sq[v][1] * 2 ** (k - 1 - i)
            return (x, y)

        def gen(seq):
            if len(seq) == k:
                cells_all.add(walk(seq))
                if all(seq[i] != seq[i + 1] for i in range(k - 1)):
                    cells_rule.add(walk(seq))
                return
            for v in range(4):
                gen(seq + [v])
        gen([])
        assert len(cells_all) == 4 ** k
        assert len(cells_rule) == 4 * 3 ** (k - 1)
    # Changing the jump: moving to scale s toward a corner leaves a middle
    # hole exactly when every barycentric coordinate can be below 1 - s;
    # since some coordinate is always >= 1/3, s >= 2/3 (jump a third of the
    # way) fills the whole triangle, while s = 1/2 leaves the centroid out.
    def covered(bary, s):
        return max(bary) >= 1 - s
    centroid = (F(1, 3), F(1, 3), F(1, 3))
    assert not covered(centroid, F(1, 2)) and covered(centroid, F(2, 3))
    grid = [(F(i, 30), F(j, 30), F(30 - i - j, 30))
            for i in range(31) for j in range(31 - i)]
    assert all(covered(b, F(2, 3)) for b in grid)
    # Pooling dots: with 27 equally likely level-3 triangles, a dot in each
    # needs about 27 * H_27, roughly 105 dots on average.
    h27 = sum(F(1, k) for k in range(1, 28))
    assert abs(float(27 * h27) - 105.07) < 0.01
    # Seeded chaos game: after 8 warm-up jumps from a random start, 3000
    # dots all avoid the open middle triangle (all coordinates < 1/2).
    rng = random.Random(175)
    x, y = rng.random() * 0.3 + 0.2, rng.random() * 0.3 + 0.1
    for i in range(3008):
        cx, cy = corners[rng.randrange(3)]
        x, y = (x + cx) / 2, (y + cy) / 2
        if i >= 8:
            z = 1 - x - y
            assert max(x, y, z) >= 0.5 - 1e-3


def main():
    for name in ('171', '172', '173', '174', '175'):
        globals()['check_week_' + name]()
        print(f'week {name}: ok')


if __name__ == '__main__':
    main()
