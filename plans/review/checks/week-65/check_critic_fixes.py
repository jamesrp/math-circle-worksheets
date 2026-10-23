#!/usr/bin/env python3
"""Check the Week 65 critic follow-up (Critic C shoulds 8-9, coulds 10-11) in the print PDFs.

Usage: python3 plans/review/checks/week-65/check_critic_fixes.py   (from the repository root)

Builds the {8,4} tiling on its own (reflections of the central right-angled octagon in the
Poincare disk, deduplicated by centre), then checks:
  - the guide's turning rule: around n rooms whose outside walk encloses only those rooms,
    left minus right quarter-turns is 4 + 4n; the ring of Home's 16 surrounding rooms has a
    simple outside walk but encloses Home too, and gives 72 = 4 + 4*17, not 68;
  - Problem 6: Home's 8 side neighbours and 8 corner rooms, the 5 off-map doors of each
    neighbour leading to 40 different rooms, so 40 + 8 = 48 rooms two crossings away;
  - the printed page 7 draws exactly those 17 rooms (112 walls) beside the 5-by-5 square floor;
  - the guide's wording, and v4 footers with no other change to student pages 1-6.
"""
from collections import Counter
from math import sqrt, pi
from pathlib import Path
import cmath
import difflib
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / 'lowell-math-circle-year-2/week-65'
A = P / 'archive-before-critic-fixes-2026-10-23'

R0 = sqrt(sqrt(2) - 1)                       # circumradius of the right-angled octagon in the disk
V = [R0 * cmath.exp(1j * (pi / 8 + k * pi / 4)) for k in range(8)]


def reflect(z, p, q):
    """Inversion in the circle through p and q orthogonal to the unit circle."""
    det = p.real * q.imag - p.imag * q.real
    a, b = (abs(p) ** 2 + 1) / 2, (abs(q) ** 2 + 1) / 2
    c = complex((a * q.imag - p.imag * b) / det, (p.real * b - a * q.real) / det)
    return c + (abs(c) ** 2 - 1) / (z - c).conjugate()


def k(z):
    return (round(z.real, 7), round(z.imag, 7))


rooms, where = [(0j, V, 0)], {k(0j): 0}
for c, poly, d in rooms:
    if d == 3:
        continue
    for i in range(8):
        p, q = poly[i], poly[(i + 1) % 8]
        z = reflect(c, p, q)
        if k(z) not in where:
            where[k(z)] = len(rooms)
            rooms.append((z, [reflect(w, p, q) for w in poly], d + 1))
walls = {}
for r, (_, poly, _) in enumerate(rooms):
    for i in range(8):
        walls.setdefault(frozenset((k(poly[i]), k(poly[(i + 1) % 8]))), set()).add(r)
door = {r: set() for r in range(len(rooms))}
for rs in walls.values():
    if len(rs) == 2:
        a, b = rs
        door[a].add(b)
        door[b].add(a)
layer = Counter(d for _, _, d in rooms)
assert (layer[0], layer[1], layer[2]) == (1, 8, 48)

HOME = 0
nbrs = sorted(door[HOME])
home_v = {k(z) for z in V}
corners = sorted(r for r, (_, poly, _) in enumerate(rooms)
                 if r != HOME and r not in nbrs and any(k(z) in home_v for z in poly))
assert len(nbrs) == 8 and len(corners) == 8
assert all(len(door[c] & set(nbrs)) == 2 for c in corners)
drawn = {HOME, *nbrs, *corners}
off = [r for n in nbrs for r in door[n] if r not in drawn]
assert all(len(door[n]) == 8 and len(door[n] & set(corners)) == 2 for n in nbrs)
assert len(off) == 40 and len(set(off)) == 40
assert set(off) | set(corners) == {r for r, (_, _, d) in enumerate(rooms) if d == 2}
print('PASS Problem 6: each of Home\'s 8 neighbours has 1 door to Home, 2 to corner rooms and 5 off the map; '
      'the 40 off-map rooms are all different, so 40 + 8 = 48 rooms are two crossings away (layers 1, 8, 48).')


def outer_turns(cluster, skip=()):
    """Left and right quarter-turns on the outside walk: a corner in 1 cluster room turns left, in 3 right."""
    at = Counter(k(z) for r in cluster for z in rooms[r][1])
    left = sum(1 for v, c in at.items() if c == 1 and v not in skip)
    right = sum(1 for v, c in at.items() if c == 3 and v not in skip)
    return left, right


A_, B_ = nbrs[0], next(n for n in nbrs if len(door[n] & door[nbrs[0]] & set(corners)) == 1 and n != nbrs[0])
star = (door[A_] & door[B_] & set(corners)).pop()
for cluster, want in (([HOME], (8, 0)), ([HOME, A_], (12, 0)), ([HOME, A_, star], (17, 1))):
    got = outer_turns(cluster)
    assert got == want and got[0] - got[1] == 4 + 4 * len(cluster), (cluster, got)
ring = nbrs + corners
L, Rt = outer_turns(ring, skip=home_v)       # Home's 8 corners are on the inner walk, around the hole
assert (L - Rt) == 72 == 4 + 4 * 17 != 4 + 4 * len(ring)
assert outer_turns(ring + [HOME]) == (L, Rt)
print(f'PASS turning rule: 1, 2 and 3 rooms (Home, A, star) give 8, 12 and 17 - 1 = 16 = 4 + 4n; the ring of '
      f'{len(ring)} rooms around Home has outside turns {L} left and {Rt} right, {L - Rt} = 4 + 4*17, not '
      f'{4 + 4 * len(ring)}, because its outside walk also encloses Home.')


def N(s):
    return re.sub(r'\s+', ' ', s.replace('−', '-')).strip()


st = pymupdf.open(P / 'week-65-students.pdf')
old = pymupdf.open(A / 'week-65-students.pdf')
assert len(st) == len(old) == 7
for i in range(6):
    a, b = N(st[i].get_text()), N(old[i].get_text())
    assert 'W65-S-v4' in a and a.replace('W65-S-v4', 'W65-S-v3') == b, (i + 1, list(difflib.ndiff([b], [a]))[:3])
t7 = N(st[6].get_text())
assert ('Problem 6: On this octagon floor every room has 8 doors. Only the rooms around Home are drawn; the floor '
        'goes on. How many rooms can you reach from Home in 2 door crossings but not fewer? How many on this square '
        'floor, where every room has 4 doors?') in t7
assert t7.count('Home') == 4 and 'Octagon floor:' in t7 and 'Square floor:' in t7 and 'W65-S-v4' in t7
MM = 25.4 / 72
draws = st[6].get_drawings()
curved = [d for d in draws if d.get('color') and any(it[0] == 'c' for it in d['items'])]
straight = [d for d in draws if d.get('color') and all(it[0] == 'l' for it in d['items'])]
assert len(curved) == 112, len(curved)        # 17 rooms x 8 walls - 8 Home walls shared - 16 neighbour/corner walls shared
xs = [p for d in curved for p in (d['rect'].x0, d['rect'].x1)]
ys = [p for d in curved for p in (d['rect'].y0, d['rect'].y1)]
sq = [d['rect'] for d in straight if abs(max(d['rect'].width, d['rect'].height) * MM - 5 * .45 * 25.4) < .2]
assert len(sq) == 12 and len(straight) == 14   # the floor's 6 + 6 lines and the two answer rules
assert max(xs) < min(r.x0 for r in sq) and min(xs) * MM > 15.7
print(f'PASS page 7: the octagon map draws 112 walls, the 17 rooms Home, 8 neighbours and 8 corner rooms '
      f'({(max(xs) - min(xs)) * MM:.0f} mm across, left of the 5-by-5 square floor of 11.4 mm cells); pages 1-6 '
      'differ from the archived v3 only in the footer, W65-S-v4.')

g = pymupdf.open(P / 'week-65-facilitator.pdf')
assert len(g) == 7 and all('W65-FAC-v4' in p.get_text() for p in g)
gt = N(' '.join(p.get_text() for p in g))
for need in ('does not touch itself and encloses only those n rooms', 'The 16 rooms around Home enclose Home too: 72, not 68.',
             'Problem 6 uses 8×7 or 8×5 + 8.', 'dot the unmarked corners first',
             'each neighbor’s doors are one to Home, two to the corner rooms drawn beside it and five off the map',
             'the student builder checks that the 40 rooms behind them are all different'):
    assert N(need).replace(' ', '') in gt.replace(' ', ''), need
assert 'the checked local geometry has no further overlaps' not in gt
print('PASS guide: seven pages, W65-FAC-v4; the rule says the walk encloses only those n rooms (ring: 72, not 68); '
      'readiness names Problem 6\'s 8 x 7 or 8 x 5 + 8; the third case dots the corners first; the Problem 6 key '
      'reads the doors off the map.')
