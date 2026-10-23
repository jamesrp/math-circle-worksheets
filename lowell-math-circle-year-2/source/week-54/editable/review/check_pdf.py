#!/usr/bin/env python3
"""Read the Week 54 PDFs and check the October 23, 2026 card fixes on the printed pages.

    python3 check_pdf.py [FOLDER]   (FOLDER holds week-54-students.pdf and week-54-facilitator.pdf;
                                     default: the repository's print folder)

With PyMuPDF it checks the student packet's headers, footers and Problems 1-9; the
new wording on p. 1 and of Problems 6 and 9; Problem 7's six answer grids, each 5 x 5
cells of 0.22 in, the size of the input squares; and that the guide has the new
sentences and has lost the replaced ones.
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


def find_repo():
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found; pass the folder that holds the PDFs')


WEEK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_repo() / 'lowell-math-circle-year-2' / 'week-54'
FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def text(page):
    return ' '.join(re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', page.get_text()).split())


doc = fitz.open(WEEK / 'week-54-students.pdf')
st = [text(p) for p in doc]
nums = []
for i, t in enumerate(st):
    band = '2–5' if i < 5 else '4–5'
    check(t.startswith(f'Week 54 / Partitions and rebuilding / Grades {band}') and f'Bellingham Math Circle / Week 54 / W54-S-v1 {i+1}' in t,
          f'students p{i+1}: header Grades {band}, footer W54-S-v1, page {i+1}')
    nums += [int(n) for n in re.findall(r'Problem (\d+):', t)]
check(len(doc) == 9 and nums == list(range(1, 10)), f'students: 9 pages, Problems {nums}')
check('W54-S-v1 1 A collection uses all the units, in straight strips. Every strip has at least one unit.' in st[0]
      and 'Use all the units in a collection' not in st[0], 'p1: "A collection uses all the units, in straight strips." (fix 5)')
check('Problem 6: Try different legal joining routes for this collection until all sizes are different. Can the routes end with different collections? '
      'Decide whether this can happen from any collection with only odd sizes.' in st[5]
      and 'four 3-unit strips' not in st[5] and 'all-odd' not in st[5], 'P6: no longer repeats the picture in words; "only odd sizes" (fix 6)')
check('Problem 9: For any total, are there exactly as many collections with only odd sizes as collections with all sizes different? Explain how you know.' in st[8]
      and 'joining and splitting can decide' not in st[8], 'P9: "Explain how you know." does not name the method (fix 8)')

# Problem 7's grids: light grey lines 1.1 in long, 0.22 in apart
page = doc[6]
IN = 72
grey = [d for d in page.get_drawings() if d.get('color') and abs(d['color'][0] - 0.84) < 0.01 and d.get('width') and abs(d['width'] - 0.35) < 0.01]
segs = [(it[1], it[2]) for d in grey for it in d['items'] if it[0] == 'l']
vert = sorted((round(a.x / IN, 3), round(min(a.y, b.y) / IN, 3)) for a, b in segs if abs(a.x - b.x) < 0.01 and abs(abs(a.y - b.y) - 1.1 * IN) < 0.01)
horiz = sorted((round(min(a.x, b.x) / IN, 3), round(a.y / IN, 3)) for a, b in segs if abs(a.y - b.y) < 0.01 and abs(abs(a.x - b.x) - 1.1 * IN) < 0.01)
grids = {}
for x, y in vert:
    grids.setdefault(y, []).append(x)
ok = len(vert) == 36 and len(horiz) == 36 and len(grids) == 3
for y, xs in grids.items():
    for x0 in (3.45, 6.07):
        col = sorted(x for x in xs if x0 - 0.01 <= x <= x0 + 1.11)
        ok = ok and len(col) == 6 and all(abs(col[k] - (x0 + 0.22 * k)) < 0.002 for k in range(6))
squares = [d['rect'] for d in page.get_drawings() if d.get('fill') and abs(d['fill'][0] - 0.94) < 0.01]
sizes = {(round(r.width / IN, 3), round(r.height / IN, 3)) for r in squares if r.y0 > (11 - 6.7) * IN}
check(ok and sizes == {(0.22, 0.22)}, f'P7: six answer grids of 5 x 5 cells, 0.22 in apart; input squares {sorted(sizes)} in (fix 7)')

g = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-54-facilitator.pdf'), '-'], capture_output=True, text=True, check=True).stdout.split())
g = re.sub(r'(?<=[a-z])- (?=[a-z])', '', g)
check(fitz.open(WEEK / 'week-54-facilitator.pdf').page_count == 8, 'guide: 8 pages')
for s in ['K–1 has no packet of its own: an adult-led route uses the cubes on student pp. 1–3', 'K–1 route, adult-led, on student pp. 1–3',
          'Five collections: one strip of 4; 3 and 1; 2 and 2; 2, 1 and 1; four 1s', 'end as an 8 and a 1',
          'Four collections use only odd strips: 5 and 1; 3 and 3; 3, 1, 1 and 1; six 1s', 'Two kits of 12 linking cubes', '108 cubes',
          '24 identical linking cubes', 'loose squares touching end to end look like one strip', '24 cm with 2 cm cubes', '34 Week 54 sheets',
          'one legal join is 3 + 3 → 6', 'joining two 1s first is legal too', 'for 7 a largest size of 3 also fails, since 3 + 2 + 1 = 6',
          'try (6, 6, 1): it rejoins as (12, 1)', 'guide/check_answers.py']:
    check(s in g, f'guide has "{s}"')
for s in ['has one legal join', 'use loose touching squares if necessary', 'guide-src/', 'pattern-block kits', 'K–1 has no Week 54 packet',
          'unit squares or snap cubes', 'at most 18 cm']:
    check(s not in g, f'guide no longer has "{s}"')

print('PASS: Week 54 PDFs carry the card fixes' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
