#!/usr/bin/env python3
"""Check the Week 48 critic follow-up (Critic C shoulds 1-2, could 3) in the print PDFs.

Usage: python3 plans/review/checks/week-48/check_critic_fixes.py   (from the repository root)

Reads lowell-math-circle-year-2/week-48/*.pdf and the archived card-fix copies. Independent of
the package's own verifiers: it measures the tile sheet's squares from the vector drawing,
counts the fine covers with its own exact clipping, and compares extracted text.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import difflib
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'lowell-math-circle-year-2/week-48'
A = P / 'archive-before-critic-fixes-2026-10-23'
MM = 25.4 / 72


def N(s):
    return re.sub(r'\s+', ' ', re.sub(r'-\s?\n', '', s)).strip()


def text(pdf):
    return [N(p.get_text()) for p in pymupdf.open(pdf)]


# 1. Tile sheet: 16 squares of 30 mm and 48 of 15 mm, caption, id.
doc = pymupdf.open(P / 'week-48-materials.pdf')
tiles = Counter()
for d in doc[0].get_drawings():
    r = d['rect']
    w, h = (r.x1 - r.x0) * MM, (r.y1 - r.y0) * MM
    if abs(w - h) < .05 and w > 10:
        tiles[round(w, 1)] += 1
assert tiles == Counter({30.0: 16, 15.0: 48}), tiles
bottom = max(d['rect'].y1 for d in doc[0].get_drawings() if abs((d['rect'].x1 - d['rect'].x0) * MM - 15) < .05) * MM
note = min(w[1] for w in doc[0].get_text('words') if w[4] == 'Physically') * MM
assert bottom < note - 3, (bottom, note)
t = text(P / 'week-48-materials.pdf')[0]
assert '16 big squares (30 mm, one cell of a 4-by-4 board) and 48 small squares (15 mm, one cell of an 8-by-8 board)' in t
assert 'the cells of the 120 mm boards' not in t and 'W48-M-v2' in t
print(f'PASS sheet: 16 squares of 30 mm and 48 of 15 mm (bottom at {bottom:.1f} mm, note at {note:.1f} mm); caption names the 4-by-4 and 8-by-8 cells; W48-M-v2.')

# Fine covers on the 8-by-8 board, by exact clipping (shapes in big-square units, y down).
h = F(1, 2)
SHAPES = {'triangle': [(0, 4), (4, 4), (4, 0)], 'diamond': [(0, 2), (2, 0), (4, 2), (2, 4)],
          'trapezoid': [(h, h), (F(7, 2), h), (3, F(7, 2)), (1, F(7, 2))]}


def area(poly):
    return abs(sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def clip(poly, x0, y0, x1, y1):
    for k, lim, keep in ((0, x0, 1), (0, x1, -1), (1, y0, 1), (1, y1, -1)):
        out = []
        for i, p in enumerate(poly):
            q = poly[(i + 1) % len(poly)]
            pin, qin = keep * (p[k] - lim) >= 0, keep * (q[k] - lim) >= 0
            if pin:
                out.append(p)
            if pin != qin:
                t_ = (lim - p[k]) / (q[k] - p[k])
                out.append(tuple(p[j] + (q[j] - p[j]) * t_ for j in range(2)))
        poly = out
        if not poly:
            return []
    return poly


def cover(shape, n):
    s = F(4, n)
    return sum(area(clip(SHAPES[shape], c * s, r * s, (c + 1) * s, (r + 1) * s)) > 0 for c in range(n) for r in range(n))


fine = {k: cover(k, 8) for k in SHAPES}
assert fine == {'triangle': 36, 'diamond': 40, 'trapezoid': 36}, fine
assert {k: cover(k, 4) for k in SHAPES} == {'triangle': 10, 'diamond': 12, 'trapezoid': 16}
assert max(fine.values()) <= 48
k1 = text(P / 'week-48-k-1.pdf')
assert any('Problem 3: Do Problem 1 again with small squares.' in p for p in k1)
assert any('Cover the triangle with as few grid-square tiles as you can' in p for p in k1)
print('PASS needs: K-1 Problem 3 repeats Problem 1 (fewest tiles) on the 8-by-8 board: 36 small tiles; the fine '
      'trapezoid takes 36 and the diamond 40, all within the 48 on the sheet (big covers 10, 12, 16 within 16).')

g = text(P / 'week-48-facilitator.pdf')
assert 'Final student packets v3' in g[0] and 'packets v2' not in ' '.join(g)
assert ("16 big 30 mm and 48 small 15 mm squares. The trapezoid’s cover takes all 16 big tiles and K-1 Problem 3’s "
        "small-square cover of the triangle takes 36 small") in g[0]
assert 'Shade complete fine covers rather than tiling them' not in g[0]
print('PASS guide: header says packets v3; materials name 48 small tiles and K-1 Problem 3\'s 36.')

# 2. Footers v3 on every page; 3. 4-5 Problem 5 wording.
for band, tag, n in (('k-1', 'K', 5), ('grades-2-3', '23', 6), ('grades-4-5', '45', 6)):
    new, old = text(P / f'week-48-{band}.pdf'), text(A / f'week-48-{band}.pdf')
    assert len(new) == len(old) == n
    for i, (a, b) in enumerate(zip(new, old)):
        assert f'Bellingham Math Circle / Week 48 / F48-{tag}-v3' in a and '-v2' not in a, (band, i)
        diff = a.replace(f'F48-{tag}-v3', f'F48-{tag}-v2')
        if band == 'grades-4-5' and i == 4:
            diff = diff.replace('between your inside count and your cover', 'between your inside and outside bounds')
        assert diff == b, (band, i + 1, list(difflib.ndiff([b], [diff]))[:4])
p5 = text(P / 'week-48-grades-4-5.pdf')[4]
assert 'Choose the three that most reduce the gap between your inside count and your cover.' in p5
assert 'outside bounds' not in ' '.join(text(P / 'week-48-grades-4-5.pdf'))
print('PASS packets: every student page reads F48-K-v3, F48-23-v3 or F48-45-v3; apart from the footer, only '
      '4-5 Problem 5 changed ("between your inside count and your cover").')
