#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card shoulds in Week 42 (plans/review/week-42.md).

Usage: python3 review/verify_card_shoulds_2026_10_23.py [folder with the built PDFs]
(default: reference-pdfs/ beside this folder). Needs PyMuPDF for the PDF checks.

1. Mathematics of every changed key: the K-1 page 4 marked pairs, the two-red, two-blue
   first-color rule (K-1 Problem 5), the other fair rules added to the Grades 4-5 keys, the
   9-against-7 rule that fails Grades 4-5 Problem 2, and the guide's counter list.
2. The problem files' wording: the K-1 return sentence, "Keep your rule." in K-1 Problem 5,
   "always give a shape", no "independently", no story demand in Grades 2-3 Problem 6, no
   presupposed success in Grades 4-5 Problem 2, no bag captions where the card cut them.
3. The built packets: v3 footers (Grades 4-5 v4 after the same day's critic follow-up); K-1 has six pages with Problems 1-6 one per page and
   page 4 pictures all 32 marked pairs; Grades 2-3 page 3 has two blank 4-by-4 grids and
   page 4 one; Grades 4-5 page 1 has a 4-by-4 grid headed R1, R2, R3, B; the cut sentences
   are gone.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def colors(bag, other=None, replace=True):
    """Counts of color pairs over the equally likely ordered pairs of marked counters."""
    if other is not None:
        return Counter(a + b for a, b in product(bag, other))
    if replace:
        return Counter(a + b for a, b in product(bag, repeat=2))
    return Counter(bag[i] + bag[j] for i, j in permutations(range(len(bag)), 2))


# 1. Mathematics
one, two = ['R', 'B1', 'B2', 'B3'], ['R1', 'R2', 'B1', 'B2']
for labels, n in ((one, 3), (two, 4)):
    pairs = [(a, c) for a in labels for c in labels]
    cl = Counter(a[0] + c[0] for a, c in pairs)
    check(len(pairs) == 16 and cl['RB'] == cl['BR'] == n,
          f'K-1 P4: the {", ".join(labels)} pictures give RB and BR {n} times each of 16')
check([sum(a != b for a, b in product('R' * r + 'B' * (4 - r), repeat=2)) for r in range(5)] == [0, 6, 8, 6, 0],
      'K-1 P5: mixed pairs by red count 0-4 are 0, 6, 8, 6, 0 of 16; two and two is best')
first = Counter('square' if a == 'R' else 'circle' for a, b in product('RRBB', repeat=2))
check(first == {'square': 8, 'circle': 8}, 'K-1 P5 key: with RRBB, first color red gives a square and blue a circle: 8 and 8 of 16, no skips')
check(all(colors(b)[b[0] * 2] > 0 for b in ('RRRR', 'RRRB', 'RRBB', 'RBBB', 'BBBB')),
      'K-1 P5 key: under the kept rule every four-counter bag has a same-color pair')
w = colors('RRRB')
check(w['RR'] == 9 and w['RB'] + w['BR'] + w['BB'] == 7, '4-5 P2 key: RR to square, the rest to circle gives 9 against 7')
c = colors('RRRB', 'RBBB')
check(c['RR'] == c['BB'] == 3 and c['RB'] == 9 and c['BR'] == 1,
      '4-5 P5 key, first case: RB 9, BR 1, but RR 3 and BB 3 of 16, so RR square, BB circle is fair')
nr = colors('RRRB', replace=False)
check(sum(nr.values()) == 12 and nr['RR'] == 6 and nr['RB'] + nr['BR'] + nr['BB'] == 6,
      '4-5 P6 key: without return, both red gives a square in 6 of 12 and anything else a circle in 6, never skipping')
check(Fraction(9, 16) ** 6 > 0, '2-3 P6 key: six RR pairs have positive chance (9/16)^6')
# The guide asks for two containers, ten red and eight blue per pair: the most any one problem
# shows at once is two bags.
shown = {'K-1 P4': ['RBBB', 'RRBB', 'RRRR', 'BBBB'], '2-3 P3': ['RRBB', 'RBBB'], '2-3 P4': ['RRRB', 'RRBB'],
         '2-3 P5': ['RRRB', 'RBBB'], '4-5 P3': ['RRRRRBB', 'RRRBBBB'], '4-5 P5 first': ['RRRB', 'RBBB'],
         '4-5 P5 second': ['RRRB', 'RRRRRRBB'], '4-5 P5 third': ['RRBB', 'RB']}
need_r = max(a.count('R') + b.count('R') for bags in shown.values() for a in bags for b in bags if a != b)
need_b = max(a.count('B') + b.count('B') for bags in shown.values() for a in bags for b in bags if a != b)
check(need_r <= 10 and need_b <= 8, f'guide p. 2: any two bags one problem shows need at most {need_r} red and {need_b} blue (ten and eight supplied)')

# 2. Wording in the problem files
PROBLEMS = next(p for p in (ROOT.parent / 'problems', ROOT / 'problem-files' / 'problems') if p.is_dir())
text = {p.name: p.read_text() for p in PROBLEMS.glob('*.md')}


def student(s):
    """The prompt and text sections only."""
    return ''.join(x for x in re.split(r'^## ', s, flags=re.M)[1:] if x.startswith(('prompt', 'text')))


everything = ''.join(student(s) for s in text.values())
check('Use the same bag. Put each counter back after every draw; for random draws, mix and draw without looking.' in text['00-k1-draws.md'],
      'K-1 p. 1 says to put each counter back after every draw')
check(student(text['07-k1-four-counter-bag.md']).split('\n', 1)[1].startswith('Keep your rule.'), 'K-1 P5 starts "Keep your rule."')
check('always give a shape' in everything and 'force a shape' not in everything, 'K-1 P6 says "always give a shape"')
check('independently' not in everything, 'no "independently" on page 1 of the upper bands')
check(student(text['16-promise-shape.md']).strip().endswith('within six pairs?') and 'six-pair story' not in student(text['16-promise-shape.md']),
      '2-3 P6 ends at "within six pairs?"')
check('Do the shape chances match? Explain.' in text['21-check-labeled.md'] and 'Explain why the shape chances match' not in everything,
      '4-5 P2 asks whether the chances match')
check('it must sometimes give each shape' not in everything, '4-5 P1 drops "it must sometimes give each shape"')
check(not re.search(r"'(two red, two blue|one red, three blue|five red, two blue|three red, four blue)'", ''.join(text.values())),
      'no bag captions on 2-3 p. 3 or 4-5 p. 2')

# 3. The built PDFs
try:
    import pymupdf
except ImportError:
    pymupdf = None
folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
if pymupdf is None:
    print('SKIP PDF checks: PyMuPDF is not installed')
else:
    MM = 25.4 / 72
    docs = {b: pymupdf.open(folder / f'{b}.pdf') for b in ('k-1', 'grades-2-3', 'grades-4-5')}
    for b, d in docs.items():
        v = 'v4' if b == 'grades-4-5' else 'v3'
        check(all(f'W42-{b}-{v}' in p.get_text() for p in d), f'{b}: every page carries W42-{b}-{v}')
    all_text = ' '.join(p.get_text() for d in docs.values() for p in d)
    for gone in ('Each box names', 'independently', 'force a shape', 'Make a six-pair story', 'Explain why the shape chances match',
                 'two red, two blue', 'one red, three blue', 'five red, two blue', 'three red, four blue'):
        check(gone not in all_text, f'no "{gone}" in any packet')

    def squares(page, side, tol=.05):
        """Stroked squares of the given side in cm (rounded boxes are drawn as paths)."""
        out = set()
        for dr in page.get_drawings():
            r = dr['rect']
            if dr['type'] == 's' and abs((r.x1 - r.x0) * MM / 10 - side) < tol and abs((r.y1 - r.y0) * MM / 10 - side) < tol:
                out.add((round(r.x0, 1), round(r.y0, 1)))
        return out

    def rects(page, w, h, tol=.05):
        return {(round(dr['rect'].x0, 1), round(dr['rect'].y0, 1)) for dr in page.get_drawings() if dr['type'] == 's'
                and abs((dr['rect'].x1 - dr['rect'].x0) * MM / 10 - w) < tol and abs((dr['rect'].y1 - dr['rect'].y0) * MM / 10 - h) < tol}

    k = docs['k-1']
    nums = [sorted(set(re.findall(r'Problem (\d):', p.get_text()))) for p in k]
    check(len(k) == 6 and nums == [['1'], ['2'], ['3'], ['4'], ['5'], ['6']], f'K-1: six pages, one problem each: {nums}')
    words = [w[4] for w in k[3].get_text('words')]
    labels = [x for x in words if re.fullmatch(r'R\d?|B\d?', x)]
    # 16 marks in the two labeled bags (the one-color bags print R and B too), 64 in the pairs,
    # and the last mark of each caption ("... B2, B3", "... B1, B2"); the others carry a comma.
    check(len(rects(k[3], 4.3, 1.65)) == 32 and len(labels) == 16 + 64 + 2,
          f'K-1 p. 4: 32 marked-pair boxes; {len(labels)} counter marks (16 in the bags, 64 in the pairs, 2 in the captions)')
    check('Keep your rule. Choose a four-counter bag' in ' '.join(k[4].get_text().split()), 'K-1 p. 5: Problem 5 starts "Keep your rule."')
    m = docs['grades-2-3']
    check(len(squares(m[2], 1.75)) == 32, f'2-3 p. 3: two blank 4-by-4 grids ({len(squares(m[2], 1.75))} cells)')
    check(len(squares(m[3], 1.75)) == 16, f'2-3 p. 4: one blank 4-by-4 grid ({len(squares(m[3], 1.75))} cells)')
    heads = [w[4] for w in m[2].get_text('words') if re.fullmatch(r'R\d?|B\d?', w[4])]
    check(len(heads) == 16 and not any(h[1:] for h in heads),
          '2-3 p. 3: the four bags carry the only counter letters (16); the grid heads are empty')
    u = docs['grades-4-5']
    check(len(squares(u[0], 1.85)) == 16, f'4-5 p. 1: one 4-by-4 grid ({len(squares(u[0], 1.85))} cells)')
    heads = [w[4] for w in u[0].get_text('words') if w[4] in ('R1', 'R3')]
    check(len(heads) == 4, '4-5 p. 1: the grid is headed R1, R2, R3, B across and down')
    check('Do the shape chances match? Explain.' in ' '.join(u[0].get_text().split()), '4-5 p. 1: Problem 2 asks "Do the shape chances match? Explain."')
print(f'{len(fails)} failure(s)')
raise SystemExit(1 if fails else 0)
