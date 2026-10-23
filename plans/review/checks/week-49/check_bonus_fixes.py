#!/usr/bin/env python3
"""Week 49 bonus companion, October 23, 2026: the review card's could 11, checked on the
print copies and by running the directed rule.

Problem 3 asked which start passes 10 "within five rounds"; the first start does so only at
round 5, so the page now says "by round 5", matching the table's rows 0-7. Run from the
repository root:
    python3 plans/review/checks/week-49/check_bonus_fixes.py
"""
import hashlib
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PRINT, SRC = Y2 / 'week-49', Y2 / 'source' / 'week-49-bonus'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
text = lambda doc: ' '.join(' '.join(p.get_text().split()) for p in doc)

for f in ('week-49-bonus', 'week-49-bonus-facilitator'):
    assert sha(PRINT / f'{f}.pdf') == sha(SRC / 'reference-pdfs' / f'{f}.pdf'), f
old = {'week-49-bonus': '93ab9d45f260c7ae0c5f7a8a5dc76a8051f0f30d5eae706dd9fa389b805c08b2',
       'week-49-bonus-facilitator': '5b18f1a2f86598c224d953885019151a9f6fc7f4f797dd8e1c8796e948358765'}
for f, h in old.items():
    assert sha(PRINT / 'archive-before-card-fixes-2026-10-23' / f'{f}.pdf') == h, f
print('PASS print copies are the bonus reference PDFs; the October 4 copies are archived unchanged')

student = pymupdf.open(PRINT / 'week-49-bonus.pdf')
guide = pymupdf.open(PRINT / 'week-49-bonus-facilitator.pdf')
s, g = text(student), text(guide)
assert len(student) == 3 and all('Bellingham Math Circle / Week 49 / F49B-S-v2' in p.get_text() for p in student)
assert all(('W49-BONUS-FAC-v2' in p.get_text()) or ('W49-BONUS-FAC-v3' in p.get_text()) for p in guide)  # v3: band-label fix
print('PASS footers F49B-S-v2 on all 3 student pages and W49-BONUS-FAC-v2 (v3 after the band-label fix) on the guide')


def run(v, rounds):
    out = [v]
    for _ in range(rounds):
        v = tuple(v[(i + 1) % 4] - v[i] for i in range(4)); out.append(v)
    return out


first, second = run((0, 1, 0, 1), 9), run((0, 0, 1, 1), 9)
passes = lambda r: next(k for k, v in enumerate(r) if max(map(abs, v)) > 10)
assert passes(first) == 5 and passes(second) == 9 and max(map(abs, first[4])) == 8
assert 'more than 10 away from 0 by round 5?' in s and 'within five rounds' not in s
rows = [w[4] for w in student[2].get_text('words') if w[4].isdigit() and w[0] < 75 and w[1] > 400]
assert sorted(set(rows)) == [str(k) for k in range(8)]
assert 'the printed question, "by round 5" (round 5 included' in g
assert [p.get_text().split('\n')[0] for p in student] == ['Week 49 / Four-tower differences / Grades 2-5',
                                                        'Week 49 / Four-tower differences / Grades 4-5',
                                                        'Week 49 / Four-tower differences / Grades 4-5']
print('PASS could 11: Problem 3 says "by round 5"; (0,1,0,1) first passes 10 at round 5 (16; 8 at round 4) and '
      '(0,0,1,1) only at round 9, so the answer needs round 5, which the table rows 0-7 include; the guide matches. '
      'The per-page level headers (2-5, 4-5, 4-5) are kept as the guide and investigations.json assign them')
