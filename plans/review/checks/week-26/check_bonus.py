"""Independent check of the Week 26 bonus companion (week-26-bonus.pdf) and its
adult guide (week-26-bonus-facilitator.pdf).

Reads the corner examples, circles and the P3 shapes from the student PDF, then
checks P1-P2 by enumerating every two-colouring of the 4x4 square, P3 by vertex
classification, and P4-P6 by counting exposed faces of actual unit cubes.
Output: check_bonus.out
"""
import os
import random
import subprocess
import sys
from itertools import permutations

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, WEEK, Log, PT_MM, perimeter, shared, connected, holes,  # noqa: E402
                    corner_counts, show, norm, redelmeier, load_extracted, N4)

L = Log()
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract.py')], check=True)
X = load_extracted(os.path.join(HERE, 'extracted.json'))
doc = pymupdf.open(os.path.join(WEEK, 'week-26-bonus.pdf'))

# ------------------------------------------------------------------ P1-P2
L.out('=== P1-P2: two rooms in the 4x4 square')
cells = [(x, y) for y in range(4) for x in range(4)]
best = None
optima = []
ident = True
for m in range(1 << 16):
    R = [cells[i] for i in range(16) if m >> i & 1]
    B = [cells[i] for i in range(16) if not m >> i & 1]
    Rs = set(R)
    fence = sum(1 for (x, y) in R for dx, dy in N4 if (x + dx, y + dy) in set(B))
    if R and B and perimeter(R) + perimeter(B) != 16 + 2 * fence:
        ident = False
    if len(R) != 8 or not connected(R) or not connected(B):
        continue
    if best is None or fence < best:
        best, optima = fence, []
    if fence == best:
        optima.append(show(R))
L.ok(ident, 'P2: P_R + P_B = 16 + 2L for every split of the square (any sizes, connected or not)')
L.ok(best == 4 and len(optima) == 4, f'P1: least shared fence {best}; optimal labelled colourings {len(optima)}: {optima}')
unconstrained = min(sum(1 for (x, y) in [cells[i] for i in range(16) if m >> i & 1]
                        for dx, dy in N4 if 0 <= x + dx < 4 and 0 <= y + dy < 4
                        and not m >> ((y + dy) * 4 + x + dx) & 1)
                    for m in range(1 << 16) if bin(m).count('1') == 8)
L.ok(unconstrained == 4, 'P1: even without the connectedness rule, a balanced split needs a fence of 4')
L.ok(perimeter([(x, y) for x in range(4) for y in range(2)]) == 12, 'P1: each half (2x4) has boundary 12')

# ------------------------------------------------------------------ P3
L.out('\n=== P3: corners and holes')
p2 = X['bonus'][1]
big = [s for s in p2['shapes'] if abs(s['cell_w_mm'] - 8.0) < 0.1]
small = [s for s in p2['shapes'] if abs(s['cell_w_mm'] - 6.0) < 0.1]
labels = []
for b in doc[1].get_text('dict')['blocks']:
    for ln in b.get('lines', []):
        t = ''.join(s['text'] for s in ln['spans']).strip()
        if t in ('1', '2', '3', '4') and ln['bbox'][1] * PT_MM < 170:
            labels.append((t, ln['bbox'][0] * PT_MM, ln['bbox'][1] * PT_MM))
numbered = {}
for s in big:
    w = max(x for x, _ in s['cells']) + 1
    h = max(y for _, y in s['cells']) + 1
    bottom = s['y_mm'] + h * 8
    cand = [lb for lb in labels if 0 < lb[2] - bottom < 12 and abs(lb[1] - s['x_mm']) < 8]
    assert len(cand) == 1, (show(s['cells']), cand)
    numbered[cand[0][0]] = s['cells']
want = {'1': (4, 0, 0), '2': (5, 1, 0), '3': (4, 4, 1), '4': (4, 8, 2)}
for k in sorted(numbered):
    c = numbered[k]
    C, R, pinch = corner_counts(c)
    H = holes(c)
    L.ok((C, R, H) == want[k] and pinch == 0 and C - R == 4 * (1 - H),
         f'shape {k} {show(c)} ({len(c)} tiles): C={C}, R={R}, holes={H}, pinches={pinch}')
L.ok(len(numbered['4']) == 13, 'the two-hole shape needs thirteen tiles')

# corner examples: the circles' vertices and the crossed pattern
circles = []
for d in doc[1].get_drawings():
    if any(it[0] == 'c' for it in d['items']):
        r = d['rect']
        circles.append(((r.x0 + r.x1) / 2 * PT_MM, (r.y0 + r.y1) / 2 * PT_MM))
for s, name, k in zip(sorted(small, key=lambda s: s['x_mm']), ('outward', 'inward', 'crossed'), (1, 3, 2)):
    tiles = [(s['x_mm'] + x * 6, s['y_mm'] + y * 6) for x, y in s['cells']]
    if name == 'crossed':
        L.ok(len(s['cells']) == 2 and sorted(norm(s['cells'])) in ([(0, 1), (1, 0)], [(0, 0), (1, 1)]),
             f'crossed-out example is two diagonal tiles: {show(s["cells"])}')
        continue
    cx, cy = min(circles, key=lambda c: abs(c[0] - s['x_mm'] - 6) + abs(c[1] - s['y_mm'] - 6))
    around = sum(1 for tx, ty in tiles if tx - 0.5 <= cx <= tx + 6.5 and ty - 0.5 <= cy <= ty + 6.5)
    L.ok(around == k, f'{name} example: circled vertex touches {around} tile(s) ({show(s["cells"])})')

ok_cr = True
pinch_fail = []
count = 0


def cb(p):
    global ok_cr, count
    C, R, pinch = corner_counts(p)
    if pinch == 0:
        count += 1
        if C - R != 4 * (1 - holes(p)) or holes(p) != holes(p, eight=True):
            ok_cr = False
    elif len(pinch_fail) < 3 and C - R != 4 * (1 - holes(p)):
        pinch_fail.append((show(p), C, R, pinch, holes(p), holes(p, eight=True)))


redelmeier(10, cb)
L.ok(ok_cr, f'C - R = 4(1 - H) on all {count} pinch-free fixed polyominoes with <= 10 tiles')
L.out('  with a pinch the rule can fail, e.g. (shape, C, R, pinches, H closed, H leaky):', pinch_fail[:2])

# ------------------------------------------------------------------ P4-P6
L.out('\n=== P4-P6: exposed cube faces')


def exposed(cubes):
    S = set(cubes)
    nb = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return sum(1 for (x, y, z) in S for dx, dy, dz in nb if (x + dx, y + dy, z + dz) not in S)


def building(heights):
    return [(x, y, z) for (x, y), h in heights.items() for z in range(h)]


row8 = building({(x, 0): 1 for x in range(8)})
two4 = building({(x, y): 1 for x in range(4) for y in range(2)})
cube2 = building({(x, y): 2 for x in range(2) for y in range(2)})
vals = [exposed(row8), exposed(two4), exposed(cube2)]
L.ok(vals == [34, 28, 24] and len(row8) == len(two4) == len(cube2) == 8,
     f'P4: row of eight {vals[0]}, 2x4 one layer {vals[1]}, 2x2 two layers {vals[2]} (all 8 cubes)')
L.ok(len(building({(0, 0): 2, (1, 0): 2})) == 4, 'opening example: two squares, two layers = 4 cubes')

ok5 = True
tested = 0


def cb5(p):
    global ok5, tested
    for k in (1, 2, 3):
        S = exposed(building({c: k for c in p}))
        tested += 1
        if S != 2 * len(p) + k * perimeter(p):
            ok5 = False


redelmeier(8, cb5)
ring = [(x, y) for x in range(3) for y in range(3) if (x, y) != (1, 1)]
two_hole = [(x, y) for x in range(5) for y in range(3) if (x, y) not in ((1, 1), (3, 1))]
for fp in (ring, two_hole):
    for k in (1, 2, 3, 4):
        tested += 1
        if exposed(building({c: k for c in fp})) != 2 * len(fp) + k * perimeter(fp):
            ok5 = False
L.ok(ok5, f'P5: S = 2m + kP for {tested} equal-height buildings (all footprints <= 8 tiles, '
          'and the ring and two-hole footprints), hole walls included')

res = {}
for perm in permutations((1, 2, 3, 4)):
    hts = dict(zip([(0, 0), (1, 0), (0, 1), (1, 1)], perm))
    res[perm] = exposed(building(hts))
from collections import Counter  # noqa: E402
cnt = Counter(res.values())
L.ok(min(res.values()) == 34 and max(res.values()) == 36 and cnt == Counter({34: 16, 36: 8}),
     f'P6: 24 arrangements give {dict(cnt)}: fewest 34, most 36')
L.ok(res[(1, 2, 3, 4)] == 34 and res[(1, 3, 4, 2)] == 36,
     'guide examples: 1 2 / 3 4 gives 34; 1 3 / 4 2 gives 36')
for cyc, v in (((1, 2, 3, 4), 6), ((1, 2, 4, 3), 6), ((1, 3, 2, 4), 8)):
    var = sum(abs(cyc[i] - cyc[(i + 1) % 4]) for i in range(4))
    L.ok(var == v and 28 + var in (34, 36), f'cycle {cyc}: variation {var}, S = {28 + var}')

random.seed(26)
ok_t = True
pool = []
redelmeier(7, lambda p: pool.append(list(p)) if len(p) == 7 else None)
for _ in range(400):
    fp = random.choice(pool)
    h = {c: random.randint(1, 5) for c in fp}
    S = set(fp)
    ext = sum(h[c] for c in fp for dx, dy in N4 if (c[0] + dx, c[1] + dy) not in S)
    diff = sum(abs(h[(x, y)] - h[(x + 1, y)]) for (x, y) in fp if (x + 1, y) in S) + \
        sum(abs(h[(x, y)] - h[(x, y + 1)]) for (x, y) in fp if (x, y + 1) in S)
    if exposed(building(h)) != 2 * len(fp) + ext + diff:
        ok_t = False
L.ok(ok_t, 'guide terrain rule S = 2m + exterior-edge heights + neighbour height differences (400 random terrains)')


# ------------------------------------------------------------- drawn grids
L.out('\n=== drawn footprints and working grids')


def line_grids(page):
    segs = []
    for d in page.get_drawings():
        if d['type'] != 's':
            continue
        for it in d['items']:
            if it[0] == 'l':
                p, q = it[1], it[2]
                if abs(p.x - q.x) < 0.01 or abs(p.y - q.y) < 0.01:
                    segs.append(pymupdf.Rect(min(p.x, q.x), min(p.y, q.y), max(p.x, q.x), max(p.y, q.y)))
    # group touching segments
    parent = list(range(len(segs)))

    def f(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            a, b = segs[i], segs[j]
            if a.x0 - 0.3 <= b.x1 and b.x0 - 0.3 <= a.x1 and a.y0 - 0.3 <= b.y1 and b.y0 - 0.3 <= a.y1:
                parent[f(i)] = f(j)
    groups = {}
    for i in range(len(segs)):
        groups.setdefault(f(i), []).append(segs[i])
    out = []
    for g in groups.values():
        xs = sorted({round(r.x0, 1) for r in g if r.width < 0.01})
        ys = sorted({round(r.y0, 1) for r in g if r.height < 0.01})
        if len(xs) >= 2 and len(ys) >= 2:
            out.append((len(xs) - 1, len(ys) - 1, round((xs[1] - xs[0]) * PT_MM, 2),
                        round((ys[1] - ys[0]) * PT_MM, 2), round(min(r.y0 for r in g) * PT_MM)))
    return sorted(out, key=lambda t: (t[4], t[0]))


g1 = [g for g in line_grids(doc[0]) if g[2] > 15 and g[3] > 15]
L.ok(len(g1) == 2 and all(g[:4] == (4, 4, 20.0, 20.0) for g in g1), f'P1: two 4x4 working grids of square 20 mm cells: {g1}')
g3 = line_grids(doc[2])
L.out('  page 3 line grids (cols, rows, cell w, cell h, top mm):', g3)
fps = sorted(g[:2] for g in g3 if 7 < g[2] < 8 and abs(g[2] - g[3]) < 0.1)
L.ok(fps == [(2, 2), (4, 2), (8, 1)], f'P4: drawn footprints 8x1, 4x2 and 2x2 with square cells: {fps}')
g4 = [g for g in line_grids(doc[3]) if g[0] == 2 and g[1] == 2]
L.ok(len(g4) == 6 and all(abs(g[2] - g[3]) < 0.05 for g in g4), 'P6: six 2x2 recording grids with square cells')

L.save(os.path.join(HERE, 'check_bonus.out'))
