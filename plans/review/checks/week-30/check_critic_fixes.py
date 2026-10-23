#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 30 in the print PDFs.

Grades 4-5 Problem 5 (page 4) asks for "the largest number of different positive targets any
three-weight kit can balance, even with gaps" (F30-45-v4); "the most any kit can balance" could be
read as the largest target, which is unbounded. The guide's materials snap "5, 6, 11 or another
weight", not 7, which the kit already has. K-1 and Grades 2-3 stay v3. Also recomputes: the most
different positive targets of any three-weight kit is 13 (search to 40), reached by 1, 3, 9; the
largest balanced target is unbounded (100, 200, 400 balance 700). Run from the repository root:
    python3 plans/review/checks/week-30/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import product
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def flat(page):
    return ' '.join(page.get_text().split())


def targets(kit):
    """Positive targets: each weight off, opposite the target (+) or beside it (-)."""
    return {s for s in (sum(c * w for c, w in zip(cs, kit)) for cs in product((-1, 0, 1), repeat=len(kit))) if s > 0}


best = max(len(targets((a, b, c))) for a in range(1, 41) for b in range(a + 1, 41) for c in range(b + 1, 41))
check(best == 13 and len(targets((1, 3, 9))) == 13, 'at most 13 different positive targets, reached by 1, 3, 9')
check(max(targets((100, 200, 400))) == 700, 'the largest target alone has no limit: 100, 200, 400 balance 700')

U = pymupdf.open(Y2 / 'week-30' / 'week-30-grades-4-5.pdf')
check(len(U) == 5 and all('F30-45-v4' in flat(p) for p in U), 'Grades 4-5: 5 pages, footer F30-45-v4')
u4 = flat(U[3])
check('What is the largest number of different positive targets any three-weight kit can balance, even with gaps? Explain why none can do better.' in u4
      and 'the most any' not in u4, '4-5 P5: the largest number of different positive targets')
old = pymupdf.open(Y2 / 'week-30' / 'archive-before-critic-fixes-2026-10-23' / 'week-30-grades-4-5.pdf')
same = [flat(a).replace('F30-45-v4', 'F30-45') == flat(b).replace('F30-45-v3', 'F30-45') for a, b in zip(U, old)]
check(same == [True, True, True, False, True], f'only page 4 changed above the footer {same}')
for band, tag in (('k-1', 'F30-K-v3'), ('grades-2-3', 'F30-23-v3')):
    D = pymupdf.open(Y2 / 'week-30' / f'week-30-{band}.pdf')
    check(all(tag in flat(p) for p in D), f'{band} unchanged at {tag}')
G = ' '.join(flat(p) for p in pymupdf.open(Y2 / 'week-30' / 'week-30-facilitator.pdf'))
check('Snap new sticks when a child chooses 5, 6, 11 or another weight.' in G and '5, 6, 7, 11' not in G, 'guide: snap 5, 6, 11 (7 is in the kit)')
check('1, 2, 3, 4, 7, 8, 9 and 10 units' in G, 'guide: the kit has a 7 stick')
F = pymupdf.open(Y2 / 'band-views' / 'week-30' / 'week-30-grades-4-5-return.pdf')
check(any('largest number of different positive targets' in flat(p) for p in F), '4-5 return view carries the new wording')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
