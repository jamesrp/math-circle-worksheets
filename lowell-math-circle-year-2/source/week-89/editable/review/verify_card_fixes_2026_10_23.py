#!/usr/bin/env python3
"""Check the October 23, 2026 review-card fixes to Week 89 (plans/review/week-89.md).

    python3 verify_card_fixes_2026_10_23.py [--pdfs DIR]

DIR holds week-89-students.pdf and week-89-facilitator.pdf (default: ../reference-pdfs).
Reads ../student/students.tex for the Problem 19 cube coordinates. Needs PyMuPDF.

Checks: the mathematics of the changed tasks and keys; the Problem 19 pictures
(the cubes drawn are the intended ones, and every visible point is painted by the
nearest cube); the page 1 example read from the PDF; the Problem 11 label clear of
its box and of the next line; the Problem 18 example and table; the changed wording;
and the guide's page references.
"""
import argparse
import re
import sys
from pathlib import Path

import pymupdf as fitz

HERE = Path(__file__).resolve().parent
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def run_machine(inputs, starts):
    state, hist = list(starts), []
    for x in inputs:
        for k in range(len(state)):
            state[k] += x
            x = state[k]          # the NEW total is copied on
        hist.append(tuple(state))
    return hist


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--pdfs', type=Path, default=HERE.parent / 'reference-pdfs')
args = ap.parse_args()
stu = fitz.open(args.pdfs / 'week-89-students.pdf')
fac = fitz.open(args.pdfs / 'week-89-facilitator.pdf')
tex = (HERE.parent / 'student' / 'students.tex').read_text()
flat = lambda s: ' '.join(s.split())
pages = [flat(p.get_text()) for p in stu]
guide = flat(' '.join(p.get_text() for p in fac))

print('== Mathematics of the changed tasks ==')
side, layers = 5, []
cells = {(x, y) for x in range(5) for y in range(5)}
while side:                                   # peel top row and right column, keep a bottom-left square
    keep = {(x, y) for x, y in cells if x < side - 1 and y < side - 1}
    layers.append(len(cells - keep))
    cells, side = keep, side - 1
check(layers == [9, 7, 5, 3, 1] and sum(layers) == 25, f'Problem 2: layers {layers} add to 25')
check(all(sum(range(1, 2 * n, 2)) == n * n for n in range(1, 30)), 'guide: 1 + 3 + ... + (2n - 1) = n^2')
start = run_machine([3], (0, 0, 0))[-1]
path = run_machine([1] * 6, (0, 0, 0))
steps = [start, (start[0] + 1, start[1], start[2])]
steps.append((steps[1][0], steps[1][1] + steps[1][0], steps[1][2]))
steps.append((steps[2][0], steps[2][1], steps[2][2] + steps[2][1]))
check(start == (3, 3, 3) and start not in path and (0, 0, 0) != start, 'Problem 18 example: (3,3,3) is one input-3 turn from zero and off the six-turn path')
check(steps[-1] == run_machine([1], start)[-1] == (4, 7, 10), f'Problem 18 example steps {steps}')
old = (start[0] + 1, start[1] + start[0], start[2] + start[1])
check(old == (4, 6, 6), 'copying old totals instead gives (4, 6, 6)')
check(path[-1] == (6, 21, 56), 'six turns of input 1 end at (6, 21, 56)')
check(3 + sum([0, 1, 2, 3, 4]) == 13, 'K-1 route, Problem 7: 13 counters in every order')
a, b = run_machine([2, 0, 3, 1], (1,)), run_machine([2, 0, 3, 1], (4,))
check(all(y[0] - x[0] == 3 for x, y in zip(a, b)), 'K-1 route, Problem 10: the gap stays 3')
check([(n + 1) ** 3 - n ** 3 for n in (1, 2)] == [7, 19], 'K-1 route, Problem 16: 7 and 19 new cubes')
pile = lambda n: sum(1 for i in range(n) for j in range(n) for k in range(n) if i + j + k < n)
check([pile(2), pile(3)] == [4, 10] and pile(10) == 220, 'K-1 route, Problem 19: piles of 4 and 10; step 10 is 220')

print('== Problem 19 pictures (TikZ coordinates and painting order) ==')
p19 = tex[tex.index('\\problem{19}'):tex.index('\\problem{20}')]
TOK = re.compile(r'\\begin\{scope\}\[shift=\{\(([^)]*)\)\}[^\]]*\]|\\end\{scope\}|\\filldraw\[fill=black!\d+\] ((?:\([^)]*\)--)+\([^)]*\))--cycle;')
figs, stack, cur = [], [], None
for m in TOK.finditer(p19):
    s = m.group(0)
    if s.startswith('\\begin'):
        vals = [float(v) for v in m.group(1).split(',')]
        if len(vals) == 2:
            cur = []
            figs.append(cur)
            stack.append(None)
        else:
            stack.append(vals)
    elif s.startswith('\\end'):
        stack.pop()
    else:
        off = [sum(v[k] for v in stack if v) for k in range(3)]
        cur.append([tuple(float(v) + o for v, o in zip(t.split(','), off)) for t in re.findall(r'\(([^)]*)\)', m.group(2))])
boxes = []
for faces in figs:
    bx = []
    for i in range(0, len(faces), 3):
        pts = [p for f in faces[i:i + 3] for p in f]
        bx.append(tuple((min(p[k] for p in pts), max(p[k] for p in pts)) for k in range(3)))
    boxes.append(bx)
unit = lambda i, j, k: ((i, i + 1), (j, j + 1), (k, k + 1))
check(len(boxes) == 3, f'three pictures: {[len(b) for b in boxes]} boxes')
check(boxes[0] == [unit(0, 0, 0)], 'step-1 pile: one cube at the corner')
stair = {unit(0, 1, 0), unit(1, 0, 0), unit(0, 0, 0)}
check(set(boxes[1]) == stair | {((0, 1), (0, 1), (1.8, 2.8))}, 'middle picture: the 2-row stair layer {(0,0,0), (1,0,0), (0,1,0)} and the step-1 pile above its square corner')
check(sorted(boxes[2]) == sorted([unit(0, 1, 0), unit(1, 0, 0), ((0, 1), (0, 1), (0, 2))]), 'step-2 pile: the stair layer with a column of two at the corner, {i+j+k<2}')
D = (-0.5, 1.0, -2.6 / 7)   # x -> (7,0) mm, y -> (3.5,2.6) mm, z -> (0,7) mm: this direction projects to a point


def entry(box, sx, sy):
    p0 = (sx / 7.0, 0.0, sy / 7.0)
    lo, hi = -1e9, 1e9
    for k in range(3):
        a, b = box[k]
        t1, t2 = (a - p0[k]) / D[k], (b - p0[k]) / D[k]
        lo, hi = max(lo, min(t1, t2)), min(hi, max(t1, t2))
    return lo if lo < hi - 1e-9 else None


for name, bx in zip(['step-1 pile', 'middle picture', 'step-2 pile'], boxes):
    wrong, step = 0, 0.05
    for i in range(-10, int(25 / step)):
        for j in range(-10, int(25 / step)):
            hits = [(entry(b, i * step, j * step), n) for n, b in enumerate(bx)]
            hits = [h for h in hits if h[0] is not None]
            if hits and min(hits)[1] != max(n for _, n in hits):
                wrong += 1
    check(wrong == 0, f'{name}: every visible point is painted by the nearest cube ({wrong * step * step:.1f} mm^2 wrong)')

print('== Page 1 example, read from the PDF ==')
p1 = stu[0]
sq = [(d['rect'], 'grey' if d['fill'][0] < 0.9 else 'white') for d in p1.get_drawings()
      if d.get('fill') is not None and d['type'] == 'fs' and len(d['items']) == 4
      and abs(d['rect'].width - d['rect'].height) < 0.05 and 15 < d['rect'].width < 25]
top = min(r.y0 for r, _ in sq)
ex = [(r, s) for r, s in sq if r.y0 < top + 3 * 7 * 72 / 25.4]
xs = sorted(ex, key=lambda t: t[0].x0)
clusters, last = [], None
for r, s in xs:
    if last is None or r.x0 - last > 7 * 72 / 25.4 + 1:
        clusters.append([])
    clusters[-1].append((r, s))
    last = r.x0
w = 7 * 72 / 25.4
desc = []
for c in clusters:
    x0, y1 = min(r.x0 for r, _ in c), max(r.y1 for r, _ in c)
    desc.append({(round((r.x0 - x0) / w), round((y1 - r.y1) / w)): s for r, s in c})
old = {(x, y): 'white' for x in range(2) for y in range(2)}
mid = dict(old) | {(2, 0): 'grey', (2, 1): 'grey'}
new = {(x, y): 'white' for x in range(3) for y in range(2)}
check(desc == [old, mid, new], 'old shape 2 x 2; two shaded tiles in a new column; new shape 2 rows by 3 columns')

print('== Problem 11 label on page 6 ==')
p6 = stu[5]
words = p6.get_text('words')
lab = [fitz.Rect(w[:4]) for w in words if w[4] in ('same', 'already', 'added')]
lab_box = fitz.Rect(min(r.x0 for r in lab), min(r.y0 for r in lab), max(r.x1 for r in lab), max(r.y1 for r in lab))
copy = [fitz.Rect(w[:4]) for w in words if w[4] == 'Copy'][0]
boxes2 = [d['rect'] for d in p6.get_drawings() if d['type'] == 's' and 26 < d['rect'].width < 30 and 18 < d['rect'].height < 22]
above = [r for r in boxes2 if r.y1 <= lab_box.y0 + 2 and abs((r.x0 + r.x1) / 2 - (lab_box.x0 + lab_box.x1) / 2) < 5]
check(bool(above) and lab_box.y0 - max(r.y1 for r in above) > 0.5, f'label clears the input box above it by {lab_box.y0 - max(r.y1 for r in above):.1f} pt')
check(copy.y0 - lab_box.y1 > 0.5, f'label clears "Copy the new first total" by {copy.y0 - lab_box.y1:.1f} pt')

print('== Wording and tables ==')
check('Problem 2: Make a square with side 5. Take it apart one layer at a time, always leaving a square in the bottom-left corner. How many tiles come off each time?' in pages[0], 'Problem 2 wording (should 4)')
check('without building it or running the trays for ten turns.' in pages[10], 'Problem 20 wording (should 5)')
check(re.search(r'before 3 first 3 second 3 third add input 1 4 first 3 second 3 third add new first total 4 first 7 second 3 third add new second total 4 first 7 second 10 third', pages[9]) is not None, 'Problem 18 worked turn (3,3,3) -> (4,3,3) -> (4,7,3) -> (4,7,10)')
check(re.search(r'turns first total second total third total 1 2 3 4 5 6', pages[9]) is not None, 'Problem 18 table has a row for each turn 1-6 (could 10)')
check(pages[3].index('Use the supplied input cards') < pages[3].index('Problem 7:'), 'one-tray rules and worked turn come before Problem 7 (could 7)')
check(pages[5].index('Each turn, add the input') < pages[5].index('Problem 11:'), 'two-tray rules and worked turn come before Problem 11 (could 7)')
check('(3, 3, 3)' in guide and '(4, 7, 10)' in guide and 'non-task example' not in guide, 'guide Problem 18 sentence (should 2)')
check('140 × 120 mm board' in guide and '120 × 140' not in guide, 'guide board size matches the materials page (could 12)')
check('K–1 return route.' in guide, 'guide K–1 return route (should 6)')
check('enlarge it to a 2 × 3 rectangle by adding one column' in guide, 'guide launch matches the page 1 example (should 3)')

print('== Guide page references ==')
where = {}
for i, p in enumerate(stu):
    for m in re.findall(r'Problem (\d+):', p.get_text()):
        where[int(m)] = i + 1
check(sorted(where) == list(range(1, 21)), 'Problems 1-20, each once')
claims = [('Problems 1–4 (student pages 1–2)', [1, 2, 3, 4], {1, 2}), ('Problems 5–6 (page 3)', [5, 6], {3}),
          ('Problems 7–10 (pages 4–5)', [7, 8, 9, 10], {4, 5}), ('Problems 11–13 (pages 6–7)', [11, 12, 13], {6, 7}),
          ('14–15 (page 8)', [14, 15], {8}), ('16–17 (page 9)', [16, 17], {9}), ('18–20 (pages 10–11)', [18, 19, 20], {10, 11}),
          ('example on student page 1', [], set())]
for text, probs, pg in claims:
    check(text in guide and {where[k] for k in probs} == pg, f'guide says "{text}"')

print(f'\n{len(FAILS)} failures')
sys.exit(1 if FAILS else 0)
