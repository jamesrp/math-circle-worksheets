"""Read the vector drawings and words of the three Week 4 student PDFs (PyMuPDF).

Writes pdf_geometry.json: for every page, the circles (centre, x- and y-radius, fill, stroke),
straight segments (with width and grey level), and words with their boxes. Coordinates are PDF
points with y downwards, as PyMuPDF reports them."""
import json
import os
import sys

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFDIR, PACKETS


def grey(c):
    return None if c is None else round(sum(c) / 3, 3)


def page_geometry(page):
    circles, segs, polys = [], [], []
    for d in page.get_drawings():
        items = d['items']
        kinds = [it[0] for it in items]
        r = d['rect']
        if kinds == ['c'] * 4:
            circles.append(dict(cx=round((r.x0 + r.x1) / 2, 3), cy=round((r.y0 + r.y1) / 2, 3),
                                rx=round((r.x1 - r.x0) / 2, 3), ry=round((r.y1 - r.y0) / 2, 3),
                                fill=grey(d.get('fill')), stroke=grey(d.get('color')),
                                width=round(d.get('width') or 0, 3)))
            continue
        if set(kinds) == {'l'}:
            pts = [(round(items[0][1].x, 3), round(items[0][1].y, 3))]
            for it in items:
                pts.append((round(it[2].x, 3), round(it[2].y, 3)))
            closed = d.get('closePath', False) or pts[0] == pts[-1]
            polys.append(dict(pts=pts, closed=bool(closed), stroke=grey(d.get('color')), fill=grey(d.get('fill')),
                              width=round(d.get('width') or 0, 3)))
            for it in items:
                segs.append(dict(a=(round(it[1].x, 3), round(it[1].y, 3)), b=(round(it[2].x, 3), round(it[2].y, 3)),
                                 stroke=grey(d.get('color')), width=round(d.get('width') or 0, 3)))
            if d.get('closePath') and pts[0] != pts[-1]:
                segs.append(dict(a=pts[-1], b=pts[0], stroke=grey(d.get('color')), width=round(d.get('width') or 0, 3)))
    words = [dict(t=w[4], x0=round(w[0], 2), y0=round(w[1], 2), x1=round(w[2], 2), y1=round(w[3], 2))
             for w in page.get_text('words')]
    return dict(circles=circles, segs=segs, polys=polys, words=words,
                size=(round(page.rect.width, 2), round(page.rect.height, 2)))


def main():
    out = {}
    for key, fn in PACKETS.items():
        if key == 'FAC':
            continue
        doc = pymupdf.open(os.path.join(PDFDIR, fn))
        out[key] = [page_geometry(p) for p in doc]
        print(key, fn, len(doc), 'pages:',
              [(len(g['circles']), len(g['segs'])) for g in out[key]])
    with open(os.path.join(HERE, 'pdf_geometry.json'), 'w') as fh:
        json.dump(out, fh)


if __name__ == '__main__':
    main()
