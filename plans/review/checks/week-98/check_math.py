#!/usr/bin/env python3
"""Independent mathematical check for Week 98 (Growing from a few seeds).

Written from scratch for the review; it does not import or run the package's
check_math.py.  The printed data (seed positions, circled squares) are typed in
here from the student pages; check_diagrams.py confirms them against the PDFs.

Model: two-neighbour bootstrap growth on an open a-by-b grid (side neighbours
only, no wraparound, no outside cells).  Cells are (row, col), 0-indexed here;
the guide's 1-indexed (row, column) coordinates are converted where quoted.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
import itertools
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT, FAILS = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------- the process
def nbrs(r, c, a, b):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < a and 0 <= cc < b:
            yield rr, cc


def legal(filled, a, b):
    """Empty cells with at least two filled side neighbours."""
    out = []
    for r in range(a):
        for c in range(b):
            if (r, c) in filled:
                continue
            if sum((x in filled) for x in nbrs(r, c, a, b)) >= 2:
                out.append((r, c))
    return out


def closure(seeds, a, b):
    filled = set(seeds)
    while True:
        add = legal(filled, a, b)
        if not add:
            return frozenset(filled)
        filled.add(add[0])          # one legal addition at a time


def fills(seeds, a, b):
    return len(closure(seeds, a, b)) == a * b


def perimeter(filled, a, b):
    """Exposed unit sides: filled cell next to an empty cell or the outside."""
    p = 0
    for (r, c) in filled:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if not (0 <= rr < a and 0 <= cc < b) or (rr, cc) not in filled:
                p += 1
    return p


def cells(a, b):
    return [(r, c) for r in range(a) for c in range(b)]


def g(*rc1):
    """Guide (row, column) from 1 -> 0-indexed cells."""
    return [(r - 1, c - 1) for r, c in rc1]


def sym8(n):
    """The 8 symmetries of an n-by-n square as cell maps."""
    m = n - 1
    return [lambda r, c: (r, c), lambda r, c: (c, m - r),
            lambda r, c: (m - r, m - c), lambda r, c: (m - c, r),
            lambda r, c: (r, m - c), lambda r, c: (m - r, c),
            lambda r, c: (c, r), lambda r, c: (m - c, m - r)]


def orbits(sets, n):
    seen, reps = set(), []
    for s in sets:
        key = frozenset(s)
        if key in seen:
            continue
        orb = {frozenset(f(*x) for x in s) for f in sym8(n)}
        seen |= orb
        reps.append((sorted(s), len(orb)))
    return reps


def show(filled, a, b, seeds=()):
    rows = []
    for r in range(a):
        rows.append(''.join('S' if (r, c) in seeds else
                            ('#' if (r, c) in filled else '.')
                            for c in range(b)))
    return '/'.join(rows)


# --------------------------------------------------------------- 1. the rules
say('== 1. Worked example (both bands, p. 1): 2 rows x 3 columns ==')
ex = [(0, 0), (1, 0), (1, 1)]
first = legal(set(ex), 2, 3)
check(first == [(0, 1)], f'exactly one legal first addition, top middle: {first}')
fin = closure(ex, 2, 3)
check(fin == frozenset(ex + [(0, 1)]),
      f'"Stopped" = seeds + top middle ({show(fin, 2, 3, ex)})')
check(legal(set(fin), 2, 3) == [], 'neither right-hand cell can then fill')
say()

# ------------------------------------------------- 2. order independence
say('== 2. Order independence (2-3 P4; guide overview) ==')


def all_terminals(a, b):
    """For every state of an a-by-b board, the set of terminal states that
    some sequence of legal additions reaches (DP over states, larger first)."""
    N = a * b
    idx = {x: i for i, x in enumerate(cells(a, b))}
    nb = [[idx[y] for y in nbrs(*x, a, b)] for x in cells(a, b)]
    term = [None] * (1 << N)
    multi = 0
    for s in sorted(range(1 << N), key=lambda v: -bin(v).count('1')):
        res = set()
        for i in range(N):
            if s >> i & 1:
                continue
            if sum(s >> j & 1 for j in nb[i]) >= 2:
                res |= term[s | (1 << i)]
        if not res:
            res = {s}
        if len(res) > 1:
            multi += 1
        term[s] = frozenset(res) if len(res) > 1 else res
    return term, multi


for (a, b) in ((3, 3), (4, 4), (2, 3), (3, 4)):
    term, multi = all_terminals(a, b)
    check(multi == 0, f'{a}x{b}: all {1 << (a * b)} starts, every legal order '
          f'reaches one and the same finish (states with >1 finish: {multi})')
diag3 = g((1, 1), (2, 2), (3, 3))
fa = legal(set(diag3), 3, 3)
check(len(fa) == 4, f'guide: three diagonal seeds have four legal first '
      f'additions: {[(r + 1, c + 1) for r, c in fa]}')
say()

# --------------------------------------------- 3. three seeds on 3-by-3
say('== 3. Three seeds on 3x3 (2-3 P1, P3; 4-5 P1) ==')
sizes = {}
for s in itertools.combinations(cells(3, 3), 3):
    sizes.setdefault(len(closure(s, 3, 3)), []).append(s)
say('finish size -> number of the 84 starts: ' +
    ', '.join(f'{k}: {len(v)}' for k, v in sorted(sizes.items())))
check(sorted(sizes) == [3, 4, 6, 9], '4-5 P1: exactly four totals, 3, 4, 6, 9')
check(len(sizes[9]) == 14, f'guide: 14 three-seed filling starts '
      f'({len(sizes[9])})')
check(len(sizes[3]) > 0 and len(sizes[9]) > 0,
      '2-3 P1: a filling and a stuck three-seed start both exist')
table = {3: g((1, 1), (1, 2), (1, 3)), 4: g((1, 1), (1, 2), (2, 1)),
         6: g((1, 1), (1, 2), (2, 3)), 9: g((1, 1), (2, 2), (3, 3))}
shape = {3: {(0, 0), (0, 1), (0, 2)},
         4: {(0, 0), (0, 1), (1, 0), (1, 1)},
         6: {(r, c) for r in range(2) for c in range(3)},
         9: set(cells(3, 3))}
for k, s in table.items():
    f = closure(s, 3, 3)
    check(f == shape[k], f'guide P3 table row {k}: finish {show(f, 3, 3, s)} '
          f'matches "{ {3: "the top row", 4: "upper-left 2x2 square", 6: "top two rows", 9: "the full square"}[k]}"')
check(legal(set(table[3]), 3, 3) == [],
      'guide P1: full top row stops immediately')

# The guide's geometric classification of the 84 starts (4-5 P1).
say('-- guide 4-5 P1 classification, tested on every start and every '
    'supporting pair --')
bad, uses = [], 0
for s in itertools.combinations(cells(3, 3), 3):
    f = len(closure(s, 3, 3))
    if not legal(set(s), 3, 3):
        if f != 3:
            bad.append((s, 'no addition', f))
        continue
    for p, q in itertools.combinations(s, 2):
        (third,) = [x for x in s if x not in (p, q)]
        dr, dc = abs(p[0] - q[0]), abs(p[1] - q[1])
        if (dr, dc) == (1, 1):            # diagonal pair -> 2x2 square
            sq = {(r, c) for r in (p[0], q[0]) for c in (p[1], q[1])}
            rows = {p[0], q[0]}
            cols = {p[1], q[1]}
            if third in sq:
                pred = 4
            elif third[0] in rows or third[1] in cols:
                pred = 6                  # extra row or column next to it
            else:
                pred = 9                  # diagonally beyond it
        elif (dr, dc) in ((0, 2), (2, 0)):   # opposite across the new cell
            mid = ((p[0] + q[0]) // 2, (p[1] + q[1]) // 2)
            if mid in s:
                continue                  # not a supporting pair
            if dr == 0:
                line, k = p[0], third[0]
            else:
                line, k = p[1], third[1]
            if abs(k - line) == 1:
                pred = 6
            elif abs(k - line) == 2:
                pred = 9
            else:                         # third seed on the line itself
                bad.append((s, 'third seed on the line', f))
                continue
        else:
            continue
        uses += 1
        if pred != f:
            bad.append((s, (p, q), pred, f))
check(not bad, f'every supporting pair of every start gets the right finish '
      f'from the classification ({uses} pair cases, mismatches {bad[:3]})')
lines = [s for s in itertools.combinations(cells(3, 3), 3)
         if len({x[0] for x in s}) == 1 or len({x[1] for x in s}) == 1]
check(len(lines) == 6 and all(not legal(set(s), 3, 3) for s in lines),
      '"A third seed on that line gives 3": the only such starts are the 6 '
      'full rows/columns, which have no legal addition at all, so this '
      'sub-case of "two seeds support a first addition" is vacuous')
say()

# ---------------------------------------------- 4. fewest seeds n-by-n
say('== 4. Fewest seeds (2-3 P2; 4-5 P2, P3, P5) ==')
for n, k in ((3, 2), (4, 3), (5, 4)):
    cnt = sum(fills(s, n, n) for s in itertools.combinations(cells(n, n), k))
    check(cnt == 0, f'{n}x{n}: none of the C({n * n},{k}) = '
          f'{math.comb(n * n, k)} starts with {k} seeds fills')
for n in range(1, 13):
    d = [(i, i) for i in range(n)]
    ad = [(i, n - 1 - i) for i in range(n)]
    if not (fills(d, n, n) and fills(ad, n, n)):
        FAILS.append(f'diagonal fails n={n}')
check(not [f for f in FAILS if f.startswith('diagonal')],
      'main and opposite diagonals fill n x n for n = 1..12 (incl. 5, 10)')
fill4 = [s for s in itertools.combinations(cells(4, 4), 4) if fills(s, 4, 4)]
reps = orbits(fill4, 4)
say(f'4x4: {len(fill4)} four-seed filling starts, {len(reps)} up to '
    f'symmetry')
check(len(fill4) >= 3, 'P2: three different four-seed starts exist')
gs = g((1, 1), (1, 3), (2, 4), (4, 1))
check(fills(gs, 4, 4), 'guide P2: {(1,1),(1,3),(2,4),(4,1)} fills 4x4')
check(fills([(i, i) for i in range(4)], 4, 4) and
      fills([(i, 3 - i) for i in range(4)], 4, 4),
      'guide P2: main diagonal and antidiagonal fill 4x4')
say('  a 5x5 minimum count, for reference: ' + str(sum(
    fills(s, 5, 5) for s in itertools.combinations(cells(5, 5), 5))) +
    ' five-seed filling starts')
say()

# ------------------------------------------------- 5. perimeter
say('== 5. Exposed sides (4-5 P4, P5; guide overview) ==')
for (a, b) in ((3, 3), (4, 4), (3, 4)):
    worst = -99
    for m in range(1 << (a * b)):
        f = {x for i, x in enumerate(cells(a, b)) if m >> i & 1}
        p0 = perimeter(f, a, b)
        for x in legal(f, a, b):
            k = sum((y in f) for y in nbrs(*x, a, b))
            d = perimeter(f | {x}, a, b) - p0
            if d != 4 - 2 * k:
                FAILS.append(f'perimeter change {a}x{b}')
            worst = max(worst, d)
    check(worst == 0, f'{a}x{b}: every legal addition in every state changes '
          f'the count by 4-2k; largest change {worst}')
pics = [([(0, 1), (1, 0)], (1, 1), (8, 8)),
        ([(0, 1), (1, 0), (1, 2)], (1, 1), (12, 10)),
        ([(0, 1), (1, 0), (1, 2), (2, 1)], (1, 1), (16, 12))]
for i, (f, x, want) in enumerate(pics, 1):
    f = set(f)
    k = sum((y in f) for y in nbrs(*x, 3, 3))
    got = (perimeter(f, 3, 3), perimeter(f | {x}, 3, 3))
    check(x in legal(f, 3, 3) and got == want,
          f'P4 picture {i}: circled centre is legal (k={k}); before/after '
          f'{got[0]} -> {got[1]} (guide {want[0]} -> {want[1]})')
for n in (4, 5, 10):
    check(perimeter(set(cells(n, n)), n, n) == 4 * n,
          f'full {n}x{n} board has {4 * n} exposed sides')
check(perimeter({(1, 1)}, 3, 3) == 4 and
      perimeter(set(cells(3, 3)) - {(1, 1)}, 3, 3) - 4 ==
      perimeter(set(cells(3, 3)), 3, 3),
      'guide: filling an isolated one-cell hole removes four exposed sides')
say()

# ------------------------------------- 6. the printed four-seed start
say('== 6. Printed four-seed start (2-3 P5, 4-5 P6) ==')
four = g((1, 1), (1, 2), (2, 3), (3, 3))
check(fills(four, 3, 3), 'the printed start fills the 3x3 board')
layers = [g((1, 3), (2, 2)), g((2, 1), (3, 2)), g((3, 1))]
f = set(four)
ok = True
for L in layers:
    for x in L:                       # either order within a layer
        ok &= x in legal(f, 3, 3)
    f |= set(L)
check(ok and len(f) == 9, "guide's growth layers (1,3),(2,2) / (2,1),(3,2) / "
      "(3,1) are each legal in either order and fill the board")
printed_omits = [g((1, 1)), g((1, 2)), g((2, 3)), g((3, 3))]  # page order
counts = []
for om in printed_omits:
    s = [x for x in four if x not in om]
    counts.append(len(closure(s, 3, 3)))
check(counts == [6, 3, 3, 6], f'deletion finishes in printed order: '
      f'{counts} (guide 6,3,3,6)')
check(fills(diag3, 3, 3), 'four is not the fewest: the 3-seed diagonal fills')


def incl_min(s, a, b):
    return fills(s, a, b) and all(
        not fills([y for y in s if y != x], a, b) for x in s)


im = {k: [s for s in itertools.combinations(cells(3, 3), k)
          if incl_min(s, 3, 3)] for k in range(1, 10)}
say('inclusion-minimal filling starts on 3x3 by size: ' +
    ', '.join(f'{k}: {len(v)}' for k, v in im.items() if v))
check(len(im[4]) == 9, f'guide: 9 inclusion-minimal four-seed starts '
      f'({len(im[4])})')
for rep, size in orbits(im[4], 3):
    say(f'  orbit of {[(r + 1, c + 1) for r, c in rep]}: {size} placements')
qt = g((1, 3), (2, 3), (3, 1), (3, 2))
check(tuple(sorted(qt)) in {tuple(sorted(s)) for s in im[4]},
      "guide: quarter-turn {(1,3),(2,3),(3,1),(3,2)} is inclusion-minimal")
check(sorted(qt) == sorted(sym8(3)[1](*x) for x in four),
      'and it is the quarter-turn of the printed start')
check(len(im[4]) - 1 >= 1, 'P6: a different indispensable four-seed start '
      'exists (8 others)')
check(max(k for k in im if im[k]) == 4,
      'no inclusion-minimal filling start on 3x3 has more than 4 seeds')
say()

# ------------------------------------------ 7. rectangles (later question)
say('== 7. Later question: a x b rectangles (guide p. 5) ==')
for a in range(1, 5):
    for b in range(a, 6):
        lb = math.ceil((a + b) / 2)
        m = next(k for k in range(1, a * b + 1) if any(
            fills(s, a, b) for s in itertools.combinations(cells(a, b), k)))
        if m < lb:
            FAILS.append(f'rect bound {a}x{b}')
        say(f'  {a}x{b}: minimum {m}, perimeter bound ceil((a+b)/2) = {lb}')
check(not [f for f in FAILS if f.startswith('rect')],
      'the stated bound s >= ceil((a+b)/2) holds on every rectangle tested')
say()

say(f'FAILURES: {len(FAILS)}')
for f in FAILS:
    say('  ' + f)
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
