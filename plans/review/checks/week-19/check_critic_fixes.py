#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 19 (guide only) in the print PDFs.

The guide's key for Grades 2-3 Problem 6 said "the problem no longer asks why it is best",
revision history in a key. It now says "Problem 8 asks why". This checks that the packet
supports that sentence (2-3 Problem 6 asks only for a largest collection; Problem 8 asks
why no larger one can work), that the answer six is right, and that the student packets
are still the v3 references. Run from the repository root:
    python3 plans/review/checks/week-19/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
PRINT, PKG = Y2 / 'week-19', Y2 / 'source' / 'week-19' / 'editable'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


cards = [frozenset(c) for r in range(5) for c in combinations('ABCD', r)]
best = max(r for r in range(1, 8) if any(all(not (a <= b or b <= a) for a, b in combinations(s, 2))
                                         for s in combinations(cards, r)))
check(best == 6, f'the largest collection from the sixteen cards has {best} cards')

text = lambda f: ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(f))
s = text(PRINT / 'week-19-grades-2-3.pdf')
p6 = s[s.index('Problem 6:'):s.index('Problem 7:')]
p8 = s[s.index('Problem 8:'):]
check('largest collection you can' in p6 and 'why' not in p6.lower() and 'Explain why no larger collection can work' in p8,
      'grades 2-3: Problem 6 asks for a largest collection without "why"; Problem 8 asks why no larger one works')
g = text(PRINT / 'week-19-facilitator.pdf')
check('Problem 8 asks why, and Problems 7 and 8 supply the universal argument.' in g and 'no longer asks' not in g
      and len(pymupdf.open(PRINT / 'week-19-facilitator.pdf')) == 12,
      'guide: 12 pages; the 2-3 Problem 6 key says "Problem 8 asks why"; no "no longer asks"')
man = json.loads((PKG / 'review' / 'reference-manifest.json').read_text())
for band in ('k-1', 'grades-2-3', 'grades-4-5', 'materials', 'facilitator'):
    ref = 'facilitator-guide' if band == 'facilitator' else band
    h = hashlib.sha256((PRINT / f'week-19-{band}.pdf').read_bytes()).hexdigest()
    check(h == man[f'{ref}.pdf']['sha256'] == hashlib.sha256((PKG / 'reference-pdfs' / f'{ref}.pdf').read_bytes()).hexdigest(),
          f'{band}: print copy, reference copy and manifest agree')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
