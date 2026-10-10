"""Week 12 return visit (student pages): read every counter circle, grid and path from the PDF and
solve each problem from the extracted data.  Run: python3 check_rv.py > check_rv.out"""
import sys
import os
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G
import comb as C

FAIL = []
RED = (0.68, 0.17, 0.21)
BLUE = (0.12, 0.39, 0.65)


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))
    if not ok:
        FAIL.append(name)


def col(c):
    return tuple(round(x, 2) for x in c)


def read_boards(page):
    big = [c for c in page.circles if not c['fill'] and c['r'] > 20]
    counters = [c for c in page.circles if c['fill'] and c['stroke'] and c['r'] < 12]
    letters = [w for w in page.words if w['text'] in ('R', 'B')]
    panel = [w for w in page.words if w['text'] in ('A', 'B', 'C') and 'Bold' in w['font']]
    boards = []
    for c in sorted(big, key=lambda c: (round(c['cy']), c['cx'])):
        mine = [k for k in counters if abs(math.dist((k['cx'], k['cy']), (c['cx'], c['cy'])) - c['r']) < 0.8]
        mine.sort(key=lambda k: G.clockwise_angle(c['cx'], c['cy'], k['cx'], k['cy']))
        probs = []
        word = ''
        for i, k in enumerate(mine):
            a = G.clockwise_angle(c['cx'], c['cy'], k['cx'], k['cy'])
            if abs(a - i * 60) > 0.3:
                probs.append(f'counter {i + 1} at {a:.1f} deg')
            inside = [w for w in letters if math.dist((w['cx'], w['cy']), (k['cx'], k['cy'])) < k['r']]
            if len(inside) != 1:
                probs.append(f'{len(inside)} letters in counter {i + 1}')
                word += '?'
                continue
            L = inside[0]['text']
            colour = 'R' if col(k['scolor']) == RED else 'B' if col(k['scolor']) == BLUE else '?'
            if colour != L:
                probs.append(f'counter {i + 1}: letter {L} on {colour} colour')
            word += L
        # the panel letter: bold A/B/C outside every counter, nearest the circle's upper-left
        cand = [w for w in panel if not any(math.dist((w['cx'], w['cy']), (k['cx'], k['cy'])) < k['r'] for k in counters)]
        lab = min(cand, key=lambda w: math.dist((w['cx'], w['cy']), (c['cx'] - c['r'], c['cy'] - c['r'])))
        boards.append(dict(r=c['r'], word=word, label=lab['text'], n=len(mine), probs=probs))
    return boards


def unlike(word):
    return [m for m in C.nc_matchings(len(word)) if all(word[a - 1] != word[b - 1] for a, b in m)]


pages = G.load('week-12-return-visit.pdf')
print('== Problem 1 (pages 1-2)')
expect = {'A': 'RBRBRB', 'B': 'RRRBBB', 'C': 'RRBRBB'}
counts = {}
for pno in (1, 2):
    boards = read_boards(pages[pno - 1])
    for b in boards:
        print(f'  page {pno} board {b["label"]} (r={b["r"] / 72:.2f} in): {b["word"]}' + (f' PROBLEMS {b["probs"]}' if b['probs'] else ''))
    check(f'page {pno}: every counter on its circle at 60-degree places from the top, letter matches colour',
          all(not b['probs'] and b['n'] == 6 for b in boards))
    check(f'page {pno}: every board carries its arrangement (A RBRBRB, B RRRBBB, C RRBRBB clockwise from the top)',
          all(expect[b['label']] == b['word'] for b in boards), [(b['label'], b['word']) for b in boards])
    for lab in 'ABC':
        counts.setdefault(lab, []).append(sum(1 for b in boards if b['label'] == lab))
print('  boards per arrangement (page 1, page 2):', counts)
for lab, w in expect.items():
    ms = unlike(w)
    print(f'  {lab} {w}: {len(ms)} unlike pairings {[C.fmt(m) for m in ms]}')
    check(f'P1 {lab}: {len(ms)} pairing(s) and {sum(counts[lab])} boards to record them', sum(counts[lab]) >= len(ms))
check('P1: counts 5, 1, 2', [len(unlike(expect[k])) for k in 'ABC'] == [5, 1, 2])

print()
print('== Problems 2-3 (page 3)')
p = pages[2]
grey = [pl for pl in p.polylines if col(pl['scolor']) == (0.85, 0.85, 0.85)]
solid = [pl for pl in p.polylines if abs(pl['lw'] - 0.9) < 0.05 and pl['dash'] is None]
dashed = [pl for pl in p.polylines if abs(pl['lw'] - 0.9) < 0.05 and pl['dash'] is not None]
probs = []
for b in solid:
    y = b['pts'][0][1]
    x0, x1 = sorted(p_[0] for p_ in b['pts'])
    vx = sorted({round(pl['pts'][0][0], 2) for pl in grey if abs(pl['pts'][0][0] - pl['pts'][1][0]) < .01
                 and x0 - .5 <= pl['pts'][0][0] <= x1 + .5 and abs(max(q[1] for q in pl['pts']) - y) < .5})
    vl = [pl for pl in grey if abs(pl['pts'][0][0] - pl['pts'][1][0]) < .01 and x0 - .5 <= pl['pts'][0][0] <= x1 + .5
          and abs(max(q[1] for q in pl['pts']) - y) < .5]
    top = min(min(q[1] for q in pl['pts']) for pl in vl)
    step = (x1 - x0) / (len(vx) - 1)
    rows = (y - top) / step
    d = [pl for pl in dashed if abs(min(q[0] for q in pl['pts']) - x0) < .5 and top - 1 <= pl['pts'][0][1] < y]
    dh = (y - d[0]['pts'][0][1]) / step if d else None
    labs = [w['text'] for w in p.words if w['text'] in '012' and abs(w['x1'] - x0) < 8 and top - 5 < w['cy'] < y + 5]
    se = [w['text'] for w in p.words if w['text'] in ('S', 'E') and y < w['top'] < y + 12 and x0 - 5 < w['cx'] < x1 + 5]
    dots = [c for c in p.circles if c['fill'] and (math.dist((c['cx'], c['cy']), (x0, y)) < .5 or math.dist((c['cx'], c['cy']), (x1, y)) < .5)]
    ok = len(vx) - 1 == 8 and abs(rows - 2) < .01 and dh is not None and abs(dh - 2) < .01 and sorted(labs) == ['0', '1', '2'] \
        and sorted(se) == ['E', 'S'] and len(dots) == 2
    if not ok:
        probs.append((y, len(vx) - 1, rows, dh, labs, se, len(dots)))
print(f'  {len(solid)} boards; unit {step / 72 * 2.54:.2f} cm')
check('P2: ten 8-step boards, square cells, dashed ceiling exactly at height 2, labels 0 1 2, S and E dots', len(solid) == 10 and not probs, probs)
ceil2 = [w for w in (''.join(t) for t in itertools.product('UD', repeat=8)) if C.is_dyck(w) and max(C.heights(w)) <= 2]
print(f'  ceiling-2 paths with four pairs: {len(ceil2)} {ceil2}')
check('P2: 8 paths for 10 boards', len(ceil2) == 8)
ceil2_5 = [w for w in (''.join(t) for t in itertools.product('UD', repeat=10)) if C.is_dyck(w) and max(C.heights(w)) <= 2]
check('P3: 16 ceiling-2 paths with five pairs', len(ceil2_5) == 16)

print()
print('== Problem 4 (page 4)')
p = pages[3]
paths = [pl for pl in p.polylines if len(pl['pts']) >= 7 and pl['lw'] > 1.1 and pl['scolor'] == (0, 0, 0)]
blue = [pl for pl in p.polylines if col(pl['scolor']) == BLUE]
grey = [pl for pl in p.polylines if col(pl['scolor']) == (0.85, 0.85, 0.85)]


def grid_info(pl):
    x0, y0 = pl['pts'][0]
    xs = sorted({round(g['pts'][0][0], 2) for g in grey if abs(g['pts'][0][0] - g['pts'][1][0]) < .01
                 and abs(max(q[1] for q in g['pts']) - y0) < .5 and x0 - .5 <= g['pts'][0][0] <= x0 + 400})
    # keep the run of equally spaced lines starting at x0
    run = [xs[0]]
    for x in xs[1:]:
        if abs((x - run[-1]) - (run[1] - run[0] if len(run) > 1 else x - run[-1])) < .05:
            run.append(x)
        else:
            break
    stepx = run[1] - run[0]
    vl = [g for g in grey if abs(g['pts'][0][0] - x0) < .5 and abs(g['pts'][0][0] - g['pts'][1][0]) < .01
          and abs(max(q[1] for q in g['pts']) - y0) < .5]
    top = min(min(q[1] for q in g['pts']) for g in vl)
    hl = sorted({round(g['pts'][0][1], 2) for g in grey if abs(g['pts'][0][1] - g['pts'][1][1]) < .01
                 and abs(min(q[0] for q in g['pts']) - x0) < .5 and top - .5 <= g['pts'][0][1] <= y0 + .5})
    stepy = hl[1] - hl[0]
    return len(run) - 1, len(hl) - 1, stepx, stepy


def nearest_text(pl, prefix):
    """Letters printed after the nearest word `prefix` (e.g. "Start:") on the same text line."""
    x0, y0 = pl['pts'][0]
    gtop = y0 - 4 * 17.0 if prefix == 'Start:' else y0 + 1  # starts are labelled above their 4-row grids
    best = None
    for w in p.words:
        if w['text'] != prefix or (prefix == 'Start:' and w['top'] > gtop):
            continue
        same = sorted([v for v in p.words if abs(v['top'] - w['top']) < 1 and v['x0'] > w['x0']], key=lambda v: v['x0'])
        letters = ''
        for v in same:
            if v['text'] in ('U', 'D'):
                letters += v['text']
            else:
                break
        d = math.dist((w['x0'], w['top']), (x0, y0))
        if best is None or d < best[0]:
            best = (d, letters, w['x0'], w['top'])
    return best


found = []
for pl in sorted(paths, key=lambda pl: (round(pl['pts'][0][1]), pl['pts'][0][0])):
    cols, rows, sx, sy = grid_info(pl)
    w, st = G.word_from_polyline(pl['pts'], sx)
    found.append((pl, w, cols, rows, sx, sy))
    print(f'  path at ({pl["pts"][0][0]:.0f},{pl["pts"][0][1]:.0f}): {w}, grid {cols} x {rows}, cell {sx:.2f} x {sy:.2f} pt')
check('page 4: every path on square cells and inside its grid',
      all(w and abs(sx - sy) < .05 and max(C.heights(w)) <= rows and len(w) == cols for _, w, cols, rows, sx, sy in found))
ex_in, ex_out = [f for f in found if len(f[1]) == 6]
check('example: input path UDUUDD, output path UUDUDD', ex_in[1] == 'UDUUDD' and ex_out[1] == 'UUDUDD', (ex_in[1], ex_out[1]))
t_in = nearest_text(ex_in[0], 'Input:')
t_out = nearest_text(ex_out[0], 'Output:')
check('example: "Input:" and "Output:" letters match the drawn paths', t_in[1] == ex_in[1] and t_out[1] == ex_out[1], (t_in[1], t_out[1]))
# blue marks: which steps do they cover?
for f, bl in [(ex_in, None), (ex_out, None)]:
    pass
marks = []
for b in blue:
    for f in (ex_in, ex_out):
        x0, y0 = f[0]['pts'][0]
        sx = f[4]
        ks = [round((q[0] - x0) / sx, 1) for q in b['pts']]
        if all(-0.01 <= k <= len(f[1]) + .01 for k in ks) and abs(b['pts'][0][1] - y0) < 3 * sx:
            on = all(math.dist(q, f[0]['pts'][int(round(k))]) < .5 for q, k in zip(b['pts'], ks))
            marks.append((f[1], ks, on))
print('  blue marks (path, vertex indices, on the path):', marks)
check('example: blue marks cover steps 2-3 of each path (the swapped DU / UD)',
      sorted((m[0], tuple(m[1])) for m in marks) == [('UDUUDD', (1.0, 2.0, 3.0)), ('UUDUDD', (1.0, 2.0, 3.0))] and all(m[2] for m in marks))
check('example: steps 2-3 read DU in the input and UD in the output', ex_in[1][1:3] == 'DU' and ex_out[1][1:3] == 'UD'
      and ex_in[1][:1] + 'UD' + ex_in[1][3:] == ex_out[1])
cards = sorted([w for w in p.words if w['text'] in ('U', 'D') and w['size'] > 13], key=lambda w: w['x0'])
check('example: the cards read D U -> U D', ''.join(w['text'] for w in cards) == 'DUUD', ''.join(w['text'] for w in cards))
big = [f for f in found if len(f[1]) == 8]
tgt = [f for f in big if nearest_text(f[0], 'Target:') and f[1] == 'UUUUDDDD']
starts = [f for f in big if f[1] != 'UUUUDDDD']
target_text = nearest_text(big[0][0], 'Target:')
check('P4: target text and drawing both UUUUDDDD', target_text[1] == 'UUUUDDDD' and len(tgt) == 1)


def neighbours(w):
    out = []
    for i in range(len(w) - 1):
        if w[i] != w[i + 1]:
            v = w[:i] + w[i + 1] + w[i] + w[i + 2:]
            if C.is_dyck(v):
                out.append(v)
    return out


dist = {'UUUUDDDD': 0}
q = ['UUUUDDDD']
for x in q:
    for y in neighbours(x):
        if y not in dist:
            dist[y] = dist[x] + 1
            q.append(y)
for f in starts:
    t = nearest_text(f[0], 'Start:')
    print(f'  start drawn {f[1]}, label "{t[1]}", distance to target {dist.get(f[1])}')
    check(f'P4 start {f[1]}: label matches drawing', t[1] == f[1])
check('P4 distances 6, 4, 1 in page order', [dist[f[1]] for f in starts] == [6, 4, 1])
areas = [pl for pl in p.polylines if pl['closed'] and col(pl['scolor']) == (0.8, 0.8, 0.8)]
print('  route areas (height in cm):', sorted(round((max(q[1] for q in a['pts']) - min(q[1] for q in a['pts'])) / 72 * 2.54, 1) for a in areas))
print()
print('FAILED:', FAIL if FAIL else 'none')
