#!/usr/bin/env python3
"""Measure week-99-materials.pdf from its vector drawing, not a render.

    python3 materials/check_materials.py [path/to/week-99-materials.pdf]

Page 1, line mat: landscape US Letter; two rows of six 30 mm bins whose centers are
35 mm apart; a 16-box move strip; a 100 mm scale line. Page 2, star roads: four
35 mm circles (O and three leaves, 56 mm from O) joined only O-A, O-B, O-C; a small
target star of four 20 mm circles; a 100 mm scale line. Every mark lies at least
10 mm inside the page. Header, footer id and page numbers are read from the text.
Needs PyMuPDF.
"""
import math, sys
from pathlib import Path
try:
    import pymupdf as fitz
except ImportError:
    import fitz

MM = 72 / 25.4
path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / 'week-99' / 'week-99-materials.pdf'
doc = fitz.open(path)
fails = []
def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)
near = lambda a, b, tol=0.15: abs(a - b) <= tol          # millimetres

check(len(doc) == 2, f'{len(doc)} pages')
for i, page in enumerate(doc, 1):
    w, h = page.rect.width / MM, page.rect.height / MM
    check(near(w, 279.4, .05) and near(h, 215.9, .05), f'page {i} is landscape US Letter ({w:.1f} x {h:.1f} mm)')
    text = ' '.join(page.get_text().split())
    last = max((wd for wd in page.get_text('words') if wd[1] > page.rect.height - 20 * MM), key=lambda wd: wd[2])  # rightmost footer word
    check('Week 99 / Moving piles / Mats' in text and 'Bellingham Math Circle / Week 99 / W99-MAT-v1' in text
          and last[4] == str(i), f'page {i}: header, footer id and page number')
    boxes = [d['rect'] for d in page.get_drawings()]
    out = [r for r in boxes if r.x0 / MM < 10 or r.y0 / MM < 10 or (page.rect.width - r.x1) / MM < 10 or (page.rect.height - r.y1) / MM < 10]
    check(not out, f'page {i}: every drawn mark at least 10 mm inside the page')
    scale = [r for r in boxes if near(r.width / MM, 100, .3) and r.height / MM < 1.5]
    check(len(scale) == 1, f'page {i}: one 100 mm scale line ({[round(r.width / MM, 2) for r in scale]} mm)')

def squares(page, size, tol=0.3):
    """Drawn paths whose bounding box is a size-by-size square (line width included approximately)."""
    out = []
    for d in page.get_drawings():
        r, lw = d['rect'], (d.get('width') or 0) / MM
        if near(r.width / MM - lw, size, tol) and near(r.height / MM - lw, size, tol) or \
           near(r.width / MM, size, tol) and near(r.height / MM, size, tol):
            out.append(((r.x0 + r.x1) / 2 / MM, (r.y0 + r.y1) / 2 / MM, r.width / MM))
    return sorted(set((round(x, 2), round(y, 2), round(s, 2)) for x, y, s in out))

p1 = doc[0]
bins = squares(p1, 30)
rows = sorted({b[1] for b in bins})
check(len(bins) == 12 and len(rows) == 2, f'page 1: 12 bins of 30 mm in two rows ({len(bins)} found)')
for y in rows:
    xs = sorted(b[0] for b in bins if b[1] == y)
    gaps = [round(b - a, 2) for a, b in zip(xs, xs[1:])]
    check(len(xs) == 6 and all(near(g, 35, .1) for g in gaps), f'page 1: row at y={y:.1f} mm has six bins, centers {gaps} mm apart')
check(len(rows) == 2 and [sorted(b[0] for b in bins if b[1] == y) for y in rows][0] == [sorted(b[0] for b in bins if b[1] == y) for y in rows][1],
      'page 1: moving lane and target row line up bin for bin')
words = [w[4] for w in p1.get_text('words')]
check(all(str(n) in words for n in range(6)) and 'moving' in words and 'target' in words and 'moves' in words, 'page 1: bins numbered 0-5; rows labelled')
strip = [d['rect'] for d in p1.get_drawings() if near(d['rect'].width / MM, 13, .3) and near(d['rect'].height / MM, 11, .3)]
check(len(strip) == 16, f'page 1: move strip of 16 boxes, 13 x 11 mm ({len(strip)} found)')

p2 = doc[1]
def circles(page, diameter):
    return [c[:2] for c in squares(page, diameter, .4)]
big, small = circles(p2, 35), circles(p2, 20)
check(len(big) == 4 and len(small) == 4, f'page 2: four 35 mm and four 20 mm circles ({len(big)}, {len(small)})')
def star(cs, arm):
    o = min(cs, key=lambda c: sum(math.dist(c, d) for d in cs))
    leaves = [c for c in cs if c != o]
    return o, leaves, [math.dist(o, l) for l in leaves]
for name, cs, arm in (('large', big, 56), ('target', small, 33)):
    if len(cs) == 4:
        o, leaves, ds = star(cs, arm)
        check(all(near(d, arm, .3) for d in ds), f'page 2: {name} star leaves {[round(d, 2) for d in ds]} mm from O')
        segs = []
        for d in p2.get_drawings():
            for it in d['items']:
                if it[0] == 'l':
                    segs.append(((it[1].x / MM, it[1].y / MM), (it[2].x / MM, it[2].y / MM)))
        def joins(a, b, r):
            return any(min(math.dist(p, a), math.dist(q, a)) < r + 1.5 and min(math.dist(p, b), math.dist(q, b)) < r + 1.5
                       and abs((q[0] - p[0]) * (b[1] - a[1]) - (q[1] - p[1]) * (b[0] - a[0])) < 2 * math.dist(a, b) for p, q in segs)
        r = 17.5 if name == 'large' else 10
        check(all(joins(o, l, r) for l in leaves), f'page 2: {name} star has a road from O to each leaf')
        check(not any(joins(a, b, r) for a in leaves for b in leaves if a < b), f'page 2: {name} star has no road between leaves')
words2 = [w[4] for w in p2.get_text('words')]
check(sum(w in ('A', 'B', 'C') for w in words2) == 6 and words2.count('O') + words2.count('O;') >= 2, 'page 2: both stars labelled A, B, C and O')
print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
