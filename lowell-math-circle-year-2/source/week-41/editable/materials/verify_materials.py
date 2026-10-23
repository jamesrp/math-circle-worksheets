#!/usr/bin/env python3
"""Measure the Week 41 table copies and check them against the student portal map.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: materials.pdf in the package root). Needs PyMuPDF. Sizes are read back from
the PDF's vector drawings in points and converted to millimetres; letters are read back
as text. The K-1 packet's Problem 2 page (the 180 mm portal map) is read from
reference-pdfs/k-1.pdf, so the copies' letter layout is checked against the map the
children use.
"""
from pathlib import Path
import sys

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
COPY = 90.0


def close(a, b, tol=0.05):
    return abs(a - b) <= tol


def letter_grid(words, x0, y0, side):
    """The 3-by-3 grid of single capital letters inside the square at (x0, y0), side mm."""
    grid = [['' for _ in range(3)] for _ in range(3)]
    c = side / 3
    for w in words:
        t = w[4]
        if len(t) != 1 or not t.isupper():
            continue
        cx, cy = (w[0] + w[2]) / 2 * MM, (w[1] + w[3]) / 2 * MM
        if x0 < cx < x0 + side and y0 < cy < y0 + side:
            col, row = int((cx - x0) // c), int((cy - y0) // c)
            grid[row][col] += t
    return grid


def squares(page, side):
    out = []
    for d in page.get_drawings():
        r = d['rect']
        w, h = (r.x1 - r.x0) * MM, (r.y1 - r.y0) * MM
        if d['type'] == 's' and close(w, side, 0.1) and close(h, side, 0.1) and [i[0] for i in d['items']] in (['re'], ['l'] * 4):
            out.append((r.x0 * MM, r.y0 * MM))
    return sorted(set((round(x, 2), round(y, 2)) for x, y in out))


def main(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    words = page.get_text('words')
    scale = [d for d in page.get_drawings() if d['type'] == 's' and [i[0] for i in d['items']] == ['l']
             and close(d['rect'].y0, d['rect'].y1, 0.01) and close((d['rect'].x1 - d['rect'].x0) * MM, 100.0)]
    assert len(scale) == 1
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')

    copies = squares(page, COPY)
    assert len(copies) == 4, copies
    xs, ys = sorted({x for x, _ in copies}), sorted({y for _, y in copies})
    assert len(xs) == len(ys) == 2 and close(xs[1] - xs[0], COPY, 0.1) and close(ys[1] - ys[0], COPY, 0.1)
    assert all(5 < x and x + COPY < 215.9 - 5 for x in xs) and all(y + COPY < 279.4 - 15 for y in ys)
    print(f'PASS copies: four {COPY:.2f} mm squares in a 2-by-2 block that touch edge to edge, inside the printable margins.')

    cells = {}
    for x, y in copies:
        vert = sorted(round(d['rect'].x0 * MM - x, 1) for d in page.get_drawings() if d['type'] == 's'
                      and [i[0] for i in d['items']] == ['l'] and close(d['rect'].x0, d['rect'].x1, 0.01)
                      and close(d['rect'].y0 * MM, y, 0.1) and close((d['rect'].y1 - d['rect'].y0) * MM, COPY, 0.1)
                      and x + 1 < d['rect'].x0 * MM < x + COPY - 1)
        horiz = sorted(round(d['rect'].y0 * MM - y, 1) for d in page.get_drawings() if d['type'] == 's'
                       and [i[0] for i in d['items']] == ['l'] and close(d['rect'].y0, d['rect'].y1, 0.01)
                       and close(d['rect'].x0 * MM, x, 0.1) and close((d['rect'].x1 - d['rect'].x0) * MM, COPY, 0.1)
                       and y + 1 < d['rect'].y0 * MM < y + COPY - 1)
        assert vert == [30.0, 60.0] and horiz == [30.0, 60.0], (x, y, vert, horiz)
        cells[(x, y)] = letter_grid(words, x, y, COPY)
    print('PASS cells: each copy has two inner lines each way, 30.00 mm apart: nine 30 mm cells.')

    k1 = pymupdf.open(ROOT / 'reference-pdfs' / 'k-1.pdf')[1]
    mats = squares(k1, 180.0)
    assert len(mats) == 1, mats
    mat = letter_grid(k1.get_text('words'), *mats[0], 180.0)
    assert mat == [['A', 'B', 'C'], ['D', 'H', 'E'], ['F', 'G', 'I']], mat
    assert all(g == mat for g in cells.values()), cells
    print('PASS letters: every copy reads A B C / D H E / F G I, as the 180 mm portal map on K-1 page 2 does.')
    print('Digital checks only: cutting, alignment on a table and pawn use are physically unrehearsed.')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'materials.pdf')
