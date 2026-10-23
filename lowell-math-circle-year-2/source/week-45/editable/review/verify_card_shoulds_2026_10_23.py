#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes to Week 45 (shoulds 1-7, coulds 10, 11, 12, 13) by
enumeration and by reading the reference PDFs.

Every claim, count and key that changed is recomputed from the six faces: the pairs of
Grades 2-3 Problem 1, the covered-number facts of Grades 4-5 Problem 3, K-1 Problem 4
under the page-1 rule, the answer slots of K-1 Problems 5 and 7, and the answer to every
hint and extension now in the guide. Nothing is imported from the packet or guide builders.
The PDFs are read with PyMuPDF (in requirements.txt). Run from anywhere:
    python3 review/verify_card_shoulds_2026_10_23.py
Should 8 (the bonus guide's 3 x 2 x 2) is checked in the repository by
plans/review/checks/week-45/check_card_shoulds.py, since the bonus is a separate package.
"""
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
CM = 72 / 2.54
checks = []

SHOW = {1: 'R', 2: 'R', 3: 'R', 4: 'B', 5: 'B', 6: 'B'}
OTHER = {1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5}
HIDE = {t: SHOW[OTHER[t]] for t in SHOW}
CARDS = {'RR': (1, 2), 'RB': (3, 4), 'BB': (5, 6)}
T = set(SHOW)


def ways(cup, clue='R'):
    return Counter(HIDE[t] for t in cup if SHOW[t] == clue)


def tie(cup, clue='R'):
    w = ways(cup, clue)
    return w['R'] == w['B'] > 0


def subsets(k=None):
    return [set(c) for n in (range(7) if k is None else [k]) for c in combinations(sorted(T), n)]


def text(page):
    """Page text on one line; a word broken at a line-end hyphen is joined (red- showing -> red-showing)."""
    return ' '.join(page.get_text().split()).replace('- ', '-')


def frames(page, top, bottom=10 ** 4):
    """Answer cells: unfilled gray!65 rectangles between two heights."""
    return [d['rect'] for d in page.get_drawings()
            if d.get('fill') is None and d.get('color') and abs(d['color'][0] - .675) < .01
            and top < d['rect'].y0 and d['rect'].y1 < bottom]


def block_top(page, start):
    return next(b[1] for b in page.get_text('blocks') if b[4].startswith(start))


k1, b23, b45 = (pymupdf.open(REF / f) for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf'))
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
gtext = [text(p) for p in guide]

# --- Student pages: wording --------------------------------------------------------------
pages = {(name, i + 1): text(p) for name, doc in (('K-1', k1), ('2-3', b23), ('4-5', b45)) for i, p in enumerate(doc)}
for (name, n), t in pages.items():
    assert f'W45-{ {"K-1": "k-1", "2-3": "grades-2-3", "4-5": "grades-4-5"}[name] }-v3' in t, (name, n)
    for gone in ('Use matching-size cards', 'small marks', 'show the face named by each draw', 'Explain using the tickets',
                 'Account for every ticket', 'Give a possible set', 'face mark', 'Choose and orient', 'show its red face',
                 'Which tickets show the same color on both faces', 'remove both its tickets', 'bet-ter', 'dif-fer'):
        assert gone not in t, (name, n, gone)
rule = 'The small numbers match the six tickets. A secret ticket picks the face that shows, with its number covered. You see only the color.'
assert pages[('K-1', 1)].count(rule) == 1 and 'same chance' not in pages[('K-1', 1)]
for b in ('2-3', '4-5'):
    assert rule + ' Every ticket has the same chance.' in pages[(b, 1)]
checks.append('should 2: page 1 of every band gives the card\'s three sentences and no operator paragraph; Grades 2-3 '
              'and 4-5 add "Every ticket has the same chance." (their chances rest on it); every footer reads v3')

assert 'Only tickets 1 and 3 are in the cup.' in pages[('K-1', 3)]
for b in ('2-3', '4-5'):
    assert 'Only tickets 1 and 3 are in the cup, each with the same chance.' in pages[(b, 3)]
assert 'Problem 4: Add just one extra ticket to this chooser: 2, 4, 5, or 6. Among red-showing rounds' in pages[('K-1', 3)]
before = ways({1, 3})
assert before['R'] == before['B'] == 1
after = {t: ways({1, 3, t}) for t in (2, 4, 5, 6)}
assert after[2] == Counter(R=2, B=1) and all(after[t] == before for t in (4, 5, 6))
# The old p. 3 rule ("show its red face") would make ticket 4 show face 3: blue 2-1, and a fourth P5 cup.
red_face = lambda t: t if SHOW[t] == 'R' else OTHER[t]
old = Counter(HIDE[red_face(t)] for t in (1, 3, 4))
assert old == Counter(R=1, B=2)
checks.append('should 1: p. 3 reads "Only tickets 1 and 3 are in the cup" under the page-1 rule; K-1 Problem 4 lost '
              '"and show the face named by each draw"; under that rule {1,3} ties, adding 2 gives red 2-1 and adding '
              '4, 5 or 6 leaves the tie (the old "show its red face" reading gave blue 2-1 for ticket 4)')

assert 'Problem 2: You are told only that red is showing. Which hidden color is the better guess, and why?' in pages[('2-3', 2)]
assert 'Problem 3: You are told only that blue is showing. Does the better guess change? red underneath' in pages[('2-3', 2)]
assert 'Problem 5: Could six red-showing rounds prove that the hidden-color chances differ?' in pages[('4-5', 3)]
checks.append('should 3: Grades 2-3 P2 ends "Which hidden color is the better guess, and why?"; the second sentences '
              'of Grades 2-3 P3 and Grades 4-5 P5 are gone')

# --- Should 4: Grades 2-3 Problem 1 -------------------------------------------------------
pairs = [set(p) for p in combinations(sorted(T), 2)
         if SHOW[p[0]] == SHOW[p[1]] and HIDE[p[0]] != HIDE[p[1]]]
assert pairs == [{1, 3}, {2, 3}, {4, 5}, {4, 6}]
assert 'Problem 1: Find every pair of tickets that show the same color but hide different colors.' in pages[('2-3', 1)]
top = block_top(b23[0], 'Problem 1')
cells = frames(b23[0], top)
assert len(cells) == 12 and all(abs(c.width - 1.5 * CM) < 1 and abs(c.height - 1.5 * CM) < 1 for c in cells)
assert len({round(c.y0) for c in cells}) == 2
key = gtext[4]
assert all(s in key for s in ('{1,3}', '{2,3}', '{4,5}', '{4,6}', 'Two of the six answer slots stay empty'))
checks.append('should 4: Grades 2-3 P1 asks for every pair that shows alike and hides differently: {1,3}, {2,3}, '
              '{4,5}, {4,6}; six two-ticket slots (12 cells of 1.5 cm), and guide p. 5 keys the four pairs')

# --- Should 5: Grades 4-5 Problem 3 -------------------------------------------------------
red = [f for f in (1, 2, 3, 4, 5, 6) if SHOW[f] == 'R']
facts = {'the number': None, 'odd': lambda f: f % 2 == 1, 'even': lambda f: f % 2 == 0, '3 or less': lambda f: f <= 3}
assert {f: HIDE[f] for f in red} == {1: 'R', 2: 'R', 3: 'B'}          # the number decides
odd = Counter(HIDE[f] for f in red if facts['odd'](f))
even = Counter(HIDE[f] for f in red if facts['even'](f))
low = Counter(HIDE[f] for f in red if facts['3 or less'](f))
assert odd == Counter(R=1, B=1) and even == Counter(R=1) and low == Counter(R=2, B=1)
t = pages[('4-5', 2)]
assert ('Problem 3: The chooser also tells you one fact about the covered number: the number, whether it is odd or even, '
        'or whether it is 3 or less. After a red clue, what does each fact do to the better guess?') in t
assert all(lbl in t for lbl in ('the number', 'odd or even', '3 or less'))
assert '“Red is showing' in t and 'same chance.” Does' in t
k = gtext[6]
assert all(s in k for s in ('The number decides', 'Odd leaves faces 1 and 3: a tie', 'Even leaves face 2: red for certain',
                            '3 or less is true of all three faces'))
checks.append('should 5: Grades 4-5 P3 asks about the three facts, with three labelled answer rows; after a red clue '
              'the number decides, odd ties 1-1, even leaves red only, 3 or less keeps red 2-1; guide p. 7 keys it; '
              'could 13: the friend\'s quotation now prints with curly quotes')

# --- Should 6: K-1 Problems 5 and 7 -------------------------------------------------------
p5 = [c for c in subsets(3) if ways(c)['B'] > 0 and ways(c)['R'] == 0]
assert p5 == [{3, 4, 5}, {3, 4, 6}, {3, 5, 6}]
cells = frames(k1[2], block_top(k1[2], 'Problem 5'))
assert len(cells) == 15 and all(abs(c.width - 1.25 * CM) < 1 for c in cells)
p7 = [c for c in subsets(2) if tie(c)]
assert p7 == [{1, 3}, {2, 3}]
cells = frames(k1[3], block_top(k1[3], 'Problem 7'))
assert len(cells) == 4 and len({round(c.y0) for c in cells}) == 1
assert 'red showing gives a tie between the hidden colors. Red must sometimes show.' in pages[('K-1', 4)]
checks.append('should 6: K-1 P5 has five groups of three boxes for its 3 answers ({3,4,5}, {3,4,6}, {3,5,6}); '
              'K-1 P7 has four boxes for its 2 answers ({1,3}, {2,3}); could 13: P7 says "a tie"')

for b in ('K-1', '2-3'):
    assert "Lay each card's two tickets on it, so removing a card takes both." in pages[(b, 4)].replace('’', "'")
checks.append('could 10: K-1 and Grades 2-3 p. 4 have children lay each card\'s two tickets on it')

# --- Should 7 and coulds 11, 12: the guide ------------------------------------------------
g2 = gtext[1]
for s in ('For eleven children', 'pairs play four to six rounds', 'Keep no tally', '35-40 minutes at the tables',
          'Problems 1-3 in each band (page 9)', 'ends with a hint to use only if needed and an extension'):
    assert s in g2, s
assert 'For ten children' not in g2 and '57-60' not in g2
keys = ' '.join(gtext[2:8])
assert keys.count('Hint.') == keys.count('Extension.') == 20
route = gtext[8]
assert 'in 35-40 minutes at the tables' in route and 'bonus companion, week-45-bonus.pdf' in route
assert len(guide) == 9
checks.append('should 7: guide p. 2 runs the first routes in 35-40 minutes after four to six paired rounds with no tally; '
              'all 20 problems have a hint and an extension (pp. 3-8); could 11: eleven children; could 12: the route '
              'page (p. 9) names the bonus as the Grades 4-5 continuation')

# --- Answers to the new extensions --------------------------------------------------------
cross = [set(p) for p in combinations(sorted(T), 2) if SHOW[p[0]] != SHOW[p[1]] and HIDE[p[0]] == HIDE[p[1]]]
assert cross == [{1, 4}, {2, 4}, {3, 5}, {3, 6}]
red_blue = [set(r) for r in combinations(sorted(T), 2) if ways(T - set(r))['B'] > 0 and ways(T - set(r))['R'] == 0]
assert red_blue == [{1, 2}]
blue_red = [set(r) for r in combinations(sorted(T), 2) if ways(T - set(r), 'B')['R'] > 0 and ways(T - set(r), 'B')['B'] == 0]
assert blue_red == [{5, 6}]
for extra in subsets():
    cup = {1, 3} | (extra - {1, 3})
    w = ways(cup)
    assert not w['B'] > w['R']
assert [c for c in subsets(4) if ways(c)['B'] > 0 and ways(c)['R'] == 0] == [{3, 4, 5, 6}]
blue_only_red = [name for name, pair in CARDS.items() if ways(T - set(pair), 'B')['R'] > 0 == ways(T - set(pair), 'B')['B']]
assert blue_only_red == ['BB']
three = [c for c in subsets(3) if tie(c)]
assert len(three) == 6 and all(3 in c and len(c & {1, 2}) == 1 for c in three)
match = sum(SHOW[t] == HIDE[t] for t in T)
assert Fraction(match, 6) == Fraction(2, 3)
assert [t for t in T if tie(T - {t}, 'B')] == [5, 6]
assert ways({1, 2, 3}) == ways(T)
two_cards = {}
for keep in CARDS:
    w = ways(set(CARDS[keep]))
    two_cards[keep] = 'never' if not w else ('red' if w['B'] == 0 else 'blue')
assert two_cards == {'RR': 'red', 'RB': 'blue', 'BB': 'never'}
assert [t for t in (1, 2, 3, 4, 5, 6) if ways(T - {t})['R'] == ways(T - {t})['B'] > 0] == [1, 2]
for f in (lambda f: f > 2, lambda f: f == 3):
    assert Counter(HIDE[x] for x in red if f(x)) == Counter(B=1)
# any fact that leaves blue ahead keeps face 3 and drops faces 1 and 2
for kept in subsets():
    w = Counter(HIDE[x] for x in kept if x in red)
    if w['B'] > w['R']:
        assert w == Counter(B=1)
two_thirds = [c for c in subsets() if sum(ways(c).values()) and Fraction(ways(c)['R'], sum(ways(c).values())) == Fraction(2, 3)]
assert len(two_thirds) == 8 and all({1, 2, 3} <= c for c in two_thirds)
assert Fraction(2, 3) ** 6 == Fraction(64, 729) and Fraction(1, 2) ** 6 == Fraction(1, 64)
assert round(float(Fraction(64, 729) / Fraction(1, 64)), 1) == 5.6
blue_fair = [c for c in subsets() if tie(c, 'B')]
both = [c for c in blue_fair if tie(c)]
assert len(blue_fair) == 16 and len(both) == 4
for a, b in product(range(4), range(7)):
    w = Counter(R=2 * a, B=b)
    if w['R'] == w['B'] > 0:
        assert b == 2 * a
    if a + b and Fraction(w['R'], w['R'] + w['B']) == Fraction(3, 4):
        assert 2 * a == 3 * b
assert Fraction(2 * 3, 2 * 3 + 2) == Fraction(3, 4) and 2 * 1 == 2
checks.append('extensions: every answer printed in the guide\'s 20 extensions is recomputed (cross pairs, removals, '
              'additions, four-ticket and three-ticket cups, 2/3 matches, two-card removals, covered-number facts, '
              'eight 2/3 cups, (2/3)^6 against (1/2)^6, 16 blue-fair and 4 both-fair subsets, card copies b = 2a and 2a = 3b)')

for c in checks:
    print('PASS', c)
