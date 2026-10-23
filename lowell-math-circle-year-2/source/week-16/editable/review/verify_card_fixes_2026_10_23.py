#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes for Week 16.

    python3 review/verify_card_fixes_2026_10_23.py [build folder] [return-visit PDF]

Reads the student LaTeX in src/ and the built PDFs (default build/, as written by
build.sh). Checks, independently of the drawing code:
  - every blank side dot of every triangle board carries exactly the tints of the
    letters its side allows, found from the dot's position (bottom R/B, left R/Y,
    right B/Y), with all three on the K-1 Problem 6 bottom and at the Grades 4-5
    Problem 6 star, and every inside dot is plain white;
  - K-1 rings are 0.30 in across, and 3/4-inch counters fit every K-1 board;
  - the four K-1 Problem 6 record triangles fit the text width;
  - the mathematics behind the changed wording (row door counts, the relaxed bottom,
    the return visit's page-2 rule);
  - the printed wording and v3 footers.
"""
import itertools
import math
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


# ---------------------------------------------------------------- drawn boards
NUM = r'(-?[\d.]+)'
FILL = re.compile(r'\\fill\[(R|B|Y)fill\] \(' + NUM + ',' + NUM + r'\) -- \+\(' + NUM + ':' + NUM + r'in\) arc\[start angle=' + NUM + r',end angle=' + NUM)
RING = re.compile(r'\\draw\[line width=0\.8pt(,fill=white)?\] \(' + NUM + ',' + NUM + r'\) circle\[radius=' + NUM + r'in\]')
EXPECT = {'bottom': {'R', 'B'}, 'left': {'R', 'Y'}, 'right': {'B', 'Y'}}


def boards(tex):
    """Each triangle board picture: (width, rings {(x,y): (white, radius)}, fills {(x,y): set})."""
    out = []
    for pic in re.findall(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', tex, re.S):
        m = re.search(r'use as bounding box\] \(-0\.63,-0\.64\) rectangle \(' + NUM, pic)
        if not m:
            continue
        width = float(m.group(1)) - 0.63
        rings = {(float(x), float(y)): (bool(w), float(r)) for w, x, y, r in RING.findall(pic)}
        fills = {}
        for letter, x, y, _a, _r, a1, a2 in FILL.findall(pic):
            fills.setdefault((float(x), float(y)), []).append((letter, float(a1), float(a2)))
        out.append((width, rings, fills, '$*$' in pic, 'R or B or Y' in pic))
    return out


def side(x, y, w):
    h = w * math.sqrt(3) / 2
    if abs(y) < 1e-3:
        return 'bottom'
    if abs(y - math.sqrt(3) * x) < 2e-3:
        return 'left'
    if abs(y - math.sqrt(3) * (w - x)) < 2e-3:
        return 'right'
    return None


for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    tex = (ROOT / 'src' / f'{band}.tex').read_text()
    bs = boards(tex)
    nside = ninside = 0
    ok = True
    for w, rings, fills, star, whole in bs:
        for (x, y), (white, r) in rings.items():
            s = side(x, y, w)
            got = fills.get((x, y), [])
            if s is None:
                ninside += 1
                ok &= white and not got
                continue
            nside += 1
            want = set(EXPECT[s])
            if whole and s == 'bottom' or star and s == 'bottom' and abs(x - w / 2) < 1e-3:
                want = {'R', 'B', 'Y'}
            letters = {g[0] for g in got}
            span = sum(a2 - a1 for _, a1, a2 in got)
            ok &= not white and letters == want and len(got) == len(want) and abs(span - 360) < 1e-6
            # the part nearer a corner takes that corner's tint
            if len(want) == 2:
                corner = {'R': (0, 0), 'B': (w, 0), 'Y': (w / 2, w * math.sqrt(3) / 2)}
                for letter, a1, a2 in got:
                    mid = math.radians((a1 + a2) / 2)
                    toward = (corner[letter][0] - x, corner[letter][1] - y)
                    ok &= math.cos(mid) * toward[0] + math.sin(mid) * toward[1] > 0
    check(ok and nside > 0, f'{band}: {nside} side dots on {len(bs)} boards carry exactly their side\'s tints, each half facing its corner; {ninside} inside dots plain')
    if band == 'k-1':
        radii = {r for _, rings, _, _, _ in bs for (_, r) in rings.values()}
        check(radii == {0.15}, f'K-1: every ring is 0.30 in across (radii {sorted(radii)})')
        spacing = min(w / n for w, n in [(5.25, 2), (5.25, 3), (5.25, 4)])
        check(spacing >= 1.3125 - 1e-9 and spacing - 0.75 >= 0.5,
              f'K-1: tightest dot spacing {spacing:.4f} in leaves {spacing - 0.75:.2f} in between 3/4-inch counters, which cover the 0.30 in rings')
        recs = re.findall(r'circle\[radius=0\.05in\]', tex)
        xs = [float(x) for x in re.findall(r'\\draw\[line width=0\.6pt,fill=white\] \(' + NUM + r',[-\d.]+\) circle\[radius=0\.05in\]', tex)]
        check(len(recs) == 40 and max(xs) - min(xs) + 0.1 <= 7.26,
              f'K-1 Problem 6: four ten-dot record triangles, {max(xs) - min(xs) + 0.1:.2f} in wide within the 7.26 in text width')

# ---------------------------------------------------------------- mathematics
def mesh(n):
    vs = [(i, j) for j in range(n + 1) for i in range(n - j + 1)]
    ts = []
    for j in range(n):
        for i in range(n - j):
            ts.append(((i, j), (i + 1, j), (i, j + 1)))
            if i + j < n - 1:
                ts.append(((i + 1, j), (i + 1, j + 1), (i, j + 1)))
    return vs, ts


def fillings(n, bottom='RB', inside='RBY'):
    vs, ts = mesh(n)
    opts = []
    for v in vs:
        i, j = v
        o = {(0, 0): 'R', (n, 0): 'B', (0, n): 'Y'}.get(v)
        if o is None:
            o = bottom if j == 0 else 'RY' if i == 0 else 'BY' if i + j == n else inside
        opts.append(o)
    for c in itertools.product(*opts):
        col = dict(zip(vs, c))
        yield sum(set(col[v] for v in t) == set('RBY') for t in ts)


# Grades 4-5 Problem 4: "Which numbers of doors can each row have?"
for ends, edges in [('RB', 3), ('RR', 4), ('RB', 5), ('RR', 6), ('RB', 7)]:
    counts = set()
    for mid in itertools.product('RB', repeat=edges - 1):
        row = ends[0] + ''.join(mid) + ends[1]
        counts.add(sum(a != b for a, b in zip(row, row[1:])))
    want = set(range(1 if ends == 'RB' else 0, edges + 1, 2))
    check(counts == want, f'4-5 P4: a {ends[0]}...{ends[1]} row of {edges} edges can have exactly {sorted(counts)} doors (every count of one parity)')
dist = {}
for k in fillings(3, bottom='RBY'):
    dist[k] = dist.get(k, 0) + 1
check(dist.get(0, 0) > 0, f'K-1 P6: with the bottom allowing Y, {dist.get(0, 0)} fillings have no R-B-Y triangle, so four different records exist')
check(min(fillings(3)) == 1, 'K-1 P2 unchanged: with the side rules kept every three-step filling has at least one')
zero = sum(k == 0 for k in fillings(3, inside='RBYG'))
check(zero == 27, f'return visit P2: with side dots on their corner letters and the middle dot R, B, Y or G, {zero} of 256 fillings have no R-B-Y triangle')

# ---------------------------------------------------------------- printed wording
def text(pdf):
    return ' '.join(' '.join(p.get_text().split()) for p in pymupdf.open(pdf))

t = {b: text(BUILD / f'{b}.pdf') for b in ('k-1', 'grades-2-3', 'grades-4-5')}
for b, tag in (('k-1', 'K'), ('grades-2-3', '23'), ('grades-4-5', '45')):
    n = len(pymupdf.open(BUILD / f'{b}.pdf'))
    check(t[b].count(f'F16-{tag}-v3') == n and '-v2' not in t[b], f'{b}: {n} F16-{tag}-v3 footers')
for b in ('grades-2-3', 'grades-4-5'):
    check(t[b].count('Problem 1:') == 1 and 'Another board for Problem 1.' in t[b], f'{b}: page 2 reads "Another board for Problem 1." and Problem 1 is printed once')
check('Which numbers of doors can each row have? Explain your answer for rows of any length.' in t['grades-4-5']
      and 'must have an odd' not in t['grades-4-5'], '4-5 P4 asks which numbers of doors each row can have')
check('Draw all the routes. Can every route from outside return outside?' in t['grades-4-5']
      and 'stay inside the big triangle' not in t['grades-4-5'], '4-5 P2 no longer mentions routes that stay inside')
check('Which outside doors lead back outside?' in t['grades-2-3'] and 'entrances' not in t['grades-2-3'], '2-3 P2 asks about outside doors')
if len(sys.argv) > 2:
    rv = pymupdf.open(sys.argv[2])
    p2 = ' '.join(rv[1].get_text().split())
    check("Side dots use that side's corner letters. The middle dot may be R, B, Y or G." in p2.replace('’', "'")
          and ' '.join(p.get_text() for p in rv).count('W16-RV-v2') == len(rv), 'return visit: page 2 states its rule; W16-RV-v2 footers')

print('\nFAILS: ' + (', '.join(fails) if fails else 'none'))
sys.exit(1 if fails else 0)
