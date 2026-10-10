#!/usr/bin/env python3
"""Week 68 diagram check: reads the delivered student PDF's vector drawings and
checks that each printed map is the graph the text describes."""
from pathlib import Path
from itertools import combinations
import math
import pymupdf

REPO = Path(__file__).resolve().parents[4]
PDF = REPO / 'lowell-math-circle-year-2/week-68/week-68-students.pdf'
doc = pymupdf.open(PDF)
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

def prims(page):
    dots, segs, heads = [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d['items']]
        if d['type'] == 'f' and kinds == ['c'] * 4:
            r = d['rect']; dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, (r.x1 - r.x0) / 2))
        elif d['type'] == 's' and set(kinds) == {'l'}:
            for it in d['items']:
                segs.append((tuple(it[1]), tuple(it[2]), d['width'], d['color']))
        elif d['type'] == 'fs' and kinds == ['c', 'l', 'c']:
            p = d['items'][0][1]; q = d['items'][1][1]; q2 = d['items'][1][2]
            base = ((q.x + q2.x) / 2, (q.y + q2.y) / 2)
            heads.append(((p.x, p.y), base))  # tip, base midpoint
    return dots, segs, heads

close = lambda a, b, tol=0.6: abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol
PT_PER_MM = 72 / 25.4
say('page size (pt):', tuple(round(v, 1) for v in doc[0].rect), 'pages', doc.page_count)

# ---- Page 1: worked example + four lines ----
dots, segs, heads = prims(doc[0])
ex = [d for d in dots if d[1] < 200]
lines = [s for s in segs if s[2] > 0.9 and abs(s[0][1] - s[1][1]) < .1 and s[1][0] - s[0][0] > 300]
say('P1/P2 lines found:', len(lines))
for s in lines:
    y = s[0][1]
    ds = sorted(d[0] for d in dots if abs(d[1] - y) < 1)
    gaps = {round(b - a, 2) for a, b in zip(ds, ds[1:])}
    hs = [h for h in heads if abs(h[0][1] - y) < 1]
    outward = sorted('L' if h[0][0] < h[1][0] else 'R' for h in hs)
    say(f'  line y={y:.1f}: dots {len(ds)}, spacing {sorted(gaps)} pt ({min(gaps)/PT_PER_MM:.1f} mm), arrowheads pointing {outward}, shaft {s[0][0]:.1f}-{s[1][0]:.1f}, dots {ds[0]:.1f}-{ds[-1]:.1f}')
# worked example frames
frames = {}
for d in ex:
    k = 0 if d[0] < 250 else (1 if d[0] < 360 else 2)
    frames.setdefault(k, []).append((round(d[0], 1), round(d[1], 1)))
exsegs = [s for s in segs if s[0][1] < 200 and s[2] > 0.9]
for k in range(3):
    E = [s for s in exsegs if (0 if s[0][0] < 250 else (1 if s[0][0] < 360 else 2)) == k]
    say(f'  example frame {k}: dots {len(frames[k])}, road segments {len(E)}')
box = [d for d in doc[0].get_drawings() if d['type'] == 'fs' and [i[0] for i in d['items']] == ['re']][0]['rect']
covered = [d for d in frames[1] if box.x0 < d[0] < box.x1 and box.y0 < d[1] < box.y1]
say('  X counter covers dot', covered, '(upper-right = min y, max x of frame 1:', (max(d[0] for d in frames[1]), min(d[1] for d in frames[1])), ')')
def rel(pts, ox, oy): return sorted((round(x - ox, 1), round(y - oy, 1)) for x, y in pts)
o = [(min(x for x, y in frames[k]), max(y for x, y in frames[k])) for k in range(3)]  # lower-left dot of each frame
segs_k = [[s for s in exsegs if (0 if s[0][0] < 250 else (1 if s[0][0] < 360 else 2)) == k] for k in range(3)]
roads = [sorted(tuple(sorted([(round(a[0]-o[k][0],1), round(a[1]-o[k][1],1)), (round(b[0]-o[k][0],1), round(b[1]-o[k][1],1))])) for a, b, *_ in segs_k[k]) for k in range(3)]
cov = (round(covered[0][0]-o[1][0],1), round(covered[0][1]-o[1][1],1))
expect_dots = [d for d in rel(frames[0], *o[0]) if d != cov]
expect_roads = [r for r in roads[0] if cov not in r]
say('  covered dot (relative to lower-left):', cov, '; frame 2 dots == frame 0 minus covered:', rel(frames[2], *o[2]) == expect_dots, '; frame 2 roads == frame 0 roads not touching covered dot:', roads[2] == expect_roads)

# ---- Page 2: ladders ----
dots, segs, heads = prims(doc[1])
rails = [s for s in segs if s[2] > 0.9 and abs(s[0][1] - s[1][1]) < .1 and abs(s[1][0] - s[0][0]) > 300]
rungs = [s for s in segs if s[2] > 0.9 and abs(s[0][0] - s[1][0]) < .1]
ys = sorted({round(s[0][1], 1) for s in rails})
say('P3/P4 ladder rails at y =', ys, '; rung count', len(rungs), '; rung widths', sorted({round(s[2], 2) for s in rungs}))
for top, bot in zip(ys[0::2], ys[1::2]):
    R = [s for s in rungs if min(s[0][1], s[1][1]) > top - 1 and max(s[0][1], s[1][1]) < bot + 1]
    xs = sorted(round(s[0][0], 1) for s in R)
    dtop = sorted(round(d[0], 1) for d in dots if abs(d[1] - top) < 1)
    dbot = sorted(round(d[0], 1) for d in dots if abs(d[1] - bot) < 1)
    full = all(abs(min(s[0][1], s[1][1]) - top) < .2 and abs(max(s[0][1], s[1][1]) - bot) < .2 for s in R)
    hs = [h for h in heads if top - 1 < h[0][1] < bot + 1]
    say(f'  ladder {top}-{bot}: {len(R)} rungs at columns == dot columns: {xs == dtop == dbot}; each rung spans both rails: {full}; arrowheads {len(hs)}; column spacing {round(xs[1]-xs[0],1)} pt, rail gap {round(bot-top,1)} pt')

# ---- Page 3: grids ----
dots, segs, heads = prims(doc[2])
words = doc[2].get_text('words')
for side, (lo, hi) in (('left', (0, 306)), ('right', (306, 612))):
    D = [d for d in dots if lo < d[0] < hi and 140 < d[1] < 360]
    xs = sorted({round(d[0], 1) for d in D}); ys = sorted({round(d[1], 1) for d in D})
    hs = [h for h in heads if lo < h[0][0] < hi and 140 < h[0][1] < 360]
    sx = {round(b - a, 2) for a, b in zip(xs, xs[1:])}; sy = {round(b - a, 2) for a, b in zip(ys, ys[1:])}
    say(f'P5 {side} grid: {len(D)} dots on {len(xs)}x{len(ys)} lattice, x spacing {sorted(sx)}, y spacing {sorted(sy)} pt (= {min(sx)/PT_PER_MM:.2f} mm); boundary arrowheads {len(hs)}')
    if side == 'right':
        cx, cy = xs[3] if len(xs) == 7 else None, ys[3] if len(ys) == 7 else None
        # the centre column dots are covered by white boxes: recover the lattice from the left grid's spacing
        step = 28.3465
        x0 = min(d[0] for d in D); y0 = min(d[1] for d in D)
        cx, cy = x0 + 3 * step, y0 + 3 * step
        lab = {}
        for w in words:
            if w[4] in ('X', 'P', 'Q') and lo < w[0] < hi and 140 < w[1] < 360:
                mx, my = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
                lab.setdefault(w[4], []).append((round((mx - cx) / step, 2), round(-(my - cy) / step, 2)))
        say('  labels in lattice coordinates (centre 0,0, y up):', {k: sorted(v) for k, v in lab.items()})
        missing = [(i, j) for i in range(-3, 4) for j in range(-3, 4) if not any(abs(d[0] - (cx + i * step)) < .5 and abs(d[1] - (cy - j * step)) < .5 for d in D)]
        say('  lattice points with no printed dot:', missing)

# ---- Page 4: tree ----
dots, segs, heads = prims(doc[3])
T = [s for s in segs if abs(s[2] - 0.9) < 0.05]
center = max(dots, key=lambda d: d[2])
say('P7 tree: dots', len(dots), '; segments', len(T), '; arrowheads', len(heads), '; largest dot (centre) radius', round(center[2], 2))
def dot_at(p):
    for i, d in enumerate(dots):
        if math.hypot(d[0] - p[0], d[1] - p[1]) < 1.0: return i
    return None
adj = {i: set() for i in range(len(dots))}
arrows = {i: 0 for i in range(len(dots))}
for a, b, *_ in T:
    ia, ib = dot_at(a), dot_at(b)
    if ia is not None and ib is not None: adj[ia].add(ib); adj[ib].add(ia)
    elif ia is not None: arrows[ia] += 1
    elif ib is not None: arrows[ib] += 1
ci = dots.index(center)
deg = sorted(len(adj[i]) + arrows[i] for i in adj)
nedges = sum(len(v) for v in adj.values()) // 2
level = {ci: 0}; frontier = [ci]
while frontier:
    nxt = []
    for u in frontier:
        for w in adj[u]:
            if w not in level: level[w] = level[u] + 1; nxt.append(w)
    frontier = nxt
from collections import Counter
say('  drawn dot-to-dot roads', nedges, '; roads leaving to arrows', sum(arrows.values()), '; degrees (roads incl. arrows):', Counter(deg))
say('  connected:', len(level) == len(dots), '; acyclic (edges = dots-1):', nedges == len(dots) - 1, '; dots per distance from centre:', sorted(Counter(level.values()).items()))
say('  arrows only on outermost dots:', all(level[i] == 3 for i in arrows if arrows[i]))
radii = {}
for i, l in level.items():
    radii.setdefault(l, []).append(math.hypot(dots[i][0] - center[0], dots[i][1] - center[1]))
say('  radius by level (pt):', {l: (round(min(r), 2), round(max(r), 2)) for l, r in sorted(radii.items())})
def cross(p, q, r, s):
    def o(a, b, c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if min(math.dist(p, r), math.dist(p, s), math.dist(q, r), math.dist(q, s)) < 1.5: return False
    return (o(p, q, r) * o(p, q, s) < 0) and (o(r, s, p) * o(r, s, q) < 0)
X = [(i, j) for i, j in combinations(range(len(T)), 2) if cross(T[i][0], T[i][1], T[j][0], T[j][1])]
say('  crossing road segments:', len(X))
md = min(math.dist(a[:2], b[:2]) for a, b in combinations(dots, 2))
say(f'  closest pair of tree dots: {md:.1f} pt = {md/PT_PER_MM:.1f} mm')
(Path(__file__).with_suffix('.out')).write_text('\n'.join(out) + '\n')
