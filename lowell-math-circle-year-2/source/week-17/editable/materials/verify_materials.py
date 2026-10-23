#!/usr/bin/env python3
"""Measure the Week 17 table kit and check it against what the student pages use.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf] [path/to/k-1.pdf]
(defaults: build/materials.pdf and reference-pdfs/k-1.pdf). Needs PyMuPDF.
Sizes are read back from the PDF's vector drawings in points and converted to
millimetres; card letters are read back as text. The printed state circles are
measured in the K-1 packet, so the markers are checked against the page the
children use. The cards and circles each problem needs are read from the
problem files (problem-files/problems in the ZIP, ../problems in the
repository).
"""
from pathlib import Path
import re
import sys

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05
RED, BLUE = (203 / 255, 45 / 255, 45 / 255), (34 / 255, 95 / 255, 176 / 255)


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def size(d):
    r = d['rect']
    return (r.x1 - r.x0) * MM, (r.y1 - r.y0) * MM


def kind(d):
    return tuple(it[0] for it in d['items'])


def within(d, box):
    r = d['rect']
    return box.x0 - .5 <= r.x0 and r.x1 <= box.x1 + .5 and box.y0 - .5 <= r.y0 and r.y1 <= box.y1 + .5


def squares(drawings, side):
    return [d for d in drawings if d['type'] == 's' and kind(d) == ('l',) * 4
            and all(close(v, side, 0.1) for v in size(d))]


def colour(c):
    return tuple(round(v, 3) for v in c) if c else None


def problems_dir():
    for p in (ROOT / 'problem-files' / 'problems', ROOT.parent / 'problems'):
        if p.is_dir():
            return p
    raise SystemExit('problem files not found')


def main(pdf, k1):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    dr = page.get_drawings()
    words = page.get_text('words')
    scale = [d for d in dr if d['type'] == 's' and kind(d) == ('l',) and close(size(d)[1], 0, 0.01)
             and close(size(d)[0], 100.0)]
    assert len(scale) == 1
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')

    cards = {'R': 0, 'B': 0}
    for box in squares(dr, 30.0):
        b = box['rect']
        glyphs = [d for d in dr if d['type'] == 'fs' and within(d, b) and all(close(v, 24.0, 0.1) for v in size(d))]
        letters = ''.join(w[4] for w in words if b.x0 < (w[0] + w[2]) / 2 < b.x1 and b.y0 < (w[1] + w[3]) / 2 < b.y1)
        assert len(glyphs) == 1 and letters in cards, (b, letters)
        g = glyphs[0]
        expect = (('l',) * 4, RED) if letters == 'R' else (('c',) * 4, BLUE)
        assert (kind(g), colour(g['color'])) == (expect[0], colour(expect[1])), (letters, kind(g), g['color'])
        cards[letters] += 1
    assert cards == {'R': 12, 'B': 12}, cards
    print('PASS cards: 12 R and 12 B cards, 30.00 mm squares; R is a red 24.00 mm square and B a blue '
          '24.00 mm circle, as on the student pages, each with its letter.')

    tiles = squares(dr, 34.0)
    assert len(tiles) == 12
    for t in tiles:
        inner = [d for d in dr if within(d, t['rect']) and d is not t]
        assert len(inner) == 1 and kind(inner[0]) == ('c',) * 4 and inner[0]['type'] == 's'
        assert all(close(v, 30.0, 0.1) for v in size(inner[0]))   # the path's diameter; the outline is centred on it
        assert not [w for w in words if t['rect'].contains(pymupdf.Rect(w[:4]))]
    state = 30.0
    print('PASS state circles: 12 blank 30.00 mm circles on 34.00 mm squares.')

    markers = squares(dr, 14.0)
    assert len(markers) == 4
    solid = ring = 0
    for m in markers:
        inner = [d for d in dr if within(d, m['rect']) and d is not m]
        assert len(inner) == 1 and kind(inner[0]) == ('c',) * 4
        d = inner[0]
        outer = size(d)[0] + (d['width'] * MM if d['type'] == 's' else 0)
        assert close(outer, 11.0, 0.05), outer
        solid += d['type'] == 'f'
        ring += d['type'] == 's'
    assert (solid, ring) == (2, 2)
    print('PASS markers: four 14.00 mm squares, two with a solid 11.00 mm disc and two with an 11.00 mm ring.')

    printed = sorted({round(size(d)[0], 2) for p in pymupdf.open(k1) for d in p.get_drawings()
                      if kind(d) == ('c',) * 4 and d['type'] == 's' and close(size(d)[0], size(d)[1], 0.05)
                      and size(d)[0] > 12})
    assert printed and min(printed) > 14.0 + 2, printed
    assert 2 * 14.0 < state
    print(f'PASS fit: the K-1 packet\'s printed circles are {", ".join(f"{v:.2f}" for v in printed)} mm across '
          f'(to the middle of the outline), so a 14 mm marker sits inside one; two markers side by side (28 mm) fit on a '
          f'30 mm state circle.')

    probs = problems_dir()
    text = ' '.join(p.read_text() for p in sorted(probs.glob('*.md')))
    lengths = {'four': 4, 'five': 5, 'six': 6}
    longest = max(lengths[w] for w in re.findall(r'\b(four|five|six)-card', text))
    groups = {'three': 3, 'threes': 3, 'fours': 4, 'fives': 5, 'six': 6}
    biggest = max(groups[w] for w in re.findall(r'groups? of (three|threes|fours|fives|six)\b', text)
                  + re.findall(r'grouped in (threes|fours|fives)\b', text)
                  + re.findall(r'do the same for groups of (six)\b', text))
    pairs = [(a, b) for a, b in re.findall(r"\('(\w*)','(\w*)',[\d.]+\)", text)]
    assert len(pairs) == 4 + 6 + 4, pairs
    ending = 2   # the guide's witness endings are at most one card; allow two after each row
    pair_r = max(a.count('R') + b.count('R') for a, b in pairs) + 2 * ending
    pair_b = max(a.count('B') + b.count('B') for a, b in pairs) + 2 * ending
    needs = {f'two {longest}-card rows side by side (any colours)': 2 * longest <= min(cards.values()),
             f'one pair of printed rows with the same ending of up to {ending} cards after each '
             f'({pair_r} R, {pair_b} B at most)': pair_r <= cards['R'] and pair_b <= cards['B'],
             f'two machines of the largest size the pages ask for ({biggest} circles each)': 2 * biggest <= 12,
             'two markers per pair, two pairs at a table': 2 * 2 <= 4}
    assert all(needs.values()), needs
    print('PASS needs: ' + '; '.join(needs) + '.')


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args[0] if args else ROOT / 'build' / 'materials.pdf',
         args[1] if len(args) > 1 else ROOT / 'reference-pdfs' / 'k-1.pdf')
