"""Adult guide pp. 3-5: read every K-1 answer picture (nodes filled black or white, grey bridges,
thick black bridges, dashed new bridges, start dots on tracing pictures) and compare each with the
student town it stands for and with the answers found by search.
Run: python3 check_guide_figs.py > check_guide_figs.out
"""
import os
import sys
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
from graphs import Town

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def guide_figs(pg):
    p, objs, words = R.page_objects('fac', pg)
    nodes = []
    for o in objs:
        if o['object_type'] == 'curve' and o.get('fill') and abs((o.get('linewidth') or 0) - 0.6) < 0.05:
            c = R.circle_of(o)
            if c:
                nodes.append((c[0], c[1], str(o.get('non_stroking_color')) in ('0.0', '0')))
    edges = []
    for o in objs:
        lw = o.get('linewidth') or 0
        if o['object_type'] == 'rect':
            continue
        kind = None
        if abs(lw - 2.99) < 0.05 and str(o.get('stroking_color')) in ('0.62', '0.6196'):
            kind = 'grey'
        elif abs(lw - 2.99) < 0.05:
            kind = 'grey'
        elif abs(lw - 3.39) < 0.05:
            kind = 'thick'
        elif abs(lw - 1.39) < 0.05 and o.get('dash'):
            kind = 'dashed'
        if not kind:
            continue
        a, b = R.endpoints(o)
        ia = min(range(len(nodes)), key=lambda i: math.hypot(nodes[i][0] - a[0], nodes[i][1] - a[1]))
        ib = min(range(len(nodes)), key=lambda i: math.hypot(nodes[i][0] - b[0], nodes[i][1] - b[1]))
        da = math.hypot(nodes[ia][0] - a[0], nodes[ia][1] - a[1])
        db = math.hypot(nodes[ib][0] - b[0], nodes[ib][1] - b[1])
        edges.append((ia, ib, kind, round(max(da, db), 2)))
    parent = list(range(len(nodes)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for a, b, k, d in edges:
        parent[find(a)] = find(b)
    comps = {}
    for i in range(len(nodes)):
        comps.setdefault(find(i), []).append(i)
    figs = []
    for members in comps.values():
        ys = [nodes[i][1] for i in members]
        xs = [nodes[i][0] for i in members]
        figs.append({'nodes': {i: nodes[i] for i in members},
                     'edges': [e for e in edges if e[0] in members],
                     'key': (round(max(ys) / 80), min(xs))})
    figs.sort(key=lambda f: f['key'])
    return figs


def normalize(pos):
    cx = sum(p[0] for p in pos.values()) / len(pos)
    cy = sum(p[1] for p in pos.values()) / len(pos)
    s = math.sqrt(sum((p[0] - cx) ** 2 + (p[1] - cy) ** 2 for p in pos.values()) / len(pos))
    return {k: ((p[0] - cx) / s, (p[1] - cy) / s) for k, p in pos.items()}


def match(fig, town_pos):
    """Map guide nodes to student islands by normalized position."""
    g = normalize({i: n[:2] for i, n in fig['nodes'].items()})
    t = normalize(town_pos)
    m = {}
    worst = 0
    for i, (x, y) in g.items():
        j = min(t, key=lambda j: math.hypot(t[j][0] - x, t[j][1] - y))
        worst = max(worst, math.hypot(t[j][0] - x, t[j][1] - y))
        m[i] = j
    return m, worst


def student(key, pg):
    out = []
    towns, probs, rects, words = R.read_towns(key, pg)
    for t in towns:
        names, edges, pos = R.town_graph(t)
        out.append((Town(names, edges), pos))
    return out


def edge_multiset(pairs):
    return sorted(tuple(sorted(e)) for e in pairs)


figs3 = guide_figs(3)
figs4 = guide_figs(4)
figs5 = guide_figs(5)
print(f'  guide figures read: p3 {len(figs3)}, p4 {len(figs4)}, p5 {len(figs5)}')
check('every guide bridge ends at node centres', all(e[3] < 0.6 for f in figs3 + figs4 + figs5 for e in f['edges']))
# Problem plan: (guide figures, student pages, rule)
plan = [
    ('K-1 P1', figs3[0:4], [('k1', 1)], 'starts'),
    ('K-1 P2', figs3[4:6], [('k1', 2)], 'starts'),
    ('K-1 P3', figs3[6:11], [('k1', 3), ('k1', 4)], 'starts'),
    ('K-1 P4', figs4[0:5], [('k1', 5), ('k1', 6)], 'starts'),
    ('K-1 P6', figs4[5:8], [('k1', 9), ('k1', 10)], 'odd+dashed'),
    ('K-1 P8', figs5[0:3], [('k1', 11), ('k1', 12)], 'thick'),
]
for name, figs, pages, rule in plan:
    towns = [tp for key, pg in pages for tp in student(key, pg)]
    used = set()
    for fi, fig in enumerate(figs):
        main = [e for e in fig['edges'] if e[2] != 'dashed']
        best = None
        for ti, (t, pos) in enumerate(towns):
            if ti in used or len(t.V) != len(fig['nodes']) or len(t.E) != len(main):
                continue
            m, worst = match(fig, pos)
            if len(set(m.values())) != len(m):
                continue
            if edge_multiset((m[a], m[b]) for a, b, k, d in main) != edge_multiset(t.E):
                continue
            if best is None or worst < best[2]:
                best = (ti, m, worst)
        check(f'{name} guide figure {fi + 1}: same town and layout as a student town', best is not None and best[2] < 0.12,
              None if best is None else f'student town {best[0] + 1}, layout error {best[2]:.3f}')
        if best is None:
            continue
        ti, m, worst = best
        used.add(ti)
        t, pos = towns[ti]
        filled = {m[i] for i, n in fig['nodes'].items() if n[2]}
        if rule == 'starts':
            se = t.start_end()
            check(f'{name} guide figure {fi + 1}: filled islands = islands where a walk can start', filled == set(se) or
                  (filled == set() and not se) or (filled == set(t.V) and set(se) == set(t.V)), (sorted(filled), sorted(se)))
        elif rule == 'odd+dashed':
            check(f'{name} guide figure {fi + 1}: filled islands = odd islands', filled == set(t.odd()), (sorted(filled), t.odd()))
            dashed = [(m[a], m[b]) for a, b, k, d in fig['edges'] if k == 'dashed']
            check(f'{name} guide figure {fi + 1}: the dashed new bridge makes a walk possible', len(dashed) == 1 and t.plus(dashed).has_walk(), dashed)
        elif rule == 'thick':
            thick = edge_multiset((m[a], m[b]) for a, b, k, d in main if k == 'thick')
            works = edge_multiset(t.E[i] for i in range(len(t.E)) if t.doubled([i]).has_walk())
            check(f'{name} guide figure {fi + 1}: thick bridges = bridges where two counters work', thick == works, (thick, works))

# Problem 5 tracing pictures: the "start at a dot" dots must sit on the two odd points
p, objs, words = R.page_objects('fac', 4)
dots = [((o['x0'] + o['x1']) / 2, (o['top'] + o['bottom']) / 2) for o in objs
        if o['object_type'] == 'curve' and o.get('fill') and abs((o.get('linewidth') or 0) - 0.4) < 0.05 and o['x1'] - o['x0'] < 6]
print('  P5 dots at', [(round(x, 1), round(y, 1)) for x, y in dots])
segs = []
for o in objs:
    if abs((o.get('linewidth') or 0) - 0.8) < 0.05 and o['object_type'] == 'line':
        a, b = R.endpoints(o)
        segs.append((a, b))
for (x, y) in dots:
    meet = sum(1 for a, b in segs for q in (a, b) if math.hypot(q[0] - x, q[1] - y) < 0.6)
    circ = [o for o in objs if o['object_type'] == 'curve' and abs((o.get('linewidth') or 0) - 0.8) < 0.05 and R.circle_of(o)
            and abs(math.hypot(x - R.circle_of(o)[0], y - R.circle_of(o)[1]) - R.circle_of(o)[2]) < 0.6]
    deg = meet + 2 * len(circ)
    check(f'K-1 P5 guide dot at ({x:.0f},{y:.0f}) sits where an odd number of lines meet', deg % 2 == 1, deg)
print()
print('FAILURES:', FAILS if FAILS else 'none')
