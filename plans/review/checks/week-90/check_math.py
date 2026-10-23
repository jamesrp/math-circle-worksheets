#!/usr/bin/env python3
"""Independent mathematical checks for Week 90 (Sliding number arrays).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

What it checks
- Parses every grid drawn in student/students.tex and student/materials.tex
  (cell kind: white/number, gray = missing, dark = outside, ring = hole, and
  the S/E markers) straight from the TikZ coordinates, and names each grid by
  the card title printed above it.
- Card data: the A, D and B cards on the materials pages, and every copy of a
  card shown on the student pages, agree; each card is increasing; each card
  family is exactly the set of all increasing fillings of its skew shape.
- Ordinary jeu de taquin, written from scratch: every legal order of inner
  corners for every card, full rectification, outlines and labelled results,
  independence of the order, preimage counts (Problem 6), the B "all distinct"
  claim, the guide's tables for Problems 1-2, 3, 5, 6, 7 and 8.
- Worked examples on student pages 1, 3 and 7 are replayed step by step from
  the drawn states.
- Problem 4 target outlines are read from the drawing and compared with the
  set of outlines B can reach.
- Reversal: every single slide of every card, and of every standard skew
  tableau in a 4x4 box with at most 7 cells, is undone by the larger
  up/left rule, both with the printed "stop at S" rule and with the natural
  stop (no numbered up/left neighbour) - to test whether S is needed.
- Regression of my implementation: the first fundamental theorem
  (order-independence) on every standard skew tableau in a 4x4 box with at
  most 7 cells.
- Larger-neighbour variant on all A cards (Problem 8).
- The guide's counting arguments (5, 6, 16) by direct enumeration of the
  sub-cases they name.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent


def find_repo(here):
    # Committed copy lives at plans/review/checks/week-90/: repo is parents[3].
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in [here, *here.parents]:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-90'
OUT = []
FAIL = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    if cond:
        say('  ok   ', msg)
    else:
        say('  FAIL ', msg)
        FAIL.append(msg)


# ---------------------------------------------------------------- parsing
NUM = r'(-?[\d.]+)'
RE_FILL = re.compile(r'\\fill\[(white|black!12|black!70)\] \(' + NUM + ',' + NUM + r'\) rectangle \+\+\(' + NUM + ',' + NUM + r'\)')
RE_DRAWCELL = re.compile(r'\\draw\[line width=\.45pt\] \(' + NUM + ',' + NUM + r'\) rectangle \+\+\(' + NUM + ',' + NUM + r'\)')
RE_LABEL = re.compile(r'\\node\[font=\\fontsize\{13\.16\}\{14\}\\selectfont\] at \(' + NUM + ',' + NUM + r'\) \{(\d)\}')
RE_RING = re.compile(r'\\draw\[line width=1\.5pt\] \(' + NUM + ',' + NUM + r'\) circle')
RE_SE = re.compile(r'\\node\[fill=white,inner sep=\.4pt,font=\\fontsize\{6\}\{6\}\\selectfont,anchor=north west\] at \(' + NUM + ',' + NUM + r'\) \{([SE])\}')
RE_TEXT = re.compile(r'\\node\[anchor=north west[^\]]*\] at \(' + NUM + ',' + NUM + r'\) \{([^{}]*)\}')


def pages(tex):
    body = tex.split('\\begin{document}', 1)[1]
    return [p for p in body.split('\\newpage') if 'tikzpicture' in p]


def grids_on_page(page):
    """Return list of grids: dict(name, x0, y0, s, cells{(r,c): kind/label}, marks)."""
    cells = {}
    for kind, x, y, w, h in RE_FILL.findall(page):
        x, y, w, h = map(float, (x, y, w, h))
        if abs(w - h) > 1e-6:
            continue
        key = (round(x, 2), round(y, 2), round(w, 2))
        k = {'white': 'W', 'black!12': 'G', 'black!70': 'D'}[kind]
        # a later gray/dark fill overrides a white fill at the same place
        if key not in cells or k != 'W':
            cells[key] = k
    for x, y, w, h in RE_DRAWCELL.findall(page):
        x, y, w, h = map(float, (x, y, w, h))
        key = (round(x, 2), round(y, 2), round(w, 2))
        if abs(w - h) < 1e-6 and key not in cells:
            cells[key] = 'W'   # outline-only cell (blank target/recording grid)
    labels = [(float(x), float(y), int(v)) for x, y, v in RE_LABEL.findall(page)]
    rings = [(float(x), float(y)) for x, y in RE_RING.findall(page)]
    marks = [(float(x), float(y), m) for x, y, m in RE_SE.findall(page)]
    texts = [(float(x), float(y), t.strip()) for x, y, t in RE_TEXT.findall(page)]
    # cluster cells by edge adjacency
    keys = list(cells)
    parent = {k: k for k in keys}

    def f(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for a in keys:
        for b in keys:
            if a < b and a[2] == b[2]:
                s = a[2]
                dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
                if (abs(dx - s) < .01 and dy < .01) or (abs(dy - s) < .01 and dx < .01):
                    parent[f(a)] = f(b)
    groups = defaultdict(list)
    for k in keys:
        groups[f(k)].append(k)
    out = []
    for g in groups.values():
        s = g[0][2]
        x0 = min(k[0] for k in g)
        y0 = min(k[1] for k in g)
        grid = {}
        for (x, y, _s) in g:
            r, c = round((y - y0) / s), round((x - x0) / s)
            grid[(r, c)] = cells[(x, y, _s)]
        for (x, y, v) in labels:
            r, c = (y - y0) / s - .5, (x - x0) / s - .5
            if abs(r - round(r)) < .01 and abs(c - round(c)) < .01 and (round(r), round(c)) in grid:
                assert grid[(round(r), round(c))] == 'W', 'label on non-white cell'
                grid[(round(r), round(c))] = v
        for (x, y) in rings:
            r, c = (y - y0) / s - .5, (x - x0) / s - .5
            if abs(r - round(r)) < .01 and abs(c - round(c)) < .01 and (round(r), round(c)) in grid:
                grid[(round(r), round(c))] = 'O'
        mk = {}
        for (x, y, m) in marks:
            r, c = int((y - y0) // s), int((x - x0) // s)
            if (r, c) in grid and 0 <= x - x0 - c * s < s and 0 <= y - y0 - r * s < s:
                mk[m] = (r, c)
        # name: a short title text just above the grid, near its left edge
        name = None
        best = None
        for (x, y, t) in texts:
            if re.fullmatch(r'[ABD]\d*', t) and y < y0 and y0 - y < 22 and abs(x - x0) < 22:
                d = (y0 - y) + abs(x - x0)
                if best is None or d < best:
                    best, name = d, t
        out.append(dict(name=name, x0=x0, y0=y0, s=s, cells=grid, marks=mk))
    out.sort(key=lambda g: (round(g['y0']), g['x0']))
    return out


def show(grid):
    R = max(r for r, c in grid) + 1
    C = max(c for r, c in grid) + 1
    rows = []
    for r in range(R):
        row = ''
        for c in range(C):
            v = grid.get((r, c), ' ')
            row += {'W': '.', 'G': 'g', 'D': '#', 'O': 'o'}.get(v, str(v))
        rows.append(row)
    return '/'.join(rows)


# ------------------------------------------------------- jeu de taquin
def corners(inner):
    return sorted((r, c) for r, c in inner if (r + 1, c) not in inner and (r, c + 1) not in inner)


def is_partition_set(cells):
    return all((r - 1, c) in cells or r == 0 for r, c in cells) and all((r, c - 1) in cells or c == 0 for r, c in cells)


def increasing(t):
    for (r, c), v in t.items():
        if (r, c + 1) in t and not v < t[(r, c + 1)]:
            return False
        if (r + 1, c) in t and not v < t[(r + 1, c)]:
            return False
    return True


def slide(t, inner, start, larger=False):
    """One whole slide. t: dict cell->label (numbered cells only). inner: set of
    gray cells. Returns (t', inner', exit, moved labels, path)."""
    assert start in corners(inner)
    t = dict(t)
    inner = set(inner) - {start}
    hole = start
    moved, path = [], [hole]
    while True:
        r, c = hole
        cand = [p for p in ((r, c + 1), (r + 1, c)) if p in t]
        assert all(p not in inner for p in ((r, c + 1), (r + 1, c))), 'gray next to the hole'
        if not cand:
            break
        p = (max if larger else min)(cand, key=t.get)
        moved.append(t[p])
        t[hole] = t.pop(p)
        hole = p
        path.append(hole)
    return t, inner, hole, moved, path


def reverse(t, inner, exit_, stop=None):
    """Undo a slide: hole at exit_, move the larger up/left numbered neighbour in.
    stop=None: stop naturally when no numbered up/left neighbour exists."""
    t = dict(t)
    hole = exit_
    moved = []
    while True:
        if stop is not None and hole == stop:
            break
        r, c = hole
        cand = [p for p in ((r - 1, c), (r, c - 1)) if p in t]
        if not cand:
            break
        p = max(cand, key=t.get)
        moved.append(t[p])
        t[hole] = t.pop(p)
        hole = p
    return t, set(inner) | {hole}, hole, moved


def all_rectifications(t, inner, orders=None, prefix=()):
    """Yield (order of corners, final tableau) over every legal order."""
    if not inner:
        yield prefix, t
        return
    for s in corners(inner):
        t2, in2, e, mv, path = slide(t, inner, s)
        assert increasing(t2), 'slide broke increasing order'
        assert sorted(t2.values()) == sorted(t.values())
        yield from all_rectifications(t2, in2, prefix=prefix + (s,))


def shape(t):
    rows = Counter(r for r, c in t)
    return tuple(rows[r] for r in range(len(rows)))


def rows_str(t):
    R = max(r for r, c in t) + 1
    return '/'.join(''.join(str(t[(r, c)]) for c in sorted(cc for rr, cc in t if rr == r)) for r in range(R))


def straight(t):
    cells = set(t)
    return is_partition_set(cells)


def fillings(cells):
    cells = sorted(cells)
    for p in permutations(range(1, len(cells) + 1)):
        t = dict(zip(cells, p))
        if increasing(t):
            yield t


def card_state(grid):
    """grid cells -> (t, inner, outer)"""
    t = {k: v for k, v in grid.items() if isinstance(v, int)}
    inner = {k for k, v in grid.items() if v in ('G', 'O')}
    outer = {k for k, v in grid.items() if v != 'D'}
    return t, inner, outer


# ------------------------------------------------------------- main
def main():
    stex = (SRC / 'student' / 'students.tex').read_text()
    mtex = (SRC / 'student' / 'materials.tex').read_text()
    gtex = (SRC / 'guide' / 'facilitator.tex').read_text()
    spages = [grids_on_page(p) for p in pages(stex)]
    mpages = [grids_on_page(p) for p in pages(mtex)]
    say('Coordinates in this output are 0-based (row, column) from the top left; the report and guide use 1-based.')
    say('Grid key: digit = label, . = blank white, g = gray (missing), # = dark (outside), o = ring; rows separated by /.')
    say('Student pages parsed:', len(spages), ' materials pages parsed:', len(mpages))
    for i, gs in enumerate(spages, 1):
        say(f' student p{i}:', '  '.join(f"{g['name'] or '-'}[{g['s']:g}mm]={show(g['cells'])}" + (f" marks={g['marks']}" if g['marks'] else '') for g in gs))
    for i, gs in enumerate(mpages, 1):
        say(f' materials p{i}:', '  '.join(f"{g['name'] or '-'}[{g['s']:g}mm]={show(g['cells'])}" for g in gs))

    # ---- cards from the materials pages
    cards = {}
    for gs in mpages[5:10]:
        for g in gs:
            if g['name']:
                cards[g['name']] = g['cells']
    say('\n== Card catalog (materials pp6-10)')
    say(' cards found:', ' '.join(sorted(cards, key=lambda n: (n[0], int(n[1:])))))
    fam = {'A': [f'A{i}' for i in range(1, 6)], 'D': [f'D{i}' for i in range(1, 7)], 'B': [f'B{i}' for i in range(1, 17)]}
    for F, names in fam.items():
        check(all(n in cards for n in names), f'{F}: all {len(names)} cards present')
        shapes = {(frozenset(card_state(cards[n])[1]), frozenset(card_state(cards[n])[2])) for n in names}
        check(len(shapes) == 1, f'{F}: all cards share one gray/outer shape')
        inner, outer = next(iter(shapes))
        check(is_partition_set(set(inner)) and is_partition_set(set(outer)), f'{F}: gray cells and non-dark cells are Young diagrams (inner {sorted(inner)}, outer rows {shape(dict.fromkeys(outer, 0))})')
        ts = [card_state(cards[n])[0] for n in names]
        check(all(increasing(t) for t in ts), f'{F}: every card increases right and down')
        check(all(sorted(t.values()) == list(range(1, len(t) + 1)) for t in ts), f'{F}: every card uses 1..n once')
        allf = list(fillings(set(outer) - set(inner)))
        check(len(allf) == len(names) and {tuple(sorted(t.items())) for t in ts} == {tuple(sorted(t.items())) for t in allf},
              f'{F}: cards are exactly all {len(allf)} increasing fillings')

    # board inserts (materials pp1-4) vs card outer shapes
    say('\n== Board inserts (materials pp1-4)')
    ins = {}
    for i, key in zip(range(4), 'ABDX'):
        g = [g for g in mpages[i] if g['s'] == 30][0]
        ins[key] = {k for k, v in g['cells'].items() if v != 'D'}
        check(g['s'] == 30, f'insert {key}: cells are 30 mm')
    for F in 'ABD':
        outer = card_state(cards[fam[F][0]])[2]
        check(ins[F] == outer, f'insert {F}: white cells = card outer shape {shape(dict.fromkeys(outer, 0))}')
    check(ins['X'] == {(0, 0), (0, 1), (1, 0), (1, 1)}, 'insert 4 (worked examples): 2x2 square')

    # every copy of a card on the student pages agrees with the materials card
    say('\n== Card copies on student pages')
    for i, gs in enumerate(spages, 1):
        for g in gs:
            n = g['name']
            if n and n in cards and any(isinstance(v, int) for v in g['cells'].values()):
                check(g['cells'] == cards[n], f'student p{i}: {n} matches materials card ({show(g["cells"])})')

    # ---- rectification catalog
    say('\n== Full rectification of every card over every legal corner order')
    result = {}
    for F, names in fam.items():
        for n in names:
            t, inner, outer = card_state(cards[n])
            runs = list(all_rectifications(t, inner))
            finals = {tuple(sorted(f.items())) for o, f in runs}
            f0 = runs[0][1]
            check(len(finals) == 1 and straight(f0) and increasing(f0),
                  f'{n}: {len(runs)} legal order(s), one final result {rows_str(f0)} shape {shape(f0)}')
            result[n] = f0
            if F in 'DB':
                orders = sorted(o for o, f in runs)
                say('       orders:', orders)
    # Problem 1
    say('\n== Problem 1/2 (A)')
    check(shape(result['A1']) == (2, 2) and shape(result['A3']) == shape(result['A5']) == (3, 1),
          'Problem 1: A1 -> (2,2); A3 and A5 -> (3,1): A3 and A5 share an outline')
    check(rows_str(result['A3']) != rows_str(result['A5']), 'A3 and A5 labelled results differ')
    # guide tables
    gtabA = {k: v for k, v in re.findall(r'(A\d)&\$([\d/]+)\$&\$\(', gtex)}
    check(len(gtabA) == 5 and all(rows_str(result[k]) == v for k, v in gtabA.items()), f'guide A table matches ({gtabA})')
    gAsh = {m[0]: tuple(map(int, m[2].split(','))) for m in re.findall(r'(A\d)&\$([\d/]+)\$&\$\(([\d,]+)\)\$', gtex)}
    check(all(shape(result[k]) == v for k, v in gAsh.items()), 'guide A outlines match')

    say('\n== Problem 3/6 (D)')
    gD = re.findall(r'(D\d)&(\d{3})&\$([\d/]+)\$', gtex)
    check(len(gD) == 6, 'guide D table has 6 rows')
    for n, diag, fin in gD:
        t = card_state(cards[n])[0]
        anti = ''.join(str(t[c]) for c in [(0, 2), (1, 1), (2, 0)])
        check(anti == diag, f'guide D {n}: "diagonal labels" {diag} = card read top-right to bottom-left ({anti})')
        check(rows_str(result[n]) == fin, f'guide D {n}: finished rows {fin} (mine {rows_str(result[n])})')
    pre = defaultdict(list)
    for n in fam['D']:
        pre[rows_str(result[n])].append(n)
    say('  D preimages:', dict(pre))
    check(sorted(len(v) for v in pre.values()) == [1, 1, 2, 2], 'D: four results, multiplicities 1,1,2,2')
    check(pre.get('13/2') == ['D2', 'D5'] and pre.get('12/3') == ['D3', 'D4'] and pre.get('1/2/3') == ['D1'] and pre.get('123') == ['D6'],
          'guide Problem 6: 13/2<-D2,D5; 12/3<-D3,D4; 1/2/3<-D1; 123<-D6')
    # targets drawn on student page 6
    tg = [g for g in spages[5] if any(isinstance(v, int) for v in g['cells'].values())]
    tgs = sorted(rows_str({k: v for k, v in g['cells'].items() if isinstance(v, int)}) for g in tg)
    check(tgs == sorted(pre), f'student p6 targets {tgs} are exactly the four D results')

    say('\n== Problems 4/5 (B)')
    gB = re.findall(r'(B\d+)&\$([\d/]+)\$&\$\(([\d,]+)\)\$', gtex)
    check(len(gB) == 16, 'guide B table has 16 rows')
    for n, fin, sh in gB:
        check(rows_str(result[n]) == fin and shape(result[n]) == tuple(map(int, sh.split(','))),
              f'guide B {n}: {fin} {sh} (mine {rows_str(result[n])} {shape(result[n])})')
    bres = [rows_str(result[n]) for n in fam['B']]
    check(len(set(bres)) == 16, 'B: all 16 labelled results distinct (answer to page-6 last question is "no")')
    byshape = defaultdict(list)
    for n in fam['B']:
        byshape[shape(result[n])].append(n)
    say('  B by outline:', dict(byshape))
    check(byshape[(2, 2, 1)] == ['B1', 'B2', 'B6', 'B7', 'B11'] and byshape[(3, 1, 1)] == ['B3', 'B4', 'B5', 'B9', 'B10', 'B13']
          and byshape[(3, 2)] == ['B8', 'B12', 'B14', 'B15', 'B16'], 'guide B grouping by outline')
    # every standard tableau of each reachable shape appears exactly once
    for sh in byshape:
        cells = {(r, c) for r, L in enumerate(sh) for c in range(L)}
        syt = {rows_str(t) for t in fillings(cells)}
        got = {rows_str(result[n]) for n in byshape[sh]}
        check(got == syt, f'B: results of outline {sh} are exactly all {len(syt)} standard tableaux of that shape')
    # Problem 4 targets drawn on student page 4 (grids with no gray/dark/numbers)
    p4 = [g for g in spages[3] if g['name'] is None and all(v == 'W' for v in g['cells'].values())]
    say('  student p4 grids:', [show(g['cells']) for g in spages[3]])
    p4shapes = sorted(shape(dict.fromkeys(g['cells'], 0)) for g in p4)
    say('  Problem 4 drawn outlines:', p4shapes)
    check(sorted(byshape) == p4shapes, 'Problem 4: drawn outlines are exactly the outlines B can reach')
    # guide witnesses
    for n, fin in [('B8', '125/34'), ('B3', '145/2/3'), ('B1', '13/25/4')]:
        check(rows_str(result[n]) == fin, f'guide Problem 4 witness {n} -> {fin}')
    # guide witness diagrams (tikz 8 mm units) match cards
    for block in re.findall(r'(B\d+) / target (.*?)\\end\{tikzpicture\}', gtex, re.S):
        n, body = block
        cells = {}
        for fill, x, y in re.findall(r'\\filldraw\[fill=([^,]+),draw=black\] \((\d),(\d)\)', body):
            cells[(int(y), int(x))] = 'G' if fill == 'black!25' else 'W'
        for x, y, v in re.findall(r'\\node at \(([\d.]+),([\d.]+)\) \{(\d)\}', body):
            cells[(int(float(y)), int(float(x)))] = int(v)
        cg = {k: v for k, v in cards[n].items() if v != 'D'}
        check(cells == cg, f'guide witness diagram {n} matches its card')

    # ---- counting arguments in the guide
    say('\n== Counting arguments')
    Acells = sorted(set(card_state(cards['A1'])[2]) - set(card_state(cards['A1'])[1]))
    a, b, c, d = (0, 1), (0, 2), (1, 0), (1, 1)
    FA = list(fillings(set(Acells)))
    check(sum(t[a] == 1 for t in FA) == 3 and sum(t[c] == 1 for t in FA) == 2 and all(t[a] == 2 for t in FA if t[c] == 1),
          'A: a=1 gives 3, c=1 forces a=2 and gives 2')
    Bcells = set(card_state(cards['B1'])[2]) - set(card_state(cards['B1'])[1])
    FB = list(fillings(Bcells))
    A_, B_, C_, D_, E_ = (0, 2), (1, 1), (1, 2), (2, 0), (2, 1)
    cnt = Counter(next(k for k in 'abd' if t[{'a': A_, 'b': B_, 'd': D_}[k]] == 1) for t in FB)
    check(cnt == Counter({'a': 5, 'b': 6, 'd': 5}), f'B: 1 at a,b,d gives 5,6,5 ({dict(cnt)})')
    a1 = [t for t in FB if t[A_] == 1]
    check(sum(t[B_] == 2 for t in a1) == 3 and sum(t[D_] == 2 for t in a1) == 2, 'B, a=1: b next 3, d next 2')
    cmp = set()
    for (r, c_) in Bcells:
        if (r, c_ + 1) in Bcells:
            cmp.add(((r, c_), (r, c_ + 1)))
        if (r + 1, c_) in Bcells:
            cmp.add(((r, c_), (r + 1, c_)))
    check(cmp == {(A_, C_), (B_, C_), (B_, E_), (D_, E_)}, 'B comparisons are exactly a<c, b<c, b<e, d<e')

    # ---- worked examples on student pages
    say('\n== Worked examples')
    # page 1: three 2x2 states
    p1 = [g for g in spages[0] if g['s'] == 14 and g['name'] is None and len(g['cells']) == 4]
    p1 = sorted(p1, key=lambda g: g['x0'])[:3]
    say('  p1 states:', [show(g['cells']) for g in p1])
    g0 = p1[0]['cells']
    t = {k: v for k, v in g0.items() if isinstance(v, int)}
    hole = [k for k, v in g0.items() if v == 'O'][0]
    check(increasing(t), 'p1 example start is increasing')
    t1, in1, e, mv, path = slide(t, {hole}, hole)
    check(mv == [1, 3] and e == (1, 1) and rows_str(t1) == '12/3', f'p1 example: moves {mv}, exit {e}, result {rows_str(t1)}')
    mid = {k: v for k, v in p1[1]['cells'].items() if isinstance(v, int)}
    check(mid == {(0, 0): 1, (0, 1): 2, (1, 1): 3} and p1[1]['cells'][(1, 0)] == 'O', 'p1 middle state = after 1 slides up')
    check(p1[2]['cells'][(1, 1)] == 'D' and {k: v for k, v in p1[2]['cells'].items() if isinstance(v, int)} == t1, 'p1 last state = result with exit dark')
    # page 3: four multi-hole states
    p3 = sorted([g for g in spages[2] if g['name'] is None and len(g['cells']) == 6], key=lambda g: g['x0'])
    say('  p3 states:', [show(g['cells']) for g in p3])
    s0 = p3[0]['cells']
    t = {k: v for k, v in s0.items() if isinstance(v, int)}
    inner = {k for k, v in s0.items() if v in ('G', 'O')}
    outer = {k for k, v in s0.items() if v != 'D'}
    check(shape(dict.fromkeys(outer, 0)) == (3, 2) and shape(dict.fromkeys(inner, 0)) == (2, 1) and increasing(t), 'p3 example: outer (3,2), missing (2,1), increasing')
    ring = [k for k, v in s0.items() if v == 'O'][0]
    check(ring in corners(inner), 'p3 example: ring placed on a legal corner')
    t1, in1, e, mv, path = slide(t, inner, ring)
    s1 = p3[1]['cells']
    check(mv[:1] == [2] and {k: v for k, v in s1.items() if isinstance(v, int)} == {(0, 2): 1, (1, 0): 2} and s1[(1, 1)] == 'O', 'p3 "2 slides left" state correct')
    check(e == (1, 1) and p3[2]['cells'][(1, 1)] == 'D' and {k: v for k, v in p3[2]['cells'].items() if isinstance(v, int)} == t1, 'p3 "cover the exit" state correct')
    s3 = p3[3]['cells']
    r3 = [k for k, v in s3.items() if v == 'O'][0]
    check(corners(in1) == [r3], f'p3 "open next corner": ring at {r3}, the only legal corner {corners(in1)}')
    check({k for k, v in s3.items() if v == 'G'} == in1 - {r3}, 'p3 unchosen gray cell kept')
    # page 7: reverse demonstration
    p7 = sorted([g for g in spages[6] if g['name'] is None and len(g['cells']) == 4], key=lambda g: g['x0'])
    say('  p7 states:', [show(g['cells']) + f" {g['marks']}" for g in p7])
    f0 = p7[0]['cells']
    tf = {k: v for k, v in f0.items() if isinstance(v, int)}
    S, E = p7[0]['marks']['S'], p7[0]['marks']['E']
    check(f0[E] == 'D' and rows_str(tf) == '12/3', f'p7 finished slide 12/3 with E={E} dark, S={S}')
    tr, inr, h, mv = reverse(tf, set(), E, stop=S)
    check(mv == [3, 1] and h == S, f'p7 reverse moves {mv}, ends at S')
    fin = p7[3]['cells']
    check(fin[S] == 'G' and {k: v for k, v in fin.items() if isinstance(v, int)} == tr, 'p7 final state = restored start with gray at S')
    # compare with p1 start
    check(tr == {k: v for k, v in g0.items() if isinstance(v, int)}, 'p7 reverse returns exactly the p1 start')
    m2 = {k: v for k, v in p7[2]['cells'].items() if isinstance(v, int)}
    check(m2 == {(0, 0): 1, (0, 1): 2, (1, 1): 3} and p7[2]['cells'][(1, 0)] == 'O', 'p7 "3 slides right" state correct')

    # ---- Problem 7: single slides and reversal
    say('\n== Problem 7 (one slide and its reversal)')
    gtab7 = re.findall(r'(A2|A4|B4 upper|B4 lower)&\$\((\d),(\d)\)\$&\$\((\d),(\d)\)\$&([\d,]+) / ([\d,]+)', gtex)
    check(len(gtab7) == 4, 'guide Problem 7 table has 4 rows')
    for row in gtab7:
        nm, sr, sc, er, ec, fw, bw = row
        n = nm.split()[0]
        t, inner, outer = card_state(cards[n])
        cs = corners(inner)
        if nm.endswith('upper'):
            s = min(cs)
        elif nm.endswith('lower'):
            s = max(cs)
        else:
            s = cs[0]
        t1, in1, e, mv, path = slide(t, inner, s)
        ok = (s == (int(sr) - 1, int(sc) - 1) and e == (int(er) - 1, int(ec) - 1)
              and mv == list(map(int, fw.split(','))))
        tr, inr, h, mvr = reverse(t1, in1, e, stop=s)
        tn, inn, hn, mvn = reverse(t1, in1, e, stop=None)
        check(ok and mvr == list(map(int, bw.split(','))) and tr == t and inr == inner,
              f'guide P7 {nm}: S={s} E={e} forward {mv} reverse {mvr}; start recovered')
        check(tn == t and hn == s, f'   {nm}: natural stop (no S) also returns to S')

    # E is genuinely needed: undoing A2's finished slide from the other addable
    # square of its outline gives a different increasing start.
    t, inner, outer = card_state(cards['A2'])
    t1, in1, e, mv, path = slide(t, inner, corners(inner)[0])
    alt = (2, 0)
    ta, ina, ha, mva = reverse(t1, in1, alt, stop=None)
    cells_a = set(ta) | ina
    check(ta != t and increasing(ta) and is_partition_set(ina) and is_partition_set(cells_a),
          f'A2 result {rows_str(t1)} undone from (3,1) instead of E=(1,3): gray {sorted(ina)}, labels {sorted(ta.items())} - a different legal start, so E is essential')

    # ---- Problem 8: larger-neighbour rule
    say('\n== Problem 8 (larger-neighbour rule on A)')
    g8 = dict(re.findall(r'(A\d)&\$([\d/]+)\$&(?:top row|first column)', gtex))
    for n in fam['A']:
        t, inner, outer = card_state(cards[n])
        t1, in1, e, mv, path = slide(t, inner, corners(inner)[0], larger=True)
        check(not increasing(t1), f'{n}: larger rule gives {rows_str(t1)} (not increasing)')
        check(g8.get(n) == rows_str(t1), f'   guide table {n}: {g8.get(n)}')

    # ---- Regression on a broad family (implementation sanity + reversal claim)
    say('\n== Regression: all standard skew tableaux in a 4x4 box, at most 7 cells')
    parts = []

    def gen(maxlen, rows, acc):
        if rows == 0:
            parts.append(tuple(x for x in acc if x))
            return
        for L in range(0, maxlen + 1):
            gen(L, rows - 1, acc + [L])
    gen(4, 4, [])
    parts = sorted(set(parts))
    n_tab = n_slides = 0
    bad_conf = bad_rev = bad_nat = s_nbr = 0
    for lam in parts:
        for mu in parts:
            if len(mu) > len(lam) or any(m > l for m, l in zip(mu, lam)):
                continue
            outer = {(r, c) for r, L in enumerate(lam) for c in range(L)}
            inner = {(r, c) for r, L in enumerate(mu) for c in range(L)}
            if not (0 < len(outer) - len(inner) <= 7) or not inner:
                continue
            for t in fillings(outer - inner):
                n_tab += 1
                finals = {tuple(sorted(f.items())) for o, f in all_rectifications(t, inner)}
                if len(finals) != 1:
                    bad_conf += 1
                for s in corners(inner):
                    n_slides += 1
                    t1, in1, e, mv, path = slide(t, inner, s)
                    tr, inr, h, _ = reverse(t1, in1, e, stop=s)
                    if tr != t or inr != inner:
                        bad_rev += 1
                    tn, inn, hn, _ = reverse(t1, in1, e, stop=None)
                    if tn != t or hn != s:
                        bad_nat += 1
                    # when the ring is back at S, is any label above or left of S?
                    if any(q in tr for q in ((s[0] - 1, s[1]), (s[0], s[1] - 1))):
                        s_nbr += 1
    check(bad_conf == 0, f'order-independence holds on all {n_tab} tableaux')
    check(bad_rev == 0, f'reverse with stop-at-S recovers all {n_slides} single slides')
    check(s_nbr == 0, f'guide hint "stop at S even if another neighboring label exists": cases with a label above/left of S = {s_nbr} of {n_slides} (situation never occurs)')
    check(bad_nat == 0, f'reverse with natural stop (S not used) recovers all {n_slides} single slides and ends at S')

    say('\nFAILURES:', len(FAIL))
    for f in FAIL:
        say('  ', f)


if __name__ == '__main__':
    main()
    text = '\n'.join(OUT) + '\n'
    (HERE / 'check_math.py.out').write_text(text)
    print(text)
    sys.exit(1 if FAIL else 0)
