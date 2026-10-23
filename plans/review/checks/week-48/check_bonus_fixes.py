#!/usr/bin/env python3
"""Week 48 bonus companion, October 23, 2026: the review card's should 11, checked on the
print copies.

Page 2's witness grids were captioned "First pair" and "Third pair", which told children
which pair of range cards is impossible. They are now captioned "Pair:" with a blank, the
pairs are numbered 1-3, and the guide no longer pins the grids to pairs. Run from the
repository root:
    python3 plans/review/checks/week-48/check_bonus_fixes.py
"""
import hashlib
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PRINT, SRC = Y2 / 'week-48', Y2 / 'source' / 'week-48-bonus'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
text = lambda doc: ' '.join(' '.join(p.get_text().split()) for p in doc)

for f in ('week-48-bonus', 'week-48-bonus-facilitator'):
    assert sha(PRINT / f'{f}.pdf') == sha(SRC / 'reference-pdfs' / f'{f}.pdf'), f
old = {'week-48-bonus': '6716015ad1f6bb4041f5cd039e8fad2d5e4fbc1567a1a8488f5ade1ce45a7f6a',
       'week-48-bonus-facilitator': '260b80e9e0957c81beac36393674be9becd49eb3b017fca76afa398831007214'}
for f, h in old.items():
    assert sha(PRINT / 'archive-before-card-fixes-2026-10-23' / f'{f}.pdf') == h, f
print('PASS print copies are the bonus reference PDFs; the October 4 copies are archived unchanged')

student = pymupdf.open(PRINT / 'week-48-bonus.pdf')
guide = pymupdf.open(PRINT / 'week-48-bonus-facilitator.pdf')
s, g = text(student), text(guide)
assert len(student) == 3 and all('Bellingham Math Circle / Week 48 / F48B-S-v2' in p.get_text() for p in student)
assert all('W48-BONUS-FAC-v2' in p.get_text() for p in guide)
print('PASS footers F48B-S-v2 on all 3 student pages and W48-BONUS-FAC-v2 on the guide')

p2 = student[1]
assert 'First pair' not in s and 'Third pair' not in s
words = p2.get_text('words')
pair_words = [w for w in words if w[4] == 'Pair:']
assert len(pair_words) == 2
numbers = sorted((round(w[1]), w[4]) for w in words if w[4] in '123' and w[0] < 70)
assert [n for _, n in numbers] == ['1', '2', '3']
cards = [((2, 8), (4, 9)), ((3, 5), (6, 7)), ((1, 6), (4, 4))]
both = [(max(a[0], b[0]), min(a[1], b[1])) for a, b in cards]
possible = [i + 1 for i, (lo, hi) in enumerate(both) if lo <= hi]
assert both == [(4, 8), (6, 5), (4, 4)] and possible == [1, 3] and len(pair_words) == len(possible)
assert 'matched to the first and third card pairs' not in g
assert 'one for each possible pair (the first and third of the numbered pairs 1-3), each captioned "Pair: ____"' in g
print('PASS should 11: page 2 numbers the card pairs 1-3 and captions its two witness grids "Pair:" with a blank; '
      'pair 2 is the impossible one (at least 6 and at most 5) and pairs 1 and 3 combine to 4-8 and 4-4, one grid '
      'each; the guide no longer names the grids\' pairs on the page')
