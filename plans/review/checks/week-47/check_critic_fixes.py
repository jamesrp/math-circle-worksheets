#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 47 (v5) in the print PDFs.

Grades 2-3 and 4-5 Problem 2 print five record rows 0 _ _ _ 2 (the star has exactly three
heights, 0, 1, 2); no word is hyphenated across a line on any student page; the guide no
longer says "one per row". Run from the repository root:
    python3 plans/review/checks/week-47/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import product
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
PRINT = ROOT / 'lowell-math-circle-year-2' / 'week-47'
MM = 72 / 25.4
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


# The star's possible heights: sites 0..4, clues h0=0, h4=2, steps of at most 1, heights >= 0.
heights = sorted({h[2] for h in product(range(5), repeat=5)
                  if h[0] == 0 and h[4] == 2 and all(abs(a - b) <= 1 for a, b in zip(h, h[1:]))})
check(heights == [0, 1, 2], f'the star can be exactly {heights}')

for band, tag, n in (('k-1', 'K', 6), ('grades-2-3', '23', 5), ('grades-4-5', '45', 6)):
    d = pymupdf.open(PRINT / f'week-47-{band}.pdf')
    check(len(d) == n and all(f'Week 47 / F47-{tag}-v5' in p.get_text() for p in d), f'{band}: {n} pages, footer F47-{tag}-v5')
    broken = [(i + 1, ln) for i, p in enumerate(d) for ln in p.get_text().split('\n') if re.search(r'[a-z]-$', ln.strip())]
    check(not broken, f'{band}: no word hyphenated at a line end {broken[:3]}')
    if band != 'k-1':
        page = d[1]
        words = page.get_text('words')
        rows = []
        for dr in page.get_drawings():
            r, f = dr['rect'], dr.get('fill')
            if 11.5 < r.height / MM < 12.5 and 10 < r.width / MM < 24 and f is not None and f[0] < .95:
                inside = ''.join(w[4] for w in words if r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1)
                rows.append((round(r.y0 / MM), inside))
        p2 = sorted(rows)[:10]
        check([v for _, v in p2] == ['0', '2'] * 5, f'{band} p. 2: five record rows 0 _ _ _ 2 ({len(p2) // 2} found)')
        check('Problem 3' in page.get_text(), f'{band} p. 2: Problem 3 keeps its place')
g = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-47-facilitator.pdf'))
check('one per row' not in g and 'two of the five record rows stay empty' in g and 'Student packets v5' in g,
      'guide: no "one per row"; two of five rows stay empty; names the v5 packets')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
