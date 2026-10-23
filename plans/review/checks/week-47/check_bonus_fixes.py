#!/usr/bin/env python3
"""Week 47 bonus companion, October 23, 2026: the math check's items 2 and 4, checked on the
print copies and by enumeration.

Item 2: bonus Problem 3 now says the gray towers count in the total, so the budgets 2-10
(2, 5, 8 and 10 work, 11 does not) are the only reading. Item 4: the guide says the envelopes
are legal when an extension exists; without one, L exceeds some clue. Run from the
repository root:
    python3 plans/review/checks/week-47/check_bonus_fixes.py
"""
import hashlib
import re
from collections import Counter
from itertools import product
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PRINT, SRC = Y2 / 'week-47', Y2 / 'source' / 'week-47-bonus'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
text = lambda doc: ' '.join(' '.join(p.get_text().split()) for p in doc)

for f in ('week-47-bonus', 'week-47-bonus-facilitator'):
    assert sha(PRINT / f'{f}.pdf') == sha(SRC / 'reference-pdfs' / f'{f}.pdf'), f
old = {'week-47-bonus': 'c8516a1e7506ee6c9f0a6de811439412e2e5805aa559221a9d80e83b19b43ae8',
       'week-47-bonus-facilitator': 'd5795249e23ce2a2771930641f73e36f4830476a9a85ab5c3aed0465e8095663'}
for f, h in old.items():
    assert sha(PRINT / 'archive-before-card-fixes-2026-10-23' / f'{f}.pdf') == h, f
print('PASS print copies are the bonus reference PDFs; the October 4 copies are archived unchanged')

student = pymupdf.open(PRINT / 'week-47-bonus.pdf')
guide = pymupdf.open(PRINT / 'week-47-bonus-facilitator.pdf')
s, g = text(student), text(guide)
assert len(student) == 3 and all('Bellingham Math Circle / Week 47 / F47B-S-v2' in p.get_text() for p in student)
assert all('W47-BONUS-FAC-v2' in p.get_text() for p in guide)
print('PASS footers F47B-S-v2 on all 3 student pages and W47-BONUS-FAC-v2 on both guide pages')

# Item 2: the six-site ring A..F, gray A = D = 1.
assert 'Gray towers stay at 1 cube each and count in the total; neighboring towers differ by at most 1.' in s
ring = [(i, (i + 1) % 6) for i in range(6)]
rings = [v for v in product(range(4), repeat=6) if v[0] == v[3] == 1 and all(abs(v[a] - v[b]) <= 1 for a, b in ring)]
with_gray = Counter(sum(v) for v in rings)
white_only = Counter(sum(v) - 2 for v in rings)
assert len(rings) == 49 and sorted(with_gray) == list(range(2, 11))
assert [with_gray[t] for t in range(2, 11)] == [1, 4, 6, 8, 11, 8, 6, 4, 1]
assert [b for b in (2, 5, 8, 10, 11) if with_gray[b]] == [2, 5, 8, 10]
assert [b for b in (2, 5, 8, 10, 11) if white_only[b]] == [2, 5, 8]          # the other reading also loses 10
assert 'The gray towers count in every total, as the page says.' in g and 'every total 2 less (0 to 8), so 10 fails too' in g
print('PASS item 2: Problem 3 says the gray towers count; 49 rings with totals 2-10 (1,4,6,8,11,8,6,4,1), so 2, 5, 8 '
      'and 10 work and 11 does not; counting only white towers would give 0-8 and lose 10, which the guide notes')

# Item 4: envelopes on rows and rings of up to six sites, clue heights 0-3.
assert 'When an extension exists, both are legal; without one the formulas miss a clue.' in g


def dist(n, cyc, a, b):
    d = abs(a - b)
    return min(d, n - d) if cyc else d


cases = 0
for n in range(2, 7):
    for cyc in (False, True) if n >= 3 else (False,):
        edges = [(i, i + 1) for i in range(n - 1)] + ([(n - 1, 0)] if cyc else [])
        for k in (1, 2, 3):
            for sites in product(range(n), repeat=k):
                if list(sites) != sorted(set(sites)) or len(sites) != k:
                    continue
                for hs in product(range(4), repeat=k):
                    clues = dict(zip(sites, hs)); cases += 1
                    L = [max([0] + [a - dist(n, cyc, v, c) for c, a in clues.items()]) for v in range(n)]
                    U = [min(a + dist(n, cyc, v, c) for c, a in clues.items()) for v in range(n)]
                    fits = lambda h: all(h[c] == a for c, a in clues.items()) and all(abs(h[x] - h[y]) <= 1 for x, y in edges)
                    exists = any(fits(h) for h in product(range(max(hs) + n + 1), repeat=n)) if n <= 5 else \
                        all(abs(a - b) <= dist(n, cyc, c, d) for (c, a) in clues.items() for (d, b) in clues.items())
                    assert exists == (fits(L) and fits(U)), (n, cyc, clues)
                    if not exists:
                        assert any(L[c] > a for c, a in clues.items())
L = [max(0, 0 - dist(5, True, v, 0), 3 - dist(5, True, v, 3)) for v in range(5)]
assert L[0] == 1                                                              # page 1's first ring, A=0 and D=3
print(f'PASS item 4: on {cases} clue sets (rows and rings of 2-6 sites, 1-3 clues of height 0-3) L and U are legal '
      'completions exactly when an extension exists, and otherwise L exceeds a clue (page 1\'s ring with A=0, D=3 '
      'gives L(A)=1); the guide now says so')
