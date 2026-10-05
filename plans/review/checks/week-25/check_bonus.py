"""Independent check of the Week 25 bonus companion (week-25-bonus.pdf) and its
adult guide (week-25-bonus-facilitator.pdf).

Reads grids, counters, dashed diagonals and their d-labels, candidate numbers
and the bold margin numbers from the student PDF, then solves every problem:
diagonal signatures, the adaptive and the prechosen cell-query minima, and the
four margin boards.  Output: check_bonus.out
"""
import os
import sys
from itertools import combinations, permutations, product

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, WEEK, margins, solutions, fmt  # noqa: E402

LOG = []


def out(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


def ok(cond, msg):
    out(('PASS ' if cond else 'FAIL ') + msg)
    return cond


doc = pymupdf.open(os.path.join(WEEK, 'week-25-bonus.pdf'))
PT_PER_MM = 72 / 25.4


def grids(page):
    drs = page.get_drawings()
    words = page.get_text('words')
    gs = []
    for d in drs:
        if d['type'] == 's' and len(d['items']) == 8 and all(it[0] == 'l' for it in d['items']):
            r = d['rect']
            gs.append({'rect': r, 'cell': (r.x1 - r.x0) / 3, 'cellh': (r.y1 - r.y0) / 3})
    gs.sort(key=lambda g: (round(g['rect'].y0 / 30), g['rect'].x0))
    for g in gs:
        r, c = g['rect'], g['cell']
        pic = [['0'] * 3 for _ in range(3)]
        for d in drs:
            if d['type'] == 'f' and d['items'] and all(it[0] == 'c' for it in d['items']):
                cx, cy = (d['rect'].x0 + d['rect'].x1) / 2, (d['rect'].y0 + d['rect'].y1) / 2
                if r.x0 < cx < r.x1 and r.y0 < cy < r.y1:
                    pic[int((cy - r.y0) // c)][int((cx - r.x0) // c)] = '1'
        g['picture'] = tuple(''.join(x) for x in pic)
        # dashed diagonals: which cells they cross, and the d-label at their lower end
        diags = {}
        for d in drs:
            if d['type'] == 's' and d.get('dashes') and len(d['items']) == 1 and d['items'][0][0] == 'l':
                p, q = d['items'][0][1], d['items'][0][2]
                if not (r.x0 - 1 < min(p.x, q.x) and max(p.x, q.x) < r.x1 + 1 and r.y0 - 1 < min(p.y, q.y) and max(p.y, q.y) < r.y1 + 1):
                    continue
                cells = set()
                for t in range(1, 200):
                    x = p.x + (q.x - p.x) * t / 200
                    y = p.y + (q.y - p.y) * t / 200
                    fx, fy = (x - r.x0) / c, (y - r.y0) / c
                    if min(fx % 1, 1 - fx % 1, fy % 1, 1 - fy % 1) > .08:   # well inside a cell
                        cells.add((int(fy), int(fx)))
                lo = p if p.y > q.y else q
                lab = min((w for w in words if w[4].startswith('d') and w[4][1:].isdigit()),
                          key=lambda w: (((w[0] + w[2]) / 2 - lo.x) ** 2 + ((w[1] + w[3]) / 2 - lo.y) ** 2))
                diags[lab[4]] = sorted(cells)
        g['diags'] = diags
        # bold margin numbers (P4) to the right of rows and below columns
        g['rows'] = [''.join(w[4] for w in words if r.x1 < w[0] < r.x1 + c and abs((w[1] + w[3]) / 2 - (r.y0 + (i + .5) * c)) < 6) for i in range(3)]
        g['cols'] = [''.join(w[4] for w in words if r.y1 < w[1] < r.y1 + .6 * c and abs((w[0] + w[2]) / 2 - (r.x0 + (j + .5) * c)) < 6) for j in range(3)]
        g['title'] = ''.join(w[4] for w in words if r.y0 - 30 < w[3] < r.y0 - 9 and r.x0 + c < (w[0] + w[2]) / 2 < r.x1 - c and w[4].isdigit() and len(w[4]) == 1 and (w[3] - w[1]) > 0)
    return gs, words


def name(cell):
    return 'ABC'[cell[0]] + str(cell[1] + 1)


# ---------------------------------------------------------------- page 1
out('== Bonus page 1: worked example and Problem 1')
g1, words = grids(doc[0])
ex = g1[0]
ok(ex['picture'] == ('110', '001', '100'), f'example picture {fmt(ex["picture"])} = A1,A2,B3,C1')
for k in sorted(ex['diags']):
    out(f'     {k}: ' + ','.join(name(c) for c in ex['diags'][k]))
expected_lines = {'d1': ['C1'], 'd2': ['B1', 'C2'], 'd3': ['A1', 'B2', 'C3'], 'd4': ['A2', 'B3'], 'd5': ['A3']}
ok({k: [name(c) for c in v] for k, v in ex['diags'].items()} == expected_lines,
   'dashed lines and labels: d1=C1, d2=B1,C2, d3=A1,B2,C3, d4=A2,B3, d5=A3 (column minus row = -2..2)')


def diag(p):
    return tuple(sum(p[i][j] == '1' for i in range(3) for j in range(3) if j - i == t) for t in range(-2, 3))


ok(diag(ex['picture']) == (1, 0, 1, 2, 0), f'example shadows {diag(ex["picture"])} match the printed table 1,0,1,2,0')
ok('Counters 1 0 1 2 0' in ' '.join(doc[0].get_text('text').split()), 'printed table reads 1 0 1 2 0')
for g in g1[1:]:
    ok({k: [name(c) for c in v] for k, v in g['diags'].items()} == expected_lines, 'P1 working grid carries the same d-lines')

PERMS = list(permutations(range(3)))     # row i -> column p[i]


def pic(p):
    return tuple(''.join('1' if p[i] == j else '0' for j in range(3)) for i in range(3))


cat = [pic(p) for p in PERMS]
sig = {c: diag(c) for c in cat}
for c in cat:
    out(f'     {fmt(c)}: d1..d5 = {sig[c]}')
coll = [(a, b) for a, b in combinations(cat, 2) if sig[a] == sig[b]]
ok(len(coll) == 1 and set(coll[0]) == {('100', '001', '010'), ('010', '100', '001')},
   f'exactly one colliding pair: {[(fmt(a), fmt(b)) for a, b in coll]} -> P1 answer "yes"')
# all pictures (any number of counters) with rows, cols and diagonals equal: how many classes collide
anyc = {}
for bits in product('01', repeat=9):
    p = (''.join(bits[0:3]), ''.join(bits[3:6]), ''.join(bits[6:9]))
    anyc.setdefault((margins(p), diag(p)), []).append(p)
out(f'     (aside) all 512 boards: {sum(1 for v in anyc.values() if len(v) > 1)} classes share rows, columns and diagonals')

# ---------------------------------------------------------------- page 2
out('\n== Bonus page 2: Problem 2 candidates and adaptive minimum')
g2, words2 = grids(doc[1])
labels = [str(n) for n in range(1, 7)]
cand = {}
for g, n in zip(g2, labels):
    cand[n] = g['picture']
    out(f'     candidate {n} ({g["cell"] / PT_PER_MM:.1f} mm cells): {fmt(g["picture"])}')
order = [pic(p) for p in PERMS]            # (1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)
ok([cand[n] for n in labels] == order, 'candidates 1-6 are columns (1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1) as the guide numbers them')
CELLS = [(i, j) for i in range(3) for j in range(3)]


def depth(cands):
    """Minimax number of paid cell questions to identify a member of cands."""
    if len(cands) <= 1:
        return 0
    best = 99
    for (i, j) in CELLS:
        yes = [c for c in cands if c[i][j] == '1']
        no = [c for c in cands if c[i][j] == '0']
        if not yes or not no:
            continue
        best = min(best, 1 + max(depth(yes), depth(no)))
    return best


ok(depth(order) == 3, f'adaptive worst-case minimum = {depth(order)} (two questions give at most 4 histories < 6)')
# the guide's strategy: A1; if occupied B2; else A2 then B1
strategy_ok = True
for c in order:
    if c[0][0] == '1':
        rest = [x for x in order if x[0][0] == '1' and x[1][1] == c[1][1]]
    else:
        rest = [x for x in order if x[0][0] == '0' and x[0][1] == c[0][1] and x[1][0] == c[1][0]]
    strategy_ok &= rest == [c]
ok(strategy_ok, 'guide strategy A1 -> (B2) / A2 -> B1 identifies every candidate in <= 3')

out('\n== Bonus page 3: Problem 3 prechosen questions')
sep = {}
for k in range(1, 6):
    sep[k] = [S for S in combinations(CELLS, k) if len({tuple(c[i][j] for (i, j) in S) for c in order}) == 6]
    out(f'     {k} cells: {len(sep[k])} separating sets of {len(list(combinations(CELLS, k)))}')
ok(not sep[3] and sep[4], 'prechosen minimum = 4')
ok(((0, 0), (0, 1), (1, 0), (1, 1)) in sep[4], 'guide set A1,A2,B1,B2 separates all six')
ok(all(sum(int(c[i][j]) for c in order) == 2 for (i, j) in CELLS),
   'each cell is occupied in exactly 2 of the 6 (so 3 cells give total weight 6 < 0+1+1+1+2+2 = 7: a short proof)')
# guide's case analysis for three cells
case_ok = True
for S in combinations(CELLS, 3):
    rows = sorted([sum(1 for (i, j) in S if i == r) for r in range(3)], reverse=True)
    resp = {}
    for c in order:
        resp.setdefault(tuple(c[i][j] for (i, j) in S), []).append(c)
    pairs = [v for v in resp.values() if len(v) > 1]
    if rows == [1, 1, 1] and len({j for _, j in S}) == 3:
        # transversal: the guide's collision is the two pictures avoiding all three cells
        avoid = [c for c in order if all(c[i][j] == '0' for (i, j) in S)]
        case_ok &= len(avoid) == 2
    else:
        # some pair differing by a switch whose four corners are all unqueried
        found = False
        for a, b in combinations(order, 2):
            diff = [(i, j) for (i, j) in CELLS if a[i][j] != b[i][j]]
            if len(diff) == 4 and not set(diff) & set(S):
                found = True
        case_ok &= found
    case_ok &= bool(pairs)
ok(case_ok, 'every 3-cell set fails, exactly by the guide cases: unqueried-rectangle pair, or (transversal) the two pictures avoiding all three cells')

out('\n== Bonus page 4: Problem 4 margin boards')
g4, _ = grids(doc[3])
g3, _ = grids(doc[2])
sizes = sorted({round(g['cell'] / PT_PER_MM, 1) for g in g1[1:] + g3 + g4} | {round(g['cellh'] / PT_PER_MM, 1) for g in g1[1:] + g3 + g4})
ok(sizes == [22.0], f'P1/P3/P4 working cells: {sizes} mm, square (guide: 22 mm)')
claimed = {((3, 3, 0), (3, 3, 0)): [], ((3, 2, 1), (2, 2, 2)): ['111/110/001', '111/101/010', '111/011/100'],
           ((2, 2, 2), (3, 3, 0)): ['110/110/110'], ((3, 3, 1), (3, 3, 1)): []}
for g in g4:
    m = (tuple(int(v) for v in g['rows']), tuple(int(v) for v in g['cols']))
    s = solutions(*m)
    ok(sorted(fmt(x) for x in s) == sorted(claimed[m]), f'rows {m[0]} cols {m[1]}: {len(s)} picture(s) {[fmt(x) for x in s]}')
    cap = [sum(min(k, cj) for cj in m[1]) for k in range(4)]
    need = [sum(sorted(m[0], reverse=True)[:k]) for k in range(4)]
    out(f'       k largest rows need {need[1:]}; capacity sum min(k, c_j) = {cap[1:]}')
# capacity bound is necessary on all 512 boards (and, with equal totals, here also sufficient)
nec = all(sum(sorted(margins(p)[0], reverse=True)[:k]) <= sum(min(k, cj) for cj in margins(p)[1])
          for p in (tuple(''.join(b[3 * i:3 * i + 3]) for i in range(3)) for b in product('01', repeat=9)) for k in range(4))
ok(nec, 'capacity bound holds for every one of the 512 binary 3x3 boards (necessary)')
suff = True
for rows in product(range(4), repeat=3):
    for cols in product(range(4), repeat=3):
        if sum(rows) != sum(cols):
            continue
        cond = all(sum(sorted(rows, reverse=True)[:k]) <= sum(min(k, c) for c in cols) for k in range(4))
        suff &= cond == bool(solutions(rows, cols))
out(f'     (aside) with equal totals the capacity bound is also sufficient on 3x3 (Gale-Ryser): {suff}')

with open(os.path.join(HERE, 'check_bonus.out'), 'w') as fh:
    fh.write('\n'.join(LOG) + '\n')
