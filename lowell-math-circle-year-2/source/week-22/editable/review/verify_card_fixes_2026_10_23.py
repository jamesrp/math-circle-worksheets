#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes of Week 22 (made in v5, current in v6) against the built PDFs.

Run from the package folder after `bash build.sh`, or pass the folder holding
k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf:

    python3 review/verify_card_fixes_2026_10_23.py [folder]

It reads the printed pages (PyMuPDF), the problem files and figures.py, and checks each
fix and the geometry behind it with exact rational arithmetic. Standard library plus PyMuPDF.
"""
import json
import re
import sys
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

import pymupdf

PKG = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PKG / 'build'
for pf in (PKG / 'problem-files', PKG.parent):
    if (pf / 'figures.py').exists():
        break
else:
    sys.exit('Cannot find figures.py (problem files)')
sys.path.insert(0, str(pf))
sys.dont_write_bytecode = True
import figures  # noqa: E402

fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


def flat(s):
    return ' '.join(s.split())


# ---------- exact geometry: which of the seven splits of four points have meeting regions
def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_seg(p, a, b):
    return orient(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def segs_meet(a, b, c, d):
    o1, o2, o3, o4 = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    return on_seg(c, a, b) or on_seg(d, a, b) or on_seg(a, c, d) or on_seg(b, c, d)


def in_triangle(p, a, b, c):
    if orient(a, b, c) == 0:
        return on_seg(p, a, b) or on_seg(p, b, c) or on_seg(p, a, c)
    s = [orient(a, b, p), orient(b, c, p), orient(c, a, p)]
    return all(v >= 0 for v in s) or all(v <= 0 for v in s)


def successful_splits(pts):
    """pts: dict label -> (x, y). Returns the splits (as 'XY | ZW') whose closed hulls meet."""
    labels = sorted(pts)
    wins = []
    for x in labels:                                   # one label against three
        rest = [y for y in labels if y != x]
        if in_triangle(pts[x], *(pts[y] for y in rest)):
            wins.append(''.join(rest) + ' | ' + x)
    for pair in combinations(labels[1:], 1):          # two against two, A's partner chosen
        g1 = ['A', pair[0]]
        g2 = [y for y in labels if y not in g1]
        if segs_meet(pts[g1[0]], pts[g1[1]], pts[g2[0]], pts[g2[1]]):
            wins.append(''.join(g1) + ' | ' + ''.join(g2))
    return wins


def exact(v):
    return F(str(v))


# ---------- the built PDFs
docs = {n: pymupdf.open(OUT / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator-guide')}
text = {n: [pg.get_text() for pg in d] for n, d in docs.items()}
bands = (('k-1', 'K-1', 'F22-K-v6', 9, 'k_tri', 3), ('grades-2-3', '2-3', 'F22-23-v6', 9, 'm_tri', 4),
         ('grades-4-5', '4-5', 'F22-45-v6', 12, 'u_tri', 4))
for name, band, tag, n, _, _ in bands:
    check(len(text[name]) == n and all(tag in p for p in text[name]), f'{band}: {n} pages, every footer {tag}')

# ---------- should 1: P1 record page, one small board per cross, with D printed
p1 = (pf / 'problems' / '01-meet-on-each-cross.md').read_text()
crosses = {b: m for b, m in re.findall(r'## figure \[([K0-9-]+)\]\nboard\(\w+,(\[.*?\])\)', p1)}
records = {b: (lst, pos) for b, lst, pos in re.findall(r'## figure \[([K0-9-]+)\]\nrecording_boards\(\[(\w+)\+\[.*?for x,y in (\[.*?\])\]', p1)}
answers = {}
for name, band, tag, n, lst, ncross in bands:
    cr = eval(crosses[band])
    rl, rp = records[band]
    rp = eval(rp)
    check(rl == lst and rp == cr and len(cr) == ncross, f'{band} P1: record page has one board per cross ({ncross}), D at the cross positions, same A, B, C')
    page1, page2 = text[name][0], text[name][1]
    labels_on = lambda t: [ln.strip() for ln in t.split('\n')].count('D')
    check('Problem 1:' in page2 and labels_on(page2) == ncross and labels_on(page1) == 0,
          f'{band} P1: p. 2 prints D {ncross} times (one per board); p. 1 keeps the crosses for the marker')
    got = []
    for x, y in cr:
        pts = {lab: (exact(px), exact(py)) for lab, px, py, _ in getattr(figures, lst)}
        pts['D'] = (exact(x), exact(y))
        wins = successful_splits(pts)
        got.append(((x, y), wins))
    answers[band] = got
    check(all(w for _, w in got), f'{band} P1: every D position has a split whose regions meet: ' +
          '; '.join(f'{p} {", ".join(w)}' for p, w in got))

# ---------- should 2: the key's inside location is a small dot, no cross
key = figures.region_key()
H, I, J = (F('13.35'), F('.8')), (F('15.75'), F('.8')), (F('14.35'), F('2.55'))
dot = (F('14.38'), F('1.48'))
s = [orient(H, I, dot), orient(I, J, dot), orient(J, H, dot)]
check(r'\fill (14.38,1.48) circle (.04);' in key and '-- (14.46' not in key and (all(v > 0 for v in s) or all(v < 0 for v in s)),
      'key: a small dot strictly inside triangle HIJ, no cross drawn')


def diagonal_strokes(page, top=None):
    """Short diagonal line segments (each cross is two of them, about 7 pt long)."""
    n = 0
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] != 'l':
                continue
            a, b = it[1], it[2]
            dx, dy = abs(b.x - a.x), abs(b.y - a.y)
            if 3 < dx < 8 and 3 < dy < 8 and abs(dx - dy) < .5 and (top is None or min(a.y, b.y) < top):
                n += 1
    return n


for name, band, tag, n, lst, ncross in bands:
    pg = docs[name][0]
    key_bottom = pg.search_for('contain this point')[0].y1
    check(diagonal_strokes(pg) == 2 * ncross and diagonal_strokes(pg, key_bottom) == 0,
          f'{band} p. 1: {ncross} board crosses, none in the key')

# ---------- could 9: 4-5 P6 wording
u6 = [flat(p) for p in text['grades-4-5'] if 'Problem 6:' in p]
check(len(u6) == 1 and 'Can every arrangement of A, B, C, and D be split into two groups whose regions meet? Give an explanation that covers all arrangements.' in u6[0]
      and 'straight line' not in u6[0] and 'same point' not in u6[0], '4-5 P6: ends "Give an explanation that covers all arrangements."')

# ---------- the guide
G = text['facilitator-guide']
g = flat('\n'.join(G))
check(all('Current v6 student packets' in p for p in G[1:-1]), 'guide: every numbered page names the v6 packets')
pages = {band: len(text[name]) for name, band, *_ in bands}
check(all(f'{band}: {pages[band]} student pages, {tag}.' in g.replace('Grades 2-3', '2-3').replace('Grades 4-5', '4-5')
          for name, band, tag, *_ in bands), 'guide: page map 9, 9, 12 with v6 packet ids')
check('counts are 9, 9, and 12 (v6, with the P1 record page)' in g, 'guide: verification page gives 9, 9 and 12 pages')
# should 3
check('On a line, draw one group just above the dots and the other just below.' in g, 'guide: "Say explicitly" adds above/below for groups on a line')
check('two colors of pencil or crayon for each pair' in g and 'Give each pair two colors, one per group' in g,
      'guide: two colors per pair (table list and launch)')
# should 1 in the guide
check("P1's record page has one small board per cross, with D printed" in g and g.count('own record board') + g.count('own board on the record page') >= 3,
      'guide: P1 record page in preparation and in the K-1, 2-3 and 4-5 P1 gates')
# could 8: the current group, page counts from the actual PDFs
k, m, u = pages['K-1'], pages['2-3'], pages['4-5']
check('4 K-1, 4 middle, and 3 upper packets (108 student sheets total)' in g and 4 * k + 4 * m + 3 * u == 108,
      f'guide: eleven children, 4x{k} + 4x{m} + 3x{u} = 108 sheets')
check('2 of each band, 60 sheets' in g and 2 * (k + m + u) == 60, f'guide: one packet per pair, 2x({k}+{m}+{u}) = 60 sheets')
# could 10
check('Say: "Split the four labels into two groups' in g and 'stretch a real rubber band around three upright markers' in g,
      'guide launch: "Split", and a real band once around three markers')
# should 2 in the guide
check('The small unlabelled interior dot marks a location' in g and 'tiny cross' not in g.split('Use the printed E-J key')[1][:400],
      'guide: the key describes a small dot')
# the P1 answers printed in the guide match the computed splits for the record boards
heads = {'K-1': 'K-1 Problem 1', '2-3': 'Grades 2-3 Problem 1', '4-5': 'Grades 4-5 Problem 1'}
for band, got in answers.items():
    i = next(i for i, p in enumerate(G) if heads[band] in p)
    sect = flat(G[i] + G[i + 1])
    check(all(w in sect for _, ws in got for w in ws), f'guide {band} P1 key names every computed split ({len(got)} placements)')
# could 5
check('Taking turns means one child places all four markers and the partner splits them; then they swap.' in g, 'guide: K-1 P6 roles')
# could 7: route note
route = flat(G[-1])
last_no = [w for w in G[-1].split() if w.isdigit()]
p3 = [flat(p) for p in G if re.search(r'\|\s*Current v6 student packets\s*\n3\n', p)]
check('already marked on guide p. 3' in route and '22' in last_no and 'guide p4' not in route,
      'route page: "guide p. 3", numbered 22')
check(len(p3) == 1 and 'P5 and P6 can continue another day' in p3[0], 'guide p. 3 marks the middle return route P5-6')
check('revised 23 October 2026' in g, 'guide: revision date')

print(json.dumps({'checks_failed': len(fails)}))
sys.exit(1 if fails else 0)
