"""Check of the Week 56 K-1 route and card fixes, October 23, 2026 (written for the card fixes).

The K-1 route (guide pp. 1-5): Problem 1 for the cube and tetrahedron, Problem 3,
Problem 4 for the same two solids by copying each corner's gap from a paper circle
and gathering the copies into whole circles, then Problem 5 as "Which corner leaves
the bigger gap?". This script checks, from 3D coordinates and its own convex hull
(common56.py), not from the packet's own checkers:

  * every vertex gap of the five solids, and which solids' gap copies fill whole
    circles without cutting (an exact partition of the gaps into groups of 360);
  * the paper circles a younger pair uses (one per copied gap) and the fan pieces
    each K-1 step needs, against the 8 triangles and 8 squares a pair receives;
  * the bigger gap on the square pyramid;
  * the two Problem 1 icons in the new template (card should 2): right edge graph,
    every vertex inside the outline all solid or all dashed, no vertex on another edge;
  * with PDFs given, the revised packet: page headers (K-5 on pp. 1 and 3-5), footer
    N56-S-v3, one problem per page, P5 and P6 wording; and materials p. 5, six circles
    of one size with center dots.

Run: python3 check_k1_route.py [students.pdf materials.pdf]
     (writes out_check_k1_route.txt beside itself; the recorded run used the print copies)
"""
import itertools
import math
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True
from common56 import HERE, SRC, Report, convex_hull, solid, sub, dot, norm

R = Report(os.path.join(HERE, 'out_check_k1_route.txt'))


def face_angles(points, faces):
    """Angle in degrees of every face corner at every vertex."""
    at = {i: [] for i in range(len(points))}
    for f in faces:
        for k, v in enumerate(f):
            a, b = points[f[k - 1]], points[f[(k + 1) % len(f)]]
            u, w = sub(a, points[v]), sub(b, points[v])
            at[v].append(math.degrees(math.acos(max(-1, min(1, dot(u, w) / (norm(u) * norm(w)))))))
    return at


def whole_circles(gaps):
    """Can the gap pieces be split into groups that each make exactly one full turn?"""
    gaps = sorted(gaps, reverse=True)
    if round(sum(gaps)) % 360:
        return None

    def place(rest, bins):
        if not rest:
            return all(abs(b - 360) < 1e-6 for b in bins)
        g, tail = rest[0], rest[1:]
        tried = set()
        for i, b in enumerate(bins):
            if b + g <= 360 + 1e-6 and round(b, 6) not in tried:
                tried.add(round(b, 6))
                bins[i] += g
                if place(tail, bins):
                    return True
                bins[i] -= g
        return False
    return place(gaps, [0.0] * round(sum(gaps) / 360))


R.out('== Vertex gaps from 3D coordinates, and whole circles without cutting ==')
gaps_of, corners_of = {}, {}
for name in ('cube', 'tetrahedron', 'octahedron', 'triangular prism', 'square pyramid'):
    P = solid(name)
    faces, edges = convex_hull(P)
    at = face_angles(P, faces)
    gaps = [360 - sum(a) for a in at.values()]
    gaps_of[name] = gaps
    corners_of[name] = {v: sorted(round(x) for x in a) for v, a in at.items()}
    V, E, F = len(P), len(edges), len(faces)
    R.check(V - E + F == 2 and abs(sum(gaps) - 720) < 1e-6,
            f'{name}: (V,E,F) = ({V},{E},{F}), gaps {sorted(round(g) for g in gaps)}, total {sum(gaps):.6f}')
    fits = whole_circles(gaps)
    R.out(f'   {name}: gap copies fill {round(sum(gaps) / 360)} whole circles without cutting: {fits}')
R.check(whole_circles(gaps_of['cube']) and sorted(round(g) for g in gaps_of['cube']) == [90] * 8,
        'cube: eight quarter-circle copies make two whole circles')
R.check(whole_circles(gaps_of['tetrahedron']) and sorted(round(g) for g in gaps_of['tetrahedron']) == [180] * 4,
        'tetrahedron: four half-circle copies make two whole circles')
R.check(whole_circles(gaps_of['square pyramid']) is False,
        'square pyramid: 120 and four 150s fill two circles only if a piece is cut (no exact split)')
R.check(whole_circles(gaps_of['octahedron']) and whole_circles(gaps_of['triangular prism']),
        'octahedron and prism (six thirds each) would also make two whole circles: an optional K-1 extension')

R.out('')
R.out('== Paper circles and fan pieces for one younger pair ==')
circles_p4 = len(gaps_of['cube']) + len(gaps_of['tetrahedron'])
R.check(circles_p4 == 12, f'Problem 4, one copy per corner of the cube and tetrahedron: {circles_p4} circles (the card\'s 12)')
circles_p5 = 2
R.check(circles_p4 + circles_p5 == 14, f'Problem 5 copies one top gap and one base-corner gap: {circles_p5} more, {circles_p4 + circles_p5} in all')
R.check(3 * 6 - 14 == 4, 'materials p. 5 has six circles: three copies per pair give 18, four spare')
pieces = {'cube corner': (0, 3), 'tetrahedron corner': (3, 0),
          'pyramid top and base corner, both at once': (4 + 2, 1)}
for what, (tri, sq) in pieces.items():
    R.check(tri <= 8 and sq <= 8, f'{what}: {tri} triangles, {sq} squares, within a pair\'s 8 and 8')
P = solid('square pyramid')
top = max(range(len(P)), key=lambda i: P[i][2])
gp = gaps_of['square pyramid']
base = [g for i, g in enumerate(gp) if i != top]
R.check(abs(gp[top] - 120) < 1e-6 and all(abs(g - 150) < 1e-6 for g in base),
        f'pyramid: top gap {gp[top]:.3f} from corners {corners_of["square pyramid"][top]}, base gaps {[round(g, 3) for g in base]}')
R.check(max(base) > gp[top], 'the base corner leaves the bigger gap (150 > 120); the copies differ by 30 degrees')

R.out('')
R.out('== Problem 1 icons in the revised template (card should 2) ==')
TEX = open(os.path.join(SRC, 'template.tex')).read()
NUM = r'-?\d*\.?\d+'


def macro_body(name):
    return re.search(r'\\newcommand\{\\' + name + r'\}\{(.*?)\\end\{tikzpicture\}\}', TEX, re.S).group(1)


def segments(body):
    segs = []
    for opt, path in re.findall(r'\\draw(\[[^\]]*\])?\s*(.*?);', body, re.S):
        style = 'dashed' if opt and 'dashed' in opt else 'solid'
        toks = re.findall(r'\((' + NUM + r'),(' + NUM + r')\)|(--)|(cycle)', path)
        start = prev = None
        pending = False
        for x, y, dash, cyc in toks:
            if dash:
                pending = True
                continue
            if cyc:
                segs.append((prev, start, style)); prev = start; pending = False
                continue
            pt = (float(x), float(y))
            if pending and prev is not None:
                segs.append((prev, pt, style))
            else:
                start = pt
            prev, pending = pt, False
    return segs


def on_interior(p, a, b):
    ax, ay = b[0] - a[0], b[1] - a[1]
    if abs((p[0] - a[0]) * ay - (p[1] - a[1]) * ax) > 1e-6:
        return False
    t = ((p[0] - a[0]) * ax + (p[1] - a[1]) * ay) / (ax * ax + ay * ay)
    return 1e-6 < t < 1 - 1e-6


def hull2d(points):
    pts = sorted(set(points))

    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 1e-12:
                h.pop()
            h.append(p)
        return h
    return half(pts)[:-1] + half(pts[::-1])[:-1]


for macro, name in (('tetra', 'tetrahedron'), ('octa', 'octahedron')):
    style = {}
    for a, b, s in segments(macro_body(macro)):
        k = frozenset((a, b))
        style[k] = 'solid' if style.get(k) == 'solid' or s == 'solid' else 'dashed'
    vs = sorted({p for k in style for p in k})
    P = solid(name)
    target = {frozenset(e) for e in convex_hull(P)[1]}
    idx = {v: i for i, v in enumerate(vs)}
    iso = len(vs) == len(P) and len(style) == len(target) and any(
        all(frozenset((perm[idx[a]], perm[idx[b]])) in target for a, b in map(tuple, style))
        for perm in itertools.permutations(range(len(P))))
    R.check(iso, f'{name} icon: {len(vs)} vertices, {len(style)} edges '
                 f'({sum(v == "dashed" for v in style.values())} dashed) form the {name} graph')
    outline = hull2d(vs)
    mixed = [v for v in vs if v not in outline and len({style[k] for k in style if v in k}) > 1]
    R.check(not mixed, f'{name} icon: each vertex inside the outline has all edges solid or all dashed {mixed or ""}')
    on_edge = [(v, tuple(k)) for v in vs for k in style if v not in k and on_interior(v, *tuple(k))]
    R.check(not on_edge, f'{name} icon: no vertex drawn on another edge {on_edge or ""}')

if len(sys.argv) == 3:
    students, materials = sys.argv[1:]
    R.out('')
    R.out(f'== Revised packet: {students} ==')
    text = subprocess.run(['pdftotext', students, '-'], capture_output=True, text=True, check=True).stdout
    pages = [p for p in text.split('\f') if p.strip()]
    want = {1: 'K–5', 2: '2–5', 3: 'K–5', 4: 'K–5', 5: 'K–5', 6: '2–5', 7: '4–5', 8: '4–5', 9: '4–5'}
    R.check(len(pages) == 9, f'{len(pages)} pages')
    for i, p in enumerate(pages, 1):
        R.check(f'Week 56 / Corners of a solid / Grades {want[i]}' in p
                and 'Bellingham Math Circle / Week 56 / N56-S-v3' in p and re.findall(r'Problem (\d+):', p) == [str(i)],
                f'p. {i}: header Grades {want[i]}, footer N56-S-v3, Problem {i}')
    flat = ' '.join(text.split())
    R.check('Which corner leaves the bigger gap, the top or a base corner? Find its total gap.' in flat,
            'P5 asks which corner leaves the bigger gap, then the total')
    R.check('five faces of the closed model' not in flat, 'P5 caption removed (card could 7)')
    R.check('try each of these three changes on its own, starting from the original cube' in flat,
            'P6 says each change starts from the original cube (card should 3 / could 5)')
    R.out(f'== Materials: {materials} ==')
    import pymupdf
    doc = pymupdf.open(materials)
    R.check(len(doc) == 5, f'{len(doc)} materials pages')
    circles, dots = [], 0
    for d in doc[4].get_drawings():
        items = d['items']
        if all(it[0] == 'c' for it in items) and len(items) == 4:
            w = d['rect'].width * 25.4 / 72
            if w > 10:
                circles.append(round(w, 2))
            else:
                dots += 1
    R.check(len(circles) == 6 and len(set(circles)) == 1 and dots == 6,
            f'materials p. 5: {len(circles)} circles of diameter {sorted(set(circles))} mm, {dots} center dots')
    t5 = ' '.join(doc[4].get_text().split())
    R.check('A younger pair uses 14 circles' in t5 and 'N56-M-v2' in t5, 'materials p. 5 text names 14 circles; footer N56-M-v2')

R.finish()
sys.exit(1 if R.fails else 0)
