#!/usr/bin/env python3
"""Check the Week 34 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-34-k-1.pdf, week-34-grades-2-3.pdf, week-34-grades-4-5.pdf and
week-34-facilitator.pdf (default: the print folder). Needs PyMuPDF. Each fix is checked
in the printed words and drawings, and each mathematical claim it relies on is
recomputed here.
"""
from itertools import product
from pathlib import Path
import math
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2' / 'week-34'
CM = 72 / 2.54
FAILS = []
BANDS = ['k-1', 'grades-2-3', 'grades-4-5']


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


def doc(name):
    return pymupdf.open(FOLDER / f'week-34-{name}.pdf')


def words(page):  # page text on one line, with line-end hyphenation undone
    return re.sub(r'(\w)- (\w)', r'\1\2', re.sub(r'\s+', ' ', page.get_text()).strip())


# ------------------------------------------------------------------ mathematics

def motions(n):
    """The 2n motions of a regular n-ring, as (kind, k, permutation); ('turn', 0) is the identity."""
    out = [('turn', k, [(i + k) % n for i in range(n)]) for k in range(n)]
    return out + [('flip', k, [(k - i) % n for i in range(n)]) for k in range(n)]


def matching(ring):
    n = len(ring)
    return [(m, k) for m, k, p in motions(n) if (m, k) != ('turn', 0) and all(ring[p[i]] == ring[i] for i in range(n))]


def same_pattern(a, b):  # some motion carries a onto b with the kinds kept fixed
    return any(all(a[i] == b[p[i]] for i in range(len(a))) for _, _, p in motions(len(a)))


mixed = [r for n in (3, 4, 5) for r in product('AB', repeat=n) if len(set(r)) == 2]
check('fix 1: 48 of the 50 mixed two-kind patterns on 3-5 rings have no matching turn',
      len(mixed) == 50 and sum(not any(m == 'turn' for m, _ in matching(r)) for r in mixed) == 48)
check('fix 1: every two-kind pattern on 3-5 rings has a matching flip',
      all(any(m == 'flip' for m, _ in matching(r)) for n in (3, 4, 5) for r in product('AB', repeat=n)))
check('could 6: on the three-ring no two-kind pattern resists every move, and ABC does',
      all(matching(r) for r in product('AB', repeat=3)) and not matching('ABC'))
for w, gaps in (('AABABBB', [1, 2, 4]), ('AABABBBBB', [1, 2, 6])):
    a = [i for i, c in enumerate(w) if c == 'A']
    check(f'fix 4: {w} has no matching turn or flip, A gaps {gaps}',
          not matching(w) and sorted((a[(j + 1) % 3] - a[j]) % len(w) for j in range(3)) == gaps)
check('fix 4: on the 7- and 9-rings every flip fixes exactly one spot',
      all(sum(p[i] == i for i in range(n)) == 1 for n in (7, 9) for m, _, p in motions(n) if m == 'flip'))
check('fix 4: on the 6- and 8-rings some flip fixes no spot',
      all(any(m == 'flip' and all(p[i] != i for i in range(n)) for m, _, p in motions(n)) for n in (6, 8)))
check('fix 5: BBABAAAA resists every move but cannot match AABABBBB with the kinds fixed',
      not matching('BBABAAAA') and not same_pattern('AABABBBB', 'BBABAAAA'))


# ------------------------------------------------------------------ the page-1 picture

def demo_rings(page):
    """Small rings on a page: centre, and the counter kinds read clockwise from the top spot (0 filled, 1 hollow)."""
    rings, spots, dots, hollow = [], [], [], []
    for d in page.get_drawings():
        r = d['rect']
        if [i[0] for i in d['items']] != ['c'] * 4 or abs(r.width - r.height) > .01:
            continue
        c = ((r.x0 + r.x1) / 2 / CM, (r.y0 + r.y1) / 2 / CM, r.width / 2 / CM)
        if abs(c[2] - 1) < .02 and d['type'] == 's':
            rings.append(c)
        elif abs(c[2] - .37) < .02:
            spots.append(c)
        elif abs(c[2] - .1665) < .02:
            (dots if d['type'] == 'f' else hollow).append(c)
    out = []
    for x, y, _ in sorted(rings):
        on = sorted((s for s in spots if abs(math.hypot(s[0] - x, s[1] - y) - 1) < .02),
                    key=lambda s: (math.atan2(s[0] - x, -(s[1] - y)) + .01) % (2 * math.pi))  # clockwise from the top spot
        kinds = []
        for sx, sy, _ in on:
            kinds.append(0 if any(math.hypot(sx - u, sy - v) < .02 for u, v, _ in dots)
                         else 1 if any(math.hypot(sx - u, sy - v) < .02 for u, v, _ in hollow) else None)
        out.append(((x, y), kinds))
    return out


def arrows(page):
    """Start and end of each black arrow shaft (a straight line or a curve of 1pt width)."""
    out = []
    for d in page.get_drawings():
        if d['type'] != 's' or abs((d.get('width') or 0) - 1) > .05 or d.get('dashes') not in (None, '[] 0'):
            continue
        items = d['items']
        if len(items) == 1 and items[0][0] in 'lc':
            a, b = items[0][1], items[0][-1]
            out.append(((a.x / CM, a.y / CM), (b.x / CM, b.y / CM)))
    return out


def nearest(pt, centres):
    return min(range(len(centres)), key=lambda i: math.hypot(pt[0] - centres[i][0], pt[1] - centres[i][1]))


for band in BANDS:
    p = doc(band)[0]
    t = words(p)
    check(f'fix 1 {band}: rules say "Turn or flip (turn over) its tracing copy"', 'Turn or flip (turn over) its tracing copy' in t)
    check(f'fix 3 {band}: rules say "neighbors may be the same kind"', 'neighbors may be the same kind' in t)
    check(f'could 8 {band}: rules drop the direction of a symbol', 'direction' not in t)
    check(f'fix 1 {band}: captions in order start, turn 1 no match, turn 2 match, flip match',
          re.search(r'start turn 1 spot: no match turn 2 spots: match flip over the dashed line: match', t) is not None)
    rings = demo_rings(p)
    kinds = [k for _, k in rings]
    centres = [c for c, _ in rings]
    start = kinds[0] if kinds else []
    turned = lambda k: start[k:] + start[:k]
    check(f'fix 1 {band}: four small rings read start 0101, turn 1, turn 2, flip',
          kinds == [[0, 1, 0, 1], turned(1), turned(2), [start[(-i) % 4] for i in range(4)]])
    check(f'fix 1 {band}: the turn 1 panel does not match and the turn 2 and flip panels do',
          len(kinds) == 4 and kinds[1] != start and kinds[2] == start and kinds[3] == start)
    dashed = [d for d in p.get_drawings() if d.get('dashes') not in (None, '[] 0') and d['items'][0][0] == 'l']
    ok = False
    if len(rings) == 4 and len(dashed) == 1:
        a, b = dashed[0]['items'][0][1], dashed[0]['items'][0][2]
        fx, fy = centres[3]
        ok = (abs(a.x / CM - fx) < .02 and abs(b.x / CM - fx) < .02
              and min(a.y, b.y) / CM < fy - 1.37 and max(a.y, b.y) / CM > fy + 1.37)
    check(f'fix 1 {band}: one dashed axis, through the flip ring\'s centre and past its top and bottom spots', ok)
    ar = arrows(p)
    check(f'could 9 {band}: three arrows, each from the start ring to a different moved copy',
          len(ar) == 3 and all(nearest(a, centres) == 0 for a, _ in ar)
          and sorted(nearest(b, centres) for _, b in ar) == [1, 2, 3])

# ------------------------------------------------------------------ the goal phrase and prompts

PHRASE = 'no turn or flip can match'
expected = {'k-1': 4, 'grades-2-3': 5, 'grades-4-5': 5}
for band in BANDS:
    d = doc(band)
    t = ' '.join(words(p) for p in d)
    for old in ('hide', 'stop every', 'stops every', 'allow a matching', 'Neighbors may match', 'Use up to three kinds'):
        check(f'fix 3/could 7 {band}: "{old}" is gone', old not in t)
    check(f'fix 3 {band}: "{PHRASE}" appears {expected[band]} times', t.count(PHRASE) == expected[band])
    check(f'fix 3 {band}: "neighbors may be the same kind" is said once', t.count('neighbors may be the same kind') == 1)
    check(f'{band}: every page has a v3 footer', all(f'W34-{band}-v3' in words(p) for p in d))

k1 = doc('k-1')
check('could 6: K-1 P1 asks "Can you make one your partner cannot match?"', 'Can you make one your partner cannot match?' in words(k1[0]))
check('fix 3: K-1 P3 asks for changes that let some turn or flip match', 'Find changes that let some turn or flip match and changes that do not.' in words(k1[1]))
g45 = doc('grades-4-5')
check('page counts 5 / 5 / 6', [len(doc(b)) for b in BANDS] == [5, 5, 6])
last = g45[len(g45) - 1]
spot_count = {}
for d in last.get_drawings():
    r = d['rect']
    if [i[0] for i in d['items']] == ['c'] * 4 and abs(r.width / CM - 2.8) < .02 and 'f' in d['type']:
        spot_count.setdefault('spots', 0)
        spot_count['spots'] += 1
gray = sorted(round(d['rect'].width / 2 / CM, 2) for d in last.get_drawings()
              if [i[0] for i in d['items']] == ['c'] * 4 and d['type'] == 's' and d['color'] and .7 < d['color'][0] < .85)
check('fix 4: 4-5 page 6 is extra workspace for Problem 5, not a numbered problem',
      'Extra workspace for Problem 5: a seven-ring and a nine-ring.' in words(last) and 'Problem 6' not in words(last))
check('fix 4: page 6 has a seven-ring and a nine-ring of full-size spots (16 spots, rings of radius 4.2 and 4.6)',
      spot_count.get('spots') == 16 and gray == [4.2, 4.6])
check('fix 4: 4-5 Problem 5 is the eight-ring general construction', 'Problem 5: Can you make a two-kind pattern that no turn or flip can match on any ring with at least six spots?' in words(g45[4]))

# ------------------------------------------------------------------ guide

g = doc('facilitator')
gt = ' '.join(words(p) for p in g)
check('guide: 6 pages, route note last', len(g) == 6 and 'Use and return choices' in words(g[5]))
check('guide: v3 footer', all('Final student packet v3' in words(p) for p in g[:5]))
check('could 10: eleven children, not ten', 'For eleven children' in gt and 'For ten children' not in gt)
check('could 10: the hour starts after the run-around, no movement break, short share',
      '0-5, after the opening run-around' in gt and '23-27' not in gt and '46-57' not in gt and '38 to the end' in gt)
check('fix 2: materials give about ten sheets per pair and coloured pencils',
      'about ten sheets of tracing paper' in gt and 'coloured pencils' in gt)
check('fix 2: guide says how to make a copy (trace, colour, fresh copy, lift)',
      all(s in gt for s in ('Making a tracing copy', 'trace each spot circle', "colour it with its counter's colour",
                            'fresh copy for each new or changed pattern', 'Lift a copy to turn or flip it')))
check('fix 2: the launch makes the copy in front of the children and shows the flip',
      'make its copy in front of the children' in gt and 'flip it over the line through two opposite spots' in gt)
check('could 8: the guide drops the backward-symbol sentence', 'face backward' not in gt)
check('fix 5: the K-1 P6 key accepts a swap of kinds', 'B B A B A A A A' in gt and 'same kinds and counts' in gt)
check('could 6: the K-1 P1 key answers the new question',
      'Can you make one your partner cannot match?” is no with two kinds' in gt)
check('fix 4: the 4-5 P5 key gives the seven- and nine-ring witnesses and says 6 through 9',
      'A A B A B B B (gaps 1, 2, 4)' in gt and 'A A B A B B B B B (gaps 1, 2, 6)' in gt and 'sizes 6 through 9' in gt)
check('status: 6 / 5 / 5 problems and the 4-5 workspace page', '6 / 5 / 5 problems; the grades 4-5 packet adds a page of extra workspace' in gt)

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
