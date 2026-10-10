"""Grades 4-5 Problem 5 (p. 6): read the Koenigsberg map from the PDF (land shapes, labels, bridge
bands), decide which two land areas each bridge joins, and answer the three questions by search.
Run: python3 check_koenigsberg.py > check_koenigsberg.out
"""
import os
import sys
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
from graphs import Town, additions

FAILS = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def inside(pt, poly):
    x, y = pt
    n = len(poly)
    c = False
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                c = not c
    return c


p, objs, words = R.page_objects('g45', 6)
lands = [o for o in objs if o['object_type'] == 'curve' and o.get('fill') and str(o.get('non_stroking_color')) in ('1.0', '1')]
polys = [R.bezier_points(o, 60) for o in lands]
water = [o for o in objs if o['object_type'] == 'rect' and o.get('fill')]
check('map: one water rectangle and four land shapes', len(water) == 1 and len(polys) == 4, (len(water), len(polys)))
letters = {w['text']: ((w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2) for w in words if w['text'] in 'ABCD' and len(w['text']) == 1}
name = {}
for k, poly in enumerate(polys):
    hits = [L for L, pt in letters.items() if inside(pt, poly)]
    check(f'land shape {k}: contains exactly one letter', len(hits) == 1, hits)
    name[k] = hits[0]
bands = [o for o in objs if abs((o.get('linewidth') or 0) - 1.6 * R.CM) < 0.3]
edges = []
for o in bands:
    a, b = R.endpoints(o)
    la = [name[k] for k, poly in enumerate(polys) if inside(a, poly)]
    lb = [name[k] for k, poly in enumerate(polys) if inside(b, poly)]
    # the middle of the band must be over water, not land
    pts = R.bezier_points(o, 40)
    path = [(a[0] + (b[0] - a[0]) * t / 50, a[1] + (b[1] - a[1]) * t / 50) for t in range(51)]
    lands_crossed = []
    for q in path:
        here = [name[k] for k, poly in enumerate(polys) if inside(q, poly)]
        tag = here[0] if here else 'water'
        if not lands_crossed or lands_crossed[-1] != tag:
            lands_crossed.append(tag)
    check(f'bridge {a[0]:.0f},{a[1]:.0f} -> {b[0]:.0f},{b[1]:.0f}: land, water, land', len(la) == 1 and len(lb) == 1 and
          lands_crossed == [la[0], 'water', lb[0]], lands_crossed)
    edges.append((la[0], lb[0]))
print('  bridges read:', sorted(''.join(sorted(e)) for e in edges))
check('7 bridges: A-B twice, A-C twice, A-D, B-D, C-D (the historical layout the guide states)',
      sorted(''.join(sorted(e)) for e in edges) == sorted(['AB', 'AB', 'AC', 'AC', 'AD', 'BD', 'CD']))
k = Town('ABCD', edges)
check('degrees A5 B3 C3 D3', k.degrees() == {'A': 5, 'B': 3, 'C': 3, 'D': 3}, k.degrees())
check('no walk crosses every bridge exactly once', not k.has_walk())
one = additions(k, 1)
check('one new bridge between any two of the four areas makes a walk possible (6 choices)', len(one) == 6, [a[0] for a in one])
for a in one:
    u, v = a[0]
    rest = set('ABCD') - {u, v}
    check(f'  after adding {u}-{v}, walks run between {"".join(sorted(rest))}', set(k.plus(a).start_end()) == rest)
check('one new bridge cannot give a closed walk', not additions(k, 1, closed=True))
two = additions(k, 2, closed=True)
check('two new bridges give a closed walk exactly when they pair up the four areas (3 ways)', len(two) == 3 and all(
    set(a[0]) | set(a[1]) == set('ABCD') for a in two), two)
# Euler's letter count
need = sum((d + 1) // 2 for d in k.degrees().values())
check('Euler: a 7-bridge walk names 8 areas, but the areas need 3+2+2+2 = 9 places', need == 9 and len(edges) + 1 == 8)
# west of A: is there water between B and C to the left of island A?
xa = min(x for x, y in polys[[kk for kk in name if name[kk] == 'A'][0]])
wx0 = water[0]['x0']
check('there is open water between B and C west of A (room for a new B-C bridge)', xa - wx0 > 1.6 * R.CM, round(xa - wx0, 1))
print()
print('FAILURES:', FAILS if FAILS else 'none')
