#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 41 (F41-45-v4) in the print PDFs and views.

Grades 4-5 Problem 4 named "the repeated map from page 2", which in the 4-5 return view is
Problem 4's own page. It now names "a repeated map, such as the one with Problem 6"; in the
full packet and in the return view that page holds the copy-labelled map. The slide picture's
line says "a square of four neighboring centers" (page 1 calls a board cell a "small square"),
and Problem 4 has nine record lines, enough for the key's 15-move record of 16 trip words.
Run from the repository root:
    python3 plans/review/checks/week-41/check_critic_fixes.py
Needs PyMuPDF."""
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
PRINT, VIEWS = Y2 / 'week-41', Y2 / 'band-views' / 'week-41'
MM = 25.4 / 72
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


# The key's record: nine slides (each swaps an adjacent perpendicular pair) take RRRUUULLLDDD to
# RRRLLLUUUDDD, then six backtracks (each erases an adjacent opposite pair) leave the empty trip.
INV = dict(zip('RLUD', 'LRDU'))
lift = lambda w: (w.count('R') - w.count('L'), w.count('U') - w.count('D'))
trip, words = 'RRRUUULLLDDD', ['RRRUUULLLDDD']
while 'UL' in trip:                          # slide each L leftward across each U
    i = trip.index('UL')
    trip = trip[:i] + 'LU' + trip[i + 2:]
    words.append(trip)
slides = len(words) - 1
while trip:                                  # erase adjacent opposite pairs
    i = next(i for i in range(len(trip) - 1) if INV[trip[i]] == trip[i + 1])
    trip = trip[:i] + trip[i + 2:]
    words.append(trip)
check(slides == 9 and len(words) - 1 - slides == 6 and words[9] == 'RRRLLLUUUDDD' and len(words) == 16
      and all(lift(w) == (0, 0) for w in words),
      f'RRRUUULLLDDD: {slides} slides and {len(words) - 1 - slides} backtracks to staying at H, 16 trip words, lift (0,0) throughout')
check(lift('RRR') == (3, 0), 'RRR lifts to three cells right, copy (1,0): no allowed move reaches staying at H')

for band, tag, n in (('k-1', 'K-v3', 4), ('grades-2-3', '23-v3', 5), ('grades-4-5', '45-v4', 6)):
    d = pymupdf.open(PRINT / f'week-41-{band}.pdf')
    check(len(d) == n and all(f'Week 41 / F41-{tag}' in p.get_text() for p in d), f'{band}: {n} pages, footer F41-{tag}')

for label, path in (('full packet', PRINT / 'week-41-grades-4-5.pdf'), ('return view', VIEWS / 'week-41-grades-4-5-return.pdf')):
    d = pymupdf.open(path)
    texts = [' '.join(p.get_text().split()) for p in d]
    i4 = next(i for i, t in enumerate(texts) if 'Problem 4:' in t)
    i6 = next(i for i, t in enumerate(texts) if 'Problem 6:' in t)
    check('Use tracing paper on a repeated map, such as the one with Problem 6.' in texts[i4] and 'page 2' not in texts[i4]
          and '(0, 0)' in texts[i6] and '(1, 1)' in texts[i6],
          f'{label}: Problem 4 (page {i4 + 1}) names the map with Problem 6, whose page ({i6 + 1}) holds the copy-labelled map')
    t4 = texts[i4]
    check('a square of four neighboring centers' in t4 and 'small square' not in t4,
          f'{label}: the slide is "a square of four neighboring centers"; no "small square" on that page')
    p = d[i4]
    rules = [dr for dr in p.get_drawings() if abs(dr['rect'].y0 - dr['rect'].y1) < .01 and dr['rect'].width * MM > 150
             and dr['rect'].y0 * MM > 150]
    word = max((l['bbox'][2] - l['bbox'][0]) * MM for b in p.get_text('dict')['blocks'] for l in b.get('lines', [])
               if ''.join(s['text'] for s in l['spans']).count('→') == 3 and len(''.join(s['text'] for s in l['spans'])) == 12)
    per_line = int(180 // (word + 5))
    check(len(rules) == 9 and len(rules) * per_line >= 16,
          f'{label}: Problem 4 has {len(rules)} record lines; a printed 12-arrow word is {word:.0f} mm, so they hold '
          f'{len(rules) * per_line} words at {per_line} a line (the record needs 16)')
g = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-41-facilitator.pdf'))
check('F41-45-v4 has 6 pages' in g and 'F41-45-v3' not in g, 'guide: the key-alignment line names F41-45-v4')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
