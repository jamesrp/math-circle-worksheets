#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes for Week 20 (see card-fixes-2026-10-23.md).

Run after build.sh has built the packets and the guide (it is the last step of build.sh).
Reads the problem files (repository or ZIP layout), the generated LaTeX in src/ and the
guide in build/. Every line printed starts with PASS; any failure stops with an error.
"""
import itertools
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent           # the editable package
LAYOUTS = [(ROOT / 'problem-files', ROOT / 'problem-files' / 'tools'),
           (ROOT.parent, ROOT.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 20 problem files and tools.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
fig = w.figures
tex = {b: (ROOT / 'src' / f'{b}.tex').read_text() for b in ('k-1', 'grades-2-3', 'grades-4-5')}
guide = ROOT / 'build' / 'facilitator-guide.pdf'
gpages = subprocess.run(['pdftotext', '-layout', str(guide), '-'], capture_output=True, text=True, check=True).stdout.split('\f')
gpages = [p for p in gpages if p.strip()]
out = []


def ok(cond, msg):
    if not cond:
        sys.exit('FAIL: ' + msg)
    out.append('PASS: ' + msg)


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj


# Should 1: spare recording boards on the K-1 pages that ask for every way.
two_cube = [v for v in itertools.product(range(4), repeat=3) if sum(v) == 6]          # three squares share to 2
cards = [v for v in itertools.permutations(range(5), 3) if v[0] + v[2] == 2 * v[1]]  # distinct cards, circle in the middle
tri = adjacency(3, [(0, 1), (1, 2), (2, 0)])
path4 = adjacency(4, [(0, 1), (1, 2), (2, 3)])
const = lambda adj: [v for v in itertools.product(range(6), repeat=len(adj)) if all(len(adj[i]) * v[i] == sum(v[j] for j in adj[i]) for i in range(len(adj)))]
boards = {
    'two-cube circle': (sum(len(xs) for _, xs in fig['RECORD_ROWS_2CUBE']), len(two_cube), 10),
    'three different cards': (2 * len(fig['RECORD_ROWS_CARDS']), len(cards), 8),
    'no-square triangle': (len(fig['RECORD_TRIANGLES']), len(const(tri)), 6),
    'no-square path': (2 * len(fig['RECORD_PATH_ROWS']), len(const(path4)), 6),
}
for name, (printed, answers, expected) in boards.items():
    ok(answers == expected and printed - answers in (2, 3),
       f'K-1 {name}: {answers} fillings (enumerated), {printed} recording boards ({printed - answers} spare)')
# The recording boards on each page do not overlap one another (bounding boxes, inches).
def disjoint(boxes):
    return all(a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1] for a, b in itertools.combinations(boxes, 2))
ok(disjoint([(x - .45 - .21, y - .35 - .21, x + .45 + .21, y + .60 + .21) for y, xs in fig['RECORD_ROWS_2CUBE'] for x in xs]),
   'two-cube recording boards are separate')
ok(disjoint([(x - .34 - .19, y - .22 - .19, x + .34 + .19, y + .30 + .19) for x, y in fig['RECORD_TRIANGLES']]) and
   min(x - .53 for x, y in fig['RECORD_TRIANGLES']) > 2.30 + 1.05 + .595 and max(x + .53 for x, y in fig['RECORD_TRIANGLES']) < 7.86 and
   min(y - .41 for x, y in fig['RECORD_TRIANGLES']) > 4.75 + .595,
   'small triangles clear each other, the large triangle, the margin and the large path')
ok(min(fig['RECORD_PATH_ROWS']) - .21 > .48 + .2 and max(fig['RECORD_PATH_ROWS']) + .21 < 4.75 - .595,
   'small paths sit between the large path and the footer')

# Should 2: linked circles after the inverse pages, in the packet and in the guide.
k1 = [a for a in w.atoms if 'K-1' in a.grades and a.numbered]
ok([a.meta['id'] for a in k1][:4] == ['w20.k1-one-circle', 'w20.k1-two-cube-circle', 'w20.k1-cards', 'w20.k1-linked-circles'],
   'K-1 order: one circle, two-cube circle, cards, linked circles (Problems 1-4)')
titles = {}
for i, page in enumerate(gpages, 1):
    m = re.search(r'K-1 Problem (\d)\s*\n\s*Student page (\d) \| ([^\n|]+)', page)
    if m:
        titles[int(m.group(1))] = (i, int(m.group(2)), m.group(3).strip())
ok([titles[n][1] for n in range(1, 8)] == list(range(1, 8)) and [titles[n][0] for n in range(1, 8)] == list(range(5, 12)),
   'guide pages 5-11 are K-1 Problems 1-7 with matching student pages')
ok(titles[2][2] == 'Revised inverse construction' and titles[3][2] == 'Three different cards' and titles[4][2] == 'Keep both circles correct together',
   'guide K-1 Problems 2, 3 and 4 are the two-cube circle, the cards and the linked circles')
ok('inverse-build Problem 2 or 3' in gpages[2] and 'linked-circle Problem 4' in gpages[2] and 'K-1 Problem 3, write 0, 1, 2, 3 and 4' in ' '.join(gpages[2].split()),
   'guide page 3: table routes and the card note use the new numbers')
ok('collections P2 or P3' in ' '.join(gpages[-1].split()) and 'linked circles in P4' in ' '.join(gpages[-1].split()),
   'route note uses the new K-1 numbers')

# Should 3: Grades 4-5 fraction cards include values no board needs.
needed = set()
for a, b, inner in [(0, 1, 1), (0, 3, 2), (0, 2, 1), (0, 1, 2)]:
    vals = [Fraction(a) + Fraction(b - a, inner + 1) * k for k in range(1, inner + 1)]
    needed |= {v for v in vals if v.denominator > 1}
printed = {Fraction(n, d) for n, d in fig['FRACTION_CARDS']}
ok(needed == {Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)} and needed < printed and printed - needed == {Fraction(1, 4), Fraction(3, 4)},
   'Grades 4-5 Problem 7 needs 1/2, 1/3, 2/3; cards print those and 1/4, 3/4, which fit no board')
ok(all(r'\frac{' + f'{n}}}{{{d}' + '}' in tex['grades-4-5'] for n, d in fig['FRACTION_CARDS']), 'all five cards are in the Grades 4-5 LaTeX')

# Should 4: captions that repeated the rules are gone; the pictures stay.
for cap, band in [('Both square stacks stay', 'k-1'), ('Keep all four stacks', 'k-1'),
                  ('same unchanged board', 'grades-2-3'), ('same unchanged board', 'grades-4-5')]:
    ok(cap not in tex[band], f'caption "{cap}" is gone from {band}')
ok(tex['k-1'].count("0's mat") == 1 and tex['k-1'].count('Share copies') == 2 and tex['grades-2-3'].count('Example: both circles work.') == 1
   and tex['grades-4-5'].count('Example: both circles work.') == 1, 'the worked examples themselves remain')

# Should 5: equal gaps and uniqueness are on guide page 4.
p4 = ' '.join(gpages[3].split())
ok('Averages and equal gaps' in p4 and 'Uniqueness.' in p4, 'guide page 4 holds the equal-gap and uniqueness arguments')
refs = [i + 1 for i, p in enumerate(gpages) if re.search(r'\bpage 4\b', ' '.join(p.split()))]
ok(not any(re.search(r'\bon page 3\b|\buse page 3\b', ' '.join(p.split())) for p in gpages) and {9, 16, 18} <= set(refs),
   f'guide pages 9, 16 and 18 point to page 4 (page 4 is named on pages {refs})')

# Coulds 6, 7, 8, 9.
ok('Can any board have a second filling with the same square numbers?' in tex['grades-4-5'] and 'Try to find a second filling' not in tex['grades-4-5'],
   'Grades 4-5 Problem 1 asks whether a second filling exists')
ok(r'(2+4)\div 2=3' in tex['grades-2-3'] and r'(2+4)/2=3' in tex['grades-4-5'], 'Grades 2-3 example uses the division sign; Grades 4-5 keeps the slash')
p3 = ' '.join(gpages[2].split())
ok('edge strips' not in p3 and 'seventh place' not in p3 and 'halves, thirds and quarters' in p3, 'guide page 3 lists only materials the tasks use')
n = len(gpages)
ok(n == 26 and all(f'{i} / {n}' in ' '.join(p.split()) for i, p in enumerate(gpages, 1)), f'every guide page footer reads N / {n}')
ok(all(p.strip().startswith('Bellingham Math Circle / Averaging / Adult guide') for p in gpages), 'every guide page, the route note included, has the same header')

# Versions.
for band, fid in [('k-1', 'GA20-K-v4'), ('grades-2-3', 'GA20-23-v3'), ('grades-4-5', 'GA20-45-v4')]:
    ok(fid in tex[band] and fid in ' '.join(gpages[24].split()), f'{band} prints {fid}, as the guide says')

print('\n'.join(out))
