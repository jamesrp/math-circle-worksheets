#!/usr/bin/env python3
"""Check the student-page changes of the October 23, 2026 card fixes (Week 12).

Independent brute force for the mathematics (every perfect matching of 1..2n, filtered
by an interleaving test; nothing imported from the problem files' figures.py), and
the reference PDFs for what is printed:

- K-1 Problem 3 (card should 3) prints every drawn pair twice: 1-4, 1-6, 1-3 and 1-5,
  two frames each. 1-4 and 1-6 have exactly two completions and 1-3 and 1-5 none, so
  the frames no longer tell a child which starts can be finished, and every
  completion has a frame.
- K-1 Problem 4 (should 4) has 6 frames on page 4 and 10 more on page 5, headed
  "Problem 4 (continued)": 16 frames for the 14 pairings of eight dots. The sentence
  about drawing extra circles on blank paper is gone.
- K-1 Problem 3's prompt says to put a string on the large circle for each drawn pair
  and leave it there (could 10). Grades 4-5 page 2 no longer says "Numbers show the
  walk order." (could 7).
- On K-1 pages 2, 3, 4 and 6 the mat's lowest label is at least 6.5 mm above the
  nearest frame label below it, against 4.9 mm before (could 9).

Run from anywhere: python3 review/verify_student_fixes_2026_10_23.py
"""
import ast
import re
from itertools import combinations
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
WEEK = next(w for w in (ROOT / 'problem-files', ROOT.parent) if (w / 'week.toml').exists())
REF = ROOT / 'reference-pdfs'
MM = 72 / 25.4


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
    return [m for m in matchings(tuple(range(1, 2 * n + 1)))
            if not any(crossing(p, q) for p, q in combinations(m, 2))]


def words(pdf, page):
    return [(w[0] / MM, w[1] / MM, w[2] / MM, w[3] / MM, w[4]) for w in pymupdf.open(pdf)[page - 1].get_text('words')]


def text(pdf, page):
    return ' '.join(pymupdf.open(pdf)[page - 1].get_text().split())


checks = []
P8 = noncrossing(4)
assert len(P8) == 14

# Should 3: every start twice; completions 2, 2, 0, 0.
src = (WEEK / 'problems/03-k1-finish-a-drawn-pair.md').read_text()
starts = ast.literal_eval(re.search(r'k1_finish_records\((\[.*?\])\)', src).group(1))
frames = {tuple(e): starts.count(e) for e in starts}
assert frames == {(1, 4): 2, (1, 6): 2, (1, 3): 2, (1, 5): 2}, frames
done = {e: sum(e in m for m in P8) for e in frames}
assert done == {(1, 4): 2, (1, 6): 2, (1, 3): 0, (1, 5): 0}, done
assert all(frames[e] >= done[e] for e in frames)
checks.append('K-1 P3 prints 1-4, 1-6, 1-3 and 1-5 twice each; their completions are 2, 2, 0, 0, so every completion has a frame and the frames show no count')

k1 = REF / 'k-1.pdf'
assert len(pymupdf.open(k1)) == 7
eight_dot_frames = lambda page: sum(1 for w in words(k1, page) if w[4] == '8')
p3 = eight_dot_frames(3) - 1   # one label 8 per eight-dot circle, less the mat
assert p3 == 8, p3
checks.append('K-1 page 3 shows the eight-dot mat and eight frames')

# Should 4: 6 + 10 frames for 14 pairings, a continued heading, no blank-paper sentence.
p4, p5 = eight_dot_frames(4) - 1, eight_dot_frames(5)
assert (p4, p5) == (6, 10), (p4, p5)
assert p4 + p5 >= len(P8)
assert 'Problem 4 (continued)' in text(k1, 5) and 'Problem 4:' in text(k1, 4)
assert 'blank paper' not in ' '.join(text(k1, i) for i in range(1, 8))
assert [n for i in range(1, 8) for n in re.findall(r'Problem (\d):', text(k1, i))] == ['1', '2', '3', '4', '5', '6']
checks.append('K-1 P4 has 6 frames on page 4 and 10 on page 5 ("Problem 4 (continued)"): 16 for the 14 pairings; no blank-paper sentence')

# Could 10 and could 7.
assert 'For each drawn pair, put a string on the large circle and leave it there.' in text(k1, 3)
assert 'Keep each drawn pair' not in text(k1, 3)
h = REF / 'grades-4-5.pdf'
assert 'Numbers show the walk order' not in text(h, 2) and 'On the path, U goes up and D goes down.' in text(h, 2)
checks.append("K-1 P3's prompt says to leave a string on the drawn pair; grades 4-5 page 2 drops \"Numbers show the walk order.\"")

# Could 9: room between each mat's lowest label and the frame labels below.
for page in (2, 3, 4, 6):
    ws = words(k1, page)
    mat_bottom = max(w[3] for w in ws if abs((w[0] + w[2]) / 2 - 108) < 2 and 140 < w[1] < 165)
    below = min(w[1] for w in ws if w[1] > mat_bottom and w[1] < 200)
    assert below - mat_bottom >= 6.5, (page, below - mat_bottom)
    checks.append(f'K-1 page {page}: {below - mat_bottom:.1f} mm between the mat\'s lowest label and the frame labels below')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 12 student-page checks')
