#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 60 in the print PDFs.

The guide (W60-FAC-v3) gives KK11's two pairs a kit each (five kits in all), 30 linking
cubes per pair, and a page 1 and pages 2 and 6 per pair; the student packet stays W60-S-v3.
Also recomputes why 30 cubes per pair suffice: a pair builds one first-offer row's take and
pass towers at a time, and the largest pair of towers (first 6: 18 and 10) uses 28 cubes.
Run from the repository root:
    python3 plans/review/checks/week-60/check_critic_fixes.py
Needs PyMuPDF."""
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


# Take: the first offer three times; pass: the bag's three tickets once each.
rows = [(bag, first, 3 * first, sum(bag)) for bag, firsts in (((0, 4, 6), (0, 4, 6)), ((0, 3, 6), (3,))) for first in firsts]
need = max(t + p for _, _, t, p in rows)
check(need == 28 <= 30, f'largest row of towers uses {need} cubes, within 30 per pair')

G = pymupdf.open(Y2 / 'week-60' / 'week-60-facilitator.pdf')
g = ' '.join(flat(p) for p in G)
check(len(G) == 8 and all('W60-FAC-v4' in flat(p) for p in G), 'guide: 8 pages, footer W60-FAC-v4 (v3 plus the roster-label fix)')
check('Five playing kits: three older-table kits and two for K–1, one per pair.' in g and 'Four playing kits' not in g, 'guide: five kits, two for KK11')
check('Each K–1 pair also needs 30 linking cubes for towers, 60 in all.' in g, 'guide: 30 cubes per KK11 pair')
check('Seven older children, one per K–1 pair and one spare 10' in g, 'guide: page 1 for each KK11 pair (10 sheets)')
check('K–1 tower pages, one of each per pair, used uncut 4' in g, 'guide: pages 2 and 6 for each KK11 pair (4 sheets)')
check('five simultaneous kits' in g and 'four simultaneous kits' not in g, 'guide: rehearse five kits')
old = pymupdf.open(Y2 / 'week-60' / 'archive-before-critic-fixes-2026-10-23' / 'week-60-facilitator.pdf')
check(all('W60-FAC-v2' in flat(p) for p in old), 'archived guide is W60-FAC-v2')
S = pymupdf.open(Y2 / 'week-60' / 'week-60-students.pdf')
check(len(S) == 8 and all('W60-S-v3' in flat(p) for p in S), 'students unchanged: 8 pages, W60-S-v3')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
