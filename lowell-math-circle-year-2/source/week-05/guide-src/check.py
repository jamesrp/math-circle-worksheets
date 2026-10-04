"""Independent check of every answer printed in the Week 5 adult guide.

The positions, cards and clue numbers below were read off the rendered
student PDFs (final/k-1.pdf, final/grades-2-3.pdf, final/grades-4-5.pdf),
not taken from the student build scripts. Everything is recomputed here by
brute force: all orders of the towers and all Latin squares of order 3 and 4.

Run:  python3 check.py        (prints a report; exits non-zero if a printed
                               claim in CLAIMS does not match the computation)
It also writes answers.tex, the solution grids that the guide prints.
"""
import os
import sys
from collections import Counter
from itertools import combinations, permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))


# ------------------------------------------------------------ basic objects
def seen(row):
    """Number of towers seen looking along `row` from its first entry."""
    best, k = 0, 0
    for h in row:
        if h > best:
            best, k = h, k + 1
    return k


def lr(row):
    return (seen(row), seen(row[::-1]))


def orders(n):
    return list(permutations(range(1, n + 1)))


def rows_for(n, pair):
    return [p for p in orders(n) if lr(p) == pair]


def s(row):
    return "".join(map(str, row))


def latin_squares(n):
    rows = orders(n)
    out = []

    def go(sq):
        if len(sq) == n:
            out.append(tuple(sq))
            return
        for r in rows:
            if all(r[c] != q[c] for q in sq for c in range(n)):
                go(sq + [r])

    go([])
    return out


def clues(sq):
    """All 4n clue numbers of a city. Keys: ('T',c) above column c looking down,
    ('B',c) below column c looking up, ('L',r) left of row r, ('R',r) right of row r.
    Rows are counted from the top, columns from the left, both from 0."""
    n = len(sq)
    d = {}
    for c in range(n):
        col = [sq[r][c] for r in range(n)]
        d[('T', c)] = seen(col)
        d[('B', c)] = seen(col[::-1])
    for r in range(n):
        d[('L', r)] = seen(sq[r])
        d[('R', r)] = seen(sq[r][::-1])
    return d


LS = {3: latin_squares(3), 4: latin_squares(4)}
CL = {n: [(sq, clues(sq)) for sq in LS[n]] for n in (3, 4)}


def solve(n, puzzle):
    return [sq for sq, cl in CL[n] if all(cl[k] == v for k, v in puzzle.items())]


def city(sq):
    return "/".join(s(r) for r in sq)


def P(**kw):
    """Puzzle from side lists, e.g. P(T=[0,1,3]) ; 0 means no number there."""
    d = {}
    for side, vals in kw.items():
        for i, v in enumerate(vals):
            if v:
                d[(side, i)] = v
    return d


# ------------------------------------------------------------ the pages
# K-1 (F05-K-v4)
K_EYE = (1, 3, 2)                         # page 1 picture, eye at the left
K_P1 = [(1, 3, 2), (3, 2, 1)]             # page 1, left and right picture
K_P3 = [(1, 3), (2, 1), (3, 3), (2, 2), (1, 1), (1, 2)]   # page 3, reading order
K_P4_HIDDEN = (2, 3, 1)                   # page 4 folder picture
K_P7 = [(2, 3), (1, 4), (3, 3), (3, 1), (4, 2), (1, 2)]   # page 7, reading order
# Grades 2-3 (F05-M-v4), page 3 and 4: Problem 3, four grids top to bottom
M_P3 = [P(T=[0, 1, 3], L=[2, 0, 0], R=[0, 2, 1]),
        P(L=[2, 1, 0], R=[0, 0, 2]),
        P(T=[2, 2, 2]),
        P(R=[0, 0, 2], B=[0, 2, 0])]
M_P4 = P(T=[1, 0, 0], L=[0, 0, 2])        # page 5
# Grades 4-5 (F05-U-v4)
U_P1 = [(1, 2), (2, 3), (3, 3), (2, 2), (1, 4), (1, 1), (3, 2), (4, 2)]  # page 1
U_P3 = [  # pages 3-4, reading order: A B / C D (page 3), E F (page 4)
    P(T=[4, 0, 1, 3], L=[3, 2, 2, 1], R=[0, 0, 1, 3], B=[0, 2, 2, 2]),
    P(T=[2, 0, 0, 0], L=[3, 1, 0, 0], R=[2, 3, 0, 1], B=[3, 0, 4, 0]),
    P(T=[3, 2, 0, 0], L=[2, 0, 0, 0], R=[0, 2, 0, 1], B=[0, 3, 0, 0]),
    P(T=[0, 0, 4, 0], L=[2, 1, 0, 0], R=[0, 2, 3, 0], B=[2, 0, 0, 0]),
    P(T=[0, 3, 0, 2], L=[0, 0, 2, 0], B=[2, 0, 2, 0]),
    P(T=[2, 0, 2, 0], L=[0, 2, 0, 0], R=[0, 0, 0, 2]),
]
U_P4 = P(T=[4, 0, 0, 0], L=[4, 0, 0, 0])  # page 5

SIDE_WORD = {'T': 'above column', 'B': 'below column', 'L': 'left of row', 'R': 'right of row'}


def where(key):
    side, k = key
    return f"{SIDE_WORD[side]} {k + 1}"


def single_additions(n, puzzle):
    out = []
    for side in 'TBLR':
        for k in range(n):
            key = (side, k)
            if key in puzzle:
                continue
            for v in range(1, n + 1):
                t = dict(puzzle)
                t[key] = v
                if len(solve(n, t)) == 1:
                    out.append((key, v))
    return out


def unique_with(n, k, forbid=None):
    """All k-number clue sets (with the values of some city) that fit exactly one city."""
    keys = [(sd, i) for sd in 'TBLR' for i in range(n)]
    found = []
    for sub in combinations(keys, k):
        groups = Counter(tuple(cl[x] for x in sub) for sq, cl in CL[n])
        for vals, cnt in groups.items():
            if cnt == 1 and not (forbid and forbid in vals):
                found.append(dict(zip(sub, vals)))
    return found


def stirling1(n, k):
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0:
        return 0
    return stirling1(n - 1, k - 1) + (n - 1) * stirling1(n - 1, k)


# ------------------------------------------------------------ compute
R = {}
R['K eye'] = seen(K_EYE)
R['K P1'] = [lr(r) for r in K_P1]
R['orders3'] = {s(p): lr(p) for p in orders(3)}
R['K P3'] = {c: [s(p) for p in rows_for(3, c)] for c in K_P3}
R['K P4 hidden'] = lr(K_P4_HIDDEN)
R['pairs3'] = sorted(set(R['orders3'].values()))
R['K P5'] = [s(p) for p in orders(4) if lr(p)[0] == 1]
R['K P6'] = [s(p) for p in rows_for(4, (2, 2))]
R['K P7'] = {c: [s(p) for p in rows_for(4, c)] for c in K_P7}
R['M P1 never'] = sorted(set(product(range(1, 4), repeat=2)) - set(R['pairs3']))
R['n3'] = len(LS[3])
R['n4'] = len(LS[4])
R['cubes3'] = sorted({sum(map(sum, sq)) for sq in LS[3]})
R['cubes4'] = sorted({sum(map(sum, sq)) for sq in LS[4]})
R['M P3'] = [[city(x) for x in solve(3, pz)] for pz in M_P3]
R['M P4'] = [city(x) for x in solve(3, M_P4)]
R['M P4 add'] = single_additions(3, M_P4)
R['M P5 one-number'] = {f"{k}={v}": len(solve(3, {k: v})) for k in [(sd, i) for sd in 'TBLR' for i in range(3)] for v in (1, 2, 3)}
R['M P5 min one-number cities'] = min(c for c in R['M P5 one-number'].values() if c > 0)
R['M P5 two-number unique'] = len(unique_with(3, 2))
R['M P7 totals'] = sorted({sum(cl.values()) for sq, cl in CL[3]})
R['M P6 first row extensions'] = sorted(Counter(sq[0] for sq in LS[3]).values())
R['U P1'] = {c: [s(p) for p in rows_for(4, c)] for c in U_P1}
R['U P3'] = [[city(x) for x in solve(4, pz)] for pz in U_P3]
R['U P3 clue counts'] = [len(pz) for pz in U_P3]
R['U P4'] = [city(x) for x in solve(4, U_P4)]
R['U P4 add'] = single_additions(4, U_P4)
R['U P5 two-number unique'] = len(unique_with(4, 2))
U3 = unique_with(4, 3)
R['U P5 three-number unique'] = len(U3)
U6 = [d for d in U3 if 4 not in d.values()]
R['U P6 count'] = len(U6)
R['U P6 all threes'] = len([d for d in U6 if set(d.values()) == {3}])
R['U P7'] = dict(sorted(Counter(lr(p) for p in orders(4)).items()))
R['U P8'] = dict(sorted(Counter(seen(p) for p in orders(5)).items()))
groups = {}
for sq, cl in CL[4]:
    groups.setdefault(tuple(sorted(cl.items())), []).append(sq)
shared = [g for g in groups.values() if len(g) > 1]
R['U P9 shared sets'] = len(shared)
R['U P9 cities in shared'] = sum(len(g) for g in shared)
R['U P9 max share'] = max(len(g) for g in shared)
g3 = Counter(tuple(sorted(cl.items())) for sq, cl in CL[3])
R['3x3 clue sets all different'] = max(g3.values()) == 1
R['stirling'] = {n: [stirling1(n, k) for k in range(1, n + 1)] for n in (3, 4, 5)}
R['stirling brute'] = {n: [sum(1 for p in orders(n) if seen(p) == k) for k in range(1, n + 1)] for n in (3, 4, 5)}
# joint distribution formula: #(L=a,R=b) = c(n-1, a+b-2) * C(a+b-2, a-1)
from math import comb
R['joint formula ok'] = all(
    Counter(lr(p) for p in orders(n)).get((a, b), 0) == stirling1(n - 1, a + b - 2) * comb(a + b - 2, a - 1)
    for n in (3, 4, 5, 6) for a in range(1, n + 1) for b in range(1, n + 1))
R['reduced 4x4'] = len([sq for sq in LS[4] if sq[0] == (1, 2, 3, 4) and [r[0] for r in sq] == [1, 2, 3, 4]])

# ------------------------------------------------------------ claims printed in the guide
SAMPLE3 = ((1, 2, 3), (2, 3, 1), (3, 1, 2))
PAIR9 = (((1, 2, 3, 4), (2, 1, 4, 3), (3, 4, 1, 2), (4, 3, 2, 1)),
         ((1, 2, 3, 4), (2, 4, 1, 3), (3, 1, 4, 2), (4, 3, 2, 1)))
U6_EXAMPLE = {('T', 0): 3, ('T', 2): 3, ('L', 3): 3}
U6_EXAMPLE2 = {('B', 2): 3, ('L', 0): 3, ('L', 3): 3}

CLAIMS = {
    'K eye': 2,
    'K P1': [(2, 2), (1, 3)],
    'orders3': {'123': (3, 1), '132': (2, 2), '213': (2, 1), '231': (2, 2), '312': (1, 2), '321': (1, 3)},
    'K P3': {(1, 3): ['321'], (2, 1): ['213'], (3, 3): [], (2, 2): ['132', '231'], (1, 1): [], (1, 2): ['312']},
    'K P4 hidden': (2, 2),
    'pairs3': [(1, 2), (1, 3), (2, 1), (2, 2), (3, 1)],
    'K P5': ['4123', '4132', '4213', '4231', '4312', '4321'],
    'K P6': ['1423', '2143', '2413', '3142', '3241', '3412'],
    'K P7': {(2, 3): ['1432', '2431', '3421'], (1, 4): ['4321'], (3, 3): [],
             (3, 1): ['1324', '2134', '2314'], (4, 2): [], (1, 2): ['4123', '4213']},
    'M P1 never': [(1, 1), (2, 3), (3, 2), (3, 3)],
    'n3': 12, 'n4': 576, 'cubes3': [18], 'cubes4': [40],
    'M P3': [['231/312/123'], ['213/321/132'], [], ['123/231/312']],
    'M P4': ['312/123/231', '321/132/213', '321/213/132'],
    'M P5 min one-number cities': 2,
    'M P5 two-number unique': 156,
    'M P7 totals': [22],
    'M P6 first row extensions': [2, 2, 2, 2, 2, 2],
    'U P1': {(1, 2): ['4123', '4213'], (2, 3): ['1432', '2431', '3421'], (3, 3): [],
             (2, 2): ['1423', '2143', '2413', '3142', '3241', '3412'], (1, 4): ['4321'], (1, 1): [],
             (3, 2): ['1243', '1342', '2341'], (4, 2): []},
    'U P3': [['1342/2413/3124/4231'], ['1243/4132/3421/2314'], ['2143/3412/4321/1234'],
             ['3214/4123/1432/2341'], ['4231/1324/2143/3412'], ['2134/1423/4312/3241']],
    'U P3 clue counts': [12, 8, 6, 6, 5, 4],
    'U P4': ['1234/2143/3412/4321', '1234/2143/3421/4312', '1234/2341/3412/4123', '1234/2413/3142/4321'],
    'U P5 two-number unique': 0,
    'U P6 count': 40, 'U P6 all threes': 16,
    'U P7': {(1, 2): 2, (1, 3): 3, (1, 4): 1, (2, 1): 2, (2, 2): 6, (2, 3): 3, (3, 1): 3, (3, 2): 3, (4, 1): 1},
    'U P8': {1: 24, 2: 50, 3: 35, 4: 10, 5: 1},
    'U P9 shared sets': 66, 'U P9 cities in shared': 204, 'U P9 max share': 6,
    '3x3 clue sets all different': True,
    'stirling': {3: [2, 3, 1], 4: [6, 11, 6, 1], 5: [24, 50, 35, 10, 1]},
    'joint formula ok': True,
    'reduced 4x4': 4,
}
ADD_M_P4 = {(('T', 1), 3), (('T', 2), 3), (('B', 0), 3), (('B', 1), 2), (('B', 2), 1),
            (('L', 1), 3), (('R', 0), 2), (('R', 1), 2), (('R', 2), 1)}
ADD_U_P4 = {(('T', 1), 3), (('B', 2), 3), (('B', 3), 2), (('B', 3), 3), (('L', 1), 3),
            (('R', 2), 3), (('R', 3), 2), (('R', 3), 3)}

bad = []
for k, v in CLAIMS.items():
    if R[k] != v:
        bad.append(f"MISMATCH {k}: guide says {v}, computed {R[k]}")
if set(R['M P4 add']) != ADD_M_P4:
    bad.append(f"MISMATCH M P4 add: computed {R['M P4 add']}")
if set(R['U P4 add']) != ADD_U_P4:
    bad.append(f"MISMATCH U P4 add: computed {R['U P4 add']}")
# 2-3 P5: one number never enough; the swap argument (swap the two other lines)
for key in [(sd, i) for sd in 'TBLR' for i in range(3)]:
    for v in (1, 2, 3):
        if 0 < len(solve(3, {key: v})) < 2:
            bad.append(f"one-number puzzle {key}={v} has a unique city")
# sample city used in the guide (2-3 P2) and its twelve numbers
cl = clues(SAMPLE3)
if [cl[('T', c)] for c in range(3)] != [3, 2, 1] or [cl[('B', c)] for c in range(3)] != [1, 2, 2] \
        or [cl[('L', r)] for r in range(3)] != [3, 2, 1] or [cl[('R', r)] for r in range(3)] != [1, 2, 2]:
    bad.append(f"sample 3x3 clues wrong: {cl}")
# 4-5 P6 examples printed in the guide
for ex in (U6_EXAMPLE, U6_EXAMPLE2):
    if len(solve(4, ex)) != 1 or 4 in ex.values():
        bad.append(f"P6 example fails: {ex}")
R['U P6 example city'] = city(solve(4, U6_EXAMPLE)[0])
R['U P6 example2 city'] = city(solve(4, U6_EXAMPLE2)[0])
# 4-5 P9 pair printed in the guide
a, b = PAIR9
if a == b or clues(a) != clues(b) or a not in LS[4] or b not in LS[4]:
    bad.append("P9 pair fails")
R['U P9 pair clues'] = clues(a)
R['U P9 pair differ in cells'] = sum(a[r][c] != b[r][c] for r in range(4) for c in range(4))
# P8 count by first tower (guide's explanation): first tower h, then 5 before every other taller tower
byfirst = Counter(p[0] for p in orders(5) if seen(p) == 2)
R['U P8 exactly-2 by first tower'] = dict(sorted(byfirst.items()))
if R['U P8 exactly-2 by first tower'] != {1: 6, 2: 8, 3: 12, 4: 24}:
    bad.append(f"P8 by-first-tower split wrong: {byfirst}")
# 3x3 sum argument: a row's two numbers add to 3 if its 1 is in the middle, else 4
if any(sum(lr(p)) != (3 if p[1] == 1 else 4) for p in orders(3)):
    bad.append("3x3 row sum rule fails")
# L + R <= n + 1
if any(sum(lr(p)) > len(p) + 1 for n in (3, 4, 5, 6) for p in orders(n)):
    bad.append("L+R <= n+1 fails")

# 2-3 P5 two-number example printed in the guide: 3 left of row 1, 3 above column 1
if [city(x) for x in solve(3, {('L', 0): 3, ('T', 0): 3})] != ['123/231/312']:
    bad.append("2-3 P5 two-number example fails")
# 2-3 P4 and 4-5 P4: which city each added number leaves (as printed in the guide)
M4_CITY = {'312/123/231': {(('T', 1), 3), (('L', 1), 3), (('R', 0), 2)},
           '321/132/213': {(('T', 2), 3), (('B', 1), 2), (('B', 2), 1), (('R', 1), 2), (('R', 2), 1)},
           '321/213/132': {(('B', 0), 3)}}
U4_CITY = {'1234/2341/3412/4123': {(('T', 1), 3), (('L', 1), 3), (('B', 3), 2), (('R', 3), 2)},
           '1234/2143/3421/4312': {(('B', 2), 3), (('B', 3), 3), (('R', 2), 3), (('R', 3), 3)}}
for n, base, table in ((3, M_P4, M4_CITY), (4, U_P4, U4_CITY)):
    for c, adds in table.items():
        for k, v in adds:
            t = dict(base)
            t[k] = v
            if [city(x) for x in solve(n, t)] != [c]:
                bad.append(f"added number {k}={v} does not leave {c}")
# 4-5 P4: the two cities that cannot be singled out share all sixteen numbers
if clues(tuple(tuple(int(ch) for ch in r) for r in '1234/2143/3412/4321'.split('/'))) != \
        clues(tuple(tuple(int(ch) for ch in r) for r in '1234/2413/3142/4321'.split('/'))):
    bad.append("4-5 P4: A and D do not share their numbers")
# 2-3 P3 puzzle 4 hint: only a 1 can stand at the bottom of the middle column
if sorted({x[2][1] for x in LS[3] if seen([x[2][2], x[2][1], x[2][0]]) == 2
           and seen([x[2][1], x[1][1], x[0][1]]) == 2}) != [1]:
    bad.append("2-3 P3 puzzle 4 hint fails")
# 4-5 P3 puzzle C hint: a column seen 2 from the top and 3 from the bottom has its 4 second
if {p[1] for p in rows_for(4, (2, 3))} != {4}:
    bad.append("4-5 P3 C hint fails")
# K-1 P6 grouping: the 4 is second in 1423 2413 3412 and third in 2143 3142 3241
if sorted(s(p) for p in rows_for(4, (2, 2)) if p[1] == 4) != ['1423', '2413', '3412'] or \
        sorted(s(p) for p in rows_for(4, (2, 2)) if p[2] == 4) != ['2143', '3142', '3241']:
    bad.append("K-1 P6 grouping fails")
# 4-5 P7 row totals 6, 11, 6, 1 and symmetry
t7 = Counter(lr(p) for p in orders(4))
if [sum(v for (a, b), v in t7.items() if a == k) for k in (1, 2, 3, 4)] != [6, 11, 6, 1] or \
        any(t7[(a, b)] != t7[(b, a)] for a in range(1, 5) for b in range(1, 5)):
    bad.append("4-5 P7 totals or symmetry fail")
# 4-5 P8 insertion count: 6 + 4*11 = 50
if 6 + 4 * 11 != R['U P8'][2]:
    bad.append("4-5 P8 insertion count fails")


# 4-5 P3: passes of line-by-line deduction (one pass = look at every row and column once)
def passes(n, pz):
    cand = {(r, c): set(range(1, n + 1)) for r in range(n) for c in range(n)}
    lines_ = [([(r, c) for c in range(n)], ('L', r), ('R', r)) for r in range(n)] + \
             [([(r, c) for r in range(n)], ('T', c), ('B', c)) for c in range(n)]
    k = 0
    while not all(len(v) == 1 for v in cand.values()):
        k += 1
        changed = False
        for cells, a, b in lines_:
            ok = [p for p in orders(n) if all(p[i] in cand[cells[i]] for i in range(n))
                  and (a not in pz or seen(p) == pz[a]) and (b not in pz or seen(p[::-1]) == pz[b])]
            for i, cell in enumerate(cells):
                u = {p[i] for p in ok}
                if u != cand[cell]:
                    cand[cell] = u
                    changed = True
        if not changed:
            return None
    return k


R['U P3 passes'] = [passes(4, pz) for pz in U_P3]
if R['U P3 passes'] != [2, 2, 2, 3, 5, 7]:
    bad.append(f"ladder passes differ: {R['U P3 passes']}")

# launch demonstration: row 2 1 3, then rearranged to 1 2 3
if lr((2, 1, 3)) != (2, 1) or lr((1, 2, 3)) != (3, 1):
    bad.append("launch row views wrong")
# 4-5 ladder hints: next to a 3 the 4 is in square 3 or 4; next to a 2 it is not in square 1
if {p.index(4) + 1 for p in orders(4) if seen(p) == 3} != {3, 4} or \
        {p.index(4) + 1 for p in orders(4) if seen(p) == 2} != {2, 3, 4}:
    bad.append("ladder 4-position hints fail")
# 2-3 P6: the second row is the top row shifted one place (left or right, wrapping round)
for sq in LS[3]:
    a, b = sq[0], sq[1]
    if b not in (a[1:] + a[:1], a[-1:] + a[:-1]):
        bad.append(f"second row is not a shift: {sq}")
# 2-3 P5: swapping the two lines a single number does not look along keeps the number
for sq, cl in CL[3]:
    for c in range(3):
        o = [x for x in range(3) if x != c]
        sw = tuple(tuple(r[o[1]] if x == o[0] else r[o[0]] if x == o[1] else r[x] for x in range(3)) for r in sq)
        cs = clues(sw)
        if sw == sq or cs[('T', c)] != cl[('T', c)] or cs[('B', c)] != cl[('B', c)]:
            bad.append("column swap argument fails")
# 2-3 P3 puzzle 3: the column under the top row's 3 always shows 1 from the top
if any(seen([sq[r][sq[0].index(3)] for r in range(3)]) != 1 for sq in LS[3]):
    bad.append("2-3 P3 puzzle 3 argument fails")


# Physical check: eye at table level, a foot from the end of the row. Side view, inches.
# Cubes 0.75 in; towers spaced `pitch` apart (0.75 = touching, 1.0 = on the 1-inch grid).
def eye_count(row, d, e, pitch, w=0.75):
    """Towers whose front-top corner the eye at (0, e) can see; front of first tower at x = d."""
    k = 0
    for j, hj in enumerate(row):
        xj, Hj = d + j * pitch, hj * w
        ok = True
        for i in range(j):
            xi, Hi = d + i * pitch, row[i] * w
            for x in (xi, xi + w):          # front and back top edges of the nearer tower
                if e + (Hj - e) * x / xj <= Hi + 1e-9:
                    ok = False
        k += ok
    return k


def eye_ok(n, d, e, pitch):
    return all(eye_count(p, d, e, pitch) == seen(p) for p in orders(n))


R['eye ok at 12 in'] = all(eye_ok(n, 12, e / 4, pitch) for n in (3, 4) for e in range(0, 13)
                           for pitch in (0.75, 1.0))
R['3124 min distance at table level, 1-inch grid'] = min(
    d / 4 for d in range(1, 200) if eye_count((3, 1, 2, 4), d / 4, 0, 1.0) == 2)
R['rows of four wrong at 4 in, table level, 1-inch grid'] = sum(
    eye_count(p, 4, 0, 1.0) != seen(p) for p in orders(4))
if not R['eye ok at 12 in'] or not 8.5 <= R['3124 min distance at table level, 1-inch grid'] <= 9.5:
    bad.append(f"eye-distance claim fails: {R['eye ok at 12 in']}, "
               f"{R['3124 min distance at table level, 1-inch grid']}")

# 4-5 P5 count and P6 second example city, as printed
if R['U P5 three-number unique'] != 1600:
    bad.append("three-number unique count is not 1600")
if R['U P6 example2 city'] != '1243/3421/4132/2314':
    bad.append("P6 second example city differs")
# Materials table: towers per child, cubes per child, totals with spares
kits = {'K-1': (4, {1: 1, 2: 1, 3: 1}, 6), '2-3': (4, {1: 3, 2: 3, 3: 3}, 10),
        '4-5': (3, {1: 4, 2: 4, 3: 4, 4: 4}, 10)}
table = {k: (sum(h * c for h, c in kit.items()), kids * sum(kit.values()),
             kids * sum(h * c for h, c in kit.items()), spare,
             kids * sum(h * c for h, c in kit.items()) + spare) for k, (kids, kit, spare) in kits.items()}
PRINTED = {'K-1': (6, 12, 24, 6, 30), '2-3': (18, 36, 72, 10, 82), '4-5': (40, 48, 120, 10, 130)}
if table != PRINTED or sum(v[1] for v in table.values()) != 96 or sum(v[2] for v in table.values()) != 216 \
        or sum(v[3] for v in table.values()) != 26 or sum(v[4] for v in table.values()) != 242:
    bad.append(f"materials table wrong: {table}")
# per-child cubes match the student pages: 18 for a 3-by-3 city, 40 for a 4-by-4 city,
# and a K-1 pair's 12 cubes cover towers 1-4 (10 cubes)
if table['2-3'][0] != R['cubes3'][0] or table['4-5'][0] != R['cubes4'][0] or 2 * table['K-1'][0] < 10:
    bad.append("per-child cubes do not match the pages")

# Mathematics section
from fractions import Fraction
dist = Counter()
for g in groups.values():
    for a_, b_ in combinations(g, 2):
        dist[sum(a_[r][c] != b_[r][c] for r in range(4) for c in range(4))] += 1
R['shared pairs'] = sum(dist.values())
R['shared pairs differing in a 2x2 block'] = dist[4]
R['L2'] = len(latin_squares(2))
R['L5'] = len(latin_squares(5))
R['rise-then-fall rows = 2^(n-1)'] = all(sum(1 for p in orders(n) if sum(lr(p)) == n + 1) == 2 ** (n - 1)
                                         for n in range(2, 7))
R['average seen = H_n'] = all(Fraction(sum(seen(p) for p in orders(n)), len(orders(n)))
                              == sum(Fraction(1, j) for j in range(1, n + 1)) for n in range(1, 7))
for k, v in {'shared pairs': 262, 'shared pairs differing in a 2x2 block': 152, 'L2': 2, 'L5': 161280,
             'rise-then-fall rows = 2^(n-1)': True, 'average seen = H_n': True}.items():
    if R[k] != v:
        bad.append(f"MISMATCH {k}: guide says {v}, computed {R[k]}")

# ------------------------------------------------------------ report
lines = []
for k, v in R.items():
    lines.append(f"{k}: {v}")
lines.append("M P4 add (readable): " + ", ".join(f"{v} {where(k)}" for k, v in R['M P4 add']))
lines.append("U P4 add (readable): " + ", ".join(f"{v} {where(k)}" for k, v in R['U P4 add']))
lines.append("U P6 examples (first 12): " + "; ".join(
    ", ".join(f"{v} {where(k)}" for k, v in sorted(d.items())) for d in U6[:12]))
report = "\n".join(lines)
with open(os.path.join(HERE, "check-report.txt"), "w") as f:
    f.write(report + "\n")
    f.write("\n".join(bad) + ("\nALL PRINTED CLAIMS CHECKED\n" if not bad else "\n"))
print(report)


# ------------------------------------------------------------ TeX for the solution grids
def grid_tex(sq, pz=None):
    """A small solved grid with the puzzle's numbers around it (TikZ)."""
    n = len(sq)
    u = 0.42
    t = "\\begin{tikzpicture}[x=%.2fcm,y=%.2fcm]\n" % (u, u)
    for i in range(1, n):
        t += f"\\draw[line width=0.4pt] ({i},0) -- ({i},{n});\n"
        t += f"\\draw[line width=0.4pt] (0,{i}) -- ({n},{i});\n"
    t += f"\\draw[line width=1pt] (0,0) rectangle ({n},{n});\n"
    for r in range(n):
        for c in range(n):
            t += f"\\node at ({c + 0.5},{n - r - 0.5}) {{\\small {sq[r][c]}}};\n"
    for (side, k), v in (pz or {}).items():
        x, y = {'T': (k + 0.5, n + 0.45), 'B': (k + 0.5, -0.45),
                'L': (-0.45, n - k - 0.5), 'R': (n + 0.45, n - k - 0.5)}[side]
        t += f"\\node[text=black!55] at ({x},{y}) {{\\footnotesize {v}}};\n"
    if not pz:
        t += f"\\path (-0.45,-0.45) rectangle ({n + 0.45},{n + 0.45});\n"
    else:
        t += f"\\path (-1,-1) rectangle ({n + 1},{n + 1});\n"
    t += "\\end{tikzpicture}"
    return t


def sq_of(text):
    return tuple(tuple(int(ch) for ch in row) for row in text.split("/"))


tex = ["% generated by check.py from the computed solutions; do not edit"]
names = "abcdefghijklmnop"
for i, pz in enumerate(M_P3):
    sols = solve(3, pz)
    if sols:
        tex.append(f"\\newcommand{{\\MthreeSol{names[i]}}}{{{grid_tex(sols[0], pz)}}}")
for i, c in enumerate(solve(3, M_P4)):
    tex.append(f"\\newcommand{{\\MfourSol{names[i]}}}{{{grid_tex(c, M_P4)}}}")
for i, pz in enumerate(U_P3):
    tex.append(f"\\newcommand{{\\UthreeSol{names[i]}}}{{{grid_tex(solve(4, pz)[0], pz)}}}")
for i, c in enumerate(solve(4, U_P4)):
    tex.append(f"\\newcommand{{\\UfourSol{names[i]}}}{{{grid_tex(c, U_P4)}}}")
tex.append(f"\\newcommand{{\\Msample}}{{{grid_tex(SAMPLE3, clues(SAMPLE3))}}}")
tex.append(f"\\newcommand{{\\UsixSol}}{{{grid_tex(solve(4, U6_EXAMPLE)[0], U6_EXAMPLE)}}}")
tex.append(f"\\newcommand{{\\UnineA}}{{{grid_tex(PAIR9[0], clues(PAIR9[0]))}}}")
tex.append(f"\\newcommand{{\\UnineB}}{{{grid_tex(PAIR9[1], clues(PAIR9[1]))}}}")
# all twelve 3x3 cities, grouped by first row
twelve = sorted(LS[3])
tex.append("\\newcommand{\\Mtwelvea}{" + "\\hspace{0.25cm}".join(grid_tex(sq) for sq in twelve[:6]) + "}")
tex.append("\\newcommand{\\Mtwelveb}{" + "\\hspace{0.25cm}".join(grid_tex(sq) for sq in twelve[6:]) + "}")
with open(os.path.join(HERE, "answers.tex"), "w") as f:
    f.write("\n".join(tex) + "\n")

if bad:
    print("\n".join(bad))
    sys.exit(1)
print("ALL PRINTED CLAIMS CHECKED")
