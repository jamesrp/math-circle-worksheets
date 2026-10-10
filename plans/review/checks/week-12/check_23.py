"""Week 12 Grades 2-3: read every dot row, arc, grid, path, step letter, box and code from the PDF
and solve each problem from the extracted data.  Run: python3 check_23.py > check_23.out"""
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G
import comb as C

FAIL = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))
    if not ok:
        FAIL.append(name)


def read_rows(page):
    """Rows of dots on a light horizontal line, with number labels and arcs."""
    lines = [pl for pl in page.polylines if len(pl['pts']) == 2 and not pl['closed']
             and abs(pl['pts'][0][1] - pl['pts'][1][1]) < 0.01 and pl['scolor'] == (0.775, 0.775, 0.775)]
    dots = [c for c in page.circles if c['fill'] and not c['stroke']]
    nums = [w for w in page.words if w['text'].isdigit() and w['top'] < 750]
    rows = []
    for pl in sorted(lines, key=lambda pl: (round(pl['pts'][0][1]), pl['pts'][0][0])):
        y = pl['pts'][0][1]
        x0, x1 = sorted((pl['pts'][0][0], pl['pts'][1][0]))
        mine = sorted([d for d in dots if abs(d['cy'] - y) < 0.3 and x0 - 0.5 <= d['cx'] <= x1 + 0.5], key=lambda d: d['cx'])
        xs = [d['cx'] for d in mine]
        sp = [b - a for a, b in zip(xs, xs[1:])]
        probs = []
        if sp and max(sp) - min(sp) > 0.05:
            probs.append(f'unequal spacing {min(sp):.2f}-{max(sp):.2f}')
        if mine and (abs(xs[0] - x0) > 0.5 or abs(xs[-1] - x1) > 0.5):
            probs.append('line does not run dot to dot')
        labels = []
        for d in mine:
            cand = [w for w in nums if w['top'] > d['cy'] and w['top'] - d['cy'] < 40 and abs(w['cx'] - d['cx']) < 4]
            cand.sort(key=lambda w: w['top'])
            labels.append(cand[0]['text'] if cand else None)
        if labels != [str(i) for i in range(1, len(mine) + 1)]:
            probs.append(f'labels {labels}')
        pairs = []
        for b in page.beziers:
            ends = []
            for p in (b['p0'], b['p3']):
                hit = [i for i, d in enumerate(mine, 1) if math.dist(p, (d['cx'], d['cy'])) < 0.6]
                ends.append(hit[0] if hit else None)
            if None in ends:
                continue
            if not (b['p1'][1] < y and b['p2'][1] < y):
                probs.append(f'arc {ends} not above the row')
            pairs.append(tuple(sorted(ends)))
        used = [p for e in pairs for p in e]
        if len(used) != len(set(used)):
            probs.append(f'a dot is used twice in {pairs}')
        rows.append(dict(y=y, x0=x0, x1=x1, n=len(mine), r=mine[0]['r'] if mine else 0, spacing=sp[0] if sp else 0,
                         pairs=sorted(pairs), probs=probs, xs=xs))
    return rows


def read_grids(page):
    """Grids: a black baseline, light grid lines, an optional thick path, a filled start dot and an open end dot."""
    bases = [pl for pl in page.polylines if len(pl['pts']) == 2 and pl['scolor'] == (0, 0, 0)
             and abs(pl['pts'][0][1] - pl['pts'][1][1]) < 0.01 and abs(pl['lw'] - 0.8) < 0.05]
    gl = [pl for pl in page.polylines if len(pl['pts']) == 2 and pl['scolor'] == (0.825, 0.825, 0.825)]
    paths = [pl for pl in page.polylines if len(pl['pts']) > 2 and pl['scolor'] == (0, 0, 0) and pl['lw'] > 1]
    out = []
    for b in sorted(bases, key=lambda b: (round(b['pts'][0][1]), b['pts'][0][0])):
        y = b['pts'][0][1]
        x0, x1 = sorted((b['pts'][0][0], b['pts'][1][0]))
        vert = sorted({round(pl['pts'][0][0], 2) for pl in gl if abs(pl['pts'][0][0] - pl['pts'][1][0]) < 0.01
                       and x0 - 0.5 <= pl['pts'][0][0] <= x1 + 0.5 and abs(max(pl['pts'][0][1], pl['pts'][1][1]) - y) < 0.5})
        vlines = [pl for pl in gl if abs(pl['pts'][0][0] - pl['pts'][1][0]) < 0.01
                  and x0 - 0.5 <= pl['pts'][0][0] <= x1 + 0.5 and abs(max(pl['pts'][0][1], pl['pts'][1][1]) - y) < 0.5]
        top = min(min(pl['pts'][0][1], pl['pts'][1][1]) for pl in vlines)
        horiz = sorted({round(pl['pts'][0][1], 2) for pl in gl if abs(pl['pts'][0][1] - pl['pts'][1][1]) < 0.01
                        and top - 0.5 <= pl['pts'][0][1] <= y + 0.5 and abs(min(pl['pts'][0][0], pl['pts'][1][0]) - x0) < 0.5})
        cols = len(vert) - 1
        rowsn = len(horiz) - 1
        stepx = (x1 - x0) / cols
        stepy = (y - top) / rowsn
        probs = []
        if abs(stepx - stepy) > 0.05:
            probs.append(f'cells not square {stepx:.2f} x {stepy:.2f}')
        start = [c for c in page.circles if math.dist((c['cx'], c['cy']), (x0, y)) < 0.5]
        end = [c for c in page.circles if math.dist((c['cx'], c['cy']), (x1, y)) < 0.5]
        if not (start and start[0]['fill'] and start[0]['fcolor'] == (0, 0, 0)):
            probs.append('no filled start dot')
        if not (end and end[0]['stroke'] and end[0]['fcolor'] == (1, 1, 1)):
            probs.append('no open end dot')
        word = None
        for pl in paths:
            if math.dist(pl['pts'][0], (x0, y)) < 0.5:
                word, st = G.word_from_polyline(pl['pts'], stepx)
                if word is None:
                    probs.append(st)
                elif max(G.heights(word)) > rowsn:
                    probs.append('path leaves the grid')
                if math.dist(pl['pts'][-1], (x1, y)) > 0.5:
                    probs.append('path does not end at the end dot')
        out.append(dict(x0=x0, x1=x1, y=y, cols=cols, rows=rowsn, step=stepx, word=word, probs=probs))
    return out


def boxes(page):
    rects = [pl for pl in page.polylines if pl['closed'] and len(pl['pts']) == 4]
    groups = {}
    for r in rects:
        ys = tuple(sorted(round(p[1], 1) for p in r['pts']))
        groups.setdefault(ys[0], []).append(r)
    return {k: len(v) for k, v in sorted(groups.items())}


pages = G.load('week-12-grades-2-3.pdf')
allrows = {}
allgrids = {}
for pno, page in enumerate(pages, 1):
    rows = read_rows(page)
    grids = read_grids(page)
    allrows[pno] = rows
    allgrids[pno] = grids
    print(f'--- page {pno}: {len(rows)} dot rows, {len(grids)} grids, boxes {boxes(page)}')
    for r in rows:
        print(f'  row y={r["y"]:.1f}: {r["n"]} dots (r={r["r"] / G.MM:.2f} mm, spacing {r["spacing"] / G.MM:.1f} mm), arcs {C.fmt(r["pairs"]) if r["pairs"] else "-"}'
              + (f' PROBLEMS {r["probs"]}' if r['probs'] else ''))
    for g in grids:
        print(f'  grid y={g["y"]:.1f}: {g["cols"]} x {g["rows"]} cells of {g["step"] / G.MM:.2f} mm, path {g["word"]}'
              + (f' PROBLEMS {g["probs"]}' if g['probs'] else ''))
    check(f'page {pno}: rows evenly spaced, labelled 1..n, arcs above the row; grids square with start/end dots',
          all(not r['probs'] for r in rows) and all(not g['probs'] for g in grids))

print()
print('== Rules example and Problem 1 (page 1)')
r1 = allrows[1]
ex = [r for r in r1 if r['n'] == 10]
check('page 1 example: one ten-dot row 14|23|5-10|67|89, noncrossing', len(ex) == 1 and C.fmt(ex[0]['pairs']) == '14|23|5-10|67|89'
      and C.noncrossing(ex[0]['pairs']))
six = [r for r in r1 if r['n'] == 6]
check('P1: 1 large + 6 small six-dot rows, all empty; 5 pairings exist',
      len(six) == 7 and all(not r['pairs'] for r in six) and len(C.nc_matchings(6)) == 5, [round(r['spacing'] / G.MM, 1) for r in six])

print()
print('== Code example and Problem 2 (page 2)')
p2 = pages[1]
r2 = sorted(allrows[2], key=lambda r: r['y'])
exrow = r2[0]
w_ex = C.code(exrow['pairs'], exrow['n'])
check('example row pairing and its code', C.fmt(exrow['pairs']) == '12|36|45|78' and w_ex == 'UDUUDDUD', (C.fmt(exrow['pairs']), w_ex))
# letters printed under the example dots
under = []
for x in exrow['xs']:
    cand = [w for w in p2.words if w['text'] in 'UD' and len(w['text']) == 1 and w['top'] > exrow['y'] + 8 and w['top'] < exrow['y'] + 40 and abs(w['cx'] - x) < 4]
    under.append(cand[0]['text'] if cand else '?')
check('example: letters printed under the dots equal the code', ''.join(under) == w_ex, ''.join(under))
g2 = sorted(allgrids[2], key=lambda g: g['y'])
exg = [g for g in g2 if g['word']]
check('example grid path equals the code', len(exg) == 1 and exg[0]['word'] == w_ex, [g['word'] for g in exg])
# step letters on the example grid: each letter should sit nearest its own step and agree with it
g = exg[0]
hs = G.heights(g['word'])
mids = [((g['x0'] + (k + 0.5) * g['step']), g['y'] - (hs[k] + hs[k + 1]) / 2 * g['step']) for k in range(len(g['word']))]
letters = [w for w in p2.words if w['text'] in ('U', 'D') and g['x0'] - 5 < w['cx'] < g['x1'] + 5 and g['y'] - (g['rows'] + 1) * g['step'] < w['cy'] < g['y']]
bad = []
for w in letters:
    k = min(range(len(mids)), key=lambda k: math.dist((w['cx'], w['cy']), mids[k]))
    above = w['cy'] < mids[k][1]
    if g['word'][k] != w['text'] or not above:
        bad.append((w['text'], k + 1))
check('example grid: 8 step letters, each above its own step and matching it', len(letters) == 8 and not bad, (len(letters), bad))
pairing_rows = r2[1:]
bx = boxes(p2)
for r, gg in zip(pairing_rows, [x for x in g2 if not x['word']]):
    w = C.code(r['pairs'], r['n'])
    h = G.heights(w)
    print(f'  P2 {C.fmt(r["pairs"])} -> {w}, heights {h}, grid {gg["cols"]}x{gg["rows"]}')
    check(f'P2 {C.fmt(r["pairs"])}: noncrossing, path fits its {gg["cols"]}x{gg["rows"]} grid, never below 0, ends at 0',
          C.noncrossing(r['pairs']) and len(w) == gg['cols'] and max(h) <= gg['rows'] and min(h) == 0 and h[-1] == 0)
check('P2: three rows of six letter boxes', sorted(bx.values()) == [6, 6, 6], bx)
check('P2 guide codes UUUDDD, UUDDUD, UDUDUD (top to bottom)',
      [C.code(r['pairs'], r['n']) for r in pairing_rows] == ['UUUDDD', 'UUDDUD', 'UDUDUD'])

print()
print('== Problem 3 (page 3)')
g3 = sorted(allgrids[3], key=lambda g: g['y'])
r3 = sorted(allrows[3], key=lambda r: r['y'])
for g, r in zip(g3, r3):
    ms = C.pairings_with_code(g['word'])
    print(f'  P3 path {g["word"]} ({g["cols"]}x{g["rows"]} grid) -> row of {r["n"]} dots; noncrossing pairings {[C.fmt(m) for m in ms]}')
    check(f'P3 {g["word"]}: Dyck, row has {len(g["word"])} dots, exactly one noncrossing pairing',
          C.is_dyck(g['word']) and r['n'] == len(g['word']) and len(ms) == 1 and abs(g['y'] - r['y']) < 1)
check('P3 guide answers 16|23|45, 12|36|45, 14|23|58|67, 18|27|34|56',
      [C.fmt(C.pairings_with_code(g['word'])[0]) for g in g3] == ['16|23|45', '12|36|45', '14|23|58|67', '18|27|34|56'])

print()
print('== Problem 4 (page 4)')
g4 = allgrids[4]
check('P4: six empty 6x3 grids for the five paths', len(g4) == 6 and all(g['cols'] == 6 and g['rows'] == 3 and not g['word'] for g in g4)
      and len([w for w in __import__('itertools').product('UD', repeat=6) if C.is_dyck(''.join(w))]) == 5)

print()
print('== Problem 5 (page 5)')
codes5 = [w['text'] for w in sorted(pages[4].words, key=lambda w: w['top']) if set(w['text']) <= set('UD') and len(w['text']) == 8]
check('P5: the four printed codes', codes5 == ['UUUDDUDD', 'UDDUUDUD', 'UUDUDUDD', 'UUUUDDUD'], codes5)
for w in codes5:
    ms = C.pairings_with_code(w)
    h = G.heights(w)
    print(f'  P5 {w}: heights {h}, valid={C.is_dyck(w)}, pairing {[C.fmt(m) for m in ms]}')
check('P5: two valid (18|25|34|67, 18|23|45|67), two invalid',
      [len(C.pairings_with_code(w)) for w in codes5] == [1, 0, 1, 0]
      and C.fmt(C.pairings_with_code(codes5[0])[0]) == '18|25|34|67' and C.fmt(C.pairings_with_code(codes5[2])[0]) == '18|23|45|67')
check('P5: four eight-dot rows', [r['n'] for r in allrows[5]] == [8, 8, 8, 8])

print()
print('== Problem 6 (page 6)')
check('P6: sixteen empty eight-dot rows for 14 pairings', len(allrows[6]) == 16 and all(r['n'] == 8 and not r['pairs'] for r in allrows[6])
      and len(C.nc_matchings(8)) == 14)
print()
print('FAILED:', FAIL if FAIL else 'none')
