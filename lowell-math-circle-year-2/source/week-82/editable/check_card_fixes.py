#!/usr/bin/env python3
"""Check the claims, keys and wording changed by the October 23, 2026 card fixes (v2).

Standard library only. Reads student/students.tex (written from the problem files by
student/regenerate.py) and guide/facilitator.tex beside this file. W is an endless row
(order type omega) and S a star; an arrangement is read left to right.
"""
from itertools import combinations, permutations
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
fails = []

def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        fails.append(name)

def shape(arr):
    """Ordinal sum of the arrangement as (a, b) for omega*a + b: a star adds 1, a row
    absorbs every finite part before it (b + omega = omega)."""
    a = b = 0
    for x in arr:
        a, b = (a + 1, 0) if x == 'W' else (a, b + 1)
    return a, b

def arrangements(rows):
    return sorted({p for s in range(3) for p in permutations('W' * rows + 'S' * s)})

two = [''.join(p) for p in arrangements(2)]
groups = {}
for arr in two:
    groups.setdefault(shape(arr), []).append(arr)
check('P4: two rows and up to two stars give ten arrangements of three shapes',
      len(two) == 10 and len(groups) == 3)
same = sum(len(g) * (len(g) - 1) // 2 for g in groups.values())
check(f'P4: {same} same-shape pairs and {45 - same} others among the 45 pairs', (same, 45 - same) == (18, 27))
check('P4: WSW has the shape of WW; WWS does not', shape('WSW') == shape('WW') != shape('WWS'))

# The WSW-to-WW match: R_n -> R_n, star -> B1, B_n -> B_(n+1), checked on the first 2000 kids
# of each row: it is increasing, one-to-one, and reaches every kid of WW up to B2000.
N = 2000
wsw = [('R', n) for n in range(1, N + 1)] + [('*', 0)] + [('B', n) for n in range(1, N + 1)]
pos_ww = {k: i for i, k in enumerate([('R', n) for n in range(1, N + 2)] + [('B', n) for n in range(1, N + 2)])}
f = {('*', 0): ('B', 1), **{('R', n): ('R', n) for n in range(1, N + 1)}, **{('B', n): ('B', n + 1) for n in range(1, N + 1)}}
images = [pos_ww[f[k]] for k in wsw]
check('P4 key: star -> B1, Bn -> B(n+1) keeps order and is one-to-one (first 2000 of each row)',
      all(x < y for x, y in zip(images, images[1:])))
check('P4 key: every kid of WW up to R2000 and B2000 is reached', {f[k] for k in wsw} >= {('R', n) for n in range(1, N + 1)} | {('B', n) for n in range(1, N + 1)})
check('P4 key: WWS has a last kid and WW has none (shapes (2, 1) and (2, 0))', shape('WWS') == (2, 1) and shape('WW') == (2, 0))

def panels(arr):
    """'This kid comes after EVERY kid' panels: one for each star placed right after a row."""
    return sum(1 for x, y in zip(arr, arr[1:]) if x == 'W' and y == 'S')
check('p. 6: WSWS beside WWS needs three "This kid" panels, and no same-shape pair needs more',
      panels('WSWS') + panels('WWS') == 3
      and max(panels(x) + panels(y) for g in groups.values() for x, y in combinations(g, 2)) == 3)

# Guide table: the six shapes for one or two rows.
names = {(1, 0): r'$\omega$ (one row)', (1, 1): r'$\omega+1$', (1, 2): r'$\omega+2$',
         (2, 0): r'$\omega\cdot2$ (two rows)', (2, 1): r'$\omega\cdot2+1$', (2, 2): r'$\omega\cdot2+2$'}
guide = (HERE / 'guide' / 'facilitator.tex').read_text()
rows = dict(re.findall(r'^(\$\\omega[^&]*?) & ([A-Z, ]+?)(?:\\\\)?$', guide, re.M))
ok = len(rows) == 6
for rowcount in (1, 2):
    for arr in arrangements(rowcount):
        s = shape(arr)
        ok &= ''.join(arr) in [x.strip() for x in rows.get(names[s], '').split(',')]
ok &= sum(len(v.split(',')) for v in rows.values()) == len(arrangements(1)) + len(arrangements(2))
check('guide table lists every one- and two-row arrangement under its shape, and nothing else', ok)

# Launch demonstration: top 1 <-> bottom 2, top 2 <-> bottom 1, top 3 <-> bottom 4, ...
partner = lambda n: n + 1 if n % 2 else n - 1
check('launch: top kid 20 is matched with bottom 19, and the rule is a complete match',
      partner(20) == 19 and all(partner(partner(n)) == n for n in range(1, 10001))
      and sorted(partner(n) for n in range(1, 1001)) == list(range(1, 1001)))

# K-1 route on Problem 1: six ways, only straight across has no crossing yarn.
ways = list(permutations((1, 2, 3)))
uncrossed = [p for p in ways if not any(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))]
check('K-1 key: six complete matches of three with three, one with no crossings (straight across)',
      len(ways) == 6 and uncrossed == [(1, 2, 3)])

# Student pages.
tex = (HERE / 'student' / 'students.tex').read_text()
check('P1 asks for every complete match', 'Find every complete match between these two class lines.' in tex)
check('P2 and P3 ask "Can a complete match keep order?"', tex.count('Can a complete match keep order?') == 2
      and 'Can a match keep order?' not in tex)
check('P1 drops "Use cards and yarn"', 'Use cards and yarn' not in tex)
check('P3 drops "There is no last red kid."', 'There is no last red kid' not in tex)
check('P4 asks for two endless rows', 'Arrange two endless numbered rows and up to two' in tex and 'one or two endless' not in tex)
check('answer lines 1 cm apart', r'\newcommand{\ruleline}{\vspace{1cm}\hrule height0.3pt\vspace{1cm}\hrule height0.3pt}' in tex)
m = re.search(r'\\foreach \\y in \{([^}]*)\}\{\n \\draw\[dashed,gray\] \(-0\.1,\\y\) rectangle \+\+\(16\.0,-2\.25\);\n \\node[^\n]*\{This kid comes after EVERY kid', tex)
check('p. 6 prints three "This kid comes after EVERY kid" panels', m is not None and len(m.group(1).split(',')) == 3)
footer = re.search(r'\\fancyfoot\[L\]\{[^\n]*', tex).group(0)
check('footer W82-S-v2, no "draft"', footer.endswith('/ W82-S-v2}') and 'draft' not in footer)
check('four problems, six pages', re.findall(r'\\problem\{(\d+)\}', tex) == ['1', '2', '3', '4'] and tex.count(r'\newpage') == 5)

# Adult guide.
flat = ' '.join(guide.split())
for phrase in [r'\rhead{Adult guide}', 'Week 82 / W82-FAC-v2', 'route on Problem 1 (see the next page)', 'row, star, row has type $\\omega+1+\\omega=\\omega+\\omega$',
               "``Who is top kid 20's partner?'' (Bottom 19", 'join partners with yarn',
               'K--1, adult-led on Problem 1', 'only straight across (R1--B1, R2--B2, R3--B3) has no crossings',
               'If both lines show numbered kids 1--6, B also shows its star', '18 two-row pairs', 'the other 27 two-row pairs',
               'The surprise is WSW with WW', r'$\bigstar\mapsto$ B1 and B$n\mapsto$ B$(n+1)$',
               'WW with WWS has a complete match but none that keeps order', 'ask about B1, the first blue kid in D']:
    check(f'guide says "{phrase}"', phrase in flat)
for phrase in ['Facilitator draft', 'Matching only six physical cards', 'first kid of block B',
               'Each construction uses one row', 'Grades 3--5 only']:
    check(f'guide no longer says "{phrase}"', phrase not in flat)

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
