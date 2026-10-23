#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 46 in the print PDFs.

v4 student packets: no line on any student page ends in a hyphen (hyphenation is off, so
"match-ing" and "cho-sen" no longer break); every footer reads v4; and, joining each old line
break back up, the words of every page are the same as v3. The guide is unchanged.
Run from the repository root:
    python3 plans/review/checks/week-46/check_critic_fixes.py
Needs PyMuPDF."""
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
WEEK, BANDS = 46, ('k-1', 'grades-2-3', 'grades-4-5')
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def words(page, tag):
    """The page's words with the footer version removed, compared without hyphens, since a
    line break at "three-draw" or "keep-ing" drops or keeps the hyphen differently."""
    t = page.get_text().replace(tag + '-v3', tag).replace(tag + '-v4', tag)
    t = re.sub(r'(\w)-\n(\w)', r'\1\2', t).replace('-', '')
    return ' '.join(t.split())


for band in BANDS:
    tag = f'W{WEEK}-{band}'
    new = pymupdf.open(Y2 / f'week-{WEEK}' / f'week-{WEEK}-{band}.pdf')
    old = pymupdf.open(Y2 / f'week-{WEEK}' / 'archive-before-critic-fixes-2026-10-23' / f'week-{WEEK}-{band}.pdf')
    check(len(new) == len(old) and all(f'{tag}-v4' in p.get_text() for p in new), f'{band}: {len(new)} pages, footer {tag}-v4')
    ends = [(i + 1, ln) for i, p in enumerate(new) for ln in p.get_text().split('\n') if ln.rstrip().endswith('-')]
    check(not ends, f'{band}: no line ends in a hyphen {ends[:3]}')
    olds = [(i + 1, ln) for i, p in enumerate(old) for ln in p.get_text().split('\n') if ln.rstrip().endswith('-')]
    if olds:
        print(f'      (v3 broke {len(olds)} lines, e.g. {olds[0]})')
    diffs = [i + 1 for i, (a, b) in enumerate(zip(new, old)) if words(a, tag) != words(b, tag)]
    check(not diffs, f'{band}: words unchanged (pages differing: {diffs})')
text = ' '.join(' '.join(p.get_text().split()) for b in BANDS for p in pymupdf.open(Y2 / f'week-{WEEK}' / f'week-{WEEK}-{b}.pdf'))
check('matching' in text and 'chosen' in text, '"matching" and "chosen" print whole')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
