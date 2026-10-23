#!/usr/bin/env python3
"""Week 47 card fixes of October 23, 2026, checked on the print copies.

Runs the package checker (shoulds 1-7, coulds 8-13: every changed prompt, board, row, key
and count, recomputed by enumeration) against the reference PDFs, and confirms that the
print copies are those references and that the replaced copies are archived unchanged.
Run from the repository root:
    python3 plans/review/checks/week-47/check_card_shoulds.py
"""
import hashlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
Y2 = REPO / 'lowell-math-circle-year-2'
PKG = Y2 / 'source' / 'week-47' / 'editable'
PRINT = Y2 / 'week-47'

print(subprocess.run([sys.executable, str(PKG / 'review' / 'verify_card_shoulds_2026_10_23.py')],
                     capture_output=True, text=True, check=True).stdout, end='')

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for ref, printed in (('k-1', 'k-1'), ('grades-2-3', 'grades-2-3'), ('grades-4-5', 'grades-4-5'),
                     ('facilitator-guide', 'facilitator')):
    assert sha(PKG / 'reference-pdfs' / f'{ref}.pdf') == sha(PRINT / f'week-47-{printed}.pdf'), ref
print('PASS print copies week-47-k-1, -grades-2-3, -grades-4-5 and -facilitator are the checked reference PDFs')

old = {'k-1': '3e9f79edb63546bb5692102de0984f59e23b186aed7373e2dfde92f9d041cbe3',
       'grades-2-3': '40c928882a784970a5b79be40416c93d1937a6f5d570ae899c12fca298bdae30',
       'grades-4-5': '557a31429a2d8c0d099f2ef39296bc7b31075a9d1991e10822c594e6f158cd5e',
       'facilitator': '94279ef1763e7d0840ae3f8f7f9be820a30f018c1f961bc812d915b99a3b0e17'}
for f, h in old.items():
    assert sha(PRINT / 'archive-before-card-fixes-2026-10-23' / f'week-47-{f}.pdf') == h, f
print('PASS the October 4 print copies (v3) are archived unchanged in week-47/archive-before-card-fixes-2026-10-23/')
