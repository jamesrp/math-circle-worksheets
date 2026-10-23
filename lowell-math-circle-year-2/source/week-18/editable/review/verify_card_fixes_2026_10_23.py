#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes for Week 18.

    python3 review/verify_card_fixes_2026_10_23.py [build folder]

Reads the built PDFs (default build/, as written by build.sh) and the guide source in
facilitator-src/. Checks, independently of the drawing code:
  - page 1 of every band: no heading or narrating sentences, the folder sentence and
    the practice row kept, and the K-1 definition of a key;
  - Problem 1 starts at the same height as Problems 2-6 in every band;
  - K-1 Problem 5: the new wording, two square strips under each triangle row, the
    triangle rows read back from the page, and the five partners of every four-counter
    row (with 1111 for 0100) against the guide's lists;
  - Grades 2-3 Problem 5 and Grades 4-5 Problem 2 no longer restate the one-change rule;
  - the guide: the launch's reveal, roles and no-change send, counters and 1-inch cells,
    the hour, the p. 3 wording, the route note and no leftover process notes;
  - v4 footers and page counts.
"""
import itertools
import json
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
CM = 2.54 / 72
fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


def flat(page):
    return ' '.join(page.get_text().split())


BANDS = {'k-1': 'K', 'grades-2-3': '23', 'grades-4-5': '45'}
docs = {b: pymupdf.open(BUILD / f'{b}.pdf') for b in BANDS}

# ------------------------------------------------------------------ page 1
for band, doc in docs.items():
    t = flat(doc[0])
    cut = [s for s in ('Example: a practice row', 'The receiver sees only this row.',
                       'The changer may also leave the row as it is.') if s in t]
    kept = all(s in t for s in ('In the game, the start row and the changed position stay hidden behind the folder.',
                                'Start row', 'Final row', 'Receiver', 'folder'))
    key = 'A key gives each picture a different row, all the same length.' in t
    check(not cut and kept and (key or band != 'k-1'),
          f'{band} p. 1: heading and two narrating sentences cut, practice row and folder sentence kept'
          + (', key defined' if band == 'k-1' else ''))

# ------------------------------------------------- Problem 1 at the top
for band, doc in docs.items():
    tops = []
    for p in doc:
        for w in p.get_text('words'):
            if w[4] == 'Problem':
                tops.append(round(w[1] * CM, 2))
                break
    check(len(tops) == 6 and max(tops) - min(tops) < .05,
          f'{band}: every problem starts {tops[0]:.2f} cm from the top of its page')

# ------------------------------------------------------------ K-1 Problem 5
p5 = docs['k-1'][5]
t = flat(p5)
check('Problem 5: For each triangle row, find every square row that always works. Use more paper if needed.' in t
      and 'both kinds' not in t, 'K-1 P5: the new wording, without "use both kinds of counter"')
dr = p5.get_drawings()
icons = {'triangle': [], 'square': []}
for d in dr:
    k = tuple(i[0] for i in d['items'])
    w, h = (d['rect'].x1 - d['rect'].x0) * CM, (d['rect'].y1 - d['rect'].y0) * CM
    if k == ('l', 'l', 'l') and .6 < w < .75:
        icons['triangle'].append(d['rect'].y0 * CM)
    if k in (('re',), ('l',) * 4) and abs(w - .68) < .02 and abs(h - .68) < .02:
        icons['square'].append(d['rect'].y0 * CM)
tri, sq = sorted(icons['triangle']), sorted(icons['square'])
groups = [[s for s in sq if a < s < b] for a, b in zip(tri, tri[1:] + [99])]
check(len(tri) == 2 and [len(g) for g in groups] == [2, 2],
      f'K-1 P5: {len(tri)} triangle rows, each followed by {[len(g) for g in groups]} square strips')
rows = []
for y in tri:
    circles = sorted((d['rect'].x0, d.get('fill')) for d in dr
                     if tuple(i[0] for i in d['items']) == ('c',) * 4 and abs(d['rect'].y0 * CM - (y - .2)) < .5)
    rows.append(''.join('1' if f == (0.0, 0.0, 0.0) else '0' for _x, f in circles))
check(rows == ['0011', '0100'], f'K-1 P5: triangle rows read from the page {rows}')


def dist(a, b):
    return sum(x != y for x, y in zip(a, b))


def partners(a):
    return sorted(b for b in map(''.join, itertools.product('01', repeat=len(a))) if dist(a, b) >= 3)


every = {a: partners(a) for a in map(''.join, itertools.product('01', repeat=4))}
g = json.loads((ROOT / 'facilitator-src' / 'guide.json').read_text())
guide = ' '.join(e if isinstance(e, str) else e.get('h', '') for p in g['pages'] for e in p['elements'] if not isinstance(e, dict) or 'h' in e)
lists = {a: sorted(re.search(rf'For triangle {a}, the square may be ([01, or]+)\.', guide).group(1).replace(' or', '').split(', '))
         for a in rows}
check(all(len(v) == 5 for v in every.values()) and lists == {a: every[a] for a in rows} and '1111' in lists['0100'],
      f'K-1 P5: every four-counter row has exactly five partners; the guide lists {lists} match, 1111 included')

# ------------------------------------------------- one-change rule restated
for band, pno, n in (('grades-2-3', 5, 5), ('grades-4-5', 2, 2)):
    t = flat(docs[band][pno])
    check(f'Problem {n}:' in t and 'after zero or one change' not in t and 'that always lets the receiver' in t,
          f'{band} P{n}: no restated one-change rule')

# ------------------------------------------------------------------ guide
gpdf = pymupdf.open(BUILD / 'facilitator-guide.pdf')
gt = ' '.join(flat(p) for p in gpdf)
table = next(e['table'] for e in g['pages'][1]['elements'] if isinstance(e, dict) and 'table' in e)
spans = [tuple(map(int, r[0].split('-'))) for r in table[1:]]
work = sum(b - a for (a, b), r in zip(spans, table[1:]) if r[1].startswith(('K-1', 'Choose')))
route = json.loads((ROOT / 'facilitator-src' / 'route-note.json').read_text())['notes'][0][1]
claims = {
    'reveal after the answer, never before': 'Before the receiver answers, never reveal whether a change occurred.' in gt
        and 'After the receiver answers, show the picture; everyone checks the answer and counts the changed counters.' in gt,
    'pair roles': 'In a pair, one child sends and changes, the other receives' in gt,
    'a no-change send in the launch': 'one with a turned counter and one left as it is' in gt,
    'red/yellow counters and the filled color named': "red/yellow counters work; the launch says which color is filled" in gt,
    'strip cells at least 1 inch, printed strips as records': 'at least 1 inch (2.54 cm)' in gt and 'printed strips are then records' in gt,
    f'hour: 5-minute run, {work} minutes at the tables': spans[0] == (0, 5) and 35 <= work <= 40 and spans[-1][1] <= 60
        and all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1)),
    'p. 3: revealing the original before the answer': 'revealing the original before the receiver answers' in gt,
    'route note (math check 1)': 'K-1 can test two-counter keys and collect every reliable three-counter key (P3-4)' in route
        and 'Grades 2-3 can return to the shortest-key and every-balanced-key arguments (P3-4)' in route,
    'no process notes': not re.search(r'FINAL|mixed|This revision adds', gt),
    'guide names the v4 packets': 'W18-K-v4, W18-23-v4, and W18-45-v4' in gt,
}
for k, v in claims.items():
    check(v, f'guide: {k}')
check(len(gpdf) == 11, f'guide: {len(gpdf)} pages, as before')

# ---------------------------------------------------------------- footers
for band, tag in BANDS.items():
    doc = docs[band]
    check(len(doc) == 7 and all(f'Week 18 / W18-{tag}-v4' in p.get_text() for p in doc),
          f'{band}: seven pages, every footer W18-{tag}-v4')

print(f'\n{len(fails)} failures' if fails else '\nAll card-fix checks pass.')
sys.exit(1 if fails else 0)
