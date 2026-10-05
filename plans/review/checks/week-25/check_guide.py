"""Independent check of the Week 25 adult guide (week-25-facilitator.pdf).

Uses the boards read from the delivered guide PDF by extract.py, plus the
caption printed above each board, and checks every answer diagram, route,
count and cross-reference against my own enumeration (common.py).
Output: check_guide.out
"""
import json
import os
import re
import sys
from itertools import combinations
from math import comb

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, WEEK, parse, fmt, margins, solutions, switches, bfs,
                    all_pictures)  # noqa: E402

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
G = X['week-25-facilitator.pdf']
doc = pymupdf.open(os.path.join(WEEK, 'week-25-facilitator.pdf'))

# printed page number = last number in the footer line
printed = {}
for n, page in enumerate(doc, 1):
    nums = [w[4] for w in page.get_text('words') if w[1] > page.rect.height - 45 and w[4].isdigit()]
    printed[n] = int(nums[-1]) if nums else None
out('PDF page -> printed page:', printed)
P2PDF = {v: k for k, v in printed.items() if v is not None and k < len(doc)}


def gboards(pp):
    """Boards with captions on printed guide page pp."""
    pdf = P2PDF[pp]
    page = doc[pdf - 1]
    blocks = page.get_text('blocks')
    res = []
    for b in G[pdf - 1]['boards']:
        cands = [bl for bl in blocks if b['y'] - 50 < bl[1] and bl[3] < b['y'] - 12 and bl[0] <= b['x']]
        cap = ' '.join(max(cands, key=lambda bl: (bl[0], bl[1]))[4].split()) if cands else ''
        p = parse(b['picture'])
        rc = tuple(int(v) for v in b['row_counts'])
        cc = tuple(int(v) for v in b['col_counts'])
        assert margins(p) == (rc, cc), (pp, cap, b)   # printed circles agree with dots
        res.append((cap, p))
    return res


def page_text(pp):
    return ' '.join(doc[P2PDF[pp] - 1].get_text('text').split())


def same_set(found, expected, label):
    return ok(sorted(found) == sorted(expected) and len(set(found)) == len(found),
              f'{label}: guide shows {len(found)}, complete list has {len(expected)}')


def top(p):
    return {j + 1 for j, v in enumerate(p[0]) if v == '1'}


def step(p, q):
    """The switch taking p to q, or None."""
    for i, k, j, l, r in switches(p):
        if r == q:
            return (i, k, j + 1, l + 1)
    return None


# ------------------------------------------------------------------ overview
out('\n== Overview (unnumbered) and general claims')
# uniqueness <=> no switch <=> nested rows, on every board up to 3x4 and 2x6
bad = 0
tot = 0
for (r, c) in ((2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (4, 3)):
    for p in all_pictures(r, c):
        tot += 1
        uniq = len(solutions(*margins(p))) == 1
        nosw = not switches(p)
        sets = [top((row,)) for row in p]
        nested = all(a <= b or b <= a for a, b in combinations(sets, 2))
        if not (uniq == nosw == nested):
            bad += 1
ok(bad == 0, f'unique <=> no legal switch <=> nested row sets, on all {tot} boards of sizes 2x2..2x6, 3x3, 3x4, 4x3')
# general connectivity (Ryser) on 3x3 and 3x4 margin classes
bad = 0
for (r, c) in ((3, 3), (3, 4)):
    seen = set()
    for p in all_pictures(r, c):
        m = margins(p)
        if m in seen:
            continue
        seen.add(m)
        s = solutions(*m)
        if set(bfs(s[0])) != set(s):
            bad += 1
ok(bad == 0, 'every margin class on 3x3 and 3x4 is switch-connected (cited Ryser theorem, finite check)')
ok(bad == 0 and 2 ** 8 + 2 ** 12 + 2 ** 9 == 4864, 'p18 "every binary 2-by-4, 2-by-6, and 3-by-3 board, totaling 4,864"')

# ------------------------------------------------------------------ printed p2
out('\n== p2 launch')
b = gboards(2)
ok(fmt(b[0][1]) == '101/010' and margins(b[0][1]) == ((2, 1), (1, 1, 1)), 'launch A1,A3,B2 -> rows 2,1; columns 1,1,1')
ok(margins(b[1][1]) == margins(b[0][1]) and b[1][1] != b[0][1], f'"a different matching picture" {fmt(b[1][1])}')

out('\n== p3 K-1 P1')
b = gboards(3)
same_set([p for _, p in b[0:2]], solutions((1, 1), (1, 1)), 'top pair')
same_set([p for _, p in b[2:4]], solutions((1, 1), (1, 0, 1)), 'middle pair')
same_set([p for _, p in b[4:7]], solutions((2, 1), (1, 1, 1)), 'bottom pair')
for cap, p in b:
    out(f'     caption "{cap}" -> {fmt(p)}')

out('\n== p4 K-1 P2')
b = gboards(4)
same_set([p for _, p in b[0:3]], solutions((1, 2), (1, 1, 1)), 'left grids (rows 1,2)')
same_set([p for _, p in b[3:6]], solutions((2, 1), (1, 1, 1)), 'right grids (rows 2,1)')
ok(all(('column %d' % (p[0].index('1') + 1)) in cap for cap, p in b[0:3]), 'left captions name the A counter column')
ok(all(('column %d' % (p[1].index('1') + 1)) in cap for cap, p in b[3:6]), 'right captions name the B counter column')

out('\n== p5 K-1 P3')
b = gboards(5)
same_set([p for _, p in b], solutions((1, 1, 1), (1, 1, 1)), 'permutation pictures')
ok(all(cap.replace(' ', '') == ','.join('ABC'[i] + str(row.index('1') + 1) for i, row in enumerate(p)) for cap, p in b),
   'captions match pictures')

out('\n== p6 K-1 P4')
b = gboards(6)
ok(solutions((3, 1), (2, 1, 1)) == [b[0][1]], f'page-5 forced picture {fmt(b[0][1])} is the only one')
ok(solutions((2, 1, 0), (2, 1, 0)) == [b[1][1]], f'page-6 top forced picture {fmt(b[1][1])} is the only one')
same_set([p for _, p in b[2:]], solutions((2, 1, 1), (2, 1, 1)), 'page-6 bottom five pictures')
ok('no, no, yes' in page_text(6) and '1, 1, and 5' in page_text(6), 'stated answers no, no, yes; counts 1, 1, 5')

out('\n== p7 K-1 P5-P6')
b = gboards(7)
for cap, p in b:
    n = len(solutions(*margins(p)))
    out(f'     "{cap}": {fmt(p)}  counters {sum(r.count("1") for r in p)}  solutions {n}')
ok(len(solutions(*margins(b[0][1]))) == 1 and len(solutions(*margins(b[3][1]))) == 1, 'left examples unique')
ok(margins(b[1][1]) == margins(b[2][1]) and b[1][1] != b[2][1] and len(solutions(*margins(b[1][1]))) == 2,
   '2x3 ambiguous pair, exactly two solutions')
ok(margins(b[4][1]) == margins(b[5][1]) and b[4][1] != b[5][1] and len(solutions(*margins(b[4][1]))) == 5,
   '3x3 ambiguous pair, five solutions "all displayed on guide page 6"')
ok(all(sum(r.count('1') for r in p) == 4 for _, p in b), 'every displayed picture uses four counters')

out('\n== p8 G2-3 P1')
b = gboards(8)
same_set([p for _, p in b[0:3]], solutions((2, 1), (1, 1, 1)), 'top pair')
same_set([p for _, p in b[3:4]], solutions((3, 1), (2, 1, 1)), 'middle pair')
same_set([p for _, p in b[4:6]], solutions((2, 2), (2, 1, 1)), 'bottom pair')
ok(all(cap == 'B%d' % (p[1].index('1') + 1) for cap, p in b[0:3]), 'captions B1, B2, B3 match')

out('\n== p9 G2-3 P2')
b = gboards(9)
same_set([p for _, p in b], solutions((2, 1, 1), (2, 1, 1)), 'five pictures')
for cap, p in b:
    out(f'     "{cap}" -> {fmt(p)}')

out('\n== p10 G2-3 P3')
b = gboards(10)
ok(fmt(b[0][1]) == '100/000/001' and set(solutions(*margins(b[0][1]))) == {b[0][1], b[1][1]},
   'page 3: start and its only alternative')
for cap, p in b[2:]:
    n = len(switches(p))
    ok(cap.split(': ')[1].startswith(str(n)), f'"{cap}": {n} switch(es)')
res = sorted(fmt(sw[4]) for sw in switches(parse('110/001/100')))
ok(res == sorted(['011/100/100', '101/010/100', '110/100/001']), f'bottom-left results {res}')

out('\n== p11 G2-3 P4-P5')
b = gboards(11)
s0, s1, s2 = (p for _, p in b[0:3])
d = bfs(s0)
ok(d[s1] == 1 and d[s2] == 2, f'start {fmt(s0)} -> {fmt(s1)} (1) -> {fmt(s2)} (2)')
ok(step(s0, s1)[2:] == (1, 3) and step(s1, s2)[2:] in ((2, 4), (4, 2)),
   f'route "switches columns 1,3 and then 2,4": {step(s0, s1)}, {step(s1, s2)}')
one = sorted(fmt(p) for p in d if d[p] == 1)
ok(sorted(''.join(str(j) for j in sorted(top(parse(x)))) for x in one) == ['13', '14', '23', '24'],
   'one-switch answers A={1,3},{1,4},{2,3},{2,4}')
ok(all(len(solutions(*margins(p))) == 1 for _, p in b[3:5]), 'P5 unique choices 111/100 and 111/100/000')

out('\n== p12 G4-5 P1-P2')
b = gboards(12)
same_set([p for _, p in b], solutions((2, 2), (1, 1, 1, 1)), 'six pictures')
ok(all(cap == 'Top columns ' + ','.join(str(j) for j in sorted(top(p))) for cap, p in b), 'captions match top columns')
ok('guide page 11' in page_text(12) and [fmt(p) for _, p in gboards(11)[0:3]] == ['1100/0011', '0110/1001', '0011/1100'],
   '"12 to 23 to 34 ... boards appear on guide page 11": they do (G2-3 P4 boards)')

out('\n== p13 G4-5 P3')
b = [p for _, p in gboards(13)]
cols = [step(b[i], b[i + 1]) for i in range(3)]
ok(all(cols) and [c[2:] for c in cols] == [(1, 4), (2, 5), (3, 6)], f'route 1,4; 2,5; 3,6 legal: {cols}')
ok(bfs(b[0])[b[3]] == 3, 'and shortest (3)')
ok(comb(6, 3) == 20, 'twenty pictures')

out('\n== p14 G4-5 P4')
b = gboards(14)
same_set([p for _, p in b], solutions((3, 3), (2, 1, 0, 1, 1, 1)), 'six pictures')
ok(all(cap.startswith('Free top pair ' + ','.join(str(j) for j in sorted(top(p) - {1}))) for cap, p in b), 'captions match')
a, mid, z = parse('110100/100011'), parse('100110/110001'), parse('100011/110100')
ok(step(a, mid)[2:] in ((2, 5), (5, 2)) and step(mid, z)[2:] in ((4, 6), (6, 4)), 'route {2,4} -(2,5)-> {4,5} -(4,6)-> {5,6} legal')
ok(fmt(b[3][1]) == '100110/110001', '"intermediate board is the first board in the second row"')

out('\n== p15 G4-5 P5')
b = gboards(15)
st, tg = b[0][1], b[1][1]
ok(sorted(top(st) - top(tg)) == [2, 4] and sorted(top(tg) - top(st)) == [5, 6] and bfs(st)[tg] == 2,
   'example: unwanted top columns 2,4; missing 5,6; distance 2')

out('\n== p16 no switch means unique')
b = gboards(16)
ok(not switches(b[0][1]) and len(solutions(*margins(b[0][1]))) == 1, '111/110/100 nested, unique')
ok(bool(switches(b[1][1])), '110/001/100 has a switch')

out('\n== p17 extensions')
b = gboards(17)
ok(margins(b[0][1]) == margins(b[1][1]) and b[0][1][0] == b[1][1][0] and bfs(b[0][1])[b[1][1]] == 1,
   'three-row pair: same counts, same top row, distance 1')
ok(solutions((2, 0), (2, 0)) == [], '2x2 rows (2,0), columns (2,0): no picture')
# count formula C(s,k) for two-row margins with column counts 0/1/2
bad = 0
for c in range(1, 8):
    for cols in __import__('itertools').product((0, 1, 2), repeat=c):
        s_, t_ = cols.count(1), cols.count(2)
        for a_ in range(c + 1):
            for b_ in range(c + 1):
                k = a_ - t_
                pred = comb(s_, k) if (0 <= k <= s_ and a_ + b_ == sum(cols)) else 0
                if len(solutions((a_, b_), cols)) != pred:
                    bad += 1
ok(bad == 0, 'two-row count "s choose k" (with feasibility conditions), all margins up to 7 columns')

out('\n== p18 verification claims')
for (r, c, nu, na) in ((2, 3, 9, 3), (3, 3, 45, 27)):
    by = {}
    for p in all_pictures(r, c, 4):
        by.setdefault(margins(p), []).append(p)
    u = sum(1 for v in by.values() if len(v) == 1)
    a_ = sum(1 for v in by.values() if len(v) > 1)
    ok((u, a_) == (nu, na), f'{r}x{c} four-counter margin classes: {u} unique, {a_} ambiguous')
ok('pages 15-17' in page_text(18) and 'arguments' in page_text(18), 'pages 15-17 hold the G4-5 P5 proof, the no-switch proof, extensions')

out('\n== cross-references')
t = {pp: page_text(pp) for pp in P2PDF if pp}
ok('Why no switch means unique' in t[16], '"no-switch test on guide page 16" / "criterion on guide page 16"')
ok('K-1 Problems 5 and 6' in t[7], '"110/101 or 110/001/100 from guide page 7"')
ok('Sources and verification' in t[18] and 'Ryser' in t[18], '"broader interchange theorem cited on page 18"')
out(f'     note (layout only): the appended route-note page is numbered {printed[len(doc)]}; '
    f'the page before it is numbered {printed[len(doc) - 1]}')

out('\n== lower bound used by the G2-3 P4 hint (p11)')
# claim on p11: "Counting four moved counters is not by itself a lower bound,
# because a route could move counters more than once."
# Test: is (number of cells occupied in start but empty in target)/2 a lower
# bound on the switch distance, for every same-margin pair?
viol = 0
pairs = 0
for (r, c) in ((2, 4), (2, 6), (3, 3), (3, 4)):
    seen = set()
    for p in all_pictures(r, c):
        m = margins(p)
        if m in seen:
            continue
        seen.add(m)
        s = solutions(*m)
        for x in s:
            dx = bfs(x)
            for y in s:
                pairs += 1
                wrong = sum(a == '1' and b_ == '0' for u, v in zip(x, y) for a, b_ in zip(u, v))
                if 2 * dx[y] < wrong:
                    viol += 1
ok(viol == 0, f'"wrong counters / 2" is a valid lower bound on all {pairs} same-margin pairs '
   f'(2x4, 2x6, 3x3, 3x4); for 1100/0011 -> 0011/1100 it gives 4/2 = 2')
st, tg = parse('1100/0011'), parse('0011/1100')
out(f'     G2-3 P4: cells occupied in start, empty in target = '
    f'{sum(a == "1" and b_ == "0" for u, v in zip(st, tg) for a, b_ in zip(u, v))}; each switch empties exactly 2 cells')

with open(os.path.join(HERE, 'check_guide.out'), 'w') as fh:
    fh.write('\n'.join(LOG) + '\n')
