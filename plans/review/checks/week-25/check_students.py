"""Independent check of every student problem in the three base packets.

Reads the boards that extract.py pulled out of the delivered PDFs, checks that
printed counts agree with any printed counters, and solves each task by
exhaustive enumeration and breadth-first search over switches.
Run extract.py first.  Output: check_students.out
"""
import json
import os
import sys
from itertools import combinations
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, parse, fmt, margins, solutions, switches, bfs,
                    all_pictures, cell_name)  # noqa: E402

LOG = []


def out(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


def ok(cond, msg):
    out(('PASS ' if cond else 'FAIL ') + msg)
    return cond


if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    import extract
    extract.main()
X = json.load(open(os.path.join(HERE, 'extracted.json')))


def boards(f, page):
    return X[f][page - 1]['boards']


def ints(lst):
    return tuple(int(v) for v in lst)


def text(f, page):
    return X[f][page - 1]['text']


# ------------------------------------------------------------ generic checks
out('== Generic: scale, labels, printed counts vs printed counters')
for f, pages in X.items():
    if 'facilitator' in f:
        continue
    for pg in pages:
        for b in pg['boards']:
            sq = max(b['cell_w_mm'] + b['cell_h_mm']) - min(b['cell_w_mm'] + b['cell_h_mm'])
            if sq > 0.1:
                ok(False, f'{f} p{pg["page"]}: non-square cells {b["cell_w_mm"]} x {b["cell_h_mm"]}')
            if b['row_labels'] != list('ABCDEF'[:b['rows']]) or b['col_labels'] != [str(j + 1) for j in range(b['cols'])]:
                ok(False, f'{f} p{pg["page"]}: labels {b["row_labels"]} {b["col_labels"]}')
            if b['picture'].count('1') and all(v not in (None, '') for v in b['row_counts'] + b['col_counts']):
                r, c = margins(parse(b['picture']))
                if (r, c) != (ints(b['row_counts']), ints(b['col_counts'])):
                    ok(False, f'{f} p{pg["page"]}: printed counts {b["row_counts"]} {b["col_counts"]} but counters give {r} {c}')
out('done (only failures are listed above)')


def margin_of(b):
    return ints(b['row_counts']), ints(b['col_counts'])


def show(sols):
    return ', '.join(fmt(s) for s in sols)


# ===================================================================== K-1
K = 'week-25-k-1.pdf'
out('\n== K-1')
b = boards(K, 1)
ok(b[1]['picture'] == '11/00' and margin_of(b[1]) == ((2, 0), (1, 1)),
   'p1 example: A1,A2 occupied -> rows 2,0 and columns 1,1')

import pymupdf  # noqa: E402
from common import WEEK  # noqa: E402
pg = pymupdf.open(os.path.join(WEEK, K))[0]
rings = [d['rect'] for d in pg.get_drawings() if d['type'] == 's' and d['items'][0][0] == 'c']
sweeps = [d for d in pg.get_drawings() if d['type'] == 's' and d.get('dashes') not in (None, '[] 0') and len(d['items']) == 2]
right = b[1]
PT = 72 / 25.4
bx, by, cell = right['x'], right['y'], 22 * PT
res = []
for d in sweeps:
    (_, p, q), (_, q2, e) = d['items']
    ring = min(rings, key=lambda r: ((r.x0 + r.x1) / 2 - e.x) ** 2 + ((r.y0 + r.y1) / 2 - e.y) ** 2)
    cx, cy, rad = (ring.x0 + ring.x1) / 2, (ring.y0 + ring.y1) / 2, (ring.x1 - ring.x0) / 2
    gap = ((cx - e.x) ** 2 + (cy - e.y) ** 2) ** .5 - rad
    if abs(p.y - q.y) < .01:      # row sweep
        band = int((p.y - by) // cell)
        res.append(('row ' + 'AB'[band], round((cy - by) / cell - .5), round(gap, 1)))
    else:                          # column sweep
        band = int((p.x - bx) // cell)
        res.append(('column ' + str(band + 1), round((cx - bx) / cell - .5), round(gap, 1)))
ok(all(r[0].endswith('AB'[r[1]] if r[0].startswith('row') else str(r[1] + 1)) and abs(r[2]) < 4 for r in res),
   f'p1 example sweeps stay in their own row/column and end within 4 pt (an arrowhead) of that line\'s circled count: {res}')

out('-- P1 (p2): "Make two different pictures for each pair of grids."')
for k in range(0, 6, 2):
    m = margin_of(boards(K, 2)[k])
    assert m == margin_of(boards(K, 2)[k + 1])
    s = solutions(*m)
    ok(len(s) >= 2, f'pair {m}: {len(s)} pictures: {show(s)}')

out('-- P2 (p3): "Find and draw every different picture for each set of counts." (6 grids)')
cnt = Counter(margin_of(x) for x in boards(K, 3))
for m, n in cnt.items():
    s = solutions(*m)
    ok(len(s) == n, f'{m}: {len(s)} pictures, {n} grids: {show(s)}')

out('-- P3 (p4-5): "Find and draw every different three-counter picture with these counts." (4+2 grids)')
grids = [x for x in boards(K, 4) + boards(K, 5) if x['rows'] == 3]
s = solutions((1, 1, 1), (1, 1, 1))
ok(len(s) == len(grids) == 6, f'{len(s)} pictures, {len(grids)} grids')

out('-- P4 (p5 bottom): "Can you make two different pictures with these counts?"')
m = margin_of(boards(K, 5)[2])
s = solutions(*m)
ok(len(s) == 1, f'{m}: {len(s)} picture(s): {show(s)} -> answer "no"')
out('-- P4 (p6): "Make two different pictures for each pair of grids, if you can."')
for k in (0, 2):
    m = margin_of(boards(K, 6)[k])
    s = solutions(*m)
    out(f'     {m}: {len(s)} picture(s): {show(s)}')

out('-- P5/P6 (p7-8): four-counter pictures, unique versus ambiguous counts')


def classes(r, c, k):
    by = Counter(margins(p) for p in all_pictures(r, c, k))
    uniq = sum(1 for v in by.values() if v == 1)
    amb = sum(1 for v in by.values() if v > 1)
    return by, uniq, amb


for (r, c) in ((2, 3), (3, 3)):
    by, u, a = classes(r, c, 4)
    pics_u = sum(v for v in by.values() if v == 1)
    pics_a = sum(v for v in by.values() if v > 1)
    out(f'     {r}x{c}, 4 counters: {u} unique margin classes ({pics_u} pictures), '
        f'{a} ambiguous classes ({pics_a} pictures)')
    ok(u > 0 and a > 0, f'{r}x{c}: both a unique and an ambiguous four-counter choice exist (P6 possible)')

# ============================================================== Grades 2-3
M = 'week-25-grades-2-3.pdf'
out('\n== Grades 2-3')
out('-- P1 (p1): "make two different pictures that match the counts, if you can"')
for k in range(0, 6, 2):
    m = margin_of(boards(M, 1)[k])
    s = solutions(*m)
    out(f'     {m}: {len(s)} picture(s): {show(s)}')

out('-- P2 (p2-3): "Find and draw every different picture with these counts." (4+2 grids)')
grids = [x for x in boards(M, 2) + boards(M, 3) if margin_of(x) == ((2, 1, 1), (2, 1, 1))]
s211 = solutions((2, 1, 1), (2, 1, 1))
ok(len(s211) == 5, f'{len(s211)} pictures, {len(grids)} grids: {show(s211)}')
D = {p: bfs(p) for p in s211}
out('     switch distances inside this catalog: ' +
    '; '.join(f'{fmt(p)}->{fmt(q)}={D[p][q]}' for p, q in combinations(s211, 2)))

out('-- P3 (p3): "Move exactly two counters from the filled picture to make a different picture with the same counts."')
start = parse(boards(M, 3)[2]['picture'])
s = solutions(*margins(start))
others = [p for p in s if p != start]
ok(len(others) == 1, f'start {fmt(start)}: other pictures {show(others)}')
moved = sum(a == '1' and b == '0' for x, y in zip(start, others[0]) for a, b in zip(x, y))
ok(moved == 2, f'cells vacated going to the only alternative: {moved}')

out('-- P3 (p4): "Find every switch in each picture. Which pictures have none?"')
ex = boards(M, 4)
ok(ex[0]['picture'] == '10/01' and ex[1]['picture'] == '01/10' and
   [sw[4] for sw in switches(('10', '01'))] == [('01', '10')], 'switch example 10/01 -> 01/10 is the one legal switch')
for x in ex[2:]:
    p = parse(x['picture'])
    sw = switches(p)
    desc = '; '.join(f"rows {'ABC'[i]},{'ABC'[k]} cols {j+1},{l+1} -> {fmt(q)}" for i, k, j, l, q in sw)
    # each geometric rectangle is found once (orientation is fixed by occupied corners)
    out(f'     {fmt(p)}: {len(sw)} switch(es){": " + desc if sw else ""}; '
        f'pictures with these counts: {len(solutions(*margins(p)))}')

out('-- P4 (p5): one switch / exactly two switches from 1100/0011')
start = parse(boards(M, 5)[0]['picture'])
d = bfs(start)
s = solutions(*margins(start))
ok(set(d) == set(s), f'all {len(s)} pictures reachable')
for k in (1, 2):
    out(f'     distance {k}: ' + show(sorted(p for p in d if d[p] == k)))
ok(sum(1 for p in d if d[p] == 2) == 1, 'exactly one picture needs two switches (answer forced: 0011/1100)')

out('-- P5 (p6): four counters; choose a picture that no different picture matches')
for (r, c) in ((2, 3), (3, 3)):
    ex_u = [p for p in all_pictures(r, c, 4) if len(solutions(*margins(p))) == 1]
    ok(bool(ex_u), f'{r}x{c}: {len(ex_u)} four-counter pictures are unique, e.g. {fmt(ex_u[0])}')
    ok(all(not switches(p) for p in ex_u) and
       all(switches(p) for p in all_pictures(r, c, 4) if len(solutions(*margins(p))) > 1),
       f'{r}x{c}: unique <=> no switch on all four-counter pictures')

# ============================================================== Grades 4-5
U = 'week-25-grades-4-5.pdf'
out('\n== Grades 4-5')
out('-- P1 (p1-2): every picture with rows 2,2 and columns 1,1,1,1 (3+3 grids)')
grids = boards(U, 1) + boards(U, 2)
s = solutions((2, 2), (1, 1, 1, 1))
ok(len(s) == len(grids) == 6, f'{len(s)} pictures, {len(grids)} grids')
out('-- P2 (p3): connected? greatest shortest distance?')
D = {p: bfs(p) for p in s}
ok(all(set(D[p]) == set(s) for p in s), 'switch graph on the 6 pictures is connected')
diam = max(D[p][q] for p in s for q in s)
ok(diam == 2, f'greatest shortest distance = {diam}')
degs = sorted(len(switches(p)) for p in s)
out(f'     one-switch neighbours per picture: {degs}')

out('-- P3 (p4-5): 111000/000111 -> 000111/111000, fewest switches')
a, b2 = parse(boards(U, 4)[0]['picture']), parse(boards(U, 4)[1]['picture'])
d = bfs(a)
ok(d[b2] == 3, f'distance = {d[b2]}; two blank route grids on p5 = intermediates of a 3-switch route')
ok(len(solutions(*margins(a))) == 20, f'pictures with these counts: {len(solutions(*margins(a)))}')
out('-- P4 (p6): 110100/100011 -> 100011/110100')
a, b2 = parse(boards(U, 6)[0]['picture']), parse(boards(U, 6)[1]['picture'])
s = solutions(*margins(a))
D = {p: bfs(p) for p in s}
ok(D[a][b2] == 2, f'fewest switches = {D[a][b2]}')
ok(len(s) == 6, f'pictures sharing these counts = {len(s)}')
ok(max(D[p][q] for p in s for q in s) == 2, f'largest shortest distance = {max(D[p][q] for p in s for q in s)}')

out('-- P5 (p7): two-row rule for any number of columns (checked for 1..8 columns)')
bad = 0
pairs = 0
for c in range(1, 9):
    seen = set()
    for p in all_pictures(2, c):
        m = margins(p)
        if m in seen:
            continue
        seen.add(m)
        s = solutions(*m)
        free = [j for j in range(c) if m[1][j] == 1]
        k = sum(1 for j in free if s[0][0][j] == '1')
        for x in s:
            dx = bfs(x)
            if set(dx) != set(s):
                bad += 1
            for y in s:
                pairs += 1
                rule = sum(1 for j in range(c) if x[0][j] == '1' and y[0][j] == '0')
                if dx[y] != rule:
                    bad += 1
        if len(s) > 1:
            diam = max(bfs(x)[y] for x in s for y in s)
            if diam != min(k, len(free) - k):
                bad += 1
ok(bad == 0, f'{pairs} ordered same-margin pairs on 2x1..2x8: connected, distance = #(top in start, not in target), '
   f'diameter = min(k, s-k)')

with open(os.path.join(HERE, 'check_students.out'), 'w') as fh:
    fh.write('\n'.join(LOG) + '\n')
