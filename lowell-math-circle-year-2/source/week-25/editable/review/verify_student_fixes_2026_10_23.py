#!/usr/bin/env python3
"""Check the student-page changes of the October 23, 2026 card fixes (Week 25).

The mathematics is checked by brute force here (every 0/1 picture with given counts,
every rectangle switch, breadth-first distances), importing nothing from the problem
files or the guide builder. What is printed is read from the reference PDFs:

- p. 1 of every band says "Two pictures are different if any cell is different." in place
  of "Keep the row and column labels in place." (card should 9);
- K-1 P6 has the card's wording (should 6);
- every continuing page is headed "Problem N (continued)" with no restated task, and
  grades 2-3 are numbered P1-P6, the every-switch page now P4 (should 5);
- grades 4-5 P1 has 8 grids for its 6 pictures, P3 three blank grids for a route that
  needs two intermediate pictures, and P4 a page of three blank grids with its counts,
  fewer than its 6 pictures (shoulds 3 and 4);
- the grades 2-3 P4 switch example and guide p. 10 show a switch recorded as a drawn
  rectangle, and the legal switch it records turns the left picture into the right one
  (should 7); grades 4-5 P2 asks for the largest number of switches ever needed (could 12).

Run from anywhere: python3 review/verify_student_fixes_2026_10_23.py
"""
from collections import deque
from itertools import product
from pathlib import Path
import re

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
MM = 72 / 25.4
checks = []


def solutions(rows, cols):
    out = []
    for bits in product((0, 1), repeat=len(rows) * len(cols)):
        a = tuple(bits[i * len(cols):(i + 1) * len(cols)] for i in range(len(rows)))
        if [sum(r) for r in a] == rows and [sum(r[j] for r in a) for j in range(len(cols))] == cols:
            out.append(a)
    return out


def switches(a):
    out = []
    for i in range(len(a)):
        for k in range(i + 1, len(a)):
            for j in range(len(a[0])):
                for l in range(len(a[0])):
                    if j != l and a[i][j] and a[k][l] and not a[i][l] and not a[k][j]:
                        b = [list(r) for r in a]
                        b[i][j] = b[k][l] = 0
                        b[i][l] = b[k][j] = 1
                        out.append(((i, k, min(j, l), max(j, l)), tuple(map(tuple, b))))
    return out


def distances(a):
    seen = {a: 0}
    queue = deque([a])
    while queue:
        x = queue.popleft()
        for _, y in switches(x):
            if y not in seen:
                seen[y] = seen[x] + 1
                queue.append(y)
    return seen


def pic(s):
    return tuple(tuple(int(c) for c in row) for row in s.split('/'))


def text(pdf, page):
    return ' '.join(pymupdf.open(pdf)[page - 1].get_text().split())


def words(pdf, page):
    return [(w[0] / MM, w[1] / MM, w[2] / MM, w[3] / MM, w[4]) for w in pymupdf.open(pdf)[page - 1].get_text('words')]


def grids(pdf, page):
    """Boards on a page: one row label A each."""
    return sum(1 for w in words(pdf, page) if w[4] == 'A')


K, M, H, G = (REF / f for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf', 'facilitator-guide.pdf'))
pages = {K: 8, M: 6, H: 8}
for pdf, n in pages.items():
    assert len(pymupdf.open(pdf)) == n, (pdf.name, len(pymupdf.open(pdf)))
# The small deferred coulds made later the same day (the last section of
# card-fixes-2026-10-23.md) respaced some grid rows and bumped the ids to v5, v4 and v4; they
# changed nothing else this script checks, so either set of ids is accepted, one per packet.
footers = {K: ('W25-K-v4', 'W25-K-v5'), M: ('W25-23-v3', 'W25-23-v4'), H: ('W25-45-v3', 'W25-45-v4')}
for pdf, n in pages.items():
    assert any(all(f in text(pdf, i) for i in range(1, n + 1)) for f in footers[pdf]), pdf.name
checks.append('page counts 8, 6, 8 and footers W25-K-v4, W25-23-v3, W25-45-v3 (v5, v4, v4 after the small coulds) on every page')

# Should 9.
for pdf in pages:
    t = text(pdf, 1)
    assert 'Two pictures are different if any cell is different.' in t and 'Keep the row and column labels' not in t, pdf.name
checks.append('p. 1 of every band: "Two pictures are different if any cell is different."; the labels sentence is gone')

# Should 6.
t = text(K, 8)
assert 'On the left grids, no other picture may fit your counts. On the right grids, another picture must fit them.' in t
assert 'Choose pictures whose counts' not in t
checks.append("K-1 P6 has the card's wording")

# Should 5: continued headings, nothing restated after them, numbering.
continued = {K: {5: 3, 6: 4}, M: {3: 2}, H: {2: 1, 5: 3, 7: 4}}
for pdf, cont in continued.items():
    for page, n in cont.items():
        ws = sorted(words(pdf, page), key=lambda w: (round(w[1]), w[0]))
        line = [w[4] for w in ws if 25 < w[1] < 32]
        assert line == ['Problem', str(n), '(continued)'], (pdf.name, page, line)
    numbered = [int(n) for i in range(1, pages[pdf] + 1) for n in re.findall(r'Problem (\d):', text(pdf, i))]
    assert numbered == list(range(1, len(numbered) + 1)), (pdf.name, numbered)
    assert len(numbered) == {K: 6, M: 6, H: 5}[pdf]
assert 'Problem 4: A switch moves' in text(M, 4) and 'Problem 5: Make a picture' in text(M, 5) and 'Problem 6: Use four counters' in text(M, 6)
assert 'Problem 4: Can you make two different pictures for each pair of grids?' in text(K, 5)
checks.append('continuing pages are headed "Problem N (continued)" alone (K-1 pp. 5-6, 2-3 p. 3, 4-5 pp. 2, 5, 7); K-1 and 2-3 number P1-P6 once each, 4-5 P1-P5')

# Should 3 and 4: spare grids.
six = solutions([2, 2], [1, 1, 1, 1])
assert len(six) == 6
assert (grids(H, 1), grids(H, 2)) == (4, 4)
checks.append(f'4-5 P1: {grids(H, 1) + grids(H, 2)} grids for its {len(six)} pictures')
start, target = pic('111000/000111'), pic('000111/111000')
d = distances(start)[target]
assert d == 3 and grids(H, 5) == 3 > d - 1
checks.append(f'4-5 P3: a shortest route has {d} switches, so {d - 1} intermediate pictures; p. 5 has {grids(H, 5)} blank grids')
p4 = solutions([3, 3], [2, 1, 0, 1, 1, 1])
a, b = pic('110100/100011'), pic('100011/110100')
assert len(p4) == 6 and distances(a)[b] == 2 and max(max(distances(x).values()) for x in p4) == 2
digits = [w for w in words(H, 7) if re.fullmatch(r'\d', w[4]) and 30 < w[1] < 260]
rows_ = [w[4] for w in digits if w[0] > 175]                       # circled row counts, right of each board
cols_ = [w[4] for w in sorted(digits, key=lambda w: (round(w[1]), w[0])) if w[0] < 175 and any(abs((w[1] + w[3]) / 2 - y) < 3 for y in (94, 164, 234))]
assert grids(H, 7) == 3 < len(p4)
assert rows_ == ['3'] * 6 and cols_ == ['2', '1', '0', '1', '1', '1'] * 3, (rows_, cols_)
checks.append('4-5 P4: endpoints 2 switches apart, 6 pictures, greatest distance 2; p. 7 has 3 blank grids with counts 3,3 / 2,1,0,1,1,1')

# Cell sizes and margins on the new two-column pages.
for page in (1, 2):
    xs = [w for w in words(H, page) if 20 < w[1] < 262]
    assert min(w[0] for w in xs) >= 14 and max(w[2] for w in xs) <= 202, page
    vx = sorted({round(dw['rect'].x0 / MM, 2) for dw in pymupdf.open(H)[page - 1].get_drawings()
                 if dw['rect'].width < .1 and dw['rect'].height / MM > 30})
    assert vx == [round(x0 + j * 18.5, 2) for x0 in (21, 118.4) for j in range(5)], vx
checks.append('4-5 pp. 1-2: two columns of 18.5 mm cells, all labels and counts within 14-202 mm')

# Should 7: the recorded switch.
assert 'Find every switch in each picture and draw its rectangle.' in text(M, 4)
before, after = pic('10/01'), pic('01/10')
assert [after] == [y for _, y in switches(before)]
rects = []
for dw in pymupdf.open(M)[3].get_drawings():
    c = dw.get('color')
    if c and all(abs(v - .45) < .02 for v in c):
        rects.append(dw['rect'])
assert len(rects) == 1, rects
r = rects[0]
assert abs(r.x0 / MM - 75) < .6 and abs(r.x1 / MM - 83) < .6 and abs(r.y0 / MM - 59) < .6 and abs(r.y1 / MM - 67) < .6, r
checks.append('2-3 P4 asks to draw each switch\'s rectangle; its example draws the 8 mm rectangle through cells A1, A2, B2, B1 of the left picture, whose one switch gives the right picture')
g10 = pymupdf.open(G)[10]
assert 'Grades 2-3 Problems 3 and 4' in g10.get_text() and 'Top right: 1 switch, recorded' in g10.get_text()
assert any(dw.get('color') and abs(dw['color'][0] - 0x77 / 255) < .01 for dw in g10.get_drawings())
start = pic('100/000/001')
assert [s for s, _ in switches(start)] == [(0, 2, 0, 2)]
checks.append('guide p. 10 draws the recorded rectangle on the top-right picture, whose only switch uses rows A, C and columns 1, 3')

# Could 12.
assert 'What is the largest number of switches ever needed between two of them?' in text(H, 3)
assert max(max(distances(x).values()) for x in six) == 2
checks.append('4-5 P2 asks for the largest number of switches ever needed (answer 2, unchanged)')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 25 student-page checks')
