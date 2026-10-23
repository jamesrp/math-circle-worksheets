#!/usr/bin/env python3
"""Check the second set of October 23, 2026 card fixes to Week 39 (shoulds 2-9, the rest of 10,
11 and 12, coulds 13-15) by enumeration and by reading the reference PDFs.

Nothing is imported from the packet or guide builders. The PDFs are read with PyMuPDF
(in requirements.txt). Run from anywhere:
    python3 review/verify_card_shoulds_2026_10_23.py
"""
import json
from functools import lru_cache
from itertools import permutations
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
MM = 25.4 / 72
checks = []


def pairs(route):
    """Positions i where step i and step i+1 run along the same road in opposite directions."""
    return [i for i in range(len(route) - 2) if route[i] == route[i + 2]]


@lru_cache(None)
def finals(route):
    """Every way to remove out-and-back pairs until none remain: {final route: number of orders}."""
    found = pairs(route)
    if not found:
        return {route: 1}
    out = {}
    for i in found:
        for r, n in finals(route[:i + 1] + route[i + 3:]).items():
            out[r] = out.get(r, 0) + n
    return out


def join(trips):
    route = trips[0]
    for t in trips[1:]:
        route += t[1:]
    return route


TRIP = {'a': 'HABH', 'A': 'HBAH', 'b': 'HCDH', 'B': 'HDCH'}   # A, B: the backward trips
def shorten(order):
    out = finals(join([TRIP[c] for c in order]))
    assert len(out) == 1
    return next(iter(out))


# --- Enumeration --------------------------------------------------------------------------
old, new = 'ABCDABCBA', 'ABCBCDABA'
assert len(pairs(old)) == 1 and finals(old) == {'ABCDA': 1}
assert len(pairs(new)) == 3 and finals(new) == {'ABCDA': 4}
checks.append('should 2: 4-5 P4\'s old third route ABCDABCBA had one removal order; ABCBCDABA has three first '
              'choices and four orders, all ending at ABCDA')

six = {''.join(o): shorten(o) for o in permutations('abA')}
assert sorted(o for o, r in six.items() if r == 'HCDH') == sorted(['aAb', 'Aab', 'baA', 'bAa'])
assert six['abA'] == 'HABHCDHBAH' and six['Aba'] == 'HBAHCDHABH'
checks.append('should 4: of the six orders of left forward, right forward and left backward, four shorten to '
              'HCDH; a b a^-1 and a^-1 b a survive and differ')

orders = [''.join(o) for o in permutations('abAB')]
gone = [o for o in orders if shorten(o) == 'H']
alternate = [o for o in orders if all(o[i].lower() != o[i + 1].lower() for i in range(3))]
assert len(orders) == 24 and len(gone) == 16 and sorted(set(orders) - set(gone)) == sorted(alternate) and len(alternate) == 8
checks.append('should 3: of the 24 orders of the four whole-ring trips, 16 disappear; the 8 survivors are exactly '
              'the orders that alternate left and right')

# --- Student pages ------------------------------------------------------------------------
docs = {b: pymupdf.open(REF / f'{b}.pdf') for b in ('k-1', 'grades-2-3', 'grades-4-5')}
text = lambda p: ' '.join(p.get_text().split())
flat = lambda p: ''.join(p.get_text().split())
allpages = [text(p) for d in docs.values() for p in d]
rules = ('Two adjacent steps along the same road in opposite directions are an out-and-back pair. '
         'Remove only out-and-back pairs, and replay the other steps in order.')
assert all(rules in text(d[0]) for d in docs.values())
for gone_word in ('immediate reversal', 'immediate out-and-back', 'detour'):   # the header's topic is "Road detours"
    assert not any(gone_word in t.replace('Week 39 / Road detours /', '') for t in allpages), gone_word
checks.append('should 5: every band\'s rules name "an out-and-back pair" once; no page says "immediate reversal", '
              '"immediate out-and-back" or "detour"')

assert not any('an adult may record' in t for t in allpages)
checks.append('should 6: "an adult may record" is gone from every page 1')

for b, d in docs.items():
    p = d[0]
    words = p.get_text('words')
    labels = [w for w in words if w[0] * MM > 150 and w[1] * MM > 55 and w[4] == 'replay']   # below the rules text
    assert not labels and 'then replay' not in text(p), b
    top = ''.join(w[4] for w in words if 170 < w[0] * MM and 60 < w[1] * MM < 90)
    low = ''.join(w[4] for w in words if 95 < w[0] * MM < 125 and 130 < w[1] * MM < 150)
    assert top == 'A→B→C→B→D' and low == 'A→B→D', (b, top, low)
checks.append('should 7: on each page 1 the worked example reads A→B→C→B→D beside the input row and A→B→D beside '
              'the output row; "replay" and "then replay" labels are gone')

for b in ('grades-2-3', 'grades-4-5'):
    p = docs[b][0]
    rules_ = sorted((round(d['rect'].y0 * MM), round(d['rect'].width * MM)) for d in p.get_drawings()
                    if d['rect'].height * MM < 1 and d['rect'].y0 * MM > 170 and d['rect'].width * MM > 50)
    assert [w for _, w in rules_] == [70, 70, 70, 91, 91], (b, rules_)
checks.append('should 8: Grades 2-3 and 4-5 Problem 1 give each recorded trip an answer line and two lines for the '
              'new seven-step trip')

k1 = docs['k-1']
assert 'Problem 5: Make trips from C to F that use every road and shorten each one. Can two of them shorten to different trips?' in text(k1[3])   # "end differently" until the critic follow-up
assert 'Problem 6: Make eight-step trips from A back to A and shorten each. Find every different result.' in text(k1[4])
checks.append('should 9: K-1 Problems 5 and 6 read as the card gives them')

b45 = docs['grades-4-5']
assert 'A→B→C→B→C→D→A→B→A' in flat(b45[2]) and 'A→B→C→D→A→B→C→B→A' not in flat(b45[2])
assert 'Problem 6: Join the same four ring trips in every possible order. Which orders disappear?' in text(b45[3])
b23 = docs['grades-2-3']
assert ('Join these three ring trips in each of the six possible orders and shorten each journey. '
        'Which orders shorten to the same trip?') in text(b23[3])
assert all('H to A to B and back to H' in text(d[3]) and 'through A' not in text(d[3]) for d in (b23, b45))
assert 'Problem 2: Make two different 12-step trips from A back to A' in text(b23[1])
checks.append('shoulds 2-4 and coulds 14-15 on the pages: 4-5 P4\'s new third route, 4-5 P6 and 2-3 P5 as above, '
              '"H to A to B and back to H" in 2-3 and 4-5 P5, two 12-step trips in 2-3 P2')

ids = {'k-1': 'F39-K-v5',   # v3 until the footer-version sweep, later on October 23; v5 after the critic follow-up
       'grades-2-3': 'F39-23-v4', 'grades-4-5': 'F39-45-v3'}
assert all(ids[b] in text(p) for b, d in docs.items() for p in d)

# --- The guide ----------------------------------------------------------------------------
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
g = [text(p) for p in guide]
assert len(guide) == 7 and all(f'{i} / 7' in t for i, t in enumerate(g, 1)) and not any(' / 6' in t for t in g)
assert 'F39-K-v5, F39-23-v4 and F39-45-v3' in g[5]
checks.append('should 10: every guide page counts "n / 7", the route note included; guide p. 6 names the IDs (K-1 v5, 2-3 v4, 4-5 v3), '
              'which every student page prints')

src = json.loads((ROOT / 'facilitator-src' / 'content.json').read_text())
key = src['pages'][2]
assert key['title'] == 'K-1 answer key'
numbered = [b[1].split('</b>')[0] for b in key['body'] if b[0] == 'p' and b[1].startswith('<b>Problem')]
assert numbered == [f'<b>Problem {n}.' for n in range(1, 8)], numbered
note = json.loads((ROOT / 'facilitator-src' / 'route-note.json').read_text())['notes']
assert [h for h, _ in note] == ['Use and return choices']
assert 'K-1 Problems 1-2' in g[6] and 'Grades 2-3 Problems 1-4; Grades 4-5 Problems 1-4' in g[6] and 'Entry keys' not in g[6]
checks.append('should 11: one K-1 key, Problems 1-7 in order on guide p. 3; the route note gives a first route for '
              'each band and no separate entry keys')

assert 'the printed maps on the student pages are the mats' in g[1] and 'two-ring mat' not in g[1]
checks.append('should 12: guide p. 2 says the printed maps are the mats')

assert not any('zero-net-count obstruction' in t for t in g)
assert 'find a zero-net-count trip that cannot disappear' in g[0] and 'zero-net-count trips that cannot disappear' in g[6]
checks.append('could 13: guide pp. 1 and 7 say "a zero-net-count trip that cannot disappear"')

assert 'ABCBCDABA' in g[4] and 'Of the 24 orders' in g[4] and '16 disappear and 8 survive' in g[4]
assert 'Four orders shorten to HCDH' in g[3]
checks.append('keys: guide p. 4 (2-3 P5) and p. 5 (4-5 P4 and P6) match the enumeration')

for c in checks:
    print('PASS', c)
