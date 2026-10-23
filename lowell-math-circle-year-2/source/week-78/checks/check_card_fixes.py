#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes for Week 78 (plans/review/week-78.md).

Reads the problem files, student/data.py and guide/facilitator.tex (no TeX needed), so it
runs with the other checks in build-manifest.json. Every claim the fixes added or changed is
recomputed here with exact fractions over a fine grid of junctions and points; the all-real
proofs are on guide page 4. Every line printed starts with PASS; a failure stops with an error.
"""
import ast
import re
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = []


def ok(cond, msg):
    if not cond:
        sys.exit('FAIL: ' + msg)
    out.append('PASS: ' + msg)


def on_line(p, j):
    """p lies on the three-armed line with junction j: the least of x-a, y-b, 0 is tied."""
    v = (p[0] - j[0], p[1] - j[1], 0)
    return v.count(min(v)) >= 2


data = {}
for node in ast.parse((ROOT / 'student' / 'data.py').read_text()).body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
        data[node.targets[0].id] = ast.literal_eval(node.value)
problems = {f.name: f.read_text() for f in sorted((ROOT / 'problems').glob('*.md'))}
guide = ' '.join((ROOT / 'guide' / 'facilitator.tex').read_text().split())
GRID = [F(i, 4) for i in range(-16, 65)]            # -4 to 16 in quarters
POINTS = list(product(GRID, repeat=2))

# Fix 5: P2's and P4's first pair is (2,6)/(6,2), on a falling diagonal.
a, b = data['INTERSECTION_PAIRS'][0]
ok((a, b) == ((2, 6), (6, 2)) and data['INVERSE_GENERAL'][0] == ((2, 6), (6, 2)), 'Problems 2 and 4 open with (2,6) and (6,2)')
shared = [p for p in POINTS if on_line(p, a) and on_line(p, b)]
ok(shared == [(6, 6)], f'P2: the lines with junctions (2,6) and (6,2) share only (6,6) among {len(POINTS)} quarter-grid points')
ok(a[0] - a[1] != b[0] - b[1] and a[0] + a[1] == b[0] + b[1], 'the pair is on a falling diagonal, not a rising one')
works = [j for j in POINTS if on_line(a, j) and on_line(b, j)]
ok(works == [(2, 2)], 'P4: only junction (2,2) puts both (2,6) and (6,2) on one line')
ok('$(2,6)$ and $(6,2)$ & One point, $(6,6)$: a falling diagonal shares no ray' in guide and '$P=(2,6)$, $Q=(6,2)$ force junction $(2,2)$' in guide,
   'guide keys for P2 and P4 give (6,6) and (2,2)')

# Fix 1: the child explanation names the rising diagonal.
ok('same row, column or rising diagonal, the matching arms keep sharing forever' in guide, 'guide P3: "same row, column or rising diagonal"')
falling = [p for p in POINTS if on_line(p, (2, 6)) and on_line(p, (6, 2))]
rising = [p for p in POINTS if on_line(p, (2, 2)) and on_line(p, (6, 6))]
ok(len(falling) == 1 and len(rising) > 1, 'junctions on a falling diagonal share one point; on a rising diagonal, a whole ray')

# Fix 2: P5 no longer prints that a stretch can be the answer; the guide's hint does.
p5 = problems['05-all-junctions.md']
ok('Mark a whole stretch' not in p5 and 'Find all possible junctions of a line through each pair of points.' in p5, 'P5 asks only for all possible junctions')
ok('a whole stretch of junctions can be the answer' in guide, 'guide P5 hint 2 says a whole stretch can be the answer')

# Fix 3: one traced three-arm shape per pair, used in the launch and in P4's first hint.
ok('one traced three-arm shape' in guide and 'three traced shapes' in guide and 'about 12\\,cm long' in guide
   and "Put the traced shape's junction at $(2,2)$" in guide and 'slide the shape, without turning it, to $(3,2)$' in guide
   and 'Slide the traced shape. Can one unchanged shape touch both targets?' in guide and 'Optional: two tracing sheets' not in guide,
   'guide: a traced shape per pair is standard, made in preparation and used in the launch and P4')
# 12 cm arms reach across every printed board: 8 squares at the largest board scale, even corner to corner.
scales = [float(x) for x in re.findall(r'\\board\{([\d.]+)\}', ''.join(problems.values()))]
scales += [float(x) for x in re.findall(r", (\.\d+), '(?:junction|target)'", (ROOT / 'figures.py').read_text())]
ok(len(scales) == 7 and max(scales) * 8 * 2 ** .5 < 12,
   f'a 12 cm arm crosses every printed board (largest {max(scales) * 8:.1f} cm wide, {max(scales) * 8 * 2 ** .5:.1f} cm corner to corner)')

# Fix 4: the adult-led younger entry and its plain-words key, on page 4's boards.
one_dot = [j for j in POINTS if on_line((2, 6), j)]
p5_left = data['INVERSE_ALIGNED'][0]
row = [j for j in POINTS if on_line(p5_left[0], j) and on_line(p5_left[1], j)]
ok(len(one_dot) > 50 and row == [j for j in POINTS if j[1] == 4 and j[0] <= 2],
   f'one dot allows many junctions ({len(one_dot)} on the quarter grid); P5 left (2,4),(6,4) allows exactly the row y = 4 left of P')
ok('A younger entry, adult-led' in guide and "on Problem 4's left board only one place works, $(2,2)$" in guide
   and "on Problem 5's left board the junction can slide anywhere along the row to the left of $P$" in guide
   and 'no K--1 or Grades 2--3 route' not in guide, 'guide p. 1: younger entry with a plain-words key, no new pages')

# Coulds 6 and 9: P3 has a blank 0-8 board; Q is a cross on page 1.
ok('\\board{.58}{}{}' in problems['03-two-points.md'], 'P3 has a blank 0-8 board beside its answer space')
intro = problems['00-intro.md']
ok('(3.82,3.82)--(4.18,4.18)' in intro and 'circle[radius=2.4pt]' not in intro, 'page 1 marks the off-line point Q with a cross, not a target circle')
ok(not on_line((4, 4), (2, 2)) and on_line((4, 2), (2, 2)), 'Q = (4,4) is off the line with junction (2,2); P = (4,2) is on it')

# Versions.
toml = (ROOT / 'week.toml').read_text()
ok('version = "v3"' in toml and 'F78-FAC-v3' in guide, 'student packet F78-S-v3 and guide F78-FAC-v3')
print('\n'.join(out))
