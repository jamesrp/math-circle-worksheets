#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 97. Standard library only.

1. The guide's K-1 route: squares 1x1 to 5x5 leave 1, 1, 0, 1, 1 in groups of 3
   (never 2) and 1, 0, 1, 0, 1 in groups of 4 (never 2 or 3).
2. The guide's counters picture: a 2x2 corner off a 5x5 square leaves 21 counters,
   a 3x5 strip and a 3x2 strip, which re-form as a 3x7 rectangle (three bundles of 7).
   The TikZ source of the picture is expanded and its dots counted.
3. The general L: a y-by-y corner off an x-by-x square leaves (x-y)(x+y) counters, and
   for the primes 3, 5, 7, 11 and inputs 0 <= y < x < p, p divides x^2 - y^2 exactly
   when x + y = p.
4. Problem 3's new question: with bundles of 7, 8 and 9 (inputs 0 to one less than the
   bundle size), bundle size 8 alone has an output that hides the most inputs (four).
5. Guide page 1 names what children find: two inputs per nonzero output for 3, 5, 7
   and 11; three or four for some output for 8, 9 and 15; nothing new past m - 1.
6. The problem files carry the new wording and the removed sentences are gone.

Run from anywhere: python3 card_fixes_2026_10_23.py
"""
import re
from collections import Counter
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


# 1. K-1 route
check([n * n % 3 for n in range(1, 6)] == [1, 1, 0, 1, 1], 'K-1: squares 1-5 in groups of 3 leave 1, 1, 0, 1, 1')
check([n * n % 4 for n in range(1, 6)] == [1, 0, 1, 0, 1], 'K-1: squares 1-5 in groups of 4 leave 1, 0, 1, 0, 1')
check(2 not in {n * n % 3 for n in range(200)} and {n * n % 4 for n in range(200)} == {0, 1},
      'K-1 key holds for every square: never 2 with groups of 3, never 2 or 3 with groups of 4')

# 2. The picture, expanded from the guide's TikZ source
guide = (WEEK / 'guide' / 'facilitator.tex').read_text()
start = guide.index('\\sub{Why the pairing is exact}')
pic = guide[guide.index('\\begin{tikzpicture}', start):guide.index('\\end{tikzpicture}', start)]


def expand(spec):
    spec = spec.strip()
    m = re.fullmatch(r'(-?\d+),\.\.\.,(-?\d+)', spec)
    return list(range(int(m[1]), int(m[2]) + 1)) if m else [int(v) for v in spec.split(',')]


def offset(expr, var, value):
    expr = expr.strip()
    m = re.fullmatch(r'(?:(-?[\d.]+)\+)?\\' + var, expr)
    return (float(m[1]) if m[1] else 0.0) + value


dots = []  # (kind, x, y)
loop = re.compile(r'\\foreach \\c in \{([^}]*)\} \\foreach \\r in \{([^}]*)\} '
                  r'\{\\(fill|draw)(\[[^\]]*\])? \(([^,]*),([^)]*)\) circle')
for cs, rs, op, style, xe, ye in loop.findall(pic):
    kind = 'open' if op == 'draw' else ('gray' if style and 'gray' in style else 'black')
    for c in expand(cs):
        for r in expand(rs):
            dots.append((kind, offset(xe, 'c', c), offset(ye, 'r', r)))
square = [d for d in dots if d[1] < 5]
rect = [d for d in dots if d[1] > 5]
sq = Counter(k for k, _, _ in square)
check(sorted((x, y) for _, x, y in square) == [(float(c), float(r)) for c in range(5) for r in range(5)],
      'picture: the square is a full 5x5 grid of 25 positions')
check(sq == Counter(black=15, gray=6, open=4), f'picture: square has 15 black, 6 gray, 4 open ({dict(sq)})')
opens = sorted((x, y) for k, x, y in square if k == 'open')
check(opens == [(3.0, 3.0), (3.0, 4.0), (4.0, 3.0), (4.0, 4.0)], 'picture: the open dots are a 2x2 corner')
dash = re.search(r'\\draw\[gray,dashed\] \(([\d.]+),([\d.]+)\) rectangle \(([\d.]+),([\d.]+)\)', pic)
check(dash is not None and all(float(dash[1]) < x < float(dash[3]) and float(dash[2]) < y < float(dash[4])
                                for x, y in opens)
      and not any(float(dash[1]) < x < float(dash[3]) and float(dash[2]) < y < float(dash[4])
                  for k, x, y in square if k != 'open'),
      'picture: the dashed outline encloses exactly the removed corner')
blacks = [(x, y) for k, x, y in square if k == 'black']
grays = [(x, y) for k, x, y in square if k == 'gray']
check(len({x for x, _ in blacks}) == 3 and len({y for _, y in blacks}) == 5
      and len({x for x, _ in grays}) == 2 and len({y for _, y in grays}) == 3,
      'picture: the L is a 3x5 strip (black) and a 3x2 strip (gray)')
rows = sorted({y for _, _, y in rect})
check(len(rows) == 3 and all(Counter(k for k, _, y in rect if y == r) == Counter(black=5, gray=2) for r in rows),
      'picture: the rectangle has 3 rows, each 5 black and 2 gray, so 3x7 = 21')
check(Counter(k for k, _, _ in rect) == Counter(black=15, gray=6), 'picture: the same 15 black and 6 gray counters move')
loops = re.findall(r'\\draw\[rounded corners=[^\]]*\] \(([\d.]+),([\d.]+)\+\\r\) rectangle \(([\d.]+),([\d.]+)\+\\r\)', pic)
ring_rows = re.search(r'\\foreach \\r in \{([^}]*)\} \{\\draw\[rounded corners', pic)
ok = False
if loops and ring_rows:
    x0, y0, x1, y1 = map(float, loops[0])
    bundles = [[d for d in rect if x0 < d[1] < x1 and y0 + r < d[2] < y1 + r] for r in expand(ring_rows[1])]
    ok = len(bundles) == 3 and all(len(b) == 7 for b in bundles) and sum(map(len, bundles)) == len(rect)
check(ok, 'picture: each of the three rounded loops holds one row of 7 (three bundles of 7)')
check(25 - 4 == 21 == 3 * 5 + 3 * 2 == 3 * 7 and (5 - 2) * (5 + 2) == 21, 'picture: 25 - 4 = 21 = 3x5 + 3x2 = 3x7')
check(5 * 5 % 7 == 2 * 2 % 7 == 4, 'picture: inputs 5 and 2 share output 4 with bundles of 7')

# 3. The general L and the prime pairing
check(all(x * x - y * y == (x - y) * (x + y) for x in range(40) for y in range(x + 1)),
      'L: a y-by-y corner off an x-by-x square leaves (x-y)(x+y) counters (checked to 39)')
for p in (3, 5, 7, 11):
    check(all(((x * x - y * y) % p == 0) == (x + y == p) for x in range(p) for y in range(x)),
          f'bundles of {p}: distinct inputs below {p} share an output exactly when they sum to {p}')

# 4. Problem 3's question
most = {}
for m in (7, 8, 9):
    groups = Counter(n * n % m for n in range(m))
    top = max(groups.values())
    most[m] = (top, sorted(o for o, k in groups.items() if k == top))
check(most == {7: (2, [1, 2, 4]), 8: (4, [1]), 9: (3, [0])}, f'Problem 3: most inputs per output {most}')
best = max(v[0] for v in most.values())
check([m for m in most if most[m][0] == best] == [8], 'Problem 3: bundle size 8 alone has an output hiding the most inputs')
check(Counter(n * n % 8 for n in range(8))[0] == 2 and Counter(n * n % 9 for n in range(9))[0] == 3
      and [n for n in range(4) if n * n % 4 == 0] == [0, 2],
      'guide follow-up: output 0 hides 2 inputs for 8, 3 for 9, and 0 and 2 for bundles of 4 on page 1')
check(len({n * n % 7 for n in range(200)}) == len({n * n % 7 for n in range(7)}) == 4,
      'Problem 5: inputs past 6 give no new output with bundles of 7 (checked to 199)')

# Guide page 1, "Discovery and readiness": what children find
for m in (3, 5, 7, 11):
    g = Counter(n * n % m for n in range(m))
    check(all(k == 2 for o, k in g.items() if o) and g[0] == 1, f'page 1: bundles of {m} give two inputs per nonzero output')
for m in (8, 9, 15):
    g = Counter(n * n % m for n in range(m))
    check(max(g.values()) in (3, 4), f'page 1: bundles of {m} have an output with {max(g.values())} inputs')
check(all({n * n % m for n in range(m, 300)} <= {n * n % m for n in range(m)} for m in range(1, 20)),
      'page 1: no new output from inputs past m - 1 (bundle sizes 1-19, inputs to 299)')

# 6. Wording in the problem files
prob = {p.name: p.read_text() for p in (WEEK / 'problems').glob('*.md')}
check('We compare outputs' not in prob['00-square-rules.md'], 'rules: the "We compare outputs" sentence is gone')
p3 = prob['03-seven-eight-nine.md']
check('Use bundles of 7, 8 and 9, each with inputs from 0 to one less than the bundle size.' in p3
      and 'Which bundle size has an output that hides the most inputs?' in p3
      and 'Can output 0' not in p3 and 'hide among' not in p3, 'Problem 3 carries the new wording')
check('Try larger squares' not in prob['05-bigger-inputs.md']
      and 'Settle the question for every whole-number input.' in prob['05-bigger-inputs.md'],
      'Problem 5 carries the new wording')
check('one less than the bundle size' in prob['06-odd-prime-rule.md'], 'Problem 3 now matches Problem 6\'s phrasing')

print(f'{len(fails)} failure(s)')
raise SystemExit(1 if fails else 0)
