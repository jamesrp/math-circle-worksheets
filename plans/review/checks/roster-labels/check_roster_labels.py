#!/usr/bin/env python3
"""Check the October 23, 2026 roster-label fix in the main adult guides of Weeks 27, 54, 55, 57 and 62.

Usage: python3 plans/review/checks/roster-labels/check_roster_labels.py   (from the repository root)

These guides printed the roster code for the current group, "KK11 / 3333 / 445" or "KK11, 3333
and 445" (K, K, 1, 1 / four third graders / 4, 4, 5), where a reader expects band labels. For
each week this reads the current print guide and the copy archived before the fix and checks:
no code is left in any of the week's print PDFs; the page count is unchanged; the footer id went
up by one (Week 27's footer has no id and must be unchanged); and, ignoring spaces, the new text
is the old text with only the labels and the footer id changed. The bonus guides had the same
fix (plans/review/checks/bonus-labels/).
"""
import re
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y = ROOT / 'lowell-math-circle-year-2'
WEEKS = [27, 54, 55, 57, 62]
CODE = re.compile(r'KK11|\b3333\b|\b445\b')
FOOT = re.compile(r'Bellingham Math Circle / Week \d+ / (\S+-v)(\d+)')


def text(pdf):
    return re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf))).strip()


def labels(s):
    s = re.sub(r'KK11 ?/ ?3333 ?/ ?445', 'K–1 / 2–3 / 4–5', s)
    return s.replace('KK11, 3333 and 445', 'K–1, 2–3 and 4–5')


rows = []
for w in WEEKS:
    name = f'week-{w}-facilitator.pdf'
    new, old = Y / f'week-{w}' / name, Y / f'week-{w}/archive-before-roster-label-fix-2026-10-23' / name
    nt, ot = text(new), text(old)
    assert CODE.search(ot), (w, 'archived guide should have the code')
    for pdf in sorted((Y / f'week-{w}').glob('*.pdf')):
        assert not CODE.search(text(pdf)), (w, pdf.name)
    n = len(pymupdf.open(new))
    assert n == len(pymupdf.open(old)), w
    fo = FOOT.search(ot)
    if fo:
        a, b = fo.group(1) + fo.group(2), fo.group(1) + str(int(fo.group(2)) + 1)
        assert b in nt and a not in nt, (w, a, b)
        ot = ot.replace(a, b)
        rows.append(f'{w}: {a} -> {b}, {n} pp.')
    else:
        assert not FOOT.search(nt), w
        rows.append(f'{w}: footer has no id (unchanged), {n} pp.')
    assert labels(ot).replace(' ', '') == nt.replace(' ', ''), w
print('PASS', len(rows), 'main guides: no roster code left in any of their print PDFs; page counts unchanged; '
      'footer ids up by one (Week 27 has none); text otherwise identical (spaces aside).')
print('\n'.join(rows))
