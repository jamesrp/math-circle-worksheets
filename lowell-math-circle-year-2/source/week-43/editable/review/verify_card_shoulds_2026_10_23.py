#!/usr/bin/env python3
"""Check the second set of October 23, 2026 card fixes to Week 43 (shoulds 2, 3, 6, 7 and 8,
coulds 10 and 11 in part, and the Sattolo naming in could 14) by enumeration and by reading
the reference PDFs.

Nothing is imported from the packet or guide builders. The PDFs are read with PyMuPDF
(in requirements.txt). The kit page is measured by materials/verify_materials.py. Run
from anywhere:
    python3 review/verify_card_shoulds_2026_10_23.py
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
CM = 72 / 2.54
checks = []


def run(start, story):
    """Swap slot k with slot story[k] (tickets count from 1), in order."""
    row = list(start)
    for k, t in enumerate(story):
        row[k], row[t - 1] = row[t - 1], row[k]
    return ''.join(row) if isinstance(start, str) else tuple(row)


def text(page):
    return ' '.join(page.get_text().split())


def frames(page, top, bottom=10 ** 4, wider=0.0):
    """Answer cells: unfilled gray!65 rectangles between two heights, wider than `wider` cm."""
    return [d['rect'] for d in page.get_drawings()
            if d.get('fill') is None and d.get('color') and abs(d['color'][0] - .675) < .01
            and top < d['rect'].y0 and d['rect'].y1 < bottom and d['rect'].width > wider * CM]


def block_top(page, start):
    return next(b[1] for b in page.get_text('blocks') if b[4].startswith(start))


def rows_of_three(cells):
    """Group cells into rows of three touching cells; return the number of rows."""
    by_line = defaultdict(list)
    for c in cells:
        by_line[round(c.y0)].append(c)
    n = 0
    for line in by_line.values():
        line.sort(key=lambda c: c.x0)
        i = 0
        while i < len(line):
            j = i
            while j + 1 < len(line) and abs(line[j + 1].x0 - line[j].x1) < 1:
                j += 1
            assert j - i + 1 == 3, [round(c.x0) for c in line]
            n += 1
            i = j + 1
    return n


k1, b23, b45 = (pymupdf.open(REF / f) for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf'))
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
src = json.loads((ROOT / 'facilitator-src' / 'guide.json').read_text())

# --- Enumeration --------------------------------------------------------------------------
two = {s: run('ABC', s) for s in product((1, 2, 3), (2, 3))}
assert sorted(two.values()) == sorted(map(''.join, permutations('ABC')))
three = defaultdict(list)
for s in product((1, 2, 3), repeat=3):
    three[run('ABC', s)].append(s)
assert [len(three[r]) for r in ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA')] == [4, 5, 5, 5, 4, 4]
assert run('ABC', (3, 2, 1)) == 'ABC' and run('ABC', (3, 2, 2)) == 'CAB' and (1, 2, 3) in three['ABC']
checks.append('should 2: the all-slots demonstration (3,2,1) ended at ABC, which (1,2,3) also makes; (3,2,2) ends at '
              'CAB; the 27 stories give ABC ACB BAC BCA CAB CBA 4, 5, 5, 5, 4, 4 times')

runs = list(product(two, repeat=6))
allsix = sum(len({two[s] for s in r}) == 6 for r in runs)
assert len(runs) == 6 ** 6 == 46656 and allsix == factorial(6) == 720 and Fraction(allsix, len(runs)) == Fraction(5, 324)
checks.append(f'should 7: of the 6^6 = 46,656 equally likely runs of six two-swap shuffles, {allsix} show all six '
              f'rows once (5/324, about 1 run in {len(runs) / allsix:.0f}); six repeats of (1,2) give ABC six times')

def one_cycle(p):
    length, x = 1, p[0]
    while x != 0:
        x, length = p[x], length + 1
    return length == len(p)


for n in range(3, 7):    # Sattolo: swap slot i with a slot drawn from i+1..n
    out = Counter(run(list(range(n)), s) for s in product(*[range(i + 2, n + 1) for i in range(n - 1)]))
    assert len(out) == factorial(n - 1) and set(out.values()) == {1} and all(one_cycle(p) for p in out)
assert sorted(Counter(run('ABC', (t, 3)) for t in (2, 3))) == ['BCA', 'CAB']
checks.append("could 14: the no-self-swap rule is Sattolo's: for n = 3 to 6 it makes each of the (n-1)! one-cycle "
              'orders by exactly one story (BCA and CAB for three cards)')

designs = []
subsets = [set(c) for k in range(1, 5) for c in combinations(range(1, 5), k)]
for S in product(subsets, repeat=3):
    stories = list(product(*[sorted(s) for s in S]))
    if len(stories) == 24 and len({run('ABCD', s) for s in stories}) == 24:
        designs.append([sorted(s) for s in S])
assert len(designs) == 6, designs
assert [[1, 4], [1, 2, 4], [1, 2, 3, 4]] in designs and [[1, 2, 3, 4], [2, 3, 4], [3, 4]] in designs
assert sorted(tuple(len(s) for s in d) for d in designs) == sorted(permutations((4, 3, 2)))
checks.append('could 10: exactly six choices of ticket sets for the swaps of slots 1, 2, 3 give one story per order of '
              'ABCD, one for each order of the set sizes 4, 3, 2; Fisher-Yates and {1,4}, {1,2,4}, {1,2,3,4} among them')

# --- Student pages --------------------------------------------------------------------------
pages = [text(p) for doc in (k1, b23, b45) for p in doc]
assert not any('Example: choose triangle' in t for t in pages)
checks.append('could 11: "Example: choose triangle, then square; circle is left." is gone from K-1 p. 2, '
              'Grades 2-3 p. 1 and Grades 4-5 p. 1 (the picture shows it)')

t = text(b23[3])
assert '3 with 2' in t and '3 with 1' not in t
last = sorted((w for w in b23[3].get_text('words') if w[4] in 'ABC' and len(w[4]) == 1
               and w[1] < block_top(b23[3], 'Problem 5')), key=lambda w: (round(w[1]), w[0]))
assert ''.join(w[4] for w in last[-3:]) == 'CAB', [w[4] for w in last]
checks.append('should 2: Grades 2-3 p. 4 demonstration ends "3 with 2" at C A B')

for doc, page, gone in ((b23, 0, 'Use the possible choices to decide.'),
                        (b45, 0, 'Settle the question using every possible choice story.'),
                        (b45, 1, 'Find all its choice stories and their final orders.'),
                        (b45, 2, 'a short run of random shuffles cannot settle the question')):
    assert gone not in text(doc[page]), gone
assert 'Problem 4: Can this rule give every order the same chance? Find an exact reason.' in text(b45[2])
hints = text(guide[1])
assert 'To decide fairness: “Use every possible choice story and its final row.” A short run of random shuffles ' \
       'cannot settle the question.' in hints
checks.append('should 3: the four method sentences are off the Grades 2-3 and 4-5 pages; the guide hints (p. 2) carry them')

spare = []
for name, page, start, end, wide, want, answers in (
        ('K-1 P1', k1[0], 'Problem 1', None, 1.5, 8, 6),
        ('K-1 P3', k1[2], 'Problem 3', None, 1.5, 8, 6),
        ('K-1 P4', k1[3], 'Problem 4', 'Problem 5', 1.2, 9, 6),
        ('Grades 2-3 P1', b23[0], 'Problem 1', None, 1.5, 8, 6),
        ('Grades 4-5 P1', b45[0], 'Problem 1', None, 1.5, 8, 6)):
    top = block_top(page, start)
    bottom = block_top(page, end) if end else 10 ** 4
    cells = frames(page, top, bottom, wide)
    if name == 'K-1 P1':
        mat = max(c.y1 for c in cells if c.width > 4 * CM)
        cells = [c for c in cells if c.y0 > mat]           # the answer rows below the slot mat
    n = rows_of_three(cells)
    assert n == want, (name, n)
    spare.append(f'{name} {n} rows for {answers} answers')
p4 = frames(k1[3], block_top(k1[3], 'Problem 4'), block_top(k1[3], 'Problem 5'), 1.2)
assert len({round(c.y0) for c in p4}) == 3 and all(c.width / CM > 1.5 for c in p4)
checks.append('should 6: spare rows: ' + '; '.join(spare) + ' (K-1 P4: three rows per missing ticket, two answers each)')

t = text(b23[2])
assert 'Problem 4: Shuffle six times with the two-swap rule. A friend says six shuffles must show all six rows once. ' \
       'Is the friend right?' in t
rec = frames(b23[2], block_top(b23[2], 'Problem 4'), wider=1.5)
assert rows_of_three(rec) == 6
key = text(guide[3])
assert '46,656' in key and '720' in key and 'about 1 run in 65' in key
checks.append('should 7: Grades 2-3 Problem 4 reads as the card gives it, with six records; guide p. 4 key gives 720 of 46,656')

g2 = text(guide[1])
assert 'Print week-43-materials.pdf' in g2 and 'physically unrehearsed' in g2
assert (ROOT / 'reference-pdfs' / 'materials.pdf').exists()
checks.append('should 8: guide p. 2 points to the card kit (week-43-materials.pdf, reference-pdfs/materials.pdf); '
              'materials/verify_materials.py measures it')

g1, g5 = text(guide[0]), text(guide[4])
assert "Sattolo's algorithm" in g1 and all(f'{w} (' in g1 for w in ('3', '63', '23', '42', '44'))
assert 'exactly six choices of ticket sets give one story per order' in g5
checks.append("could 14 and 10: guide p. 1 names the no-self-swap rule as Sattolo's with Weeks 3, 23, 42, 44, 63; "
              'guide p. 5 says other four-card designs pass')

for c in checks:
    print('PASS', c)
