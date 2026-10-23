#!/usr/bin/env python3
"""Check the October 23, 2026 student-page fixes to Week 29 (review card shoulds 2, 3, 7, 8, 9,
11 and 12, coulds 13-16) against the mathematics and the printed pages.

Run from the package folder: python3 review/verify_student_fixes_2026_10_23.py [pdf folder]
The PDFs default to reference-pdfs/. Needs PyMuPDF; the mathematics uses the standard library.
"""
from itertools import combinations
from math import gcd
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDFS = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
MM = 25.4 / 72


def builds(a, b, n):
    return [(x, (n - a * x) // b) for x in range(n // a + 1) if (n - a * x) % b == 0]


def gaps(a, b, upto=300):
    return [n for n in range(1, upto) if not builds(a, b, n)]


def text(name):
    return [re.sub(r'\s+', ' ', p.get_text()) for p in pymupdf.open(PDFS / f'{name}.pdf')]


def check(ok, msg):
    assert ok, msg
    print('PASS', msg)


K, M, U = text('k-1'), text('grades-2-3'), text('grades-4-5')
allpages = K + M + U

# Footers: every page of the three packets is v3.
check(all(re.search(r'F29-(K|23|45)-v3', p) for p in allpages) and not any('-v2' in p for p in allpages),
      'every student page carries a v3 footer (F29-K-v3, F29-23-v3, F29-45-v3)')

# Should 9: the ruler sentence is gone from K-1 P4 and 2-3 P1.
check(not any('Mark a target' in p for p in allpages), 'no page says "Mark a target on a ruler" (should 9)')

# Should 3: K-1 P2 has three strips per target, and each target has exactly two ways.
assert len(builds(3, 4, 12)) == 2 and len(builds(3, 4, 15)) == 2
page = pymupdf.open(PDFS / 'k-1.pdf')[1]
lengths = sorted(round((d['rect'][2] - d['rect'][0]) * MM / 10) for d in page.get_drawings()
                 if abs((d['rect'][3] - d['rect'][1]) * MM - 10) < .3 and (d['rect'][2] - d['rect'][0]) * MM > 100)
check(lengths == [12, 12, 12, 15, 15, 15], 'K-1 Problem 2 prints three 12 cm and three 15 cm strips; 12 and 15 '
      'each have exactly two builds from 3- and 4-rods, so one strip per target stays empty (should 3)')

# Should 8: K-1 P6 has six rows, one per pair, each with two pair boxes and targets 6-12.
pairs = list(combinations((2, 3, 4, 5), 2))
covering = [p for p in pairs if all(builds(*p, n) for n in range(6, 13))]
assert covering == [(2, 3), (2, 5), (3, 4)]
assert {p: [n for n in range(6, 13) if not builds(*p, n)] for p in pairs if p not in covering} == \
    {(2, 4): [7, 9, 11], (3, 5): [7], (4, 5): [6, 7, 11]}
page = pymupdf.open(PDFS / 'k-1.pdf')[5]
boxes = [d['rect'] for d in page.get_drawings() if d['type'] == 's' and [i[0] for i in d['items']] in (['re'], ['l'] * 4)]
targets = [r for r in boxes if abs((r[2] - r[0]) * MM - 16) < .3 and abs((r[3] - r[1]) * MM - 12) < .3]
pairbox = [r for r in boxes if abs((r[2] - r[0]) * MM - 11) < .3 and abs((r[3] - r[1]) * MM - 11) < .3]
words = page.get_text('words')
inside = sorted(int(w[4]) for w in words for r in targets if r[0] < (w[0] + w[2]) / 2 < r[2] and r[1] < (w[1] + w[3]) / 2 < r[3])
check(len(pairs) == 6 and len(targets) == 42 and len(pairbox) == 12 and inside == sorted(list(range(6, 13)) * 6)
      and sum(w[4] == 'and' and any(r[1] < (w[1] + w[3]) / 2 < r[3] for r in pairbox) for w in words) == 6,
      'K-1 Problem 6 has six rows, one for each of the six pairs, each with two boxes for the pair and targets '
      '6-12; exactly {2,3}, {2,5}, {3,4} cover 6-12 (should 8)')

# Should 11: 2-3 P4 asks about every length after 16 (3/4) and after 20 (3/5).
check('Can 3-rods and 4-rods build every length after 16? Can 3-rods and 5-rods build every length after 20?' in M[3]
      and max(gaps(3, 4)) == 5 and max(gaps(3, 5)) == 7
      and all(builds(3, 4, n) for n in (17, 18, 19)) and all(builds(3, 5, n) for n in (21, 22, 23)),
      'Grades 2-3 Problem 4 asks the two yes-or-no questions; the last gaps are 5 and 7, and 17-19 and 21-23 '
      'are buildable certificates (should 11)')

# Should 12: 2-3 P6 names the rods, not the counterexample; only 2/4 has gaps forever.
fives = list(combinations((2, 3, 4, 5, 7), 2))
forever = [p for p in fives if gcd(*p) > 1]
assert forever == [(2, 4)] and gaps(2, 4, 50) == list(range(1, 50, 2))
assert all(max(gaps(*p)) == p[0] * p[1] - p[0] - p[1] for p in fives if p not in forever)
check('Use rods 2, 3, 4, 5 and 7 to decide.' in M[4] and 'Test 2 and 4' not in M[4],
      'Grades 2-3 Problem 6 asks the claim with rods 2, 3, 4, 5 and 7; of the ten pairs only 2/4 has gaps '
      'forever (every odd length), and the other nine have last gap ab - a - b (should 12)')
check('Rod order does not count' not in M[1], 'Grades 2-3 Problem 2 no longer repeats the rule on order (could 14)')

# Should 2: 4-5 P2 asks for 3/5 and 4/5 only; P3-P4 settle 4/7.
p2 = U[1]
check('3 and 5; 4 and 5.' in p2 and '4 and 7' not in p2 and max(gaps(3, 5)) == 7 and max(gaps(4, 5)) == 11
      and all(builds(4, 5, n) for n in (12, 13, 14, 15)) and all(builds(4, 7, n) for n in (18, 19, 20, 21))
      and not builds(4, 7, 17),
      'Grades 4-5 Problem 2 asks for 3/5 (last gap 7) and 4/5 (last gap 11) only; 4/7 (17, with 18-21) is left '
      'to Problems 3 and 4 (should 2)')

# Should 7, coulds 15 and 16.
check('propose a rule that gives the last impossible length from the two rod lengths' in U[4]
      and [max(gaps(*p)) for p in ((3, 4), (3, 5), (4, 5), (4, 7), (5, 7))] == [5, 7, 11, 17, 23]
      and all(max(gaps(a, b)) == a * b - a - b for a, b in ((3, 4), (3, 5), (4, 5), (4, 7), (5, 7))),
      'Grades 4-5 Problem 7 asks for a rule giving the last gap; the five pairs met so far give 5, 7, 11, 17, 23, '
      'all ab - a - b (should 7)')
check('Find every way to build 24 with 3-rods and 4-rods. How can you change one way into another?' in U[3]
      and builds(3, 4, 24) == [(0, 6), (4, 3), (8, 0)],
      'Grades 4-5 Problem 6 is the shorter prompt; 24 has the three builds (0,6), (4,3), (8,0) (could 15)')
check('every length from some point on' in U[4] and 'sufficiently' not in U[4],
      'Grades 4-5 Problem 8 says "every length from some point on" (could 16)')

# Could 13: an even rod's label has the rod's colour behind it, hiding the cell line.
page = pymupdf.open(PDFS / 'k-1.pdf')[4]
rod = {tuple(round(c, 3) for c in d['fill']) for d in page.get_drawings() if d['type'] == 'fs'}
patches = [d for d in page.get_drawings() if d['type'] == 'f' and (d['rect'][2] - d['rect'][0]) * MM < 8]
check(len(rod) == 1 and len(patches) == 2 and all(tuple(round(c, 3) for c in d['fill']) in rod for d in patches),
      'K-1 Problem 5 draws a patch of the rod colour behind the labels of the 2- and 4-rods (could 13)')
