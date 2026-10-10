#!/usr/bin/env python3
"""Week 51 (honest measurement ranges): independent mathematical check.

Every range below is computed two ways: exactly from interval endpoints with
Fractions, and by brute force over an exact 1/8-unit grid that contains every
endpoint (the extremes of these piecewise-linear expressions occur at
endpoints, so the grid confirms them; the grid also shows that intermediate
values are attained).  Whole-unit questions are enumerated directly.  The data
are my own transcription of the printed pages; check_diagrams.py confirms the
printed geometry matches it.  No writer or guide checker code is imported.
Output is also saved to out_check_math.txt next to this script.
"""
import itertools
import random
from fractions import Fraction as F
from pathlib import Path

OUT = []
BAD = []
STEP = F(1, 8)


def say(s=''):
    OUT.append(s)
    print(s)


def ok(cond, msg):
    say(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        BAD.append(msg)


def grid(lo, hi, step=STEP):
    lo, hi = F(lo), F(hi)
    n = int((hi - lo) / step)
    return [lo + k * step for k in range(n + 1)]


def rng(vals):
    vals = list(vals)
    return (min(vals), max(vals))


def fmt(r):
    return '[%s, %s]' % (r[0], r[1])


def whole(lo, hi):
    return list(range(int(lo), int(hi) + 1))


# ------------------------------------------------------------------ launch
def launch():
    say('LAUNCH (all bands): A 2-3, B 1-2')
    r = rng(a + b for a in grid(2, 3) for b in grid(1, 2))
    ok(r == (3, 5), 'join range %s = [3,5] (printed "A + B: 3 to 5 units", joins 2+1=3, 3+2=5)' % fmt(r))


# ------------------------------------------------------------- problem 1
def p1():
    say('PROBLEM 1 (all bands): A 4-6, B 3-4')
    sums = sorted(set(a + b for a in grid(4, 6) for b in grid(3, 4)))
    ok((sums[0], sums[-1]) == (7, 10), 'tight join range [%s,%s] = [7,10]' % (sums[0], sums[-1]))
    ok(all(F(k, 8) in sums for k in range(56, 81)), 'every 1/8 value from 7 to 10 occurs (continuous range)')
    w8 = sorted((a, b) for a in whole(4, 6) for b in whole(3, 4) if a + b == 8)
    ok(w8 == [(4, 4), (5, 3)], 'K-1 "exactly at 8": whole-unit ways %s (guide: 4+4, 5+3)' % w8)
    beat = [(a, b, a + b) for a, b in [(4, 3), (6, 4)]]
    ok(all(not (8 <= s <= 9) for _, _, s in beat), 'older: claim "between 8 and 9" defeated by %s' % beat)


# ------------------------------------------------------------- problem 2
CARDS = {'A': (4, 6), 'B': (3, 4), 'C': (4, 5), 'D': (4, 5), 'E': (6, 8), 'F': (2, 4)}


def p2():
    say('PROBLEM 2: printed pairs A+B, C+D, E+F')
    res = {}
    for x, y in [('A', 'B'), ('C', 'D'), ('E', 'F')]:
        r = rng(a + b for a in grid(*CARDS[x]) for b in grid(*CARDS[y]))
        reach8 = r[0] >= 8
        fit10 = r[1] <= 10
        res[x + y] = (r, reach8, fit10)
        say('       %s+%s: sum %s; always reaches 8: %s; always fits within 10: %s' % (x, y, fmt(r), reach8, fit10))
    k1 = [p for p, v in res.items() if v[1]]
    older = [p for p, v in res.items() if v[1] and v[2]]
    ok(k1 == ['CD', 'EF'], 'K-1 ("always reach 8"): %s (guide: C with D and E with F)' % k1)
    ok(older == ['CD'], 'older (reach 8 and fit within 10): %s (guide: C with D alone)' % older)
    ok(res['AB'][2] and not res['EF'][2] and res['EF'][1] and not res['AB'][1],
       'each rejected older pair fails exactly one promise (A+B: reach, 4+3=7; E+F: fit, 8+4=12)')
    # For information: what cross-pairings would do (the page restricts to printed pairs).
    cross = []
    for x, y in itertools.combinations('ABCDEF', 2):
        lo = CARDS[x][0] + CARDS[y][0]
        hi = CARDS[x][1] + CARDS[y][1]
        if lo >= 8 and hi <= 10:
            cross.append(x + y)
    say('       info: all pairings meeting both older promises: %s' % cross)


# ------------------------------------------------------------- problem 3
def p3():
    say('PROBLEM 3: A 3-4; B card so every join reaches 7 and fits within 9')
    A = grid(3, 4)
    for lo, hi in [(3, 4), (4, 5), (5, 6)]:
        sums = [a + b for a in A for b in grid(lo, hi)]
        r = rng(sums)
        say('       K-1 card B %d-%d: joins %s; reaches 7: %s; fits within 9 (<=9): %s; fits strictly below 9: %s'
            % (lo, hi, fmt(r), r[0] >= 7, r[1] <= 9, r[1] < 9))
    good = [(lo, hi) for lo, hi in [(3, 4), (4, 5), (5, 6)]
            if min(a + b for a in A for b in grid(lo, hi)) >= 7 and max(a + b for a in A for b in grid(lo, hi)) <= 9]
    ok(good == [(4, 5)], 'K-1 answer: card %s only (guide: 4-5; 3-4 fails at 6, 5-6 fails at 10)' % good)
    strict = [(lo, hi) for lo, hi in [(3, 4), (4, 5), (5, 6)]
              if min(a + b for a in A for b in grid(lo, hi)) >= 7 and max(a + b for a in A for b in grid(lo, hi)) < 9]
    say('       note: if "fits within 9" excluded ending at 9, no K-1 card would work: %s' % strict)
    # Older: all intervals [p,q] on a 1/4 grid inside [0,10].
    pts = grid(0, 10, F(1, 4))
    valid = [(p, q) for p in pts for q in pts if p <= q
             and p + 3 >= 7 and q + 4 <= 9]
    widest = max(q - p for p, q in valid)
    best = [(p, q) for p, q in valid if q - p == widest]
    ok(best == [(4, 5)], 'older widest B card on a 1/4 grid: %s, width %s (guide: unique [4,5])' % (best, widest))
    ok(all(4 <= p and q <= 5 for p, q in valid), 'every valid card lies inside [4,5] (so [4,5] is the unique widest)')


# ------------------------------------------------------------- problem 4
def p4():
    say('OLDER PROBLEM 4: A 4-6, B 3-4; uncover one strip')
    wa = set(max(a + b for b in grid(3, 4)) - min(a + b for b in grid(3, 4)) for a in grid(4, 6))
    wb = set(max(a + b for a in grid(4, 6)) - min(a + b for a in grid(4, 6)) for b in grid(3, 4))
    ok(wa == {1} and wb == {2}, 'uncover A leaves width %s for every a; uncover B leaves width %s for every b; answer A' % (wa, wb))


# ---------------------------------------------- K-1 P4 / older P5 (shared A)
def shared():
    say('K-1 PROBLEM 4 / OLDER PROBLEM 5: A 4-6, B 4-6; white add-ons 4 and 1')
    top = set((a + 4) - (a + 1) for a in grid(4, 6))
    ok(top == {3}, 'top (A+4 vs same A+1): gap always %s' % top)
    gaps = sorted(set((a + 4) - (b + 1) for a in grid(4, 6) for b in grid(4, 6)))
    ok((gaps[0], gaps[-1]) == (1, 5), 'bottom (A+4 vs separate B+1): gap [%s,%s] = [1,5]; witnesses (4,6)->1, (6,4)->5'
       % (gaps[0], gaps[-1]))
    ok(min(gaps) > 0, 'A+4 always ends to the right of B+1 (no negative gaps)')
    ok((5 + 4) - (5 + 1) == 3 and (5 + 4) - (4 + 1) == 4, 'drawn settings: top gap 3, bottom gap 4 (A=5, B=4)')
    fixed = rng((5 + 4) - (b + 1) for b in grid(4, 6))
    say('       info: if A were held at the drawn 5 in the bottom picture, the gap would only range %s' % fmt(fixed))


# --------------------------------------------------------- K-1 P5, P6
def k1_gaps():
    say('K-1 PROBLEM 5: long 7-9, short 5-6')
    r = rng(l - s for l in grid(7, 9) for s in grid(5, 6))
    ok(r == (1, 4), 'gap range %s: biggest 9-5=4, smallest 7-6=1' % fmt(r))
    ok(7 - 5 != r[0], 'shortest minus shortest (7-5=2) is not the smallest gap (guide remark)')
    say('K-1 PROBLEM 6: gap of 3 with the same strips')
    w = [(l, s) for l in whole(7, 9) for s in whole(5, 6) if l - s == 3]
    ok(w == [(8, 5), (9, 6)], 'whole-unit ways: %s (guide: 8-5, 9-6)' % w)
    half = [(l, s) for l in grid(7, 9, F(1, 2)) for s in grid(5, 6, F(1, 2)) if l - s == 3]
    say('       info: half-unit ways: %s' % [(str(l), str(s)) for l, s in half])


# ------------------------------------------------------ older P6, P7
def older_gaps():
    say('OLDER PROBLEM 6: long 13-15, short 10-12')
    r = rng(l - s for l in grid(13, 15) for s in grid(10, 12))
    ok(r == (1, 5), 'gap range %s; witnesses 13-12=1, 15-10=5; always positive' % fmt(r))
    say('OLDER PROBLEM 7: subtract middle values')
    mid = F(13 + 15, 2) - F(10 + 12, 2)
    ok(mid == 3 and r[0] < 3 < r[1], 'middle values give %s, which is possible but not forced (range %s)' % (mid, fmt(r)))


# --------------------------------------------------------- exact total 9
def total9():
    say('K-1 PROBLEM 7 / GRADES 2-3 PROBLEM 8: A 4-6, B 3-5, A+B = 9, whole units')
    pairs = [(a, b) for a in whole(4, 6) for b in whole(3, 5) if a + b == 9]
    ok(pairs == [(4, 5), (5, 4), (6, 3)], 'ordered pairs %s; three boards printed' % pairs)


# ------------------------------------------------------- 4-5 P8 and P9
def upper():
    say('GRADES 4-5 PROBLEM 8: A 7-10, B 3-7, A+B = 12')
    feas = [(a, 12 - a) for a in grid(7, 10) if 3 <= 12 - a <= 7]
    ar = rng(a for a, _ in feas)
    br = rng(b for _, b in feas)
    gr = rng(a - b for a, b in feas)
    ok(ar == (7, 9) and br == (3, 5), 'feasible A %s, B %s (guide: A in [7,9], B in [3,5])' % (fmt(ar), fmt(br)))
    ok(gr == (2, 6), 'gap A-B range %s (guide: 2 to 6; witnesses (7,5), (9,3))' % fmt(gr))
    ok(all(a > b for a, b in feas), 'A is always the longer strip')
    ok(not (3 <= 12 - 10 <= 7), 'A = 10 would need B = 2, not allowed')
    free = rng(a - b for a in grid(7, 10) for b in grid(3, 7))
    say('       info: without the total the gap would range %s' % fmt(free))
    say('GRADES 4-5 PROBLEM 9: join A 4-6 to B 3-4, remove the same A')
    rem = rng((a + b) - a for a in grid(4, 6) for b in grid(3, 4))
    ok(rem == (3, 4), 'remainder range %s = B\'s range' % fmt(rem))
    naive = (7 - 6, 10 - 4)
    ok(naive == (1, 6), 'claimed range from separate ranges: %s' % (naive,))
    t7 = [(a, b) for a in grid(4, 6) for b in grid(3, 4) if a + b == 7]
    t10 = [(a, b) for a in grid(4, 6) for b in grid(3, 4) if a + b == 10]
    ok(t7 == [(4, 3)] and t10 == [(6, 4)], 'total 7 forces (4,3), total 10 forces (6,4), so remainders 1 and 6 never occur')


# ----------------------------------------------------- guide overview claims
def overview():
    say('GUIDE OVERVIEW: interval sum and difference formulas, tightness (random tests)')
    random.seed(51)
    bad = 0
    for _ in range(300):
        L = F(random.randint(0, 40), 4); U = L + F(random.randint(0, 16), 4)
        V = F(random.randint(0, 40), 4); W = V + F(random.randint(0, 16), 4)
        A = grid(L, U, F(1, 4)); B = grid(V, W, F(1, 4))
        s = rng(a + b for a in A for b in B)
        d = rng(a - b for a in A for b in B)
        if s != (L + V, U + W) or d != (L - W, U - V):
            bad += 1
    ok(bad == 0, 'a+b in [L+V,U+W], a-b in [L-W,U-V], both endpoints attained: 300 random cases, %d failures' % bad)
    say('GUIDE: "in every printed gap task the designated upper/longer join stays to the right"')
    tasks = {
        'shared top (A+4)-(A+1)': [(a + 4) - (a + 1) for a in grid(4, 6)],
        'shared bottom (A+4)-(B+1)': [(a + 4) - (b + 1) for a in grid(4, 6) for b in grid(4, 6)],
        'K-1 P5 long-short': [l - s for l in grid(7, 9) for s in grid(5, 6)],
        'older P6 long-short': [l - s for l in grid(13, 15) for s in grid(10, 12)],
        '4-5 P8 A-B with A+B=12': [a - (12 - a) for a in grid(7, 10) if 3 <= 12 - a <= 7],
    }
    ok(all(min(v) > 0 for v in tasks.values()), 'minimum gaps: %s' % {k: str(min(v)) for k, v in tasks.items()})


# ------------------------------------------------------------------ bonus
def bonus():
    say('BONUS PROBLEM 1: whole sides >= 1 with A + B = 6')
    rect = [(a, 6 - a, a * (6 - a)) for a in range(1, 6)]
    areas = [r[2] for r in rect]
    ok(areas == [5, 8, 9, 8, 5], 'labelled pairs and areas %s' % rect)
    ok((min(areas), max(areas)) == (5, 9), 'smallest 5 (1x5, 5x1), largest 9 (3x3); tight honest range [5,9]')
    shapes = sorted(set(tuple(sorted(r[:2])) for r in rect))
    ok(len(shapes) == 3 and len(rect) == 5, 'three shapes up to rotation, five labelled pairs (table has 5 rows)')
    naive = (1 * 1, 5 * 5)
    ok(not any(a * b in naive for a, b, _ in rect), 'neither 1 nor 25 occurs with A+B=6 (1 needs 1x1, sum 2; 25 needs 5x5, sum 10)')
    real = rng(a * (6 - a) for a in grid(1, 5))
    ok(real == (5, 9), 'with real sides in [1,5] and A+B=6 the area range is also %s' % fmt(real))
    ok(max(areas) <= 25, 'twenty-five 20-mm tiles cover every rectangle and the 5x5 of the false claim')

    say('BONUS PROBLEM 2: cards for one hidden length')
    rows = [[(2, 7), (4, 9), (5, 6)], [(1, 4), (3, 8), (5, 9)], [(1, 4), (6, 8), (7, 9)]]
    pts = grid(0, 10, F(1, 8))
    r1 = [x for x in pts if all(lo <= x <= hi for lo, hi in rows[0])]
    ok((min(r1), max(r1)) == (5, 6) and len(r1) == 9, 'row 1 all true: lengths 5 to 6 (every 1/8 value in between)')
    expect = {1: {0: (5, 8), 2: (3, 4)}, 2: {0: (7, 8)}}
    for ri in (1, 2):
        got = {}
        for k in range(3):
            w = [x for x in pts if not (rows[ri][k][0] <= x <= rows[ri][k][1])
                 and all(lo <= x <= hi for j, (lo, hi) in enumerate(rows[ri]) if j != k)]
            if w:
                got[k] = (min(w), max(w))
            others = [c for j, c in enumerate(rows[ri]) if j != k]
            inter = (max(c[0] for c in others), min(c[1] for c in others))
            say('       row %d, card %d (%s) false: others meet in %s; witnesses %s'
                % (ri + 1, k + 1, rows[ri][k], inter if inter[0] <= inter[1] else 'nothing',
                   fmt(got[k]) if k in got else 'none'))
            if inter[0] <= inter[1]:
                disjoint = inter[1] < rows[ri][k][0] or inter[0] > rows[ri][k][1]
                ok(disjoint, 'row %d card %d: the other cards\' common range is disjoint from it (guide claim)' % (ri + 1, k + 1))
        ok(got == expect[ri], 'row %d possible false cards %s (guide: %s)'
           % (ri + 1, {k + 1: fmt(v) for k, v in got.items()}, {k + 1: v for k, v in expect[ri].items()}))

    say('BONUS PROBLEM 3: separate lengths, end gap |A-B|')
    pairs = [((3, 7), (5, 9)), ((2, 4), (6, 8)), ((3, 5), (5, 7))]
    expect3 = [((0, 6), True, True, True), ((2, 6), False, True, False), ((0, 4), False, True, True)]
    for (a, b), ex in zip(pairs, expect3):
        vals = [(x, y) for x in grid(*a) for y in grid(*b)]
        r = rng(abs(x - y) for x, y in vals)
        alonger = any(x > y for x, y in vals)
        blonger = any(y > x for x, y in vals)
        tie = any(x == y for x, y in vals)
        ties = sorted(set(x for x, y in vals if x == y))
        ok((r, alonger, blonger, tie) == ex,
           'A %s, B %s: gap %s; A longer %s, B longer %s, match %s%s'
           % (a, b, fmt(r), alonger, blonger, tie,
              (' (only at %s)' % ties[0]) if len(ties) == 1 else ''))
    vals = [(x, y) for x in grid(4, 6) for y in grid(4, 6)]
    ok(max(abs(x - y) for x, y in vals) == 2 and any(x > y for x, y in vals) and any(y > x for x, y in vals),
       'guide design A 4-6, B 4-6: gap at most 2, either strip can be longer')
    # how much room does the design task have? (1/2-unit cards inside [0,10])
    hp = grid(0, 10, F(1, 2))
    designs = [(a, b, c, d) for a, b in itertools.combinations_with_replacement(hp, 2)
               for c, d in itertools.combinations_with_replacement(hp, 2)
               if max(b - c, d - a) <= 2 and b > c and d > a]
    say('       info: %d half-unit card pairs inside 0-10 meet the design task; largest total width %s'
        % (len(designs), max((b - a) + (d - c) for a, b, c, d in designs)))

    say('BONUS GUIDE OVERVIEW formulas (random tests)')
    random.seed(5151)
    bad = 0
    for _ in range(400):
        a = F(random.randint(0, 40), 4); b = a + F(random.randint(0, 12), 4)
        c = F(random.randint(0, 40), 4); d = c + F(random.randint(0, 12), 4)
        vals = [(x, y) for x in grid(a, b, F(1, 4)) for y in grid(c, d, F(1, 4))]
        lo = min(abs(x - y) for x, y in vals); hi = max(abs(x - y) for x, y in vals)
        if lo != max(0, a - d, c - b) or hi != max(abs(a - d), abs(b - c)):
            bad += 1
        if any(x > y for x, y in vals) != (b > c) or any(y > x for x, y in vals) != (d > a):
            bad += 1
        if any(x == y for x, y in vals) != (max(a, c) <= min(b, d)):
            bad += 1
        ar = rng(x * y for x, y in vals)
        if ar != (a * c, b * d):
            bad += 1
    ok(bad == 0, 'min |A-B| = max(0,a-d,c-b), max = max(|a-d|,|b-c|), A longer iff b>c, B longer iff d>a, '
                 'tie iff overlap, area in [ac,bd] for nonnegative sides: 400 random cases, %d failures' % bad)


def main():
    for f in (launch, p1, p2, p3, p4, shared, k1_gaps, older_gaps, total9, upper, overview, bonus):
        f()
        say()
    say('FAILURES: %d' % len(BAD))
    for b in BAD:
        say('  ' + b)
    (Path(__file__).resolve().parent / 'out_check_math.txt').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
