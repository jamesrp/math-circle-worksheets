#!/usr/bin/env python3
"""Check the October 23, 2026 card fix of the Week 22 bonus (T moved to (16/5, 17/5)).

Run from the package folder after `python3 build.py --out build`, or pass the folder
holding week-22-bonus.pdf and week-22-bonus-facilitator.pdf:

    python3 review/verify_card_fix_2026_10_23.py [folder]

Exact rational geometry on the printed coordinates; standard library plus PyMuPDF.
"""
import json
import re
import sys
from fractions import Fraction as F
from itertools import combinations
from math import hypot
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'build'
fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


tex = (ROOT / 'student-src' / 'bonus.tex').read_text()
board = tex.split(r'\problem{1}')[1].split(r'\problem{2}')[0]
mm = float(re.search(r'x=([\d.]+)mm,y=([\d.]+)mm', board).group(1))
tx, ty = re.search(r'\\draw\[very thick\] \(([\d.]+),([\d.]+)\) circle \(3pt\)', board).groups()
T = (F(tx), F(ty))
check(T == (F(16, 5), F(17, 5)) and r'\node[font=\small,right] at (3.32,3.4){T};' in board, 'P1: T printed at (3.2, 3.4), label beside it')
names = 'ABCDEF'
P = [(F(x), F(y)) for x, y in ((1, 0), (5, 0), (8, 2), (7, 6), (3, 7), (0, 3))]
check(r'{1/0/A,5/0/B,8/2/C,7/6/D,3/7/E,0/3/F}' in tex, 'P1: the six dots are unchanged')


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def seg_dist(p, a, b):
    dx, dy = float(b[0] - a[0]), float(b[1] - a[1])
    t = max(0.0, min(1.0, (float(p[0] - a[0]) * dx + float(p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
    return hypot(float(p[0] - a[0]) - t * dx, float(p[1] - a[1]) - t * dy)


dists = sorted((seg_dist(T, P[a], P[b]) * mm, names[a] + names[b]) for a, b in combinations(range(6), 2))
check(all(orient(P[a], P[b], T) for a, b in combinations(range(6), 2)), 'P1: T lies on none of the fifteen joining lines')
check(dists[0][0] > 12.85, f'P1: T is about 12.9 mm or more from every joining segment (closest {dists[0][1]}, {dists[0][0]:.2f} mm; was 1.3 mm from BE)')
check(min(hypot(float(T[0] - p[0]), float(T[1] - p[1])) for p in P) * mm > 20, 'P1: T is far from every dot')
tri = []
for ids in combinations(range(6), 3):
    a, b, c = (P[i] for i in ids)
    s = [orient(a, b, T), orient(b, c, T), orient(c, a, T)]
    if all(v > 0 for v in s) or all(v < 0 for v in s):
        tri.append(''.join(names[i] for i in ids))
check(tri == ['ABE', 'ACE', 'ADE', 'ADF', 'BDF', 'BEF', 'CDF', 'CEF'], f'P1: T lies strictly inside the same eight triangles: {", ".join(tri)}')
w = (F(2, 5), F(2, 5), F(1, 5))
check(sum(w) == 1 and all(v > 0 for v in w) and tuple(sum(c * P[i][k] for c, i in zip(w, (1, 4, 5))) for k in (0, 1)) == T,
      'guide: T = (2/5)B + (2/5)E + (1/5)F')

S = [p.get_text() for p in pymupdf.open(OUT / 'week-22-bonus.pdf')]
G = [p.get_text() for p in pymupdf.open(OUT / 'week-22-bonus-facilitator.pdf')]
g = ' '.join(' '.join(G).split())
check(len(S) == 5 and all('W22-BON-v2' in p for p in S), 'student: five pages, every footer W22-BON-v2')
check(len(G) == 5 and all('W22-BON-FAC-v2' in p for p in G), 'guide: five pages, every footer W22-BON-FAC-v2')
check('T=(16/5,17/5)' in g and 'BEF contains T: T=(2/5)B+(2/5)E+(1/5)F' in g and 'T=(4,16/5)' not in g and 'CEF contains T' not in g,
      'guide P1: new coordinates and containing triangle')
print(json.dumps({'checks_failed': len(fails)}))
sys.exit(1 if fails else 0)
