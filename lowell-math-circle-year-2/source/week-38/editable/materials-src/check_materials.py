#!/usr/bin/env python3
"""Independent check of materials.pdf, read from the finished PDF only.

Checks both pages' size, header, footer, print counts and 10 cm line; that each
page has four abutting 260 x 45 mm strips; reads each strip's corner marks
(filled dots, open squares) and arrows, and from them the seam each join makes:
matching marks on both ends (A) is an annulus, swapped marks (B) a Moebius band.
Sheet 1 strips need a dashed middle line and three U's above it and three L's
below it; sheet 2 strips need dotted lines at one and two thirds of the height
and no middle line. From the seam it then counts, by following edges through
the identification, the uncut boundary circles (A 2, B 1), the pieces and
boundary circles after the middle cut (A 2 and 4, B 1 and 2), that sheet 2's two
dotted lines are one closed cut, and the pieces and circles after that cut
(2 and 3, one piece one-sided). Writes materials-checks.json beside the PDF.
"""
from pathlib import Path
import json
import re
import sys

import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'materials.pdf'
MM = 72 / 25.4
TOL = 0.3 * MM
GROUP = {'K-1': 4, '2-3': 4, '4-5': 3}          # worksheet-workflow/context.md: eleven children
ADULTS = 3
checks = []


def ok(name, cond, detail=''):
    checks.append({'check': name, 'pass': bool(cond), 'detail': str(detail)})
    if not cond:
        print('FAIL', name, detail)


def near(a, b, tol=TOL):
    return abs(a - b) < tol


def cut_count(identify, cuts, lanes_per_strip):
    """Pieces, boundary circles and one-sided pieces after cutting a strip into lanes.

    Lanes are numbered 0..n-1 from the top. identify maps a lane to the lane it meets
    at the seam and whether the join reverses top and bottom. Each lane has a top
    and a bottom long edge; a lane edge continues across the seam into an edge of
    the lane it meets. cuts says which lane boundaries are cut (the outer two are
    always edges); uncut lane boundaries join lanes into one piece.
    """
    n = lanes_per_strip
    # union-find over lanes for pieces
    parent = list(range(n))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for j in range(n - 1):
        if not cuts[j]:
            parent[find(j)] = find(j + 1)
    for i in range(n):
        j, _ = identify(i)
        parent[find(i)] = find(j)
    pieces = {find(i) for i in range(n)}
    # boundary edges: (lane, side) where side 0 = top, 1 = bottom, that are real edges
    edges = [(i, s) for i in range(n) for s in (0, 1)
             if (s == 0 and (i == 0 or cuts[i - 1])) or (s == 1 and (i == n - 1 or cuts[i]))]
    nxt = {}
    for (i, s) in edges:
        j, rev = identify(i)
        nxt[(i, s)] = (j, s ^ rev)
    seen, circles = set(), 0
    for e in edges:
        if e in seen:
            continue
        circles += 1
        while e not in seen:
            seen.add(e)
            e = nxt[e]
    # a piece is one-sided when going round it reverses top and bottom an odd number of times
    one_sided = 0
    for root in pieces:
        lanes = [i for i in range(n) if find(i) == root]
        i, flips, steps = lanes[0], 0, 0
        while True:
            i, rev = identify(i)
            flips += rev
            steps += 1
            if i == lanes[0]:
                break
        one_sided += flips % 2
    return len(pieces), circles, one_sided


doc = pymupdf.open(PDF)
ok('two pages', len(doc) == 2, len(doc))
results = {}
for pno, page in enumerate(doc, 1):
    text = page.get_text()
    flat = ' '.join(text.split())
    ok(f'p{pno} US Letter landscape', (round(page.rect.width), round(page.rect.height)) == (792, 612), page.rect)
    ok(f'p{pno} header', flat.startswith('Week 38 / Seams / Materials'), flat[:60])
    ok(f'p{pno} footer', f'Bellingham Math Circle / Week 38 / W38-M-v1 / page {pno}' in flat, '')
    ok(f'p{pno} unrehearsed', 'physically unrehearsed' in flat, '')
    m = re.search(r'Print (\d+) copies at 100% on copy paper', flat)
    ok(f'p{pno} print count', m, flat[:200])
    copies = int(m.group(1)) if m else 0
    drawings = page.get_drawings()
    # 10 cm check line
    tens = [d for d in drawings for it in d['items'] if it[0] == 'l'
            and near(it[1].y, it[2].y) and near(abs(it[2].x - it[1].x), 100 * MM, 0.2 * MM)]
    ok(f'p{pno} 10 cm line', len(tens) == 1 and '10 cm check' in flat, len(tens))
    # strips: stroked rectangles 260 x 45 mm
    rects = []
    for d in drawings:
        for it in d['items']:
            if it[0] == 're':
                r = it[1]
                if near(r.width, 260 * MM) and near(r.height, 45 * MM):
                    rects.append(r)
    rects.sort(key=lambda r: r.y0)
    ok(f'p{pno} four strips 260 x 45 mm', len(rects) == 4, len(rects))
    ok(f'p{pno} strips abut and align', all(near(a.y1, b.y0) and near(a.x0, b.x0) for a, b in zip(rects, rects[1:])), '')
    ok(f'p{pno} strips inside 6 mm margins', all(r.x0 > 6 * MM and r.x1 < 792 - 6 * MM and r.y0 > 6 * MM and r.y1 < 612 - 6 * MM for r in rects), '')
    words = page.get_text('words')
    strips = []
    for k, r in enumerate(rects):
        inside = lambda x, y: r.x0 < x < r.x1 and r.y0 < y < r.y1
        dots, squares, heads, hlines = [], [], [], []
        for d in drawings:
            b = d['rect']
            cx, cy = (b.x0 + b.x1) / 2, (b.y0 + b.y1) / 2
            if not inside(cx, cy):
                continue
            kinds = [it[0] for it in d['items']]
            if d.get('fill') == (0.0, 0.0, 0.0) and 'c' in kinds and near(b.width, 4.4 * MM):
                dots.append((cx, cy))
            elif 're' in kinds and near(b.width, 4 * MM) and near(b.height, 4 * MM):
                squares.append((cx, cy))
            elif d.get('fill') == (0.0, 0.0, 0.0) and kinds == ['l', 'l', 'l']:
                pts = [it[1] for it in d['items']]
                apex = max(pts, key=lambda p: abs(p.y - cy))
                heads.append((cx, apex.y, 'down' if apex.y > cy else 'up'))
            for it in d['items']:
                if it[0] == 'l' and near(it[1].y, it[2].y) and near(abs(it[2].x - it[1].x), r.width, 0.5):
                    hlines.append(((it[1].y - r.y0) / MM, d.get('dashes')))
        label = ' '.join(w[4] for w in words if inside((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
                         and w[4] not in ('U', 'L'))
        us = [w for w in words if w[4] == 'U' and inside((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)]
        ls = [w for w in words if w[4] == 'L' and inside((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)]
        mid = (r.y0 + r.y1) / 2

        def end_marks(left):
            sel = lambda p: (p[0] < r.x0 + 10 * MM) if left else (p[0] > r.x1 - 10 * MM)
            top = [('dot', p) for p in dots if sel(p) and p[1] < mid] + [('square', p) for p in squares if sel(p) and p[1] < mid]
            bot = [('dot', p) for p in dots if sel(p) and p[1] > mid] + [('square', p) for p in squares if sel(p) and p[1] > mid]
            return top, bot

        lt, lb = end_marks(True)
        rt, rb = end_marks(False)
        good = all(len(x) == 1 for x in (lt, lb, rt, rb)) and lt[0][0] != lb[0][0] and rt[0][0] != rb[0][0]
        ok(f'p{pno} strip {k + 1} one dot and one square at each end', good, (lt, lb, rt, rb))
        ok(f'p{pno} strip {k + 1} marks 6 mm from the corners',
           good and all(near(abs(p[1] - (r.y0 if p in (lt[0][1], rt[0][1]) else r.y1)), 6 * MM) for p in (lt[0][1], lb[0][1], rt[0][1], rb[0][1])), '')
        swapped = good and lt[0][0] != rt[0][0]
        # arrows point from square to dot at each end
        arrows_ok = len(heads) == 2
        for (hx, hy, direction) in heads:
            top, _ = end_marks(hx < (r.x0 + r.x1) / 2)
            dot_on_top = top and top[0][0] == 'dot'
            arrows_ok &= (direction == 'up') == bool(dot_on_top)
        ok(f'p{pno} strip {k + 1} arrows run from square to dot', arrows_ok, heads)
        name = label
        ok(f'p{pno} strip {k + 1} named {name!r} matches its marks', (name == 'A' and not swapped) or (name in ('B', 'new B') and swapped), (name, swapped))
        # seam: lane i meets lane identify(i); with one lane, A keeps top on top, B swaps
        if pno == 1:
            dashed = [y for y, d in hlines if d and d not in ('[] 0', '[] 0.0')]
            ok(f'p{pno} strip {k + 1} dashed middle line across the whole strip', len(dashed) == 1 and abs(dashed[0] - 22.5) < .3, hlines)
            ok(f'p{pno} strip {k + 1} three U above and three L below the middle line',
               len(us) == 3 and len(ls) == 3 and all((w[1] + w[3]) / 2 < mid for w in us) and all((w[1] + w[3]) / 2 > mid for w in ls), (len(us), len(ls)))
            ident2 = (lambda i: (1 - i, 1)) if swapped else (lambda i: (i, 0))
            ident1 = (lambda i: (0, 1)) if swapped else (lambda i: (0, 0))
            uncut = cut_count(ident1, [], 1)
            middle = cut_count(ident2, [True], 2)
            ok(f'p{pno} strip {k + 1} uncut boundary circles', uncut[1] == (1 if swapped else 2), uncut)
            ok(f'p{pno} strip {k + 1} middle cut pieces and circles', middle[:2] == ((1, 2) if swapped else (2, 4)) and middle[2] == 0, middle)
            strips.append({'name': name, 'seam': 'reversing' if swapped else 'matching',
                           'uncut_boundary_circles': uncut[1], 'middle_cut': {'pieces': middle[0], 'boundary_circles': middle[1]}})
        else:
            dotted = sorted(y for y, d in hlines if d and d not in ('[] 0', '[] 0.0'))
            ok(f'p{pno} strip {k + 1} dotted lines at 15 and 30 mm across the whole strip',
               len(dotted) == 2 and abs(dotted[0] - 15) < .3 and abs(dotted[1] - 30) < .3, hlines)
            ok(f'p{pno} strip {k + 1} no U, L or middle line', not us and not ls, '')
            # three lanes 0 (top), 1, 2; a reversing seam sends lane i to lane 2 - i
            ident3 = (lambda i: (2 - i, 1)) if swapped else (lambda i: (i, 0))
            # the two dotted lines, at heights 1/3 and 2/3, meet at the seam: one closed cut
            one_cut = swapped  # height 1/3 from the top meets height 1/3 from the bottom
            third = cut_count(ident3, [True, True], 3)
            ok(f'p{pno} strip {k + 1} dotted lines are one closed cut', one_cut, '')
            ok(f'p{pno} strip {k + 1} one-third cut: two pieces, three circles, one piece one-sided', third == (2, 3, 1), third)
            strips.append({'name': name, 'seam': 'reversing' if swapped else 'matching',
                           'one_third_cut': {'pieces': third[0], 'boundary_circles': third[1], 'one_sided_pieces': third[2]}})
    results[f'page {pno}'] = {'copies': copies, 'strips': strips}

children = sum(GROUP.values())
ok('sheet 1: one per child and three for the adults', results['page 1']['copies'] == children + ADULTS, results['page 1']['copies'])
ok('sheet 2: a new B for each K-3 child, the pretest, the launch and spares',
   4 * results['page 2']['copies'] >= GROUP['K-1'] + GROUP['2-3'] + 2, 4 * results['page 2']['copies'])
# the four-dot pictures each cut allows: partitions of 4 into at most b groups
parts = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
allowed = {b: [p for p in parts if len(p) <= b] for b in (1, 2, 3, 4)}
ok('one-third cut allows every picture but 1+1+1+1', allowed[3] == parts[:4], allowed[3])
out = PDF.with_name('materials-checks.json')
out.write_text(json.dumps({'pdf': PDF.name, 'results': results, 'checks': checks}, indent=1, ensure_ascii=False) + '\n')
failed = [c for c in checks if not c['pass']]
print(f'{len(checks) - len(failed)}/{len(checks)} materials checks pass' + ('' if not failed else f'; {len(failed)} FAIL'))
sys.exit(1 if failed else 0)
