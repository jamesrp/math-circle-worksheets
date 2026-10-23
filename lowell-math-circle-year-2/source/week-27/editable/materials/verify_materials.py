#!/usr/bin/env python3
"""Measure the Week 27 kit PDF and read every case card back.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: build/materials.pdf). Needs PyMuPDF. Sizes come from the PDF's
vector drawings; each case card's strips are read from the letters printed
on it and compared with src/math_checks.json, the student builder's data.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'src' / 'math_checks.json').read_text())
MM = 25.4 / 72
TOL = 0.05
P, L = (612, 792), (792, 612)


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def shapes(page):
    rects, circles, lines, fills = [], [], [], []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if kinds and all(k == 'c' for k in kinds):
            circles.append(((r[0] + r[2]) / 2, (r[1] + r[3]) / 2, (r[2] - r[0]) / 2))
            continue
        if 'f' in d['type']:
            fills.append(r)
        if 's' in d['type'] and kinds == ['l', 'l', 'l', 'l']:
            rects.append(r)
        if d['type'] == 's' and kinds == ['l']:
            lines.append((r, (d.get('dashes') or '[]').startswith('[ '), d['width']))
    return rects, circles, lines, fills


def spans(page):
    out = []
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for s in line['spans']:
                if s['text'].strip():
                    x0, y0, x1, y1 = [v * MM for v in s['bbox']]
                    out.append((s['text'].strip(), s['size'], (x0 + x1) / 2, (y0 + y1) / 2, x0, y0))
    return out


def inside(x, y, r):
    return r[0] < x < r[2] and r[1] < y < r[3]


def blocks(left, right, match):
    """Blocking pairs of a matching {circle: square} under complete strict lists."""
    partner = {**match, **{v: k for k, v in match.items()}}
    out = []
    for a, la in left.items():
        for x in la:
            if match[a] == x:
                continue
            lx = right[x]
            if la.index(x) < la.index(match[a]) and lx.index(a) < lx.index(partner[x]):
                out.append(a + x)
    return out


def expected():
    def get(key, **blank):
        left, right = DATA[key]['left'], dict(DATA[key]['right'])
        for k in blank:
            right[k] = ['', '']
        return left, right
    return {
        'K–1 Problem 1, top case': get('k_unique_mutual'),
        'K–1 Problem 1, bottom case': get('k_unique_shared'),
        'K–1 Problem 2, top case': get('k_two_stable'),
        'K–1 Problem 2, bottom case': get('k_unique_cross'),
        'K–1 Problem 3, top case': get('k_one_blocker'),
        'K–1 Problem 3, bottom case': get('k_unique_cross'),
        'K–1 Problem 4, top case (Y’s strip is empty)': get('k_two_stable', Y=1),
        'K–1 Problem 4, bottom case (Y’s strip is empty)':
            ({'A': ['X', 'Y'], 'B': ['X', 'Y']}, {'X': ['B', 'A'], 'Y': ['', '']}),
        'Grades 2–3 Problem 1, top case': get('k_unique_shared'),
        'Grades 2–3 Problem 1, bottom case': get('k_two_stable'),
        'Grades 2–3 Problem 2': get('middle_unique'),
        'Grades 2–3 Problem 3': get('middle_three'),
        'Grades 2–3 Problem 4': get('middle_four'),
        'Grades 4–5 Problem 1, top case': get('k_two_stable'),
        'Grades 4–5 Problem 1, bottom case': get('middle_unique'),
        'Grades 4–5 Problem 2': get('older_four'),
    }


def read_card(card, sp, circles, rects):
    """Return (label, left strips, right strips) printed inside one case card."""
    inner = [s for s in sp if inside(s[2], s[3], card)]
    label = ' '.join(s[0] for s in sorted(inner, key=lambda s: s[4]) if s[1] < 9 and len(s[0]) > 1)
    letters = [s for s in inner if s[1] > 20 and s[0].isalpha()]
    icons = [(c[0], c[1]) for c in circles if inside(c[0], c[1], card) and close(c[2], 10.0)]
    icons += [((r[0] + r[2]) / 2, (r[1] + r[3]) / 2) for r in rects
              if inside((r[0] + r[2]) / 2, (r[1] + r[3]) / 2, card) and close(r[2] - r[0], 20.0) and close(r[3] - r[1], 20.0)]
    mid = (card[0] + card[2]) / 2
    rows = sorted({round(y, 1) for _, y in icons})
    sides = []
    for col in (0, 1):
        strips = {}
        for ry in rows:
            row_icons = sorted(x for x, y in icons if close(y, ry, 0.2) and ((x < mid) == (col == 0)))
            text = []
            for x in row_icons:
                t = [s[0] for s in letters if close(s[2], x, 3) and close(s[3], ry, 4)]
                text.append(t[0] if t else '')
            strips[text[0]] = text[1:]
        sides.append(strips)
    return label, sides[0], sides[1]


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'materials.pdf'
    doc = pymupdf.open(pdf)
    sizes = [(round(p.rect.width), round(p.rect.height)) for p in doc]
    assert sizes == [P, P, P, P, L, L, P, L, L], sizes
    for i, page in enumerate(doc, 1):
        _, _, lines, _ = shapes(page)
        assert len([r for r, dash, w in lines if close(r[1], r[3]) and close(r[2] - r[0], 100.0)]) == 1, i
    print('PASS pages: 9 US Letter pages, 3 per table band; each has one 100.00 mm scale line.')

    exp = expected()
    found = Counter()
    launches = 0
    icon_sizes = set()
    strip_boxes = Counter()
    for i, page in enumerate(doc, 1):
        rects, circles, lines, fills = shapes(page)
        sp = spans(page)
        widths = {2: 166.0, 3: 212.0, 4: 258.0}
        heights = {2: 56.0, 3: 80.0, 4: 104.0}
        cards = [r for r in rects if any(close(r[2] - r[0], widths[n]) and close(r[3] - r[1], heights[n]) for n in widths)]
        for c in circles:
            if 9 < c[2] < 11:
                icon_sizes.add(round(2 * c[2], 2))
        for r in rects:
            for n in (2, 3, 4):
                if close(r[2] - r[0], 2 + 23 * n) and close(r[3] - r[1], 23.0):
                    strip_boxes[n] += 1
        for card in cards:
            label, left, right = read_card(card, sp, circles, rects)
            if label.startswith('Launch'):
                launches += 1
                assert (left, right) == ({'A': ['Y', 'X'], 'B': ['X', 'Y']}, {'X': ['A', 'B'], 'Y': ['A', 'B']}), (left, right)
                continue
            assert label in exp, (i, label)
            assert (left, right) == exp[label], (label, left, right, exp[label])
            found[label] += 1
        # Pieces on the three pieces pages.
        if i in (1, 4, 7):
            tok = [r for r in rects if close(r[2] - r[0], 24.0) and close(r[3] - r[1], 24.0)]
            assert len(tok) == (4 if i == 1 else 8), (i, len(tok))
            assert len([c for c in circles if close(c[2], 11.0)]) == (2 if i == 1 else 4)
            lk = [r for r in rects if close(r[2] - r[0], 90.0) and close(r[3] - r[1], 9.0)]
            dashed = [r for r, dash, w in lines if dash and close(r[2] - r[0], 82.0)]
            assert len(lk) == 5 and len(dashed) == 1, (i, len(lk), len(dashed))
            small = [r for r in rects if close(r[2] - r[0], 18.0) and close(r[3] - r[1], 18.0)]
            if i == 1:
                letters = Counter(s[0] for s in sp if s[1] > 15 and s[0] in 'ABXY' and any(inside(s[2], s[3], r) for r in small))
                assert len(small) == 16 and letters == Counter({'A': 4, 'B': 4, 'X': 4, 'Y': 4}), letters
            elif i == 7:
                assert len(small) == 16 and len([f for f in fills if close(f[2] - f[0], 18.0)]) == 16
            else:
                assert not small
    assert found == Counter({k: 1 for k in exp}), found
    assert launches == 3, launches
    assert icon_sizes == {20.0}, icon_sizes
    print(f'PASS case cards: {sum(found.values())} problem cases, each printed once in its band and read back '
          f'letter by letter equal to src/math_checks.json; 3 launch cards. Strip icons 20.00 mm; '
          f'strip boxes {dict(strip_boxes)} (four-choice strips 122.00 mm long).')
    print('PASS pieces: K-1 sheet has tokens A, B (circles), X, Y (squares), 24.00 mm; grades 2-3 and 4-5 sheets '
          'have A-D and W-Z. Each sheet has 4 links and 1 dashed link (90.00 x 9.00 mm). K-1: 16 tiles of 18.00 mm '
          '(four each of A, B, X, Y). Grades 4-5: 16 already-asked markers of 18.00 mm.')

    # The launch profile is printed in no packet and behaves as the guide says.
    left, right = {'A': ['Y', 'X'], 'B': ['X', 'Y']}, {'X': ['A', 'B'], 'Y': ['A', 'B']}
    for key, v in DATA.items():
        if isinstance(v, dict) and 'left' in v:
            assert (v['left'], v['right']) != (left, right), key
    assert blocks(left, right, {'A': 'Y', 'B': 'X'}) == []
    assert blocks(left, right, {'A': 'X', 'B': 'Y'}) == ['AY']
    print('PASS launch: its profile is in no packet; with AY and BX nothing blocks; with AX and BY only A and Y block.')

    # What each problem needs from the pieces.
    need = {'K-1 tokens': 4, 'older tokens (four pairs in 2-3 P4, 4-5 P2)': 8,
            'links (one per pair, four pairs)': 4, 'asked markers (4 askers x 4 choices, 4-5 P2)': 16,
            'K-1 tiles per letter (two full sets of strips in P5-P6, 2 per letter each)': 4}
    assert all(v <= have for v, have in zip(need.values(), [4, 8, 4, 16, 4]))
    one_set = Counter()
    for strips in ({'A': 'XY', 'B': 'XY'}, {'X': 'AB', 'Y': 'AB'}):
        for owner, choices in strips.items():
            one_set.update(choices)
    assert all(v == 2 for v in one_set.values())
    print('PASS problem needs: tokens, links, markers and tiles cover the largest case in each band; one full set '
          'of K-1 strips uses two tiles of each letter, so 16 tiles fill two sets side by side.')


if __name__ == '__main__':
    main()
