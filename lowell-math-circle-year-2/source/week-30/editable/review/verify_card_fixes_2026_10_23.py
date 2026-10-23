#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes of Week 30 (v3 packets) against the built PDFs.

Run from the package folder after `python3 build.py`, or pass the folder holding
k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf:

    python3 review/verify_card_fixes_2026_10_23.py [folder]

It reads the printed pages (PyMuPDF) and the problem files' figures.py, and checks
each fix and the mathematics behind it. Standard library plus PyMuPDF.
"""
import itertools
import json
import sys
from pathlib import Path

import pymupdf

PKG = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PKG
for figures_dir in (PKG / 'problem-files', PKG.parent):
    if (figures_dir / 'figures.py').exists():
        break
else:
    sys.exit('Cannot find figures.py (problem files)')
sys.path.insert(0, str(figures_dir))
sys.dont_write_bytecode = True
import figures  # noqa: E402


def placements(kit):
    return itertools.product((-1, 0, 1), repeat=len(kit))


def ways(kit, t):
    """Placements balancing target t: +1 opposite the target, -1 beside it, 0 off."""
    return [p for p in placements(kit) if sum(c * w for c, w in zip(p, kit)) == t]


def positives(kit):
    return sorted({sum(c * w for c, w in zip(p, kit)) for p in placements(kit)} - {0} & set(range(1, 10 ** 4)))


def first_miss(kit):
    return next(t for t in itertools.count(1) if not ways(kit, t))


def pages(name):
    return [pg.get_text() for pg in pymupdf.open(OUT / name)]


fails = []


def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)


K, M, U = pages('k-1.pdf'), pages('grades-2-3.pdf'), pages('grades-4-5.pdf')
G = '\n'.join(pages('facilitator-guide.pdf'))
for name, pp, tag in (('K-1', K, 'F30-K-v3'), ('2-3', M, 'F30-23-v3'), ('4-5', U, 'F30-45-v3')):
    check(len(pp) == 5 and all(tag in p for p in pp), f'{name}: five pages, every footer {tag}')

# Could 9: the launch example is target 5 with weights 2 and 7, which no task uses.
check(all('Target 5; weights 2 and 7' in pp[0] and '5 + 2 = 7' in pp[0] for pp in (K, M, U)), 'launch example 5 + 2 = 7 on every first page')
check(ways((2, 7), 5) == [(-1, 1)], 'target 5 balances with 2 and 7 only by putting 2 beside it')
check(not any('2 and 7' in p for pp in (K, M, U) for p in pp[1:]) and all(pp[0].count('2 and 7') == 1 for pp in (K, M, U)),
      'the kit 2 and 7 appears in no task')

# Should 3: K-1 Problem 3 has a labelled row of boxes 1-6 for each kit, no ruled lines.
k3 = K[2]
check('1 and 4' in k3 and '1 and 3' in k3, 'K-1 P3: rows labelled 1 and 4, 1 and 3')
r14 = [t for t in positives((1, 4)) if t <= 6]
r13 = [t for t in positives((1, 3)) if t <= 6]
check(r14 == [1, 3, 4, 5] and r13 == [1, 2, 3, 4], f'K-1 P3: 1 and 4 reach {r14}, 1 and 3 reach {r13}; four each')

# Could 8: the tenth dot of the 10 card clears the card border.
step = .33
lowest = 1.05 + (9 // 3) * step                     # cm below the card's top edge
clear_pt = (2.25 - lowest) * 72 / 2.54 - 1.5        # minus the dot's radius, 1.5 pt
src = (figures_dir / 'figures.py').read_text()
check('(j // 3) * .33' in src and clear_pt > 3, f'10 card: lowest dot clears the border by {clear_pt:.1f} pt')

# Should 6 and could 10: Grades 2-3 Problem 2 boards have blank targets; no "Test your choice."
m2 = pymupdf.open(OUT / 'grades-2-3.pdf')[1]
words = m2.get_text('words')
labels = [w for w in words if w[4] == 'target' and w[1] > 300]   # board labels, not the prompt
under = [w for w in words for t in labels if w[4].isdigit() and abs(w[0] - t[0]) < 30 and 0 < w[1] - t[3] < 40]
check(len(labels) == 3 and not under, '2-3 P2: three boards, no printed target numbers')
check('Test your choice' not in M[1], '2-3 P2: "Test your choice." removed')
check([w for w in range(1, 200) if all(ways((1, 3, w), t) for t in range(1, 14))] == [9], '2-3 P2: 9 is the only third weight up to 199')

# Should 4: Grades 2-3 Problem 3 prints target boxes 1-14 under each kit.
m3 = pymupdf.open(OUT / 'grades-2-3.pdf')[2].get_text('words')
kit_lines = [w[1] for w in m3 if w[4] == '1,']
nums = sorted(int(w[4]) for w in m3 if w[4].isdigit() and 90 < w[1] < 700 and all(abs(w[1] - y) > 3 for y in kit_lines))
check(nums == sorted(list(range(1, 15)) * 3), '2-3 P3: boxes 1-14 under each of the three kits')
misses = [first_miss(k) for k in ((1, 3, 8), (1, 3, 9), (1, 3, 10))]
check(misses == [13, 14, 5] and max(misses) <= 14, f'2-3 P3: first misses {misses} all lie in 1-14')

# Should 1: Grades 2-3 Problem 4 prints three boards under each kit, so the count is not shown.
m4 = M[3]
n38, n39 = len(ways((1, 3, 8), 4)), len(ways((1, 3, 9), 4))
check(m4.count('target') == 6 and m4.count('1, 3, 8') == 1 and m4.count('1, 3, 9') == 1, '2-3 P4: three small boards under each kit')
check((n38, n39) == (2, 1) and max(n38, n39) < 3, f'2-3 P4: 4 balances {n38} and {n39} ways, fewer than the boards')

# Should 2: Grades 4-5 Problem 5 asks for the most any three-weight kit can balance.
u4 = ' '.join(U[3].split())
check('What is the most any three-weight kit can balance, even with gaps? Explain why none can do better.' in u4, '4-5 P5: new question')
best = max(len(positives((a, b, c))) for a in range(1, 41) for b in range(a + 1, 41) for c in range(b + 1, 41))
check(best == 13 and len(positives((1, 3, 9))) == 13 and (3 ** 3 - 1) // 2 == 13, '4-5 P5: at most 13 (search to 40), reached by 1, 3, 9')
check('Why none can do better' in G and 'at most 13 are positive' in G, 'guide: 4-5 P5 key gives the reason')

# Should 5: guide materials list sticks for every printed weight, the launch included.
sticks = (1, 2, 3, 4, 7, 8, 9, 10)
printed = {1, 2, 3, 4, 7, 8, 9, 10}
gtext = ' '.join(G.split())
check('1, 2, 3, 4, 7, 8, 9 and 10 units (44 cubes per kit)' in gtext and sum(sticks) == 44 and printed <= set(sticks) | {27, 81},
      'guide: a stick for every weight card the pages print; 44 cubes per kit')
check(5 * sum(sticks) == 220 and 'about 220 cubes' in gtext, 'guide: about 220 cubes for five kits')
check('target 5 with weights 2 and 7' in gtext and 'About 35-40 minutes at tables' in gtext, 'guide: launch example and 35-40 minute plan')

print(json.dumps({'checks_failed': len(fails)}))
sys.exit(1 if fails else 0)
