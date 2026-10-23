#!/usr/bin/env python3
"""Independent mathematical checks for Week 92 (Fold-and-stretch predictions).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

The move is the tent map on the continuous track [0, 16]:
    T(x) = 2 * min(x, 16 - x).
A band [a, b] is the set of all possible positions of one marker.

Two independent ways of computing the image of a band under n moves are used
and compared:
  (A) iterate the one-move interval image (continuous map, so the image of an
      interval is an interval; one move is computed from the definition by
      checking the two ends and the turn at 8 when it lies inside);
  (B) treat T^n directly as a piecewise-linear map whose only possible turns
      are the dyadic points 16k/2^n, and take min/max of T^n over the band's
      ends and every such point inside the band.
All arithmetic is exact (fractions).

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
OUT = []


def say(*args):
    line = ' '.join(str(a) for a in args)
    OUT.append(line)
    print(line)


def T(x):
    x = F(x)
    return 2 * min(x, 16 - x)


def Tn(x, n):
    for _ in range(n):
        x = T(x)
    return x


def image_A(a, b):
    a, b = F(a), F(b)
    vals = [T(a), T(b)]
    if a <= 8 <= b:
        vals.append(T(8))
    return min(vals), max(vals)


def iterate_A(a, b, n):
    for _ in range(n):
        a, b = image_A(a, b)
    return a, b


def iterate_B(a, b, n):
    a, b = F(a), F(b)
    pts = {a, b}
    step = F(16, 2 ** n) if n > 0 else F(16)
    k0 = int(a // step)
    for k in range(k0, int(b // step) + 2):
        p = k * step
        if a <= p <= b:
            pts.add(p)
    vals = [Tn(p, n) for p in pts]
    return min(vals), max(vals)


def fmt(iv):
    a, b = iv
    return '[%s, %s]' % (a, b)


def check(cond, label):
    say(('PASS ' if cond else 'FAIL ') + label)
    return cond


ALL_OK = True

# ---------------------------------------------------------------- sanity
say('== Map sanity')
ALL_OK &= check(T(13) == 6, 'worked example: input 13 -> distance 3 -> output 6')
ALL_OK &= check(min(F(13), 16 - F(13)) == 3, 'worked example distance is 3')
# Page 2 worked visual: [5,10] -> distance band [5,8] -> output band [10,16]
dists = [min(F(x, 100), 16 - F(x, 100)) for x in range(500, 1001)]
ALL_OK &= check((min(dists), max(dists)) == (5, 8), 'page 2 distance band for [5,10] is [5,8]')
ALL_OK &= check(image_A(5, 10) == (10, 16) == iterate_B(5, 10, 1), 'page 2 output band for [5,10] is [10,16]')
ALL_OK &= check(T(5) == 10 and T(8) == 16 and T(10) == 12, 'page 2 plotted points (5,10), (8,16), (10,12)')

# ---------------------------------------------------------------- P1
say('\n== Problem 1 (Grades 2-3)')
meet = [(a, b) for a, b in combinations(range(17), 2) if T(a) == T(b)]
say('pairs of different whole-number starts that meet after one move:', meet)
ALL_OK &= check(meet == [(k, 16 - k) for k in range(8)], 'exactly the 8 mirror pairs (k, 16-k), k=0..7 (guide list)')


def gaps(a, b, n):
    g = [abs(F(a) - F(b))]
    for _ in range(n):
        a, b = T(a), T(b)
        g.append(abs(a - b))
    return g


inc3_from_start = [(a, b) for a, b in combinations(range(17), 2)
                   if all(x < y for x, y in zip(gaps(a, b, 3), gaps(a, b, 3)[1:]))]
say('pairs whose gap strictly grows on moves 1, 2, 3:', len(inc3_from_start), 'of 136:', inc3_from_start)
ALL_OK &= check((0, 1) in inc3_from_start, 'guide example (0,1): gaps %s' % [str(g) for g in gaps(0, 1, 5)])
# any three consecutive moves (not necessarily starting at move 1)
inc3_any = []
for a, b in combinations(range(17), 2):
    g = gaps(a, b, 8)
    if any(g[i] < g[i + 1] < g[i + 2] < g[i + 3] for i in range(len(g) - 3)):
        inc3_any.append((a, b))
say('pairs whose gap strictly grows for some three consecutive moves:', len(inc3_any))
say('(0,1) orbit:', [(str(Tn(0, k)), str(Tn(1, k))) for k in range(6)], '-> gap grows on 4 moves in a row, then 0')

orbit_len = {}
for s in range(17):
    k = 0
    x = F(s)
    while x != 0:
        x = T(x)
        k += 1
    orbit_len[s] = k
say('moves for each whole-number start to reach 0:', orbit_len)
ALL_OK &= check(max(orbit_len.values()) == 5, 'every whole-number start reaches 0 within five moves (max is 5)')
ALL_OK &= check(all(Tn(s, 4) in (0, 16) for s in range(17)), 'after four moves every whole-number start is at an end (0 or 16)')
ALL_OK &= check(T(F(32, 3)) == F(32, 3), 'guide: 32/3 is a fixed point')
fixed = [x for x in (F(0), F(32, 3))]
say('fixed points of T on [0,16]: 2x=x -> 0; 32-2x=x -> 32/3 ->', fixed)

# ---------------------------------------------------------------- P2
say('\n== Problem 2 (Grades 2-3)')
p2 = [(1, 4), (10, 15), (6, 11), (2, 14)]
guide2 = [(2, 8), (2, 12), (10, 16), (4, 16)]
for (a, b), g in zip(p2, guide2):
    A, B = image_A(a, b), iterate_B(a, b, 1)
    ALL_OK &= check(A == B == g, 'start [%d,%d] -> %s (guide %s)' % (a, b, fmt(A), fmt(g)))

# ---------------------------------------------------------------- P3
say('\n== Problem 3 (Grades 2-3)')
for (a, b), want in [((1, 2), 4), ((7, 9), 4)]:
    hist = [fmt(iterate_A(a, b, n)) for n in range(6)]
    hb = [fmt(iterate_B(a, b, n)) for n in range(6)]
    first = next(n for n in range(10) if iterate_A(a, b, n) == (0, 16))
    ALL_OK &= check(hist == hb and first == want,
                    'start [%d,%d]: %s ; first full track after %d moves (page gives 4 tracks)' % (a, b, ' -> '.join(hist[:5]), first))

# ---------------------------------------------------------------- P4
say('\n== Problem 4 (Grades 4-5)')
ALL_OK &= check(T(6) == T(10) == 12 and image_A(6, 10) == (12, 16), '[6,10]: both ends -> 12, full output [12,16]')
for (a, b) in [(7, 9), (3, 11), (5, 11)]:
    say('  guide/other example [%d,%d] -> ends %s,%s ; full %s' % (a, b, T(a), T(b), fmt(image_A(a, b))))
# characterise: endpoint shading [min(Ta,Tb), max(Ta,Tb)] misses places iff a < 8 < b
half = [F(k, 2) for k in range(33)]
bad = True
for a, b in combinations(half, 2):
    ends = (min(T(a), T(b)), max(T(a), T(b)))
    misses = ends != image_A(a, b)
    if misses != (a < 8 < b):
        bad = False
        say('  counterexample to characterisation:', a, b)
ALL_OK &= check(bad, 'over all half-unit bands: endpoint-only shading misses places exactly when 8 is strictly inside')

# ---------------------------------------------------------------- P5
say('\n== Problem 5 (Grades 4-5) and overview width claims')
grid = [F(k, 8) for k in range(129)]
ok_never_narrower = ok_formula = ok_equal_iff_sym = ok_double = True
for a, b in combinations(grid, 2):
    lo, hi = image_A(a, b)
    w, w2 = b - a, hi - lo
    if w2 < w:
        ok_never_narrower = False
    if b <= 8 or a >= 8:
        if w2 != 2 * w:
            ok_double = False
    if a <= 8 <= b:
        if (lo, hi) != (min(2 * a, 32 - 2 * b), 16) or w2 != 2 * max(8 - a, b - 8):
            ok_formula = False
    if a < 8 < b and ((w2 == w) != (8 - a == b - 8)):
        ok_equal_iff_sym = False
ALL_OK &= check(ok_never_narrower, 'no band of positive width gets narrower (all eighth-unit bands)')
ALL_OK &= check(ok_double, 'a band on one half doubles its width')
ALL_OK &= check(ok_formula, 'for a<=8<=b image is [min(2a,32-2b),16], width 2max(8-a,b-8)')
ALL_OK &= check(ok_equal_iff_sym, 'a strictly crossing band keeps its width exactly when symmetric about 8')
ALL_OK &= check(image_A(1, 3) == (2, 6) and image_A(6, 10) == (12, 16), 'guide examples [1,3] width 2->4, [6,10] width 4->4')

# ---------------------------------------------------------------- P6, P7
say('\n== Problems 6-7 (Grades 4-5)')


def stays(q, n):
    return all(iterate_A(0, q, k)[1] <= 2 and iterate_A(0, q, k)[0] >= 0 for k in range(n + 1))


for n, g in [(3, F(1, 4)), (4, F(1, 8)), (6, F(1, 32))]:
    # exact: search the largest q on a fine grid, then confirm the exact value
    cand = [F(k, 4096) for k in range(0, 4097)]
    good = [q for q in cand if stays(q, n)]
    ALL_OK &= check(max(good) == g and stays(g, n) and not stays(g + F(1, 10 ** 9), n),
                    '%d moves: widest [0,q] staying in [0,2] has q = %s (grid max %s); history %s'
                    % (n, g, max(good), ' -> '.join(fmt(iterate_A(0, g, k)) for k in range(n + 1))))
# other reading: only the position after exactly n moves must lie in [0,2]
for n, g in [(3, F(1, 4)), (4, F(1, 8)), (6, F(1, 32))]:
    good = [F(k, 1024) for k in range(0, 16 * 1024 + 1) if iterate_A(0, F(k, 1024), n)[1] <= 2]
    ALL_OK &= check(max(good) == g, '%d moves, "after exactly n moves" reading: widest q is still %s' % (n, max(good)))
# wider bands with one end at 0 up to the whole track: none works even for 1 move beyond q=1
ALL_OK &= check(not any(stays(F(k, 16), 1) for k in range(17, 257)), 'no [0,q] with q>1 stays in [0,2] even for one move')
ALL_OK &= check(all(stays(F(2, 2 ** n), n) for n in range(0, 30)), 'Problem 7: [0, 2/2^n] stays in [0,2] for n moves, n=0..29')
ALL_OK &= check(all(not stays(F(2, 2 ** n), n + 1) for n in range(0, 30)), '... and leaves [0,2] on move n+1 (no single band works forever)')
# enlarged line scale on page 5: whole track unit [0,1] (x 8..18 mm) -> 160 mm line
for q in (F(1, 4), F(1, 8), F(1, 32)):
    say('  answer %s on the 160 mm enlarged 0-1 line sits %s mm from 0' % (q, float(160 * q)))

# ---------------------------------------------------------------- P8 and overview dyadic claim
say('\n== Problem 8 (Grades 4-5) and dyadic coverage')
ok_cover = ok_not_earlier = ok_affine = True
for n in range(1, 11):
    w = F(16, 2 ** n)
    for k in range(2 ** n):
        a, b = k * w, (k + 1) * w
        if iterate_A(a, b, n) != (0, 16) or iterate_B(a, b, n) != (0, 16):
            ok_cover = False
        if iterate_A(a, b, n - 1) == (0, 16):
            ok_not_earlier = False
        # one move sends the piece exactly onto a cell of the 2^(n-1) subdivision
        lo, hi = image_A(a, b)
        if hi - lo != 2 * w or (n > 1 and lo % (2 * w) != 0) or (n == 1 and (lo, hi) != (0, 16)):
            ok_affine = False
ALL_OK &= check(ok_cover, 'every cell [16k/2^n,16(k+1)/2^n] maps onto [0,16] after n moves, n=1..10 (both methods)')
ALL_OK &= check(ok_not_earlier, '... and not after n-1 moves')
ALL_OK &= check(ok_affine, 'one move sends each 2^n-cell exactly onto a 2^(n-1)-cell (guide induction step)')
pieces = {'A': (0, 8), 'B': (8, 16)}
for i, L in enumerate('CDEF'):
    pieces[L] = (4 * i, 4 * i + 4)
for i, L in enumerate('GHIJKLMN'):
    pieces[L] = (2 * i, 2 * i + 2)
moves = {L: (1 if L in 'AB' else 2 if L in 'CDEF' else 3) for L in pieces}
for L, (a, b) in pieces.items():
    hist = [fmt(iterate_A(a, b, k)) for k in range(moves[L] + 1)]
    ALL_OK &= check(iterate_A(a, b, moves[L]) == (0, 16), 'piece %s = [%d,%d], %d move(s): %s' % (L, a, b, moves[L], ' -> '.join(hist)))

# ---------------------------------------------------------------- P9
say('\n== Problem 9 (Grades 4-5)')
random.seed(92)
ok_fill = ok_bound = ok_mono = True
worst = 0
for _ in range(4000):
    den = random.choice([3, 7, 10, 11, 13, 100, 997, 1024, 3000])
    a = F(random.randrange(0, 16 * den), den)
    b = a + F(random.randrange(1, max(2, 16 * den - int(a * den) + 1)), den)
    b = min(b, F(16))
    if b <= a:
        continue
    n = 0
    lo, hi = a, b
    prev_w = b - a
    while (lo, hi) != (0, 16):
        lo, hi = image_A(lo, hi)
        if hi - lo < prev_w:
            ok_mono = False
        prev_w = hi - lo
        n += 1
        if n > 60:
            ok_fill = False
            break
    # guide's proof: choose a dyadic piece width <= (b-a)/2, i.e. 16/2^m <= (b-a)/2; then fill within m moves
    m = 0
    while F(16, 2 ** m) > (b - a) / 2:
        m += 1
    if n > m:
        ok_bound = False
    if iterate_B(a, b, n) != (0, 16):
        ok_fill = False
    worst = max(worst, n)
ALL_OK &= check(ok_fill, '4000 random rational bands (ends between ticks) all reach [0,16]; method B agrees')
ALL_OK &= check(ok_bound, 'each fills no later than the guide proof bound m (16/2^m <= width/2)')
ALL_OK &= check(ok_mono, 'widths never decreased along the way')
ALL_OK &= check(image_A(0, 16) == (0, 16), 'once filled it stays filled: T([0,16]) = [0,16]')
ALL_OK &= check(iterate_A(0, 0, 50) == (0, 0) and iterate_A(F(32, 3), F(32, 3), 50) == (F(32, 3), F(32, 3)),
                'zero-width bands are genuine exceptions (0 and 32/3 stay put)')
# guide claim: a pair of consecutive subdivision marks lies inside [a,b] whenever piece width < (b-a)/2
ok_piece = True
for _ in range(3000):
    den = random.choice([7, 13, 1000])
    a = F(random.randrange(0, 15 * den), den)
    b = a + F(random.randrange(1, den), den)
    if b > 16:
        continue
    m = 0
    while not F(16, 2 ** m) < (b - a) / 2:
        m += 1
    w = F(16, 2 ** m)
    k = -(-a // w)  # ceil
    if not (a <= k * w and (k + 1) * w <= b):
        ok_piece = False
ALL_OK &= check(ok_piece, 'guide P9 step: piece width < half the band width always fits a whole piece inside')

say('\nALL CHECKS PASSED' if ALL_OK else '\nSOME CHECK FAILED')
(HERE / (Path(__file__).name + '.out')).write_text('\n'.join(OUT) + '\n')
