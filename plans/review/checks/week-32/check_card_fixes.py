#!/usr/bin/env python3
"""Check the Week 32 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-32-k-1.pdf, week-32-grades-2-3.pdf, week-32-grades-4-5.pdf,
week-32-facilitator.pdf and week-32-materials.pdf (default: the print folder).
Needs PyMuPDF. Each fix is checked in the printed words and drawings, and each
mathematical claim it relies on is recomputed here.
"""
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2' / 'week-32'
CM = 72 / 2.54
FAILS = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


def doc(name):
    return pymupdf.open(FOLDER / f'week-32-{name}.pdf')


def words(page):
    return re.sub(r'\s+', ' ', page.get_text()).strip()


def boards(page):
    """Black-outlined boards at 1 cm per unit, as (width, height), top to bottom then left to right."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        w, h = r.width / CM, r.height / CM
        if d.get('color') == (0.0, 0.0, 0.0) and w > 1.5 and h > 1.5 and abs(w - round(w)) < .01 and abs(h - round(h)) < .01:
            out.append((round(r.y0), round(r.x0), round(w), round(h)))
    return [(w, h) for _, _, w, h in sorted(out)]


def grids(page):
    """Light work grids: count the gray vertical and horizontal lines and their spans in cm."""
    v, hz = [], []
    for d in page.get_drawings():
        if d.get('color') and d['color'][0] > .5 and len(d['items']) == 1 and d['items'][0][0] == 'l':
            a, b = d['items'][0][1], d['items'][0][2]
            if abs(a.x - b.x) < .01 and abs(a.y - b.y) > CM:
                v.append((round(a.x / CM, 2), round(abs(a.y - b.y) / CM, 2)))
            elif abs(a.y - b.y) < .01 and abs(a.x - b.x) > CM:
                hz.append((round(a.y / CM, 2), round(abs(a.x - b.x) / CM, 2)))
    return v, hz


def rule(a, b):
    a, b = max(a, b), min(a, b)
    seq = []
    while b:
        seq += [b] * (a // b)
        a, b = b, a % b
    return seq


def sizes(a, b):
    return len(set(rule(a, b)))


k, m, u, g = doc('k-1'), doc('grades-2-3'), doc('grades-4-5'), doc('facilitator')
G = re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in g))

# Footers and page counts
check('packets are v3, with 5, 6 and 5 pages', [len(k), len(m), len(u)] == [5, 6, 5] and all(
    f'F32-{t}-v3' in words(p) for d, t in ((k, 'K'), (m, '23'), (u, '45')) for p in d))

# Fix 1 and could 11: 2-3 P6 alone on page 6 with a 12 by 18 grid that holds every trio
p6 = words(m[5])
check('2-3 P6 is alone on page 6 and says "Use only side lengths 3, 6, 9 and 12."',
      p6.count('Problem') == 1 and 'Problem 6: Make three rectangles with different first squares and the same last '
      'square of side 3. Use only side lengths 3, 6, 9 and 12.' in p6 and 'Problem 6' not in words(m[4]))
v, hz = grids(m[5])
check('2-3 P6 grid is 12 cm wide and 18 cm tall (13 vertical and 19 horizontal lines)',
      len(v) == 13 and len(hz) == 19 and all(abs(s - 18.3) < .02 for _, s in v) and all(abs(s - 12.3) < .02 for _, s in hz))
S = (3, 6, 9, 12)
rects = sorted({(a, b) for a, b in product(S, S) if a >= b and gcd(a, b) == 3})
first = {r: r[1] for r in rects}
trios = [t for i, t in enumerate(product(rects, repeat=3)) if t[0] < t[1] < t[2] and len({first[r] for r in t}) == 3]
check(f'every trio has 12x9 and 9x6 plus a 3-wide rectangle ({len(trios)} trios, areas '
      f'{min(sum(a*b for a, b in t) for t in trios)}-{max(sum(a*b for a, b in t) for t in trios)})',
      all((12, 9) in t and (9, 6) in t and any(r[1] == 3 for r in t) for t in trios) and len(trios) == 4)
check('every trio fits the 12 by 18 grid stacked (9 + 6 + 3 rows, each at most 12 long)',
      all(sum(min(a, b) for a, b in t) <= 18 and all(max(a, b) <= 12 for a, b in t) for t in trios))
check('guide P6 key names both forced rectangles and the 12-by-18 grid',
      'only 9×6 and 12×9 end at 3 with a first square above 3' in G and 'The 12-by-18 grid holds any trio stacked' in G)

# Fix 2 and 10: 4-5 P6 asks whether any other rectangle ties; 13 by 8 is the unique maximum
check('4-5 P6 asks "Does any other rectangle tie with it? How do you know?"',
      'Does any other rectangle tie with it? How do you know?' in words(u[4]) and 'Find every rectangle that ties' not in words(u[4]))
table = {(a, b): sizes(a, b) for a in range(9, 16) for b in range(2, 9)}
best = max(table.values())
check('13x8 is the only rectangle with five sizes among long 9-15, short 2-8',
      best == 5 and [r for r, s in table.items() if s == best] == [(13, 8)])
smallest = []
for n in range(1, 6):
    cands = [(a, b) for a in range(1, 40) for b in range(1, a) if sizes(a, b) == n]
    smallest.append(min(cands, key=lambda r: (r[1], r[0])))
check('smallest rectangles with 1 to 5 sizes are 2x1, 3x2, 5x3, 8x5, 13x8 (Lame: five sizes need long >= 13, short >= 8)',
      smallest == [(2, 1), (3, 2), (5, 3), (8, 5), (13, 8)] and all(
          a >= 13 and b >= 8 for a in range(1, 60) for b in range(1, a) if sizes(a, b) >= 5))
def quotients(a, b):
    return [a // b] + quotients(b, a % b) if b else []


check('13x8 quotients are 1,1,1,1,2 (every quotient but the last is 1)', quotients(13, 8) == [1, 1, 1, 1, 2])
check('14x8 and 15x8 have three sizes', table[(14, 8)] == 3 and table[(15, 8)] == 3)
check('guide P6 and overview give the reason',
      'No other rectangle ties.' in G and 'every quotient but the last is 1' in G and 'no rectangle with long side under 13 has five sizes' in G
      and 'consecutive Fibonacci numbers make the steps as many as possible' in G)

# Fix 3: K-1 P5 work grid 12 by 9 holds 3x12 and 6x6 together
v, hz = grids(k[4])
v = [x for x in v if abs(x[1] - 9.3) < .02]
hz = [x for x in hz if abs(x[1] - 12.3) < .02]
check('K-1 P5 work grid is 12 cm by 9 cm', len(v) == 13 and len(hz) == 10)
check('3x12 (3 rows) and 6x6 (6 rows) fit together in 12 by 9', 3 + 6 <= 9 and max(12, 6) <= 12)

# Fix 4: K-1 P4 boards 6x4 and 9x6, answers 2 and 3, equal to the last squares of P1 and P3
check('K-1 P4 boards are 6x4 and 9x6', boards(k[3]) == [(6, 4), (9, 6)])
check('K-1 P4 answers 2 and 3 equal the last squares of 6x4 (P1) and 9x6 (P3)',
      gcd(6, 4) == 2 and gcd(9, 6) == 3 and rule(6, 4)[-1] == 2 and rule(9, 6)[-1] == 3
      and (6, 4) in boards(k[0]) and (9, 6) in boards(k[2]))
check('guide K P4 key', 'for 9×6 it has side 3' in G and 'Ask which square came last on this rectangle in P1 or P3' in G
      and 'For both 6×4 and 8×6' not in G)

# Fix 5: the square sheet (measured in detail by materials/verify_materials.py)
mat = pymupdf.open(FOLDER / 'week-32-materials.pdf')
sq = Counter(round(d['rect'].width / CM) for d in mat[0].get_drawings() if d['fill'] and abs(d['rect'].width - d['rect'].height) < .01
             and abs(d['rect'].width / CM - round(d['rect'].width / CM)) < .005)
check('materials page: two sets of one 6, one 5, two 4s, six 3s, two 2s, three 1s', len(mat) == 1 and sq == Counter({6: 2, 5: 2, 4: 4, 3: 12, 2: 4, 1: 6}))
need = Counter()
for b in [(6, 4), (8, 4), (7, 4), (8, 5), (9, 6), (10, 6)]:
    need |= Counter(rule(*b))
check(f'one set covers the rule on every K-1 P1-P3 board at once (max need {dict(need)})',
      all(need[n] <= sq[n] // 2 for n in need))
check('guide names the sheet', 'week-32-materials.pdf' in G and 'tries the next size up and sees it overhang' in G)

# Fix 6: 4-5 P4 wording; common divisors before and after the cut
p4 = words(u[3])
check('4-5 P4 wording', 'Problem 4: Which sizes of identical whole-grid square can cover the 14 by 8 rectangle? Which can cover '
      'the 6 by 8? Explain why these two lists always match after a biggest-square cut.' in p4 and 'loses an 8 by 8' not in p4)
cd = lambda a, b: [d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0]
check('identical squares that cover 14x8 and 6x8 have sides {1,2} both', cd(14, 8) == cd(6, 8) == [1, 2])
check('cut keeps common divisors for every a > b <= 20', all(cd(a, b) == cd(a - b, b) for a in range(2, 21) for b in range(1, a)))

# Fix 7: no printed "Predict ... then test" method step in K-1 P2 or 4-5 P2
check('K-1 P2 wording', 'Problem 2: Will the last squares match? Use the biggest-square rule on both rectangles.' in words(k[1]))
check('4-5 P2 wording', 'Problem 2: Find a rule that predicts the last square from the two starting side lengths.' in words(u[1])
      and 'then test' not in words(u[1]))
check('guide hint asks for a guess first', 'ask for a guess before anyone covers a rectangle' in G)

# Fix 8: timing; fix 9: cutout counts; could 14: Week 4 by star hops
check('guide timing fits 35-40 minutes at the tables', '0-5, after the opening run-around' in G and '5-20:' in G and '20-38:' in G
      and '38 to the end' in G and '48-60' not in G)
check('guide cutout count', '16 for the K-1 table of four, or 8 if pairs share' in G and '12 cutouts' not in G)
check('guide Week 4 note', 'Week 4 reaches by star hops' in G and 'subtraction-gcd' not in G)

# Coulds 12 and 13
check('2-3 P4 drops the sort clause', 'and sort them' not in words(m[3]))
for i in (1, 2):
    lines = [d for d in m[i].get_drawings() if len(d['items']) == 1 and d['items'][0][0] == 'l' and d.get('color')
             and abs(d['rect'].width / CM - 4.5) < .02]
    check(f'2-3 P{i + 1} has two answer lines beside each board', len(lines) == 4)

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
