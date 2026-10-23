#!/usr/bin/env python3
"""Measure the Week 29 rod sheet and check it against what each problem builds.

Usage: python3 materials/verify_materials.py [path/to/materials.pdf]
(default: materials.pdf in the package folder). Needs PyMuPDF. Rod sizes are
read back from the PDF's vector drawings in points and converted to
millimetres, and each rod's printed numeral is read back too. The K-1 strips
the rods must fill are measured from reference-pdfs/k-1.pdf. Then every
target each problem prints is built from one kit, and the consecutive runs the
keys use as certificates are checked for fitting one kit at the same time.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
MM = 25.4 / 72
TOL = 0.05
UNIT = 10.0
KIT = Counter({2: 10, 3: 10, 4: 10, 5: 10, 6: 3, 7: 10})


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def measure(pdf):
    doc = pymupdf.open(pdf)
    assert len(doc) == 1 and (round(doc[0].rect.width), round(doc[0].rect.height)) == (612, 792)
    page = doc[0]
    rods, scale = [], []
    for d in page.get_drawings():
        r = [v * MM for v in d['rect']]
        kinds = [it[0] for it in d['items']]
        if 'f' in d['type'] and 's' in d['type'] and kinds in (['l'] * 4, ['re']) and close(r[3] - r[1], UNIT):
            rods.append(r)
        elif d['type'] == 's' and kinds == ['l'] and close(r[1], r[3]) and close(r[2] - r[0], 100.0):
            scale.append(r)
    assert len(scale) == 1, scale
    print('PASS page: one US Letter portrait page with one 100.00 mm scale line.')
    words = page.get_text('words')
    got, rows = Counter(), {}
    for r in rods:
        n = round((r[2] - r[0]) / UNIT)
        assert close(r[2] - r[0], n * UNIT), r
        label = [w[4] for w in words if r[0] < (w[0] + w[2]) / 2 * MM < r[2] and r[1] < (w[1] + w[3]) / 2 * MM < r[3]]
        assert label == [str(n)], (r, label)
        got[n] += 1
        rows.setdefault(round(r[1], 2), []).append(r)
    assert got == KIT, got
    ys = sorted(rows)
    assert all(close(ys[i + 1] - ys[i], UNIT) for i in range(len(ys) - 1))
    x0 = min(r[0] for rs in rows.values() for r in rs)
    for y in ys:
        rs = sorted(rows[y], key=lambda r: r[0])
        assert close(rs[0][0], x0) and all(close(a[2], b[0]) for a, b in zip(rs, rs[1:])), y
        assert close(rs[-1][2] - x0, 190.0), y
    print(f'PASS rods: {sum(got.values())} rods, each 10.00 mm wide at 10.00 mm per unit: ten each of 2, 3, 4, 5 '
          f'and 7 and three 6-rods, each carrying its length. The {len(ys)} rows each measure 190.00 mm and abut, '
          f'so every cut is straight and shared.')


def student_strips():
    """The K-1 strips are outlines the rods must fill: 1 cm high, n cm long (page 1 has 1-10)."""
    page = pymupdf.open(ROOT / 'reference-pdfs' / 'k-1.pdf')[0]
    found = sorted(round((d['rect'][2] - d['rect'][0]) * MM / UNIT, 2) for d in page.get_drawings()
                   if close((d['rect'][3] - d['rect'][1]) * MM, UNIT, 0.3) and (d['rect'][2] - d['rect'][0]) * MM > 5
                   and d['type'] == 's' and [it[0] for it in d['items']] in (['re'], ['l'] * 4))
    lengths = [n for n in found if close(n, round(n), 0.01)]
    assert {1, 2, 5, 6, 8, 9, 10} <= set(round(n) for n in lengths), found
    print(f'PASS scale: the strips and rods on K-1 page 1 measure {sorted(set(round(n) for n in lengths))} cm by '
          f'1 cm, so a kit rod of n units fills an n-cell strip exactly.')


def builds(a, b, n):
    return [(x, (n - a * x) // b) for x in range(n // a + 1) if (n - a * x) % b == 0]


def fits(a, b, n):
    """A build of n from one kit, using as few rods as possible, or None."""
    ok = [(x, y) for x, y in builds(a, b, n) if x <= KIT[a] and y <= KIT[b]]
    return min(ok, key=sum) if ok else None


# (problem id, pair, printed or keyed targets)
TARGETS = [
    ('w29.rules', (3, 4), [7]),
    ('w29.lengths-3-4 K-1', (3, 4), [1, 2, 5, 6, 8, 9, 10]),
    ('w29.lengths-3-4 2-3', (3, 4), range(1, 17)),
    ('w29.lengths-3-4 4-5', (3, 4), range(1, 21)),
    ('w29.ways-3-4', (3, 4), [12, 15, 16, 24]),
    ('w29.last-gaps', (3, 5), range(1, 21)),
    ('w29.last-gaps', (4, 5), range(1, 21)),
    ('w29.lengths-3-5', (3, 5), range(1, 21)),
    ('w29.four-seven-18-29', (4, 7), range(17, 30)),
    ('w29.from-some-point-on K-1', (3, 4), range(6, 19)),
    ('w29.from-some-point-on 2-3', (3, 4), range(1, 24)),
    ('w29.from-some-point-on 2-3', (3, 5), range(1, 24)),
    ('w29.two-and-four', (2, 4), range(1, 13)),
    ('w29.four-seven-last', (4, 7), range(12, 29)),
    ('w29.ways-24', (3, 4), [24]),
    ('w29.five-seven', (5, 7), range(19, 32)),
] + [('w29.which-pairs', p, range(6, 13)) for p in combinations((2, 3, 4, 5), 2)] \
  + [('w29.claim', p, range(1, 25)) for p in combinations((2, 3, 4, 5, 7), 2)] \
  + [('w29.infinitely-many', p, range(1, 25)) for p in ((2, 4), (3, 6), (4, 6), (3, 5), (4, 7))]

# Consecutive runs a key builds side by side as a certificate.
TOGETHER = [((3, 4), [6, 7, 8]), ((3, 5), [8, 9, 10]), ((4, 5), [12, 13, 14, 15]), ((4, 7), [18, 19, 20, 21])]


def check_targets():
    every_way = 0
    for name, (a, b), targets in TARGETS:
        for n in targets:
            if builds(a, b, n):
                assert fits(a, b, n), (name, a, b, n)
    for n in (12, 15, 16, 24):
        for x, y in builds(3, 4, n):
            assert x <= KIT[3] and y <= KIT[4], n
            every_way += 1
    print(f'PASS problem needs: every buildable target that the problems print or the keys use, with every pair '
          f'they name (including all pairs from 2, 3, 4, 5 and 7 up to 24, and 3/6 and 4/6 with three 6-rods), '
          f'has a build from one kit; all {every_way} ways to build 12, 15, 16 and 24 with 3- and 4-rods fit.')
    for (a, b), run in TOGETHER:
        use = Counter()
        for n in run:
            x, y = fits(a, b, n)
            use[a] += x
            use[b] += y
        assert all(use[k] <= KIT[k] for k in use), (a, b, use)
    a, b, run = 5, 7, range(24, 29)
    fives = sum(min(builds(a, b, n), key=sum)[0] for n in run)
    assert fives == 12
    print('PASS certificates: the runs 6-8 (3/4), 8-10 (3/5), 12-15 (4/5) and 18-21 (4/7) fit one kit side by side. '
          'The 5/7 run 24-28 needs 12 five-rods at once, two more than a kit: build it in turns or record counts, '
          'as the guide says for large targets.')


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'materials.pdf'
    measure(pdf)
    student_strips()
    check_targets()


if __name__ == '__main__':
    main()
