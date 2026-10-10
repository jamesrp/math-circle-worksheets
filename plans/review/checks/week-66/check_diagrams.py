#!/usr/bin/env python3
"""Week 66 diagram check: reads the delivered student PDF's vector drawings.

For every street (row of lamp circles) it recovers the position labels, the lit
lamps and the walker marker, then compares the decoded state with the state the
problem needs. It also checks circles are round, equally spaced, labelled
-4..4 in order, and measures the large-lamp diameter quoted by the guide.
Run: python3 check_diagrams.py  (finds the repository four folders up).
"""
from pathlib import Path
import pymupdf

REPO = Path(__file__).resolve().parents[4]
PDF = REPO / 'lowell-math-circle-year-2/week-66/week-66-students.pdf'
PT_MM = 25.4 / 72
fails = checks = 0


def ok(cond, msg):
    global fails, checks
    checks += 1
    fails += not cond
    print(('PASS ' if cond else 'FAIL ') + msg)


doc = pymupdf.open(PDF)
ok(len(doc) == 4, f'{len(doc)} student pages')
decoded = {}
for pno, page in enumerate(doc, 1):
    dr = page.get_drawings()
    circles = []  # (cx, cy, r, filled_black)
    for d in dr:
        kinds = [it[0] for it in d['items']]
        if kinds == ['c'] * 4:
            r = d['rect']
            circles.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width, r.height,
                            d.get('fill') == (0.0, 0.0, 0.0)))
    tris = []
    for d in dr:
        if [it[0] for it in d['items']] == ['l', 'l', 'l'] and d.get('fill') == (0.0, 0.0, 0.0):
            r = d['rect']
            tris.append(((r.x0 + r.x1) / 2, r.y1))
    words = page.get_text('words')
    # group circles into rows by centre y
    rows = {}
    for c in circles:
        rows.setdefault(round(c[1], 1), []).append(c)
    for y in sorted(rows):
        row = rows[y]
        whites = sorted({round(c[0], 2): c for c in row if not c[4]}.values())
        xs = sorted({round(c[0], 2) for c in row})
        w = row[0][2]
        # labels: numeric words just below each circle centre
        labels = []
        for x in xs:
            cand = [wd for wd in words if abs((wd[0] + wd[2]) / 2 - x) < 3 and 0 < wd[1] - y < w / 2 + 14]
            labels.append(cand[0][4] if cand else '?')
        lit = sorted(int(labels[xs.index(round(c[0], 2))]) for c in row if c[4])
        walker = [t for t in tris if abs(t[1] - (y - w / 2)) < 12 and xs[0] - 3 < t[0] < xs[-1] + 3]
        wpos = None
        if walker:
            i = min(range(len(xs)), key=lambda j: abs(xs[j] - walker[0][0]))
            ok(abs(xs[i] - walker[0][0]) < 0.6, f'p{pno} y={y}: walker centred over a lamp (offset {abs(xs[i]-walker[0][0]):.2f} pt)')
            wpos = int(labels[i])
        gaps = [round(b - a, 2) for a, b in zip(xs, xs[1:])]
        round_ok = all(abs(c[2] - c[3]) < 0.01 for c in row)
        key = (pno, len(xs), round(w, 1))
        decoded.setdefault(pno, []).append((y, labels, lit, wpos, w, gaps, round_ok))
        print(f'INFO p{pno} y={y:.0f} n={len(xs)} diam={w*PT_MM:.1f}mm labels={labels} lit={lit} walker={wpos} gap={gaps[0]*PT_MM:.1f}mm')
        ok(round_ok, f'p{pno} y={y:.0f}: lamps are round (w = h)')
        if labels == ['-2', '-1', '0'] * 3:  # launch demo row: three separate 3-lamp streets on one line
            g3 = [gaps[i] for i in (0, 1, 3, 4, 6, 7)]
            ok(max(g3) - min(g3) < 0.05, f'p{pno} y={y:.0f}: equal lamp spacing within each demo street')
        else:
            ok(max(gaps) - min(gaps) < 0.05, f'p{pno} y={y:.0f}: equal lamp spacing')

# Expected decoded diagrams, top to bottom on each page: (labels, lit, walker)
L9 = [str(i) for i in range(-4, 5)]
L3 = ['-2', '-1', '0']
exp = {
    1: [(L3, [], -2), (L3, [], -1), (L3, [-1], -1),  # launch demo: start, after R, after RF
        (L9, [], 0), (L9, [1], 1), (L9, [-1, 1], 1), (L9, [0, 2], 0)],
    2: [(L9, [], 0), (L9, [-2, 0, 2], -2), (L9, [-2, 0, 2], 0), (L9, [-2, 0, 2], 2)],
    3: [(L9, [-1, 0, 1], 0), (L9, [], 0)],
    4: [(L9, [], None), (L9, [], None), (L9, [], None)],
}
names = {1: ['demo start', 'demo after R', 'demo after RF', 'P1 large street', 'P1 A', 'P1 B', 'P1 C'],
         2: ['P2 large street', 'P2 A', 'P2 B', 'P2 C'],
         3: ['P3 target', 'P3 workspace'], 4: ['P4 L blank', 'P4 R blank', 'P4 F blank']}
# demo streets share a y; order them left to right
for pno in exp:
    got = decoded[pno]
    if pno == 1:
        # first row in y holds all three demo streets (9 circles); split by x
        pass
    print(f'INFO page {pno}: {len(got)} circle rows')

# Re-decode page 1 demo row by x clusters
page = doc[0]
dr = page.get_drawings()
demo = sorted([((d['rect'].x0 + d['rect'].x1) / 2, d.get('fill') == (0.0, 0.0, 0.0)) for d in dr
               if [it[0] for it in d['items']] == ['c'] * 4 and d['rect'].width < 6 and d['rect'].y0 < 200])
whites = sorted({round(x, 1) for x, f in demo if not f})
tris = sorted((d['rect'].x0 + d['rect'].x1) / 2 for d in dr
              if [it[0] for it in d['items']] == ['l', 'l', 'l'] and d.get('fill') == (0.0, 0.0, 0.0) and d['rect'].y0 < 200)
streets = [whites[i:i + 3] for i in range(0, 9, 3)]
for k, st in enumerate(streets):
    lit = [L3[i] for i, x in enumerate(st) if any(f and abs(x - dx) < .5 for dx, f in demo)]
    wp = [L3[i] for i, x in enumerate(st) for t in tris if abs(t - x) < .6]
    e = exp[1][k]
    ok(lit == [str(v) for v in e[1]] and wp == [str(e[2])], f'{names[1][k]}: lit {lit}, walker {wp}; expected lit {e[1]}, walker {e[2]}')

for pno in exp:
    rows9 = [r for r in decoded[pno] if r[1] == L9]
    e9 = [e for e in exp[pno] if len(e[0]) == 9]
    nm = [n for n, e in zip(names[pno], exp[pno]) if len(e[0]) == 9]
    ok(len(rows9) == len(e9), f'page {pno}: {len(rows9)} nine-lamp streets (expected {len(e9)})')
    for (y, labels, lit, wpos, w, gaps, _), e, n in zip(rows9, e9, nm):
        ok(labels == e[0] and lit == e[1] and wpos == e[2],
           f'{n}: labels -4..4 = {labels == e[0]}, lit {lit}, walker {wpos}; expected lit {e[1]}, walker {e[2]}')

big = [r for p in decoded.values() for r in p if r[4] > 30]
diam = {round(r[4] * PT_MM, 1) for r in big}
ok(diam == {13.0}, f'large lamp diameter {diam} mm (guide: "about 13 mm")')
ok(len(big) == 4, f'{len(big)} large streets (P1, P2, P3 target, P3 workspace)')
print(f'\n{checks} checks, {fails} failures')
