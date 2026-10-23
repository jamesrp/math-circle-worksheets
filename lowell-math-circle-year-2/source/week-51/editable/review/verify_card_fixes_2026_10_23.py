#!/usr/bin/env python3
"""Check the October 23, 2026 student-page fixes to Week 51 by enumeration and by reading
the reference PDFs and the guide source.

Nothing is imported from the packet or guide builders. The PDFs are read with PyMuPDF
(in requirements.txt). Run from anywhere:
    python3 review/verify_card_fixes_2026_10_23.py
"""
import json
import re
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
MM = 25.4 / 72
checks = []


def grid(lo, hi, step=F(1, 4)):
    """Every quarter-unit length from lo to hi; it contains every endpoint used here."""
    n = int((hi - lo) / step)
    return [lo + i * step for i in range(n + 1)]


def text(page):
    return ' '.join(page.get_text().split())


# 1. Mathematics of the changed problems.
joins = [a + b for a in grid(2, 3) for b in grid(1, 2)]
assert (min(joins), max(joins)) == (3, 5) and 2 + 2 in joins and 3 < 4 < 5
checks.append('launch: A 2-3 with B 1-2 joins 3 to 5; the printed join A 2 + B 2 = 4 is one legal join, '
              'strictly inside, so it shows the action without showing either extreme')

card = [a + b for a in grid(3, 4) for b in grid(4, 5)]
assert (min(card), max(card)) == (7, 9)
assert [c for c in ((3, 4), (4, 5), (5, 6)) if 7 <= 3 + c[0] and 4 + c[1] <= 9] == [(4, 5)]
checks.append('K-1 P3: only card B 4-5 keeps every join in 7 to 9, and its longest join ends exactly at 9, '
              'so the page must say that fitting within 9 includes 9')

gaps = [(a, b, (a + 4) - (b + 1)) for a in grid(4, 6) for b in grid(4, 6)]
lo, hi = min(g for *_, g in gaps), max(g for *_, g in gaps)
assert (lo, hi) == (1, 5)
assert {(a, b) for a, b, g in gaps if g == lo} == {(4, 6)} and {(a, b) for a, b, g in gaps if g == hi} == {(6, 4)}
assert all((a + 4) - (a + 1) == 3 for a in grid(4, 6))
frozen = [(5 + 4) - (b + 1) for b in grid(4, 6)]
assert (min(frozen), max(frozen)) == (2, 4)
checks.append('shared page: the same A gives gap 3 every time; A and B separately in 4-6 give 1 to 5, with the '
              'extremes only at A=4,B=6 and A=6,B=4, so A must change between tries (held at the drawn 5, '
              'the gap runs only 2 to 4: the reading the old K-1 wording invited)')

three = [(L, S) for L in range(7, 10) for S in range(5, 7) if L - S == 3]
assert three == [(8, 5), (9, 6)]
checks.append('K-1 P5: the whole-unit gaps of 3 are 8-5 and 9-6, one for each of the two printed rulers')

pairs = [(a, 9 - a) for a in range(3, 8) if 3 <= 9 - a <= 5]
assert pairs == [(4, 5), (5, 4), (6, 3)] and (3, 6) not in pairs and (7, 2) not in pairs
assert [(a, 9 - a) for a in range(4, 7) if 3 <= 9 - a <= 5] == pairs   # the answers did not change
checks.append('fill 9: with A 3-7 and B 3-5 the pairs are still (4,5), (5,4), (6,3); A=3 (B=6) and A=7 (B=2) '
              'now fail on B\'s card, and four boards exceed the three answers')

# 2. The packets as printed.
docs = {n: pymupdf.open(REF / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5')}
expect = {'k-1': [[1], [2], [3], [4, 5], [6], [7]],
          'grades-2-3': [[1], [2], [3, 4], [5, 6], [7], [8]],
          'grades-4-5': [[1], [2], [3, 4], [5, 6], [7], [8, 9]]}
for name, doc in docs.items():
    got = [[int(n) for n in re.findall(r'Problem (\d+):', text(p))] for p in doc]
    assert got == expect[name], (name, got)
    gap_page = next(i for i, p in enumerate(doc) if 'long strip:' in text(p))
    shared_page = next(i for i, p in enumerate(doc) if 'Smallest gap:' in text(p))
    assert gap_page + 1 == shared_page, (name, gap_page, shared_page)
    whole = ' '.join(text(p) for p in doc)
    assert 'keep A unchanged' not in whole and 'One possible setting' not in whole, name
    assert 'The white pieces are exactly 4 and 1 units long.' in text(doc[shared_page]), name
checks.append('page order: in every band the gap page comes before the shared page, and problems run '
              'K-1 1-7, Grades 2-3 1-8, Grades 4-5 1-9 consecutively; no page says "One possible setting"')

k1 = docs['k-1']
assert ("Problem 6: Find how small and how big each end gap can be. Start at 0. Both A's in the top picture "
        "are the same length. Each try may use new lengths.") in text(k1[4]).replace('’', "'")
for name in ('grades-2-3', 'grades-4-5'):
    assert ('Repeated A means the same unchanged length; B may vary separately.' in text(docs[name][4]))
checks.append('K-1 p. 5, Problem 6: "Both A\'s in the top picture are the same length. Each try may use new '
              'lengths." The older bands keep their wording')

assert 'Fitting within 9 includes ending at 9.' in text(k1[2])
checks.append('K-1 p. 3: "Fitting within 9 includes ending at 9." is printed under the cards')


def tick_rulers(page):
    """Rulers as {y: sorted tick x (mm)}, from 4 mm vertical tick strokes."""
    out = defaultdict(set)
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                a, b = it[1], it[2]
                if abs(a.x - b.x) < .01 and abs(abs(a.y - b.y) * MM - 4) < .02:
                    out[round((a.y + b.y) / 2 * MM, 2)].add(round(a.x * MM, 2))
    return {y: sorted(xs) for y, xs in out.items()}


p5_top = next(b[1] for b in k1[3].get_text('blocks') if b[4].startswith('Problem 5')) * MM
below = [y for y, xs in tick_rulers(k1[3]).items() if y > p5_top and len(xs) == 17]
assert len(below) == 2, below
checks.append(f'K-1 p. 4: two 0-16 rulers under Problem 5 (at {below[0]:.0f} and {below[1]:.0f} mm from the top edge), one per way')

for name, doc in docs.items():
    page = doc[0]
    rulers = tick_rulers(page)
    joins_drawn = [d['rect'] for d in page.get_drawings()
                   if d.get('fill') and abs(d['rect'].height * MM - 9) < .05]
    assert len(joins_drawn) == 2, (name, len(joins_drawn))     # one join: an A piece and a B piece
    a, b = sorted(joins_drawn, key=lambda r: r.x0)
    assert abs(a.width * MM - 20) < .05 and abs(b.width * MM - 20) < .05 and abs(a.x1 - b.x0) < .01
    y, xs = min(((y, xs) for y, xs in rulers.items() if len(xs) == 8 and y < a.y0 * MM),
                key=lambda t: abs(t[1][0] - a.x0 * MM))
    assert abs(xs[0] - a.x0 * MM) < .05 and abs(xs[4] - b.x1 * MM) < .05, (name, xs, a, b)
checks.append('p. 1, every band: one launch join, A 20 mm + B 20 mm, starting at the A + B ruler\'s 0 and '
              'ending at its 4 (before, two joins started 2 mm right of 0)')

for name in ('k-1', 'grades-2-3'):
    page = docs[name][5]
    assert 'A: 3 to 7 units' in text(page) and 'B: 3 to 5 units' in text(page)
    boards = [d['rect'] for d in page.get_drawings() if not d.get('fill')
              and abs(d['rect'].width * MM - 90) < .05 and abs(d['rect'].height * MM - 13) < .05]
    assert len(boards) == 4, (name, len(boards))
    nine = [xs for y, xs in tick_rulers(page).items() if len(xs) == 10]
    assert len(nine) == 4 and all(abs(xs[-1] - xs[0] - 90) < .05 for xs in nine)
checks.append('fill-9 page (K-1 P7, Grades 2-3 P8): A 3 to 7 units, and four 90 mm boards on 0-9 rulers')

# 3. The guide agrees with the pages and the enumeration.
pages = json.loads((ROOT / 'facilitator-src' / 'content.json').read_text())['pages']
paras = [b[1] for page in pages for b in page if b[0] == 'p']
nine_key = next(p for p in paras if p.startswith('<b>K-1 Problem 7; Grades 2-3 Problem 8.</b>'))
assert 'A from 3 to 7' in nine_key and 'Four boards' in nine_key
listed = re.findall(r'<b>([^<]*)</b>', nine_key)[1]   # the bold pair list after the label
assert re.findall(r'\((\d),(\d)\)', listed) == [(str(a), str(b)) for a, b in pairs], listed
labels = [re.match(r'<b>([^<]*Problem[^<]*)</b>', p).group(1) for p in paras if re.match(r'<b>[^<]*Problem', p)]
assert labels == ['Problem 1, all bands.', 'Problem 2.', 'Problem 3.', 'Grades 2-3 and 4-5 Problem 4.',
                  'K-1 Problem 4.', 'K-1 Problem 5.', 'Grades 2-3 and 4-5 Problem 5.', 'Grades 2-3 and 4-5 Problem 6.',
                  'K-1 Problem 6; older Problem 7.', 'K-1 Problem 7; Grades 2-3 Problem 8.', 'Grades 4-5 Problem 8.',
                  'Grades 4-5 Problem 9.'], labels
launch = next(p for p in paras if p.startswith('<b>Launch'))
assert 'end at 4' in launch and 'shorter join and a longer one' in launch
route = json.loads((ROOT / 'facilitator-src' / 'route-note.json').read_text())['notes'][0][1]
assert 'K-1 can make gap extremes (P4-5), compare shared and separate strips (P6)' in route and 'in P7.' in route
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
assert len(guide) == 4
g = [text(p) for p in guide]
assert 'end at 4, inside the A + B band' in g[0]
assert 'Key for gaps between two strips' in g[1] and 'K-1 Problem 4.' in g[1] and 'Problem 6.' in g[1]
assert 'K-1 Problem 6; older Problem 7.' in g[2] and 'With A from 3 to 7' in g[2]
assert '(P4-5)' in g[3] and 'in P7.' in g[3]
checks.append('guide: keys in problem order with the new numbers (gap keys p. 2, shared and exact-total keys '
              'p. 3), the fill-9 key for A 3 to 7 lists the enumerated pairs, the launch asks for a shorter and a '
              'longer join, and the route note (p. 4) gives K-1 P4-5, P6 and Grades 4-5 P7')

for c in checks:
    print('PASS', c)
