#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 45 in the print PDFs.

v4 student packets: no line on any student page ends in a hyphen (hyphenation is off, so
"keep-ing", "cer-tain", "some-times" and "when-ever" no longer break); K-1 Problem 4 says
"Add just one extra ticket to this cup"; every footer reads v4; and, joining each old line
break back up, the words of every page are the same as v3 apart from that one change.
The guide is unchanged. Also recomputes K-1 Problem 4: with tickets 1 and 3 in the cup
(red shows on both, hiding red on 1 and blue on 3), adding 2 makes hidden red more likely
and adding 4, 5 or 6 keeps the tie. Run from the repository root:
    python3 plans/review/checks/week-45/check_critic_fixes.py
Needs PyMuPDF."""
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
WEEK, BANDS = 45, ('k-1', 'grades-2-3', 'grades-4-5')
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


# Ticket n shows face n of the three cards: faces 1 and 2 are the red-red card, 3 and 4 the
# red/blue card (3 shows red over blue, 4 blue over red), 5 and 6 the blue-blue card.
# The hidden colour on each red-showing ticket:
hidden_when_red = {1: 'red', 2: 'red', 3: 'blue'}
base = [hidden_when_red[t] for t in (1, 3)]
check(base.count('red') == base.count('blue'), 'tickets 1 and 3: a red clue hides red and blue equally')
plus2 = base + [hidden_when_red[2]]
check(plus2.count('red') == 2 and plus2.count('blue') == 1, 'adding 2: hidden red 2 ways, blue 1')
check(all(t not in hidden_when_red for t in (4, 5, 6)), 'adding 4, 5 or 6: no new red-showing round, still a tie')

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
    check(diffs == ([3] if band == 'k-1' else []), f'{band}: words unchanged except where intended (pages differing: {diffs})')
k = words(pymupdf.open(Y2 / f'week-{WEEK}' / f'week-{WEEK}-k-1.pdf')[2], 'W45-k-1')
check('Add just one extra ticket to this cup: 2, 4, 5, or 6.' in k and 'chooser' not in k and 'Only tickets 1 and 3 are in the cup.' in k, 'K-1 p. 3: "this cup", matching the rule line')
G = pymupdf.open(Y2 / 'week-45' / 'week-45-facilitator.pdf')
check(len(G) == 9 and not any('this chooser: 2, 4, 5' in ' '.join(p.get_text().split()) for p in G), 'guide: 9 pages, quotes no old K-1 Problem 4 wording')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
