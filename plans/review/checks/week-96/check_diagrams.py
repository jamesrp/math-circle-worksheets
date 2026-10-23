"""Diagram check for Week 96: tokens sit inside their bag outlines without overlapping,
the worked examples show the arithmetic their captions state, and every printed bag
matches its value label. Coordinates are read from the student LaTeX sources.

Finds the repository by walking up from this file until it sees lowell-math-circle-year-2/.
"""
import re
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = next(p for p in HERE.parents if (p / 'lowell-math-circle-year-2').is_dir())
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-96' / 'student'
fails = []


def check(cond, msg):
    print(('ok    ' if cond else 'FAIL  ') + msg)
    if not cond:
        fails.append(msg)


for name in ('grades-2-3.tex', 'grades-4-5.tex'):
    tex = (SRC / name).read_text()
    print('==', name)
    # \bag macro: outline (-.5,-.43)-(3.4,.43), tokens of diameter .52 at x = .58 i
    m = re.search(r'\\draw\[rounded corners=9pt\]\(([-\d.]+),([-\d.]+)\) rectangle \(([-\d.]+),([-\d.]+)\);\s*'
                  r'\\foreach \\v \[count=\\i from 0\] in \{#1\}\{\\node\[draw,circle,minimum size=([\d.]+)cm,inner sep=0pt\] at \(([\d.]+)\*\\i,0\)', tex)
    x0, y0, x1, y1, dia, step = map(float, m.groups())
    r = dia / 2
    bags = re.findall(r'\\bag\{([\d,]+)\}\\quad value (\d+)', tex)
    for toks, val in bags:
        t = [int(v) for v in toks.split(',')]
        last = step * (len(t) - 1)
        check(prod(t) == int(val), f'bag {t} labelled value {val}')
        check(-r > x0 and last + r < x1 and r < y1, f'bag {t}: tokens span {-r:.2f}..{last + r:.2f} inside outline {x0}..{x1}')
    check(step > dia, f'bag tokens do not overlap (step {step} > diameter {dia}, gap {step - dia:.2f} cm)')

    # page-1 example: card 20 -> 4 x 5 -> bag 2,2,5
    ex1 = tex.split(r'\begin{center}')[1].split(r'\end{center}')[0]
    check('{20}' in ex1 and '{4}' in ex1 and '{5}' in ex1 and '{2,2,5}' in ex1 and '4\\times5=20' in ex1
          and '2\\times2\\times5=20' in ex1, 'page-1 example: 20 -> 4 x 5 -> bag {2,2,5}, captions 4x5=20, 2x2x5=20')
    rect = tuple(map(float, re.search(r'\\draw\[rounded corners=9pt\]\(([\d.]+),([-\d.]+)\) rectangle\(([\d.]+),([\d.]+)\)', ex1).groups()))
    xs = [5.3 + .85 * i for i in range(3)]
    check(rect[0] < xs[0] - .275 and xs[-1] + .275 < rect[2], f'page-1 example tokens {xs} inside bag {rect[0]}..{rect[2]}')

    # page-2 example: three bags; shaded tokens are the chosen ones
    ex2 = tex.split(r'\begin{center}')[2].split(r'\end{center}')[0]
    outlines = [tuple(map(float, g)) for g in re.findall(r'\\draw\[rounded corners=9pt\]\(([-\d.]+),([-\d.]+)\) rectangle\(([-\d.]+),([-\d.]+)\)', ex2)]
    nodes = [(float(x), int(v), 'fill' in opts) for opts, x, v in
             re.findall(r'\\node\[(draw,circle[^\]]*)\] at\(([\d.]+),0\)\{(\d+)\}', ex2)]
    groups = [[n for n in nodes if o[0] < n[0] < o[2]] for o in outlines]
    for o, g in zip(outlines, groups):
        check(all(o[0] < x - .275 and x + .275 < o[2] for x, _, _ in g), f'page-2 example: tokens {[v for _, v, _ in g]} inside bag {o[0]}..{o[2]}')
    full, chosen, result = groups
    shaded = [v for _, v, f in chosen if f]
    unshaded = [v for _, v, f in chosen if not f]
    check(prod(v for _, v, _ in full) == 20 and 'value 20' in ex2, 'page-2 example: left bag has value 20')
    check([v for _, v, _ in chosen] == [v for _, v, _ in full], 'page-2 example: middle bag is the same bag')
    check(sorted(shaded) == sorted(v for _, v, _ in result) and prod(shaded) == 10 and 'value 10' in ex2,
          f'page-2 example: shaded {shaded} = right bag, value 10')
    check(prod(unshaded) == 2 and '20\\div10=2' in ex2 and '2\\times5=10' in ex2,
          f'page-2 example: unshaded {unshaded} gives the quotient 20/10 = 2 as captioned')

print('\nFAILURES:', len(fails))
for f in fails:
    print('  ', f)
