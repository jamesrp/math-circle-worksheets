"""Independent reader of the final K-1 student pages (k-1.pdf).

Finds every bucket outline (rounded rectangle, taller than wide) and every
filled dot, assigns each dot to the bucket that contains it, and prints the
bucket pictures page by page, grouped into rows and left-to-right order,
so the starts can be compared with the guide's tables.
Usage: python3 -I parse_pages.py [path/to/k-1.pdf]
"""
import sys, os
import pymupdf as fitz

here = os.path.dirname(os.path.abspath(__file__))
cands = [os.path.join(here, '..', '..', '..', 'k1-drafts', 'week-81', 'k-1.pdf')]
path = sys.argv[1] if len(sys.argv) > 1 else cands[0]
doc = fitz.open(path)
MM = 25.4 / 72

for pno, pg in enumerate(doc, start=1):
    buckets, dots = [], []
    for d in pg.get_drawings():
        r = d['rect']
        w, h = r.width * MM, r.height * MM
        if d.get('fill') is not None and d.get('type') in ('f', 'fs') and 1.5 < w < 5 and abs(w - h) < 0.5:
            dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
        elif d.get('type') in ('s', 'fs') and 8 < w < 60 and h > w * 1.1 and h < 150:
            # outline taller than wide: a bucket
            buckets.append(r)
    # de-duplicate
    uniq = []
    for b in buckets:
        if not any(abs(b.x0 - u.x0) < 1 and abs(b.y0 - u.y0) < 1 for u in uniq):
            uniq.append(b)
    rows = {}
    for b in uniq:
        n = sum(1 for (x, y) in dots if b.x0 <= x <= b.x1 and b.y0 <= y <= b.y1)
        key = round(b.y0 * MM / 4)
        rows.setdefault(key, []).append((b.x0 * MM, b.width * MM, b.height * MM, n))
    print(f"--- page {pno}: {len(uniq)} buckets, {len(dots)} dots")
    for key in sorted(rows):
        row = sorted(rows[key])
        print(f"  y~{key*4:>3} mm:", ' '.join(f"[{n}]{'' if w>12 else 's'}" for (x, w, h, n) in row),
              " sizes:", sorted(set((round(w), round(h)) for (x, w, h, n) in row)))
