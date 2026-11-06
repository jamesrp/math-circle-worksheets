#!/usr/bin/env python3
"""Check the November 6, 2026 kid-fit revision of Week 36 (student packets v4) and its guide.

    python3 review/verify_kid_fit_2026_11_06.py [PDF_DIR]

PDF_DIR holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf
(default: reference-pdfs/). The mathematics behind every changed guide sentence is
recomputed from the two attribute tests; the pages are read back with pdfplumber.
Prints each check and exits 1 on any failure. The October 23 checks
(verify_card_shoulds_2026_10_23.py) describe the v3 pages, now archived.
"""
import itertools
import sys
from functools import lru_cache
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / 'reference-pdfs'
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def pages(name):
    with pdfplumber.open(PDF / name) as pdf:
        return [' '.join((p.extract_text() or '').split()) for p in pdf.pages]


def squares(name, page, lo_mm, hi_mm):
    with pdfplumber.open(PDF / name) as pdf:
        pg = pdf.pages[page - 1]
        mm = lambda v: v * 25.4 / 72
        return [r for r in pg.rects if abs(r['width'] - r['height']) < .5 and lo_mm < mm(r['width']) < hi_mm]


# ---------------------------------------------------------------- mathematics
tiles = list(itertools.product(range(3), repeat=2))           # (shape, fill)
def allowed(t, attrs=(0, 1)): return all(len({x[k] for x in t}) in (1, 3) for k in attrs)
lines = [frozenset(t) for t in itertools.combinations(tiles, 3) if allowed(t)]
def cap(t, attrs=(0, 1)): return not any(allowed(u, attrs) for u in itertools.combinations(t, 3))
check(len(lines) == 12, '12 allowed threes')
check(all(not cap(t) for t in itertools.combinations(tiles, 5)),
      'any five tiles contain an allowed three (Grades 2-3 Problem 3: the partner\'s hunt on five tiles always succeeds)')
check(max(n for n in range(10) for t in itertools.combinations(tiles, n) if cap(t)) == 4, 'K-1 Problem 4 / 2-3 Problem 3: the maximum is 4')
# K-1 Problem 3 (middle tile): the four threes through a tile pair off the other eight, so they fit
# a 3 x 3 mat as the four lines through the centre cell (opposite cells).
def pairs_off(x):
    through = [l - {x} for l in lines if x in l]
    return len(through) == 4 and len(set().union(*through)) == 8 and x not in set().union(*through)
check(all(pairs_off(x) for x in tiles), 'every tile: four threes that pair off the other eight tiles (the four opposite-cell pairs around the mat centre)')
# The game (2-3 Problem 5, 4-5 Problem 5): normal play from empty; every legal game lasts four moves.
@lru_cache(None)
def lengths(chosen):
    moves = [y for y in tiles if y not in chosen and cap(tuple(sorted(chosen + (y,))))]
    if not moves:
        return frozenset([len(chosen)])
    return frozenset().union(*(lengths(tuple(sorted(chosen + (y,)))) for y in moves))
check(lengths(()) == frozenset([4]), 'every legal game lasts exactly four moves, so the second player always wins')
# Shapes-only fallback (guide p. 2): Problems 2 and 4 still work.
shape_lines = [t for t in itertools.combinations(tiles, 3) if allowed(t, (0,))]
shape_splits = [s for s in itertools.combinations(shape_lines, 3) if len(set().union(*map(set, s))) == 9]
best = max(n for n in range(10) for t in itertools.combinations(tiles, n) if cap(t, (0,)))
check(len(shape_splits) > 0 and best == 4, f'shapes only: K-1 Problem 2 has splits ({len(shape_splits)}) and Problem 4 has maximum 4')
splits = [s for s in itertools.combinations(lines, 3) if len(set().union(*s)) == 9]
check(len(splits) == 4, 'four splits; six boards on Grades 2-3 p. 2 leave room for a repeat')

# ---------------------------------------------------------------- student pages (v4)
want = {
    'k-1': ['Use the nine tiles', 'Problem 1: Pick a third tile for each pair to make an allowed three. Your partner checks each three.',
            'Problem 2: Put all nine tiles', 'Problem 3: Choose one tile and keep it in the middle of the table.',
            'Problem 4: Choose tiles without making any allowed three. Your partner looks for an allowed three in your tiles.'],
    'grades-2-3': ['Problem 1: Complete each pair', 'Problem 2: Split all nine tiles',
                   'Problem 3: Choose as many tiles as you can with no allowed three among them. Your partner looks',
                   'Problem 4: Choose one tile.', 'Problem 5: Start with no tiles chosen. Take turns'],
    'grades-4-5': ['Problem 1: Complete the pairs.', 'Problem 2: Choose as many tiles as possible',
                   'Problem 3: Find as many allowed threes through one chosen tile as possible',
                   'Problem 4: Split the nine tiles', 'Problem 5: Start with no tiles chosen. Two players take turns'],
}
for band, starts in want.items():
    t = pages(f'{band}.pdf')
    check(len(t) == 5, f'{band}: five pages')
    check(all(f'W36-{band}-v4' in p for p in t), f'{band}: every footer reads W36-{band}-v4')
    check(all(s in p for s, p in zip(starts, t)), f'{band}: each page carries its v4 problem')
check(len(squares('k-1.pdf', 2, 63, 65)) == 4, 'K-1 p. 2: four 64 mm answer boxes that hold a 60 mm tile')
with pdfplumber.open(PDF / 'k-1.pdf') as pdf:
    pg = pdf.pages[4]
    xs = sorted({round(l['x0'] * 25.4 / 72, 1) for l in pg.lines if abs(l['x0'] - l['x1']) < .1 and l['height'] > 400})
check(len(xs) == 4 and {round(b - a, 1) for a, b in zip(xs, xs[1:])} == {60.0}, f'K-1 p. 5: the tile page is cut into 60 mm cells ({xs})')
check(len(squares('grades-2-3.pdf', 2, 17.5, 18.5)) == 54, 'Grades 2-3 p. 2: six record boards of nine 18 mm cells')
check(len(squares('grades-2-3.pdf', 5, 17.5, 18.5)) == 36, 'Grades 2-3 p. 5: four record boards')

# ---------------------------------------------------------------- guide
g = pages('facilitator-guide.pdf')
G = ' '.join(g)
check(len(g) == 6, 'guide: six pages, as before')
check('Version 4 (kid-fit revision, November 6, 2026) has 4 / 5 / 5 problems' in g[0], 'guide p. 1: version 4 status')
check(all('Student packets v4 / Revised November 6 2026' in p for p in g[:5]), 'guide pp. 1-5: footer names the v4 packets')
check('On every printed nine-tile grid (K-1 p. 5, Grades 2-3 pp. 2-5, Grades 4-5 pp. 2-4)' in g[0], 'guide p. 1: the straight-line warning names every v4 grid')
check('print K-1 p. 5 on card stock' in g[1] and 'K-1 p. 3' not in G, 'guide p. 2: tiles are cut from K-1 p. 5')
check('Problems 2 and 4 still work' in g[1], 'guide p. 2: the shapes-only fallback names K-1 Problems 2 and 4')
check('Problem 3: four triples through any chosen tile' in g[2] and 'Problem 4: 4 tiles is the maximum' in g[2], 'guide p. 3: K-1 keys follow the new order')
check('Six boards leave room for a repeat' in g[2] and 'The p. 5 boards can save each final four' in g[2], 'guide p. 3: Grades 2-3 boards explained')
check('Split 1, shapes' in g[3] and 'The maximum proof with physical pairs' in g[4], 'guide: "page 4 lists all" and "page 5 explains" still hold')
check('so the second player wins' in g[3], 'guide p. 4: Grades 4-5 Problem 5 as a game')
check('collect triples through one tile (P3), or build no-three collections (P4)' in g[5], 'guide p. 6: route note follows the new K-1 order')

print(f'{len(FAIL)} failure(s)')
sys.exit(1 if FAIL else 0)
