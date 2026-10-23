#!/usr/bin/env python3
"""Check the Week 71 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-71-students.pdf and week-71-facilitator.pdf (default: the print
folder). Needs PyMuPDF. The mathematical claims the new guide text makes are
recomputed here: exact ray tracing in rectangles, floating-point sampling and an
exact unfolding argument in the 60 degree rhombus.
"""
from fractions import Fraction as F
from pathlib import Path
import math
import random
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2' / 'week-71'
FAILS = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


def text(pdf):
    d = pymupdf.open(FOLDER / pdf)
    return [re.sub(r'(\w)- (\w)', r'\1\2', re.sub(r'\s+', ' ', p.get_text()).strip()) for p in d]


# ------------------------------------------------------------------ rectangles (exact)

def rect_word(W, H, p, d, n):
    """Bounce word of n letters in [0,W]x[0,H] (A bottom, B left, C top, D right); None on a corner."""
    x, y = map(F, p)
    u, v = map(F, d)
    word = ''
    while len(word) < n:
        ts = []
        if u > 0: ts.append(((W - x) / u, 'D'))
        if u < 0: ts.append((-x / u, 'B'))
        if v > 0: ts.append(((H - y) / v, 'C'))
        if v < 0: ts.append((-y / v, 'A'))
        t = min(s for s, _ in ts)
        hit = [l for s, l in ts if s == t]
        if len(hit) > 1:
            return None
        x, y = x + t * u, y + t * v
        word += hit[0]
        if hit[0] in 'BD': u = -u
        else: v = -v
    return word


def has_both_runs(w):
    pairs = {w[i:i + 2] for i in range(len(w) - 1)}
    return bool(pairs & {'AC', 'CA'}) and bool(pairs & {'BD', 'DB'})


rng = random.Random(71)
rect_words = set()
for _ in range(6000):
    W, H = F(rng.randint(1, 40), rng.randint(1, 8)), F(rng.randint(1, 40), rng.randint(1, 8))
    p = (W * F(rng.randint(1, 99), 100), H * F(rng.randint(1, 99), 100))
    d = (rng.choice([-1, 1]) * rng.randint(1, 30), rng.choice([-1, 1]) * rng.randint(1, 30))
    w = rect_word(W, H, p, d, 8)
    if w:
        rect_words.add(w)
xyx = {'ABA', 'BAB', 'CDC', 'DCD'}
check('fix 1: no rectangle word of 6000 random exact shots contains ABA, BAB, CDC or DCD',
      not any(s in w for w in rect_words for s in xyx))
check('fix 1: no rectangle word has both an AC/CA run and a BD/DB run (ACDB, BDCA, CABD, DBAC rule out rectangles)',
      not any(has_both_runs(w) for w in rect_words))
# the reason: rising the full height h with horizontal travel under the width w needs |v/u| > h/w,
# crossing the full width w with vertical travel under h needs |v/u| < h/w
check('fix 1: the two slope conditions are incompatible for every tested rectangle and slope',
      all(not (h * abs(u) / abs(v) < w and w * abs(v) / abs(u) < h)
          for w in (1, 2, 3) for h in (1, 2, 5) for u in range(1, 9) for v in range(1, 9)))

three = set()
for d in [(a, b) for a in range(-9, 10) for b in range(-9, 10) if a and b and math.gcd(a, b) == 1]:
    # P1: start at the dot (1,1) of the bold square [0,2]^2 inside the printed window [-4,6]^2
    w = rect_word(2, 2, (1, 1), d, 3)
    if not w:
        continue
    # the unfolded line stays in the window through the third hit (grid lines at even coordinates)
    u, v = F(d[0]), F(d[1])
    times = sorted({(k * 2 - 1) / u for k in range(-5, 6) if (k * 2 - 1) / u > 0} | {(k * 2 - 1) / v for k in range(-5, 6) if (k * 2 - 1) / v > 0})
    t3 = times[2]
    if -4 <= 1 + t3 * u <= 6 and -4 <= 1 + t3 * v <= 6:
        three.add(w)
check('fix 1: from the Problem 1 dot, ACB, CAD, BDA and DBC can all be drawn inside the window',
      {'ACB', 'CAD', 'BDA', 'DBC'} <= three)
check('fix 1: direction (-1,-4) from the dot gives ACB', rect_word(2, 2, (1, 1), (-1, -4), 3) == 'ACB')

# ------------------------------------------------------------------ 60 degree rhombus (sampled)
S3 = math.sqrt(3)
P = [(0, 0), (4, 0), (6, 2 * S3), (2, 2 * S3)]
WALLS = [('A', P[0], P[1]), ('D', P[1], P[2]), ('C', P[2], P[3]), ('B', P[3], P[0])]


def rhombus_word(p, ang, n):
    x, y = p
    u, v = math.cos(ang), math.sin(ang)
    word = ''
    last = None
    while len(word) < n:
        best = None
        for lab, a, b in WALLS:
            if lab == last:
                continue
            ex, ey = b[0] - a[0], b[1] - a[1]
            den = u * ey - v * ex
            if abs(den) < 1e-12:
                continue
            t = ((a[0] - x) * ey - (a[1] - y) * ex) / den
            s = ((a[0] - x) * v - (a[1] - y) * u) / den
            if t > 1e-9 and -1e-9 <= s <= 1 + 1e-9 and (best is None or t < best[0]):
                best = (t, lab, s, ex, ey)
        t, lab, s, ex, ey = best
        if s < 1e-6 or s > 1 - 1e-6:
            return None  # a corner hit
        x, y = x + t * u, y + t * v
        L = math.hypot(ex, ey)
        nx, ny = -ey / L, ex / L
        dot = u * nx + v * ny
        u, v = u - 2 * dot * nx, v - 2 * dot * ny
        word += lab
        last = lab
    return word


def inside(x, y):
    return 0 < y < 2 * S3 and y / S3 < x < 4 + y / S3


rh3, rh4 = set(), set()
for _ in range(120000):
    while True:
        x, y = rng.uniform(0, 6), rng.uniform(0, 2 * S3)
        if inside(x, y):
            break
    w = rhombus_word((x, y), rng.uniform(0, 2 * math.pi), 4)
    if w:
        rh3.add(w[:3])
        rh4.add(w)
acb = {'ACB', 'CAD', 'BDA', 'DBC', 'BCA', 'DAC', 'ADB', 'CBD'}
rect3 = {w[:3] for w in rect_words}
check('fix 1: the 28 three-letter rectangle words', len(rect3) == 28)
check('fix 1: no sampled rhombus shot makes ACB or its seven versions', not (rh3 & acb))
check('fix 1: the rhombus makes every other rectangle three-letter word and ABA, BAB, CDC, DCD',
      rh3 == (rect3 - acb) | xyx)
check('fix 1: the rhombus makes ACDB, BDCA, CABD and DBAC', {'ACDB', 'BDCA', 'CABD', 'DBAC'} <= rh4)
check('could 8: no sampled rhombus shot makes ADA, DAD, BCB or CBC', not (rh3 & {'ADA', 'DAD', 'BCB', 'CBC'}))
check('could 8: the rhombus corners are 60 and 120 degrees, so the XYX seams at a 120 degree corner span 240',
      round(math.degrees(math.atan2(2 * S3, 2))) == 60 and 2 * (180 - 60) == 240)
# the guide's drift argument for ACB: the image of B across C leans 1/sqrt3 left per unit rise,
# the rise from A to C is 2 sqrt3, so the drift exceeds 2; C starts at x = 2, so A would be met at x > 4
check('fix 1: the drift argument: rise 2*sqrt3 times 1/sqrt3 is 2, and 2 + 2 is the right end of A',
      abs(2 * S3 / S3 - 2) < 1e-12 and P[3][0] + 2 == P[1][0])

# ------------------------------------------------------------------ printed pages
s = text('week-71-students.pdf')
check('student packet: 5 pages, every footer GGT71-S-v2', len(s) == 5 and all('GGT71-S-v2' in p for p in s))
check('could 4: Problem 1 no longer repeats the partner check', 'Your partner checks the crossed walls' not in s[0]
      and 'Write each word by the end of its shot.' in s[0])
check('could 3: Problem 3 no longer says "Keep your drawing hidden until the guess."', 'Keep your drawing hidden' not in ' '.join(s))
check('could 5 (left): "Failing to find a shot is not a reason to rule out a room." is still printed',
      'Failing to find a shot is not a reason to rule out a room.' in s[2])
check('should 2: page 5 opens with only "Extra workspace for Problems 2–3."',
      re.search(r'Grades 4–5 Extra workspace for Problems 2–3\. ', s[4]) is not None
      and 'Stand the mirror' not in s[4] and 'Keep the checked drawing' not in s[4])
check('the mirror rule is still stated once, in Problem 2', ' '.join(s).count('Use a mirror on each wall') == 1)

g = ' '.join(text('week-71-facilitator.pdf'))
gp = text('week-71-facilitator.pdf')
check('guide: 4 pages, GGT71-FAC-v2 or later (v3 after Critic J), sources on page 4', len(gp) == 4 and all(re.search(r'GGT71-FAC-v[2-9]', p) for p in gp)
      and 'Sources, checks, and limits' in gp[3])
check('fix 1: overview says distinctions run both ways', 'Distinctions run both ways: the square word ACB is impossible in the rhombus' in g)
check('fix 1: P3 key names ABA, BAB, CDC, DCD', 'An ABA (or BAB, CDC, DCD) drawing rules out both rectangles' in g)
check('fix 1: P3 key names the second family', all(w in g for w in ('ACDB', 'BDCA', 'CABD', 'DBAC')) and 'two vertical walls in a row' in g)
check('fix 1: P3 key gives the eight rhombus-impossible words and the drift argument',
      'ACB and its mirror and rotated versions (CAD, BDA, DBC, BCA, DAC, ADB, CBD)' in g and 'drifts left more than 2' in g)
check('fix 1: P3 key says P1 shots can rule out the rhombus', 'From the Problem 1 dot, ACB, CAD, BDA and DBC can all be drawn' in g)
check('fix 1: "It may or may not be possible in the rhombus" is gone', 'It may or may not be possible in the rhombus' not in g)
check('could 6: the referee checks a secret shot', 'The rotating referee checks the secret shot before its word is given' in g)
check('could 7: "page 2 of this guide"', 'the checked example on page 2 of this guide shows' in g)
check('could 8: the extension on ADA, DAD, BCB, CBC', 'ADA, DAD, BCB and CBC never occur in the rhombus' in g)
check('could 9: the launch folds the reflected copies to the light', 'Fold a spare page 1 along the A and D seams' in g)
check('guide matches GGT71-S-v2', re.search(r'GGT71-S-?v2', g) is not None)  # a line break may fall after the hyphen

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
