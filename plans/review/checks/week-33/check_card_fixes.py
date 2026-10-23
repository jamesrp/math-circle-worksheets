#!/usr/bin/env python3
"""Check the Week 33 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-33-k-1.pdf, week-33-grades-2-3.pdf, week-33-grades-4-5.pdf,
week-33-facilitator.pdf and week-33-bonus-facilitator.pdf (default: the print
folder). Needs PyMuPDF. Each fix is checked in the printed words and drawings,
and each mathematical claim it relies on is recomputed here.
"""
from itertools import product
from pathlib import Path
import math
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2' / 'week-33'
CM = 72 / 2.54
FAILS = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


def doc(name):
    return pymupdf.open(FOLDER / f'week-33-{name}.pdf')


def words(page):
    return re.sub(r'\s+', ' ', page.get_text()).strip()


def boards(page):
    """Ring boards on a page: (centre x, centre y, radius) in cm and the number of bead spots on each."""
    rings, beads = [], []
    for d in page.get_drawings():
        r = d['rect']
        if [i[0] for i in d['items']] != ['c'] * 4 or abs(r.width - r.height) > .01:
            continue
        c = ((r.x0 + r.x1) / 2 / CM, (r.y0 + r.y1) / 2 / CM, r.width / 2 / CM)
        if d['type'] == 's' and d['color'] and .6 < d['color'][0] < .75:
            rings.append(c)
        elif 'f' in d['type']:
            beads.append(c)
    out = []
    for x, y, r in rings:
        n = sum(1 for bx, by, _ in beads if abs(math.hypot(bx - x, by - y) - r) < .02)
        out.append((round(x, 2), round(y, 2), round(r, 2), n))
    return out


def readouts(word):
    return {word[i:] + word[:i] for i in range(len(word))}


def mixed_counts(n):
    return sorted({len(readouts(''.join(w))) for w in product('AB', repeat=n) if len(set(w)) == 2})


def rings_of(n):
    return {min(readouts(''.join(w))) for w in product('AB', repeat=n)}


k, m, u, g = doc('k-1'), doc('grades-2-3'), doc('grades-4-5'), doc('facilitator')
G = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in g))

# The critic follow-up (e33eed1, v4) changed P1 and the 4-5 P5 key word after these card fixes; the expectations
# below follow v4 where it differs (six P1 boards of radius 1.75 cm; key word AAAAABBBB).  check_critic_fixes.py
# checks the follow-up itself.
check('packets are v4 with 6, 6 and 6 pages', [len(k), len(m), len(u)] == [6, 6, 6] and all(
    f'F33-{t}-v4' in words(p) for d, t in ((k, 'K'), (m, '23'), (u, '45')) for p in d))

# Fix 1: four three-bead boards on page 1 in every band (six since v4); no AAA sentence in the launch
three = rings_of(3)
for name, d in (('K-1', k), ('2-3', m), ('4-5', u)):
    b = [x for x in boards(d[0]) if x[2] > 1.5]
    check(f'{name} P1 has six three-bead boards of radius 1.75 cm (four of 2.3 cm in v3)', len(b) == 6 and all(x[2] == 1.75 and x[3] == 3 for x in b))
check(f'there are exactly four three-bead rings {sorted(three)}, and six A and six B counters build all four at once',
      len(three) == 4 and sum(w.count('A') for w in three) == 6 and sum(w.count('B') for w in three) == 6)
check('launch no longer shows AAA', 'Show AAA as a different ring' not in G)

# Could 7: each moved "start" label in the example sits nearer its own ring than any other
for name, d in (('K-1', k), ('2-3', m), ('4-5', u)):
    ex = [x for x in boards(d[0]) if x[2] < 1.5]
    spans = [sp for bl in d[0].get_text('dict')['blocks'] for ln in bl.get('lines', []) for sp in ln['spans']]
    labels = [((sp['bbox'][0] + sp['bbox'][2]) / 2 / CM, (sp['bbox'][1] + sp['bbox'][3]) / 2 / CM) for sp in spans
              if sp['text'].strip() == 'start' and abs(sp['size'] - 9) < .2 and sp['bbox'][1] / CM < 8]
    owners = [min(range(3), key=lambda i: math.hypot(lx - ex[i][0], ly - ex[i][1])) for lx, ly in labels]
    gap = min(math.dist(a, b) for i, a in enumerate(labels) for b in labels[i + 1:])
    check(f'{name} example: one start label per ring, each nearest its own ring, at least 3 cm apart ({gap:.2f} cm)',
          len(ex) == 3 and sorted(owners) == [0, 1, 2] and gap >= 3)

# Fix 2: six, seven and nine beads before 4-5's prime rule; K-1's six-bead problem ends 2-3
p5 = words(u[4])
check('4-5 P5 wording', 'Problem 5: Which numbers of different readouts can a ring using both A and B have on six beads? On seven? On nine?' in p5)
check('4-5 P5 boards have 6, 7 and 9 bead spots', sorted(x[3] for x in boards(u[4])) == [6, 7, 9])
check('4-5 prime rule and colour count are now P6 and P7 on page 6',
      'Problem 6: A prime number has exactly two positive divisors' in words(u[5]) and 'Problem 7: How many five-bead rings' in words(u[5]))
check(f'mixed rings: six beads {mixed_counts(6)}, seven {mixed_counts(7)}, nine {mixed_counts(9)}',
      mixed_counts(6) == [2, 3, 6] and mixed_counts(7) == [7] and mixed_counts(9) == [3, 9])
for w, n in (('ABABAB', 2), ('AABAAB', 3), ('AAAAAB', 6), ('AABAABAAB', 3), ('AAAAABBBB', 9)):   # AAAAAAAAB in v3
    check(f'key example {w} has {n} readouts', len(readouts(w)) == n and w in G)
check('2-3 P7 repeats K-1 P6 with two six-bead boards per row',
      'Problem 7: Use both A and B on a six-bead ring. Find rings with two, three and six different readouts.' in words(m[5])
      and sorted(x[3] for x in boards(m[5])) == [6, 6, 6, 6])
check('guide keys 2-3 P7 and 4-5 P5', 'P7. The K-1 P6 examples' in G and 'P5. Six beads: 2, 3 or 6 readouts' in G)

# Fix 3: materials and hints
check('guide says how to make single-board mats, a sticky-note start and scissors',
      'cut a spare page of four- or five-bead boards into single-board mats' in G and 'sticky note cut to an arrow' in G
      and 'bring scissors for the cards' in G and 'printed ring templates' not in G and 'single-board mats cut from a spare board page' in G)

# Fix 4: 4-5 P2 and P4 in 2-3 P6's form
check('4-5 P2 wording', 'Problem 2: Group the eight cards by turning. Someone divides 8 by 3 to count the rings. What went wrong?' in words(u[1]))
check('4-5 P4 wording', 'Problem 4: Group the 32 cards by turning. Count the rings with a calculation, and explain why the group sizes differ from the four-bead case.' in words(u[3]))
check(f'counts: 2+(8-2)/3 = {len(three)}, 2+(32-2)/5 = {len(rings_of(5))}', len(three) == 2 + 6 // 3 and len(rings_of(5)) == 2 + 30 // 5 == 8
      and '2+(32-2)/5=8' in G)

# Fix 5: the four-bead physical argument covers matches after 1, 2 and 3 steps
ok = True
for w in map(''.join, product('AB', repeat=4)):
    for s in (1, 2, 3):
        if w[s:] + w[:s] == w:
            ok &= (len(set(w)) == 1) if s in (1, 3) else len(readouts(w)) <= 2
check('a four-bead match after 1 or 3 steps forces one colour; after 2, at most two readouts; three readouts never happen',
      ok and 3 not in {len(readouts(''.join(w))) for w in product('AB', repeat=4)}
      and 'After 1 or 3 steps' in G and 'After 2 steps, opposite beads agree' in G)

# Could 6 and 9: lines under the older P3 boards; 2-3 P3 no longer announces a failure
for name, d in (('2-3', m), ('4-5', u)):
    lines = [x for x in d[2].get_drawings() if [i[0] for i in x['items']] == ['l'] and abs(x['rect'].width / CM - 18.5) < .01]
    check(f'{name} P3 has two lines under the boards', len(lines) == 2)
check('2-3 P3 wording', 'Which numbers are possible? Explain how you know.' in words(m[2]) and 'For each impossible number' not in words(m[2]))

# Could 8: timing
check('guide timing fits 35-40 minutes; K-1 first visit stays with three and four beads',
      '0-5, after the opening run-around' in G and '38 to the end' in G and '48-60' not in G and 'K can remain with four positions' not in G)

# Could 10: bonus guide
b = pymupdf.open(FOLDER / 'week-33-bonus-facilitator.pdf')
B = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in b))
flip = lambda w: w[::-1]
r1, r2 = readouts('AAABABBB'), readouts('AAABBBAB')
check('bonus P7: flipping either ring gives a turn of the other', flip('AAABABBB') in r2 and flip('AAABBBAB') in r1 and not r1 & r2
      and 'Flipping either ring gives a turn of the other' in B and 'Their flipped copies are rotations of each other' not in B)
ring = 'ABAAB'   # drawn clockwise from the top bead; the start arrow marks index 4
win = lambda i: ''.join(ring[(i + j) % 5] for j in range(3))
check('bonus launch: from the marked B the window is BAB; from the lower-left A it is ABA and crosses the gap',
      win(4) == 'BAB' and win(3) == 'ABA' and 'from the marked B read clockwise B-A-B' in B and 'lower-left A' in B and 'starting at the last B' not in B)

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
