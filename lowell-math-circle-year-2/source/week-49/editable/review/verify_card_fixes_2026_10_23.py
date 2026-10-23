#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the Week 49 PDFs.

Usage: python3 review/verify_card_fixes_2026_10_23.py [folder]
(default: reference-pdfs/). Needs PyMuPDF. Reads k-1.pdf, grades-2-3.pdf,
grades-4-5.pdf and facilitator-guide.pdf from the folder: the theme name, the
moved and deleted sentences, the printed ring values (read from their page
positions), the mat sizes and gaps, the record rows and the guide's changed keys.
The mathematics behind the keys is checked by src/check.py. Run on the earlier
PDFs, it fails at the first check.
"""
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
OX, OY = 14, 18          # the canvas origin on the page, in mm (left and top margins)


def words(page):
    return ' '.join(page.get_text().split())


def at(page, x, y, tol=2.5):
    """The words centred within tol mm of canvas point (x, y)."""
    out = []
    for w in page.get_text('words'):
        cx, cy = (w[0] + w[2]) / 2 * MM - OX, (w[1] + w[3]) / 2 * MM - OY
        if abs(cx - x) < tol and abs(cy - y) < tol:
            out.append(w[4])
    return out


def ring_values(page, x, y, span):
    return [''.join(at(page, a, b)) for a, b in ((x, y), (x+span, y), (x+span, y+span), (x, y+span))]


def squares(page, side):
    """Canvas boxes (x0, y0, x1, y1) of drawn squares with the given side in mm."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        w, h = r.width * MM, r.height * MM
        if abs(w - side) < .05 and abs(h - side) < .05:
            out.append((round(r.x0 * MM - OX, 2), round(r.y0 * MM - OY, 2), round(r.x1 * MM - OX, 2), round(r.y1 * MM - OY, 2)))
    return sorted(set(out))


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
    doc = {n: pymupdf.open(folder / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5')}
    for n, d in doc.items():
        assert all(words(p).startswith('Week 49 / Four towers and differences /') for p in d), n
        flat = ' '.join(words(p) for p in d)
        assert 'Four-tower' not in flat, n
        assert 'Make every new tower before changing any old tower. An all- zero start takes 0 moves.' in words(d[0]) \
            or 'Make every new tower before changing any old tower. An all-zero start takes 0 moves.' in words(d[0]), n
        for gone in ('All four gaps use the old ring', 'Use these big mats', 'count as different here'):
            assert gone not in flat, (n, gone)
    print('PASS names and rules: every page is headed "Four towers and differences"; the all-zero sentence is in the '
          'page-1 rules; the caption repeat, the page-2 mat sentence and the 2-3 counting sentence are gone.')

    assert ring_values(doc['k-1'][4], 23, 53, 42) == ['0', '2', '1', '4']
    assert ring_values(doc['k-1'][4], 123, 53, 42) == ['0', '1', '4', '2']
    assert ring_values(doc['grades-2-3'][4], 25, 48, 42) == ['0', '2', '1', '4']
    assert ring_values(doc['grades-2-3'][4], 123, 48, 42) == ['0', '1', '4', '2']
    assert ring_values(doc['grades-2-3'][4], 25, 181, 42) == ['', '', '', '']
    assert ring_values(doc['grades-2-3'][4], 123, 181, 42) == ['', '', '', '']
    assert ring_values(doc['grades-4-5'][5], 25, 43, 38) == ['2', '5', '1', '0']
    assert ring_values(doc['grades-4-5'][5], 123, 43, 38) == ['4', '10', '2', '0']
    print('PASS rings: K-1 P6 and 2-3 P5 print (0,2,1,4) and (0,1,4,2); 2-3 P6 has two blank rings; 4-5 P6 prints '
          '(2,5,1,0) and (4,10,2,0).')

    for n, d in doc.items():
        for page, count in ((1, 8), (3, 6)):
            sq = squares(d[page], 36.0)
            assert len(sq) == count, (n, page, sq)
            old = [s for s in sq if s[0] < 92.5]
            new = [s for s in sq if s[0] > 92.5]
            assert len(old) == len(new) == count // 2
            assert abs(min(s[0] for s in new) - max(s[2] for s in old) - 9) < .05, (n, page)
            assert not squares(d[page], 40.0)
    print('PASS mats: pages 2 and 4 of every band have 36 mm stations, four (or three) per mat, with a 9 mm gap '
          'between the old and new mats.')

    for n, d in doc.items():
        t = d[3].get_text('words')
        rows = sorted({w[4] for w in t if w[4] in '123456' and abs((w[0] + w[2]) / 2 * MM - OX - 24) < 2})
        rows += sorted({w[4] for w in t if w[4] in '123456' and abs((w[0] + w[2]) / 2 * MM - OX - 114) < 2})
        assert rows == ['1', '2', '3', '4', '5', '6'], (n, rows)
        assert len(squares(d[3], 14.0)) == 0  # record boxes are 14 by 11, not squares
    for n in ('grades-2-3', 'grades-4-5'):
        labels = [w for w in doc[n][2].get_text('words') if w[4] == 'old'
                  and min(abs((w[0] + w[2]) / 2 * MM - OX - x) for x in (12, 104)) < 2]
        assert len(labels) == 4, n
    assert len(squares(doc['grades-4-5'][4], 9.0)) == 80
    print('PASS records: six numbered A-B-C rows on every three-station page, an old-ring row under each older P3 '
          'target, and 4-5 P5\'s four columns of five A-B-C-D rows (80 letter boxes).')

    g = pymupdf.open(folder / 'facilitator-guide.pdf')
    gt = ' '.join(words(p) for p in g)
    for need in ('Week 49 Four towers and differences', 'Per pair: 40 linking cubes', '36 mm square stations',
                 'clear the old mat and move each new tower to the same letter on it',
                 'Both printed orders last 4 moves: (0,2,1,4)', 'The page gives two blank rings',
                 '(2,5,1,0) → (3,4,1,2)', '(4,10,2,0) → (6,8,2,4)', 'Both runs take 6 moves', '0-5 running around',
                 'four columns of letter boxes'):
        assert need in gt, need
    for gone in ('optional cubes', 'number cards', 'gap cards', 'swap old/new roles', '40 mm', 'Four tower differences'):
        assert gone not in gt, gone
    print('PASS guide: the theme name, cubes per pair, 36 mm stations, the mat-clearing step, the printed orders\' key, '
          'the blank rings, the new 4-5 P6 runs, the hour after the run, and no cards or role swap.')


if __name__ == '__main__':
    main()
