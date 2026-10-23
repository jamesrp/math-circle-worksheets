#!/usr/bin/env python3
"""Measure the Week 51 kit PDF and check it against what each problem builds.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: build/materials.pdf). Needs PyMuPDF. Strip sizes are read back from
the PDF's vector drawings in points and converted to millimetres; each
strip's printed numeral is read back too. The problem ranges are read from
the student reference PDFs, and each key's witnesses are rebuilt from the
kit's pieces.
"""
from collections import Counter
from pathlib import Path
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05
UNIT = 10.0


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def measure(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    strips, scale = [], []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if 'f' in d['type'] and 's' in d['type'] and kinds in (['l'] * 4, ['re']) and close(r[3] - r[1], UNIT):
            white = all(c > 0.99 for c in d['fill'])
            assert white or all(close(c, 0.88, 0.01) for c in d['fill']), d['fill']
            strips.append((r, white))
        elif d['type'] == 's' and kinds == ['l'] and close(r[1], r[3]) and close(r[2] - r[0], 100.0):
            scale.append(r)
    assert len(scale) == 1
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')

    words = page.get_text('words')
    gray, white = Counter(), Counter()
    rows = {}
    for r, is_white in strips:
        units = (r[2] - r[0]) / UNIT
        n = round(units)
        assert close(units * UNIT, n * UNIT), r
        label = [w[4] for w in words if r[0] < (w[0] + w[2]) / 2 * MM < r[2] and r[1] < (w[1] + w[3]) / 2 * MM < r[3]]
        assert label == [str(n)], (r, label)
        (white if is_white else gray)[n] += 1
        rows.setdefault(round(r[1], 2), []).append(r)
    assert gray == Counter({n: 2 for n in range(1, 16)}), gray
    assert white == Counter({4: 2, 1: 2}), white
    ys = sorted(rows)
    assert len(ys) == 16 and all(close(ys[i + 1] - ys[i], UNIT) for i in range(15))
    x0 = min(r[0] for rs in rows.values() for r in rs)
    for y in ys:
        rs = sorted(rows[y], key=lambda r: r[0])
        assert close(rs[0][0], x0) and all(close(a[2], b[0]) for a, b in zip(rs, rs[1:])), y
        if y != ys[-1]:
            assert close(rs[-1][2] - x0, 160.0), y
    print('PASS strips: 30 gray strips, 10.00 mm wide, two of every length 1 to 15 units at 10.00 mm per unit; '
          'four white add-ons (two of 4, two of 1). Each strip carries its length. The 15 gray rows each '
          'measure 160.00 mm (one 0-16 ruler) and abut, so every cut is straight and shared.')
    return gray, white


def printed_ranges():
    """Every 'L to U' range printed in each student packet, from the reference PDFs."""
    out = {}
    for name in ('k-1', 'grades-2-3', 'grades-4-5'):
        text = ' '.join(p.get_text() for p in pymupdf.open(ROOT / 'reference-pdfs' / f'{name}.pdf'))
        text = re.sub(r'\s+', ' ', text)
        assert not re.search(r'\d[.,]\d+ to|to \d+[.,]\d', text), name
        out[name] = {(int(a), int(b)) for a, b in re.findall(r'(\d+) to (\d+)', text)}
    return out


K, M, U = 'k-1', 'grades-2-3', 'grades-4-5'
ALL = (K, M, U)
# Each entry: (what is built at the same time, packets, strips as (length, range), add-ons, check).
BUILDS = [
    ('Launch: shortest and longest joins', ALL, [(2, (2, 3)), (1, (1, 2)), (3, (2, 3)), (2, (1, 2))], [],
     ('sums', [3, 5])),
    ('P1: shortest and longest joins', ALL, [(4, (4, 6)), (3, (3, 4)), (6, (4, 6)), (4, (3, 4))], [],
     ('sums', [7, 10])),
    ('K-1 P1: a join ending at 8', (K,), [(5, (4, 6)), (3, (3, 4))], [], ('sums', [8])),
    ('P2: C with D, both extremes', ALL, [(4, (4, 5)), (4, (4, 5)), (5, (4, 5)), (5, (4, 5))], [],
     ('sums', [8, 10])),
    ('P2: E with F, both extremes', ALL, [(6, (6, 8)), (2, (2, 4)), (8, (6, 8)), (4, (2, 4))], [],
     ('sums', [8, 12])),
    ('P3: B from 4 to 5 against A from 3 to 4', ALL, [(3, (3, 4)), (4, (4, 5)), (4, (3, 4)), (5, (4, 5))], [],
     ('sums', [7, 9])),
    ('K-1 P3: the 3-4 card fails low', (K,), [(3, (3, 4)), (3, (3, 4))], [], ('sums', [6])),
    ('K-1 P3: the 5-6 card fails high', (K,), [(4, (3, 4)), (6, (5, 6))], [], ('sums', [10])),
    ('K-1 P4, older P5: same A on top, smallest bottom gap below', ALL,
     [(5, (4, 6)), (5, (4, 6)), (4, (4, 6)), (6, (4, 6))], [4, 1, 4, 1], ('pair_gaps', [3, 1])),
    ('K-1 P4, older P5: largest bottom gap', ALL, [(6, (4, 6)), (4, (4, 6))], [4, 1], ('pair_gaps', [5])),
    ('K-1 P5: biggest and smallest gaps', (K,), [(9, (7, 9)), (5, (5, 6)), (7, (7, 9)), (6, (5, 6))], [],
     ('gaps', [4, 1])),
    ('K-1 P6: gap 3 two ways', (K,), [(8, (7, 9)), (5, (5, 6)), (9, (7, 9)), (6, (5, 6))], [], ('gaps', [3, 3])),
    ('K-1 P7, 2-3 P8: all three pairs filling 9', (K, M),
     [(4, (4, 6)), (5, (3, 5)), (5, (4, 6)), (4, (3, 5)), (6, (4, 6)), (3, (3, 5))], [], ('sums', [9, 9, 9])),
    ('Older P4: uncover A = 5, then B can still vary', (M, U), [(5, (4, 6)), (3, (3, 4)), (5, (4, 6)), (4, (3, 4))],
     [], ('sums', [8, 9])),
    ('Older P6, P7: both bounds of the gap', (M, U), [(13, (13, 15)), (12, (10, 12)), (15, (13, 15)), (10, (10, 12))],
     [], ('gaps', [1, 5])),
    ('4-5 P8: all three pairs totalling 12', (U,),
     [(7, (7, 10)), (5, (3, 7)), (8, (7, 10)), (4, (3, 7)), (9, (7, 10)), (3, (3, 7))], [], ('gaps', [2, 4, 6])),
    ('4-5 P9: remove the same A from both extreme joins', (U,), [(4, (4, 6)), (3, (3, 4)), (6, (4, 6)), (4, (3, 4))],
     [], ('remainders', [3, 4])),
]


def check_builds(gray, white):
    ranges = printed_ranges()
    for name, packets, pieces, addons, (kind, want) in BUILDS:
        for length, (lo, hi) in pieces:
            assert lo <= length <= hi, (name, length, lo, hi)
            assert all((lo, hi) in ranges[p] for p in packets), (name, (lo, hi), packets)
        need = Counter(n for n, _ in pieces)
        assert all(need[n] <= gray[n] for n in need), (name, need)
        assert all(Counter(addons)[n] <= white[n] for n in Counter(addons)), (name, addons)
        lengths = [n for n, _ in pieces]
        pairs = list(zip(lengths[::2], lengths[1::2]))
        if kind == 'sums':
            got = [a + b for a, b in pairs]
            assert all(s <= 16 for s in got)
        elif kind == 'gaps':
            got = [a - b for a, b in pairs]
            assert all(a <= 16 for a, _ in pairs)
        elif kind == 'remainders':
            got = [(a + b) - a for a, b in pairs]
        else:  # long piece plus add-on 4 against short piece plus add-on 1
            got = [(a + 4) - (b + 1) for a, b in pairs]
            assert all(a + 4 <= 16 for a, _ in pairs)
        assert got == want, (name, got, want)
    print(f'PASS problem needs: {len(BUILDS)} witness builds from the keys (every extreme of every join, gap and '
          f'shared-A comparison, and every listed pair) use ranges printed in their packets, fit one set at the same '
          f'time, stay on a 0-16 ruler and give the keys\' values. Every printed range has whole ends, so whole '
          f'strips reach every bound.')


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'materials.pdf'
    gray, white = measure(pdf)
    check_builds(gray, white)


if __name__ == '__main__':
    main()
