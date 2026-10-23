#!/usr/bin/env python3
"""Week 45 card fixes of October 23, 2026, checked on the print copies.

Runs the package checker (shoulds 1-7, coulds 10-13 and every new extension answer) against
the reference PDFs, confirms the print copies are those references, and checks should 8,
the bonus guide's "3 × 2 × 2 = 12" (and the same lost asterisks in "b × h = r × f").
Run from the repository root:
    python3 plans/review/checks/week-45/check_card_shoulds.py
"""
import hashlib
import subprocess
import sys
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PKG = Y2 / 'source' / 'week-45' / 'editable'
PRINT = Y2 / 'week-45'
BONUS = Y2 / 'source' / 'week-45-bonus'

out = subprocess.run([sys.executable, str(PKG / 'review' / 'verify_card_shoulds_2026_10_23.py')],
                     capture_output=True, text=True, check=True).stdout
print(out, end='')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for ref, printed in (('k-1', 'k-1'), ('grades-2-3', 'grades-2-3'), ('grades-4-5', 'grades-4-5'),
                     ('facilitator-guide', 'facilitator')):
    assert sha(PKG / 'reference-pdfs' / f'{ref}.pdf') == sha(PRINT / f'week-45-{printed}.pdf'), ref
print('PASS print copies week-45-k-1, -grades-2-3, -grades-4-5 and -facilitator are the checked reference PDFs')

src = (BONUS / 'guide.md').read_text()
assert '3*2*2' not in src and 'b*h' not in src
guide = ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(PRINT / 'week-45-bonus-facilitator.pdf'))
assert 'There are 3 × 2 × 2 = 12 equally likely histories.' in guide and '322=12' not in guide
assert 'The equation b × h = r × f has' in guide and 'bh=rf' not in guide
assert sha(BONUS / 'reference-pdfs' / 'week-45-bonus-facilitator.pdf') == sha(PRINT / 'week-45-bonus-facilitator.pdf')
assert 3 * 2 * 2 == 12
print('PASS should 8: the bonus guide prints "3 × 2 × 2 = 12" (was "322=12") and "b × h = r × f" (was "bh=rf"); '
      'its reference copy is the print copy')
