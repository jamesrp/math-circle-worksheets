"""Read the Week 74 student diagrams back from the delivered PDF and check them.

For each elevator board (student pp. 1, 2, 4): the dot lattice (29 columns x
5 levels, uniform pitch), coordinate labels -4..24 under the right columns,
level labels 0..4 on the right rows, 'step 2^h' beside level h, the start ring
at (0, 0), the grey column lines that carry a dot vertically, the row lines'
extent, and that no white label backing covers a dot.  The p. 1 worked
example: node labels and U/R/D arrow labels in order, replayed under the rules.
Also checks the guide's stated dot spacing (0.23 in, about 5.84 mm).
Run: python3 check_diagrams.py   (writes check_diagrams.out beside itself)
"""
import re
from collections import defaultdict
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
STUDENT = REPO / 'lowell-math-circle-year-2' / 'week-74' / 'week-74-students.pdf'

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def spans(page):
    res = []
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for s in line['spans']:
                if s['text'].strip():
                    res.append((s['text'].strip(), pymupdf.Rect(s['bbox']), s['size']))
    return res


def close(a, b, tol=0.6):
    return abs(a - b) <= tol


doc = pymupdf.open(str(STUDENT))
check(doc.page_count == 4, f'student PDF has {doc.page_count} pages')

for pno in (0, 1, 3):
    page = doc[pno]
    say(f'\n== Board on student p. {pno + 1}')
    dr = page.get_drawings()
    dots = [g['rect'] for g in dr if g['type'] == 'f' and close(g['rect'].width, 2, .1)
            and close(g['rect'].height, 2, .1) and g.get('fill') == (0.0, 0.0, 0.0)]
    cx = sorted({round((r.x0 + r.x1) / 2, 2) for r in dots})
    cy = sorted({round((r.y0 + r.y1) / 2, 2) for r in dots})
    check(len(dots) == 145 and len(cx) == 29 and len(cy) == 5,
          f'{len(dots)} dots in {len(cx)} columns x {len(cy)} rows (want 29 x 5)')
    dx = [b - a for a, b in zip(cx, cx[1:])]
    dy = [b - a for a, b in zip(cy, cy[1:])]
    check(max(dx) - min(dx) < .05 and close(sum(dx) / len(dx), .23 * 72, .05),
          f'column pitch {sum(dx) / len(dx):.3f} pt = {sum(dx) / len(dx) / 72:.4f} in '
          f'= {sum(dx) / len(dx) / 72 * 25.4:.2f} mm (guide: 0.23 in, 5.84 mm)')
    check(max(dy) - min(dy) < .05, f'row pitch uniform {dy[0]:.2f} pt')
    full = all(any(close((r.x0 + r.x1) / 2, x) and close((r.y0 + r.y1) / 2, y)
                   for r in dots) for x in cx for y in cy)
    check(full, 'every column has a dot on every level (complete lattice)')
    col = {c: -4 + i for i, c in enumerate(cx)}         # pdf x -> coordinate
    lev = {y: 4 - i for i, y in enumerate(cy)}          # pdf y (top down) -> level
    S = spans(page)
    # coordinate labels: numbers just below the level-0 row
    y0 = cy[-1]
    labs = [(t, r) for t, r, s in S if re.fullmatch(r'-?\d+', t) and 0 < r.y0 - y0 < 15]
    okl = len(labs) == 15
    for t, r in labs:
        mid = (r.x0 + r.x1) / 2
        if t.startswith('-'):        # minus sign widens the box to the left
            mid = r.x1 - (r.x1 - r.x0) * 0.35
        c = min(cx, key=lambda x: abs(x - mid))
        okl &= col[c] == int(t) and abs(c - mid) < 3
    check(okl and sorted(int(t) for t, r in labs) == list(range(-4, 25, 2)),
          'coordinate labels -4,-2,...,24 sit under their own columns')
    # level labels: left of the lattice, vertically centred on the rows
    llabs = [(t, r) for t, r, s in S if re.fullmatch(r'[0-4]', t) and r.x1 < cx[0] - 5]
    okv = len(llabs) == 5
    for t, r in llabs:
        y = min(cy, key=lambda v: abs(v - (r.y0 + r.y1) / 2))
        okv &= lev[y] == int(t) and abs(y - (r.y0 + r.y1) / 2) < 3
    check(okv, 'level labels 0..4 are on their own rows')
    # step labels: 'step' span followed by its number, just above level h
    steps = []
    for i, (t, r, s) in enumerate(S):
        if t == 'step' and s < 9:
            num = next(tt for tt, rr, ss in S[i + 1:] if re.fullmatch(r'\d+', tt))
            y = min(cy, key=lambda v: abs(v - r.y1) if v > r.y1 else 1e9)
            steps.append((lev[y], int(num)))
    check(sorted(steps) == [(h, 2 ** h) for h in range(5)],
          f'step labels by level {sorted(steps)} (want step 2^h on level h)')
    # start ring
    rings = [g['rect'] for g in dr if g['type'] == 's' and close(g['rect'].width, 6, .2)]
    okr = len(rings) == 1 and col[min(cx, key=lambda x: abs(x - (rings[0].x0 + rings[0].x1) / 2))] == 0 \
        and lev[min(cy, key=lambda y: abs(y - (rings[0].y0 + rings[0].y1) / 2))] == 0
    check(okr, 'start ring is at coordinate 0, level 0')
    # grey column lines
    grey = [g['rect'] for g in dr if g['type'] == 's' and g['rect'].width < .1
            and g['rect'].height > 100]
    okg = len(grey) == 29 and all(any(close(r.x0, x) for r in grey) for x in cx) and \
        all(close(r.y0, cy[0]) and close(r.y1, cy[-1]) for r in grey)
    check(okg, '29 grey column lines join each column from level 0 to level 4')
    # row lines
    rows = [g['rect'] for g in dr if g['type'] == 's' and g['rect'].height < .1
            and g['rect'].width > 400 and g.get('color') == (0.0, 0.0, 0.0)
            and any(close(g['rect'].y0, y) for y in cy)]
    heads = [g['rect'] for g in dr if g['type'] == 'fs'
             and any(close((g['rect'].y0 + g['rect'].y1) / 2, y) for y in cy)]
    okrow = len(rows) == 5 and len(heads) == 10 and all(r.x0 < cx[0] and r.x1 > cx[-1] for r in rows)
    check(okrow, '5 row lines extend past both end columns (arrowheads: continuation)')
    # white label backings must not cover dots
    whites = [g['rect'] for g in dr if g['type'] == 'f' and g.get('fill') == (1.0, 1.0, 1.0)]
    hidden = [(col[x], lev[y]) for x in cx for y in cy
              if any(w.contains(pymupdf.Point(x, y)) for w in whites)]
    check(not hidden, f'{len(whites)} white label backings cover no dot {hidden}')

# worked example on p. 1
say('\n== Worked example, student p. 1')
page = doc[0]
S = spans(page)
nodes = defaultdict(dict)
for t, r, s in S:
    if 150 < r.y0 < 182 and re.fullmatch(r'\d', t):
        x = round((r.x0 + r.x1) / 2)
        kind = 'coord' if r.y0 < 167 else 'level'
        nodes[kind][x] = int(t)
cs = [v for k, v in sorted(nodes['coord'].items())]
ls = [v for k, v in sorted(nodes['level'].items())]
moves = [t for t, r, s in sorted(S, key=lambda z: z[1].x0)
         if t in 'URD' and len(t) == 1 and 150 < r.y0 < 166]
check(cs == [1, 1, 3, 3] and ls == [0, 1, 1, 0] and moves == ['U', 'R', 'D'],
      f'example nodes {list(zip(cs, ls))}, arrow labels {moves}')
x, h, ok = 1, 0, True
for m, (c2, l2) in zip(moves, list(zip(cs, ls))[1:]):
    x, h = (x, h + 1) if m == 'U' else (x, h - 1) if m == 'D' else (x + 2 ** h, h)
    ok &= (x, h) == (c2, l2)
check(ok, 'replaying U, R, D under the rules from (1,0) gives every printed node')

say('\nRESULT:', 'all checks pass' if not FAIL else f'{len(FAIL)} FAIL(s)')
(HERE / 'check_diagrams.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
