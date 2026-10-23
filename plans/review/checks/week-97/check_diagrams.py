#!/usr/bin/env python3
"""Diagram and delivered-PDF checks for Week 97 (Square remainders).

Written for the math-check stage of the review. Reads the delivered PDFs with
PyMuPDF (pymupdf) and the guide source; does not use the package's checker.

What it checks
- Student PDF, every page: header, footer, one numbered problem per page,
  problems numbered 1-6 in order.
- Student p. 1: the opening picture (a 3x3 square of dots, equal spacing in
  both directions; two loops of 4 dots and one dot outside; one output dot)
  and Problem 1's five input boxes (n x n dots in box n, square grid, inside
  its box, "0 counters" in box 0).
- Student pp. 2-6: every printed fact card read back from the PDF text
  (a x a = a^2), and the inputs covered on each page.
- Guide p. 4 strip diagram: rectangles read from the PDF drawings, their
  side ratios (equal scaling) and areas 70, 21, 9 out of 100.
- Rebuild: recompiles students.tex and facilitator.tex with pdflatex into a
  scratch folder beside this script and compares extracted text and SHA-256
  with the delivered PDFs, so the sources read are the sources printed.

Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import hashlib, os, re, shutil, subprocess, tempfile
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and \
            (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-97'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-97'
STUD = WEEK / 'week-97-students.pdf'
GUIDE = WEEK / 'week-97-facilitator.pdf'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def close(a, b, tol=0.6):
    return abs(a - b) <= tol


# ------------------------------------------------------------- student pages
say('== Student PDF: headers, footers, problem numbers ==')
doc = pymupdf.open(STUD)
check(doc.page_count == 6, 'student PDF has 6 pages (%d)' % doc.page_count)
nums = []
for i, page in enumerate(doc, start=1):
    t = page.get_text()
    check('Week 97 / Square remainders / Grades 3–5' in t, 'p.%d header' % i)
    check('Bellingham Math Circle / Week 97 / W97-35-v1' in t, 'p.%d footer' % i)
    found = [int(x) for x in re.findall(r'Problem (\d+):', t)]
    check(len(found) == 1, 'p.%d has one numbered problem: %s' % (i, found))
    nums += found
check(nums == [1, 2, 3, 4, 5, 6], 'problems numbered consecutively: %s' % nums)
check(all(('Name' not in pg.get_text() and 'Date' not in pg.get_text()) for pg in doc), 'no Name/Date fields')

# ------------------------------------------------------------- page 1 dots
say('\n== Student p.1: opening picture and Problem 1 boxes ==')
p1 = doc[0]
dr = p1.get_drawings()
dots = []
for d in dr:
    r = d['rect']
    if d['type'] == 'f' and 3.5 < r.width < 6 and 3.5 < r.height < 6:
        dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
loops = [d['rect'] for d in dr if d['type'] == 's' and d.get('color') == (0.0, 0.0, 0.0)
         and d['rect'].width > 20 and d['rect'].height > 20]
boxes = sorted([d['rect'] for d in dr if d['type'] == 's' and d.get('color') and d['color'][0] > 0.7
                and 80 < d['rect'].width < 100], key=lambda r: r.x0)
say('   dots found: %d; black loops: %d; grey input boxes: %d' % (len(dots), len(loops), len(boxes)))
top = [p for p in dots if p[1] < 250]
low = [p for p in dots if p[1] > 380]


def grid_ok(pts, n):
    """pts form an n x n square grid with equal spacing in x and y."""
    if len(pts) != n * n:
        return False, 'count %d' % len(pts)
    if n <= 1:
        return True, 'single'
    xs = sorted({round(p[0], 1) for p in pts}); ys = sorted({round(p[1], 1) for p in pts})
    if len(xs) != n or len(ys) != n:
        return False, 'columns %d rows %d' % (len(xs), len(ys))
    dx = [b - a for a, b in zip(xs, xs[1:])]; dy = [b - a for a, b in zip(ys, ys[1:])]
    ok = all(close(v, dx[0]) for v in dx + dy)
    return ok, 'spacing x %s y %s' % ([round(v, 2) for v in dx], [round(v, 2) for v in dy])


three = [p for p in top if p[0] < 200]
ok, info = grid_ok(three, 3)
check(ok, 'opening: input 3 drawn as a 3 x 3 square grid (%s)' % info)
check(len(loops) == 2, 'opening: two bundle loops')
in_loop = [[p for p in top if L.x0 < p[0] < L.x1 and L.y0 < p[1] < L.y1] for L in loops]
check([len(x) for x in in_loop] == [4, 4], 'opening: each loop holds 4 dots %s' % [len(x) for x in in_loop])
mid = [p for p in top if 200 < p[0] < 400]
outside = [p for p in mid if not any(L.x0 < p[0] < L.x1 and L.y0 < p[1] < L.y1 for L in loops)]
check(len(mid) == 9 and len(outside) == 1, 'opening: 9 dots in the bundle picture, 1 outside the loops')
right = [p for p in top if p[0] > 400]
check(len(right) == 1, 'opening: output picture shows 1 dot')

check(len(boxes) == 5, 'Problem 1: five input boxes')
t1 = p1.get_text('words')
for n, B in enumerate(boxes):
    inside = [p for p in low if B.x0 < p[0] < B.x1 and B.y0 < p[1] < B.y1]
    ok, info = grid_ok(inside, n)
    label = ' '.join(w[4] for w in t1 if B.x0 < w[0] < B.x1 and B.y0 < w[1] < B.y1)
    check(ok and ('Input %d' % n) in label, 'Problem 1 box %d: label "%s", %d dots, %s' % (n, label, len(inside), info))
    if n == 0:
        check('0 counters' in label, 'Problem 1 box 0 says "0 counters"')
check(len(low) == sum(n * n for n in range(5)), 'Problem 1: 30 dots in all, none stray')

# ------------------------------------------------------------- cards in PDF
say('\n== Student pp.2-6: fact cards read from the PDF ==')
need = {2: range(0, 7), 3: range(0, 9), 4: range(0, 15), 5: range(7, 16), 6: range(0, 11)}
total = 0
for i in range(2, 7):
    t = doc[i - 1].get_text().replace('×', 'x').replace('−', '-')
    cards = [(int(a), int(b), int(c)) for a, b, c in re.findall(r'(\d+)\s*x\s*(\d+)\s*=\s*(\d+)', t)]
    total += len(cards)
    bad = [c for c in cards if not (c[0] == c[1] and c[2] == c[0] * c[0])]
    check(not bad, 'p.%d: %d cards, all a x a = a^2 %s' % (i, len(cards), bad or ''))
    check(sorted(c[0] for c in cards) == list(need[i]), 'p.%d: inputs on cards %s' % (i, sorted(c[0] for c in cards)))
check(total == 51, 'cards printed in total: %d' % total)

# ------------------------------------------------------------- guide strip
say('\n== Guide p.4: strip diagram ==')
g = pymupdf.open(GUIDE)
check(g.page_count == 6, 'guide PDF has 6 pages (%d)' % g.page_count)
heads = {1: 'Mathematical overview', 2: 'Preparation, launch', 3: 'Problems 1', 4: 'Problems 4',
         5: 'Problem 6: the odd-prime rule', 6: 'Optional return visit'}
for k, v in heads.items():
    check(v in g[k - 1].get_text(), 'guide p.%d begins section "%s" (page references in the overview)' % (k, v))
gd = g[3].get_drawings()
fills = [d['rect'] for d in gd if d['type'] == 'f' and d['rect'].width > 10 and d['rect'].height > 10]
fills.sort(key=lambda r: r.x0)
outer = [d['rect'] for d in gd if d['type'] == 's' and d['rect'].width > 60 and d['rect'].height > 60]
check(len(fills) == 2 and len(outer) >= 1, 'two shaded regions and the outer square found')
if len(fills) == 2 and outer:
    O = outer[0]
    unit = O.width / 10
    check(close(O.width, O.height, 0.3), 'outer square is square: %.2f x %.2f pt' % (O.width, O.height))
    big, strip = fills
    dims = lambda r: (round(r.width / unit, 2), round(r.height / unit, 2))
    check(dims(big) == (7.0, 10.0), 'left region is 7 x 10 units: %s' % (dims(big),))
    check(dims(strip) == (3.0, 7.0), 'strip is 3 x 7 units: %s' % (dims(strip),))
    rest = 100 - 70 - 21
    check(rest == 9, 'unshaded corner is 3 x 3 = 9 = 100 - 70 - 21')
gt = g[3].get_text()
check('7 × 10 = 70' in gt.replace('\n', ' ') or '7 × 10 = 70' in gt or '7×10' in gt.replace(' ', ''),
      'label "7 x 10 = 70" present')

# ------------------------------------------------------------- rebuild
say('\n== Rebuild from source and compare ==')
latex = shutil.which('pdflatex')
if not latex:
    check(False, 'pdflatex not found')
else:
    env = dict(os.environ, SOURCE_DATE_EPOCH='1792195200', FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix='w97-rebuild-', dir=HERE) as tmp:
        for kind, name, delivered in (('student', 'students', STUD), ('guide', 'facilitator', GUIDE)):
            folder = Path(tmp) / kind
            folder.mkdir()
            shutil.copy2(SRC / kind / (name + '.tex'), folder)
            for _ in range(2):
                r = subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error', name + '.tex'],
                                   cwd=folder, env=env, capture_output=True, text=True)
            check(r.returncode == 0, '%s.tex compiles' % name)
            built = folder / (name + '.pdf')
            if built.exists():
                same_hash = hashlib.sha256(built.read_bytes()).hexdigest() == \
                    hashlib.sha256(delivered.read_bytes()).hexdigest()
                tb = ''.join(pg.get_text() for pg in pymupdf.open(built))
                td = ''.join(pg.get_text() for pg in pymupdf.open(delivered))
                check(tb == td, '%s: rebuilt text identical to delivered PDF (sha256 identical: %s)' % (name, same_hash))

say('\nFAILURES: %d' % len(FAIL))
for f in FAIL:
    say('  ' + f)
text = '\n'.join(OUT) + '\n'
(HERE / 'check_diagrams.py.out').write_text(text)
print(text)
