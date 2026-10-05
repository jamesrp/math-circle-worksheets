"""K-1 picture rings (Problems 8-10): read every icon from the vector drawing and check the answers.

Each icon is recognised from its strokes (sun: circle + 8 rays; fish: ellipse + eye + tail;
tree: closed triangle + open trunk; house: closed roof + two open polylines; heart: closed curve
symmetric left-right; moon: closed curve that is not). Then the ring order, the rows of
Problems 8-10 and the guide's answers are checked by stepping round the ring."""
import math
import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PDFDIR

BAD = []


def bad(m):
    BAD.append(m)
    print('  !!', m)


def drawings(page):
    out = []
    for d in page.get_drawings():
        items = d['items']
        kinds = ''.join(it[0] for it in items)
        r = d['rect']
        pts = []
        if set(kinds) == {'l'}:
            pts = [(items[0][1].x, items[0][1].y)] + [(it[2].x, it[2].y) for it in items]
        out.append(dict(kinds=kinds, rect=(r.x0, r.y0, r.x1, r.y1), pts=pts, fill=d.get('fill'),
                        stroke=d.get('color'), closed=bool(pts) and math.dist(pts[0], pts[-1]) < 0.05))
    return out


def inside(r, box, pad=0.5):
    return r[0] >= box[0] - pad and r[1] >= box[1] - pad and r[2] <= box[2] + pad and r[3] <= box[3] + pad


def classify(ds):
    circles = [d for d in ds if d['kinds'] == 'cccc']
    round_c = [d for d in circles if abs((d['rect'][2] - d['rect'][0]) - (d['rect'][3] - d['rect'][1])) < 0.05]
    ellipses = [d for d in circles if d not in round_c]
    rays = [d for d in ds if d['kinds'] == 'l']
    polys = [d for d in ds if d['pts'] and len(d['pts']) >= 4]
    closed_small = [d for d in polys if d['closed'] and len(d['pts']) <= 5]
    open_small = [d for d in polys if not d['closed'] and len(d['pts']) <= 5]
    curves = [d for d in polys if d['closed'] and len(d['pts']) > 20]
    if round_c and len(rays) == 8:
        return 'sun'
    if ellipses:
        return 'fish'
    if len(closed_small) == 1 and len(open_small) == 1:
        return 'tree'
    if len(closed_small) == 1 and len(open_small) == 2:
        return 'house'
    if len(curves) == 1:
        p = curves[0]['pts']
        x0, x1 = curves[0]['rect'][0], curves[0]['rect'][2]
        mid = (x0 + x1) / 2
        # mirror every point in the vertical line through the middle; a heart maps onto itself
        err = max(min(math.dist((2 * mid - x, y), q) for q in p) for x, y in p)
        return 'heart' if err < 1.0 else 'moon'
    return '?'


def containers(ds, size_range):
    """Boxes (closed 4-segment squares) and picture circles (filled white circles)."""
    boxes, circ = [], []
    for d in ds:
        w, h = d['rect'][2] - d['rect'][0], d['rect'][3] - d['rect'][1]
        if d['kinds'] == 'llll' and d['closed'] and abs(w - h) < 0.1 and size_range[0] < w < size_range[1] \
                and d['fill'] is None:
            boxes.append(d)
        if d['kinds'] == 'cccc' and d['fill'] == (1.0, 1.0, 1.0) and abs(w - h) < 0.05 and w > 50:
            circ.append(d)
    return boxes, circ


def content(ds, c):
    return classify([d for d in ds if d is not c and inside(d['rect'], c['rect'])
                     and (d['rect'][2] - d['rect'][0]) < (c['rect'][2] - c['rect'][0]) - 1])


def ring_order(ds, circ):
    cx = sum((c['rect'][0] + c['rect'][2]) / 2 for c in circ) / len(circ)
    cy = sum((c['rect'][1] + c['rect'][3]) / 2 for c in circ) / len(circ)
    items = []
    for c in circ:
        x, y = (c['rect'][0] + c['rect'][2]) / 2, (c['rect'][1] + c['rect'][3]) / 2
        a = math.degrees(math.atan2(cy - y, x - cx))
        items.append((round(90 - a, 3) % 360, math.hypot(x - cx, y - cy), content(ds, c)))
    items.sort()
    angs = [t[0] for t in items]
    gaps = [(angs[(i + 1) % 6] - angs[i]) % 360 for i in range(6)]
    radii = [t[1] for t in items]
    print(f'   ring: {len(items)} pictures, gap spread {max(gaps) - min(gaps):.4f} deg, radius spread '
          f'{max(radii) - min(radii):.3f}pt, first at {angs[0]:.3f} deg from the top')
    return [t[2] for t in items]


def boxes_grid(ds, boxes):
    rows = {}
    for b in boxes:
        y = round((b['rect'][1] + b['rect'][3]) / 2 / 5) * 5
        rows.setdefault(y, []).append(b)
    out = []
    for y in sorted(rows):
        bs = sorted(rows[y], key=lambda b: b['rect'][0])
        out.append([content(ds, b) if any(inside(d['rect'], b['rect']) and d is not b for d in ds) else None
                    for b in bs])
    return out


def step(ring, name, k):
    return ring[(ring.index(name) + k) % 6]


def main():
    doc = pymupdf.open(os.path.join(PDFDIR, 'week-04-k-1.pdf'))
    rings = {}
    for pno in (8, 9, 10):
        ds = drawings(doc[pno - 1])
        bx, circ = containers(ds, (40, 70))
        print(f'K1 p{pno}:')
        rings[pno] = ring_order(ds, circ)
        print('   ring clockwise from the top:', rings[pno])
        grid = boxes_grid(ds, bx)
        print('   boxes, row by row:', grid)
        rings[pno, 'grid'] = grid
    ring = rings[8]
    if not (rings[9] == ring and rings[10] == ring):
        bad('picture rings differ between pages')
    guide_ring = ['sun', 'moon', 'heart', 'tree', 'fish', 'house']
    print('guide ring order agrees:', ring == guide_ring)
    if ring != guide_ring:
        bad('ring order')

    # Problem 8: hop 2 row by row
    top = rings[8, 'grid'][0]
    rows = [top]
    while True:
        rows.append([step(ring, x, 2) for x in rows[-1]])
        if rows[-1] == top:
            break
    blank_rows = len(rings[8, 'grid']) - 1
    print(f'P8 top row {top}; rows until the top row returns: {rows[1:]}; '
          f'{len(rows) - 1} rows needed, {blank_rows} blank rows printed')
    guide8 = [['heart', 'house', 'sun'], ['fish', 'moon', 'heart'], ['sun', 'tree', 'fish']]
    print('P8 guide agrees:', rows[1:] == guide8, '; guide says the last two rows stay empty:', blank_rows - 3 == 2)

    # Problem 9: rows of three boxes: start, after hop k, and start again
    rows9 = [r for r in rings[9, 'grid'] if len(r) == 3]
    print('P9 rows (left, middle, right):', rows9)
    words = doc[8].get_text('words')
    ks = [int(w[4]) for w in sorted(words, key=lambda w: w[1]) if w[4].isdigit() and 300 < w[1] < 700 and w[0] < 300]
    print('P9 printed hops:', ks)
    back = []
    for (a, b, c), k in zip(rows9, ks):
        if step(ring, a, k) != b or a != c:
            bad(f'P9 row {a} hop {k} -> {b} -> {c} inconsistent')
        back.append([h for h in range(1, 6) if step(ring, b, h) == c])
    print('P9 hops 1-5 that change the middle picture back:', back, '(guide: 5, 4, 3, 2)')
    if back != [[5], [4], [3], [2]]:
        bad('P9 answers')

    # Problem 10: secret hop
    g = rings[10, 'grid']
    print('P10 rows:', g)
    ex = [r for r in g if r[0] == 'sun'][0]
    secret = [h for h in range(1, 6) if step(ring, 'sun', h) == ex[1]]
    pairs = [(r[0], step(ring, r[0], secret[0])) for r in g if r[0] != 'sun'] + \
            [(r[2], step(ring, r[2], secret[0])) for r in g if len(r) == 4]
    print('P10 secret hop(s) from sun -> tree:', secret, '; answers:', pairs)
    if secret != [3]:
        bad('P10 secret')


if __name__ == '__main__':
    main()
    print('SUMMARY:', 'all checks agree' if not BAD else BAD)
