#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes to Week 90 (plans/review/week-90.md).

    python3 verify_card_fixes_2026_10_23.py [--pdfs DIR] [--before DIR]

DIR holds week-90-students.pdf, week-90-materials.pdf and week-90-facilitator.pdf
(default: ../reference-pdfs). --before names a folder of the previous print PDFs
(default: the repository's week-90/archive-before-card-fixes-2026-10-23, when
present) for the unchanged-page checks. Needs PyMuPDF.

Checks: by a jeu de taquin written here, the K-1 key, the corner-order results, the
D and B preimages, the 5 + 6 + 5 count, the larger-neighbour failures, that the exit alone undoes a slide
(the ring stops by itself at S) on the cards and on every standard skew tableau in a
4 x 4 box with at most 7 cells, and the A2 example in the guide; from the PDFs, the
changed student wording and figures, the D table's reading direction against the
drawn cards, the guide's changed sentences and page references, and the pages and
packets meant to be unchanged.
"""
import argparse
import re
import sys
from collections import Counter
from itertools import permutations
from pathlib import Path

import pymupdf as fitz

HERE = Path(__file__).resolve().parent
MM = 72 / 25.4
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# ------------------------------------------------------------------ jeu de taquin (0-based (row, col))
def diagram(rows):
    return {(r, c) for r, n in enumerate(rows) for c in range(n)}


def increasing(t):
    return all(t[(r, c)] < t[q] for (r, c) in t for q in ((r, c + 1), (r + 1, c)) if q in t)


def corners(inner):
    return sorted(p for p in inner if (p[0] + 1, p[1]) not in inner and (p[0], p[1] + 1) not in inner)


def fillings(outer, inner):
    cells = sorted(outer - inner)
    for labels in permutations(range(1, len(cells) + 1)):
        t = dict(zip(cells, labels))
        if increasing(t):
            yield t


def slide(t, start, larger=False):
    t, hole = dict(t), start
    while True:
        r, c = hole
        nb = [q for q in ((r, c + 1), (r + 1, c)) if q in t]
        if not nb:
            return t, hole
        q = (max if larger else min)(nb, key=t.get)
        t[hole] = t.pop(q)
        hole = q


def undo(t, exit_cell):
    """Larger up/left neighbour into the hole until none is numbered; returns the tableau and the stop."""
    t, hole = dict(t), exit_cell
    while True:
        r, c = hole
        nb = [q for q in ((r - 1, c), (r, c - 1)) if q in t]
        if not nb:
            return t, hole
        q = max(nb, key=t.get)
        t[hole] = t.pop(q)
        hole = q


def rectify(t, inner, order=()):
    if not inner:
        yield order, t
        return
    for s in corners(inner):
        q, _ = slide(t, s)
        yield from rectify(q, inner - {s}, order + (s,))


def rows(t):
    n = max(r for r, c in t) + 1
    return '/'.join(''.join(str(t[(r, c)]) for c in range(max(cc for rr, cc in t if rr == r) + 1)) for r in range(n))


def shape(t):
    n = max(r for r, c in t) + 1
    return tuple(sum(1 for rr, _ in t if rr == r) for r in range(n))


FAM = {'A': ((3, 2), (1,)), 'D': ((3, 2, 1), (2, 1)), 'B': ((3, 3, 2), (2, 1))}
cards = {k: list(fillings(diagram(o), diagram(i))) for k, (o, i) in FAM.items()}   # reading order = card order

print('== Mathematics ==')
fin = {k: [] for k in FAM}
split = []
for k, (o, i) in FAM.items():
    for t in cards[k]:
        res = {rows(q) for _, q in rectify(t, diagram(i))}
        split += [f'{k}{cards[k].index(t) + 1}'] if len(res) != 1 else []
        fin[k].append(sorted(res)[0])
check(not split, 'Problems 3 and 5: every legal corner order gives the same finish on every A, D and B card')
check([len(cards[k]) for k in 'ADB'] == [5, 6, 16], 'A, D and B have exactly 5, 6 and 16 increasing starts')
ashape = [next(shape(q) for _, q in rectify(t, diagram((1,)))) for t in cards['A']]
check(fin['A'] == ['12/34', '13/24', '134/2', '123/4', '124/3'] and Counter(ashape) == {(2, 2): 2, (3, 1): 3}
      and ashape[0] == ashape[1] == (2, 2), 'K-1 key: A1, A2 finish as a square of four; A3, A4, A5 as a row of three with one below')
check(ashape[2] == ashape[4] and fin['A'][2] != fin['A'][4], 'K-1 key: A3 and A5 make the same shape with the numbers in different places')
dpre = Counter(fin['D'])
check(fin['D'] == ['1/2/3', '13/2', '12/3', '12/3', '13/2', '123'] and dpre == {'13/2': 2, '12/3': 2, '1/2/3': 1, '123': 1},
      'Problem 6: D2, D5 share 13/2 and D3, D4 share 12/3')
check(len(set(fin['B'])) == 16, 'Problem 6: the sixteen B finishes are all different')
first = Counter('a' if t[(0, 2)] == 1 else 'b' if t[(1, 1)] == 1 else 'd' for t in cards['B'])
check(first == {'a': 5, 'b': 6, 'd': 5}, 'Problem 5 key: 5 + 6 + 5 starts by where 1 sits')
bad = 0
for t in cards['A']:
    q, _ = slide(t, (0, 0), larger=True)
    bad += increasing(q)
check(bad == 0, 'Problem 8: the larger-neighbour rule leaves every A start out of order')
dlab = [''.join(str(t[p]) for p in [(0, 2), (1, 1), (2, 0)]) for t in cards['D']]
check(dlab == ['123', '132', '213', '231', '312', '321'], 'Problem 3 table: D labels read from top right to bottom left are 123, 132, 213, 231, 312, 321')

# the exit alone undoes a slide; the ring stops by itself at S
def single_slides(outer, inner):
    for t in fillings(outer, inner):
        for s in corners(inner):
            yield t, s

def partitions(n, cap):
    if n == 0:
        yield ()
        return
    for k in range(min(n, cap), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

slides = above_left = wrong = 0
shapes = [p for n in range(0, 17) for p in partitions(n, 4) if len(p) <= 4]
for o in shapes:
    for i in shapes:
        O, I = diagram(o), diagram(i)
        if not I or not I < O or len(O - I) > 7:
            continue
        for t, s in single_slides(O, I):
            q, e = slide(t, s)
            back, stop = undo(q, e)
            slides += 1
            wrong += (stop != s or back != t)
            above_left += any(p in t for p in ((s[0] - 1, s[1]), (s[0], s[1] - 1)))
check(slides == 37320 and wrong == 0 and above_left == 0,
      f'Problem 7 key: over all {slides} single slides in a 4 x 4 box with at most 7 cells, undoing from the exit alone stops at S and restores the start; no label ever lies above or left of S')
a2 = cards['A'][1]
q, e = slide(a2, (0, 0))
back, stop = undo(q, (2, 0))
check(rows(q) == '13/24' and e == (0, 2) and back == {(0, 1): 3, (1, 0): 1, (1, 1): 4, (2, 0): 2} and stop == (0, 0)
      and increasing(back) and back != a2,
      "guide Problem 7 hint: undoing A2's finish 13/24 from (3,1) instead of its exit (1,3) gives a different legal start")

# ------------------------------------------------------------------ PDFs
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--pdfs', type=Path, default=HERE.parent / 'reference-pdfs')
ap.add_argument('--before', type=Path, default=HERE.parents[3] / 'week-90' / 'archive-before-card-fixes-2026-10-23')
args = ap.parse_args()
flat = lambda s: ' '.join(s.split())
stu = fitz.open(args.pdfs / 'week-90-students.pdf')
fac = fitz.open(args.pdfs / 'week-90-facilitator.pdf')
mat = fitz.open(args.pdfs / 'week-90-materials.pdf')
sp = [flat(p.get_text()) for p in stu]
gp = [flat(p.get_text()) for p in fac]
g = ' '.join(gp)

print('== Student pages ==')
check(stu.page_count == 8 and all(t.startswith('Week 90 / Sliding number arrays / Grades 2–5') and 'W90-students-v2' in t for t in sp),
      'students: 8 pages, header and footer as before')
check('Slide tiles to close a missing corner' not in sp[0], 'p1: the teaser line is gone')
rule = [b for b in stu[0].get_text('blocks') if b[4].startswith('Numbers increase')]
check(len(rule) == 1 and abs(rule[0][1] / MM - 27) < 1.5, 'p1: the rules start at 27 mm, as on pages 3 and 7')
check('Could an increasing start be missing from this collection? Explain how you know.' in sp[1]
      and 'Explain why your collection is complete' not in sp[1], 'p2, Problem 2: "Explain how you know."')
check('Use the unchanged D card' not in sp[2], 'p3: the reset sentence is gone (it is in the launch)')
check('Could an increasing start be missing from the sixteen cards?' in sp[4] and 'Can you account for' not in sp[4], 'p5, Problem 5: "Could an increasing start be missing from the sixteen cards?"')
check('Use your finished B arrangements from Problem 5.' in sp[5] and 'B catalog' not in sp[5], 'p6, Problem 6: "Use your finished B arrangements from Problem 5."')
dark6 = [d for d in stu[5].get_drawings() if d.get('fill') and max(d['fill']) < 0.5 and d['rect'].width > 10 * MM]
check(not dark6, 'p6: no target shows a dark exit square, so all four are drawn alike')
check('Use the S and E markers' not in sp[6], 'p7: the repeated S and E sentence is gone')

def grid_labels(page, name):
    """Numbers drawn in the 14 mm grid under a card title, read top right to bottom left."""
    words = page.get_text('words')
    title = [w for w in words if w[4] == name]
    x0, y0 = title[0][0], title[0][3]
    nums = [w for w in words if w[4].isdigit() and len(w[4]) == 1 and x0 - 2 < w[0] < x0 + 45 * MM and y0 < w[1] < y0 + 45 * MM]
    nums.sort(key=lambda w: -w[0])
    return ''.join(w[4] for w in nums)

drawn = {n: grid_labels(stu[2], n) for n in ('D1', 'D3', 'D5')}
table = {m.group(1): m.group(2) for m in re.finditer(r'\b(D[1-6]) ([1-3]{3}) ', g)}
check(drawn == {'D1': '123', 'D3': '213', 'D5': '312'} and all(table.get(k) == v for k, v in drawn.items()),
      f'guide Problem 3 table reads the drawn D cards top right to bottom left: {drawn}')

print('== Guide ==')
check(fac.page_count == 9, 'guide: 9 pages, as before')
for s in ['What children are meant to discover.', 'K–1 route, adult-read.', 'Plain-words key', 'page 3 gives an adult-read K–1 route',
          'Its same-visit continuation is Problem 3, then Problem 4', 'The pooled record is each B finish, saved as made',
          'children answer it from the B finishes saved in Problem 5', 'If the deleted exit cell is known',
          'that square is the original cell', 'The exit marker carries essential information; S serves as a check.',
          'the ring stops by itself at S', 'Which marker do you need?', 'diagonal from top right to bottom left',
          'labels, top right to bottom left', 'Two orders that give different finishes mean a slip']:
    check(s in g, f'guide has "{s}"')
for s in ['descending diagonal', 'stop at S even if another neighboring label exists', 'Boundary markers carry essential information',
          'If the original starting cell and deleted exit cell are known', 'A separate familiar activity is appropriate for the K–1 table']:
    check(s not in g, f'guide no longer has "{s}"')
check('K–1 route, adult-read.' in gp[2] and 'Problems 1–2' in gp[2], 'guide: the K–1 route is on page 3, the Problems 1–2 page')
check('material pages 1, 5, 6' in g, 'guide K–1 route names material pages 1, 5, 6 (A board, pieces, A cards)')

print('== Unchanged pages ==')
if not args.before.is_dir():
    print(f'SKIP no previous PDFs at {args.before}')
else:
    def same(a, b, label):
        # The footer ids were bumped later on October 23 (W90-students-v2, W90-FAC-v2); compare the rest.
        ta = flat(a.get_text())
        tb = flat(b.get_text().replace('W90-students-v2', 'W90-students-v1').replace('W90-FAC-v2', 'W90-FAC-v1'))
        pa = a.get_pixmap(dpi=100, colorspace=fitz.csGRAY).samples
        pb = b.get_pixmap(dpi=100, colorspace=fitz.csGRAY).samples
        diff = sum(abs(x - y) > 64 for x, y in zip(pa, pb)) if len(pa) == len(pb) else -1
        check(ta == tb and 0 <= diff <= 800, f'{label}: text and pixels unchanged ({diff} differ at 100 dpi; allowance 800, since the print copies came from a newer pdfTeX and the old source built with TeX Live 2023 already differs from them by up to 678)')
    old_s = fitz.open(args.before / 'week-90-students.pdf')
    old_f = fitz.open(args.before / 'week-90-facilitator.pdf')
    for n in (4, 8):
        same(old_s[n - 1], stu[n - 1], f'students p{n}')
    for n in (5, 8, 9):
        same(old_f[n - 1], fac[n - 1], f'guide p{n}')

print()
print(f'{len(FAILS)} failure(s)')
sys.exit(1 if FAILS else 0)
