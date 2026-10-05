"""Read every counter strip back out of the delivered Week 18 student PDFs.

For each page: every strip (found by its left-end arrow), its number of cells,
cell size in cm, contents (0 = empty circle, 1 = filled circle or digit 1,
- = blank cell), and the picture icon to its left. Also every stand-alone
picture icon (pages with answer lines instead of strips).

Writes pdf_strips.json and prints a readable summary.
"""
import json
import pymupdf
from repo import WEEK, HERE

PT_PER_CM = 72 / 2.54
BANDS = ['k-1', 'grades-2-3', 'grades-4-5']


def cm(v):
    return round(v / PT_PER_CM, 3)


def classify_icon(d):
    items = d['items']
    kinds = [it[0] for it in items]
    r = d['rect']
    if kinds == ['l'] * 3:
        return 'triangle'
    if kinds == ['l'] * 4:
        p0, p1 = items[0][1], items[0][2]
        if abs(p0.x - p1.x) < 0.01 or abs(p0.y - p1.y) < 0.01:
            return 'square'
        return 'diamond'
    if kinds == ['l'] * 10 or (len(kinds) >= 9 and set(kinds) == {'l'}):
        return 'star'
    if 're' in kinds and len(kinds) == 1:
        return 'square'
    return 'other:' + ''.join(kinds)


def page_data(page):
    drawings = page.get_drawings()
    arrows = [d for d in drawings if d['type'] == 'f' and d['fill'] == (0.0, 0.0, 0.0)
              and [it[0] for it in d['items']] == ['l'] * 3 and d['rect'].width < 8]
    rects = [d for d in drawings if d['type'] == 's' and d['color'] == (0.0, 0.0, 0.0)
             and [it[0] for it in d['items']] == ['l'] * 4]
    seps = [d for d in drawings if d['type'] == 's' and [it[0] for it in d['items']] == ['l']
            and abs(d['rect'].width) < 0.01]
    circles = [d for d in drawings if [it[0] for it in d['items']] == ['c'] * 4 and d['fill'] is not None]
    words = page.get_text('words')
    strips = []
    used_rects = set()
    for a in arrows:
        ar = a['rect']
        cy = (ar.y0 + ar.y1) / 2
        best = None
        for i, s in enumerate(rects):
            r = s['rect']
            if abs(r.x0 - (ar.x1 + 0.12 * PT_PER_CM)) < 1.0 and r.y0 - 1 < cy < r.y1 + 1:
                best = (i, r)
        if best is None:
            continue
        i, r = best
        used_rects.add(i)
        xs = sorted({round(sp['rect'].x0, 2) for sp in seps
                     if r.x0 + 1 < sp['rect'].x0 < r.x1 - 1 and abs(sp['rect'].y0 - r.y0) < 1 and abs(sp['rect'].y1 - r.y1) < 1})
        edges = [r.x0] + xs + [r.x1]
        cells = []
        for x0, x1 in zip(edges, edges[1:]):
            val = '-'
            for c in circles:
                cr = c['rect']
                ccx, ccy = (cr.x0 + cr.x1) / 2, (cr.y0 + cr.y1) / 2
                if x0 < ccx < x1 and r.y0 < ccy < r.y1:
                    val = '1' if c['fill'] == (0.0, 0.0, 0.0) else '0'
            for w in words:
                wx, wy = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
                if x0 < wx < x1 and r.y0 < wy < r.y1 and w[4] in ('0', '1'):
                    val = w[4]
            cells.append(val)
        widths = [cm(x1 - x0) for x0, x1 in zip(edges, edges[1:])]
        # icon immediately left of the arrow
        icon = None
        for d in drawings:
            if d['type'] != 's' or d is a:
                continue
            dr = d['rect']
            if (0.3 * PT_PER_CM < dr.width < 1.2 * PT_PER_CM and dr.height > 0.3 * PT_PER_CM
                    and 0 < ar.x0 - dr.x1 < 0.3 * PT_PER_CM and dr.y0 - 2 < cy < dr.y1 + 2):
                icon = classify_icon(d)
        strips.append({
            'x_cm': cm(r.x0), 'y_cm': cm(r.y0), 'cells': len(cells), 'contents': ''.join(cells),
            'cell_w_cm': sorted(set(widths)), 'cell_h_cm': cm(r.height), 'icon': icon,
        })
    strips.sort(key=lambda s: (round(s['y_cm']), s['x_cm']))
    # stand-alone icons: small stroked shapes not attached to an arrow
    icons = []
    for d in drawings:
        if d['type'] != 's' or d['color'] != (0.0, 0.0, 0.0):
            continue
        dr = d['rect']
        if dr.width > 1.2 * PT_PER_CM or dr.height > 1.2 * PT_PER_CM or dr.width < 0.3 * PT_PER_CM:
            continue
        attached = any(0 < a['rect'].x0 - dr.x1 < 0.3 * PT_PER_CM and dr.y0 - 2 < (a['rect'].y0 + a['rect'].y1) / 2 < dr.y1 + 2 for a in arrows)
        if not attached:
            icons.append({'icon': classify_icon(d), 'x_cm': cm(dr.x0), 'y_cm': cm(dr.y0),
                          'w_cm': cm(dr.width), 'h_cm': cm(dr.height)})
    icons.sort(key=lambda s: (round(s['y_cm']), s['x_cm']))
    text = page.get_text().strip().splitlines()
    problem = next((t for t in text if t.startswith('Problem')), None)
    return {'problem_line': problem, 'strips': strips, 'standalone_icons': icons}


def main():
    out = {}
    for band in BANDS:
        doc = pymupdf.open(WEEK / f'week-18-{band}.pdf')
        out[band] = []
        for pno, page in enumerate(doc, start=1):
            pd = page_data(page)
            pd['page'] = pno
            pd['size_in'] = (round(page.rect.width / 72, 2), round(page.rect.height / 72, 2))
            out[band].append(pd)
    (HERE / 'pdf_strips.json').write_text(json.dumps(out, indent=1))
    for band, pages in out.items():
        print(f'== {band}')
        for p in pages:
            print(f"  page {p['page']} {p['size_in']}: {p['problem_line']}")
            for s in p['strips']:
                print(f"    {str(s['icon']):8s} {s['contents']:8s} cells={s['cells']} w={s['cell_w_cm']} h={s['cell_h_cm']} at ({s['x_cm']},{s['y_cm']})")
            for ic in p['standalone_icons']:
                print(f"    standalone {ic['icon']} {ic['w_cm']}x{ic['h_cm']} at ({ic['x_cm']},{ic['y_cm']})")


if __name__ == '__main__':
    main()
