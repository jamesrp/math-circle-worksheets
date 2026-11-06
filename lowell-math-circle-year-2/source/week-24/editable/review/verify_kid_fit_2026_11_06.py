#!/usr/bin/env python3
"""Check the November 6, 2026 kid-fit release of Week 24 against the built PDFs.

Run from the package folder after `bash build.sh`, or pass the folder holding
k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf:

    python3 review/verify_kid_fit_2026_11_06.py [folder]

It reads the printed pages (pypdf) and recomputes the mathematics behind the new and
renumbered guide entries. Standard library plus pypdf.
"""
import itertools
import re
import sys
from fractions import Fraction
from pathlib import Path

from pypdf import PdfReader

PKG = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PKG / 'build'
fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


def flat(text):
    return ' '.join(text.split())


def wins(x, y):
    return sum(a > b for a in x for b in y)


def pages(name):
    return [flat(p.extract_text()) for p in PdfReader(OUT / f'{name}.pdf').pages]


K, M, U, GP = pages('k-1'), pages('grades-2-3'), pages('grades-4-5'), pages('facilitator-guide')
G = ' '.join(GP)
A, B, C = (2, 4, 9), (1, 6, 8), (3, 5, 7)

# Student packets: page counts, footers, problem numbers in order.
for name, pp, n, tag, probs in (('K-1', K, 9, 'F24-K-v4', 9), ('2-3', M, 8, 'F24-23-v3', 8), ('4-5', U, 8, 'F24-45-v4', 8)):
    check(len(pp) == n and all(tag in p for p in pp), f'{name}: {n} pages, every footer {tag}')
    found = [int(x) for x in re.findall(r'Problem (\d+):', ' '.join(pp))]
    check(found == list(range(1, probs + 1)), f'{name}: Problems 1-{probs} in order')
check('Play six rounds of each game' in K[0] and 'Is it better to pick first or second?' in M[0] and 'third player draws the cards' in U[0],
      'Problem 1 is the game in every band')

# Guide: packets, counts, pages.
check('F24-K-v4, F24-23-v3 and F24-45-v4 (9, 8 and 8 pages)' in G and 'all 25 numbered problems' in G, 'guide p. 1 names the packets and 25 problems')
check(len(GP) == 16, f'guide: 16 pages (overview, 14 numbered, route page), found {len(GP)}')
check(all('2026-11-06' in p for p in GP[1:15]) and '6 November 2026' in GP[0], 'guide: dated 2026-11-06 on every numbered page and the overview')
check(not any(s in G for s in ('F24-K-v3', '2026-10-23', '22 numbered', 'two distinguishable styles', 'adult secretly')), 'guide: no stale version, date or wording')
for head in ('K-1 Problem 1 Play A against B', 'Grades 2-3 and 4-5 Problem 1 Pick first or pick second', 'K-1 Problems 2 to 4',
             'K-1 Problems 5 to 7', 'K-1 Problems 8 and 9', 'Grades 2-3 Problems 2 to 4', 'Grades 2-3 Problems 5 to 8',
             'Grades 4-5 Problems 2 and 3', 'Grades 4-5 Problems 4 and 5', 'Grades 4-5 Problems 6 and 7', 'Grades 4-5 Problem 8'):
    check(head in G, f'guide heading "{head}"')
check('Hidden-bag letters' in G and 'removable slips' in G, 'guide p. 1: Grades 2-3 hidden-bag letters in the materials')
check('The cycle shows by counting all the card pairs' in GP[3], 'guide p. 3: the cycle shows by counting pairs, not one short game')

# Short games, from the actual decks.
def series(x, y, n):
    dist = {0: 1}
    for _ in range(n):
        nd = {}
        for k, v in dist.items():
            for u, w in itertools.product(x, y):
                nd[k + (u > w)] = nd.get(k + (u > w), 0) + v
        dist = nd
    tot = (len(x) * len(y)) ** n
    win = Fraction(sum(v for k, v in dist.items() if 2 * k > n), tot)
    tie = Fraction(dist.get(n // 2, 0), tot)
    return win, tie, 1 - win - tie

for n, cells in ((6, ('45.3%', '30.1%', '24.6%')), (10, ('51.9%', '23.1%', '25.0%'))):
    got = {series(x, y, n) for x, y in ((A, B), (B, C), (C, A))}
    check(len(got) == 1 and tuple(f'{100 * float(v):.1f}%' for v in got.pop()) == cells, f'{n}-round game: favored deck wins/ties/loses {cells}')
w6, t6, l6 = series(A, B, 6)
w10, t10, _ = series(A, B, 10)
champ = sum(p0 * p1 * p2 for (r0, p0), (r1, p1), (r2, p2) in itertools.product((('W', w6), ('T', t6), ('L', l6)), repeat=3)
            if (r0, r2) == ('W', 'L') or (r1, r0) == ('W', 'L') or (r2, r1) == ('W', 'L'))
check(round(float(w6 ** 3), 3) == 0.093 and 'about 1 time in 11' in G, 'K-1 P1: all three favored decks win only about 1 time in 11 (9.3%)')
check(round(float(champ), 2) == 0.33 and 'about 1 time in 3 some deck wins both' in G, 'K-1 P1: some deck wins both its games about 1 time in 3')
check(round(float(w6 + t6 / 2), 2) == 0.60 and round(float(w10 + t10 / 2), 2) == 0.63 and 'about 60%' in G and 'about 63%' in G,
      '2-3 P3: a six-round guess is right about 60%, a ten-round guess about 63%')
best = {n: [m for m, d in zip('ABC', (A, B, C)) if wins(d, o) > 4] for n, o in zip('ABC', (A, B, C))}
check(best == {'A': ['C'], 'B': ['A'], 'C': ['B']} and 'C against A, A against B, B against C' in G, 'P1 (2-5): second pick takes the deck that beats the first')

# Rewritten and annotated problems.
check('boxes read A beside side A-B, B beside B-C and C beside C-A' in G and [wins(A, B), wins(B, C), wins(C, A)] == [5, 5, 5], 'K-1 P4: triangle boxes')
swaps = []
for i, j in itertools.product(range(3), range(3)):
    a, b = list(A), list(B)
    a[i], b[j] = b[j], a[i]
    if wins(b, a) > wins(a, b):
        swaps.append((A[i], B[j]))
check(swaps == [(2, 1), (4, 1), (9, 1), (9, 6), (9, 8)] and all(x > y for x, y in swaps) and len(swaps) == sum(x > y for x in A for y in B),
      'K-1 P7: the five swaps are exactly those where A gives the larger card')
check(set(swaps) == {(x, 1) for x in A} | {(9, y) for y in B} and "whole row of B's 1 and the whole column of A's 9" in G, 'K-1 P7: marked boxes are B 1 row and A 9 column')
A6, B6 = tuple(v for v in A for _ in (0, 1)), tuple(v for v in B for _ in (0, 1))
A4, B4, C4 = (2, 2, 4, 9), (1, 1, 6, 8), (3, 3, 5, 7)
check((wins(A6, B6), wins(B6, A6)) == (20, 16) and 'A wins 20 of the 36 physical pairs against B and B wins 16' in G, '2-3 P6: six-card A 20, B 16')
check((wins(A4, B4), wins(C4, A4), wins(C4, B4), wins(B4, C4)) == (10, 10, 9, 7) and 'C now beats B 9 to 7' in G, '2-3 P6: four-card 10-6, 10-6, C over B 9-7')

print({'checks_failed': len(fails)})
sys.exit(1 if fails else 0)
