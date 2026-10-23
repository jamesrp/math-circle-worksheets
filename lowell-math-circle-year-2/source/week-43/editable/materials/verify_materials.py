#!/usr/bin/env python3
"""Measure the Week 43 kit PDF and check it against what the problems use.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: materials.pdf in the package root). Needs PyMuPDF. Sizes are read
back from the PDF's vector drawings in points and converted to millimetres;
letters and numerals are read back as text. The K-1 Problem 1 mat is measured
in the K-1 reference PDF, so the strip's slots and the cards are checked
against the page the children use.
"""
from pathlib import Path
import sys

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05
CARD = (43.18, 55.88)


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def boxes(page, w, h, kinds=None):
    out = []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        if d['type'] == 's' and close(r[2] - r[0], w, 0.1) and close(r[3] - r[1], h, 0.1):
            if kinds is None or [it[0] for it in d['items']] == kinds:
                out.append(r)
    return out


def inside(words, r):
    return [w[4] for w in words if r[0] < (w[0] + w[2]) / 2 * MM < r[2] and r[1] < (w[1] + w[3]) / 2 * MM < r[3]]


def main(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    words = page.get_text('words')
    scale = [d for d in page.get_drawings() if d['type'] == 's' and [it[0] for it in d['items']] == ['l']
             and close(d['rect'].y0, d['rect'].y1, 0.01) and close((d['rect'].x1 - d['rect'].x0) * MM, 100.0)]
    assert len(scale) == 1
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')

    cards = boxes(page, *CARD, kinds=['l'] * 4)
    letters = sorted(''.join(inside(words, r)) for r in cards)
    assert letters == list('ABCDE'), letters
    pictures = [d for d in page.get_drawings() if d['type'] == 'fs']
    assert len(pictures) == 5
    for r in cards:
        pics = [d for d in pictures if r[0] < d['rect'].x0 * MM and d['rect'].x1 * MM < r[2]
                and r[1] < d['rect'].y0 * MM and d['rect'].y1 * MM < r[3]]
        assert len(pics) == 1, r
    shapes = {''.join(inside(words, r)): [it[0] for it in next(
        d for d in pictures if r[0] < d['rect'].x0 * MM < r[2] and r[1] < d['rect'].y0 * MM < r[3])['items']]
        for r in cards}
    assert shapes == {'A': ['l'] * 4, 'B': ['c'] * 4, 'C': ['l'] * 3, 'D': ['l'] * 4, 'E': ['l'] * 5}, shapes
    print(f'PASS cards: five cards {CARD[0]:.2f} x {CARD[1]:.2f} mm (1.7 x 2.2 in), A square, B circle, '
          'C triangle, D diamond, E pentagon, each with its letter.')

    tickets = boxes(page, 20.0, 20.0, kinds=['l'] * 4)
    nums = sorted(''.join(inside(words, r)) for r in tickets)
    assert nums == ['1', '2', '2', '3', '3', '4', '5'], nums
    print('PASS tickets: seven 20.00 mm tickets, 1 to 5 and a second 2 and 3.')

    strip = boxes(page, 141.0, 61.0)
    assert len(strip) == 1
    s = strip[0]
    dividers = sorted(d['rect'].x0 * MM for d in page.get_drawings() if d['type'] == 's'
                      and [it[0] for it in d['items']] == ['l'] and close(d['rect'].x0, d['rect'].x1, 0.01)
                      and close((d['rect'].y1 - d['rect'].y0) * MM, 61.0))
    assert len(dividers) == 2 and close(dividers[0] - s[0], 47.0) and close(dividers[1] - s[0], 94.0), dividers
    labels = [''.join(inside(words, [s[0] + i * 47, s[1], s[0] + i * 47 + 10, s[1] + 10])) for i in range(3)]
    assert labels == ['1', '2', '3'], labels
    print('PASS strip: one strip of three 47.00 x 61.00 mm slots numbered 1, 2, 3.')

    k1 = pymupdf.open(ROOT / 'reference-pdfs' / 'k-1.pdf')[0]
    mat = [[v * MM for v in d['rect']] for d in k1.get_drawings()
           if close((d['rect'].x1 - d['rect'].x0) * MM, 47.0, 0.1) and close((d['rect'].y1 - d['rect'].y0) * MM, 61.0, 0.1)]
    assert len(mat) == 3, len(mat)
    margin = min(47.0 - CARD[0], 61.0 - CARD[1]) / 2
    assert margin >= 1.5
    print(f'PASS fit: the K-1 Problem 1 mat has three 47 x 61 mm slots, the same as the strip; a card leaves at '
          f'least {margin:.1f} mm on each side of a slot.')

    # Each problem's needs, against one sheet (plus a second sheet per adult table for the second A B C set).
    needs = {'K-1 P1-P5, Grades 2-3 P1-P6, Grades 4-5 P1-P5: cards A, B, C': set('ABC') <= set(letters),
             'two-swap rule: tickets 1, 2, 3, then 2, 3 again from the same set': {'1', '2', '3'} <= set(nums),
             'all-slots rule: tickets 1, 2, 3, replaced after each draw': {'1', '2', '3'} <= set(nums),
             'K-1 P4: a first set 1, 2, 3 less one ticket, beside a whole second set 2, 3': nums.count('2') >= 2 and nums.count('3') >= 2,
             'Grades 4-5 P6: cards A-D and tickets 1-4': set('ABCD') <= set(letters) and '4' in nums,
             'Grades 4-5 P7: cards A-E and tickets 1-5': set('ABCDE') <= set(letters) and '5' in nums}
    assert all(needs.values()), needs
    print('PASS needs: ' + '; '.join(needs) + '. A second A B C set for K-1 P5 comes from the per-table sheet.')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'materials.pdf')
