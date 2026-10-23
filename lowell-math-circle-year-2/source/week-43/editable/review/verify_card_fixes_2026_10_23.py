#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes to Week 43 (K-1 Problems 2 and 3, the guide key) by
enumeration and by reading the reference PDFs.

Nothing is imported from the packet or guide builders. The PDFs are read with
PyMuPDF (in requirements.txt). Run from anywhere:
    python3 review/verify_card_fixes_2026_10_23.py
"""
import json
import re
from collections import defaultdict
from itertools import permutations
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
FILLS = {'A': (1.0, 0.89, 0.78), 'B': (0.78, 1.0, 0.78), 'C': (0.89, 0.78, 0.89)}  # orange!22, green!22, violet!22
checks = []


def close(a, b, tol=0.02):
    return all(abs(x - y) <= tol for x, y in zip(a, b))


# 1. The chooser: draw a first card from three, a second from the two left; the last is forced.
rows_by_first = defaultdict(set)
draws = {}
for first, second, last in permutations('ABC'):
    rows_by_first[first].add(first + second + last)
    draws[(first, second)] = first + second + last
assert {k: sorted(v) for k, v in rows_by_first.items()} == {'A': ['ABC', 'ACB'], 'B': ['BAC', 'BCA'], 'C': ['CAB', 'CBA']}
assert len(set(draws.values())) == len(draws) == 6
checks.append('chooser: with A, B or C drawn first exactly two rows can still happen (ABC ACB / BAC BCA / CAB CBA); '
              'the six first-two draws give six different rows')

# 2. K-1 page 2 as printed: the new wording, no cross-outs, each card in the first box of exactly two rows.
k1 = pymupdf.open(REF / 'k-1.pdf')
page = k1[1]
text = ' '.join(page.get_text().split())
assert 'Problem 2: Each row starts with the card drawn first. Find every row that can still happen. ' \
       'Could two different first-two draws make the same row?' in text, text
assert 'crossed-out' not in text and 'same chance' not in text
top = next(b[1] for b in page.get_text('blocks') if b[4].startswith('Problem 2'))
icons, frames, diagonals = [], [], 0
for d in page.get_drawings():
    r, fill, col = d['rect'], d.get('fill'), d.get('color')
    if r.y0 < top:
        continue
    if fill is not None and col is not None and close(col, (0, 0, 0)):
        letter = next(k for k, v in FILLS.items() if close(fill, v))
        icons.append((letter, (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    elif fill is None and col is not None and abs(col[0] - .675) < .01:
        frames.append(r)
    for it in d['items']:   # a cross-out is an unfilled slanted stroke; the triangle icons are filled
        if fill is None and it[0] == 'l' and abs(it[1].x - it[2].x) > 1 and abs(it[1].y - it[2].y) > 1:
            diagonals += 1
assert diagonals == 0, 'a slanted line (cross-out) is still drawn'
assert len(frames) == 18 and len(icons) == 6, (len(frames), len(icons))
rows = defaultdict(list)
for f in frames:
    rows[round(f.y0)].append(f)
assert len(rows) == 3 and all(len(v) == 6 for v in rows.values())   # three bands of two rows of three cells
printed = defaultdict(int)
for y, cells in sorted(rows.items()):
    cells.sort(key=lambda f: f.x0)
    for row in (cells[:3], cells[3:]):
        inside = [[i for i in icons if c.x0 <= i[1] <= c.x1 and c.y0 <= i[2] <= c.y1] for c in row]
        assert len(inside[0]) == 1 and not inside[1] and not inside[2], inside
        printed[inside[0][0][0]] += 1
assert printed == {c: len(rows_by_first[c]) for c in 'ABC'}, printed
checks.append('K-1 p. 2: new Problem 2 wording; no cross-outs; A, B and C each fill the first box of exactly two '
              'empty rows, the number of rows that can still happen')

# 3. K-1 page 3: the swap rule without the chance sentence; P3's records without the second mat, at P4's size.
t3 = ' '.join(k1[2].get_text().split())
assert 'Start A B C. Pick a ticket from 1, 2, 3 and swap that slot with slot 1. Then pick from 2, 3 and swap that slot ' \
       'with slot 2. A slot may swap with itself.' in t3, t3[:300]
assert not any(w in ' '.join(p.get_text().split()) for p in k1 for w in ('same chance', 'equal chances'))
checks.append('K-1 p. 3: the swap rule reads as the card gives it; no K-1 page speaks of chance')
CM = 72 / 2.54
def boxes(page, below):
    top = next(b[1] for b in page.get_text('blocks') if b[4].startswith(below))
    return [d['rect'] for d in page.get_drawings()
            if d['rect'].y0 > top and d.get('fill') is None and d.get('color') and abs(d['color'][0] - .675) < .01]
p3 = boxes(k1[2], 'Problem 3')
assert not [r for r in p3 if r.width > 4 * CM], 'the slot mat is still printed under Problem 3'
cards = [r for r in p3 if r.width > 1.5 * CM]
tix = [r for r in p3 if r.width <= 1.5 * CM]
assert len(cards) == 18 and len(tix) == 12, (len(cards), len(tix))
p4 = [r for r in boxes(k1[3], 'Problem 4') if r.width > 1.5 * CM]
size3 = min(r.width for r in cards) / 72
size4 = max(r.width for r in p4) / 72   # P4's card boxes (P5's printed rows are 0.79 in)
assert size3 >= 0.8 and abs(size3 - size4) < 0.05 and min(r.height for r in cards) / 72 >= 0.85, (size3, size4)
checks.append(f'K-1 p. 3: no second mat under Problem 3; six records of two tickets and three card boxes, '
              f'card boxes {size3:.2f} in wide (P4: {size4:.2f} in; before, 0.41 in)')

# 4. The key: the guide's source and the printed guide agree with the page and the enumeration.
guide = json.loads((ROOT / 'facilitator-src' / 'guide.json').read_text())
key = next(b[1] for i, b in enumerate(guide['pages'][2]) if b[0] == 'p' and 'displayed card' in b[1])
assert key.startswith('Each displayed card is the card drawn first.'), key
listed = dict(re.findall(r'<b>([ABC])</b> is first, (?:the rows are )?(\w+ and \w+)', key))
assert {c: sorted(v.split(' and ')) for c, v in listed.items()} == {c: sorted(v) for c, v in rows_by_first.items()}
pdf = pymupdf.open(REF / 'facilitator-guide.pdf')
assert 'Each displayed card is the card drawn first.' in ' '.join(pdf[2].get_text().split())
assert 'crossed-out' not in ' '.join(p.get_text() for p in pdf)
assert 'The 27-story' in ' '.join(pdf[5].get_text().split())
checks.append('guide p. 3: "Each displayed card is the card drawn first." with rows ABC ACB / BAC BCA / CAB CBA; '
              'p. 6 typo "The27-story" fixed')

for c in checks:
    print('PASS', c)
