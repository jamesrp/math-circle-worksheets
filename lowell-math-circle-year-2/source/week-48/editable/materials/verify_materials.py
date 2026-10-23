#!/usr/bin/env python3
"""Measure the Week 48 tile sheet and check it against the boards and the problems.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: materials.pdf beside build.py). Needs PyMuPDF. Tile sizes are read
back from the sheet's vector drawings in points and converted to millimetres.
The student boards' cell sizes are read back the same way from the built
packets (k-1.pdf, grades-2-3.pdf, grades-4-5.pdf beside build.py), and the
tile counts each problem needs come from src/check.py's exact cell counts.
"""
from collections import Counter
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'src'))
MM = 25.4 / 72
TOL = 0.05


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def measure(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    tiles, scale = Counter(), []
    for d in doc[0].get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if kinds in (['l'] * 4, ['re']) and close(r[2] - r[0], r[3] - r[1]):
            tiles[round(r[2] - r[0], 2)] += 1
        elif kinds == ['l'] and close(r[1], r[3]) and close(r[2] - r[0], 100.0):
            scale.append(r)
    assert len(scale) == 1, scale
    assert tiles == Counter({30.0: 16, 15.0: 48}), tiles
    print('PASS sheet: one US Letter page with a 100.00 mm scale line, 16 squares of 30.00 mm and 48 of 15.00 mm.')
    return tiles


def board_cells(pdf, page):
    """Cell sizes of the boards on one student page: gaps between parallel 120 mm grid lines."""
    xs = set()
    for d in pymupdf.open(pdf)[page - 1].get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                a, b = it[1], it[2]
                if close(a.x, b.x) and close(abs(a.y - b.y) * MM, 120.0):
                    xs.add(round(a.x * MM, 2))
    xs = sorted(xs)
    return {round(b - a, 2) for a, b in zip(xs, xs[1:])}


def check_boards():
    # (packet, page, cell size in mm): page 1's triangle, the trapezoid boards and the fine boards.
    for name, page, cell in (('k-1', 1, 30.0), ('k-1', 2, 30.0), ('grades-4-5', 5, 30.0),
                             ('k-1', 3, 15.0), ('grades-2-3', 5, 15.0)):
        got = board_cells(ROOT / f'{name}.pdf', page)
        assert got == {cell}, (name, page, got)
    print('PASS boards: the 4-by-4 boards (K-1 pp. 1-2, 4-5 p. 5) have 30.00 mm cells and the 8-by-8 boards '
          '(K-1 p. 3, 2-3 p. 5) have 15.00 mm cells, the tile sizes.')


def check_needs(tiles):
    import check  # noqa: F401  (runs the exact cell counts; its asserts must pass)
    cov = check.cells('trap', 4)
    cover_big = sum(v != 'O' for v in cov.values())
    tri_big = sum(v != 'O' for v in check.cells('triangle', 4).values())
    dia_big = sum(v != 'O' for v in check.cells('diamond', 4).values())
    assert (tri_big, dia_big, cover_big) == (10, 12, 16)
    assert max(tri_big, dia_big, cover_big) <= tiles[30.0]
    fine = {k: sum(v != 'O' for v in check.cells(k, 8).values()) for k in ('triangle', 'trap', 'diamond')}
    assert fine == {'triangle': 36, 'trap': 36, 'diamond': 40}, fine
    assert max(fine.values()) <= tiles[15.0]  # K-1 Problem 3 tiles the fine triangle cover: 36
    k1_small, older_small = 2 * 4, 3 * 4      # K-1: two big tiles split; grades 4-5: three
    assert max(k1_small, older_small) <= tiles[15.0]
    print('PASS problem needs: the coarse covers take 10 (triangle), 12 (diamond) and 16 (trapezoid) big tiles; '
          'the fine covers take 36 (triangle, K-1 Problem 3), 36 (trapezoid) and 40 (diamond) small tiles, '
          'at most the 48 on the sheet; K-1 splits two big tiles (8 small) and grades 4-5 three (12 small).')


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'materials.pdf'
    tiles = measure(pdf)
    check_boards()
    check_needs(tiles)


if __name__ == '__main__':
    main()
