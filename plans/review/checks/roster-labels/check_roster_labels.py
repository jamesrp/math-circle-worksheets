#!/usr/bin/env python3
"""Check the October 23, 2026 roster-label fix in the main adult guides of Weeks 27, 53, 54, 55, 57, 58, 60, 62 and 63.
Also the return-visit adult guides of Weeks 6, 7 and 11-17 (RV6-FAC-v2, RV7-FAC-v2, RV-11-FAC-v2 ... RV-17-FAC-v2).

Usage: python3 plans/review/checks/roster-labels/check_roster_labels.py   (from the repository root)

These guides printed the roster code for the current group, "KK11 / 3333 / 445" or "KK11, 3333
and 445" (K, K, 1, 1 / four third graders / 4, 4, 5), where a reader expects band labels. For
each week this reads the current print guide and the copy archived before the fix and checks:
no code is left in any of the week's print PDFs; the page count is unchanged; the footer id went
up by one (Week 27's footer has no id and must be unchanged); and, ignoring spaces, the new text
is the old text with only the labels and the footer id changed (hyphens
aside too, since a reflowed line can break a word differently). The bonus guides had the same
fix (plans/review/checks/bonus-labels/).

Weeks 58 and 60 (added later that day) used the code as table names throughout ("KK11: parent
volunteer ...", "two for KK11, two for 3333, one for 445"). Each lone code became its band label,
and where Week 60 used the code as a sentence's subject it became "the K-1 table" (and "the 2-3
table", "the 4-5 table"); EXTRA lists those exact rewrites, which the text comparison allows.
"""
import re
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y = ROOT / 'lowell-math-circle-year-2'
WEEKS = [27, 53, 54, 55, 57, 58, 60, 62, 63]
RV_WEEKS = [6, 7, 11, 12, 13, 14, 15, 16, 17]
# A guide revised again after this fix is checked through the copy archived before that revision.
LATER = {57: 'archive-before-critic-j-fixes-2026-10-23'}   # W57-FAC-v3; v4 changed p. 1's K-1 route reference
CODE = re.compile(r'KK11|\b3333\b|\b445\b')
FOOT = re.compile(r'Bellingham Math Circle / Week \d+ / (\S+-v)(\d+)')


def text(pdf):
    return re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf))).strip()


# Week 60's rewrites beyond a plain label, as old text -> new text (the code as a subject or
# possessive); every other lone code in Weeks 58 and 60 became its band label.
EXTRA = {60: [("KK11's tower pages", 'K–1 tower pages'), ('KK11’s tower pages', 'K–1 tower pages'),
              ('K–1 route at KK11, adult-led', 'K–1 route, adult-led'),
              ('KK11 plays two-offer', 'The K–1 table plays two-offer'), ('; KK11 builds', '; the K–1 table builds'),
              ('; KK11 may try', '; the K–1 table may try'), ('At 3333,', 'At the 2–3 table,'), ('At 445,', 'At the 4–5 table,')]}
LONE = {58, 60}


def labels(s, w=None):
    s = re.sub(r'KK11 ?/ ?3333 ?/ ?445', 'K–1 / 2–3 / 4–5', s)
    s = s.replace('KK11, 3333 and 445', 'K–1, 2–3 and 4–5')
    for a, b in EXTRA.get(w, []):
        s = s.replace(a, b)
    if w in LONE:
        s = re.sub(r'\b445\b', '4–5', re.sub(r'\b3333\b', '2–3', s.replace('KK11', 'K–1')))
    return s


rows = []
for w in WEEKS:
    name = f'week-{w}-facilitator.pdf'
    new, old = Y / f'week-{w}' / name, Y / f'week-{w}/archive-before-roster-label-fix-2026-10-23' / name
    if w in LATER:
        new = Y / f'week-{w}' / LATER[w] / name
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
    flat = lambda s: s.replace(' ', '').replace('-', '')  # line breaks may hyphenate differently after a reflow
    assert flat(labels(ot, w)) == flat(nt), w
print('PASS', len(rows), 'main guides: no roster code left in any of their print PDFs; page counts unchanged; '
      'footer ids up by one (Week 27 has none); text otherwise identical (spaces aside).')
print('\n'.join(rows))

# Return-visit adult guides (added later that day). Each printed "KK11 / 3333 / 445" once, on p. 2;
# Week 9's never had it, and Weeks 8 and 10 were left to the footer sweep that owned those files.
RVFOOT = re.compile(r'(RV-?\d+-FAC-v)(\d+)')
rv = []
for w in RV_WEEKS:
    folder = Y / f'week-{w:02d}'
    name = f'week-{w:02d}-return-visit-facilitator.pdf'
    new, old = folder / name, folder / 'archive-before-roster-label-fix-2026-10-23' / name
    nt, ot = text(new), text(old)
    assert len(CODE.findall(ot)) == 3, (w, 'archived guide should have the code once')
    for pdf in sorted(folder.glob('*return-visit*.pdf')):
        assert not CODE.search(text(pdf)), (w, pdf.name)
    n = len(pymupdf.open(new))
    assert n == len(pymupdf.open(old)), w
    fo = RVFOOT.search(ot)
    a, b = fo.group(1) + fo.group(2), fo.group(1) + str(int(fo.group(2)) + 1)
    assert b in nt and a not in nt, (w, a, b)
    assert ot.count(a) == n, (w, 'footer on every page')
    flat = lambda s: s.replace(' ', '').replace('-', '')
    assert flat(labels(ot.replace(a, b))) == flat(nt), w
    rv.append(f'RV{w}: {a} -> {b}, {n} pp.')
nine = text(Y / 'week-09/week-09-return-visit-facilitator.pdf')
assert not CODE.search(nine)
print('PASS', len(rv), 'return-visit guides: the same checks (the code once each; every return-visit print PDF '
      'of the week free of it); Week 9\'s guide never had it.')
print('\n'.join(rv))
