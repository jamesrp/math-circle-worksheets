#!/usr/bin/env python3
"""Check the November 6, 2026 kid-fit revision of Week 12 against the reference PDFs.

Independent brute force for the mathematics (every perfect matching of 1..2n, filtered
by an interleaving test; nothing imported from figures.py or the guide builder), and
the reference PDFs for what is printed:

- K-1 order: P1 six-dot pairings, P2 odd and even circles, P3 drawn pairs, P4 eight-dot
  pairings (continued on page 5), P5 checking the six-dot collection, P6 neighbors.
  P4 has 3 + 6 = 9 frames, fewer than the 14 pairings.
- The reworded rules and questions (K-1 and Grades 4-5 rules, Grades 2-3 P2, Grades 4-5
  P4) and the Grades 4-5 mirror pair of five-edge trees.
- The guide's string lengths: every K-1 string mat is located on the printed page by
  its number labels, and every chord is measured. Neighbors are 2.7-4.0 cm apart and
  every other pair 5.1-8.6 cm, so a 3.5 cm string fits every neighbor pair and a
  7.5 cm string every other pair (its ends within a 15 mm disc of each dot, or at most
  12.5 mm past a dot centre). No noncrossing pairing needs more than five short or
  three long strings at once.
- The guide keys the new packet ids and puts K-1 P2 (parity) on page 3 and P5 (check)
  on page 4.

Needs pypdf and Poppler's pdftotext. Run from anywhere:
python3 review/verify_kid_fit_2026_11_06.py
"""
import math
import re
import subprocess
from itertools import combinations
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
MM = 72 / 25.4
SHORT, LONG = 35.0, 75.0           # mm, the guide's K-1 string lengths
checks = []


def matchings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for i in range(1, len(points)):
        for rest in matchings(points[1:i] + points[i + 1:]):
            yield ((a, points[i]),) + rest


def crossing(p, q):
    (a, b), (c, d) = sorted(p), sorted(q)
    return a < c < b < d or c < a < d < b


def noncrossing(n):
    return [m for m in matchings(tuple(range(1, n + 1)))
            if not any(crossing(p, q) for p, q in combinations(m, 2))]


def text(pdf, page):
    return ' '.join(PdfReader(pdf).pages[page - 1].extract_text().split())


def labels(pdf, page):
    out = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), str(pdf), '-'],
                         check=True, capture_output=True, text=True).stdout
    return [((float(a) + float(c)) / 2 / MM, (float(b) + float(d)) / 2 / MM, w)
            for a, b, c, d, w in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', out)]


# Counts and the string budget, by brute force.
NC = {n: noncrossing(n) for n in (6, 8, 10)}
assert [len(NC[n]) for n in (6, 8, 10)] == [5, 14, 42]
nb = lambda n, a, b: (b - a) % n in (1, n - 1)
most_long = max(sum(not nb(10, a, b) for a, b in m) for n in NC for m in NC[n] if n == 10)
most_short = max(sum(nb(n, a, b) for a, b in m) for n in NC for m in NC[n])
assert (most_long, most_short) == (3, 5), (most_long, most_short)
assert max(sum(not nb(n, a, b) for a, b in m) for n in (6, 8) for m in NC[n]) <= 3
checks.append('5, 14 and 42 noncrossing pairings of 6, 8 and 10 circle dots; at most 3 non-neighbor and 5 neighbor strings at once')

# K-1 order, frames and wording.
k1 = REF / 'k-1.pdf'
assert len(PdfReader(k1).pages) == 7
heads = {1: 'Problem 1: Find every way to pair six dots.',
         2: 'Problem 2: Pair all the dots in each circle if you can.',
         3: 'Problem 3: For each drawn pair, put a string on the large circle and leave it there.',
         4: 'Problem 4: Pair eight dots in as many different ways as you can.',
         5: 'Problem 4 (continued)',
         6: 'Problem 5: Check your six-dot pairings from Problem 1.',
         7: 'Problem 6: Can you pair eight dots without joining any two neighbors around the circle?'}
for page, head in heads.items():
    assert head in text(k1, page), (page, head)
assert 'Strings stay inside the circle and do not cross.' in text(k1, 1)
assert 'Use strings on large circles' not in text(k1, 1)
checks.append('K-1 pages 1-7 carry P1, P2 (odd and even), P3, P4, P4 continued, P5 (check), P6; the rules say strings stay inside the circle')
eights = lambda page: sum(1 for w in labels(k1, page) if w[2] == '8')
frames = (eights(4) - 1, eights(5))   # page 4 less its mat
assert frames == (3, 6) and sum(frames) < 14, frames
checks.append('K-1 P4 has 3 frames on page 4 and 6 on page 5: 9 frames for the 14 pairings')

# Measure every K-1 string mat from its printed labels (12.5 mm outside the dots).
MATS = {1: (61, 188, 6, 32), 2: (108, 102, 10, 43), 3: (108, 104, 8, 40), 4: (108, 104, 8, 40),
        6: (108, 110, 6, 40), 7: (108, 107, 8, 40)}
near, other = [], []
for page, (x, y, n, r) in MATS.items():
    ws = labels(k1, page)
    for i in range(1, n + 1):
        th = math.radians(90 - (i - 1) * 360 / n)
        R = r + 12.5 + (1 if i >= 10 else 0)
        ex, ey = x + R * math.cos(th), y - R * math.sin(th)
        assert any(w[2] == str(i) and math.dist((w[0], w[1]), (ex, ey)) < 1.5 for w in ws), (page, i)
    for k in range(1, n // 2 + 1):
        c = 2 * r * math.sin(math.pi * k / n)
        (near if k == 1 else other).append(c)
fits = lambda L, c: c - 15 <= L <= c + 25
assert all(fits(SHORT, c) for c in near) and all(fits(LONG, c) for c in other)
assert not any(fits(SHORT, c) for c in other) and not any(fits(LONG, c) for c in near)
assert round(min(near) / 10, 1) == 2.7 and round(max(near) / 10, 1) == 4.0
assert round(min(other) / 10, 1) == 5.1 and round(max(other) / 10, 1) == 8.6
checks.append(f'K-1 mats located on pages {sorted(MATS)}: neighbors {min(near)/10:.2f}-{max(near)/10:.2f} cm apart, other pairs '
              f'{min(other)/10:.2f}-{max(other)/10:.2f} cm; 3.5 cm strings fit every neighbor pair and 7.5 cm strings every other pair')

# Grades 2-3 and 4-5 wording; the mirror pair.
assert 'Can a pairing ever make a path that goes below the dark line?' in text(REF / 'grades-2-3.pdf', 2)
h = REF / 'grades-4-5.pdf'
assert 'Every other dot hangs by one edge from exactly one dot above it.' in text(h, 1)
assert 'Two different trees with five edges:' in text(h, 1)
assert 'Describe how to rebuild' not in ' '.join(text(h, i) for i in range(1, 7))
rules = (ROOT.parent / 'problems/00-rules.md' if (ROOT.parent / 'problems').exists() else ROOT / 'problem-files/problems/00-rules.md').read_text()
codes = re.findall(r"tree\(\d+,\d+,'([UD]+)'", (ROOT.parent / 'figures.py' if (ROOT.parent / 'figures.py').exists() else ROOT / 'problem-files/figures.py').read_text().split('def five_edge_pair')[1].split('\ndef ')[0])
assert 'five_edge_pair(' in rules and len(codes) == 2
mirror = lambda w: ''.join('U' if c == 'D' else 'D' for c in reversed(w))
assert codes[0] != codes[1] and mirror(codes[0]) == codes[1] and all(len(w) == 10 for w in codes)
checks.append(f'grades 2-3 P2 asks about going below the dark line; grades 4-5 rules show {codes[0]} beside its mirror image {codes[1]}; P4 no longer asks for the rebuilding')

# Guide.
g = REF / 'facilitator-guide.pdf'
assert len(PdfReader(g).pages) == 10
assert 'W12-K-v5, W12-23-v4 and W12-45-v5' in text(g, 1)
assert 'Ten, four and six dots are possible' in text(g, 3) and 'Check the P1 collection' in text(g, 4)
assert '9 larger frames' in text(g, 4) and '3.5 cm' in text(g, 2) and '7.5 cm' in text(g, 2)
assert 'mirror images' in text(g, 8) and 'Kid-fit revision, 6 November 2026' in text(g, 9)
checks.append('guide: 10 pages; keys W12-K-v5, W12-23-v4, W12-45-v5; K-1 P2 parity on page 3, P5 check and the 9 frames on page 4; string lengths on page 2')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 12 kid-fit checks')
