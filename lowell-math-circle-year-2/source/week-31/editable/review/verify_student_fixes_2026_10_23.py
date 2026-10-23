#!/usr/bin/env python3
"""Check the October 23, 2026 student-page fixes to Week 31 (review card shoulds 2-5, coulds 7-13)
against the mathematics and the printed pages.

Run from the package folder: python3 review/verify_student_fixes_2026_10_23.py [pdf folder]
The PDFs default to reference-pdfs/. Needs PyMuPDF; the mathematics uses the standard library.
"""
from math import gcd
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDFS = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
MM = 25.4 / 72


def blockers(a, b):
    """Lattice points strictly between O and (a, b), by collinearity, not by the gcd rule."""
    return [(x, y) for x in range(a + 1) for y in range(b + 1)
            if (x, y) not in ((0, 0), (a, b)) and x * b == y * a]


def text(name):
    return [re.sub(r'\s+', ' ', p.get_text()) for p in pymupdf.open(PDFS / f'{name}.pdf')]


def check(ok, msg):
    assert ok, msg
    print('PASS', msg)


K, M, U = text('k-1'), text('grades-2-3'), text('grades-4-5')
G = ' '.join(text('facilitator-guide'))
GRID = [(a, b) for a in range(7) for b in range(7) if a or b]

check(len(K) == 5 and len(M) == 5 and len(U) == 6, 'K-1 has 5 pages, grades 2-3 has 5 and grades 4-5 has 6')
check(all('F31-K-v3' in p for p in K) and all('F31-23-v3' in p for p in M) and all('F31-45-v3' in p for p in U)
      and not any('-v2' in p for p in K + M + U), 'every student page carries a v3 footer')

# Should 2: grades 4-5 order P3 predict, P4 ray groups, P5 common factor, then P6 and P7.
order = ['Problem 3: Predict the first dot', 'Problem 4: List all the targets',
         'Problem 5: A target is (a, b)', 'Problem 6: Explain why your Problem 3 rule', 'Problem 7: Find an entire row']
pages = [next(i for i, p in enumerate(U) if s in p) for s in order]
check(pages == sorted(pages) and pages[0] != pages[2] and 'common factor larger than 1' in U[pages[2]]
      and 'Does every blocker produce a common factor?' in U[pages[2]] and not any('common divisor' in p for p in U),
      'grades 4-5: Problem 3 (rule), Problem 4 (ray groups), Problem 5 (common factor, both directions), then 6 and 7; '
      'the divisor question is no longer on the page of Problem 3 (should 2)')

# Should 3: 4-5 P1 asks for every visible dot and as many blocker counts as possible; the counts are 1-5.
counts = sorted({len(blockers(a, b)) for a, b in GRID} - {0})
check('Problem 1: Circle every dot visible from O. Then find hidden targets with as many different numbers of '
      'blockers as you can, and mark each blocker.' in U[0]
      and sum(not blockers(a, b) for a, b in GRID) == 25 and counts == [1, 2, 3, 4, 5]
      and all(len(blockers(a, b)) == gcd(a, b) - 1 for a, b in GRID)
      and 'the possible counts are 1, 2, 3, 4 and 5' in G,
      'grades 4-5 Problem 1: 25 visible dots on the 0-6 grid, hidden blocker counts exactly 1-5, and the guide says so (should 3)')

# Should 4: K-1 P5 says "visible dot"; the three ties hide five each, every other visible dot at most two.
hides = {(a, b): sum(1 for k in range(2, 7) if k * a <= 6 and k * b <= 6) for a, b in GRID if not blockers(a, b)}
top = max(hides.values())
check('Which visible dot hides the most dots behind it? Find every visible dot that ties for the most.' in K[4]
      and not any('first dot' in p for p in K) and top == 5
      and sorted(v for v, h in hides.items() if h == top) == [(0, 1), (1, 0), (1, 1)]
      and max(h for v, h in hides.items() if h < top) == 2 and 'Three visible dots tie' in G,
      'K-1 Problem 5 asks about visible dots; (1,0), (0,1), (1,1) hide five each and every other visible dot at most two (should 4)')

# Should 5: the "(4, 2)" label sits beside its ring at (4, 2), in grades 2-3 and 4-5.
for name in ('grades-2-3', 'grades-4-5'):
    page = pymupdf.open(PDFS / f'{name}.pdf')[1]
    rings = [d['rect'] for d in page.get_drawings() if d['type'] == 's' and [i[0] for i in d['items']] == ['c'] * 4
             and 2 < (d['rect'][2] - d['rect'][0]) * MM < 3.5]
    words = page.get_text('words')
    labels = [w for w in words if w[4] == '(4,' and 100 < w[1] < 200]   # the picture's label, not the problem text
    assert len(rings) == 1 and len(labels) == 1, (name, rings, labels)
    r, w = rings[0], labels[0]
    cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
    check(0 < (w[0] - cx) * MM < 6 and abs((w[1] + w[3]) / 2 - cy) * MM < 1.5,
          f'{name} p. 2: the "(4, 2)" label starts {(w[0] - cx) * MM:.1f} mm right of its ring, level with it (should 5)')

# Could 7: K-1 P4; only row 1 is all visible on the 0-6 grid, and no row is all hidden.
rows = {y: [not blockers(x, y) for x in range(7) if x or y] for y in range(7)}
check('Find a row where every dot is visible. Is there a row where every dot is hidden?' in K[3]
      and [y for y, r in rows.items() if all(r)] == [1] and not any(not any(r) for r in rows.values()),
      'K-1 Problem 4: row 1 is the only all-visible row of the 0-6 grid and no row is all hidden (could 7)')

# Could 9: 2-3 P6 asks for a row where every dot is visible; on every larger grid row 1 is the only one.
check('Give a row where every dot is visible, and explain why each one is visible.' in M[4]
      and not any('infinitely many visible' in p for p in M)
      and all([y for y in range(n + 1) if all(not blockers(x, y) for x in range(n + 1) if x or y)] == [1]
              for n in range(2, 25)),
      'grades 2-3 Problem 6 asks for an all-visible row; row 1 is the only one on every square grid up to 24 (could 9)')

# Could 10: 4-5 P6 starts from Problem 3's rule.
check('Problem 6: Explain why your Problem 3 rule finds every blocker' in U[pages[3]],
      'grades 4-5 Problem 6 starts from the Problem 3 rule (could 10)')

# Could 11: 4-5 P3 has a 26 by 16 dot grid at 7 mm, reaching (25, 15), so every target can be tested.
page = pymupdf.open(PDFS / 'grades-4-5.pdf')[pages[0]]
dots = [d['rect'] for d in page.get_drawings() if d['type'] == 'f' and abs((d['rect'][2] - d['rect'][0]) * MM - .78) < .05]
xs = sorted({round((r[0] + r[2]) / 2, 1) for r in dots})
ys = sorted({round((r[1] + r[3]) / 2, 1) for r in dots})
steps = [(b - a) * MM for v in (xs, ys) for a, b in zip(v, v[1:])]
labels = {w[4] for w in page.get_text('words')}
targets = [(12, 8), (15, 10), (21, 14), (25, 15), (13, 8)]
check(len(dots) == 26 * 16 and len(xs) == 26 and len(ys) == 16 and all(abs(s - 7) < .05 for s in steps)
      and {'25', '15'} <= labels and all(a <= 25 and b <= 15 for a, b in targets)
      and [len(blockers(a, b)) for a, b in targets] == [3, 4, 6, 4, 0],
      'grades 4-5 Problem 3 has a 0-25 by 0-15 grid of 416 dots at 7.0 mm, holding all five targets (could 11)')

# Could 13: on every p. 1 the captions clear the axis numerals.
for name in ('k-1', 'grades-2-3', 'grades-4-5'):
    words = pymupdf.open(PDFS / f'{name}.pdf')[0].get_text('words')
    caps = [w for w in words if w[4] in ('hidden', 'visible')]
    caps = [w for w in caps if w[1] < min(c[1] for c in caps) + 1]   # the two captions, not a prompt word
    nums = [w for w in words if w[4].isdigit() and w[1] < 300 and w[1] > 60]
    gap = min(c[1] - n[3] for c in caps for n in nums if n[0] < c[2] + 20 and c[0] - 20 < n[2] and n[3] <= c[1] + 1)
    check(len(caps) == 2 and gap * MM > 3, f'{name} p. 1: "hidden" and "visible" sit {gap * MM:.1f} mm below the axis numerals (could 13)')

# Guide: the 4-5 key follows the new order, the K-1 key notes, the tape advice and the route note.
check(G.index('P4. For (6,4), the group is') < G.index('P5. If q>1 divides a and b')
      and 'An adult can write on the lines' in G and 'tape the thread down at O' in G
      and 'Row y=1 is the only row where every dot is visible' in G
      and 'complete ray groups (P4), explain both directions of the criterion (P5)' in G,
      'guide: 4-5 key P4 ray groups then P5 common factor; K-1 notes (coulds 7, 8), tape at O (could 12), route note renumbered')
print('All Week 31 student-fix checks passed.')
