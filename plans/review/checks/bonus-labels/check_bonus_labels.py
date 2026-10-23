#!/usr/bin/env python3
"""Check the October 23, 2026 band-label fix in the bonus adult guides (Weeks 18-29, 35-37, 39-51).

Usage: python3 plans/review/checks/bonus-labels/check_bonus_labels.py   (from the repository root)

The guides printed the roster code "KK11 / 3333 / 445" (K, K, 1, 1 / four third graders /
4, 4, 5), in Week 40 as "KK11 /3333 /445", and a lone "KK11", "3333" or "445" for one table.
For each week this reads the current print guide and the copy archived before the fix and checks:
no code is left in any bonus PDF; the footer id went up by one; the page count is unchanged;
and, ignoring spaces, the new text is the old text with only the labels and the footer changed.
Weeks 18, 39 and 40 also had spaces restored before numbers (and Week 40 a missing period in
"PDF pp. 9-11"), which the comparison allows; their joins are checked separately.
"""
import re
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y = ROOT / 'lowell-math-circle-year-2'
WEEKS = [*range(18, 30), 35, 36, 37, *range(39, 52)]
CODE = re.compile(r'KK11|\b3333\b|\b445\b')


def text(pdf):
    return re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf))).strip()


def labels(s):
    s = re.sub(r'KK11 ?/ ?3333 ?/ ?445', 'K–1 / 2–3 / 4–5', s).replace('KK11', 'K–1')
    return re.sub(r'\b445\b', '4–5', re.sub(r'\b3333\b', '2–3', s))


# Bonus guides changed again after the label fix: the copy the fix produced is archived there.
# Week 44: could 15 (3e5ac6e) renumbered the bonus marks (W44-BONUS-FAC-v4); the label-fix v3 is in
# archive-before-small-coulds-2026-10-23. The current copy is still checked for leftover codes.
AFTER_FIX = {44: 'archive-before-small-coulds-2026-10-23'}
rows = []
for w in WEEKS:
    current = Y / f'week-{w}/week-{w}-bonus-facilitator.pdf'
    new = Y / f'week-{w}/{AFTER_FIX[w]}/week-{w}-bonus-facilitator.pdf' if w in AFTER_FIX else current
    old = Y / f'week-{w}/archive-before-bonus-label-fix-2026-10-23/week-{w}-bonus-facilitator.pdf'
    nt, ot = text(new), text(old)
    assert CODE.search(ot) and not CODE.search(nt) and not CODE.search(text(current)), w
    assert not CODE.search(text(Y / f'week-{w}/week-{w}-bonus.pdf')), (w, 'student')
    fo = re.search(r'W\d\d-BON(?:US)?-FAC-v(\d+)', ot); fn = re.search(r'W\d\d-BON(?:US)?-FAC-v(\d+)', nt)
    assert int(fn.group(1)) == int(fo.group(1)) + 1, (w, fo.group(0), fn.group(0))
    assert len(pymupdf.open(new)) == len(pymupdf.open(old)), w
    ot2 = labels(ot).replace(fo.group(0), fn.group(0)).replace(' ', '')
    if w == 40:
        ot2 = ot2.replace('PDFpp9–11', 'PDFpp.9–11')  # Week 40's one non-space fix: a missing period
    assert ot2 == nt.replace(' ', ''), w
    joins = len(re.findall(r'(?<=[a-z]{2})\d|(?<=[a-z]{2}),\d|PDF\d|Python\d|[a-z]\(r\d|pp\.[a-z0-9]', nt.replace('python3', '')))
    joins -= len(re.findall(r'part00\d', nt))
    if w in (18, 39, 40):
        assert joins == 0, (w, joins)
    rows.append(f'{w} {fo.group(0)} -> {fn.group(0)}, {len(pymupdf.open(new))} pp.')
print('PASS', len(rows), 'bonus guides: no "KK11", "3333" or "445" left in any bonus PDF; each footer id up by one; '
      'page counts unchanged; text otherwise identical (spaces aside); Weeks 18, 39 and 40 have no word-number joins.')
print('\n'.join(rows))
