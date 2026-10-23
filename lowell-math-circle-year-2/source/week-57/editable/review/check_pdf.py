#!/usr/bin/env python3
"""Read the Week 57 PDFs and check the October 23, 2026 card fixes on the printed pages.

    python3 check_pdf.py [FOLDER]   (FOLDER holds week-57-students.pdf, week-57-materials.pdf
                                     and week-57-facilitator.pdf; default: the print folder)

With PyMuPDF it checks the student packet's headers, footers and Problems 1-10; the new
wording on pp. 1, 2, 3, 5 and 8; that P3's two 5 x 5-dot boards are stacked with a gap
well above the 20 mm dot spacing; that the materials pages are 6 x 10 grids of 20 mm squares
(the second with one diagonal in each) with a 100 mm bar; and the guide's new sentences and
the removal of the replaced ones.
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:
    import fitz

HERE = Path(__file__).resolve().parent
MM = 72 / 25.4


def find_repo():
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found; pass the folder that holds the PDFs')


WEEK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_repo() / 'lowell-math-circle-year-2' / 'week-57'
FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def text(page):
    return ' '.join(re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', page.get_text()).split())


doc = fitz.open(WEEK / 'week-57-students.pdf')
st = [text(p) for p in doc]
nums = []
for i, t in enumerate(st):
    band = 'Grades 3–5' if i < 6 else 'Grades 4–5'
    check(t.startswith(f'Week 57 / Area from dots / {band}') and t.endswith(f'Bellingham Math Circle / Week 57 / N57-S-final-v3 {i+1}'),
          f'students p{i+1}: header {band}, footer N57-S-final-v3, page {i+1}')
    nums += [int(n) for n in re.findall(r'Problem (\d+):', t)]
check(len(doc) == 10 and nums == list(range(1, 11)), f'students: 10 pages, Problems {nums}')
check('Sides cannot cross or touch except at neighboring corners. The area of one grid square is 1. Find or check areas with pieces, cuts or copies.' in st[0]
      and 'Leave no holes' not in st[0] and '20 mm' not in st[0] and 'print at 100%' not in st[0],
      'p1: the rule says "pieces, cuts or copies" once; no holes or 20 mm sentence (coulds 7-8)')
check(sum(t.count('pieces, cuts or copies') for t in st) == 1 and not any('second copy' in t or 'using cuts or copies' in t for t in st),
      'packet: "pieces, cuts or copies" only on p1 (could 8)')
check('Problem 1: Find the exact area of each shape. area=' in st[0], 'P1: "Find the exact area of each shape." (could 8)')
check('make an I, B, area record. I =' in st[1] and 'Check area with' not in st[1], 'P2: the check sentence is gone (could 8)')
check('Problem 3: Make a triangle and a four-sided shape, each with I = 2 and B = 6. Find their areas. I =' in st[2], 'P3: no opening question (could 9)')
check('Check at least one' not in st[4] and 'as many different (I, B) records as you can.' in st[4], 'P5: the check sentence is gone (could 8)')
check('Problem 8: Explain why Pick’s rule works for every allowed polygon, including these two.' in st[7]
      and 'Use the joining result' not in st[7] and 'test cases' not in st[7], 'P8: the new one-sentence task (fix 5)')


def dot_centres(page):
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if d['type'] == 'f' and d.get('fill') == (0, 0, 0) and abs(r.width - 1.1 * MM) < .05 and abs(r.height - 1.1 * MM) < .05:
            out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    return out


dots = dot_centres(doc[2])
xs = sorted({round(x, 1) for x, _ in dots})
ys = sorted({round(y, 1) for _, y in dots})
gaps = [b - a for a, b in zip(ys, ys[1:])]
big = [g for g in gaps if g > 21 * MM]
check(len(dots) == 50 and len(xs) == 5 and len(ys) == 10 and all(abs(b - a - 20 * MM) < .05 for a, b in zip(xs, xs[1:])),
      f'P3: 50 dots in 5 columns 20 mm apart and 10 rows (fix 4)')
check(len(big) == 1 and big[0] > 30 * MM and all(abs(g - 20 * MM) < .05 for g in gaps if g not in big),
      f'P3: two stacked 5 x 5 boards, rows 20 mm apart, {big[0] / MM if big else 0:.1f} mm between the boards (fix 4)')

m = fitz.open(WEEK / 'week-57-materials.pdf')
mt = [text(p) for p in m]
check(len(m) == 2 and all(t.startswith('Week 57 / Area from dots / Materials') and t.endswith(f'Bellingham Math Circle / Week 57 / N57-M-v1 {i+1}')
                          for i, t in enumerate(mt)), 'materials: 2 pages, header and footer N57-M-v1 (fix 6)')
for i, page in enumerate(m):
    segs = [(it[1], it[2]) for d in page.get_drawings() for it in d['items'] if it[0] == 'l']
    vert = sorted(a.x / MM for a, b in segs if abs(a.x - b.x) < .01 and abs(abs(a.y - b.y) - 200 * MM) < .05)
    horiz = sorted(a.y / MM for a, b in segs if abs(a.y - b.y) < .01 and abs(abs(a.x - b.x) - 120 * MM) < .05)
    diag = [s for s in segs if abs(abs(s[0].x - s[1].x) - 20 * MM) < .05 and abs(abs(s[0].y - s[1].y) - 20 * MM) < .05]
    bar = [s for s in segs if abs(s[0].y - s[1].y) < .01 and abs(abs(s[0].x - s[1].x) - 100 * MM) < .05]
    check(len(vert) == 7 and len(horiz) == 11 and all(abs(b - a - 20) < .02 for a, b in zip(vert, vert[1:]))
          and all(abs(b - a - 20) < .02 for a, b in zip(horiz, horiz[1:])), f'materials p{i+1}: a 6 x 10 grid of 20 mm squares, 60 squares')
    check(len(diag) == (60 if i else 0), f'materials p{i+1}: {len(diag)} diagonals of 20 mm squares')
    check(len(bar) == 1, f'materials p{i+1}: one 100 mm check bar')
check('60 squares, each 20 mm' in mt[0] and '120 halves' in mt[1], 'materials: 60 squares on p1, 120 halves from p2')

g = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-57-facilitator.pdf'), '-'], capture_output=True, text=True, check=True).stdout.split())
g = re.sub(r'(?<=[a-z])- (?=[a-z])', '', g)
check(fitz.open(WEEK / 'week-57-facilitator.pdf').page_count == 10 and g.count('W57-FAC-v2') == 10, 'guide: 10 pages, footer W57-FAC-v2')
for s in ['contact in two or more separate places, overlaps, pinches and closed seams do not satisfy this claim. A seam made of several consecutive sides does',
          'K–1 has an adult-led route with four or five squares on the existing grids (p. 3)',
          'Younger: the K–1 four-square route below, with the parent.',
          'K–1 route, outside the numbered packet.', 'Can you make a four-square shape with a different number?',
          'every four-square shape has 10 outline dots and none inside, except the 2 × 2 square, which has 8 and one inside',
          'Five squares give 12 outline dots, or 10 with one inside dot', 'Each inside dot means two fewer outline dots.',
          'Print week-57-materials.pdf once on card stock', 'plus the two materials pages on card stock',
          'Both options need the two materials pages.', 'Allow about 20–35 minutes once to cut the two printed materials pages',
          'measure a square (20 mm) and the 100 mm bar', 'The shared rule on p. 1 permits pieces, cuts or copies',
          'Both witness areas are 4.', '(0, 0), (2, 0), (1, 6) 6 × 1 rectangle', 'Base 3, height 2 Base 2, height 3 Base 2, height 6 The slender',
          'The slender parallelogram (0, 0), (2, 1), (6, 6), (4, 5) is also (5, 4)',
          'Do not accept it here: P8 proves Pick’s rule from this result, so explain it with the dots.',
          'every join used is along one side', 'student version N57-S-final-v3']:
    check(s in g, f'guide has "{s[:70]}"')
for s in ['several shared sides', 'K–1 shallow option', 'Week 1 pattern-block', 'oral shape/inside sorting', 'Yes. Both witness',
          'measure/cut the 120 raw squares', 'Cut 120 squares', '45–75 minutes', 'The page permits', 'For the last slender parallelogram',
          'no bent seam is passed off', 'Horizontal width 6/5 on the middle', 'REPUBLISHING', 'N57-S-final-v2', 'W57-FAC-v1']:
    check(s not in g, f'guide no longer has "{s}"')

print('PASS: Week 57 PDFs carry the card fixes' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
