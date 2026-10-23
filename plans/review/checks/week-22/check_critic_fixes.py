#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 22 (v6) in the print PDFs.

Problem 1's page 1 asks only for the search with the D marker; the drawing request is
on page 2 alone. Run from the repository root:
    python3 plans/review/checks/week-22/check_critic_fixes.py
Needs PyMuPDF."""
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
PRINT = ROOT / 'lowell-math-circle-year-2' / 'week-22'
OLD = PRINT / 'archive-before-critic-fixes-2026-10-23'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def flat(page):
    return ' '.join(page.get_text().split())


want = {
    'k-1': ('F22-K-v6', 9, 'Put D on each cross. Each time, find a split whose regions meet.',
            'For each place of D, draw the two regions you found and mark a point they share.'),
    'grades-2-3': ('F22-23-v6', 9, 'Put D on each cross. For each position, find a split of A, B, C, and D whose two regions meet.',
                   'For each position of D, draw the two regions of your split and mark a shared point.'),
    'grades-4-5': ('F22-45-v6', 12, 'Put D on each cross. For each position, find a split of A, B, C, and D whose two regions meet.',
                   'For each position of D, draw the two regions of your split and mark a shared point.'),
}
for band, (tag, n, p1, p2) in want.items():
    d = pymupdf.open(PRINT / f'week-22-{band}.pdf')
    old = pymupdf.open(OLD / f'week-22-{band}.pdf')
    check(len(d) == n and all(tag in flat(p) for p in d), f'{band}: {n} pages, footer {tag} on each')
    one, two = flat(d[0]), flat(d[1])
    check(p1 in one, f'{band} p. 1: the search only')
    check('draw' not in one.split('Problem 1:')[1] and 'mark' not in one.split('Problem 1:')[1], f'{band} p. 1: Problem 1 asks for no drawing or mark')
    check(p2 in two, f'{band} p. 2: the drawing request on the record page')
    same = all(flat(a).rsplit('Bellingham', 1)[0] == flat(b).rsplit('Bellingham', 1)[0] for a, b in zip(list(d)[2:], list(old)[2:]))
    check(same and len(old) == n, f'{band}: pages 3-{n} have the same text as v5 above the footer')
g = ' '.join(flat(p) for p in pymupdf.open(PRINT / 'week-22-facilitator.pdf'))
check(all(f'{t}.' in g for t in ('F22-K-v6', 'F22-23-v6', 'F22-45-v6')) and 'v5 student packets' not in g,
      'guide names the v6 packets')
check('Draw each placement on its own board on the record page' in g, 'guide: P1 drawings go on the record page')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
