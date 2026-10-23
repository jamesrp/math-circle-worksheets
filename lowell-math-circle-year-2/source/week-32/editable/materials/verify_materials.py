#!/usr/bin/env python3
"""Measure the Week 32 square sheet and check it against the K-1 boards.

Usage: python3 materials/verify_materials.py [materials.pdf] [k-1.pdf]
(defaults: materials.pdf and reference-pdfs/k-1.pdf beside this folder). Needs
PyMuPDF. Square sizes are read back from the sheet's vector drawings in points
and converted to millimetres, with each square's printed numeral; the K-1
boards are read back the same way from the K-1 packet. Each board's
biggest-square sequence is then rebuilt from one set's squares.
"""
from collections import Counter
from math import gcd
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05
UNIT = 10.0
SET = Counter({6: 1, 5: 1, 4: 2, 3: 6, 2: 2, 1: 3})


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def rects(page, filled):
    out = []
    for d in page.get_drawings():
        kinds = [it[0] for it in d['items']]
        if kinds not in (['l'] * 4, ['re']) or 's' not in d['type'] or ('f' in d['type']) != filled:
            continue
        if not filled and d['color'] != (0.0, 0.0, 0.0):
            continue
        out.append([v * MM for v in d['rect']])
    return out


def measure(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    W, H = page.rect.width * MM, page.rect.height * MM
    scale = [d for d in page.get_drawings() if d['type'] == 's' and [i[0] for i in d['items']] == ['l']
             and close(d['rect'][1], d['rect'][3]) and close((d['rect'][2] - d['rect'][0]) * MM, 100.0)]
    assert len(scale) == 1, len(scale)
    words = page.get_text('words')
    squares = []
    for r in rects(page, True):
        side = (r[2] - r[0]) / UNIT
        n = round(side)
        assert close(r[2] - r[0], n * UNIT) and close(r[3] - r[1], n * UNIT), r
        assert r[0] >= 6.35 and r[1] >= 6.35 and r[2] <= W - 6.35 and r[3] <= H - 6.35, ('inside printable area', r)
        label = [w[4] for w in words if r[0] < (w[0] + w[2]) / 2 * MM < r[2] and r[1] < (w[1] + w[3]) / 2 * MM < r[3]]
        assert label == [str(n)], (r, label)
        squares.append((n, r))
    for i, (_, p) in enumerate(squares):
        for _, q in squares[i + 1:]:
            assert (p[2] + 3 - TOL <= q[0] or q[2] + 3 - TOL <= p[0] or p[3] + 3 - TOL <= q[1]
                    or q[3] + 3 - TOL <= p[1]), ('3 mm apart', p, q)
    tops = sorted({round(r[1]) for n, r in squares if n == 6})
    assert len(tops) == 2
    sets = [Counter(n for n, r in squares if t - 1 <= r[1] < t + 95) for t in tops]
    assert sets == [SET, SET], sets
    assert len(squares) == 2 * sum(SET.values())
    print(f'PASS sheet: one US Letter page with one 100.00 mm scale line and two sets of {sum(SET.values())} '
          'squares, each exactly n x 10.00 mm with its side printed inside, at least 3 mm apart and inside a '
          '6.35 mm printer margin. Each set: one 6, one 5, two 4s, six 3s, two 2s and three 1s.')
    return SET


def boards(pdf):
    """The labelled K-1 boards, page by page, as (long, short) in units."""
    out = {}
    for i, page in enumerate(pymupdf.open(pdf), 1):
        for r in rects(page, False):
            w, h = (r[2] - r[0]) / UNIT, (r[3] - r[1]) / UNIT
            if w > 1.5 and h > 1.5 and close(w, round(w), .005) and close(h, round(h), .005):
                out.setdefault(i, []).append(tuple(sorted((round(w), round(h)), reverse=True)))
    return out


def rule(a, b):
    seq = []
    while b:
        seq += [b] * (a // b)
        a, b = b, a % b
    return seq


def main():
    sheet = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'materials.pdf'
    k1 = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / 'reference-pdfs' / 'k-1.pdf'
    kit = measure(sheet)
    b = boards(k1)
    rule_boards = b[1] + b[2] + b[3]   # the worked example's 0.7-scale strip is not a 1 cm board
    assert rule_boards == [(6, 4), (8, 4), (7, 4), (8, 5), (9, 6), (10, 6)], rule_boards
    for a, c in rule_boards:
        need = Counter(rule(a, c))
        assert all(need[n] <= kit[n] for n in need), ((a, c), need)
    p4 = b[4]
    assert p4 == [(6, 4), (9, 6)], p4
    for a, c in p4:
        g = gcd(a, c)
        assert all(kit[n] for n in range(1, min(c, 6) + 1)), (a, c)   # every size a child might test, up to the short side
        assert kit[g] and (g + 1 > 6 or kit[g + 1]), (a, c, g)
    assert kit[3] >= 6 and gcd(9, 6) == 3 and (9 // 3) * (6 // 3) == 6   # one set's six 3s tile 9 by 6 exactly
    assert kit[3] >= 4 and len(b[5]) == 4 and all(x == (3, 3) for x in b[5]), b[5]
    print('PASS boards: one set carries out the biggest-square rule on every K-1 Problem 1-3 board at once '
          '(6x4: 4,2,2; 8x4: 4,4; 7x4: 4,3,1,1,1; 8x5: 5,3,2,1,1; 9x6: 6,3,3; 10x6: 6,4,2,2); for Problem 4 it has '
          'every size up to each short side, so the answer (2 for 6x4, 3 for 9x6) and the next size up can be '
          'tried, and its six 3s tile 9x6; it has four 3-by-3 squares, matching Problem 5\'s four printed ones.')


if __name__ == '__main__':
    main()
