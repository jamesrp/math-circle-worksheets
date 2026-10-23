#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card shoulds in Week 41 (plans/review/week-41.md).

Usage: python3 review/verify_card_shoulds_2026_10_23.py [folder with the built PDFs]
(default: reference-pdfs/ beside this folder). Needs PyMuPDF for the PDF checks.

1. Mathematics of every changed key: Grades 2-3 Problem 4's three trips, the Grades 4-5
   follow-up on trips home of exactly 4, 5 and 6 steps, the K-1 plain-board contrast, and
   the two allowed changes pictured on Grades 4-5 page 4.
2. The problem files' wording: no "Draw or replay", no named invariant in Grades 4-5
   Problem 6, "trip" rather than "journey", "keep going the same way", and no "Repeated
   copies continue beyond the page." for K-1.
3. The built packets: v3 footers; every band's page 1 names the portal map and the
   repeated map and no longer says input/process/output; Grades 2-3 Problem 2's map is
   120 mm with ruled lines; Grades 4-5 has six pages, the finishing-copy map before the
   four trips home, and Problem 5 alone on page 5.
"""
from itertools import product
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


STEP = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
LETTERS = {(-1, 1): 'A', (0, 1): 'B', (1, 1): 'C', (-1, 0): 'D', (0, 0): 'H', (1, 0): 'E',
           (-1, -1): 'F', (0, -1): 'G', (1, -1): 'I'}


def disp(w):
    return tuple(sum(STEP[c][i] for c in w) for i in (0, 1))


def portal_cell(w):
    x, y = disp(w)
    return LETTERS[((x + 1) % 3 - 1, (y + 1) % 3 - 1)]


def copy_of(w):
    x, y = disp(w)
    assert x % 3 == 0 and y % 3 == 0, w
    return (x // 3, y // 3)


# 1. Mathematics
trips = {'RRRUUU': (1, 1), 'RURURU': (1, 1), 'RRRDDD': (1, -1)}
check(all(portal_cell(w) == 'H' and copy_of(w) == c for w, c in trips.items()),
      '2-3 Problem 4: all three trips end at H; RRRUUU and RURURU in copy (1,1), RRRDDD in (1,-1)')
expected = {4: {(0, 0)}, 5: {(1, 0), (-1, 0), (0, 1), (0, -1)},
            6: {(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2)}}
for n, want in expected.items():
    got = {copy_of(w) for w in map(''.join, product('RLUD', repeat=n)) if portal_cell(w) == 'H'}
    check(got == want, f'4-5 Problem 3 follow-up: trips home of exactly {n} steps reach copies {sorted(got)}')
for w, c in {'RRR': (1, 0), 'LLL': (-1, 0), 'UUU': (0, 1), 'DDD': (0, -1)}.items():
    check(copy_of(w) == c, f'4-5 Problem 3 key: {w} finishes in {c}')


def plain_walks(n):
    """Walks of exactly n steps from H on a 3-by-3 board with no portals."""
    ends = [(0, 0, '')]
    for _ in range(n):
        ends = [(x + dx, y + dy, w + c) for x, y, w in ends for c, (dx, dy) in STEP.items()
                if abs(x + dx) <= 1 and abs(y + dy) <= 1]
    return ends


check({LETTERS[(x, y)] for x, y, _ in plain_walks(2)} == set('HACFI'),
      'K-1 contrast: on a plain board two steps from H reach exactly H, A, C, F and I')
check(all((x, y) != (0, 0) for n in (1, 3, 5, 7, 9) for x, y, _ in plain_walks(n)),
      'K-1 contrast: on a plain board no trip of 1, 3, 5, 7 or 9 steps returns to H')
check(portal_cell('RRR') == 'H', 'K-1 contrast: on the portal map RRR returns to H in three steps')
# Page 4 pictures: lower-left block D H / F G; slide F-G-H (R U) to F-D-H (U R); backtrack F-G-F-D (R L U) to F-D (U).


def reduce(w):
    out = []
    for c in w:
        if out and STEP[out[-1]] == tuple(-v for v in STEP[c]):
            out.pop()
        else:
            out.append(c)
    return ''.join(out)


check(disp('RU') == disp('UR') == (1, 1), 'page 4 slide picture: F to G to H and F to D to H have the same ends')
check(reduce('RLU') == 'U', 'page 4 backtrack picture: F to G to F to D becomes F to D')

# 2. Wording in the problem files
PROBLEMS = next(p for p in (ROOT.parent / 'problems', ROOT / 'problem-files' / 'problems') if p.is_dir())
text = {p.name: p.read_text() for p in PROBLEMS.glob('*.md')}


def student(s):
    """The prompt and text sections only."""
    return ''.join(c for c in re.split(r'^## ', s, flags=re.M)[1:] if c.startswith(('prompt', 'text')))


everything = ''.join(student(s) for s in text.values())
check('Draw or replay' not in everything, 'no "Draw or replay" (2-3 Problem 2)')
check('finishing copies decide' not in everything and
      'When can two trips from H back to H be changed into each other? Explain.' in text['12-when-same.md'],
      '4-5 Problem 6 asks the open question without naming the invariant')
check('journey' not in everything.lower(), 'student pages say "trip", never "journey"')
check('Keep moving in the arrow direction' not in everything and everything.count('Keep going the same way.') == 2,
      'rules say "Keep going the same way." for every band')
k1_rules = re.search(r'## text [^\n]*\[K-1\]\n(.*?)\n\n', text['00-rules.md'], re.S).group(1)
check('Repeated copies' not in k1_rules, 'K-1 rules drop "Repeated copies continue beyond the page."')
check('Start at H in copy (0,0). Find the finishing copy for each trip.' in text['05-finishing-copies.md']
      and 'One copy right adds 1' not in everything, '4-5 finishing-copy problem no longer narrates the labels')

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
    for b, tag in (('k-1', 'K'), ('grades-2-3', '23'), ('grades-4-5', '45')):
        d = docs[b]
        check(all(f'F41-{tag}-v3' in p.get_text() for p in d), f'{b}: every page carries F41-{tag}-v3')
        t = d[0].get_text()
        check('portal map' in t and 'repeated map' in t and not re.search(r'\b(input|process|output)\b', t),
              f'{b} page 1: panels named "portal map" and "repeated map"; no input/process/output')
    d = docs['grades-2-3']
    sq = [r for r in (dr['rect'] for dr in d[1].get_drawings() if dr['type'] == 's')
          if abs((r.x1 - r.x0) * MM - 120) < .2 and abs((r.y1 - r.y0) * MM - 120) < .2]
    rules = [dr for dr in d[1].get_drawings() if dr['type'] == 's' and abs(dr['rect'].y0 - dr['rect'].y1) < .01
             and (dr['rect'].x1 - dr['rect'].x0) * MM > 40]
    check(len(sq) == 1 and len(rules) >= 15, f'2-3 Problem 2: one 120 mm map and {len(rules)} ruled lines')
    t = d[3].get_text()
    check(t.count('Problem 4') == 1 and 'three trips' in t and t.count('original') == 3,
          '2-3 Problem 4 compares three trips, each on its own repeated map, on one page')
    d = docs['grades-4-5']
    pages = [p.get_text() for p in d]
    nums = [sorted(set(re.findall(r'Problem (\d):', t))) for t in pages]
    check(len(d) == 6 and nums == [['1'], ['2'], ['3'], ['4'], ['5'], ['6']],
          f'4-5: six pages with problems {nums}')
    check('(0,0)' in pages[1].replace(' ', '') or '(0, 0)' in pages[1], '4-5 page 2 holds the copy-labelled repeated map')
    check('Slide' in pages[3] and 'Backtrack' in pages[3] and 'page 2' in pages[3], '4-5 page 4: both pictures with their lines; P4 points to page 2')
print(f'{len(fails)} failure(s)')
raise SystemExit(1 if fails else 0)
