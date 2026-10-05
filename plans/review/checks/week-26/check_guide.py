"""Independent check of the Week 26 adult guide (week-26-facilitator.pdf).

Every one of the 82 answer figures is read from the delivered PDF by
extract.py, with the caption printed under it, and checked against the caption
and against my own enumeration.  The guide's general claims, worked numbers and
cross-references are checked separately.  Guide pages below are the printed
page numbers (PDF page minus one).  Output: check_guide.out
"""
import math
import os
import re
import subprocess
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, WEEK, Log, perimeter, shared, connected, rows_cols, bbox,  # noqa: E402
                    intervals, has_block, longest_run, holes, canon, show, norm,
                    neighbors_empty, redelmeier, load_extracted, from_rows, N4)

L = Log()
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract.py')], check=True)
X = load_extracted(os.path.join(HERE, 'extracted.json'))
G = X['guide']
for f in G:
    f['page'] = f['pdf_page'] - 1
L.out(f'{len(G)} guide figures read from the PDF')


def fig(page, caption_start):
    hits = [f for f in G if f['page'] == page and f['caption'].startswith(caption_start)]
    assert len(hits) == 1, (page, caption_start, len(hits))
    return hits[0]


def row_lengths(cells):
    c = norm(cells)
    h = max(y for _, y in c) + 1
    out = []
    for y in range(h):
        xs = sorted(x for x, yy in c if yy == y)
        out.append((xs[0], len(xs), xs == list(range(xs[0], xs[0] + len(xs)))))
    return out


def changes(cells):
    S = set(cells)
    return sorted({perimeter(S | {t}) - perimeter(S) for t in neighbors_empty(S)})


# ---------------------------------------------------- generic caption checks
L.out('\n=== Every figure against the numbers in its caption')
for f in G:
    cap = f['caption']
    cells = f['cells']
    allc = cells + f['added']
    n = len(cells)
    msgs = []
    good = connected(allc) and abs(f['cell_w_pt'] - f['cell_h_pt']) < 0.05
    if not f['added']:
        good &= connected(cells)
        m = re.search(r'P = (\d+)', cap)
        if m:
            good &= perimeter(cells) == int(m.group(1))
            msgs.append(f'P={perimeter(cells)}')
        m = re.search(r'e = (\d+)', cap)
        if m:
            good &= shared(cells) == int(m.group(1))
            msgs.append(f'e={shared(cells)}')
        m = re.search(r'(\d+) (tiles|squares)', cap)
        if m:
            good &= n == int(m.group(1))
            msgs.append(f'n={n}')
        m = re.search(r'(shortest|longest) (\d+)', cap)
        if m:
            good &= perimeter(cells) == int(m.group(2))
            msgs.append(f'P={perimeter(cells)}')
        m = re.search(r'rows ([\d,]+);', cap)
        if m:
            want = [int(v) for v in m.group(1).split(',')]
            rl = row_lengths(cells)
            good &= [k for _, k, _ in rl] == want and all(x0 == 0 and run for x0, _, run in rl)
            msgs.append(f'left-aligned rows {[k for _, k, _ in rl]}')
        m = re.search(r'(\d+) rows, (\d+) columns', cap)
        if m:
            good &= rows_cols(cells) == (int(m.group(1)), int(m.group(2)))
            msgs.append(f'rows/cols {rows_cols(cells)}')
        m = re.search(r'(\d+) x (\d+) = (\d+)', cap)
        if m:
            w, h = bbox(cells)
            good &= sorted((w, h)) == sorted((int(m.group(1)), int(m.group(2)))) and n == int(m.group(3)) \
                and n == w * h
            msgs.append(f'{w}x{h} full={n == w * h}')
        m = re.search(r'before (\d+)', cap)
        if m:
            good &= perimeter(cells) == int(m.group(1))
            msgs.append(f'before {perimeter(cells)}, changes {changes(cells)}')
    else:
        m = re.search(r'after (\d+)', cap)
        if m:
            good &= perimeter(allc) == int(m.group(1))
            msgs.append(f'after {perimeter(allc)}')
        m = re.search(r'([+-]?\d+): (\d+) starting tile', cap)
        if m:
            good &= connected(cells) and n == int(m.group(2)) and \
                perimeter(allc) - perimeter(cells) == int(m.group(1))
            msgs.append(f'start n={n} connected={connected(cells)} change {perimeter(allc) - perimeter(cells):+d}')
    L.ok(good, f'p.{f["page"]} [{cap}] {show(allc)} ' + '; '.join(msgs))

# ------------------------------------------------------------- page 4
L.out('\n=== p.4 K-1 Problem 1')
tets = [fig(4, c)['cells'] for c in ('Straight', 'Square', 'L:', 'T:', 'Zigzag')]
L.ok(len({canon(t) for t in tets}) == 5 and all(len(t) == 4 for t in tets),
     'five pictured tetrominoes are the five distinct free tetrominoes')
L.ok([shared(t) for t in tets] == [3, 4, 3, 3, 3], 'shared sides: square 4, others 3 (16-8=8, 16-6=10)')
grow = {}
for name, t in zip(('straight', 'square', 'L', 'T', 'zigzag'), tets):
    grow[name] = 0 in changes(t)
L.out('  can gain a fifth tile without increasing P:', grow)
L.ok(grow == {'straight': False, 'square': False, 'L': True, 'T': True, 'zigzag': True},
     'extension answer: L, T and zigzag can; straight and square cannot')
L.out('NOTE p.4: the guide says only "the square cannot, while L can fill its missing corner"; '
      'T and zigzag can too, and the straight cannot')

# ------------------------------------------------------------- page 5
L.out('\n=== p.5 K-1 Problems 2-3')
census = {}


def cb(p):
    census.setdefault(len(p), set()).add(perimeter(p))


redelmeier(8, cb)
for n in (5, 6, 7, 8):
    a = fig(5, f'{n} tiles: shortest')['cells']
    b = fig(5, f'{n} tiles: longest')['cells']
    L.ok(perimeter(a) == min(census[n]) and perimeter(b) == max(census[n]) and len(a) == len(b) == n,
         f'{n} tiles: pictured shortest {perimeter(a)} = min, longest {perimeter(b)} = max')
L.ok(show(fig(5, '7 tiles: shortest')['cells']) in ('####/###.', '####/.###', '###./####', '.###/####'),
     'seven-tile minimum pictured is a 2-by-4 rectangle with one corner missing')
L.ok(max(r * (4 - r) for r in range(1, 4)) == 4 and max(r * (5 - r) for r in range(1, 5)) == 6,
     'r+c<=4 holds at most 4 tiles; r+c<=5 holds at most 6')

# ------------------------------------------------------------- page 6
L.out('\n=== p.6 K-1 Problems 4-5')
a, b = fig(6, 'P = 12: one type')['cells'], fig(6, 'P = 12: another type')['cells']
c, d = fig(6, 'P = 14: one type')['cells'], fig(6, 'P = 14: another type')['cells']
L.ok(canon(a) != canon(b) and sorted(bbox(a)) == [2, 4] and sorted(bbox(b)) == [3, 3],
     '12-side pair are different, with 4x2 and 3x3 bounding boxes')
L.ok(canon(c) != canon(d) and longest_run(c) == 6, '14-side pair: a row and a different bent row')

# ------------------------------------------------------------- page 7
L.out('\n=== p.7 K-1 Problem 6')
starts = [fig(7, c)['cells'] for c in ('Top start', 'Middle start', 'Bottom start')]
results = [fig(7, f'Best after one move: {v}')['cells'] for v in (14, 10, 12)]
k1p6 = [s['cells'] for s in X['k1'][5]['shapes']]
L.ok([canon(s) for s in starts] == [canon(s) for s in k1p6], 'guide starts match student page 6 (up to turns/flips)')
for s, r, want_moves in zip(starts, results, (22, 1, 2)):
    S = set(s)
    reach = set()
    opt = 0
    best = None
    for src in S:
        rest = S - {src}
        for dst in neighbors_empty(rest) - {src}:
            new = rest | {dst}
            if connected(new):
                reach.add(canon(new))
                P = perimeter(new)
                if best is None or P < best:
                    best, opt = P, 0
                if P == best:
                    opt += 1
    L.ok(canon(r) in reach and perimeter(r) == best and opt == want_moves,
         f'{show(s)}: pictured result {show(r)} is one legal move away; best {best}; {opt} optimal moves')
top = starts[0]
L.ok(norm(results[0]) == norm(set(top[:5]) | {(0, 1)}) or canon(results[0]) == canon([(x, 0) for x in range(5)] + [(0, 1)]),
     'top: right endpoint moved just below the left endpoint')
two_by_three = []
for w, h in ((3, 2), (2, 3)):
    for x0 in range(-3, 5):
        for y0 in range(-3, 4):
            box = {(x0 + i, y0 + j) for i in range(w) for j in range(h)}
            two_by_three.append(len(box & set(starts[2])))
L.ok(max(two_by_three) == 4, 'bottom: every 2x3 or 3x2 box holds at most 4 of the L tiles')

# ------------------------------------------------------------- page 8
L.out('\n=== p.8 Grades 2-3 Problem 1')
sq = [(x, y) for x in range(3) for y in range(3)]
dele = {}
for cell in sq:
    rest = [q for q in sq if q != cell]
    kind = 'corner' if cell in [(0, 0), (0, 2), (2, 0), (2, 2)] else ('center' if cell == (1, 1) else 'edge')
    dele.setdefault(kind, set()).add(perimeter(rest))
L.ok(dele == {'corner': {12}, 'edge': {14}, 'center': {16}}, f'3x3 minus one cell: {dele}')
s1, s2 = fig(8, 'Shortest: 2 by 4')['cells'], fig(8, 'Shortest: corner missing')['cells']
l1, l2 = fig(8, 'Longest: row')['cells'], fig(8, 'Longest: bent row')['cells']
L.ok(canon(s1) != canon(s2) and canon(l1) != canon(l2), 'both pairs are genuinely different shapes')

# ------------------------------------------------------------- page 9
L.out('\n=== p.9 Grades 2-3 Problem 2')
st = [fig(9, c)['cells'] for c in ('Row: before', 'Stair: before', 'U: before', 'Frame: before')]
L.ok([changes(s) for s in st] == [[2], [0, 2], [-2, 2], [-4, 2]], 'change sets {+2}, {0,+2}, {-2,+2}, {-4,+2}')
after = []
for s in st:
    top_row = min(y for _, y in s)
    left = min(x for x, y in s if y == top_row)
    after.append(perimeter(list(s) + [(left - 1, top_row)]))
L.ok(after == [14, 14, 14, 18], f'tile beyond the left end of the top row gives {after}')
L.ok([[len([t for t in neighbors_empty(s) if sum((t[0] + dx, t[1] + dy) in set(s) for dx, dy in N4) == k])
       for k in (1, 2, 3, 4)] for s in st] == [[12, 0, 0, 0], [6, 3, 0, 0], [9, 0, 1, 0], [12, 0, 0, 1]],
     'neighbor counts of empty positions as the guide describes (U has no two-neighbor position)')
fr = st[3]
L.ok(perimeter(fr) == 16 and perimeter(fr + [(1, 1)]) == 12, 'frame: 12 outside + 4 inside = 16; filled 12')

# ------------------------------------------------------------- page 10
L.out('\n=== p.10 Grades 2-3 Problems 3-4')
for rows_, e_want in (((8, 2), 10), ((7, 3), 11), ((6, 4), 12), ((5, 5), 13)):
    sh = from_rows(rows_)
    L.ok(shared(sh) == e_want and perimeter(sh) == 40 - 2 * e_want, f'rows {rows_}: e={shared(sh)}, P={perimeter(sh)}')

# ------------------------------------------------------------- page 11
L.out('\n=== p.11 Grades 2-3 Problem 5')
given = [fig(11, c)['cells'] for c in ('Given top left', 'Given top right', 'Given bottom left', 'Given bottom right')]
g23p5 = X['g23'][4]['shapes']
by_pos = sorted(g23p5, key=lambda s: (s['y_mm'] > 110, s['x_mm']))
L.ok([canon(g) for g in given] == [canon(s['cells']) for s in by_pos],
     'guide "given" figures match the student page in reading order')
L.ok([perimeter(g) for g in given] == [18, 18, 12, 16] and [shared(g) for g in given] == [7, 7, 10, 8],
     'boundaries 18, 18, 12, 16; shared sides 7, 7, 10, 8')
n1, n2 = fig(11, 'New staircase')['cells'], fig(11, 'New bent path')['cells']
L.ok(all(len(x) == 8 and shared(x) == 7 and longest_run(x) <= 3 for x in (n1, n2))
     and bbox(n1) == (5, 4) and bbox(n2) == (3, 4) and canon(n1) != canon(n2),
     f'new shapes: 8 tiles, e=7, longest runs {longest_run(n1)}, {longest_run(n2)}; boxes {bbox(n1)}, {bbox(n2)}')

# ------------------------------------------------------------- page 12
L.out('\n=== p.12 Grades 2-3 Problem 6')
last = fig(12, '-4: 7 starting tiles')
L.ok(bbox(last['cells']) == (3, 3) and len(set(sq) - set(norm(last['cells']))) == 2
     and (1, 1) in set(sq) - set(norm(last['cells'])) and last['added'] == [(1, 1)]
     and holes(last['cells']) == 1
     and holes(last['cells'], eight=True) == 0,
     'the -4 start is the 3x3 frame missing its centre and one corner; its centre is point-sealed')
L.ok([perimeter(fig(12, c)['cells']) for c in ('+2:', '0:', '-2:', '-4:')] == [4, 8, 12, 16]
     and [perimeter(fig(12, c)['cells'] + fig(12, c)['added']) for c in ('+2:', '0:', '-2:', '-4:')] == [6, 8, 10, 12],
     'start perimeters 4, 8, 12, 16; after 6, 8, 10, 12')
# chessboard argument: no connected set of 6 or fewer cells contains all four neighbors of an empty cell
bad = []


def cb6(p):
    S = set(p)
    for t in neighbors_empty(S):
        if all((t[0] + dx, t[1] + dy) in S for dx, dy in N4):
            bad.append(show(p))


redelmeier(6, cb6)
L.ok(not bad, 'no legal start of <= 6 tiles surrounds an empty cell on all four sides')

# ------------------------------------------------------------- page 13
L.out('\n=== p.13 Grades 4-5 Problem 1')
pairs = {n: [f['cells'] for f in G if f['page'] == 13 and f['caption'].startswith(f'{n} tiles')] for n in (7, 10, 13)}
for n, (a, b) in pairs.items():
    L.ok(canon(a) != canon(b) and perimeter(a) == perimeter(b) == 2 * math.ceil(2 * math.sqrt(n))
         and intervals(a) == sum(rows_cols(a)) and intervals(b) == sum(rows_cols(b)),
         f'{n} tiles: two different minimum shapes, rows/columns single runs')
a, b = pairs[13]
deg = [min(sum((x + dx, y + dy) in set(s) for dx, dy in N4) for x, y in s) for s in (a, b)]
L.ok(deg == [1, 2], f'13 tiles: least tile degree {deg} (first has a one-neighbor tile, second not)')

# ------------------------------------------------------------- page 14
L.out('\n=== p.14 Grades 4-5 Problem 2')
three = [fig(14, c)['cells'] for c in ('Bent row', 'Branch', 'Point-sealed hole')]
L.ok(all(len(t) == 12 and shared(t) == 11 and perimeter(t) == 26 and min(bbox(t)) > 1 for t in three),
     'three non-straight twelve-tile trees with P = 26')
h = three[2]
S = set(h)
L.ok((1, 1) not in S and all((1 + dx, 1 + dy) in S for dx, dy in N4) and (0, 0) not in S
     and (1, 0) in S and (0, 1) in S,
     'centre (1,1) empty with four side neighbors; upper-left (0,0) empty; (1,0),(0,1) meet at a corner')
inner = sum(1 for dx, dy in N4 if (1 + dx, 1 + dy) in S)
L.ok(holes(h) == 1 and holes(h, eight=True) == 0 and inner == 4 and perimeter(h) - inner == 22,
     'hole if diagonal contact seals (4 inner + 22 outer edges); no hole if a corner gap leaks')

# ------------------------------------------------------------- page 15
L.out('\n=== p.15 Grades 4-5 Problem 3')
first = fig(15, '12 tiles, 4 by 5 span, P = 18')['cells']
second = fig(15, '12 tiles, 4 by 5 span, P = 20')['cells']
fs = set(norm(first))
bottom_y = max(y for _, y in fs)
right_bottom = max(x for x, y in fs if y == bottom_y)
moved = (fs - {(right_bottom, bottom_y)}) | {(4, 1)}
L.ok(sorted(moved) == sorted(norm(second)) and connected(second) and rows_cols(second) == (4, 5),
     'second construction = first with its bottom-row right tile moved to the far right of row 2')
L.ok(intervals(second) == 4 + 5 + 1, 'second construction: one extra run (row 2), columns all single runs')

# ------------------------------------------------------------- page 16/17
L.out('\n=== pp.16-17 Grades 4-5 Problems 4-6')
for n, P in ((12, 14), (13, 16), (17, 18), (20, 18), (21, 20)):
    f = fig(16, f'{n} tiles: P = {P}')
    L.ok(intervals(f['cells']) == sum(rows_cols(f['cells'])), f'{n} tiles: every row/column one run')
for n, base in ((37, (6, 6)), (50, (7, 7)), (73, (9, 8))):
    f = fig(17, f'{n} squares')
    cs = set(f['cells'])
    w, hh = base
    rect = None
    for x0 in range(0, 3):
        for y0 in range(0, 3):
            for (ww, h2) in ((w, hh), (hh, w)):
                R = {(x0 + i, y0 + j) for i in range(ww) for j in range(h2)}
                if R <= cs:
                    rect = R
    extra = cs - rect if rect else None
    L.ok(rect is not None and len(extra) == 1 and
         sum((e[0] + dx, e[1] + dy) in rect for e in extra for dx, dy in N4) == 1
         and bbox(f['cells'])[0] <= 11 and bbox(f['cells'])[1] <= 10,
         f'{n}: {w}x{hh} rectangle plus one tile touching one side; fits an 11x10 grid')
for P in range(4, 81, 2):
    s = P // 2
    assert (s // 2) * ((s + 1) // 2) == P * P // 16
L.ok(True, 'floor(s/2)*ceil(s/2) = floor(P^2/16) for every even P from 4 to 80')
L.ok([(s // 2) * ((s + 1) // 2) for s in (12, 14, 17)] == [36, 49, 72],
     'boundary 24, 28, 34 permit at most 36, 49, 72')

# ------------------------------------------------------------- page 3 and 18
L.out('\n=== pp.3, 18 general claims')
ok_int = True
ok_build = True
for n in range(1, 201):
    k = math.isqrt(n)
    if k * k == n:
        want = 4 * k
    elif n <= k * (k + 1):
        want = 4 * k + 2
    else:
        want = 4 * k + 4
    if want != 2 * math.ceil(2 * math.sqrt(n) - 1e-12) or want != 2 * min(r + c for r in range(1, n + 1)
                                                                              for c in range(1, n + 1) if r * c >= n):
        ok_int = False
    # page 3 construction: k-by-k, then a corner-started strip; then k-by-(k+1), then a strip
    if k * k == n:
        cells = [(x, y) for x in range(k) for y in range(k)]
    elif n <= k * (k + 1):
        j = n - k * k
        cells = [(x, y) for x in range(k) for y in range(k)] + [(k, y) for y in range(j)]
    else:
        j = n - k * (k + 1)
        cells = [(x, y) for x in range(k + 1) for y in range(k)] + [(x, k) for x in range(j)]
    if len(set(cells)) != n or not connected(cells) or perimeter(cells) != want:
        ok_build = False
L.ok(ok_int, 'least boundary 4k at k^2, 4k+2 up to k(k+1), 4k+4 up to (k+1)^2 equals 2*ceil(2*sqrt n), n <= 200')
L.ok(ok_build, 'corner-started strip construction attains it for every n <= 200')
L.ok(all((c - r - 1) == (r + 1) * (c - 1) - r * c for r in range(1, 20) for c in range(r + 2, 40)),
     'balancing step (r,c) -> (r+1,c-1) gains c-r-1')
L.ok(perimeter([(0, 0), (0, 1), (1, 1)]) == 8 and perimeter([(0, 0), (1, 0), (2, 0)]) == 8,
     'p.2 launch: three-tile L and row both have boundary 8')
eight_frame = [(x, y) for x in range(3) for y in range(3) if (x, y) != (1, 1)]
L.ok(not has_block(eight_frame) and shared(eight_frame) == 8 and perimeter(eight_frame) == 16,
     'p.18: the eight-tile frame has no 2x2 block, e = 8, P = 16')

# ------------------------------------------------------------ cross-references
L.out('\n=== cross-references')
doc = pymupdf.open(os.path.join(WEEK, 'week-26-facilitator.pdf'))
title = {i: doc[i].get_text().split('\n')[1] if i else '' for i in range(len(doc))}
printed = {i: i for i in range(1, 19)}  # printed page p is PDF index p
refs = {3: 'The three reusable arguments', 5: 'K-1 / Problems 2 and 3', 6: 'K-1 / Problems 4 and 5',
        14: 'Grades 4-5 / Problem 2'}
for p, t in refs.items():
    L.ok(t in doc[p].get_text(), f'printed page {p} is "{t}"')
L.ok('24 by 24 cm' in doc[1].get_text() and 12 * 20 == 240, 'p.1: a 12-by-12 mat of 20 mm tiles is 24 cm')

L.save(os.path.join(HERE, 'check_guide.out'))
