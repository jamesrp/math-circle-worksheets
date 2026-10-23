#!/usr/bin/env python3
"""Check the student-page changes of the October 23, 2026 card fixes (Week 26).

Reads the printed shapes from the problem files' figures.py (problem-files/ in the
portable ZIP, the week folder in the repository) and checks the mathematics the
changed pages and guide rely on, by direct counting and exhaustive search:

- Grades 4-5 Problem 2 now says that two tiles touching at a corner leave no gap.
  Under that rule a twelve-tile shape with the longest boundary, 26, can have a hole;
  if a corner gap let the inside out, none could (the full census of trees up to 12
  tiles is in verify_card_fixes_2026_10_23.py).
- Grades 4-5 Problem 3's third shape is now rows 5; 3 plus a separate tile; 2; 1:
  12 tiles, 4 rows, 5 columns, boundary 20, two more than 2 x (rows + columns).
  The least boundary for a shape occupying 4 rows and 5 columns is still 18.
- Grades 2-3 Problem 2 prints three recording boxes per start; no start allows more
  than two different changes, so every start keeps a spare box.

Standard library only. Run from anywhere: python3 review/verify_student_fixes_2026_10_23.py
"""
import importlib.util
import itertools
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
WEEK = next(w for w in (PACKAGE / 'problem-files', PACKAGE.parent) if (w / 'figures.py').exists())
spec = importlib.util.spec_from_file_location('week26_figures', WEEK / 'figures.py')
fig = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(fig)

SIDE = ((1, 0), (-1, 0), (0, 1), (0, -1))
EIGHT = SIDE + ((1, 1), (1, -1), (-1, 1), (-1, -1))


def perimeter(s):
    return sum((x + dx, y + dy) not in s for x, y in s for dx, dy in SIDE)


def shared(s):
    return sum((x + dx, y + dy) in s for x, y in s for dx, dy in SIDE) // 2


def connected(s):
    s = set(s)
    start = next(iter(s)); seen = {start}; todo = [start]
    while todo:
        x, y = todo.pop()
        for dx, dy in SIDE:
            p = (x + dx, y + dy)
            if p in s and p not in seen:
                seen.add(p); todo.append(p)
    return seen == s


def span(s):
    return len({y for x, y in s}), len({x for x, y in s})


def runs(s):
    """Number of maximal horizontal runs (one per row exactly when no row has a gap)."""
    return sum(1 for x, y in s if (x - 1, y) not in s)


def has_hole(s, steps):
    """SIDE steps: a corner contact closes a gap. EIGHT steps: a corner gap leaks."""
    x0 = min(x for x, y in s) - 1; x1 = max(x for x, y in s) + 1
    y0 = min(y for x, y in s) - 1; y1 = max(y for x, y in s) + 1
    space = {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)} - set(s)
    seen = {(x0, y0)}; todo = [(x0, y0)]
    while todo:
        x, y = todo.pop()
        for dx, dy in steps:
            p = (x + dx, y + dy)
            if p in space and p not in seen:
                seen.add(p); todo.append(p)
    return len(seen) < len(space)


checks = []

# Grades 4-5 Problem 2: the page's corner rule, and the guide's point-sealed example.
p2 = (WEEK / 'problems/14-longest-twelve.md').read_text()
assert 'Two tiles that touch at a corner leave no gap between them.' in p2.split('## figure')[0]
assert 'none of them a straight row' in p2
example = {(1, 0), (2, 0), (0, 1), (2, 1)} | {(x, 2) for x in range(8)}
assert len(example) == 12 and connected(example) and shared(example) == 11 and perimeter(example) == 26
assert has_hole(example, SIDE) and not has_hole(example, EIGHT)
checks.append('4-5 P2: the page states that corner contacts close gaps; under that rule the guide\'s '
              '12-tile tree (11 shared sides, boundary 26) has a hole, and under the other rule it has none')
guide = (PACKAGE / 'facilitator-src/build_guide.py').read_text()
assert 'leaves this open' not in guide and 'leaves open' not in (PACKAGE / 'facilitator-src/overview-content.json').read_text()
assert "A hole: yes, sealed at a corner." in guide and 'tree adjacency implies no holes' in guide
checks.append('guide: no longer says the page leaves the corner convention open; p. 14 answers yes under the page\'s rule')

# Grades 4-5 Problem 3: the three printed shapes.
triples = []
for s in fig.shape3:
    s = set(s)
    assert len(s) == 12 and connected(s)
    r, c = span(s)
    triples.append((r, c, perimeter(s)))
assert triples == [(2, 6, 16), (3, 4, 14), (4, 5, 20)], triples
third = set(fig.shape3[2])
assert [perimeter(set(s)) - 2 * sum(span(set(s))) for s in fig.shape3] == [0, 0, 2]
assert runs(third) == 5 and sorted(sum(1 for x, y in third if y == row) for row in range(4)) == [1, 2, 4, 5]
checks.append('4-5 P3: printed (rows, columns, boundary) = (2,6,16), (3,4,14), (4,5,20); only the third '
              'exceeds 2 x (rows + columns), by 2, because its second row has two runs')
guide_triple = re.search(r'triples, left to right, are <b>([^<]*)</b>', guide).group(1)
assert guide_triple == '(2,6,16), (3,4,14), (4,5,20)', guide_triple
assert "'4 rows, 5 columns, P = 20'" in guide
checks.append('guide p. 15: triples and caption match the printed shapes')

# Least boundary over every connected shape occupying exactly 4 rows and 5 columns.
box = [(x, y) for y in range(4) for x in range(5)]
best_any, twelve = None, set()
for mask in range(1, 1 << 20):
    if bin(mask).count('1') < 8:          # 4 rows and 5 columns need at least 8 tiles to connect
        continue
    s = {box[i] for i in range(20) if mask >> i & 1}
    if span(s) != (4, 5) or not connected(s):
        continue
    p = perimeter(s)
    best_any = p if best_any is None else min(best_any, p)
    if len(s) == 12:
        twelve.add(p)
assert best_any == 18 and sorted(twelve) == [18, 20, 22, 24, 26]
checks.append('4-5 P3: over all connected shapes occupying 4 rows and 5 columns the least boundary is 18; '
              'twelve-tile ones reach 18, 20, 22, 24 and 26')

# Grades 2-3 Problem 2: three boxes per start, at most two changes per start.
changes = []
for s in fig.start2:
    s = set(s)
    empty = {(x + dx, y + dy) for x, y in s for dx, dy in SIDE} - s
    changes.append(sorted({perimeter(s | {e}) - perimeter(s) for e in empty}))
assert changes == [[2], [0, 2], [-2, 2], [-4, 2]], changes
tex = fig.m_add_one_tile()
assert tex.count('After:') == 12 and tex.count('Change:') == 12
xs = sorted({float(x) for x in re.findall(r'\\begin\{scope\}\[shift=\{\(([\d.]+),', tex)})
assert xs == [64, 108, 152] and all(b - a >= 39 + 4 for a, b in zip(xs, xs[1:])) and xs[-1] + 39 <= 199
assert max(15 + 8 * (x + 1) for s in fig.start2 for x, y in s) <= xs[0] - 8
checks.append('2-3 P2: change sets {+2}, {0,+2}, {-2,+2}, {-4,+2}; three boxes per start, so each start '
              'keeps at least one spare; boxes do not overlap each other, the starts or the margin')

# Grades 4-5 Problem 6 says tiles; the answers are unchanged.
p6 = (WEEK / 'problems/18-area-rule.md').read_text().split('## key')[0]
assert 'squares' not in p6.split('+++')[2] and 'tiles; boundary' in fig.u_rule_grids()
for n, best in ((37, 26), (50, 30), (73, 36)):
    assert min(2 * (r + c) for r in range(1, n + 1) for c in range(1, n + 1) if r * c >= n) == best
checks.append('4-5 P6: the page and labels say tiles; least boundaries 26, 30, 36 for 37, 50, 73')

for c in checks:
    print('PASS', c)
print(f'PASS: {len(checks)} Week 26 student-page checks')
