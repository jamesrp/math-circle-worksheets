#!/usr/bin/env python3
"""Check the Week 73 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-73-students.pdf and week-73-facilitator.pdf (default: the print
folder). Needs PyMuPDF. The new key claims (the 8-by-1 target, the centered fan as
(x/2, 2y), A-D as the lower bound, the doubling strip on A-D) are recomputed here
with exact fractions; the printed pages are read for the changes, and pages 1-3 are
compared with the version 1 PDFs archived beside the print folder.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import random
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PRINT = ROOT / 'lowell-math-circle-year-2' / 'week-73'
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else PRINT
OLD = PRINT / 'archive-before-card-fixes-2026-10-23'
if not (OLD / 'week-73-students.pdf').exists() and FOLDER.resolve() != PRINT.resolve():
    OLD = PRINT  # before the release, the print folder still holds version 1
FAILS = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


# ------------------------------------------------------------------ mathematics
def d2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


rng = random.Random(73)
pts = [(F(rng.randint(0, 400), 100), F(rng.randint(0, 100), 100)) for _ in range(300)]
pairs = [(p, q) for p, q in zip(pts, pts[1:]) if p != q]

# fix 2: the 8-by-1 target
rule81 = lambda p: (2 * p[0], p[1])
check('fix 2: (2x, y) stretches no sampled pair by more than 2, and (2p)^2 + q^2 <= 4(p^2 + q^2) always',
      all(d2(rule81(p), rule81(q)) <= 4 * d2(p, q) for p, q in pairs)
      and all((2 * a) ** 2 + b ** 2 <= 4 * (a * a + b * b) for a, b in product(range(-9, 10), repeat=2)))
check('fix 2: the bottom corners, 4 apart, land on the new bottom corners 8 apart (stretch exactly 2)',
      d2((0, 0), (4, 0)) == 16 and d2(rule81((0, 0)), rule81((4, 0))) == 64)
check('fix 2: 8 by 1 has optimum max(8/4, 1) = 2 decided by the width; 6 by 2 has max(6/4, 2) = 2 decided by the height',
      max(F(8, 4), 1) == 2 and F(8, 4) > 1 and max(F(6, 4), 2) == 2 and F(6, 4) < 2)
rule62 = lambda p: (F(3, 2) * p[0], 2 * p[1])
check('fix 2: the 6-by-2 rule (3x/2, 2y) still stretches no sampled pair by more than 2',
      all(d2(rule62(p), rule62(q)) <= 4 * d2(p, q) for p, q in pairs))

# fix 3: corners go to corners, so A-D and B-C double under every legal rule; the centered fan is (x/2, 2y)
A, B, C, D, O = (0, 0), (4, 0), (4, 1), (0, 1), (2, F(1, 2))
A2, B2, C2, D2, O2 = (0, 0), (2, 0), (2, 2), (0, 2), (1, 1)
check('fix 3: A-D and B-C go from 1 to 2 (squared 1 to 4)', d2(A, D) == d2(B, C) == 1 and d2(A2, D2) == d2(B2, C2) == 4)


def affine(src, dst, p):
    """Barycentric coordinates of p in triangle src, applied to triangle dst."""
    (x1, y1), (x2, y2), (x3, y3) = [tuple(map(F, v)) for v in src]
    det = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    l1 = ((y2 - y3) * (p[0] - x3) + (x3 - x2) * (p[1] - y3)) / det
    l2 = ((y3 - y1) * (p[0] - x3) + (x1 - x3) * (p[1] - y3)) / det
    l3 = 1 - l1 - l2
    return tuple(l1 * a + l2 * b + l3 * c for a, b, c in zip(*dst))


tris = [((A, B, O), (A2, B2, O2)), ((B, C, O), (B2, C2, O2)), ((C, D, O), (C2, D2, O2)), ((D, A, O), (D2, A2, O2))]
same = True
for src, dst in tris:
    for _ in range(200):
        a, b = F(rng.randint(0, 100), 100), F(rng.randint(0, 100), 100)
        if a + b > 1:
            a, b = 1 - a, 1 - b
        p = tuple(a * s + b * t + (1 - a - b) * u for s, t, u in zip(*src))
        same &= affine(src, dst, p) == (p[0] / 2, 2 * p[1])
check('fix 3: the centered fan agrees with (x/2, 2y) at 800 exact points of its four triangles', same)


# ------------------------------------------------------------------ printed pages
def words(page):
    return re.sub(r'(\w)- (\w)', r'\1\2', re.sub(r'\s+', ' ', page.get_text()).strip())


s = pymupdf.open(FOLDER / 'week-73-students.pdf')
st = [words(p) for p in s]
check('student packet: 4 pages, every footer GGT73-S-v2', len(s) == 4 and all('GGT73-S-v2' in t for t in st))
if (OLD / 'week-73-students.pdf').exists():
    o = [words(p) for p in pymupdf.open(OLD / 'week-73-students.pdf')]
    cap = 'Example: M stays halfway from P to Q; N stays halfway from P to R. '
    check('pages 1 and 3 keep their v1 text apart from the footer', all(st[i] == o[i].replace('GGT73-S-v1', 'GGT73-S-v2') for i in (0, 2)))
    check('could 8: page 2 keeps its v1 text apart from the caption and the footer',
          cap in o[1] and st[1] == o[1].replace(cap, '').replace('GGT73-S-v1', 'GGT73-S-v2'))
check('could 8: the caption "Example: M stays halfway" is gone', 'M stays halfway' not in ' '.join(st))
p5 = st[3]
check('could 6: Problem 5 says the partner chooses a rectangle "and tests your rule"',
      'Your partner chooses one of these new rectangles and tests your rule.' in p5)
check('could 5: "a pair that every legal rule stretches at least that much"',
      'find a pair that every legal rule stretches at least that much.' in p5 and 'no legal rule can stretch less' not in p5)
check('fix 2: page 4 prints 8 by 1 and no 2 by 3', '8 by 1' in p5 and '2 by 3' not in p5)

U4 = 0.6 * 72


def outlines(page):
    out = []
    for d in page.get_drawings():
        it = d['items']
        if d['type'] == 's' and len(it) == 4 and all(i[0] == 'l' for i in it) and abs((d.get('width') or 0) - .8) < .05:
            xs = [q.x for i in it for q in i[1:]]
            ys = [q.y for i in it for q in i[1:]]
            out.append((min(xs), min(ys), max(xs), max(ys)))
    return out


R1 = outlines(s[0])
old_h = [r[3] - r[1] for r in R1 if abs(r[2] - r[0] - 4 * .94 * 72) < .3]
new_h = [r[3] - r[1] for r in R1 if abs(r[2] - r[0] - 2 * .94 * 72) < .3]
check('fix 1: on page 1, A-D is 0.94 in on the old sheet and exactly twice that on the square, so a doubled strip fits it',
      len(old_h) == 1 and len(new_h) == 1 and abs(old_h[0] - .94 * 72) < .2 and abs(new_h[0] - 2 * old_h[0]) < .2)
R4 = outlines(s[3])
dims = sorted((round((r[2] - r[0]) / U4, 2), round((r[3] - r[1]) / U4, 2)) for r in R4)
check(f'fix 2: page 4 draws 4 by 1 twice, 6 by 2 and 8 by 1 at 0.6 in per unit (found {dims})',
      dims == [(4.0, 1.0), (4.0, 1.0), (6.0, 2.0), (8.0, 1.0)])
eight = [r for r in R4 if abs((r[2] - r[0]) / U4 - 8) < .05]
fours = sorted([r for r in R4 if abs((r[2] - r[0]) / U4 - 4) < .05], key=lambda r: r[1])
check('fix 2: the 8 by 1 is drawn under the second 4 by 1, left edges aligned',
      len(eight) == 1 and len(fours) == 2 and eight[0][1] > fours[1][3] and abs(eight[0][0] - fours[1][0]) < .2)
lines = [d['rect'] for d in s[3].get_drawings() if d['type'] == 's' and [i[0] for i in d['items']] == ['l']]
heads = [d['rect'] for d in s[3].get_drawings() if d['type'] == 'fs' and [i[0] for i in d['items']] == ['l'] * 4]


def with_head(r):
    """An arrow's full extent: its line and the Stealth head touching its end."""
    h = [q for q in heads if q.intersects(pymupdf.Rect(r.x0 - 2, r.y0 - 2, r.x1 + 2, r.y1 + 2))]
    return pymupdf.Rect(min(r.x0, h[0].x0), min(r.y0, h[0].y0), max(r.x1, h[0].x1), max(r.y1, h[0].y1)) if h else None


horiz = [with_head(r) for r in lines if r.height < .1 and .3 < r.width / U4 < .6]
vert = [with_head(r) for r in lines if r.width < .1 and .3 < r.height / U4 < .7]
left_lab = [l['bbox'] for b in s[3].get_text('dict')['blocks'] for l in b.get('lines', [])
            if ''.join(sp['text'] for sp in l['spans']).strip() == 'left']
first = horiz[0] if len(horiz) == 1 and horiz[0] else None
gap = min((lb[0] - first.x1 for lb in left_lab if lb[0] > first.x1), default=0) if first else 0
check(f'could 7: the first arrow runs {first.width / U4 if first else 0:.2f} units (4.4 to 4.9) and its tip stops '
      f'{gap:.1f} pt before the 6 by 2 "left" label', first is not None and abs(first.width / U4 - .5) < .03 and gap > 10)
check('fix 2: a downward arrow, tip at the bottom, joins the second 4 by 1 to the 8 by 1',
      len(vert) == 1 and vert[0] is not None and fours[1][3] < vert[0].y0 and vert[0].y1 < eight[0][1]
      and any(abs(q.y1 - vert[0].y1) < .1 for q in heads))


def inner_gap(page):
    """Space between the old sheet's "right" label and the square's "left" label."""
    lab = {}
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(sp['text'] for sp in l['spans']).strip()
            lab.setdefault(t, []).append(l['bbox'])
    R = outlines(page)
    U = .94 * 72
    rect = [r for r in R if abs(r[2] - r[0] - 4 * U) < .3][0]
    sq = [r for r in R if abs(r[2] - r[0] - 2 * U) < .3][0]
    right, left = lab['right'][0], lab['left'][0]
    return left[0] - right[2], right[0] - rect[2], sq[0] - left[2]


for pn in range(3):
    g, r_off, l_off = inner_gap(s[pn])
    check(f'could 4: p. {pn + 1} inner "right" and "left" are {g:.1f} pt = {g / 72 * 25.4:.1f} mm apart, '
          f'each beside its own sheet ({r_off:.1f} and {l_off:.1f} pt from its edge)', g > 15 and 0 < r_off < 12 and 0 < l_off < 12)

g = pymupdf.open(FOLDER / 'week-73-facilitator.pdf')
gt = ' '.join(words(p) for p in g)
check('guide: 3 pages, every footer GGT73-FAC-v2, matched to GGT73-S-v2',
      len(g) == 3 and all('GGT73-FAC-v2' in words(p) for p in g) and 'matched to the four-page GGT73-S-v2 student packet' in gt)
check('fix 1: the launch uses a doubling strip for "more than twice?" and demonstrates it on A–D',
      'Problems 1–2 need no division, only “more than twice?”: mark the old length twice along a paper strip' in gt
      and 'Demonstrate this doubling strip on A–D, whose new length fits it exactly.' in gt)
check('fix 3: the Problem 1 key names A–D as Problem 4\'s lower bound for every legal rule',
      'A–D (and B–C) is already Problem 4’s lower bound.' in gt and 'every legal rule sends it to the matching corner' in gt)
check('fix 3: the Problem 3 hint says a Problem 2 fan is a rule and the centered fan is (x/2, 2y)',
      'Hint: a Problem 2 fan is already a rule for every point. The centered fan is exactly (x/2, 2y)' in gt)
check('fix 2: the Problem 5 key gives 8 by 1, optimum 2, rule (2x, y) and the bottom corners',
      'The 8-by-1 target also has optimum 2, for a different reason. Use F(x, y) = (2x, y).' in gt
      and 'the two bottom corners, 4 apart, must land on the new bottom corners, 8 apart' in gt
      and 'For 8 by 1 it is the two bottom corners.' in gt)
check('fix 2: the 2-by-3 key is gone', '2-by-3' not in gt and 'optimum 3' not in gt)
pkg = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-73' / 'editable'
check('fix 2: the package checks and notes use 8 by 1, not 2 by 3',
      '(8,1,2)' in (pkg / 'student' / 'check_math.py').read_text() and '(8,1,2)' in (pkg / 'guide' / 'check_math.py').read_text()
      and '"5_8_by_1": 2' in (pkg / 'checks' / 'results.json').read_text() and 'and2-by-3' not in (pkg / 'MATHEMATICS.md').read_text())

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
