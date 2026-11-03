#!/usr/bin/env python3
"""Checks for the logic-group draft plans, weeks 137-140.

Every small number quoted in week-137 to week-140 drafts is computed here.
Standard library only. Run: python3 check_logic.py
"""

import itertools
from collections import Counter
from fractions import Fraction
from math import factorial


# ---------------------------------------------------------------- week 137
def life_step(cells):
    counts = {}
    for (x, y) in cells:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    key = (x + dx, y + dy)
                    counts[key] = counts.get(key, 0) + 1
    return frozenset(c for c, n in counts.items()
                     if n == 3 or (n == 2 and c in cells))


def normalise(cells):
    if not cells:
        return frozenset()
    mx = min(x for x, _ in cells)
    my = min(y for _, y in cells)
    return frozenset((x - mx, y - my) for x, y in cells)


def life_fate(cells, max_gen=100):
    """Return ('dies', g) or ('settles', first_gen, period, size)."""
    seen = {}
    cur = frozenset(cells)
    for g in range(max_gen):
        if not cur:
            return ('dies', g)
        key = normalise(cur)
        if key in seen:
            return ('settles', seen[key], g - seen[key], len(cur))
        seen[key] = g
        cur = life_step(cur)
    return ('unknown',)


def rule90_ring(row):
    n = len(row)
    return tuple(row[(i - 1) % n] ^ row[(i + 1) % n] for i in range(n))


def check_week_137():
    # Still life, blinker, glider.
    block = {(0, 0), (1, 0), (0, 1), (1, 1)}
    assert life_step(block) == frozenset(block)
    beehive = {(1, 0), (2, 0), (0, 1), (3, 1), (1, 2), (2, 2)}
    assert life_step(beehive) == frozenset(beehive)
    blinker = {(0, 1), (1, 1), (2, 1)}
    b1 = life_step(blinker)
    assert b1 == frozenset({(1, 0), (1, 1), (1, 2)}) and life_step(b1) == frozenset(blinker)
    glider = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
    g = frozenset(glider)
    shapes = set()
    for _ in range(4):
        shapes.add(normalise(g))
        g = life_step(g)
    assert g == frozenset((x + 1, y + 1) for x, y in glider)  # one diagonal step in 4
    assert len(shapes) == 4 and all(len(s) == 5 for s in shapes)

    # Three counters in a 3-by-3 square: 84 placements; 62 die, 16 become a block, 6 blink.
    cells9 = [(x, y) for x in range(3) for y in range(3)]
    tally = Counter()
    for s in itertools.combinations(cells9, 3):
        f = life_fate(s)
        if f[0] == 'dies':
            tally['dies'] += 1
        elif f[2] == 1 and f[3] == 4:
            tally['block'] += 1
        elif f[2] == 2 and f[3] == 3:
            tally['blinker'] += 1
        else:
            tally['other'] += 1
    assert sum(tally.values()) == 84
    assert tally == Counter({'dies': 62, 'block': 16, 'blinker': 6})

    # The five tetrominoes.
    tets = {
        'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
        'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
        'T': [(0, 0), (1, 0), (2, 0), (1, 1)],
        'L': [(0, 0), (0, 1), (0, 2), (1, 0)],
        'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    }
    fates = {k: life_fate(v) for k, v in tets.items()}
    assert fates['O'] == ('settles', 0, 1, 4)        # block
    assert fates['I'] == ('settles', 2, 1, 6)        # beehive by generation 2
    assert fates['S'] == ('settles', 2, 1, 6)        # beehive by generation 2
    assert fates['L'] == ('settles', 3, 1, 6)        # beehive by generation 3
    assert fates['T'] == ('settles', 9, 2, 12)       # traffic light (4 blinkers) from generation 9

    # A single counter has a parent: three in a diagonal line.
    assert life_step({(0, 0), (1, 1), (2, 2)}) == frozenset({(1, 1)})

    # Rule 90 from one black cell: Pascal's triangle mod 2, row n has 2^(ones in n) black cells.
    width = 2 * 32 + 1
    row = [0] * width
    row[32] = 1
    for n in range(32):
        black = [i - 32 for i, v in enumerate(row) if v]
        assert len(black) == 2 ** bin(n).count('1')
        # cell at offset 2k - n is binomial(n, k) mod 2
        from math import comb
        expect = sorted(2 * k - n for k in range(n + 1) if comb(n, k) % 2)
        assert black == expect
        row = [(row[i - 1] if i > 0 else 0) ^ (row[i + 1] if i < width - 1 else 0)
               for i in range(width)]

    # Rule 90 on a ring: every child has an even number of black cells (each black cell
    # feeds two neighbours), so an odd ring pattern is an orphan.  On odd rings the
    # orphans are exactly the odd patterns; twins (a pattern and its opposite) always exist.
    for n in range(3, 12):
        patterns = list(itertools.product((0, 1), repeat=n))
        children = Counter(rule90_ring(p) for p in patterns)
        assert all(sum(c) % 2 == 0 for c in children)
        orphans = [p for p in patterns if p not in children]
        assert len(orphans) > 0
        for p in patterns:  # opposite twin
            q = tuple(1 - v for v in p)
            assert rule90_ring(p) == rule90_ring(q)
        if n % 2 == 1:
            assert set(orphans) == {p for p in patterns if sum(p) % 2 == 1}
            assert len(orphans) == 2 ** (n - 1)
    # Ring of 7: 128 patterns, 64 children, 64 orphans; every child has exactly 2 parents.
    pats7 = list(itertools.product((0, 1), repeat=7))
    ch7 = Counter(rule90_ring(p) for p in pats7)
    assert len(pats7) == 128 and len(ch7) == 64 and set(ch7.values()) == {2}
    # Ring of 6: 64 patterns, 16 children, so 48 orphans (more than the 32 odd ones).
    ch6 = Counter(rule90_ring(p) for p in itertools.product((0, 1), repeat=6))
    assert len(ch6) == 16 and 64 - len(ch6) == 48


# ---------------------------------------------------------------- week 138
def tm_run(table, cap):
    """table[state][symbol] is None (halt, writing 1) or (write, move, next).
    The halting transition counts as a step.  Returns (steps, ones) or None."""
    tape = {}
    pos = 0
    state = 0
    steps = 0
    while steps < cap:
        tr = table[state][tape.get(pos, 0)]
        steps += 1
        if tr is None:
            tape[pos] = 1
            return steps, sum(tape.values())
        w, d, ns = tr
        tape[pos] = w
        pos += d
        state = ns
    return None


def check_week_138():
    R, L = 1, -1
    A, B, C, D = 0, 1, 2, 3
    # Aaronson's BB(2) champion: A0 1RB, A1 1LB, B0 1LA, B1 halt.  6 steps, 4 ones.
    bb2 = [[(1, R, B), (1, L, B)], [(1, L, A), None]]
    assert tm_run(bb2, 100) == (6, 4)

    # All 2-state, 2-symbol cards: 9 choices per box, 9^4 = 6561 cards.
    trs2 = [None] + [(w, d, s) for w in (0, 1) for d in (L, R) for s in (A, B)]
    assert len(trs2) == 9
    hist = Counter()
    best_ones = 0
    total = 0
    for combo in itertools.product(trs2, repeat=4):
        total += 1
        t = [[combo[0], combo[1]], [combo[2], combo[3]]]
        r = tm_run(t, 50)
        if r:
            hist[r[0]] += 1
            best_ones = max(best_ones, r[1])
    assert total == 6561
    assert sum(hist.values()) == 1165          # cards that stop (BB(2) = 6, so the cap is safe)
    assert max(hist) == 6 and hist[6] == 10    # ten cards run the full six steps
    assert hist == Counter({1: 729, 2: 324, 3: 72, 4: 26, 5: 4, 6: 10})
    assert best_ones == 4

    # 1-state: 5 choices per box, 25 cards, 5 stop, each after 1 step.
    trs1 = [None] + [(w, d, A) for w in (0, 1) for d in (L, R)]
    stops1 = [tm_run([[a, b]], 20) for a in trs1 for b in trs1]
    assert len(stops1) == 25 and sum(1 for s in stops1 if s) == 5
    assert all(s == (1, 1) for s in stops1 if s)

    # 3-state: 13^6 cards.  Up to mirror image and renaming, the first move is
    # A0 -> (w, R, B).  Among those that stop within 30 steps the longest run is 21
    # with at most 6 ones, consistent with BB(3) = 21 and Sigma(3) = 6 (Lin and Rado).
    assert 13 ** 6 == 4826809
    trs3 = [None] + [(w, d, s) for w in (0, 1) for d in (L, R) for s in (A, B, C)]
    best_steps = best_ones3 = 0
    for a0 in [(0, R, B), (1, R, B)]:
        for combo in itertools.product(trs3, repeat=5):
            t = [[a0, combo[0]], [combo[1], combo[2]], [combo[3], combo[4]]]
            r = tm_run(t, 30)
            if r:
                best_steps = max(best_steps, r[0])
                best_ones3 = max(best_ones3, r[1])
    assert best_steps == 21 and best_ones3 == 6
    # A 21-step card: A0 1RB, A1 halt; B0 1LB, B1 0RC; C0 1LC, C1 1LA.
    bb3 = [[(1, R, B), None], [(1, L, B), (0, R, C)], [(1, L, C), (1, L, A)]]
    assert tm_run(bb3, 100) == (21, 5)

    # Brady's 4-state machine: 107 steps, 13 ones.
    bb4 = [[(1, R, B), (1, L, B)], [(1, L, A), (0, L, C)],
           [None, (1, L, D)], [(1, R, D), (0, R, A)]]
    assert tm_run(bb4, 1000) == (107, 13)

    # A card that never stops: A0 1RA marches right over blank tape forever.
    assert tm_run([[(1, R, A), None]], 10000) is None


# ---------------------------------------------------------------- week 139
SAMPLE = ("ONCE THERE WAS A GREEN FROG WHO LIVED NEAR THE EDGE OF A DEEP POND. "
          "EVERY EVENING THE FROG SAT ON A STONE AND SANG TO THE STARS. ONE NIGHT "
          "A HERON CAME TO THE POND AND THE FROG HID UNDER THE WATER UNTIL THE "
          "HERON FLEW AWAY TO THE TREES.")


def check_week_139():
    # Number of substitution keys (any shuffle of the alphabet): 26!.
    assert factorial(26) == 403291461126605635584000000
    assert 4 * 10 ** 26 < factorial(26) < 5 * 10 ** 26
    # Shift keys (Caesar): 26, of which 25 change the message.
    assert len({s % 26 for s in range(100)}) == 26

    # The sample message: E is the most common letter, T second.
    letters = [c for c in SAMPLE if c.isalpha()]
    freq = Counter(letters)
    assert len(letters) == 183
    top = freq.most_common(3)
    assert top == [('E', 33), ('T', 19), ('N', 18)]
    assert Fraction(1, 6) < Fraction(33, 183) < Fraction(1, 5)
    assert len(freq) == 20  # six letters never appear

    # Padlocks made of shifts leak: Eve sees M+a, M+a+b, M+b (mod 26).
    for M in range(26):
        for a in range(26):
            for b in range(26):
                s1, s2, s3 = (M + a) % 26, (M + a + b) % 26, (M + b) % 26
                assert (s1 + s3 - s2) % 26 == M
    # App example: the carrier sees 9, 14, 17 (M+a, M+a+b, M+b); the letter is 12.
    assert (9 + 17 - 14) % 26 == 12
    # Padlocks made of multiplying leak too (when the multipliers can be undone mod 26).
    for M in range(26):
        for a in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
            for b in (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):
                s1, s2, s3 = M * a % 26, M * a * b % 26, M * b % 26
                inv = pow(s2, -1, 26) if M % 2 and M % 13 else None
                if inv is not None:
                    assert s1 * s3 * inv % 26 == M

    # Powers of 2 on an 11-hour clock visit every hour 1..10: 2,4,8,5,10,9,7,3,6,1.
    powers = [pow(2, k, 11) for k in range(1, 11)]
    assert powers == [2, 4, 8, 5, 10, 9, 7, 3, 6, 1]
    assert sorted(powers) == list(range(1, 11))
    # Key exchange: Ana keeps 3, Ben keeps 7; Ana says 8, Ben says 7; both reach 2.
    a, b = 3, 7
    A_pub, B_pub = pow(2, a, 11), pow(2, b, 11)
    assert (A_pub, B_pub) == (8, 7)
    assert pow(B_pub, a, 11) == pow(A_pub, b, 11) == 2
    # Every choice of secrets gives a shared key for both sides.
    for a in range(1, 11):
        for b in range(1, 11):
            assert pow(pow(2, a, 11), b, 11) == pow(pow(2, b, 11), a, 11)

    # Three-pass with powers mod 11 (Shamir's no-key protocol): message 5,
    # Ana's lock 3 (undo 7), Ben's lock 7 (undo 3): 5 -> 4 -> 5 -> 3 -> 5.
    M = 5
    s1 = pow(M, 3, 11)
    s2 = pow(s1, 7, 11)
    s3 = pow(s2, 7, 11)
    s4 = pow(s3, 3, 11)
    assert (s1, s2, s3, s4) == (4, 5, 3, 5)
    for M in range(1, 11):
        for a, ai in ((3, 7), (7, 3), (9, 9), (1, 1)):
            for b, bi in ((3, 7), (7, 3), (9, 9), (1, 1)):
                assert pow(pow(pow(pow(M, a, 11), b, 11), ai, 11), bi, 11) == M


# ---------------------------------------------------------------- week 140
def wheel(rim):
    hub = 0
    edges = [(hub, i) for i in range(1, rim + 1)]
    edges += [(i, i % rim + 1) for i in range(1, rim + 1)]
    return rim + 1, edges


def min_bad_edges(nv, edges, k=3):
    best = None
    for col in itertools.product(range(k), repeat=nv):
        bad = sum(1 for u, v in edges if col[u] == col[v])
        best = bad if best is None else min(best, bad)
    return best


def rounds_below(p_survive, target):
    k = 0
    p = Fraction(1)
    while p >= target:
        p *= p_survive
        k += 1
    return k


def check_week_140():
    # Cave: a bluffer passes one round half the time; 10 rounds about 1 in 1000,
    # 20 rounds about 1 in a million.
    assert Fraction(1, 2) ** 10 == Fraction(1, 1024)
    assert 2 ** 20 == 1048576
    assert rounds_below(Fraction(1, 2), Fraction(1, 100)) == 7

    # Flower maps: a centre with r petals in a ring.
    for rim, three_ok, ne in ((4, True, 8), (5, False, 10), (6, True, 12)):
        nv, edges = wheel(rim)
        assert len(edges) == ne
        assert (min_bad_edges(nv, edges) == 0) == three_ok
    nv5, e5 = wheel(5)
    assert min_bad_edges(nv5, e5) == 1
    # Cheating on the five-petal flower: caught with chance at least 1/10 per round.
    assert rounds_below(Fraction(9, 10), Fraction(1, 100)) == 44
    assert rounds_below(Fraction(9, 10), Fraction(1, 2)) == 7
    # Four regions all touching (centre plus three around): needs 4 colours; 6 borders.
    k4 = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]
    assert min_bad_edges(4, k4) == 1
    assert rounds_below(Fraction(5, 6), Fraction(1, 100)) == 26
    assert rounds_below(Fraction(5, 6), Fraction(1, 2)) == 4

    # Shuffling colours hides the colouring: on the four-petal flower with a proper
    # colouring, every border shows each of the 6 ordered colour pairs exactly once
    # across the 6 colour shuffles.
    nv4, e4 = wheel(4)
    col = {0: 0, 1: 1, 2: 2, 3: 1, 4: 2}
    assert all(col[u] != col[v] for u, v in e4)
    perms = list(itertools.permutations(range(3)))
    assert len(perms) == 6
    for u, v in e4:
        seen = Counter((p[col[u]], p[col[v]]) for p in perms)
        assert len(seen) == 6 and set(seen.values()) == {1}
    # Proper 3-colourings of the four-petal flower: the centre takes one colour (3 ways)
    # and the petals alternate the other two (2 ways), so 6: exactly the 6 shuffles of one.
    count4 = sum(1 for c in itertools.product(range(3), repeat=5)
                 if all(c[u] != c[v] for u, v in e4))
    assert count4 == 6

    # Shamir 2-of-3 with clock arithmetic mod 11: height at 0 is the secret s,
    # share i is s + r*i mod 11.  One share fits every secret exactly once;
    # any two shares fix the line.
    p = 11
    for x in (1, 2, 3):
        for y in range(p):
            fits = Counter(s for s in range(p) for r in range(p) if (s + r * x) % p == y)
            assert set(fits) == set(range(p)) and set(fits.values()) == {1}
    for s in range(p):
        for r in range(p):
            shares = {x: (s + r * x) % p for x in (1, 2, 3)}
            for x1, x2 in itertools.combinations((1, 2, 3), 2):
                cands = [(s2, r2) for s2 in range(p) for r2 in range(p)
                         if (s2 + r2 * x1) % p == shares[x1] and (s2 + r2 * x2) % p == shares[x2]]
                assert cands == [(s, r)]
    # Ordinary numbers leak: with secret 0..9 and upward step 1..3, the share at 1
    # being 3 leaves only secrets 0, 1, 2.
    leaks = sorted({s for s in range(10) for r in (1, 2, 3) if s + r == 3})
    assert leaks == [0, 1, 2]
    # Example on paper: secret 4, step 3: shares (1,7), (2,10), (3,13); any two recover 4.
    sh = {1: 7, 2: 10, 3: 13}
    for x1, x2 in itertools.combinations(sh, 2):
        step = Fraction(sh[x2] - sh[x1], x2 - x1)
        assert sh[x1] - step * x1 == 4


def main():
    for name in ("check_week_137", "check_week_138", "check_week_139", "check_week_140"):
        globals()[name]()
        print(name.replace("check_", ""), "ok")


if __name__ == "__main__":
    main()
