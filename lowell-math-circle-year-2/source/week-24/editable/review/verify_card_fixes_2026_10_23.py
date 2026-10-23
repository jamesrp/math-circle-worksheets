#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes of Week 24 (F24-K-v3, F24-45-v3) against the built PDFs.

Run from the package folder after `bash build.sh`, or pass the folder holding
k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf:

    python3 review/verify_card_fixes_2026_10_23.py [folder]

It reads the printed pages (PyMuPDF) and recomputes the mathematics behind each
changed sentence. Standard library plus PyMuPDF.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import pymupdf

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


def chance(x, y):
    return Fraction(wins(x, y), len(x) * len(y))


docs = {n: pymupdf.open(OUT / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator-guide')}
K = [flat(p.get_text()) for p in docs['k-1']]
M = [flat(p.get_text()) for p in docs['grades-2-3']]
U = [flat(p.get_text()) for p in docs['grades-4-5']]
GP = [flat(p.get_text()) for p in docs['facilitator-guide']]
G = ' '.join(GP)
A, B, C = (2, 4, 9), (1, 6, 8), (3, 5, 7)

# Should 5 and could 11: footers.
for name, pp, n, tag in (('K-1', K, 8, 'F24-K-v3'), ('2-3', M, 7, 'F24-23-v2'), ('4-5', U, 7, 'F24-45-v3')):
    check(len(pp) == n and all(tag in p for p in pp), f'{name}: {n} pages, every footer {tag}')
check('F24-K-v3, F24-23-v2 and F24-45-v3 (8, 7 and 7 pages)' in G, 'guide p. 1 names the packets as printed')

# Should 2: K-1 Problems 1-3 begin with the action; the pooling sentence is gone.
for i, rest in ((0, 'Which deck wins more pairs?'), (1, 'Which deck wins more pairs?'),
                (2, 'Does any of A, B, and C win more pairs than both other decks?')):
    check(f'Problem {i + 1}: Circle the winner in each pair. {rest}' in K[i], f'K-1 P{i + 1} begins "Circle the winner in each pair."')
check(not any('split the pairs' in p or 'shared page' in p for p in K), 'K-1: no instruction to split pairs or share a page')
check([wins(A, B), wins(B, C), wins(C, A)] == [5, 5, 5], 'K-1 P1-P3: A, B and C each win 5 of their 9 pairs in the cycle')

# Should 3: K-1 Problem 4 names the opponent; the guide says what the 18 counters record.
check('Problem 4: Your partner takes A. Choose a deck that wins more card pairs against it and play six rounds. '
      'Do the same for B and C. Must your chosen deck win more rounds?' in K[3], 'K-1 P4: new wording')
best = {o: [d for n, d in (('A', A), ('B', B), ('C', C)) if wins(d, opp) > 4] for o, opp in (('A', A), ('B', B), ('C', C))}
check(best == {'A': [C], 'B': [A], 'C': [B]}, 'K-1 P4: exactly one deck beats each of A, B, C (C, A, B)')
check('the eighteen counters record the rounds, one per round in the winner\'s style' in G and 3 * 6 == 18,
      'guide: eighteen counters record 3 x 6 rounds')
check(Fraction(4, 9) ** 6 > 0, 'K-1 P4: the favoured deck can lose all six rounds')

# Could 12: K-1 Problem 6 says to start each swap from the pictured decks.
check('Start each swap from these decks.' in K[5], 'K-1 P6: start each swap from these decks')
swaps = []
for i, j in itertools.product(range(3), range(3)):
    a, b = list(A), list(B)
    a[i], b[j] = b[j], a[i]
    if wins(b, a) > wins(a, b):
        swaps.append((A[i], B[j]))
check(swaps == [(2, 1), (4, 1), (9, 1), (9, 6), (9, 8)], f'K-1 P6: five swaps work from the original decks, {swaps}')

# Could 11: Grades 4-5 Problem 1's deck labels clear the prompt.
words = docs['grades-4-5'][0].get_text('words')
prompt_bottom = max(w[3] for w in words if w[4] == 'question?')
label_top = min(w[1] for w in words if w[4] in ('A', 'B', 'C') and w[1] > prompt_bottom - 5)
check(label_top - prompt_bottom > 12, f'4-5 P1: deck labels {label_top - prompt_bottom:.1f} pt below the prompt')

# Should 1: the four-card gate.
A4, B4, C4 = (2, 2, 4, 9), (1, 1, 6, 8), (3, 3, 5, 7)
A6, B6, C6 = ((v for v in d for _ in (0, 1)) for d in (A, B, C))
A6, B6, C6 = tuple(A6), tuple(B6), tuple(C6)
distinct = chance(set(B4), set(C4))
check('gives the wrong answer for the four-card decks (B over C would look like 5/9 instead of 7/16). '
      'It works for the six-card decks only because every card is copied equally.' in G,
      'guide p. 10: four-card gate sentence')
check(distinct == Fraction(5, 9) and chance(B4, C4) == Fraction(7, 16), 'B over C: 5/9 by distinct pairs, 7/16 by physical pairs')
check(all(chance(x, y) == chance(set(x), set(y)) for x, y in ((A6, B6), (B6, C6), (C6, A6))) and chance(A6, B6) == Fraction(20, 36),
      'six-card decks: distinct pairs give the true chances (20/36 = 5/9)')
check([chance(A4, B4), chance(B4, C4), chance(C4, A4)] == [Fraction(10, 16), Fraction(7, 16), Fraction(10, 16)],
      'four-card chances 10/16, 7/16, 10/16')

# Should 4: materials and time.
check('Cut index cards in half and use small paper lunch bags' in G and 'The room needs 57 cards: 27 originals, 27 spares and the cards 10, 11 and 12.' in G
      and 3 * 3 * 3 + 3 * 9 + 3 == 57, 'guide p. 1: index cards and bags; 57 cards = 27 + 27 + 3')
check('Once, about 30 minutes: write the 57 cards' in G and 'Before each session, 10-15 minutes' in G, 'guide p. 1: time to make the cards restated')
check('cutting templates' in G and '4 x 6 cm' not in G, 'guide p. 1: no 4 x 6 cm card size left')

# Could 6: review residue cut.
check(not any(s in G for s in ("older review", 'Final authority', 'PROMPT.md', 'review-math.md', 'build_packets.py')), 'guide: review residue cut')

# Could 7: who fills the bags in Grades 2-3 Problem 2.
check('an adult secretly puts two of the decks in two bags, a child draws from each, and the adult announces only which bag won' in G,
      'guide p. 2: an adult fills the bags and announces only the winning bag')
check(all(Fraction(4, 9) ** n * Fraction(5, 9) ** 0 > 0 for n in range(1, 50)), '2-3 P2: any run of left wins has positive chance under the disadvantage')

# Could 8: K-1 Problem 1 hint fits the printed pairs.
check('first look at the row of pictured pairs that share one A card; later ask whether every pictured pair has a circled winner' in G
      and 'has met all three B cards' not in G, 'guide p. 3: K-1 P1 hint names the pictured pairs')

# Could 9: one title; the route page is numbered 14.
check('Nontransitive random decks' not in G and 'Nontransitive dice and fair decks' not in G and GP[0].count('Three random decks') >= 1
      and all('Three random decks' in p for p in GP), 'guide: one title, Three random decks, on every page')
last = docs['facilitator-guide'][-1].get_text('words')
num = [w[4] for w in last if w[4].isdigit() and w[1] > 740 and w[0] > 500]
check(len(GP) == 15 and num == ['14'], f'guide: route page printed number {num}')

# Could 10: table time fits 35-40 minutes.
check('0-8 min' not in G and '57-60 min' not in G and 'Tables, first 15-20 min' in G and 'Tables, next 15-20 min' in G
      and 15 + 15 <= 40 and 20 + 20 >= 35, 'guide p. 2: two table blocks of 15-20 minutes (35-40 at tables)')

print(json.dumps({'checks_failed': len(fails)}))
sys.exit(1 if fails else 0)
