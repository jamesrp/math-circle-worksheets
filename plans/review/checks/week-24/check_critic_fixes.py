#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 24 (guide only) in the print PDFs.

The guide's card list had no 0 card, though Grades 2-3 Problem 4 offers 0 for A's empty
card, and told adults to write every value in marker while keeping spares erasable for
Grades 4-5 Problem 3, whose decks may repeat a value. It now lists 58 cards (0, 10, 11, 12
added in marker) and has the spares in soft pencil, erased and rewritten for that problem.
Run from the repository root:
    python3 plans/review/checks/week-24/check_critic_fixes.py
Needs PyMuPDF."""
from collections import Counter
from itertools import combinations_with_replacement as cwr, product
import hashlib
import json
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
PRINT, PKG = Y2 / 'week-24', Y2 / 'source' / 'week-24' / 'editable'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def wins(x, y):
    return sum(a > b for a, b in product(x, y))


A, B, C = (2, 4, 9), (1, 6, 8), (3, 5, 7)
cycle = lambda a, b, c: wins(a, b) > wins(b, a) and wins(b, c) > wins(c, b) and wins(c, a) > wins(a, c)
good = [x for x in (0, 2, 4, 9, 10) if cycle((2, x, 9), B, C)]
check(good == [2, 4] and not cycle((2, 0, 9), B, C),
      f'2-3 Problem 4: the choices that keep the cycle are {good}; 0 is offered and fails, so a 0 card is needed to try it')

# Grades 4-5 Problem 3: three decks of three from 1-6, repeats within a deck, no value in two decks,
# each deck beating the next in more than half its 9 pairs.
decks = list(cwr(range(1, 7), 3))
sols = [(a, b, c) for a in decks for b in decks for c in decks
        if not (set(a) & set(b) or set(b) & set(c) or set(a) & set(c))
        and wins(a, b) > 4.5 and wins(b, c) > 4.5 and wins(c, a) > 4.5]
most = max(max(Counter(a + b + c).values()) for a, b, c in sols)
key = ((1, 4, 4), (3, 3, 3), (2, 2, 5))
originals = Counter(A + B + C)
check(key in sols and most == 3 and originals[3] + 1 < 3,
      f'4-5 Problem 3: {len(sols)} constructions; the key\'s B=(3,3,3) needs three 3s, but one original 3 and one copied spare give two; '
      'nine rewritten spares hold any construction')

text = lambda f: ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(f))
s23 = text(PRINT / 'week-24-grades-2-3.pdf')
check('Choose 0, 2, 4, 9, or 10 for A' in s23, 'grades 2-3 print: Problem 4 offers 0')
g = text(PRINT / 'week-24-facilitator.pdf')
check('The room needs 58 cards: 27 originals, 27 spares and the cards 0, 10, 11 and 12, in marker.' in g
      and 3 * 9 + 3 * 9 + 4 == 58 and 'originals in marker, spares in soft pencil' in g
      and 'erase the nine spares and write its decks on them' in g and '57' not in g
      and 'Write each value large in marker' not in g and 'write the 58 cards' in g,
      'guide: 58 cards = 27 + 27 + 4 (0, 10, 11, 12); spares in pencil, rewritten for upper Problem 3; no 57')
man = json.loads((PKG / 'review' / 'reference-manifest.json').read_text())
for band in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator'):
    ref = 'facilitator-guide' if band == 'facilitator' else band
    h = hashlib.sha256((PRINT / f'week-24-{band}.pdf').read_bytes()).hexdigest()
    check(h == man[f'{ref}.pdf']['sha256'] == hashlib.sha256((PKG / 'reference-pdfs' / f'{ref}.pdf').read_bytes()).hexdigest(),
          f'{band}: print copy, reference copy and manifest agree')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
