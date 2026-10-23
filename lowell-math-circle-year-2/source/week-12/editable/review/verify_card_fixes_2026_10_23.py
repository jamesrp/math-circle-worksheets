#!/usr/bin/env python3
"""Check the statements changed in the October 23, 2026 guide corrections (Week 12).

Independent brute force: every perfect matching of 1..2n, filtered by an
interleaving test. Nothing is imported from the packet or guide builders.
Run from anywhere: python3 review/verify_card_fixes_2026_10_23.py
"""
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def matchings(points):
    if not points:
        yield ()
        return
    a = points[0]
    for i in range(1, len(points)):
        b = points[i]
        for rest in matchings(points[1:i] + points[i + 1:]):
            yield ((a, b),) + rest


def crossing(p, q):
    (a, b), (c, d) = sorted(p), sorted(q)
    return a < c < b < d or c < a < d < b


def noncrossing(n):
    out = []
    for m in matchings(tuple(range(1, 2 * n + 1))):
        if not any(crossing(p, q) for p, q in combinations(m, 2)):
            out.append(m)
    return out


def partner(m):
    d = {}
    for a, b in m:
        d[a] = b
        d[b] = a
    return d


def name(m):
    return '|'.join(f'{a}{b}' for a, b in sorted(tuple(sorted(p)) for p in m))


checks = []
P8 = noncrossing(4)
assert len(P8) == 14
checks.append('14 noncrossing pairings of 8 dots')

# Old hint: "compare only the partners at a single numbered dot". False:
for d in range(1, 9):
    groups = {}
    for m in P8:
        groups.setdefault(partner(m)[d], []).append(m)
    sizes = sorted(len(g) for g in groups.values())
    assert sizes == [2, 2, 5, 5], (d, sizes)
    agreeing = sum(len(g) * (len(g) - 1) // 2 for g in groups.values())
    assert agreeing == 22, (d, agreeing)
checks.append('at every dot the 14 pairings split 5, 2, 2, 5 by partner, so 22 pairs of different pairings agree there')

a = ((1, 2), (3, 4), (5, 6), (7, 8))
b = ((1, 2), (3, 8), (4, 5), (6, 7))
assert a in P8 and b in P8 and partner(a)[1] == partner(b)[1] == 2 and a != b
checks.append('12|34|56|78 and 12|38|45|67 are both legal, agree at dot 1, and differ')

most = max(sum(partner(x)[d] == partner(y)[d] for d in range(1, 9)) for x, y in combinations(P8, 2))
assert most == 4
checks.append('two different pairings agree at up to 4 of the 8 dots')

# New hint: same partner at every dot <=> same pairing; sorting by 1's partner
# and comparing dot by dot within a group separates all 14.
keys = {(partner(m)[1], tuple(partner(m)[d] for d in range(1, 9))) for m in P8}
assert len(keys) == 14
by1 = {}
for m in P8:
    by1.setdefault(partner(m)[1], []).append(name(m))
assert {k: len(v) for k, v in by1.items()} == {2: 5, 4: 2, 6: 2, 8: 5}
checks.append("sorting by 1's partner gives groups 5, 2, 2, 5; within each group the full partner lists are all different")

# Route note: Grades 2-3 P3 and P5 go from codes to pairings (inverse map).
try:
    import pymupdf
    pages = [p.get_text() for p in pymupdf.open(ROOT / 'reference-pdfs' / 'grades-2-3.pdf')]
    text = ' '.join(' '.join(pages).split())
    assert 'Draw a pairing for each path' in text
    assert 'Draw the pairing whenever it is possible' in text
    assert 'Match your paths to your six-dot pairings' in text
    checks.append('grades 2-3 P3 and P5 ask for pairings from paths/codes; P4 matches paths to pairings')
except ImportError:
    checks.append('PyMuPDF missing: student-text route check skipped')

# String length (card fix 5): measure the printed string boards at 100%.
try:
    import math
    import pymupdf
    MM = 72 / 25.4

    def shapes(page):
        dots, rings = [], []
        for d in page.get_drawings():
            r = d['rect']
            w, h = r.width / MM, r.height / MM
            if not any(it[0] == 'c' for it in d['items']) or abs(w - h) > 0.3:
                continue
            c = ((r.x0 + r.x1) / 2 / MM, (r.y0 + r.y1) / 2 / MM)
            if w < 4 and d.get('fill') is not None:
                dots.append((c, w / 2))
            elif w >= 10:
                rings.append((c, w / 2))
        return dots, rings

    longest_chord = 0
    for page in pymupdf.open(ROOT / 'reference-pdfs' / 'k-1.pdf'):
        dots, rings = shapes(page)
        for c, R in rings:
            if R < 30:  # the large string circles; smaller ones are pencil records
                continue
            on = [q for q, _ in dots if abs(math.dist(q, c) - R) < 1]
            longest_chord = max([longest_chord] + [math.dist(a, b) for a in on for b in on])
    assert abs(longest_chord - 86.0) < 0.2, longest_chord
    checks.append(f'longest chord on a large K-1 circle: {longest_chord:.1f} mm (8.6 cm)')

    dots, _ = shapes(pymupdf.open(ROOT / 'reference-pdfs' / 'grades-2-3.pdf')[0])
    big = sorted(q for q, r in dots if r > 1.6)  # the P1 working row has the larger dots
    assert len(big) == 6 and max(q[1] for q in big) - min(q[1] for q in big) < 0.1, big
    span = big[-1][0] - big[0][0]
    half = math.pi * span / 2
    assert abs(span - 120) < 0.2 and half < 200, (span, half)
    checks.append(f'grades 2-3 P1 row: dots 1 and 6 are {span / 10:.1f} cm apart; a half-circle arc is {half / 10:.1f} cm, under 20 cm')
except ImportError:
    checks.append('PyMuPDF missing: string-length measurement skipped')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 12 correction checks')
