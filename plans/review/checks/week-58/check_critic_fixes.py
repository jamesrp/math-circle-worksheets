#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 58 in the print PDFs and band slice.

Problem 5 (page 5, headed Grades K-5) asks for a division "so that neither person would
rather have the other's cards" and no longer says "envies" or "envy-free"; the guide's K-1
route uses pages 1 and 5 only, matching its print list and the K-1 band slice. Also
recomputes Problem 5: three equal whole cards admit no division where nobody prefers the
other's tray; with R3 cut in half, each person gets 3/2. Run from the repository root:
    python3 plans/review/checks/week-58/check_critic_fixes.py
Needs PyMuPDF."""
from fractions import Fraction
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


# "Would rather have the other's cards" is envy: the other tray is worth strictly more.
whole = [a for a in product('UV', repeat=3)
         if not any(sum(1 for x in a if x == o) > sum(1 for x in a if x == p) for p, o in (('U', 'V'), ('V', 'U')))]
check(whole == [], 'whole cards: every division leaves someone preferring the other tray')
half = Fraction(1, 2)
check(1 + half == 1 + half == Fraction(3, 2), 'R3 cut in half: one card and a half each, 3/2 against 3/2')

S = pymupdf.open(Y2 / 'week-58' / 'week-58-students.pdf')
check(len(S) == 7 and all('W58-shared-v4' in flat(p) for p in S), 'students: 7 pages, footer W58-shared-v4')
p5 = flat(S[4])
check('Grades K–5' in p5 and "so that neither person would rather have the other’s cards" in p5.replace("'", '’'), 'p. 5 (Grades K-5): "would rather have the other\'s cards"')
check('Can you now make such a division?' in p5 and 'envies' not in p5 and 'envy' not in p5, 'p. 5: no "envies" or "envy-free"')
old = pymupdf.open(Y2 / 'week-58' / 'archive-before-critic-fixes-2026-10-23' / 'week-58-students.pdf')
same = [flat(a).rsplit('Bellingham', 1)[0] == flat(b).rsplit('Bellingham', 1)[0] for a, b in zip(S, old)]
check(same == [True, True, True, True, False, True, True], f'only page 5 changed above the footer {same}')
M = pymupdf.open(Y2 / 'week-58' / 'week-58-materials.pdf')
check(all('W58-materials-v3' in flat(p) for p in M), 'materials unchanged at W58-materials-v3')
G = ' '.join(flat(p) for p in pymupdf.open(Y2 / 'week-58' / 'week-58-facilitator.pdf'))
check('K–1: parent volunteer, two pairs, adult-led on pages 1 and 5.' in G and 'pages 1, 2 and 5' not in G, 'guide: K-1 route on pages 1 and 5')
check('done with the cards (page 2 itself is not needed)' in G, 'guide: Problem 2\'s splits done with the cards')
check('two copies each of pages 1,5 for K–1' in G, 'guide: print list gives K-1 pages 1 and 5')
K = pymupdf.open(Y2 / 'band-views' / 'week-58' / 'week-58-k-1.pdf')
check(len(K) == 2 and 'Problem 1:' in flat(K[0]) and 'Problem 5:' in flat(K[1]) and 'W58-shared-v4' in flat(K[1]), 'K-1 band slice: pages 1 and 5, v4')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
