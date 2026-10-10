"""Drawn-town geometry in the three student PDFs: bands that touch or overlap away from a shared
island (which would read as a junction), band visible lengths, island labels, regular shapes,
and the answer boxes and lines the pages provide.
Run: python3 check_geometry.py > check_geometry.out
"""
import os
import sys
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R

FAILS = []
W = 1.6 * R.CM
RI = 27.0


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


PAGES = {'k1': range(1, 13), 'g23': range(1, 13), 'g45': range(1, 13)}
min_vis = []
for key, pages in PAGES.items():
    for pg in pages:
        towns, probs, rects, words = R.read_towns(key, pg)
        for ti, t in enumerate(towns):
            isl = t['islands']
            polys = t['polylines']
            # visible length of each band
            for a, b, pts in polys:
                L = sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
                min_vis.append((L - 2 * RI, key, pg, ti))
            # band-band clearance away from shared islands
            bad = []
            for (a1, b1, p1), (a2, b2, p2) in itertools.combinations(polys, 2):
                shared = {a1, b1} & {a2, b2}

                def far(p):
                    return all(math.hypot(p[0] - isl[s][0], p[1] - isl[s][1]) > RI + W for s in shared)
                q1 = [p for p in p1 if far(p)]
                q2 = [p for p in p2 if far(p)]
                if not q1 or not q2:
                    continue
                d = min(math.hypot(x1 - x2, y1 - y2) for x1, y1 in q1 for x2, y2 in q2)
                if d < W + 2:
                    bad.append((a1, b1, a2, b2, round(d, 1)))
            check(f'{key} p{pg} town {ti + 1}: no two bands touch away from a shared island', not bad, bad)
            labs = [v for v in t['labels'].values() if v]
            if labs:
                check(f'{key} p{pg} town {ti + 1}: labels unique, consecutive from A', sorted(labs) == [chr(65 + i) for i in range(len(labs))]
                      and len(labs) == len(isl), sorted(labs))
            else:
                check(f'{key} p{pg} town {ti + 1}: unlabelled (K-1)', key == 'k1')
        # towns must not overlap one another
        for (i, t1), (j, t2) in itertools.combinations(enumerate(towns), 2):
            a, b = t1['bbox'], t2['bbox']
            sep = max(b[0] - a[2], a[0] - b[2], b[1] - a[3], a[1] - b[3])
            check(f'{key} p{pg} towns {i + 1} and {j + 1}: island centres separated', sep > 2 * RI + 10, round(sep, 1))
v = min(min_vis)
check('every band shows at least 3 cm between its islands (guide p. 2 claim)', v[0] >= 3 * R.CM - 0.5,
      f'shortest {v[0] / R.CM:.2f} cm at {v[1]} p{v[2]} town {v[3] + 1}')

# K-1 boxes: Problems 3 and 4 put one check box with every town
for pg, n in [(3, 3), (4, 2), (5, 3), (6, 2)]:
    towns, probs, rects, words = R.read_towns('k1', pg)
    boxes = [r for r in rects if abs(r['x1'] - r['x0'] - 1.35 * R.CM) < 1 and abs(r['bottom'] - r['top'] - 1.35 * R.CM) < 1]
    check(f'k1 p{pg}: one check box per town', len(towns) == n and len(boxes) == n, (len(towns), len(boxes)))

# equal scaling: equilateral triangles of islands in the triangle-lattice towns
for key, pg, sig in [('k1', 1, (3, 3)), ('k1', 2, (6, 9)), ('g23', 4, (6, 9)), ('g45', 9, (10, 18)), ('k1', 6, (7, 9)),
                     ('g23', 3, (7, 9)), ('g45', 3, (7, 9))]:
    towns, probs, rects, words = R.read_towns(key, pg)
    for t in towns:
        if (len(t['islands']), len(t['bridges'])) != sig:
            continue
        lens = []
        for a, b, kind in t['bridges']:
            (x1, y1), (x2, y2) = t['islands'][a], t['islands'][b]
            lens.append(math.hypot(x2 - x1, y2 - y1))
        check(f'{key} p{pg} {sig}: all bridges the same length (equal x/y scaling)', max(lens) - min(lens) < 0.5,
              f'{min(lens):.2f}-{max(lens):.2f} pt')

print()
print('FAILURES:', FAILS if FAILS else 'none')

# guide p. 1 counter counts: busiest page per band
print('---- bridges printed per page (guide p. 1: K-1 20 on p. 1; 2-3 22 on p. 7; 4-5 18 on p. 9)')
FAILS2 = []
for key, want in [('k1', (1, 20)), ('g23', (7, 22)), ('g45', (9, 18))]:
    per = {}
    for pg in range(1, 13):
        towns, probs, rects, words = R.read_towns(key, pg)
        per[pg] = sum(len(t['bridges']) for t in towns)
    top = max(per.values())
    print(f'  {key}: ' + ', '.join(f'p{pg} {n}' for pg, n in per.items() if n))
    ok = per[want[0]] == want[1] == top
    print(('PASS ' if ok else 'FAIL ') + f'{key}: busiest page is p{want[0]} with {want[1]} bridges')
    if not ok:
        FAILS2.append(key)
print('FAILURES (counts):', FAILS2 if FAILS2 else 'none')
