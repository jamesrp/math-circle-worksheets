"""Week 12 Grades 4-5: read every tree, walk arrow, grid path, box, root dot and code from the PDF
and solve each problem from the extracted data.  Run: python3 check_45.py > check_45.out"""
import sys
import os
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfgeo as G
import comb as C

FAIL = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + str(detail)) if detail != '' else ''))
    if not ok:
        FAIL.append(name)


def read_trees(page, edge_lw=(0.85, 0.95), node_r=(4.0, 5.0)):
    nodes = [c for c in page.circles if node_r[0] < c['r'] < node_r[1] and c['fill']]
    edges = [pl for pl in page.polylines if len(pl['pts']) == 2 and not pl['closed'] and edge_lw[0] < pl['lw'] < edge_lw[1]
             and pl['scolor'] == (0, 0, 0)]
    idx_edges = []
    for e in edges:
        ends = []
        for p in e['pts']:
            hit = [i for i, n in enumerate(nodes) if math.dist(p, (n['cx'], n['cy'])) < 0.6]
            ends.append(hit[0] if hit else None)
        if None in ends:
            print('  edge not ending at nodes', e['pts'])
            continue
        idx_edges.append(tuple(ends))
    # components
    parent = list(range(len(nodes)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in idx_edges:
        parent[find(a)] = find(b)
    comps = {}
    for i in range(len(nodes)):
        comps.setdefault(find(i), []).append(i)
    trees = []
    for members in comps.values():
        roots = [i for i in members if nodes[i]['fcolor'] == (0, 0, 0)]
        sub = {old: new for new, old in enumerate(members)}
        pts = [(nodes[i]['cx'], nodes[i]['cy']) for i in members]
        es = [(sub[a], sub[b]) for a, b in idx_edges if a in sub]
        probs = []
        if len(roots) != 1:
            probs.append(f'{len(roots)} filled roots')
            code = None
        else:
            r = sub[roots[0]]
            if any(p[1] < pts[r][1] - 0.5 for p in pts):
                probs.append('a node is above the root')
            code, pr = G.tree_code(pts, es, r)
            probs += pr
        trees.append(dict(code=code, n_nodes=len(members), cx=min(p[0] for p in pts), cy=min(p[1] for p in pts),
                          rootxy=pts[sub[roots[0]]] if roots else None, probs=probs))
    return sorted(trees, key=lambda t: (round(t['cy'] / 20), t['cx']))


def all_trees(n):
    if n == 0:
        return [()]
    out = []
    for comp in comps(n):
        for kids in itertools.product(*[all_trees(s - 1) for s in comp]):
            out.append(tuple(kids))
    return out


def comps(m):
    if m == 0:
        yield ()
        return
    for f in range(1, m + 1):
        for r in comps(m - f):
            yield (f,) + r


def walk(t):
    return ''.join('U' + walk(c) + 'D' for c in t)


pages = G.load('week-12-grades-4-5.pdf')

print('== Page 1: rules example and Problem 1')
t1 = read_trees(pages[0])
for t in t1:
    print(f'  tree at ({t["cx"]:.0f},{t["cy"]:.0f}): {t["n_nodes"]} nodes, code {t["code"]}' + (f' PROBLEMS {t["probs"]}' if t['probs'] else ''))
ex = [t for t in t1 if t['n_nodes'] > 1]
check('example tree: five edges, code UUDUDDUUDD (root: left child with two leaves, right child with one leaf)',
      len(ex) == 1 and ex[0]['code'] == 'UUDUDDUUDD' and not ex[0]['probs'])
root_word = sorted([w for w in pages[0].words if w['text'] == 'root'], key=lambda w: math.dist((w['x0'], w['cy']), ex[0]['rootxy']))
others = [n for n in [(c['cx'], c['cy']) for c in pages[0].circles if c['fill']] if n != ex[0]['rootxy']]
check('example: "root" label sits beside the filled root and nearer to it than to any other node',
      math.dist((root_word[0]['x0'], root_word[0]['cy']), ex[0]['rootxy']) < 20
      and all(math.dist((root_word[0]['cx'], root_word[0]['cy']), ex[0]['rootxy']) < math.dist((root_word[0]['cx'], root_word[0]['cy']), o) for o in others),
      round(math.dist((root_word[0]['x0'], root_word[0]['cy']), ex[0]['rootxy']), 1))
lone = [t for t in t1 if t['n_nodes'] == 1]
check(f'P1: {len(lone)} printed roots for {len(all_trees(3))} three-edge trees', len(lone) == 6 and len(all_trees(3)) == 5)

print()
print('== Page 2: walk example and Problem 2')
p2 = pages[1]
t2 = read_trees(p2)
for t in t2:
    print(f'  tree at ({t["cx"]:.0f},{t["cy"]:.0f}): {t["n_nodes"]} nodes, code {t["code"]}' + (f' PROBLEMS {t["probs"]}' if t['probs'] else ''))
fork = [t for t in t2 if t['code'] == 'UDUD']
check('walk example tree is the two-edge fork UDUD', len(fork) == 1 and not fork[0]['probs'])
rootxy = fork[0]['rootxy']
# arrows: thin black segments, each with a filled arrowhead near one end
arrows = [pl for pl in p2.polylines if len(pl['pts']) == 2 and abs(pl['lw'] - 0.55) < 0.05 and pl['scolor'] == (0, 0, 0)
          and pl['pts'][0][1] < 300]
heads = [pl for pl in p2.polylines if pl['fill'] and pl['closed'] and len(pl['pts']) == 4 and abs(pl['lw'] - 0.55) < 0.05]
labs = [w for w in p2.words if w['text'] in ('1', '2', '3', '4') and w['top'] < 300]
lets = [w for w in p2.words if w['text'] in ('U', 'D') and w['top'] < 300 and w['x0'] < 300]
info = []
for a in arrows:
    p, q = a['pts']
    hc = min(heads, key=lambda h: min(math.dist(h['pts'][0], p), math.dist(h['pts'][0], q)))
    tip = p if math.dist(hc['pts'][0], p) < math.dist(hc['pts'][0], q) else q
    tail = q if tip is p else p
    away = math.dist(tip, rootxy) > math.dist(tail, rootxy)
    mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)

    def segdist(w):
        x, y = w['cx'], w['cy']
        dx, dy = q[0] - p[0], q[1] - p[1]
        t = max(0, min(1, ((x - p[0]) * dx + (y - p[1]) * dy) / (dx * dx + dy * dy)))
        return math.dist((x, y), (p[0] + t * dx, p[1] + t * dy))
    num = min(labs, key=segdist)
    let = min(lets, key=lambda w: math.dist((w['cx'], w['cy']), (num['cx'], num['cy'])))
    side = 'left' if mid[0] < rootxy[0] else 'right'
    info.append((int(num['text']), let['text'], 'away' if away else 'toward', side))
info.sort()
print('  arrows (number, letter, direction from root, edge):', info)
check('walk arrows: 1 U away and 2 D back on the left edge, 3 U away and 4 D back on the right edge',
      info == [(1, 'U', 'away', 'left'), (2, 'D', 'toward', 'left'), (3, 'U', 'away', 'right'), (4, 'D', 'toward', 'right')])
# grid example
base = [pl for pl in p2.polylines if len(pl['pts']) == 2 and abs(pl['lw'] - 0.8) < 0.05 and pl['scolor'] == (0, 0, 0)]
path = [pl for pl in p2.polylines if len(pl['pts']) > 2 and pl['lw'] > 1]
gl = [pl for pl in p2.polylines if pl['scolor'] == (0.825, 0.825, 0.825)]
xs = sorted({round(pl['pts'][0][0], 2) for pl in gl if abs(pl['pts'][0][0] - pl['pts'][1][0]) < .01})
ys = sorted({round(pl['pts'][0][1], 2) for pl in gl if abs(pl['pts'][0][1] - pl['pts'][1][1]) < .01})
step = xs[1] - xs[0]
w, st = G.word_from_polyline(path[0]['pts'], step)
check('example grid: square cells, path UDUD from the filled start dot', w == 'UDUD' and abs((ys[1] - ys[0]) - step) < 0.05
      and abs(path[0]['pts'][0][1] - base[0]['pts'][0][1]) < 0.1, (w, len(xs) - 1, len(ys)))
hs = G.heights(w)
x0, y0 = path[0]['pts'][0]
mids = [(x0 + (k + .5) * step, y0 - (hs[k] + hs[k + 1]) / 2 * step) for k in range(4)]
gl_lets = [w_ for w_ in p2.words if w_['text'] in ('U', 'D') and w_['x0'] > 300 and y0 - 3 * step < w_['top'] < y0]
bad = [(x['text'], k) for x in gl_lets for k in [min(range(4), key=lambda k: math.dist((x['cx'], x['cy']), mids[k]))] if w[k] != x['text']]
check('example grid: four step letters, each over its own step', len(gl_lets) == 4 and not bad, (len(gl_lets), bad))
code_word = [x['text'] for x in p2.words if x['text'] == 'UDUD']
check('example: "Walk code: UDUD"', code_word == ['UDUD'])
prob = [t for t in t2 if t['code'] != 'UDUD']
codes = [t['code'] for t in sorted(prob, key=lambda t: (round(t['rootxy'][1] / 50), t['rootxy'][0]))]
print('  P2 trees (top-left, top-right, bottom-left, bottom-right):', codes)
check('P2: four 4-edge trees with codes UUUUDDDD, UDUDUDUD, UUDUDDUD, UDUUUDDD (guide key)',
      codes == ['UUUUDDDD', 'UDUDUDUD', 'UUDUDDUD', 'UDUUUDDD'] and all(not t['probs'] for t in prob))
rects = [pl for pl in p2.polylines if pl['closed'] and pl['scolor'] == (0.675, 0.675, 0.675)]
check('P2: 32 code boxes (8 per tree)', len(rects) == 32)
# features the guide says can be read from the code, checked on these four trees and on all trees n<=6
ok = True
for n in range(1, 7):
    for t in all_trees(n):
        c = walk(t)
        hs = G.heights(c)

        def depth(t):
            return 0 if not t else 1 + max(depth(x) for x in t)

        def leaves(t):
            return 1 if not t else sum(leaves(x) for x in t)
        ok &= (len(c) == 2 * n and max(hs) == depth(t) and c.count('UD') == leaves(t) and hs[1:].count(0) == len(t))
check('P2 guide features: length = 2 x edges, max height = depth, UD peaks = leaves, returns = root children (n<=6)', ok)

print()
print('== Page 3: Problem 3')
p3 = pages[2]
codes3 = [w['text'] for w in sorted(p3.words, key=lambda w: (round(w['top']), w['x0'])) if set(w['text']) <= set('UD') and len(w['text']) >= 6]
check('P3: codes UUDDUD, UDUUDD, UUDUDUDD, UUUDDUDD', codes3 == ['UUDDUD', 'UDUUDD', 'UUDUDUDD', 'UUUDDUDD'], codes3)
for c in codes3:
    ts = [t for t in all_trees(len(c) // 2) if walk(t) == c]
    print(f'  {c}: {len(ts)} tree(s) {ts}')
check('P3: each code has exactly one tree', all(len([t for t in all_trees(len(c) // 2) if walk(t) == c]) == 1 for c in codes3))
check('P3: one printed root under each code', len([c for c in p3.circles if c['fill']]) == 4)

print()
print('== Page 4: Problem 4')
codes4 = [w['text'] for w in sorted(pages[3].words, key=lambda w: (round(w['top']), w['x0'])) if set(w['text']) <= set('UD') and len(w['text']) == 8]
check('P4: six printed codes', codes4 == ['UUUUDDDD', 'UUDDDUUD', 'UDUDUUDD', 'UUDUDUDU', 'UUUDUDDD', 'DUUUDDUD'], codes4)
for c in codes4:
    ts = [t for t in all_trees(4) if walk(t) == c]
    print(f'  {c}: heights {G.heights(c)} -> {len(ts)} tree(s)')
check('P4: valid exactly UUUUDDDD, UDUDUUDD, UUUDUDDD',
      [c for c in codes4 if any(walk(t) == c for t in all_trees(4))] == ['UUUUDDDD', 'UDUDUUDD', 'UUUDUDDD'])

print()
print('== Pages 5-6: Problems 5 and 6')
check('P5: 16 printed roots for 14 four-edge trees', len([c for c in pages[4].circles if c['fill']]) == 16 and len(all_trees(4)) == 14)
check('P6: 42 five-edge and 132 six-edge trees', len(all_trees(5)) == 42 and len(all_trees(6)) == 132)
print()
print('FAILED:', FAIL if FAIL else 'none')
