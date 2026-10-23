#!/usr/bin/env python3
"""Check the Critic L coulds of October 23, 2026 (K-1 v5, Grades 4-5 v5, guide).

    python3 review/verify_critic_coulds_2026_10_23.py [build-folder] [views-folder]

The build folder (default: this package's root) holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and
facilitator-guide.pdf; the optional views folder is problem-files/tools/build.py's output, whose
grades-4-5-return.pdf is checked for a self-contained Problem 3. Needs PyMuPDF. The borders are
tested exactly with the package's motif (src/mathematical-checks.json) and a frieze test written
here; nothing imports the builders or the other verifiers.

Could 6: Grades 4-5 Problem 3 opens the return-route view, which lacks Problem 2's definition of a
glide, so the prompt names the move: a flip over the middle line and a 3 cm slide along it.
Could 7: K-1 Problem 4 asked for "a longer slide", which Problem 3's own border G already has
(the flip and a 9 cm slide match); it now asks for a border whose shortest slide is longer.
Could 8: five groups (two K-1 pairs, two Grades 2-3 pairs, one Grades 4-5 trio) need five sets of
24 cards, not four; at the guide's old rate (20 minutes for 96 cards) that is 25 minutes.
"""
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
build = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
views = Path(sys.argv[2]) if len(sys.argv) > 2 else None
checks = 0


def ok(cond, what):
    global checks
    assert cond, what
    checks += 1


def text(page):
    t = ' '.join(page.get_text().replace('–', '-').replace('’', "'").split())
    return re.sub(r'([a-z])- ([a-z])', r'\1\2', t)


def pages(pdf):
    return [text(p) for p in pymupdf.open(pdf)]


# ------------------------------------------------------------ borders, exactly
V = json.loads((ROOT / 'src' / 'mathematical-checks.json').read_text())['motif_vertices']
MOTIF = [(F(str(x)), F(str(y))) for x, y in V]
FORM = {'A': (1, 1), 'mirror': (1, -1)}          # mirror = A flipped over the middle line
h = F(3, 2)
BORDER = {'G': (6, [(0, h, 'A'), (3, -h, 'mirror')]), 'G8': (8, [(0, h, 'A'), (4, -h, 'mirror')])}


def outline(name, reps):
    P, cards = BORDER[name]
    return {(x + P * k + FORM[f][0] * u, y - FORM[f][1] * v) for k in reps for x, y, f in cards for u, v in MOTIF}


def maps(name, flip, d):
    """Does (x, y) -> (x + d, -y if flip else y) carry the endless border onto itself?"""
    inner, outer = outline(name, range(-2, 3)), outline(name, range(-8, 9))
    return all((x + d, -y if flip else y) in outer for x, y in inner)


def shortest(name, flip):
    P = BORDER[name][0]
    return min(d for d in (F(i, 2) for i in range(1, 6 * P)) if maps(name, flip, d))


# Could 7: G (Problem 3's border) already has a longer flip-and-slide, so "a longer slide" asked nothing new.
ok(maps('G', True, 3) and maps('G', True, 9) and not maps('G', True, 0), "G: flip + 3 and flip + 9 match, the flip alone fails")
ok(shortest('G', True) == 3 and shortest('G8', True) == 4, 'shortest slide after the flip: G 3 cm, G8 4 cm (longer)')
ok(shortest('G', False) == 6 and shortest('G8', False) == 8, 'shortest plain slide: G 6, G8 8 (longer either way)')
ok(not maps('G8', True, 0), 'G8: the flip alone still fails')
# Could 6: the named move is a 3 cm glide; twice it is a 6 cm slide; G shows a 3 cm slide need not match.
for name in BORDER:
    P = BORDER[name][0]
    for i in range(1, 4 * P):
        d = F(i, 2)
        if maps(name, True, d):
            ok(maps(name, False, 2 * d), (name, 'flip + slide d, done twice, is a slide 2d', d))
ok(maps('G', True, 3) and maps('G', False, 6) and not maps('G', False, 3), '4-5 P3 witness G')
# Could 8: five groups, five sets.
groups = {'K-1': 4 // 2, 'Grades 2-3': 4 // 2, 'Grades 4-5': 1}   # pairs, pairs, one trio (worksheet-workflow/context.md)
sets = sum(groups.values())
ok(sets == 5 and 2 * 3 >= sets, 'five sets; three sheets of two sets each cover them')
ok(sets * 24 == 120 and F(20, 96) * 120 == 25, '120 cards, 25 minutes at the old rate')

# ------------------------------------------------------------ the printed pages
K, M, U = (pages(build / f'{n}.pdf') for n in ('k-1', 'grades-2-3', 'grades-4-5'))
ok("Problem 4: Make another border like Problem 3's, where the shortest slide is longer." in K[2], 'K-1 P4 prompt')
ok('with a longer slide' not in ' '.join(K), 'old K-1 P4 wording gone')
ok('Problem 3: A border matches after a flip over the middle line and a 3 cm slide along it. Must a 6 cm slide also match? '
   'Must a 3 cm slide match? Explain why.' in U[1], '4-5 P3 prompt')
ok('3 cm glide' not in ' '.join(U), 'old 4-5 P3 wording gone')
for name, pp, n, v in (('k-1', K, 5, 'v5'), ('grades-2-3', M, 4, 'v4'), ('grades-4-5', U, 5, 'v5')):
    ok(len(pp) == n and all(f'Bellingham Math Circle / Week 35 / W35-{name}-{v}' in t for t in pp), (name, 'footers', v))
g = pages(build / 'facilitator-guide.pdf')
G = ' '.join(g)
ok(len(g) == 8, 'guide keeps 8 pages')
ok('about 25 minutes to cut five sets with scissors (120 cards on straight lines; less with a paper trimmer): both sets on the K-1 '
   'and Grades 2-3 sheets, for two pairs each, and Set 1 for the Grades 4-5 trio.' in g[1], 'preparation estimate')
ok('four sets' not in G and '96 cards' not in G, 'old count gone')
ok('Print one sheet of week-35-materials.pdf per table' in g[1] and 'each half is a set of 24 footprint cards for one pair or trio' in g[1],
   'print note still one sheet per table, two sets a sheet')
ok('Current packets (October 23, 2026: K-1 v5, Grades 2-3 v4, Grades 4-5 v5)' in g[0], 'status names the packets')
ok('K-1 v5, Problems 1-7; Grades 2-3 v4 and Grades 4-5 v5, Problems 1-6.' in g[6], 'packet basis')
ok(all('Unpiloted / Current base packets / Revised October 23 2026 (K-1 and 4-5 v5)' in t for t in g[:7]), 'guide footer')
ok('A 3 cm glide is the flip over the middle line followed by a 3 cm slide along it' in g[5], '4-5 P3 key still names the move')
ok('G8 matches after the flip and a 4 cm slide, where G used 3 cm' in g[4], 'K-1 P4 key unchanged and still right')
if views:
    R = pages(views / 'grades-4-5-return.pdf')
    p3 = [t for t in R if 'Problem 3:' in t]
    ok(len(p3) == 1 and 'a flip over the middle line and a 3 cm slide along it' in p3[0] and 'A glide is' not in ' '.join(R),
       'return view: Problem 3 names its move without Problem 2')
    ok(all('W35-grades-4-5-v5-return' in t for t in R), 'return view footer')
print(f'PASS: {checks} checks of the Critic L coulds' + (' (with the views)' if views else ''))
