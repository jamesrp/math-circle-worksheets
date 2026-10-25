"""Exact checks for the Week 58 return-visit pages (fractions only)."""
from fractions import Fraction as F
from itertools import combinations, permutations, product


# ---------------------------------------------------------------- trains
def min_cuts(train):
    """Fewest gaps to cut so the pieces can go into two trays with equal
    counts of every colour.  None if impossible."""
    n = len(train)
    cols = set(train)
    need = {c: train.count(c) for c in cols}
    if any(v % 2 for v in need.values()):
        return None
    for k in range(0, n):
        for gaps in combinations(range(1, n), k):
            bounds = [0, *gaps, n]
            pieces = [train[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]
            for assign in product((0, 1), repeat=len(pieces)):
                tray = {c: 0 for c in cols}
                for p, a in zip(pieces, assign):
                    if a == 0:
                        for c in p:
                            tray[c] += 1
                if all(2 * tray[c] == need[c] for c in cols):
                    return k
    return None


def distinct_orders(r, b):
    out = set()
    for pos in combinations(range(r + b), r):
        out.add(''.join('R' if i in pos else 'B' for i in range(r + b)))
    return sorted(out)


def tally(r, b):
    t = {}
    for s in distinct_orders(r, b):
        k = min_cuts(s)
        t[k] = t.get(k, 0) + 1
    return t


print('2R2B', {s: min_cuts(s) for s in distinct_orders(2, 2)})
print('4R4B', tally(4, 4))
print('6R4B', tally(6, 4))
print('4R2B', tally(4, 2), '2R4B', tally(2, 4), '6R2B', tally(6, 2))
# criterion for 4R4B: one cut iff first four hold two reds
assert all((min_cuts(s) == 1) == (s[:4].count('R') == 2) for s in distinct_orders(4, 4))

worst = 0
for n in range(2, 15, 2):
    for r in range(0, n + 1, 2):
        for s in distinct_orders(r, n - r):
            # fast: one cut iff prefix of length n/2 holds r/2 reds; else 2
            h = n // 2
            if r == 0 or r == n:
                k = 1
            elif any(s[i:i + h].count('R') == r // 2 for i in [0]):
                k = 1
            else:
                k = 2  # sliding window guarantees a middle window
                assert any(s[i:i + h].count('R') == r // 2 for i in range(0, n - h + 1))
            worst = max(worst, k)
print('max cuts up to 14 cards (two colours, even counts):', worst)
# brute check of the fast rule on all trains up to 10 cards
for n in range(2, 11, 2):
    for r in range(0, n + 1, 2):
        for s in distinct_orders(r, n - r):
            h = n // 2
            fast = 1 if s[:h].count('R') == r // 2 else 2
            assert min_cuts(s) == fast, s
print('fast rule agrees with brute force up to 10 cards')
print('RRBBGG needs', min_cuts('RRBBGG'))

# ---------------------------------------------------------------- strip
# red 0-120, blue 120-240 ; A: red panel 3, blue panel 1 ; B: red 1, blue 3
def strip_val(card, a, b):
    red = max(F(0), min(F(b), F(120)) - max(F(a), F(0)))
    blue = max(F(0), min(F(b), F(240)) - max(F(a), F(120)))
    return card[0] * red / 120 + card[1] * blue / 120


A2, B2 = (F(3), F(1)), (F(1), F(3))
one = [x for x in range(0, 241) if strip_val(A2, 0, x) == 2 and strip_val(B2, 0, x) == 2]
print('one-cut exact for both (mm grid):', one)
print('A exact one-cut:', [x for x in range(241) if strip_val(A2, 0, x) == 2],
      'B:', [x for x in range(241) if strip_val(B2, 0, x) == 2])
two = [(x, y) for x in range(0, 241) for y in range(x + 1, 241)
       if strip_val(A2, x, y) == 2 and strip_val(B2, x, y) == 2 and 0 < x and y < 240]
print('two-cut middle pieces (1 mm grid):', two)
# half-millimetre grid too
two_h = [(x, y) for x in [F(i, 2) for i in range(1, 480)] for y in [F(j, 2) for j in range(1, 480)]
         if x < y and strip_val(A2, x, y) == 2 and strip_val(B2, x, y) == 2]
print('two-cut middle pieces (0.5 mm grid):', two_h)
print('B value of A half-window at start', strip_val(B2, 0, 80), 'end', strip_val(B2, 80, 240))


# ---------------------------------------------------------------- X Y Z
cards3 = {'A': {'X': F(4), 'Y': F(8), 'Z': F(0)},
          'B': {'X': F(0), 'Y': F(4), 'Z': F(8)},
          'C': {'X': F(8), 'Y': F(0), 'Z': F(4)}}


def row_val(order, card, a, b):
    v = F(0)
    for i, p in enumerate(order):
        lo, hi = 50 * i, 50 * (i + 1)
        L = max(F(0), min(F(b), F(hi)) - max(F(a), F(lo)))
        v += cards3[card][p] * L / 50
    return v


def tray_vals(order, cuts, card):
    bounds = [F(0), *map(F, cuts), F(150)]
    t0 = F(0)
    for i in range(len(bounds) - 1):
        if i % 2 == 0:
            t0 += row_val(order, card, bounds[i], bounds[i + 1])
    return t0


for order in ['XYZ']:
    grid = [F(i, 2) for i in range(1, 300)]
    for k in (1, 2, 3):
        sols = []
        for cuts in combinations(grid, k):
            if all(tray_vals(order, cuts, c) == 6 for c in 'ABC'):
                sols.append(tuple(float(c) for c in cuts))
        print(order, k, 'cuts, three tastes, 0.5mm grid:', sols[:10], len(sols))
# all orders, 2 cuts never, check 3 cuts at half points
for order in map(''.join, permutations('XYZ')):
    print(order, 'cuts 25,75,125 ->', [tray_vals(order, (25, 75, 125), c) for c in 'ABC'])

# two tastes (three-person cards A and B, C, etc) on XYZ: two cuts
for order in map(''.join, permutations('XYZ')):
    for pair in [('A', 'B'), ('B', 'C'), ('A', 'C')]:
        grid = [F(i, 2) for i in range(1, 300)]
        one = [float(x) for x in grid if all(tray_vals(order, (x,), c) == 6 for c in pair)]
        twos = [(float(x), float(y)) for x, y in combinations(grid, 2)
                if all(tray_vals(order, (x, y), c) == 6 for c in pair)]
        if order == 'XYZ':
            print('two tastes', pair, order, 'one cut:', one, 'two cuts:', twos)


# ---------------------------------------------------------------- marking game
def mark(order, card, start, target):
    """Leftmost point m >= start with value(start, m) = target (exact)."""
    v = F(0)
    pos = F(start)
    for i, p in enumerate(order):
        lo, hi = F(50 * i), F(50 * (i + 1))
        if hi <= pos:
            continue
        a = max(lo, pos)
        rate = cards3[card][p] / 50
        seg = rate * (hi - a)
        if v + seg >= target and rate > 0:
            return a + (target - v) / rate
        v += seg
    return None


def last_diminisher(order, people='ABC', target=F(4)):
    start = F(0)
    left = list(people)
    got = {}
    log = []
    while len(left) > 1:
        ms = {p: mark(order, p, start, target) for p in left}
        m = min(ms.values())
        takers = [p for p in left if ms[p] == m]
        assert len(takers) == 1, (order, ms)
        t = takers[0]
        log.append((dict((p, float(x)) for p, x in ms.items()), t, float(start), float(m)))
        got[t] = (start, m)
        left.remove(t)
        start = m
    got[left[0]] = (start, F(150))
    return got, log


for order in map(''.join, permutations('XYZ')):
    got, log = last_diminisher(order)
    vals = {p: {q: row_val(order, p, *got[q]) for q in 'ABC'} for p in 'ABC'}
    envy = [(p, q) for p in 'ABC' for q in 'ABC' if vals[p][q] > vals[p][p]]
    print(order, [(l[0], l[1], l[2], l[3]) for l in log])
    print('   pieces', {p: (float(a), float(b)) for p, (a, b) in got.items()},
          'own values', {p: vals[p][p] for p in 'ABC'}, 'envy', envy,
          'full table', {p: [str(vals[p][q]) for q in 'ABC'] for p in 'ABC'})

# whole panels A:Y, B:Z, C:X
print('whole panels', cards3['A']['Y'], cards3['B']['Z'], cards3['C']['X'])


# ---------------------------------------------------------------- split cards
# Both people use the two-person card A on R1 B1 R3 B2 R2 (each card a 25 mm square)
def card_row_half(row, vals):
    tot = sum(vals[c[0]] for c in row)
    half = F(tot, 2)
    v = F(0)
    for i, c in enumerate(row):
        if v + vals[c[0]] >= half:
            return i, c, (half - v) / vals[c[0]], tot
        v += vals[c[0]]


Avals = {'R': F(3), 'B': F(1)}
print('R1 B1 R3 B2 R2 half point (card index, card, fraction into card, total):',
      card_row_half(['R1', 'B1', 'R3', 'B2', 'R2'], Avals))
inside_red = True
for s in distinct_orders(3, 2):
    i, c, frac, tot = card_row_half(list(s), Avals)
    if not (c == 'R' and 0 < frac < 1):
        inside_red = False
        print('  not strictly inside a red:', s, i, c, frac)
print('every order of 3R 2B: half falls strictly inside a red card:', inside_red)

# Two reds, three people valuing every red at 1: marks with target 2/3
row = ['R', 'R']
uv = {'R': F(1), 'B': F(0)}
# all three identical, first mark at 2/3 of first red; second at 4/3 total -> 1/3 into second red
print('two reds three people: first mark', F(2, 3), 'into red 1; second mark at', F(4, 3) - 1, 'into red 2')

# Steinhaus check with random tastes (rational) for n=3,4 on 3-5 panels
import random
random.seed(1)
bad = 0
envyc = 0
trials = 0
for trial in range(2000):
    n = random.choice([3, 4])
    m = random.choice([3, 4, 5])
    tastes = [[F(random.randint(0, 9)) for _ in range(m)] for _ in range(n)]
    if any(sum(t) == 0 for t in tastes):
        continue
    trials += 1

    def val(t, a, b):
        v = F(0)
        for i in range(m):
            L = max(F(0), min(b, F(i + 1)) - max(a, F(i)))
            v += t[i] * L
        return v

    def mk(t, start, target):
        v = F(0)
        for i in range(m):
            lo, hi = F(i), F(i + 1)
            if hi <= start:
                continue
            a = max(lo, start)
            seg = t[i] * (hi - a)
            if t[i] > 0 and v + seg >= target:
                return a + (target - v) / t[i]
            v += seg
        return F(m)

    left = list(range(n))
    start = F(0)
    got = {}
    while len(left) > 1:
        ms = {p: mk(tastes[p], start, sum(tastes[p]) / n) for p in left}
        mn = min(ms.values())
        t = min(p for p in left if ms[p] == mn)
        got[t] = (start, mn)
        left.remove(t)
        start = mn
    got[left[0]] = (start, F(m))
    for p in range(n):
        if val(tastes[p], *got[p]) < sum(tastes[p]) / n:
            bad += 1
    if any(val(tastes[p], *got[q]) > val(tastes[p], *got[p]) for p in range(n) for q in range(n)):
        envyc += 1
print('random trials', trials, 'proportionality failures', bad, 'trials with envy', envyc)

# ---------------------------------------------------------------- revision checks
# Shared worked example RBR|BRR: one cut, after card 3, and the trays hold the
# same counts in different orders.  It is not one of the printed task trains.
assert min_cuts('RBRBRR') == 1
tasks = ["RBRB", "RRBB", "BRRB", "BBRR", "RBBR", "BRBR",
         "RRRRBB", "BRRBRR", "RBRBR", "RRBBBBRR", "RRRRBBBB", "RRRBBBBRRR", "RRRRRRBBBB",
         "RBBRRR", "BRRBRRBB", "RRRBBBBR", "RBRRBRB", "RRBRRRBBBR", "RBBRRRRBBR",
         "BRRBRBBR", "RBRRRRBRBB", "BBRRRRRRBB", "RRRRRRBB"]
assert 'RBRBRR' not in tasks and 'RRBRBR' not in tasks
print('shared example RBRBRR: one cut, not a task train')
# K-1 P5: no train with at most 6 reds and 4 blues needs three pull-aparts
assert all((min_cuts(s) or 0) <= 2 for r in range(7) for b in range(5)
           for s in distinct_orders(r, b) if r + b > 0)
print('K-1 P5: no train with <= 6R, <= 4B needs three cuts')
