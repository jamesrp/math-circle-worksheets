#!/usr/bin/env python3
"""Check the Week 72 card fixes of October 23, 2026 in the printed PDFs.

Usage: python3 check_card_fixes.py [folder]
The folder holds week-72-students.pdf and week-72-facilitator.pdf (default: the print
folder). Needs PyMuPDF. The memories, the rival card rule and the launch example are
recomputed here from the robot's rules; the printed pages are read for the changes.
"""
from itertools import permutations
from pathlib import Path
import re
import sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FOLDER = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'lowell-math-circle-year-2' / 'week-72'
SOURCE = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-72'
CM = 72 / 2.54
FAILS = []


def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name)
    if not cond:
        FAILS.append(name)


def walk(route, x=0, y=0, z=0):
    """The robot: N adds the column to the memory, S subtracts it."""
    for m in route:
        if m == 'E': x += 1
        elif m == 'W': x -= 1
        elif m == 'N': z += x; y += 1
        elif m == 'S': z -= x; y -= 1
    return x, y, z


def outline(start, route):
    """Final memory of a closed route from a start corner, and its card count."""
    x, y, z = walk(route, *start, 0)
    assert (x, y) == start, route
    return z, len(route)


# ------------------------------------------------------------------ mathematics
routes = sorted({''.join(p) for p in permutations('EENN')})
mem = {r: walk(r)[2] for r in routes}
check('P1: six routes with memories 4,3,2,2,1,0', [mem[r] for r in ['EENN', 'ENEN', 'ENNE', 'NEEN', 'NENE', 'NNEE']] == [4, 3, 2, 2, 1, 0])


def squares_left(route):
    """Unit squares of the 2-by-2 block lying left of the route, row by row."""
    x, y, count = 0, 0, 0
    for m in route:
        if m == 'E': x += 1
        else: count += x; y += 1   # in row y the squares 0..x-1 are left of the N step
    return count


check('fix 4: every P1 route remembers the squares of the block to its left (EENN 4, ENNE and NEEN 2, NNEE 0)',
      all(squares_left(r) == mem[r] for r in routes) and [squares_left(r) for r in ('EENN', 'ENNE', 'NEEN', 'NNEE')] == [4, 2, 2, 0])

shapes = {
    'unit loop (P2)': ((0, 0), 'ENWS'),
    'rectangle at column 0': ((0, 0), 'EENWWS'),
    'rectangle at column 2': ((2, 0), 'EENWWS'),
    'rectangle at column -3': ((-3, 0), 'EENWWS'),
    'L': ((0, 0), 'EENWNWSS'),
    '2-by-2 square': ((0, 0), 'EENNWWSS'),
}
rev = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}
res = {}
for k, (s, r) in shapes.items():
    ccw, cards = outline(s, r)
    cw, _ = outline(s, ''.join(rev[m] for m in reversed(r)))
    res[k] = (ccw, cw, cards)
check('fix 1: the three rectangles remember +2 and -2', all(res[k][:2] == (2, -2) for k in res if k.startswith('rectangle')))
check('fix 1: the L remembers +3 and -3 and the square +4 and -4, both with 8 cards',
      res['L'] == (3, -3, 8) and res['2-by-2 square'] == (4, -4, 8))
rival = lambda cards: cards // 2 - 1
check('fix 1: the rival rule "half the cards minus one" fits the unit loop, rectangles and L',
      all(res[k][0] == rival(res[k][2]) for k in res if k != '2-by-2 square'))
check('fix 1: the rival rule fails on the square (predicts 3, memory 4)', rival(8) == 3 and res['2-by-2 square'][0] == 4)
check('fix 3: at column -2, N takes memory 0 to -2 and S brings it back to 0',
      walk('N', -2, 0, 0)[2] == -2 and walk('NS', -2, 0, 0)[2] == 0)

# ------------------------------------------------------------------ printed pages


def words(page):
    return re.sub(r'(\w)- (\w)', r'\1\2', re.sub(r'\s+', ' ', page.get_text()).strip())


s = pymupdf.open(FOLDER / 'week-72-students.pdf')
st = [words(p) for p in s]
check('student packet: 5 pages, every footer GGT72-S-v2', len(s) == 5 and all('GGT72-S-v2' in t for t in st))
check('could 8: page 1 drops "so you can replay it" and "Swap jobs for the next route"',
      'replay' not in st[0] and 'Swap jobs' not in st[0] and 'Keep the cards in order, or write a longer route as letters. Each trial' in st[0])
tips = [d for d in s[0].get_drawings() if d['type'] == 'fs' and [i[0] for i in d['items']] == ['l'] * 4]
dots = sorted([d for d in s[0].get_drawings() if d['type'] == 'f' and [i[0] for i in d['items']] == ['c'] * 4
               and d['rect'].width / CM < .15], key=lambda d: d['rect'].x0)
first = dots[0]['rect'] if dots else None
check('could 5: three arrow tips in the example, none at the start panel\'s dot',
      len(tips) == 3 and first is not None and all(abs(t['rect'].x0 - first.x0) / CM > .5 for t in tips))
W = s[1].rect.width
long_rules = [d for d in s[1].get_drawings() if d['rect'].width > .56 * W and d['rect'].height < 2]
check('fix 2: Problem 2 has six answer lines (plus the header rule)', len(long_rules) == 7)
check('could 6: Problem 3 no longer says "Write each memory beside an arrow"', 'beside an arrow' not in st[2])
blanks = [d for d in s[2].get_drawings() if abs(d['rect'].width - .65 * 72) < 1 and d['rect'].height < 2]
arcs = [d for d in s[2].get_drawings() if d['type'] == 's' and any(i[0] == 'c' for i in d['items']) and d['rect'].width / CM < .5]
check('fix 1 and could 6: Problem 3 has five outlines with ten blanks, each after a turn arrow', len(blanks) == 10 and len(arcs) == 10)
check('fix 1: Problem 3 prints the column-0, column-2, column-(-3), L and square boards',
      st[2].count('0 1 2 3') == 3 and '2 3 4 5' in st[2] and '-3 -2 -1 0' in st[2])
check('could 7: page 5 no longer says "Extra workspace for every problem."', 'Extra workspace' not in st[4] and st[4].split('Grades 4–5 ')[1].startswith('Cut out the memory strip'))

g = pymupdf.open(FOLDER / 'week-72-facilitator.pdf')
gt = ' '.join(words(p) for p in g)
check('guide: 3 pages, GGT72-FAC-v2, matches GGT72-S-v2', len(g) == 3 and all('GGT72-FAC-v2' in words(p) for p in g)
      and re.search(r'GGT72-S-?v2', gt) is not None)
check('fix 3: the launch shows the column -2 N and S example and the marker reading',
      'Then show a negative column: at column −2, N moves the memory marker from 0 to −2' in gt
      and 'right for a positive column and left for a negative one; S moves it the other way' in gt)
check('fix 3: the rehearsal paragraph no longer repeats the example', gt.count('subtracting −2') == 1)
check('fix 4: the P1 key gives the squares-to-the-left reading and the held hint',
      'number of squares of the 2-by-2 block to the left of the route' in gt and 'Shade the squares left of your route.' in gt)
check('fix 1: the P3 key gives the square and the rival rule',
      '2-by-2 square +4 and −4' in gt and 'half the number of cards, minus one' in gt and 'remembers 4, its area' in gt)
check('could 7: the materials count page 5 once', 'the four problem pages, and page 5 pre-cut' in gt and 'prepared apparatus sheet' not in gt)
check('could 10: MATHEMATICS.md no longer cites topics.json', 'topics.json' not in (SOURCE / 'editable' / 'MATHEMATICS.md').read_text())

print(f'{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
