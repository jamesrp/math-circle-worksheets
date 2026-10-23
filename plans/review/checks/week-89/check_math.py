#!/usr/bin/env python3
"""Independent mathematics check for Week 89 (Growing shapes and totals).

Written for the review; does not import or run the package's own check_math.py.
Standard library only. Finds the repository by walking up from this file
(four folders up from plans/review/checks/week-89/, three from tmp/review-runs/week-89/).
"""
from fractions import Fraction
from itertools import permutations, product, combinations
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent


def find_repo():
    for p in [HERE, *HERE.parents]:
        if (p / 'AGENTS.md').exists() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(HERE))


REPO = find_repo()
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def note(msg):
    print('NOTE ' + msg)


# ---------------------------------------------------------------- shapes
def square(n):
    return {(x, y) for x in range(n) for y in range(n)}


def stairs(n):
    # row with k tiles sits at height n-k, left-aligned (as \stairfig draws it)
    return {(x, n - k) for k in range(1, n + 1) for x in range(k)}


def rect(n):
    # n rows, n+1 columns (as \rectfig draws it)
    return {(x, y) for x in range(n + 1) for y in range(n)}


print('== Problems 1, 2, 3, 5, 6: layers kept in a corner ==')
sq_layers, st_layers, re_layers = [], [], []
for n in range(1, 6):
    a, b = square(n), square(n + 1)
    check(a <= b, f'square side {n} sits in the corner of side {n+1}')
    layer = b - a
    row = {c for c in layer if c[1] == n}
    col = layer - row
    check(len(row) == n + 1 and len(col) == n and len(layer) == 2 * n + 1,
          f'square layer {n}->{n+1}: row {len(row)} + column {len(col)} = {len(layer)}')
    sq_layers.append(len(layer))
for n in range(1, 6):
    a = stairs(n)
    b = {(x, y + 1) for (x, y) in a} | {(x, 0) for x in range(n + 1)}  # old rows lifted, new bottom row
    check(b == stairs(n + 1), f'stairs {n} rows + new bottom row of {n+1} = stairs {n+1} rows')
    st_layers.append(len(b) - len(a))
for n in range(1, 6):
    a, b = rect(n), rect(n + 1)
    check(a <= b, f'rectangle {n}x{n+1} sits in the corner of {n+1}x{n+2}')
    layer = b - a
    row = {c for c in layer if c[1] == n}
    check(len(row) == n + 2 and len(layer - row) == n and len(layer) == 2 * n + 2,
          f'rectangle layer {n}->{n+1}: row {n+2} + column {n} = {len(layer)}')
    re_layers.append(len(layer))
print('P6 table squares', sq_layers, 'stairs', st_layers, 'rectangles', re_layers)
check(sq_layers == [3, 5, 7, 9, 11] and st_layers == [2, 3, 4, 5, 6] and re_layers == [4, 6, 8, 10, 12],
      'P6 table matches the guide (3..11 / 2..6 / 4..12)')
diffs = [[b - a for a, b in zip(L, L[1:])] for L in (sq_layers, st_layers, re_layers)]
check(diffs == [[2] * 4, [1] * 4, [2] * 4], 'second differences 2, 1, 2 (overview, guide P6)')
check([len(stairs(n)) for n in range(1, 7)] == [1, 3, 6, 10, 15, 21], 'P3 stair totals 1,3,6,10,15,21')
check([len(rect(n)) for n in range(1, 7)] == [2, 6, 12, 20, 30, 42], 'P5 rectangle totals 2,6,12,20,30,42')
check([2 * len(stairs(n)) == len(rect(n)) for n in range(1, 30)] == [True] * 29,
      'two n-stairs have the area of the n x (n+1) rectangle (n<30)')

print('== Problem 2: smaller squares in the bottom-left corner of side 5 ==')
big = square(5)
kept = [k for k in range(1, 5) if square(k) <= big]
check(kept == [1, 2, 3, 4], f'possible nonempty smaller sides {kept}')
check([25 - k * k for k in kept] == [24, 21, 16, 9], 'removed tiles 24,21,16,9 (guide)')


def orientations(cells):
    out = set()
    pts = list(cells)
    for sx, sy, sw in product((1, -1), (1, -1), (False, True)):
        q = [((y if sw else x) * sx, (x if sw else y) * sy) for x, y in pts]
        mx, my = min(a for a, _ in q), min(b for _, b in q)
        out.add(frozenset((a - mx, b - my) for a, b in q))
    return out


def tilings_two(piece, w, h):
    """All ways to cover a w x h rectangle exactly with two copies of piece (any rotation/reflection)."""
    board = {(x, y) for x in range(w) for y in range(h)}
    places = []
    for o in orientations(piece):
        ow = max(a for a, _ in o) + 1
        oh = max(b for _, b in o) + 1
        for dx in range(w - ow + 1):
            for dy in range(h - oh + 1):
                places.append(frozenset((a + dx, b + dy) for a, b in o))
    sols = set()
    pset = set(places)
    for p in places:
        rest = frozenset(board - p)
        if rest in pset:
            sols.add(frozenset((p, rest)))
    return sols


print('== Problem 4: two copies of the same stairs make a rectangle ==')
for n in range(2, 7):
    area = 2 * len(stairs(n))
    found = {}
    for w in range(1, area + 1):
        if area % w == 0:
            h = area // w
            if w <= h:
                t = tilings_two(stairs(n), h, w) if h >= w else set()
                found[(w, h)] = len(t)
    good = {k: v for k, v in found.items() if v}
    check(list(good) == [(n, n + 1)], f'n={n}: only the {n}x{n+1} rectangle works; tilings per rectangle {found}')

# ---------------------------------------------------------------- machines
print('== Problem 7: one tray, every order ==')
for start in (0, 3):
    finals = set()
    for order in permutations([0, 1, 2, 3, 4]):
        t = start
        for u in order:
            t += u
        finals.add(t)
    check(finals == {start + 10}, f'start {start}: all 120 orders end at {finals}')

print('== Problem 8: recover inputs ==')
start, totals = 2, [5, 5, 9, 12]
inputs = [b - a for a, b in zip([start] + totals, totals)]
check(inputs == [3, 0, 4, 3], f'inputs {inputs}')

print('== Problem 9: hidden start ==')
totals = [4, 7, 7, 12]
sols = []
for b in range(-20, 40):
    for us in product(range(6), repeat=4):
        t, row = b, []
        for u in us:
            t += u
            row.append(t)
        if row == totals:
            sols.append((b, us))
print('all integer starts:', sols)
nonneg = [s for s in sols if s[0] >= 0]
check(nonneg == [(b, (4 - b, 3, 0, 5)) for b in range(5)], 'nonnegative starts 0..4 with inputs (4-b,3,0,5): 5 cases')
check([s for s in sols if s[0] < 0] == [(-1, (5, 3, 0, 5))],
      'only extra integer solution is start -1 (excluded because a start is a pile of counters)')

print('== Problem 10: same inputs, different starts ==')


def run1(start, us):
    out, t = [start], start
    for u in us:
        t += u
        out.append(t)
    return out


r1, r4 = run1(1, [2, 0, 3, 1]), run1(4, [2, 0, 3, 1])
check(r1 == [1, 3, 3, 6, 7] and r4 == [4, 6, 6, 9, 10], f'rows {r1} {r4}')
check({b - a for a, b in zip(r1, r4)} == {3}, 'gap stays 3')
ok = all({y - x for x, y in zip(run1(b, us), run1(c, us))} == {c - b}
         for b in range(4) for c in range(4) for us in product(range(3), repeat=4))
check(ok, 'gap equals difference of starts for every small input list')


def run2(us, a=0, b=0):
    rows = []
    for u in us:
        a += u
        b += a  # copy of the NEW first total
        rows.append((a, b))
    return rows


print('== Problems 11-13: two-stage cascade ==')
check(run2([2], 1, 1) == [(3, 4)], 'page 6 worked turn: (1,1) with input 2 -> (3,4)')
orders = sorted(set(permutations([2, 2, 1, 0, 0])))
vals = {o: run2(o)[-1][1] for o in orders}
mx, mn = max(vals.values()), min(vals.values())
check(len(orders) == 30, f'{len(orders)} distinct orders')
check(mx == 21 and [o for o in orders if vals[o] == mx] == [(2, 2, 1, 0, 0)], 'maximum 21, only from 2,2,1,0,0')
check(mn == 9 and [o for o in orders if vals[o] == mn] == [(0, 0, 1, 2, 2)], 'minimum 9, only from 0,0,1,2,2')
check(run2((2, 2, 1, 0, 0)) == [(2, 2), (4, 6), (5, 11), (5, 16), (5, 21)], 'guide max table rows')
check(run2((0, 0, 1, 2, 2)) == [(0, 0), (0, 0), (1, 1), (3, 4), (5, 9)], 'guide min table rows')
print('values reached:', sorted(set(vals.values())))
# weighted formula
ok = all(run2(us)[-1][1] == sum((len(us) - i) * u for i, u in enumerate(us))
         for n in range(1, 6) for us in product(range(4), repeat=n))
check(ok, 'B_N = N u1 + (N-1) u2 + ... + uN for all inputs 0..3, N<=5')

print('Problem 12 rows (1 before 3, two zeros):')
rows12 = {}
for pos in combinations(range(4), 2):
    row = [0] * 4
    row[pos[0]], row[pos[1]] = 1, 3
    rows12[tuple(row)] = run2(row)[-1][1]
for k, v in rows12.items():
    print('  ', k, v)
guide12 = {(1, 3, 0, 0): 13, (1, 0, 3, 0): 10, (1, 0, 0, 3): 7, (0, 1, 3, 0): 9, (0, 1, 0, 3): 6, (0, 0, 1, 3): 5}
check(rows12 == guide12, 'guide P12 table exact')
check(max(rows12, key=rows12.get) == (1, 3, 0, 0) and min(rows12, key=rows12.get) == (0, 0, 1, 3),
      'zeros last largest (13), zeros first smallest (5)')
note(f'without the "1 before 3" rule, 3,1,0,0 would give {run2([3,1,0,0])[-1][1]} (the page keeps that rule)')

print('Problem 13: sorted orders are optimal for every 5-input list')
ok = True
for us in product(range(6), repeat=5):
    if list(us) != sorted(us):
        continue
    best = max(run2(p)[-1][1] for p in set(permutations(us)))
    worst = min(run2(p)[-1][1] for p in set(permutations(us)))
    ok &= best == run2(sorted(us, reverse=True))[-1][1] and worst == run2(sorted(us))[-1][1]
check(ok, 'descending maximizes, ascending minimizes, all multisets from 0..5')
rng = random.Random(89)
ok = True
for _ in range(300):
    us = [Fraction(rng.randint(-9, 9), rng.randint(1, 4)) for _ in range(rng.randint(2, 6))]
    vals_ = [run2(p)[-1][1] for p in permutations(us)]
    ok &= max(vals_) == run2(sorted(us, reverse=True))[-1][1] and min(vals_) == run2(sorted(us))[-1][1]
check(ok, 'same with signed rational inputs (guide: "any fixed length and real inputs")')
ok = all(run2([*pre, b, a, *post])[-1][1] - run2([*pre, a, b, *post])[-1][1] == b - a
         for a in range(4) for b in range(4) for pre in product(range(3), repeat=1) for post in product(range(3), repeat=2))
check(ok, 'adjacent exchange a,b -> b,a changes the end total by exactly b-a')

# ---------------------------------------------------------------- rules
print('== Problems 14-15: two building rules ==')


def ruleA(n):
    return square(n)


def ruleB(n):
    tail = {(n + t, 0) for t in range(max(0, n - 4))}
    return square(n) | tail


def rule15(n):
    tail = {(n + t, 0) for t in range(max(0, 2 * (n - 4)))}
    return square(n) | tail


for n in range(1, 5):
    check(ruleA(n) == ruleB(n) == rule15(n) == square(n), f'step {n}: all rules give the pictured square')
check([len(ruleA(n)) for n in (5, 6)] == [25, 36], 'Rule A steps 5,6: 25, 36')
check([len(ruleB(n)) for n in (5, 6)] == [26, 38], 'Rule B steps 5,6: 26, 38')
check(max(x for x, _ in ruleB(6)) + 1 == 8, 'Rule B step 6 is 8 tiles wide (guide)')
check([len(rule15(n)) for n in (5, 6)] == [27, 40], 'guide P15 example: 27, 40')

# ---------------------------------------------------------------- cubes
print('== Problems 16-17: cube shells ==')


def cube(n):
    return {(x, y, z) for x in range(n) for y in range(n) for z in range(n)}


shells = [len(cube(n + 1) - cube(n)) for n in (1, 2, 3)]
check(shells == [7, 19, 37], f'shells {shells}')
check([len(cube(n)) for n in range(1, 5)] == [1, 8, 27, 64], 'totals 1,8,27,64 (64-cube kit is enough)')


def boxes_in(region):
    """All axis boxes contained in region."""
    pts = sorted(region)
    out = []
    rs = set(region)
    xs = sorted({p[0] for p in pts}); ys = sorted({p[1] for p in pts}); zs = sorted({p[2] for p in pts})
    for x0 in xs:
        for x1 in xs:
            if x1 < x0: continue
            for y0 in ys:
                for y1 in ys:
                    if y1 < y0: continue
                    for z0 in zs:
                        for z1 in zs:
                            if z1 < z0: continue
                            b = {(x, y, z) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1) for z in range(z0, z1 + 1)}
                            if b <= rs:
                                out.append(frozenset(b))
    return out


for n in (1, 2, 3, 4):
    shell = cube(n + 1) - cube(n)
    bx = boxes_in(shell)
    flat = all(min(max(c[i] for c in b) - min(c[i] for c in b) for i in range(3)) == 0 for b in bx)
    sizes = set()
    count = 0
    bset = set(bx)
    for i, b1 in enumerate(bx):
        for b2 in bx[i + 1:]:
            if b1 & b2: continue
            rest = frozenset(shell - b1 - b2)
            if rest in bset:
                count += 1
                sizes.add(tuple(sorted((len(b1), len(b2), len(rest)), reverse=True)))
    count //= 3
    check(flat, f'n={n}: every box inside the shell is one cube thick (flatness is automatic)')
    check(count > 0 and sizes == {((n + 1) ** 2, n * (n + 1), n * n)},
          f'n={n}: {count} three-slab splits, all with sizes {sizes}')
    top = {c for c in shell if c[2] == n}
    side = {c for c in shell if c[0] == n and c[2] < n}
    last = {c for c in shell if c[1] == n and c[0] < n and c[2] < n}
    check(top | side | last == shell and len(top) + len(side) + len(last) == len(shell)
          and (len(top), len(side), len(last)) == ((n + 1) ** 2, n * (n + 1), n * n),
          f'n={n}: guide priority split z=n, x=n, y=n gives {(len(top), len(side), len(last))}')
s = [len(cube(n + 1) - cube(n)) for n in range(1, 6)]
check([b - a for a, b in zip(s, s[1:])][:2] == [12, 18], 'shell first differences 12, 18')
c = [n ** 3 for n in range(0, 8)]
d3 = c
for _ in range(3):
    d3 = [b - a for a, b in zip(d3, d3[1:])]
check(set(d3) == {6}, 'cubes have constant third difference 6')

# ---------------------------------------------------------------- three stages and piles
print('== Problems 18-20: three trays and corner piles ==')


def run3(us, s=(0, 0, 0)):
    a, b, c = s
    rows = [(a, b, c)]
    for u in us:
        a += u; b += a; c += b
        rows.append((a, b, c))
    return rows


rows = run3([1] * 10)
check(rows[:7] == [(0, 0, 0), (1, 1, 1), (2, 3, 4), (3, 6, 10), (4, 10, 20), (5, 15, 35), (6, 21, 56)],
      'guide P18 table turns 0..6')
check(all(r == (n, n * (n + 1) // 2, n * (n + 1) * (n + 2) // 6) for n, r in enumerate(rows)),
      'closed forms n, n(n+1)/2, n(n+1)(n+2)/6 for n<=10')
check(run3([1], (2, 3, 4))[-1] == (3, 6, 10), 'page 10 worked turn (2,3,4) -> (3,6,10)')
check(rows[2] == (2, 3, 4) and rows[3] == (3, 6, 10),
      'page 10 worked turn is the task\'s own turn 2 -> turn 3 (guide calls it a "non-task example")')
alt = run3([3])[-1]
check(alt == (3, 3, 3) and alt not in rows and run3([1], alt)[-1] == (4, 7, 10),
      'proposed replacement example: (3,3,3) (one input 3 from zero, off the all-ones path) -> (4,7,10) with input 1')
a, b, c = 3, 3, 3
note(f'copying OLD totals from (3,3,3) would give {(a + 1, b + a, c + b)}, so the example still separates the two readings')
wrong = []
a, b, c = 2, 3, 4
wrong = (a + 1, b + a, c + b)  # if old totals were copied
note(f'copying OLD totals instead would give {wrong} from (2,3,4)')


def pile_by_stacking(n):
    pile = set()
    for step in range(1, n + 1):
        base = {(i, j, 0) for i in range(step) for j in range(step) if i + j < step}  # step-row stairs
        pile = base | {(i, j, k + 1) for (i, j, k) in pile}  # previous pile on the square corner
    return pile


for n in range(1, 13):
    p = pile_by_stacking(n)
    corner = {(i, j, k) for i in range(n) for j in range(n) for k in range(n) if i + j + k < n}
    assert p == corner
check(True, 'stacking rule of P19 gives exactly the corner pile i+j+k<n (n<=12)')
check([len(pile_by_stacking(n)) for n in range(1, 6)] == [1, 4, 10, 20, 35], 'piles 1,4,10,20,35')
check(all(len(pile_by_stacking(n)) == rows[n][2] for n in range(1, 11)), 'pile = third tray for n<=10')
check(len(pile_by_stacking(10)) == 220 == 10 * 11 * 12 // 6 == sum(k * (k + 1) // 2 for k in range(1, 11)),
      'step 10 = 220 = 10*11*12/6 = sum of ten staircase layers')
for n in range(1, 13):
    pile = pile_by_stacking(n)
    img = {(i + 1, i + j + 2, i + j + k + 3) for (i, j, k) in pile}
    trip = set(combinations(range(1, n + 3), 3))
    assert img == trip and len(img) == len(pile)
check(True, 'guide bijection (i+1, i+j+2, i+j+k+3) onto increasing triples from 1..n+2 (n<=12)')

# ---------------------------------------------------------------- overview background facts
print('== Guide overview: difference facts ==')
from math import comb, factorial
ok = True
for d in range(0, 6):
    for _ in range(20):
        co = [rng.randint(-5, 5) for _ in range(d)] + [rng.choice([-3, -2, -1, 1, 2, 3])]
        f = [sum(cc * n ** i for i, cc in enumerate(co)) for n in range(d + 4)]
        for _ in range(d):
            f = [b - a for a, b in zip(f, f[1:])]
        ok &= set(f) == {factorial(d) * co[-1]}
        f = [b - a for a, b in zip(f, f[1:])]
        ok &= set(f) == {0}
check(ok, 'degree-d polynomial: d-th differences constant = d! * leading coefficient, (d+1)-st are 0')
check(all(comb(n + 1, k) - comb(n, k) == comb(n, k - 1) for n in range(0, 20) for k in range(1, 20)),
      'Delta C(n,k) = C(n,k-1) for k>=1')

# ---------------------------------------------------------------- materials
print('== Materials vs tasks ==')
cards = [0, 0, 1, 2, 2, 3, 4]
from collections import Counter
C = Counter(cards)
for name, need in (('P7', [0, 1, 2, 3, 4]), ('P10', [2, 0, 3, 1]), ('P11', [2, 2, 1, 0, 0]), ('P12', [1, 3, 0, 0])):
    check(not (Counter(need) - C), f'{name} inputs {need} available among cards {cards}')
board1, board2 = (6, 6), (7, 6)  # cells (w, h) of 120x120 and 140x120 boards at 20 mm
def fits(cells, wh):
    w = max(x for x, _ in cells) + 1; h = max(y for _, y in cells) + 1
    return w <= wh[0] and h <= wh[1]
check(fits(square(5), board1) and fits(stairs(6), board1) and fits(ruleA(6), board1), 'P1/P2 side 5, P3 6-row stairs, Rule A step 6 fit board 1')
check(fits(rect(6), board2), 'P4/P5 6x7 rectangle fits board 2 (7 wide, 6 tall)')
check(not fits(ruleB(6), board2) and fits(ruleB(5), board1), 'Rule B step 6 (8 wide) needs the tabletop; step 5 fits')
check(max(len(rect(6)), len(ruleB(6)), len(square(6))) <= 72, 'largest single shape (42) within 72 tiles')

print()
print('FAILURES:', len(FAILS))
for f in FAILS:
    print('  ', f)
