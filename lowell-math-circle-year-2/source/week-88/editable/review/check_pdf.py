#!/usr/bin/env python3
"""Read the Week 88 PDFs and check the October 23, 2026 card fixes on the printed pages.

    python3 check_pdf.py [FOLDER]   (FOLDER holds week-88-students/materials/facilitator.pdf;
                                     default: the repository's print folder)

With PyMuPDF it checks
- the student packet: headers, footers and Problems 1-11; the three tray interiors
  (160 x 112, 110 and 108 mm, between the inner edges of the border strips) and no
  repeated "tray ... interior" caption; Problem 4's own "not actual size" caption below
  its figure; room for a six-ring (60 mm) above and below Problem 6's actual-size 40 mm
  middle; the revised wording of Problems 7, 10 and 11;
- the materials pages: every circle is round and has the stated diameter (40, 80 or
  120 mm, to 0.01 mm) with a dot at its centre, no two circles come within 3 mm of each
  other, every circle is at least 15 mm inside the paper edge, each page has a 100 mm bar,
  and the guide's print recipe (page 1 five times, page 2 twice, page 3 three times) gives
  at least 65 small, 25 large and three 120 mm disks;
- the guide: the new sentences are present and the replaced ones are gone.
"""
import math
import re
import subprocess
import sys
from pathlib import Path

try:
    import pymupdf as fitz  # PyMuPDF >= 1.24
except ImportError:
    import fitz  # older PyMuPDF

HERE = Path(__file__).resolve().parent


def find_repo():
    for p in HERE.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    sys.exit('repository not found; pass the folder that holds the PDFs')


WEEK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_repo() / 'lowell-math-circle-year-2' / 'week-88'
MM = 25.4 / 72  # millimetres per point
PAGE_W, PAGE_H = 215.9, 279.4
FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def text(page):
    return ' '.join(re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', page.get_text()).split())


def circles(page):
    out = []
    for d in page.get_drawings():
        kinds = [it[0] for it in d['items']]
        if kinds.count('c') >= 4 and set(kinds) <= {'c'}:
            r = d['rect']
            out.append({'cx': (r.x0 + r.x1) / 2 * MM, 'cy': (r.y0 + r.y1) / 2 * MM, 'w': r.width * MM, 'h': r.height * MM,
                        'filled': d.get('fill') is not None, 'stroked': d.get('color') is not None})
    return out


def blocks(page):
    return [(b[1] * MM, b[3] * MM, ' '.join(b[4].split())) for b in page.get_text('blocks')]


# ------------------------------------------------------------------ student packet
doc = fitz.open(WEEK / 'week-88-students.pdf')
nums = []
for i, page in enumerate(doc):
    t = text(page)
    check(t.startswith('Week 88 / Packing and kissing circles / Grades K–5') and f'Bellingham Math Circle / Week 88 / W88-shared-v2 {i+1}' in t,
          f'students p{i+1}: header, footer W88-shared-v2, page {i+1}')
    nums += [int(n) for n in re.findall(r'Problem (\d+):', t)]
check(len(doc) == 8 and nums == list(range(1, 12)), f'students: 8 pages, Problems {nums}')

for pno, H in ((2, 112), (6, 110), (7, 108)):
    page = doc[pno - 1]
    strips = [d['rect'] for d in page.get_drawings() if d.get('fill') is not None and d['rect'].width * MM > 0.3 and d['rect'].height * MM > 0.3
              and (d['rect'].width * MM > 100 or d['rect'].height * MM > 100)]
    horiz = sorted([r for r in strips if r.width * MM > 100], key=lambda r: r.y0)
    vert = sorted([r for r in strips if r.height * MM > 100], key=lambda r: r.x0)
    W = (vert[1].x0 - vert[0].x1) * MM
    Hm = (horiz[1].y0 - horiz[0].y1) * MM
    check(abs(W - 160) < 0.01 and abs(Hm - H) < 0.01, f'p{pno}: tray interior {W:.3f} x {Hm:.3f} mm')
    check('interior' not in text(page), f'p{pno}: the repeated "tray: 160 mm x {H} mm interior" caption is gone (could 11)')

page = doc[2]
cs = sorted(circles(page), key=lambda c: c['cy'])
caps = [y0 for y0, y1, t in blocks(page) if 'not actual size' in t]
p4_top = max(y1 for y0, y1, t in blocks(page) if t.startswith('Problem 4:'))
p4 = [c for c in cs if c['cy'] > p4_top]
check(len(p4) == 2 and any(y > max(c['cy'] + c['h'] / 2 for c in p4) for y in caps), 'p3: Problem 4\'s figure has its own "Sketches, not actual size" caption below it (could 9)')

page = doc[4]
mid = [c for c in circles(page) if c['filled'] and abs(c['w'] - 40) < 0.01]
check(len(mid) == 1, 'p5: Problem 6 has one actual-size 40 mm middle')
up = mid[0]['cy'] - max(y1 for y0, y1, t in blocks(page) if y1 < mid[0]['cy'] and not t.startswith('Week 88'))
down = min([y0 for y0, y1, t in blocks(page) if y0 > mid[0]['cy']]) - mid[0]['cy']
check(up >= 60 and down >= 60, f'p5: {up:.1f} mm clear above and {down:.1f} mm below the middle centre; a six-ring reaches 60 mm (could 10)')

st = [text(p) for p in doc]
check('Problem 7: Can eleven 40 mm disks fit in this tray in three straight horizontal rows: 4, then 3, then 4? Explain how you know.' in st[5]
      and 'center distances' not in st[5], 'P7 asks whether the rows fit and leaves the method open (fix 6)')
check('Problem 10: For each of Problems 3–5, what is the largest possible ring? Explain why no ring can have more outside disks.' in st[7]
      and 'Return to your rings' not in st[7], 'P10 asks for the largest rings, so a child with a smaller ring is not asked to prove a falsehood (fix 2)')
check('Problem 11: Make the biggest ring of 40 mm disks around a 120 mm disk.' in st[7], 'P11 starts with the 120 mm ring (fix 4)')

# ------------------------------------------------------------------ materials
mat = fitz.open(WEEK / 'week-88-materials.pdf')
check(len(mat) == 3, f'materials: 3 pages ({len(mat)})')
counts = []
for i, page in enumerate(mat):
    t = text(page)
    check(t.startswith('Week 88 / Packing and kissing circles / Materials') and f'Bellingham Math Circle / Week 88 / W88-M-v2 {i+1}' in t,
          f'materials p{i+1}: header, footer W88-M-v2, page {i+1}')
    cs = circles(page)
    disks = [c for c in cs if c['stroked'] and not c['filled']]
    dots = [c for c in cs if c['filled'] and c['w'] < 1.5]
    sizes = {}
    for c in disks:
        size = min((40, 80, 120), key=lambda s: abs(c['w'] - s))
        sizes[size] = sizes.get(size, 0) + 1
        ok = abs(c['w'] - size) < 0.01 and abs(c['h'] - size) < 0.01
        ok = ok and any(math.hypot(d['cx'] - c['cx'], d['cy'] - c['cy']) < 0.01 for d in dots)
        ok = ok and min(c['cx'] - c['w'] / 2, c['cy'] - c['w'] / 2, PAGE_W - c['cx'] - c['w'] / 2, PAGE_H - c['cy'] - c['w'] / 2) >= 15
        if not ok:
            check(False, f'materials p{i+1}: circle at ({c["cx"]:.1f}, {c["cy"]:.1f}) is {c["w"]:.3f} x {c["h"]:.3f} mm, centred dot, 15 mm inside the paper')
    gaps = [math.hypot(a['cx'] - b['cx'], a['cy'] - b['cy']) - (a['w'] + b['w']) / 2 for k, a in enumerate(disks) for b in disks[k + 1:]]
    bars = [d['rect'] for d in page.get_drawings() for it in d['items'] if it[0] == 'l' and abs(it[1].y - it[2].y) < 0.01 and abs(abs(it[2].x - it[1].x) * MM - 100) < 0.01]
    check(all(abs(c['w'] - min((40, 80, 120), key=lambda s: abs(c['w'] - s))) < 0.01 for c in disks) and len(dots) == len(disks)
          and min(gaps) >= 3 - 1e-6 and bars,
          f'materials p{i+1}: {dict(sorted(sizes.items()))} disks, each round to 0.01 mm with a centre dot; closest pair {min(gaps):.1f} mm apart; 100 mm bar')
    counts.append(sizes)
check(counts == [{80: 4, 40: 4}, {40: 20}, {120: 1, 40: 3, 80: 2}], f'materials: per-page disks {counts}')
recipe = {s: 5 * counts[0].get(s, 0) + 2 * counts[1].get(s, 0) + 3 * counts[2].get(s, 0) for s in (40, 80, 120)}
check(recipe[40] >= 65 and recipe[80] >= 25 and recipe[120] == 3, f'materials: pages 1 x5, 2 x2, 3 x3 give {recipe[40]} small, {recipe[80]} large, {recipe[120]} 120 mm (guide p. 2)')

# ------------------------------------------------------------------ guide
g = ' '.join(subprocess.run(['pdftotext', str(WEEK / 'week-88-facilitator.pdf'), '-'], capture_output=True, text=True, check=True).stdout.split())
g = re.sub(r'(?<=[a-z])- (?=[a-z])', '', g)
for s in ['adds about 2.7 mm of height but no width', 'Where the disks come from.', 'How exact the disks must be.',
          'page 2 twice and page 3 three times: 26 large, 69 small and three 120 mm disks',
          'Use disks measured at 39.7–40.0 mm for Problems 7–9', 'for the Grades 4–5 trio print pages 1–5, with Problem 6 as the target',
          'about 18.5◦ more around the 80 mm middle and about 21◦ more around the 40 mm middle', 'six green pattern-block triangles',
          'Around the 120 mm middle twelve 40 mm disks fit', 'Problem 10 without angles.', 'leave about 9 mm between the first and the last',
          'three fixed tables (K, K, 1, 1; four third graders; 4, 4, 5)']:
    check(s in g, f'guide has "{s[:70]}"')
for s in ['gives more tolerance', 'can change which size consumes the most room', 'KK11', 'in[20', 'For(20', 'radiia']:
    check(s not in g, f'guide no longer has "{s}"')

print('PASS: Week 88 PDFs carry the card fixes' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
