#!/usr/bin/env python3
"""Diagram check of the delivered Week 42 student PDFs (base and bonus).

Reads the vector drawings and word positions of each page with PyMuPDF and
rebuilds every counter diagram: which coloured counters sit in which box, in
what order, with what label, and whether each label matches its fill colour.
It then compares them with what the printed text says, and checks that
squares and circles are drawn with equal width and height.

Requires PyMuPDF (python3 -m pip install pymupdf).
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
The repository is found by walking up from this file; from the committed copy
in plans/review/checks/week-42/ that is four folders up.
"""
import itertools
import math
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo():
    for d in [HERE] + list(HERE.parents):
        if (d / 'lowell-math-circle-year-2').is_dir() and (d / 'AGENTS.md').is_file():
            return d
    sys.exit('repository not found above ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-42'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def colour_of(fill):
    if fill is None:
        return None
    r, g, b = fill[:3]
    if abs(r - b) < 0.05:
        return None
    return 'R' if r > b else 'B'


def analyse(page):
    words = page.get_text('words')
    tokens, boxes, squares, circles, tris = [], [], [], [], []
    for d in page.get_drawings():
        r = d['rect']
        kinds = [i[0] for i in d['items']]
        col = colour_of(d.get('fill'))
        if col and kinds and all(k == 'c' for k in kinds):
            cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            lab = [w[4] for w in words if r.x0 < (w[0] + w[2]) / 2 < r.x1 and r.y0 < (w[1] + w[3]) / 2 < r.y1]
            tokens.append(dict(x=cx, y=cy, w=r.width, h=r.height, col=col, label=' '.join(lab)))
            continue
        if d.get('fill') is None and kinds and all(k == 'c' for k in kinds):
            circles.append(r)       # outline circle (shape symbol)
            continue
        if d.get('fill') is None and r.width > 15 and r.height > 15 and ('c' in kinds or 're' in kinds):
            boxes.append(r)
        if (kinds == ['re'] or kinds == ['l'] * 4) and d.get('fill') is None and 10 < r.width < 30 and 10 < r.height < 30:
            squares.append(r)   # shape symbol; equal sides checked below
        if kinds.count('l') == 3 and len(kinds) == 3 and r.width < 30:
            pts = [d['items'][0][1]] + [it[2] for it in d['items']]
            tris.append(pts)
    return words, tokens, boxes, squares, circles, tris


def container(tok, boxes):
    inside = [b for b in boxes if b.x0 < tok['x'] < b.x1 and b.y0 < tok['y'] < b.y1]
    return min(inside, key=lambda b: b.width * b.height) if inside else None


def groups(tokens, boxes):
    g = {}
    for t in tokens:
        c = container(t, boxes)
        key = (round(c.y0, 1), round(c.x0, 1), round(c.x1, 1), round(c.y1, 1)) if c else ('free', round(t.get('y'), 0))
        g.setdefault(key, []).append(t)
    out = []
    for key, ts in sorted(g.items(), key=lambda kv: (kv[0][0] if kv[0][0] != 'free' else kv[0][1], kv[0][1] if kv[0][0] != 'free' else 0)):
        ts = sorted(ts, key=lambda t: (round(t['y'] / 5), t['x']))
        out.append((key, ''.join(t['col'] for t in ts), [t['label'] for t in ts]))
    return out


def label_colour_ok(tokens):
    return all(t['label'] and t['label'][0] == t['col'] for t in tokens)


def caption_near(words, box_key, below=40):
    """Words just below a box (bag captions such as 'five red, two blue')."""
    y1, x0, x1 = box_key[3], box_key[1], box_key[2]
    ws = [w for w in words if y1 < w[1] < y1 + below and x0 - 5 < w[0] < x1 + 60]
    ws.sort(key=lambda w: (round(w[1]), w[0]))
    return ' '.join(w[4] for w in ws)


def doc_pages(name):
    return pymupdf.open(str(WEEK / name))


report = {}


def page_summary(name, i):
    page = doc_pages(name)[i]
    words, tokens, boxes, squares, circles, tris = analyse(page)
    gs = groups(tokens, boxes)
    say(f'\n### {name} p.{i + 1}')
    for key, cols, labs in gs:
        cap = caption_near(words, key) if key[0] != 'free' else ''
        say(f'   box {key}: {cols} {labs}' + (f'  caption: "{cap}"' if cap else ''))
    for s in squares:
        say(f'   square symbol {s.width:.2f} x {s.height:.2f}')
    for c in circles:
        say(f'   circle symbol {c.width:.2f} x {c.height:.2f}')
    for t in tris:
        a, b, c = t[0], t[1], t[2]
        sides = [math.dist(a, b), math.dist(b, c), math.dist(c, a)]
        say('   triangle symbol sides ' + ', '.join(f'{x:.2f}' for x in sides))
    tok_round = all(abs(t['w'] - t['h']) < 0.05 for t in tokens)
    check(tok_round, f'{name} p.{i + 1}: all {len(tokens)} counters are round (equal width/height)')
    check(label_colour_ok(tokens), f'{name} p.{i + 1}: every counter label matches its fill colour')
    check(all(abs(s.width - s.height) < 0.05 for s in squares), f'{name} p.{i + 1}: square symbols have equal sides')
    check(all(abs(c.width - c.height) < 0.05 for c in circles), f'{name} p.{i + 1}: circle symbols are round')
    return words, tokens, boxes, gs, squares, circles, tris


def seqs(gs):
    return [cols for _, cols, _ in gs]


def labels(gs):
    return [labs for _, _, labs in gs]


# ------------------------------------------------------------ K-1
K = 'week-42-k-1.pdf'
w, t, b, gs, sq, ci, tr = page_summary(K, 0)
check(seqs(gs)[:2] == ['RRRB', 'RB'], 'K-1 p1: launch bag RRRB -> pair R then B ("Red, then blue")')
check(seqs(gs)[2:] == ['RRR', 'RRRB'], 'K-1 p1 P1: comparison bags RRR (blue removed) and RRRB')
two_cell = [x for x in b if 200 < x.width < 215 and 95 < x.height < 102]
check(len(two_cell) == 4, f'K-1 p1 P1: four two-position record boxes for four colour pairs (found {len(two_cell)})')

w, t, b, gs, sq, ci, tr = page_summary(K, 1)
check(seqs(gs)[0] == 'BR' and len(sq) >= 1, 'K-1 p2: sample BR -> square')
board = seqs(gs)[1:]
check(sorted(board) == sorted(['RR', 'RB', 'BR', 'BB']), 'K-1 p2 P2: rule board lists RR, RB, BR, BB once each')

w, t, b, gs, sq, ci, tr = page_summary(K, 2)
labs = [tuple(l) for l in labels(gs)]
expected = [(a, c) for a in ['R1', 'R2', 'R3', 'B'] for c in ['R1', 'R2', 'R3', 'B']]
check(labs == expected, 'K-1 p3 P3: the 16 pictures are exactly the 16 ordered labelled pairs, row-major')

w, t, b, gs, sq, ci, tr = page_summary(K, 3)
check(seqs(gs) == ['RBBB', 'RRBB', 'RRRR', 'BBBB'], 'K-1 p4 P4: bags RBBB, RRBB, RRRR, BBBB')

page = doc_pages(K)[4]
dr = page.get_drawings()
slots = [d['rect'] for d in dr if d.get('fill') is None and 100 < d['rect'].width < 103 and 45 < d['rect'].height < 48]
outs = [d['rect'] for d in dr if d.get('fill') is None and 28 < d['rect'].width < 31 and 28 < d['rect'].height < 31]
say(f'\n### {K} p.5: {len(slots)} pair slots, {len(outs)} output boxes')
check(len(slots) == 18 and len(outs) == 18, 'K-1 p5 P6: three targets x six pair slots, each with an output box')

# ------------------------------------------------------------ Grades 2-3
G23 = 'week-42-grades-2-3.pdf'
w, t, b, gs, sq, ci, tr = page_summary(G23, 0)
check(seqs(gs)[0] == 'BR' and len(sq) >= 1, 'G2-3 p1: sample BR -> square')
check(sorted(seqs(gs)[1:]) == sorted(['RR', 'RB', 'BR', 'BB']), 'G2-3 p1 P1: rule board RR, RB, BR, BB')

page = doc_pages(G23)[1]
words, tokens, boxes, squares, circles, tris = analyse(page)
gs = groups(tokens, boxes)
say(f'\n### {G23} p.2')
for key, cols, labs in gs:
    say(f'   box {key}: {cols} {labs}')
check(label_colour_ok(tokens), 'G2-3 p2: every counter label matches its fill colour')
cells = sorted([x for x in boxes if 83 < x.width < 86 and 83 < x.height < 86], key=lambda r: (round(r.y0), r.x0))
say(f'   grid cells: {len(cells)}')
check(len(cells) == 16, 'G2-3 p2 P2: 4 x 4 grid of cells')
xs = sorted({round(c.x0, 1) for c in cells})
ys = sorted({round(c.y0, 1) for c in cells})
free = [tk for tk in tokens if container(tk, boxes) is None]
top = sorted([tk for tk in free if tk['y'] < ys[0]], key=lambda tk: tk['x'])
side = sorted([tk for tk in free if tk['x'] < xs[0]], key=lambda tk: tk['y'])
check([tk['label'] for tk in top] == ['R1', 'R2', 'R3', 'B'], 'G2-3 p2: column heads R1, R2, R3, B (second draw)')
check([tk['label'] for tk in side] == ['R1', 'R2', 'R3', 'B'], 'G2-3 p2: row heads R1, R2, R3, B (first draw)')
col_ok = all(abs(tk['x'] - (cells[0].x0 + (i + .5) * cells[0].width)) < 2 for i, tk in enumerate(top))
row_ok = all(abs(tk['y'] - (ys[i] + cells[0].height / 2)) < 2 for i, tk in enumerate(side))
check(col_ok and row_ok, 'G2-3 p2: heads centred on their columns and rows')
thick = [d['rect'] for d in page.get_drawings() if d.get('width', 0) > 1.2 and d.get('fill') is None and d['rect'].width > 60]
inner = [tk for tk in tokens if thick and thick[0].contains(pymupdf.Point(tk['x'], tk['y']))]
if thick:
    th = thick[0]
    col = xs.index(min(xs, key=lambda v: abs(v - th.x0)))
    row = ys.index(min(ys, key=lambda v: abs(v - th.y0)))
    say(f'   highlighted cell at row {row}, column {col}: {[tk["label"] for tk in sorted(inner, key=lambda tk: tk["x"])]}')
    check((row, col) == (1, 3) and [tk['label'] for tk in sorted(inner, key=lambda tk: tk['x'])] == ['R2', 'B'],
          'G2-3 p2: highlighted cell is row R2, column B and shows R2 then B, matching "row R2, column B"')
else:
    check(False, 'G2-3 p2: highlighted cell found')
example = [g for g in gs if g[0][0] != 'free' and g[2] == ['R2', 'B']]
check(len(example) >= 1, 'G2-3 p2: example pair R2 then B above the grid')

w, t, b, gs, sq, ci, tr = page_summary(G23, 2)
caps = [caption_near(w, k) for k, _, _ in gs]
check(seqs(gs) == ['RRBB', 'RBBB', 'RRRB', 'RRBB'], 'G2-3 p3: P3 bags RRBB, RBBB; P4 bags RRRB (three-red), RRBB (two-red)')
check(caps[0].startswith('two red, two blue') and caps[1].startswith('one red, three blue'), 'G2-3 p3 P3 captions match bags')

w, t, b, gs, sq, ci, tr = page_summary(G23, 3)
caps = [caption_near(w, k) for k, _, _ in gs]
check(seqs(gs) == ['RRRB', 'RBBB'] and caps[0].startswith('first draw') and caps[1].startswith('second draw'),
      'G2-3 p4 P5: first-draw bag RRRB, second-draw bag RBBB')

# ------------------------------------------------------------ Grades 4-5
G45 = 'week-42-grades-4-5.pdf'
w, t, b, gs, sq, ci, tr = page_summary(G45, 0)
s = seqs(gs)
check(s[0] == 'BR' and sorted(s[1:5]) == sorted(['RR', 'RB', 'BR', 'BB']) and labels(gs)[5] == ['R2', 'B'],
      'G4-5 p1: sample BR -> square; rule board; example R2 then B')

w, t, b, gs, sq, ci, tr = page_summary(G45, 1)
caps = [caption_near(w, k) for k, _, _ in gs]
check(sorted(seqs(gs)[0]) == sorted('RRRRRBB') and seqs(gs)[0].count('R') == 5 and caps[0].startswith('five red, two blue'),
      'G4-5 p2 P3: left bag has 5 red, 2 blue as captioned')
check(seqs(gs)[1].count('R') == 3 and seqs(gs)[1].count('B') == 4 and caps[1].startswith('three red, four blue'),
      'G4-5 p2 P3: right bag has 3 red, 4 blue as captioned')

w, t, b, gs, sq, ci, tr = page_summary(G45, 2)
comp = [(x.count('R'), x.count('B')) for x in seqs(gs)]
check(comp == [(3, 1), (1, 3), (3, 1), (6, 2), (2, 2), (1, 1)],
      'G4-5 p3 P5: cases (3R1B -> 1R3B), (3R1B -> 6R2B), (2R2B -> 1R1B)')

w, t, b, gs, sq, ci, tr = page_summary(G45, 3)
check(seqs(gs)[0] == 'RRRB' and labels(gs)[1] == ['R1', 'B'], 'G4-5 p4 P6: bag RRRB and labelled pair R1 then B')

# ------------------------------------------------------------ Bonus
BN = 'week-42-bonus.pdf'
w, t, b, gs, sq, ci, tr = page_summary(BN, 0)
words3 = [cols for _, cols, _ in gs]
check(sorted(words3) == sorted(''.join(x) for x in itertools.product('RB', repeat=3)),
      'bonus p1 P1: the eight boxes hold all eight three-draw words once each')
check(len(sq) == 1 and len(ci) == 1 and len(tr) == 1, 'bonus p1: legend square, circle, triangle')

page = doc_pages(BN)[1]
txt = page.get_text()
lines = [l.strip() for l in txt.splitlines()]
stories = [l for l in lines if len(l) == 7 and l[2:5] == ' | ']
say(f'\n### {BN} p.2 story labels: {stories}')
grid_stories = stories[1:]   # first occurrence is the BRRB -> BR | RB example above the problem
check(stories[0] == 'BR | RB' and grid_stories == [f'{a}{b} | {c}{d}' for a, b, c, d in itertools.product('RB', repeat=4)],
      'bonus p2 P2: example BR | RB, then sixteen story boxes, each four-draw word once (RR|RR ... BB|BB)')
check('BRRB' in lines and 'BR | RB' in lines, 'bonus p2: example BRRB -> BR | RB')
words, tokens, boxes, squares, circles, tris = analyse(page)
check(all(abs(s.width - s.height) < 0.05 for s in squares) and all(abs(c.width - c.height) < 0.05 for c in circles),
      'bonus p2: square and circle symbols have equal width and height')
say(f'   squares {[(round(s.width,2), round(s.height,2)) for s in squares]}, circles {[(round(c.width,2), round(c.height,2)) for c in circles]}')

page = doc_pages(BN)[2]
wl = [w[4] for w in page.get_text('words')]
words, tokens, boxes, squares, circles, tris = analyse(page)
tickets = [x for x in boxes if 240 < x.width < 250 and 85 < x.height < 90]
say(f'\n### {BN} p.3: {len(tickets)} ticket boxes {[(round(x.width), round(x.height)) for x in tickets]}')
check(len(tickets) == 8 and wl.count('left') == 9 and wl.count('right') == 9 and 'Cup' in wl,
      'bonus p3 P3: two cups of four equal-size left/right tickets (8 boxes; "left"/"right" once in text + 8 labels)')

say('\n## Summary')
n = sum(1 for l in OUT if l.startswith(('PASS', 'FAIL')))
say(f'{n} checks, {len(FAIL)} failures')
for f in FAIL:
    say('FAILED:', f)
(HERE / 'out_check_diagrams.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
