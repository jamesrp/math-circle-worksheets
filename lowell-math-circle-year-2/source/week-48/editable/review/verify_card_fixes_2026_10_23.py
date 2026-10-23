#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the Week 48 PDFs.

Usage: python3 review/verify_card_fixes_2026_10_23.py [folder]
(default: reference-pdfs/). Needs PyMuPDF. Reads k-1.pdf, grades-2-3.pdf,
grades-4-5.pdf and facilitator-guide.pdf from the folder: problem numbers and
wording in every band, the removed sentences, the two 85 mm boards, the 2-3
trapezoid page, the outside sample's gray neighbour and the guide's changed keys.
The mathematics behind the keys is checked by src/check.py; the tile sheet by
materials/verify_materials.py. Run on the earlier PDFs, it fails at the first check.
"""
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72


def words(page):
    return ' '.join(page.get_text().split())


def h_lines(page, length):
    """Left ends (x, y) in mm of horizontal lines of the given length."""
    out = set()
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                a, b = it[1], it[2]
                if abs(a.y - b.y) < .01 and abs(abs(a.x - b.x) * MM - length) < .05:
                    out.add((round(min(a.x, b.x) * MM, 2), round(a.y * MM, 2)))
    return out


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
    doc = {n: pymupdf.open(folder / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5')}
    text = {n: [words(p) for p in d] for n, d in doc.items()}
    flat = {n: ' '.join(t) for n, t in text.items()}

    for n, last in (('k-1', 6), ('grades-2-3', 7), ('grades-4-5', 7)):
        assert [int(k) for k in re.findall(r'Problem (\d+):', flat[n])] == list(range(1, last + 1)), n
        assert 'Whole squares are all gray. A cover uses every square with some gray in it. A touch at an edge or ' \
               'corner adds no square.' in text[n][0], n
        p1 = re.sub(r'grid- square', 'grid-square', text[n][0])
        assert 'Problem 1: Mark all the whole squares inside the triangle. Cover the triangle with as few ' \
               'grid-square tiles as you can.' in p1, n
        for gone in ('Cover all squares with some gray area', 'inside cover and an outside cover', 'outside-cover',
                     'One grid square is 1 big-square unit', 'one at a time', 'not to scale', 'second copy'):
            assert gone not in flat[n], (n, gone)
    print('PASS wording, all bands: problems numbered 1-6 (K-1) and 1-7 (older); the new shared rules; every '
          'Problem 1 as K-1\'s; no "inside cover"/"outside cover", unit line, "one at a time" or thumbnail caption.')

    assert 'Problem 3: Do Problem 1 again with small squares.' in text['k-1'][2]
    assert 'Could any shape with exactly 4 whole and 4 partly gray squares have area less than 4 big squares? ' \
           'More than 8?' in text['grades-2-3'][5]
    t = text['grades-2-3'][4]
    assert "Problem 5: Trap this shape’s area with big squares and then with small squares." in t
    assert t.count('Big squares:') == 1 and t.count('Small squares:') == 1
    assert 'Problem 7: Find the exact area of the gray shape in Problem 5.' in text['grades-4-5'][5]
    assert "Could the cover’s area go up?" in text['grades-4-5'][5]
    print('PASS problems: K-1 P3 refers to P1; 2-3 P5 is the trapezoid on both grids with two answer rows; 2-3 P7 '
          'asks about any shape; 4-5 P7 asks for the trapezoid\'s exact area; 4-5 P6 says "cover".')

    # Two 85 mm boards side by side (K-1 p. 5, 2-3 p. 6), each with five 85 mm horizontal lines.
    for n, page in (('k-1', 4), ('grades-2-3', 5)):
        lefts = h_lines(doc[n][page], 85.0)
        xs = sorted({x for x, _ in lefts})
        assert len(xs) == 2, (n, xs)
        for x in xs:
            ys = sorted(y for xx, y in lefts if xx == x)
            assert len(ys) == 5 and all(abs((b - a) - 21.25) < .05 for a, b in zip(ys, ys[1:])), (n, x, ys)
        assert xs[1] - xs[0] > 85, (n, xs)
    print('PASS boards: K-1 p. 5 and 2-3 p. 6 each carry two separate 85 mm 4-by-4 boards side by side.')

    # The 2-3 trapezoid page: an 8-by-8 board of 120 mm with 15 mm cells.
    ys = sorted(y for _, y in h_lines(doc['grades-2-3'][4], 120.0))
    assert len(ys) == 9 and all(abs((b - a) - 15) < .05 for a, b in zip(ys, ys[1:])), ys
    # 4-5 p. 6 has no small thumbnail boards any more (23 mm grids).
    assert not h_lines(doc['grades-4-5'][5], 23.0)
    print('PASS figures: the 2-3 trapezoid board is 8 by 8 at 15 mm; 4-5 p. 6 has no thumbnails.')

    # Page 1: a gray strip touching the outside sample's left edge, in every band.
    for n, d in doc.items():
        fills = [dr['rect'] for dr in d[0].get_drawings() if dr.get('fill') and dr['type'] == 'f']
        strips = [r for r in fills if abs((r.x1 - r.x0) * MM - 10) < .05 and abs((r.y1 - r.y0) * MM - 24) < .05]
        assert len(strips) == 1, (n, len(strips))
    print('PASS samples: page 1 shows gray beside the outside cell, touching only its edge, in every band.')

    g = pymupdf.open(folder / 'facilitator-guide.pdf')
    gt = ' '.join(words(p) for p in g)
    for need in ('strictly between w and w + p', 'week-48-materials.pdf', '16 big 30 mm and 48 small 15 mm',
                 'Up to eight could change this way, one in each partial big cell.',
                 'bounds 6 and 9 big units', 'The gap falls from 12 to 3', 'at most 2.5 mm wide',
                 '15/2 = 7.5 big-square units', 'Grades 2-3 Problem 6.', 'Grades 2-3 Problem 7.',
                 '0-5 running around; 5-9 launch', 'Grades 2-3 can test on the trapezoid'):
        assert need in gt, need
    for gone in ('stand and sort', 'not to scale', 'Exactly four previously outside small cells can become',
                 'at least 8 paper 15 mm squares', '8 big-square units'):
        assert gone not in gt, gone
    print('PASS guide: the markings interval and the split limit in the overview, the tile sheet, K-1 Problem 4\'s '
          'four of up to eight, the 2-3 trapezoid key, the slivers, 4-5 Problem 7 at 15/2, renumbered 2-3 keys and '
          'the first-visit hour after the run.')


if __name__ == '__main__':
    main()
