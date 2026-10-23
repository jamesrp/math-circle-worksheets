#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes to Week 39 (K-1 Problem 7, its key and the K-1
version) by enumeration and by reading the reference PDFs.

Nothing is imported from the packet or guide builders. The PDFs are read with
PyMuPDF (in requirements.txt). Run from anywhere:
    python3 review/verify_card_fixes_2026_10_23.py
"""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
checks = []
RING = {'A': 'BD', 'B': 'AC', 'C': 'BD', 'D': 'AC'}   # roads AB, BC, CD, DA


def walks(start, end, n):
    out = [start]
    for _ in range(n):
        out = [w + v for w in out for v in RING[w[-1]]]
    return [w for w in out if w[-1] == end]


def reduce(w):
    """Left-to-right stack: a step that retraces the last road removes it."""
    s = []
    for v in w:
        if len(s) >= 2 and s[-2] == v:
            s.pop()
        else:
            s.append(v)
    return ''.join(s)


def roads(w):
    return frozenset(frozenset(p) for p in zip(w, w[1:]))


# 1. K-1 Problem 7 by enumeration: what six-step A-to-C trips leave, and which pairs use the same four roads.
trips = walks('A', 'C', 6)
results = Counter(reduce(w) for w in trips)
assert len(trips) == 32 and results == {'ABC': 15, 'ADC': 15, 'ABCDABC': 1, 'ADCBADC': 1}, results
same_four = [(a, b) for a, b in combinations(sorted(results), 2) if roads(a) == roads(b) and len(roads(a)) == 4]
assert same_four == [('ABCDABC', 'ADCBADC')], same_four
a, b = same_four[0]
tiles = lambda w: Counter(zip(w, w[1:]))                       # direction kept
road_uses = lambda w: Counter(frozenset(p) for p in zip(w, w[1:]))
assert tiles(a) != tiles(b) and road_uses(a) != road_uses(b)
assert {frozenset(r) for r, k in road_uses(a).items() if k == 2} == {frozenset('AB'), frozenset('BC')}
assert {frozenset(r) for r, k in road_uses(b).items() if k == 2} == {frozenset('AD'), frozenset('CD')}
checks.append('P7: the 32 six-step A-to-C trips leave ABC, ADC (15 each), ABCDABC and ADCBADC (1 each); only '
              'ABCDABC and ADCBADC use the same four roads (yes), and their tiles differ: each crosses a different '
              'two roads twice (so "no, the tiles differ" is a fair reading)')

# 2. The printed K-1 packet: the new question, the old one gone, its id on every page (F39-K-v3 after this fix,
# F39-K-v4 since the afternoon's K-1 changes, bumped by the footer-version sweep the same day; F39-K-v5 since
# a critic's follow-up reworded K-1 Problem 5).
K1_ID = 'F39-K-v5'
k1 = pymupdf.open(REF / 'k-1.pdf')
text = lambda p: ' '.join(p.get_text().split())
p6 = text(k1[5])
assert ('Problem 7: Make every different trip from A to C that can remain after shortening a six-step trip. '
        'Can two of your remaining trips use the same four roads?') in p6, p6
assert not any('in a different order' in text(p) or 'visit exactly the same roads' in text(p) for p in k1)
assert all(f'Bellingham Math Circle / Week 39 / {K1_ID}' in text(p) for p in k1) and len(k1) == 6
for band, tag, v in (('grades-2-3', '23', 'v4'), ('grades-4-5', '45', 'v3')):   # v2 until the afternoon's shoulds made them v3; 2-3 v4 after the critic's follow-up
    assert all(f'F39-{tag}-{v}' in text(p) for p in pymupdf.open(REF / f'{band}.pdf'))
checks.append('K-1 p. 6: "Can two of your remaining trips use the same four roads?"; every K-1 page reads ' + K1_ID + ', '
              'as guide p. 6 says; Grades 2-3 and 4-5 read v3 since review/card-shoulds-2026-10-23.md (2-3 v4 since the critic follow-up)')

# 3. The key: the guide's source and the printed guide accept the "no" reading.
guide = json.loads((ROOT / 'facilitator-src' / 'content.json').read_text())
key = next(b[1] for b in guide['pages'][2]['body'] if b[0] == 'p' and b[1].startswith('<b>Problem 7.</b>'))
assert key.endswith('Accept no with the reason that the tiles differ.') and 'ABCDABC, and ADCBADC' in key, key
pdf = pymupdf.open(REF / 'facilitator-guide.pdf')
assert len(pdf) == 7 and 'Accept no with the reason that the tiles differ.' in text(pdf[2])
assert 'K-1 has six pages, Problems 1-7;' in text(pdf[5]) and K1_ID in text(pdf[5])
checks.append('guide p. 3: the Problem 7 key adds "Accept no with the reason that the tiles differ."; '
              'guide p. 6 names ' + K1_ID + ', now true')

for c in checks:
    print('PASS', c)
