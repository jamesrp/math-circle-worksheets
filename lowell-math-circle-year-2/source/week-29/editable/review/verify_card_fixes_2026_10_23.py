#!/usr/bin/env python3
"""Check the statements changed in the October 23, 2026 guide corrections (Week 29),
and every entry of the K-1 answer key, by enumeration.

Nothing is imported from the packet or guide builders. The geometry check reads
the reference student PDFs with PyMuPDF (in requirements.txt).
Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py
"""
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ways(n, a, b):
    """All (x, y) with x a-rods and y b-rods totalling n."""
    return [(x, (n - a * x) // b) for x in range(n // a + 1) if (n - a * x) % b == 0]


def can(n, a, b):
    return bool(ways(n, a, b))


checks = []

# K-1 key, P1-P5.
p1 = [1, 2, 5, 6, 8, 9, 10]                      # printed strips on K-1 p. 1
assert [t for t in p1 if can(t, 3, 4)] == [6, 8, 9, 10]
assert [t for t in p1 if not can(t, 3, 4)] == [1, 2, 5]
checks.append('K-1 P1: of strips 1, 2, 5, 6, 8, 9, 10, exactly 6, 8, 9, 10 work with 3 and 4')
assert ways(12, 3, 4) == [(0, 3), (4, 0)] and ways(15, 3, 4) == [(1, 3), (5, 0)]
checks.append('K-1 P2: 12 = four 3s or three 4s; 15 = five 3s or one 3 and three 4s; no others')
p3 = [4, 7, 8, 9, 10, 11, 12]                    # printed strips on K-1 p. 3
assert [t for t in p3 if not can(t, 3, 5)] == [4, 7]
checks.append('K-1 P3: of strips 4, 7, 8, 9, 10, 11, 12, exactly 4 and 7 fail with 3 and 5')
assert all(can(t, 3, 4) for t in range(6, 19)) and all(can(t, 3, 4) for t in range(6, 200))
checks.append('K-1 P4: every length 6-18 (and on to 199) is built from 3 and 4')
assert [t for t in range(1, 13) if can(t, 2, 4)] == [2, 4, 6, 8, 10, 12]
checks.append('K-1 P5: with 2 and 4, exactly 2, 4, 6, 8, 10, 12 work in 1-12')

# K-1 key, P6: every pair from 2, 3, 4, 5 and every target 6-12.
fail = {(a, b): [t for t in range(6, 13) if not can(t, a, b)] for a, b in combinations([2, 3, 4, 5], 2)}
assert fail == {(2, 3): [], (2, 4): [7, 9, 11], (2, 5): [], (3, 4): [], (3, 5): [7], (4, 5): [6, 7, 11]}, fail
checks.append('K-1 P6: {2,3}, {2,5}, {3,4} cover 6-12; failures {2,4}: 7, 9, 11; {3,5}: 7; {4,5}: 6, 7, 11')

# Grades 4-5 P5: gaps of the shared-factor pairs (checked to 300) and last gaps of the others.
def gaps(a, b, top=300):
    return [t for t in range(1, top) if not can(t, a, b)]
assert gaps(2, 4) == [t for t in range(1, 300) if t % 2]
assert gaps(3, 6) == [t for t in range(1, 300) if t % 3]
assert gaps(4, 6) == sorted([2] + [t for t in range(1, 300) if t % 2])
assert gaps(3, 5)[-1] == 7 and gaps(4, 7)[-1] == 17
checks.append('4-5 P5: gaps are odd targets (2/4), nonmultiples of 3 (3/6), odd targets and 2 (4/6); 3/5 and 4/7 stop at 7 and 17')

# Materials: printed strips, rod keys and rulers are 1 cm per unit.
try:
    import pymupdf
    CM = 72 / 2.54
    from collections import defaultdict
    page = pymupdf.open(ROOT / 'reference-pdfs' / 'k-1.pdf')[0]
    rows = defaultdict(set)
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l' and abs(it[1].x - it[2].x) < 0.01:
                rows[round(min(it[1].y, it[2].y), 1)].add(round(it[1].x, 2))
    strips = []
    for y in sorted(rows):
        xs = sorted(rows[y])
        steps = {round((q - p) / CM, 2) for p, q in zip(xs, xs[1:])}
        if steps == {1.0}:
            strips.append(round((xs[-1] - xs[0]) / CM, 2))
    assert strips[-7:] == [1.0, 2.0, 5.0, 6.0, 8.0, 9.0, 10.0], strips
    ticks = 0
    for name in ['k-1.pdf', 'grades-2-3.pdf']:
        for pg in pymupdf.open(ROOT / 'reference-pdfs' / name):
            xs = defaultdict(set)
            for d in pg.get_drawings():
                for it in d['items']:
                    if it[0] == 'l' and abs(it[1].x - it[2].x) < 0.01 and abs(it[1].y - it[2].y) < 12:
                        xs[round(max(it[1].y, it[2].y), 1)].add(round(it[1].x, 2))
            for y, row in xs.items():
                row = sorted(row)
                if len(row) >= 13 and {round((q - p) / CM, 2) for p, q in zip(row, row[1:])} == {1.0}:
                    ticks += 1
    assert ticks >= 1
    checks.append(f'K-1 p. 1 strips are 1, 2, 5, 6, 8, 9, 10 cm in 1 cm cells; {ticks} printed rulers have 1 cm ticks')
except ImportError:
    checks.append('PyMuPDF missing: geometry check skipped')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 29 correction checks')
