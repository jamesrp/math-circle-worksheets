#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes in the Week 75 student packet (GGT75-S-v3, or v4).

    python3 verify_card_fixes_2026_10_23.py [students.pdf] [previous-students.pdf]

The defaults are ../reference-pdfs/week-75-students.pdf and, when present, the
previous print copy (v2) in the repository's week-75/archive-before-shoulds-2026-10-23/.
Version 2 made fixes 1-3 on pages 3-4; version 3 made shoulds 4-7 on pages 1-2; version 4
(a true minus in page 2's lift-board labels) is checked by verify_minus_signs_2026_10_23.py
and passes here too, since it reads every footer's version from page 1.
Reads the printed PDF's vector data and text (PyMuPDF, `pip install pymupdf`).

  1. Twist words: the 28 words of two to four twists from winding 0 end at windings
     -4..4, and every partial word stays in -4..4 (review card fix 2; math check).
  2. The strip under Problem 4 on page 3: nine equal copies labelled B, copy -4 .. 4,
     a B dot centred at the top of each copy, A centred at the bottom of copy 0,
     dashed copy boundaries, dotted lines at quarter heights; it holds every winding
     the words reach.
  3. The shrunk twist example on page 3: each arrow's shift, in copies, equals its
     height fraction, and the twisted straight route ends one copy right.
  4. Page 4: Problems 6-7 say strand crossings (fix 1); the record column is headed
     Sketch and its rows are at least 0.8 in tall (fix 3).
  5. Pages 1-2 (shoulds 4-7): the opening rules leave taping and feeding to the
     launch; Problem 1 has two sketch boxes, each with A below B; Problem 2's partner
     lays each route with yarn; Problem 3 ends "Explain the difference."
  6. Pages 3-4 differ from the previous packet (v2) only in the footer version.
"""
import sys
from itertools import product
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'reference-pdfs' / 'week-75-students.pdf'
OLD = Path(sys.argv[2]) if len(sys.argv) > 2 else (
    HERE.parents[3] / 'week-75' / 'archive-before-shoulds-2026-10-23' / 'week-75-students.pdf')
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def dashed(pattern):
    """PyMuPDF writes a solid stroke's dash pattern as '[] 0'."""
    return bool(pattern) and not pattern.strip().startswith('[]')


def lines(page):
    out = []
    for dr in page.get_drawings():
        for it in dr['items']:
            if it[0] == 'l':
                out.append(dict(x0=it[1].x, y0=it[1].y, x1=it[2].x, y1=it[2].y,
                                filled=dr.get('fill') is not None, dashes=dashed(dr.get('dashes')),
                                gray=dr.get('color')))
    return out


def rects(page):
    return [dr['rect'] for dr in page.get_drawings()
            if dr.get('fill') is None and [i[0] for i in dr['items']] == ['l'] * 4]


def dots(page):
    out = []
    for dr in page.get_drawings():
        if dr.get('fill') is not None and dr['items'] and dr['items'][0][0] == 'c':
            r = dr['rect']
            out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    return out


def number(token):
    return int(token.replace('−', '-'))


# 1. words
words = [w for n in (2, 3, 4) for w in product((-1, 1), repeat=n)]
finals = {sum(w) for w in words}
partials = {sum(w[:i]) for w in words for i in range(len(w) + 1)}
check(len(words) == 28 and finals == set(range(-4, 5)),
      f'{len(words)} words of two to four twists end at windings {sorted(finals)}')
check(partials <= set(range(-4, 5)), f'every partial word stays in {min(partials)}..{max(partials)}')

doc = pymupdf.open(PDF)
check(len(doc) == 4, f'{PDF.name} has 4 pages ({len(doc)})')
VERSION = next(v for v in ('GGT75-S-v4', 'GGT75-S-v3') if v in doc[0].get_text())
check(all(VERSION in p.get_text() for p in doc), f'every page footer reads {VERSION}')

# 2. the strip
p3 = doc[2]
strip = max(rects(p3), key=lambda r: r.width)
w_in, h_in = strip.width / 72, strip.height / 72
print(f'  strip {w_in:.2f} x {h_in:.2f} in at y {strip.y0:.1f}..{strip.y1:.1f} pt')
top_dots = sorted(d for d in dots(p3) if abs(d[1] - strip.y0) < 1 and strip.x0 < d[0] < strip.x1)
bottom_dots = [d for d in dots(p3) if abs(d[1] - strip.y1) < 1 and strip.x0 < d[0] < strip.x1]
xs = [d[0] for d in top_dots]
gaps = [b - a for a, b in zip(xs, xs[1:])]
cw = sum(gaps) / len(gaps)
check(len(xs) == 9 and max(gaps) - min(gaps) < 0.1, f'nine B dots on the top edge, {cw / 72:.2f} in apart')
check(abs(xs[0] - cw / 2 - strip.x0) < 0.1 and abs(xs[-1] + cw / 2 - strip.x1) < 0.1,
      'each B dot is centred in its copy; the strip is exactly nine copies wide')
L3 = lines(p3)
inside = lambda l: strip.x0 - .5 <= min(l['x0'], l['x1']) and max(l['x0'], l['x1']) <= strip.x1 + .5 \
    and strip.y0 - .5 <= min(l['y0'], l['y1']) and max(l['y0'], l['y1']) <= strip.y1 + .5
dashed_v = sorted(l['x0'] for l in L3 if inside(l) and l['dashes'] and abs(l['x0'] - l['x1']) < .01
                  and abs(abs(l['y1'] - l['y0']) - strip.height) < .1)
mids = [(a + b) / 2 for a, b in zip(xs, xs[1:])]
check(len(dashed_v) == 8 and all(abs(a - b) < 0.1 for a, b in zip(dashed_v, mids)),
      'dashed copy boundaries halfway between B dots')
dotted_h = sorted(round((strip.y1 - l['y0']) / strip.height, 4) for l in L3 if inside(l) and l['dashes']
                  and abs(l['y0'] - l['y1']) < .01 and abs(abs(l['x1'] - l['x0']) - strip.width) < .1)
check(dotted_h == [0.25, 0.5, 0.75], f'dotted lines across the strip at heights {dotted_h}')
labels = []
text = p3.get_text('words')
for x in xs:
    near = sorted((w for w in text if w[3] <= strip.y0 and strip.y0 - w[3] < 8 and w[0] <= x + cw / 2 and w[2] >= x - cw / 2),
                  key=lambda w: w[0])
    tokens = [w[4] for w in near]
    labels.append(number(tokens[-1]) if tokens[:2] == ['B,', 'copy'] and len(tokens) == 3 else None)
check(labels == list(range(-4, 5)), f'labels above the dots read B, copy {labels}')
zero = xs[labels.index(0)] if 0 in labels else None
check(len(bottom_dots) == 1 and zero is not None and abs(bottom_dots[0][0] - zero) < 0.1,
      'A is on the bottom edge, centred under B copy 0')
check(finals | partials <= set(labels), 'every winding the twist words reach has its B copy on the strip')

# 3. the twist example
ex = min(rects(p3), key=lambda r: r.width)
boundary = [l['x0'] for l in L3 if l['dashes'] and abs(l['x0'] - l['x1']) < .01 and ex.x0 < l['x0'] < ex.x1
            and ex.y0 - .5 <= min(l['y0'], l['y1'])]
ecw = boundary[0] - ex.x0
start = [d for d in dots(p3) if abs(d[1] - ex.y1) < 1 and ex.x0 < d[0] < ex.x1][0][0]
arrows = [l for l in L3 if not l['filled'] and not l['dashes'] and abs(l['y0'] - l['y1']) < .01
          and abs(l['x0'] - start) < .1 and l['x1'] > l['x0'] + 1]
tips = [l for l in L3 if l['filled']]
ok = len(arrows) == 4
for a in arrows:
    h = (ex.y1 - a['y0']) / ex.height
    tip = max(t['x0'] for t in tips if abs(t['y0'] - a['y0']) < 2 and t['x0'] > start)
    shift = (tip - start) / ecw
    print(f'  example arrow at height {h:.3f}: shift {shift:.3f} copy')
    ok &= abs(shift - h) < .02
check(ok, f'example ({ex.width / 72:.2f} x {ex.height / 72:.2f} in): four arrows, shift equals height fraction')
route = [l for l in L3 if abs(l['x0'] - start) < .1 and abs(l['y0'] - ex.y1) < .1 and l['x1'] - l['x0'] > 1]
check(len(route) == 1 and abs((route[0]['x1'] - route[0]['x0']) / ecw - 1) < .01,
      'the twisted straight route ends one copy right')

# 4. page 4
t4 = ' '.join(doc[3].get_text().split())
check('Make the number of places where the two strands cross each other as small as possible.' in t4
      and 'remove another of these crossings' in t4, 'Problem 6 asks for places where the two strands cross each other')
check('Fewest strand crossings' in t4 and 'Sketch' in t4 and 'seam-crossing record' not in t4
      and 'crossings between the rims' not in t4, 'table headed Windings / Fewest strand crossings / Sketch')
check('Predict the fewest strand crossings for windings 2 and 7' in t4
      and 'change the fewest strand crossings?' in t4, 'Problem 7 says fewest strand crossings twice')
rule_y = sorted(l['y0'] for l in lines(doc[3]) if abs(l['y0'] - l['y1']) < .01 and l['x1'] - l['x0'] > 400)
table = rule_y[:7]
rows = [(b - a) / 72 for a, b in zip(table, table[1:])]
check(len(rows) == 6 and min(rows) >= 0.8, f'six sketch rows, each at least 0.8 in ({min(rows):.2f} in)')

# 5. pages 1-2
t1 = ' '.join(doc[0].get_text().split())
t2 = ' '.join(doc[1].get_text().split())
check('Each yarn route goes upward from A to B' in t1 and 'Tape' not in t1 and 'spare yarn' not in t1
      and 'Keep the cylinder still' not in t1, 'page 1 rules: no taping, feeding or still-cylinder handling')
cut = max((l for l in lines(doc[0]) if abs(l['y0'] - l['y1']) < .01), key=lambda l: abs(l['x1'] - l['x0']))
below = sorted((d for d in dots(doc[0]) if d[1] > cut['y0'] + 200), key=lambda d: (round(d[0]), d[1]))
pairs = [(below[i], below[i + 1]) for i in range(0, len(below) - 1, 2)]
check(len(below) == 4 and all(abs(b[0] - a[0]) < .1 and abs(abs(b[1] - a[1]) - 72) < .5 for a, b in pairs),
      'Problem 1: two sketch boxes, each with A one inch below B')
check('Same winding, different routes (winding' in t1, 'Problem 1: the boxes are labelled with one shared winding blank')
check('Your partner lays each route on the cylinder with yarn.' in t2 and 'tracing' not in t2,
      'Problem 2: the partner lays each route with yarn')
check('Find a pair that can and a pair that cannot. Explain the difference.' in t2 and 'repeated rectangles to explain' not in t2,
      'Problem 3 ends "Explain the difference."')

# 6. pages 3-4
if OLD.exists():
    old = pymupdf.open(OLD)
    for i in (2, 3):
        a = doc[i].get_text().replace(VERSION, 'GGT75-S-v2')
        check(a == old[i].get_text(), f'page {i + 1} text matches the previous packet apart from the footer version')
        pa, pb = doc[i].get_pixmap(dpi=100), old[i].get_pixmap(dpi=100)
        diff_rows = {y for y in range(pa.height) for x in range(0, pa.width, 1)
                     if abs(pa.pixel(x, y)[0] - pb.pixel(x, y)[0]) > 32} if (pa.width, pa.height) == (pb.width, pb.height) else {-1}
        footer = pa.height * (10.35 / 11)
        check(diff_rows and min(diff_rows) > footer, f'page {i + 1} pixels differ only in the footer band')
else:
    print(f'SKIP pages 3-4: no previous packet at {OLD}')

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
