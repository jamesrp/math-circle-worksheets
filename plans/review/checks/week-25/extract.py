"""Read every board back out of the delivered Week 25 PDFs (vector data).

For each page: the grids (cell lines), the cell size in mm on both axes,
row letters, column numbers, circled row/column counts, and the filled
counters (dots).  Works on the TikZ student packets and the ReportLab guide.
Output: extracted.json (and a readable summary on stdout).
"""
import json
import os
import sys
from collections import defaultdict

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WEEK, HERE  # noqa: E402

PT_PER_MM = 72 / 25.4
FILES = ['week-25-k-1.pdf', 'week-25-grades-2-3.pdf', 'week-25-grades-4-5.pdf',
         'week-25-facilitator.pdf']


def r1(v):
    return round(v, 1)


def page_boards(page):
    drs = page.get_drawings()
    words = page.get_text('words')
    H = defaultdict(set)   # (xa, xb) -> {y}
    V = defaultdict(set)   # (ya, yb) -> {x}
    dots, rings = [], []
    for d in drs:
        items = d['items']
        if d['type'] == 's' and len(items) == 1 and items[0][0] == 'l' and 0.5 <= (d.get('width') or 0) <= 0.6:
            p, q = items[0][1], items[0][2]
            if abs(p.y - q.y) < 0.01:
                H[(r1(min(p.x, q.x)), r1(max(p.x, q.x)))].add(r1(p.y))
            elif abs(p.x - q.x) < 0.01:
                V[(r1(min(p.y, q.y)), r1(max(p.y, q.y)))].add(r1(p.x))
        elif items and all(it[0] == 'c' for it in items):
            rect = d['rect']
            if d['type'] == 'f':
                dots.append(rect)
            elif d['type'] == 's':
                rings.append(rect)
    boards = []
    for (xa, xb), ys in H.items():
        for (ya, yb), xs in V.items():
            if ya in ys and yb in ys and xa in xs and xb in xs:
                bxs = sorted(x for x in xs if xa - .05 <= x <= xb + .05)
                bys = sorted(y for y in ys if ya - .05 <= y <= yb + .05)
                boards.append((xa, xb, ya, yb, bxs, bys))
    # drop boards that are unions of others (none expected, but be safe)
    out = []
    for (xa, xb, ya, yb, bxs, bys) in boards:
        nc, nr = len(bxs) - 1, len(bys) - 1
        cw = [bxs[i + 1] - bxs[i] for i in range(nc)]
        ch = [bys[i + 1] - bys[i] for i in range(nr)]
        cell = cw[0]
        pic = [['0'] * nc for _ in range(nr)]
        for rct in dots:
            cx, cy = (rct.x0 + rct.x1) / 2, (rct.y0 + rct.y1) / 2
            if xa < cx < xb and ya < cy < yb:
                j = int((cx - xa) // cell)
                i = int((cy - ya) // ch[0])
                # dot must be centred in its cell
                assert abs(cx - (bxs[j] + bxs[j + 1]) / 2) < .6 and abs(cy - (bys[i] + bys[i + 1]) / 2) < .6, (cx, cy)
                pic[i][j] = '1'

        def text_in(rect):
            return ''.join(w[4] for w in words
                           if rect.x0 - 1 <= (w[0] + w[2]) / 2 <= rect.x1 + 1 and rect.y0 - 1 <= (w[1] + w[3]) / 2 <= rect.y1 + 1)
        rowc, colc = [None] * nr, [None] * nc
        for rg in rings:
            cx, cy = (rg.x0 + rg.x1) / 2, (rg.y0 + rg.y1) / 2
            if xb < cx < xb + 1.2 * cell:
                for i in range(nr):
                    if abs(cy - (bys[i] + bys[i + 1]) / 2) < .6:
                        rowc[i] = text_in(rg)
            if yb < cy < yb + 1.0 * cell:
                for j in range(nc):
                    if abs(cx - (bxs[j] + bxs[j + 1]) / 2) < .6:
                        colc[j] = text_in(rg)
        rowl, coll = [], []
        for i in range(nr):
            mid = (bys[i] + bys[i + 1]) / 2
            rowl.append(''.join(w[4] for w in words if xa - 30 < w[2] <= xa + .5 and abs((w[1] + w[3]) / 2 - mid) < 4))
        for j in range(nc):
            mid = (bxs[j] + bxs[j + 1]) / 2
            coll.append(''.join(w[4] for w in words if ya - 25 < w[3] <= ya + .5 and abs((w[0] + w[2]) / 2 - mid) < 4))
        out.append({
            'x': round(xa, 1), 'y': round(ya, 1), 'rows': nr, 'cols': nc,
            'cell_w_mm': sorted({round(c / PT_PER_MM, 2) for c in cw}),
            'cell_h_mm': sorted({round(c / PT_PER_MM, 2) for c in ch}),
            'row_labels': rowl, 'col_labels': coll,
            'row_counts': rowc, 'col_counts': colc,
            'picture': '/'.join(''.join(r) for r in pic),
        })
    out.sort(key=lambda b: (round(b['y'] / 20), b['x']))
    return out


def main():
    result = {}
    for f in FILES:
        doc = pymupdf.open(os.path.join(WEEK, f))
        pages = []
        for n, page in enumerate(doc, 1):
            text = ' '.join(page.get_text('text').split())
            pages.append({'page': n, 'text': text, 'boards': page_boards(page)})
        result[f] = pages
    with open(os.path.join(HERE, 'extracted.json'), 'w') as fh:
        json.dump(result, fh, indent=1)
    for f, pages in result.items():
        print('=' * 70)
        print(f)
        for pg in pages:
            if not pg['boards']:
                continue
            print(f"  page {pg['page']}: {len(pg['boards'])} boards")
            for b in pg['boards']:
                rc = ','.join(x if x is not None else '-' for x in b['row_counts'])
                cc = ','.join(x if x is not None else '-' for x in b['col_counts'])
                print(f"    {b['rows']}x{b['cols']} cell {b['cell_w_mm']}x{b['cell_h_mm']} mm  "
                      f"labels {''.join(b['row_labels'])}/{''.join(b['col_labels'])}  "
                      f"rows[{rc}] cols[{cc}]  picture {b['picture']}")


if __name__ == '__main__':
    main()
