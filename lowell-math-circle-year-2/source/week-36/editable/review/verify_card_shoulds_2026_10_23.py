#!/usr/bin/env python3
"""Check every claim changed by the October 23, 2026 review-card fixes (Week 36, v3).

    python3 review/verify_card_shoulds_2026_10_23.py [PDF_DIR] [--bonus-guide PDF]

PDF_DIR holds k-1.pdf, grades-2-3.pdf, grades-4-5.pdf and facilitator-guide.pdf
(default: reference-pdfs/). The mathematics is recomputed from the two attribute
tests; the pages are read back with pdfplumber. Prints each check and exits 1 on
any failure.
"""
import itertools
import sys
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith('--')]
PDF = Path(args[0]) if args else HERE.parent / 'reference-pdfs'
BONUS = Path(sys.argv[sys.argv.index('--bonus-guide') + 1]) if '--bonus-guide' in sys.argv else None
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def text(name, page=None):
    with pdfplumber.open(PDF / name) as pdf:
        pages = pdf.pages if page is None else [pdf.pages[page - 1]]
        return ' '.join(' '.join((p.extract_text() or '').split()) for p in pages)


# ---------------------------------------------------------------- mathematics
SHAPE, FILL = ['circle', 'triangle', 'square'], ['open', 'striped', 'solid']
tiles = list(itertools.product(range(3), repeat=2))          # (shape, fill)
def allowed(t, attrs=(0, 1)): return all(len({x[k] for x in t}) in (1, 3) for k in attrs)
lines = [t for t in itertools.combinations(tiles, 3) if allowed(t)]
check(len(lines) == 12, '12 allowed threes')
name = lambda x: f'{FILL[x[1]]} {SHAPE[x[0]]}'

# Record boards: row = shape (circle, triangle, square), column = fill (open, striped, solid).
pos = {x: (x[0], x[1]) for x in tiles}                         # (row, column)
def straight(t):
    (r1, c1), (r2, c2), (r3, c3) = sorted(pos[x] for x in t)
    return (r2 - r1, c2 - c1) == (r3 - r2, c3 - c2)
geo = [t for t in itertools.combinations(tiles, 3) if straight(t)]
check(len(geo) == 8 and all(allowed(t) for t in geo), 'all eight straight lines of the record-board layout are allowed threes')
bent = sorted(sorted(name(x) for x in t) for t in lines if not straight(t))
guide_bent = [['open circle', 'solid triangle', 'striped square'], ['striped circle', 'open triangle', 'solid square'],
              ['striped circle', 'solid triangle', 'open square'], ['solid circle', 'open triangle', 'striped square']]
check(bent == sorted(sorted(b) for b in guide_bent), 'the four bent allowed threes are the four the guide lists')
def through(x, ls): return sum(x in t for t in ls)
centre, corner, edge = (1, 1), (0, 0), (0, 1)
check((through(centre, geo), through(corner, geo), through(edge, geo)) == (4, 3, 2),
      'straight lines through the centre, a corner and an edge tile: 4, 3, 2')
check(all(through(x, lines) == 4 for x in tiles), 'every tile is in four allowed threes')
splits = [s for s in itertools.combinations(lines, 3) if len(set().union(*map(set, s))) == 9]
check(len(splits) == 4, 'four splits, so six boards on Grades 4-5 Problem 4 leave room for two more attempts')
def cap(t, attrs=(0, 1)): return not any(allowed(u, attrs) for u in itertools.combinations(t, 3))
check(max(n for n in range(10) for t in itertools.combinations(tiles, n) if cap(t)) == 4, 'the most tiles without an allowed three is 4')
check(all(not any(cap(t + (y,)) for y in tiles if y not in t) for t in itertools.combinations(tiles, 4) if cap(t)),
      'Grades 2-3 Problem 3: every unused tile completes an allowed three with any legal four (the check the key accepts)')
check(all(sum(set(l) < set(t + (y,)) for l in lines) >= 1 for t in itertools.combinations(tiles, 3) if cap(t)
          for y in tiles if y not in t and not cap(t + (y,))), 'a blocked tile always lies in a three with two chosen tiles')
# Grades 4-5 Problem 1: no pair has two completing tiles or none.
check(all(sum(set(p) < set(l) for l in lines) == 1 for p in itertools.combinations(tiles, 2)), 'every pair of tiles has exactly one completing tile')
# Readiness fallback: shapes only.
shape_caps = [t for n in range(10) for t in itertools.combinations(tiles, n) if cap(t, (0,))]
best = max(len(t) for t in shape_caps)
witnesses = [t for t in shape_caps if len(t) == best]
check(best == 4 and all(sorted({x[0] for x in t}) != [0, 1, 2] and all(sum(x[0] == s for x in t) == 2 for s in {x[0] for x in t}) for t in witnesses),
      'shapes only: the most tiles without a three is 4, always two each of two shapes')
shape_lines = [t for t in itertools.combinations(tiles, 3) if allowed(t, (0,))]
shape_splits = [s for s in itertools.combinations(shape_lines, 3) if len(set().union(*map(set, s))) == 9]
check(len(shape_splits) > 4, f'shapes only: Problem 2 still works ({len(shape_splits)} splits)')

# ---------------------------------------------------------------- student pages
for band, n in (('k-1', 4), ('grades-2-3', 4), ('grades-4-5', 5)):
    t = text(f'{band}.pdf')
    check(t.count(f'W36-{band}-v3') == n, f'{band}: every footer reads W36-{band}-v3')
check('Problem 1: Complete the pairs. Can two different tiles have two completing tiles, or none? Explain.' in text('grades-4-5.pdf', 1),
      'Grades 4-5 Problem 1 asks openly')
check('How do you know you cannot keep more?' in text('grades-2-3.pdf', 3) and 'change one chosen tile' not in text('grades-2-3.pdf', 3),
      'Grades 2-3 Problem 3 asks "How do you know you cannot keep more?"')
with pdfplumber.open(PDF / 'grades-4-5.pdf') as pdf:
    pg = pdf.pages[3]
    cells = [r for r in pg.rects if abs(r['width'] - r['height']) < .5 and 50 < r['width'] < 52.5]
    side_mm = sorted({round(r['width'] * 25.4 / 72, 1) for r in cells})
    check(len(cells) == 54 and side_mm == [18.0], f'Grades 4-5 p. 4: six boards of nine 18 mm cells ({len(cells)} cells, {side_mm} mm)')
with pdfplumber.open(PDF / 'k-1.pdf') as pdf:
    pg = pdf.pages[2]
    xs = sorted({round(l['x0'] * 25.4 / 72, 1) for l in pg.lines if abs(l['x0'] - l['x1']) < .1 and l['height'] > 400})
    gaps = {round(b - a, 1) for a, b in zip(xs, xs[1:])}
    check(len(xs) == 4 and gaps == {60.0}, f'K-1 p. 3: the tile sheet is cut into 60 mm cells ({xs})')

# ---------------------------------------------------------------- guide
g = text('facilitator-guide.pdf')
check('45 mm' not in g and 'print K-1 p. 3 on card stock once per child, plus one, and cut on the grey lines: nine 60 mm tiles' in g,
      'guide: the tiles are cut from K-1 p. 3 at 60 mm')
check('For eleven children' in g and 'For ten children' not in g, 'guide: eleven children')
check('youngest adult' not in g and g.count("K-1 table's adult") == 2, "guide: the K-1 table's adult, pp. 2 and 6")
check('all eight straight lines of that layout are allowed threes' in g and 'four threes through the centre tile, three through a corner and two through an edge tile' in g,
      'guide p. 1: the record-board facts')
check('judge shapes only, with all nine tiles (fills ignored)' in g and 'again four, two each of two shapes' in g, 'guide p. 2: the shapes-only fallback')
check('0-5 minutes: the usual movement break' in g and '48-55 minutes' in g and '57-60' not in g, 'guide p. 2: the timetable fits the hour (35-40 minutes at tables)')
with pdfplumber.open(PDF / 'facilitator-guide.pdf') as pdf:
    check(len(pdf.pages) == 6, 'guide: six pages, as before')
    heads = [' '.join((p.extract_text() or '').split())[:160] for p in pdf.pages]
check('Key for Grades 4-5' in heads[3] and 'Proofs and source notes' in heads[4], 'guide: page references hold (partition list p. 4, proofs p. 5)')
check('Split 1, shapes' in text('facilitator-guide.pdf', 4) and 'The maximum proof with physical pairs' in text('facilitator-guide.pdf', 5),
      'guide: "page 4 lists all" and "page 5 explains" still point at the partition list and the proof')

# ---------------------------------------------------------------- bonus guide, Problem 3 extension
cards = list(itertools.product(range(3), repeat=3))           # (shape, fill, number)
blines = {frozenset(t) for t in itertools.combinations(cards, 3) if allowed(t, (0, 1, 2))}
def third(a, b): return tuple((-a[k] - b[k]) % 3 for k in range(3))
check(all(third(a, b) == (a[0], a[1], 3 - a[2] - b[2]) for a in cards for b in cards if a[:2] == b[:2] and a != b),
      'bonus: two copies of a shape/fill tile are completed only by its third copy')
def capsets9():
    # Depth-first search over 9-card sets with no allowed three.
    out = []
    def go(start, chosen, banned):
        if len(chosen) == 9:
            out.append(tuple(chosen)); return
        for i in range(start, 27):
            c = cards[i]
            if c in banned: continue
            nb = set(banned) | {third(c, d) for d in chosen}
            go(i + 1, chosen + [c], nb)
    go(0, [], set())
    return out
sets9 = capsets9()
reps = sum(len({c[:2] for c in s}) < 9 for s in sets9)
check((len(sets9), reps) == (2106, 1944), f'bonus: {len(sets9)} nine-card sets have no allowed three; {reps} of them repeat a shape/fill tile')
if BONUS:
    with pdfplumber.open(BONUS) as pdf:
        b = ' '.join(' '.join((p.extract_text() or '').split()) for p in pdf.pages)
    check('cross-layer' not in b and 'Two copies of a tile are completed only by its third copy.' in b and (b.count('W36-BONUS-FAC-v2') == 3 or b.count('W36-BONUS-FAC-v3') == 3),
          'bonus guide: the Problem 3 extension is replaced, footer v2 (v3 after the band-label fix)')

print(f'{len(FAIL)} failure(s)')
sys.exit(1 if FAIL else 0)
