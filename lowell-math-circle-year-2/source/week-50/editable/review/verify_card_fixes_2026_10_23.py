#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes in the Week 50 PDFs.

Usage: python3 review/verify_card_fixes_2026_10_23.py [folder]
(default: reference-pdfs/). Needs PyMuPDF. Reads k-1.pdf, grades-2-3.pdf,
grades-4-5.pdf and facilitator-guide.pdf from the folder: the one 70 mm bar and
the relettered example on page 1, the new and deleted wording in every band, the
7.5 mm strip and the guide's changed text. The mathematics behind the keys is
checked by src/check.py. Run on the earlier PDFs, it fails at the first check.
"""
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
X0, Y0 = 14, 18          # the canvas origin on the page, in mm


def words(page):
    return ' '.join(page.get_text().split())


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
    doc = {n: pymupdf.open(folder / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5')}
    text = {n: [words(p) for p in d] for n, d in doc.items()}
    flat = {n: ' '.join(t) for n, t in text.items()}

    # Page 1, every band: one bar of four pieces in path order, 10 + 20 + 30 + 10 = 70 mm.
    for n, d in doc.items():
        t = text[n][0]
        assert 'A: 10 B: 20 C: 30 D: 10 A B C D the pieces in a row 70 mm' in t, (n, t)
        assert 'right pieces' not in t and 'up pieces' not in t, n
        bars = sorted((r.x0 * MM - X0, (r.x1 - r.x0) * MM) for r in
                      (dr['rect'] for dr in d[0].get_drawings() if dr['type'] in ('f', 'fs') and dr.get('fill')
                       and dr['fill'][0] > .5 and abs((dr['rect'].y1 - dr['rect'].y0) * MM - 7) < .05))
        assert [round(w, 2) for _, w in bars] == [10, 20, 30, 10], (n, bars)
        assert all(abs(a[0] + a[1] - b[0]) < .01 for a, b in zip(bars, bars[1:])), (n, bars)
        # B's label sits right of piece B (canvas x = 25, y 36..56), at canvas (31, 46).
        ws = d[0].get_text('words')
        b = next(w for w in ws if w[4] == 'B:')
        assert abs((b[0] + b[2]) / 2 * MM - X0 - 29.6) < 1.5 and abs((b[1] + b[3]) / 2 * MM - Y0 - 46.3) < .5, (n, b)
    print('PASS page 1, all bands: the example is lettered A-D in path order (B: 20 beside its piece) and its pieces '
          'make one bar of 10, 20, 30 and 10 mm, end to end, labelled 70 mm.')

    for n, last in (('k-1', 6), ('grades-2-3', 5), ('grades-4-5', 7)):
        assert [int(k) for k in re.findall(r'Problem (\d+):', flat[n])] == list(range(1, last + 1)), n
        for gone in ('shortcut', 'greatest vertical gap', 'clipped by the rectangle', 'It goes left once',
                     'A straight diagonal is 200 mm long', 'using the width and height',
                     'which distances can shrink'):
            assert gone not in flat[n], (n, gone)
    assert 'Problem 3: Make a staircase inside the gray strip. Compare its length with this one using string.' \
        in text['k-1'][2]
    for n in ('grades-2-3', 'grades-4-5'):
        assert 'Problem 2: Compare the lengths of these two staircases. Find the exact length of each staircase.' \
            in text[n][1]
        assert "Problem 3: Make a staircase inside the gray strip. Compare the two staircase lengths with the " \
               "diagonal’s length." in text[n][2]
        assert 'The gray strip reaches 15 mm vertically above and below the dotted diagonal.' in text[n][3]
    t = re.sub(r'differ- ent', 'different', text['grades-2-3'][4])
    assert 'Could a path with leftward pieces be shorter than 280 mm? Explain your answer.' in t
    t = text['grades-4-5']
    assert 'Problem 5: Make a staircase inside this narrower strip with as few turns as you can. Its pieces may ' \
           'follow the strip’s boundary. Is it shorter than your staircase in the wider strip? Explain your ' \
           'answer.' in t[4]  # boundary sentence added by the critic follow-up, later on October 23
    assert 'The strip reaches 7.5 mm vertically above and below the diagonal.' in t[4]
    assert "Problem 6: Find this path’s exact length. Explain which part" in t[5]
    assert 'as the 200 mm diagonal? Explain your answer.' in t[5]
    print('PASS wording: numbering unchanged; K-1 P3 and older P2-P4 reworded; 2-3 P5 asks about paths with '
          'leftward pieces; 4-5 P5 asks for fewest turns in the narrower strip, P6 no longer says it goes left, P7 '
          'ends "Explain your answer."; the deleted phrases are gone from every band.')

    # Grades 4-5 p. 5: the gray strip is 7.5 mm above and below the diagonal (10 mm along the edges at S and F).
    page = doc['grades-4-5'][4]
    strips = []
    for dr in page.get_drawings():
        if dr['type'] in ('f', 'fs') and dr.get('fill') and .8 < dr['fill'][0] < .95:
            pts = {(round(q.x * MM - X0 - 10, 2), round(q.y * MM - Y0 - 45, 2))
                   for it in dr['items'] if it[0] == 'l' for q in it[1:3]}
            strips.append(sorted(pts))
    assert strips == [[(0.0, 112.5), (0.0, 120.0), (10.0, 120.0), (150.0, 0.0), (160.0, 0.0), (160.0, 7.5)]], strips
    print('PASS strip: Grades 4-5 p. 5 shades |y - 3x/4| <= 7.5 mm, half of Problem 4\'s strip.')

    g = pymupdf.open(folder / 'facilitator-guide.pdf')
    assert len(g) == 4
    gt = ' '.join(words(p) for p in g)
    for need in ('Revised 23 October 2026', 'Fewest turns.', 'Without the boundary the answer is 9.',
                 '7.5 mm strip of Grades 4-5 Problem 5 it is 16 (17 if no piece may touch the boundary)', '30 cm pipe cleaner',
                 'piece by piece, A to D, and straighten it beside the 70 mm bar',
                 'First-visit hour. 0-5 running around; 5-9 launch; 9-48 Problems 1-3, then Problem 4 for any pair '
                 'that finishes; 48-55 share; 55-60 reset.',
                 'its lower corners lie outside the strip', 'The strip is 7.5 mm, half of Problem 4',
                 'The fewest turns is 16', '10+7×20=150', 'suggest collecting the right pieces and the up pieces',
                 'First visits in all bands: P1-3, then P4 for any pair that finishes'):
        assert need in gt, need
    for gone in ('horizontal strip', 'vertical strip', 'Flexible hour', 'imagined', 'as the opening diagram does',
                 '±8 mm', 'P1-2 for different staircases'):
        assert gone not in gt, gone
    print('PASS guide: the turn optimum in the overview, the pipe cleaner, the single-bar launch, one first-visit '
          'hour on pages 1 and 4, the Problem 3 key, and the 16-turn key with its bound for the 7.5 mm strip.')


if __name__ == '__main__':
    main()
