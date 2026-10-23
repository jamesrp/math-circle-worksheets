"""Check of the Week 61 review card's fixes, October 23, 2026 (W61-S-v4, W61-F-v3).

Areas come from the Van Oosterom-Strackee solid angle and the cap formula, never from
Girard's rule; corners from tangent vectors. Constructions (from_angles, meridian,
side_view) are imported from the package's geometry.py only to place points. With the
PDFs it checks the printed wording, the p. 5 example's geometry against a 70-70-70 and an
80-80-80 triangle, the label boxes on p. 5, and every changed guide statement.

Run: python3 check_card_fixes.py [students.pdf facilitator.pdf]
     (default: the print copies in lowell-math-circle-year-2/week-61/; writes
     out_check_card_fixes.txt beside itself)
"""
import itertools
import math
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'lowell-math-circle-year-2/source/week-61/editable/student'))
sys.dont_write_bytecode = True
from geometry import from_angles, meridian, side_view  # noqa: E402

PDF_S = sys.argv[1] if len(sys.argv) > 2 else os.path.join(ROOT, 'lowell-math-circle-year-2/week-61/week-61-students.pdf')
PDF_G = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'lowell-math-circle-year-2/week-61/week-61-facilitator.pdf')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok ' + msg)


def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def unit(a): n = math.sqrt(dot(a, a)); return tuple(x / n for x in a)


def solid_fraction(a, b, c):
    """Fraction of the sphere inside the convex triangle abc (Van Oosterom-Strackee)."""
    num = abs(dot(a, cross(b, c)))
    den = 1 + dot(a, b) + dot(b, c) + dot(c, a)
    return 2 * math.atan2(num, den) / (4 * math.pi)


def corner(a, b, c):
    tb = unit(tuple(x - dot(a, b) * y for x, y in zip(b, a)))
    tc = unit(tuple(x - dot(a, c) * y for x, y in zip(c, a)))
    return math.degrees(math.acos(max(-1, min(1, dot(tb, tc)))))


def text(pdf):
    # The degree glyph extracts as U+25E6 and with no space before a following word.
    return [re.sub(r'°(?=[A-Za-z0-9(])', '° ', re.sub(r'\s+', ' ', p.get_text().replace('◦', '°'))) for p in pymupdf.open(pdf)]


S, G = text(PDF_S), text(PDF_G)
GA = ' '.join(G)

# Versions.
ok(len(S) == 7 and all('W61-S-v4' in p for p in S), 'student packet: 7 pages, every footer W61-S-v4')
ok(len(G) == 9 and all(('W61-F-v3' in p) or ('W61-F-v4' in p) for p in G), 'guide: 9 pages, every footer W61-F-v3 (W61-F-v4 after the critic follow-up)')

# Should 2, p. 1: the rule no longer answers Problem 1.
ok('A shortest surface route between two points runs along a great circle through them.' in S[0]
   and 'not opposite, its shorter arc' not in S[0], 'p. 1 rule: "runs along a great circle through them", no uniqueness claim (should 2)')
for az in (0, 35, 90):   # opposite points: many semicircles of length pi
    h = math.radians(az)
    vs = [(math.sin(math.pi * j / 180) * math.cos(h), math.sin(math.pi * j / 180) * math.sin(h), math.cos(math.pi * j / 180)) for j in range(181)]
    assert abs(sum(math.acos(max(-1, min(1, dot(a, b)))) for a, b in zip(vs, vs[1:])) - math.pi) < 1e-9
ok(True, 'P1 answer unchanged: opposite points have equal semicircle routes of length pi through different meridians')

# Should 3, p. 2: the smaller region is the convex one, so "smaller region" implies corners below 180.
ok('Use the smaller region inside the three sides.' in S[1] and 'straight angle' not in S[1] and 'angle meter' not in S[1],
   'p. 2 rules: "Use the smaller region inside the three sides."; no straight-angle or angle-meter sentence (should 3)')
import random
rnd = random.Random(61)
worst = 0
for _ in range(2000):
    v = [unit((rnd.gauss(0, 1), rnd.gauss(0, 1), rnd.gauss(0, 1))) for _ in range(3)]
    if abs(dot(v[0], cross(v[1], v[2]))) < 1e-3 or min(1 + dot(a, b) for a, b in itertools.combinations(v, 2)) < 1e-3:
        continue
    f = solid_fraction(*v)
    assert 0 < f < .5 and all(corner(v[i], v[(i + 1) % 3], v[(i + 2) % 3]) < 180 for i in range(3))
    worst = max(worst, f)
ok(worst < .5, 'for 2000 random allowed triples the convex region (all corners < 180) is the smaller one, area < 1/2')
oct_ = meridian(90)
ok(abs(solid_fraction(*oct_) - 1 / 8) < 1e-12 and all(abs(corner(oct_[i], oct_[(i + 1) % 3], oct_[(i + 2) % 3]) - 90) < 1e-9 for i in range(3)),
   'P2 and P3 triangles with corners on the equator still obey the new rule: the octant is the smaller region, 1/8')

# Could 11, p. 3.
ok('Its corner with the equator is a right angle.' not in S[2] and 'Problem 3:' in S[2], 'p. 3: the right-angle sentence is cut (could 11)')

# Should 7, p. 4: gaps 45, 60, 120.
p4 = {g: solid_fraction(*meridian(g)) for g in (45, 60, 120)}
ok('gaps 45°, 60°, and 120°' in S[3] and '72' not in S[3]
   and all(abs(p4[g] - want) < 1e-12 for g, want in ((45, 1 / 16), (60, 1 / 12), (120, 1 / 6))),
   'P4 gaps 45, 60, 120 degrees; triangle fractions 1/16, 1/12, 1/6 by solid angle (should 7)')
ok(all(g % 15 == 0 for g in (45, 60, 120)) and 72 % 15 != 0, 'all three gaps lie on a 15-degree globe grid, which 72 did not')

# Should 4, P7.
ok('Use it for these three triangles. Explain why your rule works for every triangle under our rules.' in S[6]
   and 'persist' not in S[6] and 'opposite triangles' not in S[6], 'P7 asks for the rule and its explanation, without the proof plan (should 4)')
ok('the covering counts are the same for every triangle under our rules, and opposite triangles have equal area' in GA,
   'guide p. 8 hint holds the two steps (should 4)')

# Should 5, p. 5: the example is a 70-70-70 triangle, not Problem 6's 80-80-80.
t70, t80 = from_angles(70, 70, 70), from_angles(80, 80, 80)
c70 = [corner(t70[i], t70[(i + 1) % 3], t70[(i + 2) % 3]) for i in range(3)]
ok(all(abs(c - 70) < 1e-9 for c in c70) and abs(solid_fraction(*t70) - 1 / 24) < 1e-12,
   'the p. 5 example triangle has corners 70, 70, 70 and covers 1/24; no problem uses it (P6 is 80-80-80, P7 60-60-90, 80s, 100s)')
page = pymupdf.open(PDF_S)[4]
R = .62 * 72
discs = sorted({(round((d['rect'][0] + d['rect'][2]) / 2, 1), round((d['rect'][1] + d['rect'][3]) / 2, 1)) for d in page.get_drawings()
                if abs((d['rect'][2] - d['rect'][0]) - 2 * R) < 1.5 and abs((d['rect'][3] - d['rect'][1]) - 2 * R) < 1.5})
ok(len(discs) == 4, 'p. 5 has four example balls of radius 0.62 in')
cx, cy = discs[0]
words = page.get_text('words')
def label(t): return [w for w in words if w[4] == t and cx - R - 15 < (w[0] + w[2]) / 2 < cx + R + 15 and cy - R - 15 < (w[1] + w[3]) / 2 < cy + R + 15]
dots = [((d['rect'][0] + d['rect'][2]) / 2, (d['rect'][1] + d['rect'][3]) / 2) for d in page.get_drawings()
        if d.get('fill') and abs(d['rect'][2] - d['rect'][0] - .04 * R) < .3 and math.hypot((d['rect'][0] + d['rect'][2]) / 2 - cx, (d['rect'][1] + d['rect'][3]) / 2 - cy) < R + 1]
a_dot = [p for p in dots if math.hypot(p[0] - cx, p[1] - cy) < .9 * R]
ok(len(a_dot) == 1, 'panel "Corner A" has one front vertex dot, A')
ax, ay = (a_dot[0][0] - cx) / R, (cy - a_dot[0][1]) / R
def proj(t):
    v = side_view(t); return v.p(t[0])
p70, p80 = proj(t70), proj(t80)
ok(math.hypot(ax - p70[0], ay - p70[1]) < .01 and math.hypot(ax - p80[0], ay - p80[1]) > .05,
   f'printed A sits at ({ax:.3f}, {ay:.3f}) ball radii: the 70-70-70 view ({p70[0]:.3f}, {p70[1]:.3f}), not P6\'s ({p80[0]:.3f}, {p80[1]:.3f})')

# Could 9, p. 5: the A and A* label boxes sit beside their dots and cross no drawn line.
strokes = []
for d in page.get_drawings():
    if d['type'] in ('s', 'fs') and d.get('color') is not None:
        for it in d['items']:
            pts = [it[1], it[-1]] if it[0] == 'l' else ([it[1], it[2], it[3], it[4]] if it[0] == 'c' else [])
            if it[0] == 'c':
                p0, p1, p2, p3 = pts
                pts = [((1 - s) ** 3 * p0.x + 3 * (1 - s) ** 2 * s * p1.x + 3 * (1 - s) * s * s * p2.x + s ** 3 * p3.x,
                        (1 - s) ** 3 * p0.y + 3 * (1 - s) ** 2 * s * p1.y + 3 * (1 - s) * s * s * p2.y + s ** 3 * p3.y) for s in [k / 20 for k in range(21)]]
            elif it[0] == 'l':
                pts = [(it[1].x + (it[2].x - it[1].x) * k / 20, it[1].y + (it[2].y - it[1].y) * k / 20) for k in range(21)]
            strokes += pts
checked = 0
for t in ('A', 'A∗'):
    for w in [w for w in words if w[4] in (t, t.replace('∗', '*'))
              and any(math.hypot((w[0] + w[2]) / 2 - x, (w[1] + w[3]) / 2 - y) < R for x, y in discs)]:
        x0, y0, x1, y1 = w[0] + .8, w[1] + 1.5, w[2] - .8, w[3] - 1.5
        hits = [p for p in strokes if x0 < p[0] < x1 and y0 < p[1] < y1]
        assert not hits, (t, w[:4], hits[:3])
        checked += 1
ok(checked == 4, 'p. 5: the labels A (three panels) and A* (back panel) sit beside their dots and no drawn line crosses them (could 9)')

# Guide statements.
ok('non-task 70° example' in GA and 'non-task triangle with three 70° corners' in GA, 'guide pp. 3 and 5 call the 70-degree example non-task, truly (should 5)')
ok('P1–4 for each of the seven older children = 28' in GA and 'P5–7 for the upper trio = 9 sheets' in GA and 4 * 7 + 3 * 3 == 37,
   'guide p. 2 prints P1-4 for all seven older children and P5-7 for the trio on the first visit: 28 + 9 = 37 sheets (should 6)')
ok('45,60,120' in GA.replace(' ', '') and 'rough marks suffice' in GA and '72' not in G[1], 'guide p. 2 kit: 45, 60, 120 references, rough marks suffice (should 7)')
ok('60° & 6' not in GA and re.search(r'60°\s*6\s*1/6\s*1/12', GA) is not None, 'guide P4 key row: 60 degrees, 6 lunes, 1/6, 1/12')
# Should 8: outside our rules.
complement = 1 - solid_fraction(*oct_)
rule = lambda s: (s - 180) / 720
long_side = {g: ((360 - g) / 360) / 2 for g in (60, 110)}       # northern half of the complementary lune
lat = math.radians(30); cap_quarter = (1 - math.sin(lat)) / 2 / 4
ok('Outside our rules.' in GA and 'Counterexamples' not in GA and 'This proof does not cover' in G[0]
   and abs(complement - rule(810)) < 1e-12 and all(abs(long_side[g] - rule(360 - g + 180)) < 1e-12 for g in long_side)
   and abs(cap_quarter - 1 / 16) < 1e-12 and abs(rule(270) - 1 / 8) < 1e-12,
   'guide p. 8 "Outside our rules": the rule gives the complement 7/8 and the long-side triangle (360-g)/720 correctly; '
   'only the 30-degree latitude triangle fails (1/16, rule 1/8); p. 1 says "This proof does not cover" (should 8)')
# Could 10: cells 1 and 2 of the 80-degree map make the lune at C.
A_, B_, C_ = t80
cells = {}
for s in itertools.product((1, -1), repeat=3):
    cells[s] = solid_fraction(*(tuple(k * x for x in v) for k, v in zip(s, t80)))
ok(abs(cells[(1, 1, 1)] - 1 / 12) < 1e-12 and abs(cells[(1, 1, -1)] - 5 / 36) < 1e-12
   and abs(cells[(1, 1, 1)] + cells[(1, 1, -1)] - 2 / 9) < 1e-12 and 'together make the 80° lune at C, which is 2/9 of the ball' in GA,
   'guide p. 6 hint: cells 1 (+++) and 2 (++-) are the 80-degree lune at C, 1/12 + 5/36 = 2/9 (could 10)')
# Should 1: the K-1 route and its plain-words key.
ok('Plain-words key:' in GA and 'three straws on the table' in G[2] and 'six drinking straws' in G[1]
   and all(abs(corner(oct_[i], oct_[(i + 1) % 3], oct_[(i + 2) % 3]) - 90) < 1e-9 for i in range(3)) and 90 + 90 + 0 == 180,
   'guide p. 3 K-1 route: opposite dots, three square corners on the ball (the octant) but not on the table '
   '(two right angles already use the flat 180), straws in the K-1 kit (should 1)')

with open(os.path.join(HERE, 'out_check_card_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\nPASS: {len(OUT)} checks\n')
print('\n'.join(OUT)); print(f'PASS: {len(OUT)} checks')
