"""Week 9 (bouncing paths) math check: every board, every problem, every guide claim.

Part A  compares every board read out of the delivered PDFs (extract.py) with my
        transcription (expected.py): sizes, labels, dots, walls, fold/copy lines,
        equal scaling, the rules pictures and the guide's 19 path thumbnails.
Part B  solves every student problem from the board sizes read out of the PDFs,
        with billiards.py (step-by-step simulation, no lcm formula).
Part C  checks each guide sentence against the computation.  Every quoted
        sentence is first confirmed to be in the delivered guide PDF.
Part D  tests the general statements of the guide's overview and section 5.
Lines starting with MISMATCH or NOTE are the ones to read.
"""
import json
import re
import subprocess
from itertools import product
from math import gcd
from pathlib import Path

from billiards import (ball, box_home, christoffel_lower, crossings, cutting_word, fold,
                       segments, sheet_line, slope_ball)
from expected import GUIDE_THUMBS, K1, K1_ICONS, M23, U45, U45_CHART
from pdfgeom import PDF, words

HERE = Path(__file__).resolve().parent
GEO = HERE / 'pdf_geometry.json'
subprocess.run(['python3', str(HERE / 'extract.py')], check=True, stdout=subprocess.DEVNULL)
geo = json.loads(GEO.read_text())

n_checks = 0
problems = []


def check(label, ok, detail=''):
    global n_checks
    n_checks += 1
    tag = 'ok      ' if ok else 'MISMATCH'
    print(f'  {tag} {label}' + (f': {detail}' if detail else ''))
    if not ok:
        problems.append(label)


def note(label, detail):
    print(f'  NOTE     {label}: {detail}')


def lcm(a, b):
    return a * b // gcd(a, b)


def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    s = s.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    return re.sub(r'\s+', ' ', s).strip()


def pdf_text(path):
    raw = subprocess.run(['pdftotext', str(path), '-'], capture_output=True, text=True, check=True).stdout
    lay = subprocess.run(['pdftotext', '-layout', str(path), '-'], capture_output=True, text=True, check=True).stdout
    return norm(raw), norm(raw.replace('-\n', '')), norm(lay)


GUIDE_TEXT = pdf_text(PDF['guide'])
STUDENT_TEXT = {k: pdf_text(PDF[k]) for k in ('K-1', '2-3', '4-5')}


def quoted(q, where=None):
    """Is this sentence in the delivered guide (or a student PDF)?"""
    texts = GUIDE_TEXT if where is None else STUDENT_TEXT[where]
    qn = norm(q)
    ok = any(qn in t for t in texts)
    if not ok:
        print(f'  MISSING-QUOTE {qn[:90]}')
        problems.append('quote not found: ' + qn[:60])
    return ok


def CN(c):
    return {'TR': 'top right', 'TL': 'top left', 'BR': 'bottom right', 'BL': 'bottom left'}[c]


# =========================================================== Part A: boards
print('Part A. Boards read from the PDFs against my transcription')


def page_grids(band, page):
    gs = geo[band].get(str(page), {}).get('grids', [])
    # reading order: rows share a bottom edge (items in a row are bottom-aligned)
    return sorted(gs, key=lambda g: (-round(g['y0'] / 12), g['x0']))


def compare_band(band, expected):
    for page, items in expected.items():
        gs = page_grids(band, page)
        check(f'{band} p{page}: {len(items)} boards', len(gs) == len(items), f'found {len(gs)}')
        for (w, h, kind, ex), g in zip(items, gs):
            name = f'{band} p{page} {w} by {h} {kind}'
            ok = (g['w'], g['h']) == (w, h)
            ok &= g['uniform'] and g['full_lines']
            ok &= abs(g['cell_w'] - g['cell_h']) < 0.01            # equal scaling
            ok &= abs(g['side_in'][0] - ex['side']) < 0.002
            ok &= g['walls'] == (kind != 'blank')
            lines = ex.get('lines', ([], []))
            if kind == 'sheet':
                ok &= (g['thick_x'], g['thick_y']) == tuple(lines) and not g['dashed_x']
            elif kind == 'fold':
                ok &= (g['dashed_x'], g['dashed_y']) == tuple(lines) and not g['thick_x']
            else:
                ok &= not (g['thick_x'] or g['thick_y'] or g['dashed_x'] or g['dashed_y'])
            ok &= not g['thick_other']
            dot = ex.get('dot')
            want = [] if dot is None else [(0 if dot[1] == 'L' else w, 0)]
            ok &= [tuple(d[:2]) for d in g['dots']] == want
            if 'label' in ex:
                ok &= g['label'] == ex['label']
            ok &= bool(g['boxes']) == bool(ex.get('box'))
            detail = (f"measured {g['w']} x {g['h']}, cell {g['side_in']} in, walls {g['walls']}, "
                      f"thick {g['thick_x']}/{g['thick_y']}, dashed {g['dashed_x']}/{g['dashed_y']}, "
                      f"dots {g['dots']}, label '{g['label']}', boxes {g['boxes']}")
            check(name, ok, detail)
            # the label, where printed, names the drawn size ("w by h" = w wide, h high)
            if kind == 'table' and 'label' in ex and ex['label'].endswith(f'{w} by {h}'):
                check(f'{name}: printed label matches the drawn width and height',
                      g['label'] == f"{g['w']} by {g['h']}", g['label'])
            if ex.get('rules'):
                path = g['path'][0]['pts']
                steps = len(path) - 2          # whole steps, then the arrow shaft ends part-way
                sim = ball(w, h)['points']
                okp = [tuple(p) for p in path[:-1]] == [tuple(map(float, q)) for q in sim[:steps + 1]]
                last = path[-1]
                a, b = sim[steps], sim[steps + 1]
                # the shaft's last point lies on the segment to the next lattice point
                t = (last[0] - a[0]) / (b[0] - a[0])
                okp &= 0 < t < 1 and abs((last[1] - a[1]) - t * (b[1] - a[1])) < 0.01
                check(f'{name}: rules picture path follows the ball, arrow ends inside the table',
                      okp, f'{path} vs simulation {sim[:steps + 2]}')


compare_band('K-1', K1)
compare_band('2-3', M23)
compare_band('4-5', U45)

for page, rings in K1_ICONS.items():
    icons = sorted(geo['K-1'][str(page)]['icons'], key=lambda i: -i['y'])
    got = [(i.get('dot'), i.get('ring')) for i in icons]
    want = [('bl', r.lower()) for r in rings]
    check(f'K-1 p{page}: small pictures (dot, ring corner) top to bottom', got == want, str(got))

ch = geo['4-5']['2']['chart']
check('4-5 p2 chart: 6 by 6 square boxes', ch['cols'] == 6 and ch['rows'] == 6 and
      abs(ch['cell_w'] - ch['cell_h']) < 1e-3, str(ch))
w45 = words(PDF['4-5'])[2]
ch_box = [w for w in w45 if 90 < w[1] < 560 and 220 < w[2] < 640]     # the chart and its axis labels only
nums = [w for w in ch_box if re.fullmatch(r'[1-6]', w[0])]
bottom = sorted([w for w in nums if w[2] < min(n[2] for n in nums) + 5], key=lambda w: w[1])
left = sorted([w for w in nums if w not in bottom], key=lambda w: w[2])
check('4-5 p2 chart: widths 1-6 left to right under the columns, heights 1-6 bottom to top',
      [w[0] for w in bottom] == list('123456') and [w[0] for w in left] == list('123456'))
lab_w = [w for w in ch_box if w[0] == 'width']
lab_h = [w for w in ch_box if w[0] == 'height']
check('4-5 p2 chart: "width" under the columns, "height" beside the rows',
      bool(lab_w) and bool(lab_h) and lab_w[0][2] < bottom[0][2] and lab_h[0][1] < left[0][1])

# guide thumbnails
for page, thumbs in GUIDE_THUMBS.items():
    gs = sorted(geo['guide'][str(page)]['grids'], key=lambda g: (-round(g['y0'] / 12), g['x0']))
    gw = words(PDF['guide'])[page]
    check(f'guide p{page}: {len(thumbs)} path thumbnails', len(gs) == len(thumbs), f'found {len(gs)}')
    for (w, h, start, cap1, cap2), g in zip(thumbs, gs):
        r = ball(w, h, start)
        sim = [tuple(map(float, p)) for p in r['points']]
        path = [tuple(p) for p in g['path'][0]['pts']] if g['path'] else []
        cx, cy = {'TR': (w, h), 'TL': (0, h), 'BR': (w, 0)}[r['corner']]
        sx = 0 if start == 'BL' else w
        ok = (g['w'], g['h']) == (w, h) and abs(g['cell_w'] - g['cell_h']) < 0.01
        ok &= path == sim
        ok &= [tuple(d[:2]) for d in g['dots']] == [(sx, 0)]
        ok &= [tuple(x) for x in g['rings']] == [(float(cx), float(cy))]
        # caption directly below the thumbnail
        below = [x for x in gw if x[4] < g['y0'] and g['y0'] - x[4] < 30 and
                 g['x0'] - 25 < (x[1] + x[3]) / 2 < g['x1'] + 25]
        below.sort(key=lambda x: (-round(x[4]), x[1]))
        cap = ' '.join(x[0] for x in below)
        want = cap1 if cap2 is None else cap1 + ' ' + cap2
        ok &= cap.startswith(want)
        if cap2 is not None:
            if cap2[0].isdigit():
                n, rest = cap2.split(' ', 1)
                ok &= int(n) == r['bounces'] and rest == f'({CN(r["corner"])})'
            else:
                cname, n = cap2.split(', ')
                ok &= cname == CN(r['corner']) and int(n) == r['bounces']
        check(f'guide p{page} thumbnail {cap1}: drawn path = simulated path, dot, ring, caption',
              ok, f"caption '{cap}', simulated {CN(r['corner'])} {r['bounces']}")


# =========================================================== Part B: student problems
print('\nPart B. Student problems solved from the boards in the PDFs')


def tables(band, page, kind='table', rules=False):
    out = []
    for (w, h, k, ex), g in zip({'K-1': K1, '2-3': M23, '4-5': U45}[band][page], page_grids(band, page)):
        if k == kind and bool(ex.get('rules')) == rules:
            out.append((g['w'], g['h']))
    return out


def outcome(w, h, start='BL'):
    r = ball(w, h, start)
    return r['corner'], r['bounces']


def show(ts):
    return '; '.join(f'{w} by {h} {outcome(w, h)[0]} {outcome(w, h)[1]}' for w, h in ts)


ANS = {}
print(' K-1')
fl = tables('K-1', 1)
for (w, h), start in zip(fl, ('BL', 'BR')):
    r = ball(w, h, start)
    print(f'    P1 floor {w} by {h} from {start}: {CN(r["corner"])}, {r["bounces"]} bounces, {r["steps"]} steps, '
          f'crossings {crossings(w, h, start)["count"]}')
    ANS[('K-1', 1, start)] = r
for p, prob in ((2, 2), (3, 3), (4, 4), (5, 4)):
    print(f'    P{prob} (p{p}): {show(tables("K-1", p))}')
for target in ('TL', 'BR', 'TR'):
    sols = [(w, h) for w in range(1, 4) for h in range(1, 4) if outcome(w, h)[0] == target]
    print(f'    P5 {target} on a 3 by 3 grid: {sols}')
    ANS[('K-1', 5, target)] = sols
    check(f'K-1 P5 {target} has a table on the 3 by 3 grid', bool(sols))
home = [(w, h) for w in range(1, 5) for h in range(1, 5) if outcome(w, h)[0] == 'BL']
check('K-1 P6: no table on the 4 by 4 grids returns to the dot', not home, str(home))
k8 = page_grids('K-1', 8)
for big, small in ((k8[0], k8[1]), (k8[2], k8[3]), (k8[4], k8[5])):
    W, H = big['w'], big['h']
    xs = [0] + big['dashed_x'] + [W]
    pw = {b - a for a, b in zip(xs, xs[1:])}
    w, h = small['w'], small['h']
    ok = W == H and pw == {w} and H == h
    s = sheet_line(w, h, W // w, 1, 'opposite-corner')
    ok &= set(s['folded']) == set(segments(ball(w, h)['points'])) and W == lcm(w, h)
    check(f'K-1 P7: {W} by {W} square folded on its dashed lines is the {w} by {h} table; the line to the far '
          f'corner folds onto the whole ball path', ok,
          f'panels {s["panels"]}, folded = {CN(ball(w, h)["corner"])} {ball(w, h)["bounces"]}')

print(' Grades 2-3')
for p, prob in ((1, 1), (2, 2), (3, 3)):
    print(f'    P{prob}: {show(tables("2-3", p))}')
TARGETS23 = [('BR', 1), ('TR', 4), ('TL', 7), ('TR', 3)]
labels23 = [g['label'] for g in page_grids('2-3', 4)]
for (c, n), lab_, g in zip(TARGETS23, labels23, page_grids('2-3', 4)):
    check(f'2-3 P4 label reads {CN(c)} after {n}', lab_ == f"stops at the {CN(c)} after {n} bounce{'s' if n != 1 else ''}")
    sols = [(w, h) for w in range(1, g['w'] + 1) for h in range(1, g['h'] + 1) if outcome(w, h) == (c, n)]
    every = [(w, h) for w in range(1, 61) for h in range(1, 61) if outcome(w, h) == (c, n)]
    print(f'    P4 {c} {n}: on the {g["w"]} by {g["h"]} grid {sols}; all tables up to 60 by 60: {every}')
    ANS[('2-3', 4, c, n)] = sols
one = [(w, h) for w in range(1, 7) for h in range(1, 7) if outcome(w, h)[1] == 1]
print(f'    P6 one bounce up to 6 by 6: {one}')
ANS[('2-3', 6)] = one
k7 = page_grids('2-3', 7)
for big, small in ((k7[0], k7[1]), (k7[2], k7[3])):
    w, h = small['w'], small['h']
    xs = [0] + big['thick_x'] + [big['w']]
    ys = [0] + big['thick_y'] + [big['h']]
    ok = {b - a for a, b in zip(xs, xs[1:])} == {w} and {b - a for a, b in zip(ys, ys[1:])} == {h}
    s = sheet_line(w, h, big['w'] // w, big['h'] // h, 'opposite-corner')
    ok &= s['end'] == (big['w'], big['h']) and s['connected']
    ok &= set(s['folded']) == set(segments(ball(w, h)['points']))
    print(f'    P7 {big["w"]} by {big["h"]} sheet of {w} by {h}: crosses {len(s["crossed"])} thick lines '
          f'{s["crossed"]}, passes through {len(s["panels"])} tables {s["panels"]}; folded = {w} by {h} path '
          f'{CN(ball(w, h)["corner"])} {ball(w, h)["bounces"]}')
    check(f'2-3 P7 {big["w"]} by {big["h"]} sheet: copies of the {w} by {h} table; the line to the opposite '
          f'corner folds onto the whole ball path; crossings = bounces',
          ok and len(s['crossed']) == ball(w, h)['bounces'])
    ANS[('2-3', 7, w, h)] = s
home = [(w, h) for w in range(1, 201) for h in range(1, 201) if outcome(w, h)[0] == 'BL']
check('2-3 P8 / 4-5 P7 / K-1 P6: no table up to 200 by 200 stops at the start corner', not home)

print(' Grades 4-5')
print(f'    P1: {show(tables("4-5", 1))}')
chart = {(w, h): outcome(w, h) for w in range(1, 7) for h in range(1, 7)}
for h in range(6, 0, -1):
    print('    P2 h=%d: ' % h + '  '.join(f'{chart[(w, h)][0]} {chart[(w, h)][1]}' for w in range(1, 7)))
s3 = page_grids('4-5', 4)
big, small = s3[0], s3[1]
w, h = small['w'], small['h']
s = sheet_line(w, h, big['w'] // w, big['h'] // h, 'first-crossing')
ok = s['fits'] and s['connected'] and set(s['folded']) == set(segments(ball(w, h)['points']))
print(f'    P3 {big["w"]} by {big["h"]} sheet of {w} by {h}: first crossing {s["end"]}, crosses {s["crossed"]}, '
      f'tables {s["panels"]}')
check('4-5 P3: the line on the sheet reaches a crossing of thick lines inside the sheet and folds to the 2 by 3 path',
      ok and len(s['crossed']) == ball(w, h)['bounces'])
ANS[('4-5', 3)] = s
g4 = page_grids('4-5', 5)[0]
s4 = sheet_line(4, 3, 3, 4, 'first-crossing')
check('4-5 P4: the 4 by 3 sheet up to the first crossing fits the 13 by 13 grid',
      s4['end'][0] <= g4['w'] and s4['end'][1] <= g4['h'], f'end {s4["end"]}, grid {g4["w"]} by {g4["h"]}')
print(f'    P4 4 by 3 sheet: first crossing {s4["end"]} = {s4["end"][0] // 4} tables across, {s4["end"][1] // 3} up; '
      f'crosses {len(s4["crossed"])} thick lines; ball {outcome(4, 3)}')
ANS[('4-5', 4)] = s4
P5 = [(6, 10), (8, 12), (12, 9), (7, 5), (5, 8), (20, 30)]
check('4-5 P5: the six tables printed in the table', all(STUDENT_TEXT['4-5'][0].count(f'{a} by {b}') for a, b in P5))
print(f'    P5: {show(P5)}; 6 by 10 takes {ball(6, 10)["steps"]} steps')
TARGETS45 = [('TL', 13), ('TR', 8), ('BR', 11), ('BR', 10)]
g6 = page_grids('4-5', 7)[0]
for c, n in TARGETS45:
    on = [(w, h) for w in range(1, g6['w'] + 1) for h in range(1, g6['h'] + 1) if outcome(w, h) == (c, n)]
    every = [(w, h) for w in range(1, 61) for h in range(1, 61) if outcome(w, h) == (c, n)]
    print(f'    P6 {c} {n}: on the {g6["w"]} by {g6["h"]} grid {on}; all up to 60 by 60 {every}')
    ANS[('4-5', 6, c, n)] = (on, every)
bad = [(w, h) for w in range(1, 61) for h in range(1, 61)
       if outcome(w, h) != ((('T' if (lcm(w, h) // h) % 2 else 'B') + ('R' if (lcm(w, h) // w) % 2 else 'L')),
                            lcm(w, h) // w + lcm(w, h) // h - 2)]
check('4-5 P8: corner by parity of tables across/up and bounces = across + up - 2, all tables up to 60 by 60',
      not bad, str(bad[:5]))


# =========================================================== Part C: the guide
print('\nPart C. The adult guide against the computation')


def claim(q, ok, detail=''):
    if quoted(q):
        check(q[:100] + ('...' if len(q) > 100 else ''), ok, detail)


def says(q):
    """A guide sentence whose correctness is judged in a NOTE below rather than by one test."""
    quoted(q)


# overview
claim('2 by 3 and 4 by 6 both stop at the bottom right after 3 bounces.',
      outcome(2, 3) == outcome(4, 6) == ('BR', 3))
scal = all(outcome(k * w, k * h) == outcome(w, h) for w in range(1, 21) for h in range(1, 21) for k in range(2, 6))
claim('A bigger copy of a table (both sides doubled or tripled) behaves exactly like the small one', scal)

# K-1 floor and launch
r = ANS[('K-1', 1, 'BL')]
rr = ANS[('K-1', 1, 'BR')]
claim('Both walks end at the far opposite corner after 6 bounces',
      r['corner'] == 'TR' and rr['corner'] == 'TL' and r['bounces'] == rr['bounces'] == 6)
claim('From the left dot: the far right corner, 6 bounces (15 steps). From the right dot: the far left corner, 6 bounces.',
      (r['corner'], r['bounces'], r['steps']) == ('TR', 6, 15) and (rr['corner'], rr['bounces']) == ('TL', 6))
cr = crossings(3, 5)
claim('The path crosses itself four times; the walker just keeps going.', cr['count'] == 4 and
      crossings(3, 5, 'BR')['count'] == 4, str(cr))
claim('A K–1 child stands on the dot and takes three slanted steps, landing on the right-hand wall.',
      r['hits'][0][0] == (3, 3) and r['hits'][0][1] == 'R')
claim('use a block 3 tiles across and 5 tiles long', True)
claim('tape a rectangle 4½ ft by 7½ ft (1.35 m by 2.25 m), mark every 18 inches (45 cm) along all four sides',
      4.5 * 12 / 18 == 3 and 7.5 * 12 / 18 == 5 and abs(1.35 / 0.45 - 3) < 1e-9 and abs(2.25 / 0.45 - 5) < 1e-9)
tape = 2 * (4.5 + 7.5) + 2 * 7.5 + 4 * 4.5
claim('run 2 tape lines the long way and 4 across. That gives 3 by 5 squares of 18 inches, using about 60 ft of tape.',
      abs(tape - 60) <= 5, f'{tape} ft of tape (single walls)')
note('floor-grid tape', f'single walls use {tape} ft; doubling the outside walls as step 3 suggests adds '
     f'{2 * (4.5 + 7.5)} ft, {tape + 24} ft in all, beyond the "about 60 ft" in the list (the second-colour '
     f'option stays within it)')
rope = {(3, 1): ('TR', 2), (3, 2): ('TL', 3), (3, 3): ('TR', 0), (3, 4): ('TL', 5), (2, 5): ('BR', 5), (1, 5): ('TR', 4)}
claim('From the left dot: rope 1 square up (3 by 1) far right, 2 bounces; 2 up (3 by 2) far left, 3; 3 up (3 by 3) far '
      'right, 0; 4 up (3 by 4) far left, 5. Rope the long way leaving 2 columns (2 by 5): near right, 5 bounces; '
      'leaving 1 column (1 by 5): far right, 4.', all(outcome(*t) == v for t, v in rope.items()))

# K-1 problem answers
K1P2 = {(2, 2): ('TR', 0), (1, 3): ('TR', 2), (2, 1): ('BR', 1), (2, 3): ('BR', 3), (3, 3): ('TR', 0), (3, 2): ('TL', 3)}
check('guide K-1 P2 answers (thumbnail captions, checked in Part A) cover the six page-2 tables',
      sorted(tables('K-1', 2)) == sorted(K1P2) and all(outcome(*t) == v for t, v in K1P2.items()))
check('guide K-1 P3 answers 3, 4, 5, 5 for 1 by 4, 1 by 5, 2 by 5, 3 by 4',
      [outcome(*t)[1] for t in tables('K-1', 3)] == [3, 4, 5, 5], str(tables('K-1', 3)))
claim('On the one-square-wide tables the ball touches a wall at every step except the last.',
      all(ball(1, n)['bounces'] == ball(1, n)['steps'] - 1 for n in range(1, 30)))
check('guide K-1 P4 answers: 1 by 2, 2 by 4, 3 by 6 top left, 1; 2 by 3 and 4 by 6 bottom right, 3',
      [outcome(*t) for t in tables('K-1', 4) + tables('K-1', 5)] == [('TL', 1)] * 3 + [('BR', 3)] * 2)
claim('Answer: Every table that fits the 3 by 3 grids. Top left: 1 by 2 or 3 by 2. Bottom right: 2 by 1 or 2 by 3. '
      'Top right: 1 by 1, 1 by 3, 2 by 2, 3 by 1 or 3 by 3.',
      ANS[('K-1', 5, 'TL')] == [(1, 2), (3, 2)] and ANS[('K-1', 5, 'BR')] == [(2, 1), (2, 3)] and
      ANS[('K-1', 5, 'TR')] == [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)])
claim('Top left: try one square wide and two tall. Bottom right: two wide and one tall. Top right: any square.',
      outcome(1, 2)[0] == 'TL' and outcome(2, 1)[0] == 'BR' and all(outcome(n, n)[0] == 'TR' for n in range(1, 4)))
claim('Answer: There is none.', True)
claim('2 by 2 square: the 1 by 2 path (top left, 1 bounce). 3 by 3 square: the 1 by 3 path (top right, 2 bounces). '
      '4 by 4 square: the 2 by 4 path (top left, 1 bounce).',
      outcome(1, 2) == ('TL', 1) and outcome(1, 3) == ('TR', 2) and outcome(2, 4) == ('TL', 1))
claim('These match the paths on pages 2 and 4.',
      (1, 3) in tables('K-1', 2) and (1, 2) in tables('K-1', 4) and (2, 4) in tables('K-1', 4))
claim('stay with the small tables (2 by 2, 1 by 3 and 2 by 1 on page 2; 1 by 2 on page 4)',
      {(2, 2), (1, 3), (2, 1)} <= set(tables('K-1', 2)) and (1, 2) in tables('K-1', 4))
claim('skip the 2 by 5, 3 by 4 and 4 by 6 tables and Problem 5.',
      (2, 5) in tables('K-1', 3) and (3, 4) in tables('K-1', 3) and (4, 6) in tables('K-1', 5))

# The direction rule of thumb in the K-1 walking instructions and hints
print('  -- the "keep going up" rule of thumb (K-1 floor walk and hints)')
says('After a side wall, keep going up the grid but slant the other way; after the far end, keep slanting the same '
     'way but come back down the grid.')
says('Hints: (1) "Which way were you slanting before the wall? Keep going up the room and slant the other way."')
says('(2) Move the counter one square at a time and stop at each wall: "Which way now? Keep going up, and turn away '
     'from the wall."')
for start in ('BL', 'BR'):
    hs = ball(3, 5, start)['hits']
    desc = ', '.join(f'{wall} at {pt} going {"up" if d[1] > 0 else "down"}' for pt, wall, d in hs)
    side_down = [x for x in hs if x[1] in 'LR' and x[2][1] < 0]
    near_end = [x for x in hs if x[1] == 'B']
    note(f'K-1 P1 floor walk from {start}', f'bounces: {desc}. Side walls met while going down: {len(side_down)}; '
         f'near-end (bottom) bounces: {len(near_end)}. The printed rule sends the walker the wrong way at each side '
         f'wall met going down and has no rule for the near end.')
tot = dict(bounces=0, side_down=0, top=0, bottom=0)
for page in (2, 3, 4, 5):
    for t in tables('K-1', page):
        hs = ball(*t)['hits']
        side_down = [f'{wall} at {pt}' for pt, wall, d in hs if wall in 'LR' and d[1] < 0]
        top = [f'T at {pt}' for pt, wall, d in hs if wall == 'T']
        bottom = [f'B at {pt}' for pt, wall, d in hs if wall == 'B']
        if page == 2:
            tot['bounces'] += len(hs)
            tot['side_down'] += len(side_down)
            tot['top'] += len(top)
            tot['bottom'] += len(bottom)
        if side_down or top or bottom:
            note(f'K-1 p{page} {t[0]} by {t[1]}',
                 f'{len(hs)} bounces; side walls met going down (the hint gives a wrong move): {side_down or "none"}; '
                 f'top wall (the hint contradicts itself): {top or "none"}; bottom wall: {bottom or "none"}')
note('K-1 page 2 (Problem 2) in all', f"{tot['bounces']} bounces: {tot['side_down']} side walls met going down, "
     f"{tot['top']} top-wall bounces, {tot['bottom']} bottom-wall bounce(s); the rest are side walls met going up")

# Grades 2-3
G23P1 = {(2, 3): ('BR', 3), (3, 2): ('TL', 3), (1, 4): ('TL', 3), (3, 4): ('TL', 5), (4, 3): ('BR', 5), (3, 5): ('TR', 6)}
claim('Answer: 2 by 3 BR 3; 3 by 2 TL 3; 1 by 4 TL 3; 3 by 4 TL 5; 4 by 3 BR 5; 3 by 5 TR 6.',
      sorted(tables('2-3', 1)) == sorted(G23P1) and all(outcome(*t) == v for t, v in G23P1.items()))
claim('Answer: 1 by 2, 2 by 4, 3 by 6: all TL 1. 1 by 3 and 2 by 6: TR 2. 4 by 6: BR 3 (it is 2 by 3 doubled, not a copy of 1 by 3).',
      [outcome(*t) for t in tables('2-3', 2)] == [('TL', 1)] * 3 + [('TR', 2)] * 2 + [('BR', 3)])
claim('5 by 10: TL 1 (1 by 2 made five times bigger). 8 by 12: BR 3 (2 by 3 made four times bigger).',
      outcome(5, 10) == ('TL', 1) and outcome(8, 12) == ('BR', 3))
claim('BR after 1 bounce: 2 by 1, 4 by 2, 6 by 3. TR after 4: 1 by 5, 5 by 1. TL after 7: 5 by 4 only. TR after 3: impossible.',
      ANS[('2-3', 4, 'BR', 1)] == [(2, 1), (4, 2), (6, 3)] and ANS[('2-3', 4, 'TR', 4)] == [(1, 5), (5, 1)] and
      ANS[('2-3', 4, 'TL', 7)] == [(5, 4)] and ANS[('2-3', 4, 'TR', 3)] == [])
tr_parity = all(outcome(w, h)[1] % 2 == 0 for w in range(1, 121) for h in range(1, 121) if outcome(w, h)[0] == 'TR')
side_even = all(sum(1 for x in ball(w, h)['hits'] if x[1] in 'LR') % 2 == (0 if outcome(w, h)[0][1] == 'R' else 1)
                for w in range(1, 41) for h in range(1, 41))
claim('Even plus even is even, so a top right stop never has 3 bounces.', tr_parity and side_even)
trs = [outcome(*t)[1] for t in tables('2-3', 1) + tables('2-3', 2) if outcome(*t)[0] == 'TR']
claim('(The children can check: every TR on pages 1–2 has 2 or 6.)', set(trs) <= {2, 6}, str(trs))
claim('Check any table up to 6 by 6 in the chart in the 4–5 section below.', True)
claim('Answer: Exactly six tables: 1 by 2, 2 by 4, 3 by 6 (TL) and 2 by 1, 4 by 2, 6 by 3 (BR).',
      sorted(ANS[('2-3', 6)]) == sorted([(1, 2), (2, 4), (3, 6), (2, 1), (4, 2), (6, 3)]) and
      all(outcome(*t)[0] == ('TL' if t[1] > t[0] else 'BR') for t in ANS[('2-3', 6)]))
# the argument: taller than wide, first bounce on the right wall at height w; one bounce iff h = 2w
arg = True
for w in range(1, 30):
    for h in range(w + 1, 60):
        r1 = ball(w, h)
        arg &= r1['hits'][0][:2] == ((w, w), 'R')
        arg &= (r1['bounces'] == 1) == (h == 2 * w)
        if h < 2 * w:
            arg &= r1['hits'][1][1] == 'T'
        if h > 2 * w:
            arg &= r1['hits'][1][1] == 'L'
claim('If the table is taller than it is wide, the first bounce is on the right wall, when the ball has gone up as many '
      'squares as the table is wide.', arg)
claim('a square table has no bounces.', all(outcome(n, n) == ('TR', 0) for n in range(1, 50)))
s7a, s7b = ANS[('2-3', 7, 2, 3)], ANS[('2-3', 7, 1, 3)]
claim('Top sheet (6 by 6, copies of 2 by 3): the line crosses 3 thick lines inside the sheet; it passes through 4 tables '
      '(a staircase); folded, it is the 2 by 3 path, BR 3.',
      len(s7a['crossed']) == 3 and len(s7a['panels']) == 4 and outcome(2, 3) == ('BR', 3))
claim('Bottom sheet (3 by 3, copies of 1 by 3): crosses 2 thick lines, passes through all 3 tables, folds to the 1 by 3 '
      'path, TR 2. Thick lines crossed equal bounces.',
      len(s7b['crossed']) == 2 and len(s7b['panels']) == 3 and outcome(1, 3) == ('TR', 2))
claim('cut out the 4 tables the line passes through as one piece', len(s7a['panels']) == 4 and s7a['connected'])

# reversal argument (2-3 P8, K-1 P6 hint): judged in the report
claim('The ball only turns right around when it hits two walls at once, in a corner, and there it would already have '
      'stopped.', True)

# Grades 4-5
G45P1 = {(2, 3): ('BR', 3), (3, 2): ('TL', 3), (1, 4): ('TL', 3), (3, 4): ('TL', 5), (6, 4): ('TL', 3), (3, 5): ('TR', 6)}
claim('Answer: 2 by 3 BR 3; 3 by 2 TL 3; 1 by 4 TL 3; 3 by 4 TL 5; 6 by 4 TL 3 (3 by 2 doubled); 3 by 5 TR 6.',
      sorted(tables('4-5', 1)) == sorted(G45P1) and all(outcome(*t) == v for t, v in G45P1.items()))
CHART = {6: 'TL 5 TR 2 TL 1 BR 3 TL 9 TR 0', 5: 'TR 4 BR 5 TR 6 BR 7 TR 0 BR 9', 4: 'TL 3 TL 1 TL 5 TR 0 TL 7 TL 3',
         3: 'TR 2 BR 3 TR 0 BR 5 TR 6 BR 1', 2: 'TL 1 TR 0 TL 3 BR 1 TL 5 TR 2', 1: 'TR 0 BR 1 TR 2 BR 3 TR 4 BR 5'}
for h, row in CHART.items():
    toks = row.split()
    claim(f'{h} {row}', all((toks[2 * i], int(toks[2 * i + 1])) == chart[(i + 1, h)] for i in range(6)))
steps36 = sum(ball(w, h)['steps'] for w in range(1, 7) for h in range(1, 7))
claim('Tracing all 36 takes 303 diagonal steps', steps36 == 303, str(steps36))
claim('the diagonal (squares) is TR 0; a box and its doubled box agree; height 1 gives TR for odd widths and BR for even '
      'ones, with width minus 1 bounces; no box is bottom left.',
      all(chart[(n, n)] == ('TR', 0) for n in range(1, 7)) and
      all(chart[(w, h)] == chart[(2 * w, 2 * h)] for w in range(1, 4) for h in range(1, 4)) and
      all(chart[(w, 1)] == ('TR' if w % 2 else 'BR', w - 1) for w in range(1, 7)) and
      all(v[0] != 'BL' for v in chart.values()))
s = ANS[('4-5', 3)]
claim('Answer: The sheet is 8 by 9, copies of 2 by 3. The line first meets a crossing of thick lines at 6 squares across '
      'and 6 up (3 tables across, 2 up). Before that it crosses 3 thick lines: the upright line 2 squares across, the '
      'level line 3 squares up, the upright line 4 squares across. It passes through 4 tables; folded, it is the 2 by 3 '
      'path, BR 3.',
      s['end'] == (6, 6) and s['crossed'] == [('x', 2), ('y', 3), ('x', 4)] and len(s['panels']) == 4 and
      (page_grids('4-5', 4)[0]['w'], page_grids('4-5', 4)[0]['h']) == (8, 9))
s4 = ANS[('4-5', 4)]
claim('Answer: Thick lines every 4 squares across (4, 8, 12) and every 3 up (3, 6, 9, 12). The line first meets a '
      'crossing at 12 across and 12 up: 3 tables across, 4 tables up. It crosses 5 thick lines on the way. The 4 by 3 '
      'table stops BR after 5 bounces.',
      s4['end'] == (12, 12) and len(s4['crossed']) == 5 and outcome(4, 3) == ('BR', 5))
claim('On the 2 by 3 sheet, the line went 3 tables across and ended on the right.', s['end'][0] // 2 == 3 and outcome(2, 3)[0][1] == 'R')
G45P5 = {(6, 10): ('TR', 6), (8, 12): ('BR', 3), (12, 9): ('BR', 5), (7, 5): ('TR', 10), (5, 8): ('TL', 11), (20, 30): ('BR', 3)}
claim('Answer: 6 by 10 TR 6; 8 by 12 BR 3; 12 by 9 BR 5; 7 by 5 TR 10; 5 by 8 TL 11; 20 by 30 BR 3. Tracing the 6 by 10 '
      'takes 30 steps.', all(outcome(*t) == v for t, v in G45P5.items()) and ball(6, 10)['steps'] == 30)
on, every = ANS[('4-5', 6, 'TL', 13)]
claim('TL after 13: 13 by 2, 11 by 4, 7 by 8 (also 1 by 14, which does not fit the grid).',
      sorted(on) == sorted([(13, 2), (11, 4), (7, 8)]) and (1, 14) in every and
      sorted(t for t in every if t not in on) == [(1, 14)] + sorted(t for t in every if t not in on and t != (1, 14)),
      f'on grid {on}; all up to 60: {every}')
on, every = ANS[('4-5', 6, 'TR', 8)]
claim('TR after 8: 9 by 1, 7 by 3, 3 by 7, 1 by 9, and 14 by 6.',
      sorted(on) == sorted([(9, 1), (7, 3), (3, 7), (1, 9), (14, 6)]), f'on grid {on}')
on, every = ANS[('4-5', 6, 'BR', 11)]
claim('BR after 11: 12 by 1, 10 by 3, 8 by 5, 6 by 7, 4 by 9, 2 by 11.',
      sorted(on) == sorted([(12, 1), (10, 3), (8, 5), (6, 7), (4, 9), (2, 11)]), f'on grid {on}')
on, every = ANS[('4-5', 6, 'BR', 10)]
claim('BR after 10: impossible.', not every)
claim('With the sheet: bottom right means an odd number of tables across and an even number up, and bounces are across '
      'plus up minus 2, which is odd.',
      all(outcome(w, h)[1] % 2 == 1 for w in range(1, 61) for h in range(1, 61) if outcome(w, h)[0] == 'BR'))
claim('Choose tables across and tables up that add to 15.', 13 + 2 == 15)
claim('Halfway there the line is at 2 tables across and 3 up, which is also a crossing of thick lines', True)
claim('Example: 12 by 9 shrinks to 4 by 3: 3 across (right), 4 up (bottom), 5 bounces.',
      (12 // gcd(12, 9), 9 // gcd(12, 9)) == (4, 3) and outcome(12, 9) == ('BR', 5))
claim('The line on its sheet goes q tables across and p tables up. The ball stops on the right if q is odd and the left '
      'if even; at the top if p is odd and the bottom if even. Bounces = p + q − 2.',
      all(outcome(w, h) == (('T' if (w // gcd(w, h)) % 2 else 'B') + ('R' if (h // gcd(w, h)) % 2 else 'L'),
                            w // gcd(w, h) + h // gcd(w, h) - 2) for w in range(1, 61) for h in range(1, 61)))
claim('in Problem 5 do only the doubled tables (6 by 10, 8 by 12, 20 by 30).', True)
note('4-5 struggling route', '"doubled" is loose for 20 by 30 (2 by 3 times ten) and 8 by 12 (2 by 3 times four); '
     'all three are copies of a smaller table, which is the intended point. Not counted as a problem.')

# print and materials arithmetic
sheets = 7 * 3 + 6 + 8 * 5 + 2 * 2 + 8 * 4 + 6 + 2
claim('111 student sheets in all.', sheets == 111, str(sheets))
area = sum(w * h for w in range(1, 7) for h in range(1, 7))
g3 = page_grids('4-5', 3)[0]
claim('the 36 tables of Problem 2 need 441 squares, one page has 224.', area == 441 and g3['w'] * g3['h'] == 224,
      f'{area}, {g3["w"]} x {g3["h"]}')
claim('Measure the squares: 3/4 inch on the K–1 pages, 1/2 inch on the others.', True)
rules_sides = {b: [g['side_in'][0] for g in page_grids(b, 1)] for b in ('K-1', '2-3', '4-5')}
note('square sizes on page 1', f'{rules_sides}: the rules picture beside the opening text is 0.5 in on K-1 and 0.4 in '
     f'on 2-3 and 4-5; every numbered problem uses 0.75 in (K-1) or 0.5 in (2-3, 4-5).')
claim('Put a counter on a corner of a K–1 square. It must not cover the next corner, 3/4 inch away.',
      all(abs(g['side_in'][0] - 0.75) < 1e-3 for p in range(2, 9) for g in page_grids('K-1', p)))


# =========================================================== Part D: section 5 and the overview
print('\nPart D. General statements (section 5)')
ok = True
for w in range(1, 21):
    for h in range(1, 21):
        pts = ball(w, h)['points']
        ok &= all(pts[t] == (fold(t, w), fold(t, h)) for t in range(len(pts)))
        ok &= len(pts) - 1 == lcm(w, h)
claim('the bouncing path is the image of the straight line y = x under the folding map (φw , φh ), which is what the '
      'paper sheets do.', ok)
claim('so it first stops at t = L = lcm(w, h).', ok)
claim('L/w + L/h − 2 bounces.', all(outcome(w, h)[1] == lcm(w, h) // w + lcm(w, h) // h - 2
                                    for w in range(1, 61) for h in range(1, 61)))
claim('Stopping at (0, 0) needs p and q both even, impossible for coprime p, q.', True)
par = all((outcome(w, h)[1] % 2 == 1) == (outcome(w, h)[0] in ('TL', 'BR')) for w in range(1, 81) for h in range(1, 81))
claim('p + q − 2 is odd iff exactly one of p, q is even iff the ball stops TL or BR; TR means both odd, so an even count.', par)
ok = True
for c in ('TL', 'TR', 'BR'):
    for n in range(0, 25):
        sim = {(w, h) for w in range(1, 61) for h in range(1, 61) if outcome(w, h) == (c, n)}
        form = set()
        for p in range(1, 61):
            for q in range(1, 61):
                if gcd(p, q) == 1 and p + q == n + 2:
                    corner = ('T' if p % 2 else 'B') + ('R' if q % 2 else 'L')
                    if corner == c:
                        form |= {(k * p, k * q) for k in range(1, 61) if k * p <= 60 and k * q <= 60}
        ok &= sim == form
claim('A table stops at a given corner after n bounces iff it is a multiple (kp, kq) of a coprime pair with p + q = n + 2 '
      'and the right parities.', ok)
claim('One bounce: {p, q} = {1, 2}, one side twice the other.',
      {(w, h) for w in range(1, 61) for h in range(1, 61) if outcome(w, h)[1] == 1} ==
      {(w, h) for w in range(1, 61) for h in range(1, 61) if w == 2 * h or h == 2 * w})
ok = True
for w in range(1, 13):
    for h in range(1, 13):
        g = gcd(w, h)
        p, q = w // g, h // g
        s = sheet_line(w, h, q, p, 'first-crossing')
        ok &= s['end'] == (lcm(w, h),) * 2 and len(s['crossed']) == (q - 1) + (p - 1) and len(s['panels']) == p + q - 1
claim('On a sheet of copies, the diagonal first meets a crossing of copy walls at (L, L), after q tables across and p up, '
      'crossing (q − 1) + (p − 1) walls and visiting p + q − 1 tables in a staircase', ok)
ok = True
for w in range(1, 7):
    for h in range(1, 7):
        for a in range(1, 5):
            for b in range(1, 5):
                if gcd(a, b) == 1:
                    ok &= slope_ball(w, h, a, b) == outcome(a * w, b * h)
claim('Other slopes: direction (b, a) on a w by h table is slope 1 on an aw by bh table (rescale the', ok)
ok = True
for w in range(1, 13):
    for h in range(1, 13):
        for d in range(1, 13):
            t, home = box_home(w, h, d)
            ok &= t == lcm(lcm(w, h), d) and not home
claim('A box w × h × d works the same with lcm(w, h, d), and the ball still never returns home.', ok)
pal = True
central = True
whole = False
for w in range(1, 25):
    for h in range(1, 25):
        word = cutting_word(w, h)
        g = gcd(w, h)
        p, q = w // g, h // g
        cw = christoffel_lower(q, p).replace('x', 'S').replace('y', 'E')
        pal &= word == word[::-1] and len(word) == p + q - 2
        central &= word == cw[1:-1]
        whole |= word == cw
says('The order of side and end hits along the path is a cutting sequence (a Christoffel word), built by the Euclidean '
     'algorithm on w and h.')
note('section 5 "cutting sequence (a Christoffel word)"',
     f'for every table up to 24 by 24 the side/end sequence has p + q - 2 letters and is a palindrome ({pal}); it equals '
     f'the lower Christoffel word with its first and last letters removed (the central word) ({central}); it equals a '
     f'whole Christoffel word for no table ({not whole}).')

# section 6 "Claims to listen for" (a three-column table on p. 10, so the cells are checked by hand
# against the rendered page and only computed here)
print('  -- section 6 claims to listen for (p. 10 table)')
T = range(1, 61)
check('"It never comes back to the dot."', all(outcome(w, h)[0] != 'BL' for w in T for h in T))
check('"A bigger copy ends in the same corner." / "Doubling both sides gives the same corner and bounces."',
      all(outcome(2 * w, 2 * h) == outcome(w, h) for w in range(1, 31) for h in range(1, 31)))
check('"Square tables go straight to the corner."', all(ball(n, n)['bounces'] == 0 for n in T))
check('"One bounce means one side is twice the other."',
      all((outcome(w, h)[1] == 1) == (w == 2 * h or h == 2 * w) for w in T for h in T))
check('"Top right always has an even number of bounces."',
      all(outcome(w, h)[1] % 2 == 0 for w in T for h in T if outcome(w, h)[0] == 'TR'))
check('"Odd number of tables across means the right side." "Bounces are tables across plus tables up minus 2."',
      all(outcome(w, h)[0][1] == ('R' if (lcm(w, h) // w) % 2 else 'L') and
          outcome(w, h)[1] == lcm(w, h) // w + lcm(w, h) // h - 2 for w in T for h in T))
check('"It can\'t come home: both would be even and you could halve."',
      all(not ((lcm(w, h) // w) % 2 == 0 and (lcm(w, h) // h) % 2 == 0) for w in T for h in T))

print(f'\n{n_checks} checks, {len(problems)} mismatches')
for p in problems:
    print('  MISMATCH:', p)
