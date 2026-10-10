"""Diagram check of the Week 56 student pages and materials (written for this review).

Reads coordinates from the editable student source students.tex (no writer
code is imported), text from the delivered student PDF, and pixels from a
254 dpi render (10 px per mm) of the delivered materials PDF.
  * Packet structure: headers, footers, Problems 1-9 in order, grade labels.
  * The five model icons (pp.1, 5): their drawn edge graphs are the right
    solids, and whether the drawing is a possible view of a convex solid
    (a vertex inside the outline has all its edges solid or all dashed; no
    vertex sits in the middle of another drawn edge).
  * Equal scaling / regular shapes in every worked visual and problem
    diagram (pp.2-9): equilateral triangles, squares, the regular pentagon,
    the 5x60 and 3x108 fans of Problem 9, the gap arcs.
  * Problem 6 pictures (diagonal, centre lines, edge midpoint) and the
    Problem 7 drawings (opened cube, tetrahedron view and tree).
  * Delivered materials PDF at 100%: 30 mm check bar, 80 mm circles.
Run: python3 check_diagrams.py   (writes out_check_diagrams.txt beside itself)
"""
import itertools
import math
import os
import re
import subprocess
import tempfile

import sys
sys.dont_write_bytecode = True  # keep the check folder free of __pycache__
from common56 import HERE, SRC, STUDENT_PDF, MATERIALS_PDF, Report, pdftext, convex_hull, solid

R = Report(os.path.join(HERE, 'out_check_diagrams.txt'))
TEX = open(os.path.join(SRC, 'student', 'students.tex')).read()
NUM = r'-?\d*\.?\d+'

# ---------------------------------------------------------------- structure
R.out('== Packet structure (delivered student PDF) ==')
pages = pdftext(STUDENT_PDF).split('\f')
pages = [p for p in pages if p.strip()]
R.check(len(pages) == 9, f'{len(pages)} student pages')
probs = []
for i, p in enumerate(pages, 1):
    head = 'Week 56 / Corners of a solid / ' + ('Grades 2–5' if i <= 6 else 'Grades 4–5')
    R.check(head in p and 'Bellingham Math Circle / Week 56 / N56-S-v2' in p, f'p.{i}: header "{head}" and footer')
    probs += [(int(n), i) for n in re.findall(r'Problem (\d+):', p)]
R.check([n for n, _ in probs] == list(range(1, 10)), f'problems numbered consecutively: {probs}')

# ---------------------------------------------------------------- icons


def macro_body(name):
    m = re.search(r'\\newcommand\{\\' + name + r'\}(?:\[1\]\[\])?\{(.*?)\\end\{tikzpicture\}\}', TEX, re.S)
    return m.group(1)


def parse_paths(body):
    coords = {k: (float(x), float(y)) for k, x, y in re.findall(r'\\coordinate \((\w+)\) at \((' + NUM + '),(' + NUM + r')\)', body)}
    segs = []
    for opt, path in re.findall(r'\\draw(\[[^\]]*\])?\s*(.*?);', body, re.S):
        style = 'dashed' if opt and 'dashed' in opt else 'solid'
        if opt and 'fill' in opt:
            style = 'solid'
        # tokens: points or '--' or 'cycle'
        toks = re.findall(r'\((' + NUM + r'),(' + NUM + r')\)|\((\w+)\)|(--)|(cycle)', path)
        start = prev = None
        pending = False
        for xa, ya, nm, dash, cyc in toks:
            if dash:
                pending = True
                continue
            if cyc:
                segs.append((prev, start, style)); prev = start; pending = False
                continue
            pt = (float(xa), float(ya)) if xa else coords[nm]
            if pending and prev is not None:
                segs.append((prev, pt, style))
            else:
                start = pt
            prev = pt
            pending = False
    return segs


def on_segment_interior(p, a, b, tol=1e-6):
    ax, ay = b[0] - a[0], b[1] - a[1]
    cr = (p[0] - a[0]) * ay - (p[1] - a[1]) * ax
    if abs(cr) > tol:
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
    lo, up = half(pts), half(pts[::-1])
    return lo[:-1] + up[:-1]


def graph_iso(vs, es, solid_name):
    P = solid(solid_name)
    hf, he = convex_hull(P)
    target = {frozenset(e) for e in he}
    if len(vs) != len(P) or len(es) != len(target):
        return False
    idx = {v: i for i, v in enumerate(vs)}
    E = [(idx[a], idx[b]) for a, b in es]
    for perm in itertools.permutations(range(len(P))):
        if all(frozenset((perm[a], perm[b])) in target for a, b in E):
            return True
    return False


def icon_bodies():
    for macro, name in [('cube', 'cube'), ('tetra', 'tetrahedron'), ('prism', 'triangular prism'),
                        ('octa', 'octahedron'), ('pyramid', 'square pyramid')]:
        yield name, macro_body(macro)
    # the smallest fixes proposed in math.md, checked with the same tests
    yield 'tetrahedron (proposed fix: PS solid)', macro_body('tetra').replace(
        '\\draw[dashed,gray] (0,0)--(1.65,1);', '\\draw (0,0)--(1.65,1);')
    yield 'octahedron (proposed fix: front (1,1.15), back (1.8,2.05))', macro_body('octa').replace(
        '(1.4,1.15)', '(1,1.15)').replace('(1.4,2.1)', '(1.8,2.05)')


R.out('')
R.out('== Model icons (p.1 table, p.5 pyramid), then the proposed fixes ==')
for name, body in icon_bodies():
    segs = parse_paths(body)
    vs = sorted({p for a, b, _ in segs for p in (a, b)})
    style = {}
    for a, b, s in segs:
        k = frozenset((a, b))
        style[k] = 'solid' if style.get(k) == 'solid' or s == 'solid' else 'dashed'
    es = [tuple(k) for k in style]
    iso = graph_iso(vs, es, name.split(' (')[0])
    R.check(iso, f'{name} icon: {len(vs)} drawn vertices, {len(es)} drawn edges ({sum(1 for v in style.values() if v=="dashed")} dashed) form the {name} graph')
    sil = hull2d(vs)
    interior = [v for v in vs if v not in sil]
    mixed = []
    for v in interior:
        st = {style[k] for k in style if v in k}
        if len(st) > 1:
            mixed.append((v, {tuple(sorted(k - {v}))[0]: style[k] for k in style if v in k}))
    R.check(not mixed, f'{name} icon: every vertex inside the outline has all its edges solid or all dashed'
            + (f' -- MIXED at {mixed}' if mixed else ''))
    hidden_under = []
    for v in vs:
        for k in style:
            a, b = tuple(k)
            if v not in k and on_segment_interior(v, a, b):
                hidden_under.append((v, (a, b), style[k]))
    overl = []
    for k1, k2 in itertools.combinations(style, 2):
        a, b = tuple(k1); c, d = tuple(k2)
        if (on_segment_interior(c, a, b) or on_segment_interior(d, a, b) or on_segment_interior(a, c, d)
                or on_segment_interior(b, c, d)):
            # collinear and overlapping?
            def cr(p, q, r):
                return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
            if abs(cr(a, b, c)) < 1e-9 and abs(cr(a, b, d)) < 1e-9:
                overl.append(((a, b), style[k1], (c, d), style[k2]))
    R.check(not hidden_under and not overl, f'{name} icon: no vertex drawn in the middle of another edge and no two edges drawn on top of each other'
            + (f' -- vertex-on-edge {hidden_under}; overlapping {overl}' if (hidden_under or overl) else ''))

# ---------------------------------------------------------------- regular shapes


def tri_equilateral(p):
    d = [math.dist(p[i], p[(i + 1) % 3]) for i in range(3)]
    return max(d) - min(d) < 2e-3 * max(d), d


R.out('')
R.out('== Regular shapes in worked visuals and problem diagrams (all tikzpictures use equal x/y units) ==')
R.check(not re.search(r'x=([\d.]+)cm,y=(?!\1)', TEX), 'every tikzpicture with x=..,y=.. uses equal x and y units')
tris = {
    'p.2 separate triangles': [[(0, 0), (1.3, 0), (.65, 1.1258)], [(1.6, 0), (2.9, 0), (2.25, 1.1258)]],
    'p.2 joined pair': [[(4.6, 0), (5.9, 0), (5.25, 1.1258)], [(5.9, 0), (6.55, 1.1258), (5.25, 1.1258)]],
    'p.3 loose corners': [[(-.8, 0), (.1, 0), (-.35, .7794)], [(.35, 0), (1.25, 0), (.8, .7794)]],
    'p.3/p.4 fan in circle': [[(0, 0), (1, 0), (.5, .866)], [(0, 0), (.5, .866), (-.5, .866)]],
    'p.4 loose corners': [[(-.8, 0), (.2, 0), (-.3, .866)], [(.45, 0), (1.45, 0), (.95, .866)]],
    'p.5 faces': [[(x, 0), (x + 1, 0), (x + .5, .866)] for x in (1.6, 2.95, 4.3, 5.65)],
}
for k, lst in tris.items():
    R.check(all(tri_equilateral(t)[0] for t in lst), f'{k}: {len(lst)} triangle(s) equilateral')
# the p.2 joined pair shares a whole side
R.check({(5.9, 0), (5.25, 1.1258)} <= set(tris['p.2 joined pair'][0]) & set(tris['p.2 joined pair'][1]),
        'p.2 joined pair shares the thick side (5.9,0)-(5.25,1.1258) and its two endpoint dots')
# make sure these coordinates are the ones in the source
for frag in ['(0,0)--(1.3,0)--(.65,1.1258)', '(5.9,0)--(6.55,1.1258)--(5.25,1.1258)', '(-.8,0)--(.1,0)--(-.35,.7794)',
             '(0,0)--(1,0)--(.5,.866)', '(0,0)--(.5,.866)--(-.5,.866)', '(-.8,0)--(.2,0)--(-.3,.866)',
             '(\\x,0)--++(1,0)--++(-.5,.866)', 'arc (120:360:1.08)']:
    R.check(frag in TEX, f'source contains {frag}')
R.check(TEX.count('arc (120:360:1.08)') == 2, 'pp.3-4 gap arcs run 120..360 = 240 degrees, matching "gap = 240" and two 60-degree corners')
# squares p.1 conventions and p.5
R.check('(0,0) rectangle (1.1,1.1)' in TEX and '(1.45,0) rectangle (2.55,1.1)' in TEX and '(0,0) rectangle (1,1)' in TEX,
        'p.1 face-side squares and p.5 square face are squares')
# Problem 9 pentagon
pent = [(0, 0), (.9, 0), (1.178115, .855951), (.45, 1.384957), (-.278115, .855951)]
R.check('(0,0)--(.9,0)--(1.178115,.855951)--(.45,1.384957)--(-.278115,.855951)' in TEX, 'p.9 pentagon coordinates read from source')
sides = [math.dist(pent[i], pent[(i + 1) % 5]) for i in range(5)]
angs = []
for i in range(5):
    u, v, w = pent[i - 1], pent[i], pent[(i + 1) % 5]
    a = (u[0] - v[0], u[1] - v[1]); b = (w[0] - v[0], w[1] - v[1])
    angs.append(math.degrees(math.acos((a[0] * b[0] + a[1] * b[1]) / (math.hypot(*a) * math.hypot(*b)))))
R.check(max(sides) - min(sides) < 1e-5 and all(abs(x - 108) < 1e-3 for x in angs),
        f'p.9 pentagon regular: sides {[round(s, 5) for s in sides]}, angles {[round(x, 3) for x in angs]}')
R.check('\\foreach \\a in {0,108,216}' in TEX, 'p.9 three pentagons rotated by 0,108,216: corners fill 0..324, gap 36')
far = max(math.hypot(*p) for p in pent)
R.check(far < 1.5, f'p.9 pentagons fit inside their r=1.5 circle (farthest corner {far:.3f})')
R.check('\\foreach \\a in {0,60,120,180,240}{\\draw[fill=blue!10] (0,0)--(\\a:1.5)--(\\a+60:1.5)--cycle;}' in TEX,
        'p.9 five triangles 0..300 with equal radii 1.5 (equilateral), gap 60')
R.check('\\foreach \\i in {0,...,4}{\\coordinate (P\\i) at (90+72*\\i:1.4);}' in TEX and '(P0)--(P2) (P0)--(P3)' in TEX,
        'p.8 regular pentagon split from one corner by two diagonals into three triangles')

# ---------------------------------------------------------------- P6 and P7 drawings
R.out('')
R.out('== Problem 6 and Problem 7 drawings ==')
R.check('(0,0) rectangle (2.7,2.7);\\draw[very thick] (0,0)--(2.7,2.7)' in TEX, 'P6 diagonal: corner to opposite corner of a 2.7 square')
R.check('\\foreach \\p in {(4,0),(6.7,0),(6.7,2.7),(4,2.7)}{\\draw[very thick] \\p --(5.35,1.35);}' in TEX
        and abs(5.35 - (4 + 6.7) / 2) < 1e-9 and abs(1.35 - 2.7 / 2) < 1e-9,
        'P6 centre: dot (5.35,1.35) is the square centre, joined to all four corners')
R.check('(10.3,1.35) circle' in TEX and abs(1.35 - 2.7 / 2) < 1e-9, 'P6 edge vertex: dot at the midpoint of the shared edge x=10.3, 0..2.7')
R.check(TEX.count('{(0,0),(4.5,0),(4.5,4.5),(0,4.5),(1.4,1.4),(3.1,1.4),(3.1,3.1),(1.4,3.1)}') == 2,
        'P7 opened cube and its extra workspace mark the same 8 dots')

# ---------------------------------------------------------------- materials fan pieces (source)
R.out('')
R.out('== Materials pp.3-4 fan pieces (source materials.tex) ==')
MT = open(os.path.join(SRC, 'student', 'materials.tex')).read()
R.check('(\\x,\\y)--++(30,0)--++(-15,25.980762)--cycle' in MT and abs(math.hypot(15, 25.980762) - 30) < 1e-5,
        'fan triangles: 30 mm equilateral (sides 30, 30, %.5f)' % math.hypot(15, 25.980762))
R.check('\\foreach \\x in {0,39,78,117}{\\foreach \\y in {0,37}' in MT and 37 > 25.980762 and 39 > 30,
        'eight triangles on a 39 x 37 mm grid: no overlaps')
R.check('(\\x,\\y) rectangle ++(30,30)' in MT and '\\foreach \\y in {0,41}' in MT, 'eight 30 mm squares on a 39 x 41 mm grid: no overlaps')
R.check(MT.count('circle (40)') == 2, 'two circles of radius 40 mm (80 mm across)')

# ---------------------------------------------------------------- materials scale
R.out('')
R.out('== Delivered materials PDF scale (254 dpi = 10 px/mm) ==')
try:
    from PIL import Image
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-r', '254', '-gray', '-f', '4', '-l', '4', '-png', MATERIALS_PDF, os.path.join(td, 'm')], check=True)
        subprocess.run(['pdftoppm', '-r', '254', '-gray', '-f', '1', '-l', '1', '-png', MATERIALS_PDF, os.path.join(td, 'm')], check=True)
        files = sorted(os.listdir(td))
        im4 = Image.open(os.path.join(td, [f for f in files if f.endswith('4.png')][0])).convert('L')
        im1 = Image.open(os.path.join(td, [f for f in files if f.endswith('1.png')][0])).convert('L')
        w, h = im4.size
        px = im4.load()
        # circles: find rows of the two centre dots (dark blobs) in the lower half
        best = None
        for y in range(h // 2, h - 300):
            row = [x for x in range(w) if px[x, y] < 128]
            if len(row) >= 4:
                # candidate horizontal chord; the diameter is the longest chord of the left circle
                xs = [x for x in row if x < w // 2]
                if len(xs) >= 2:
                    span = max(xs) - min(xs)
                    if best is None or span > best[0]:
                        best = (span, y)
        diam_mm = best[0] / 10
        R.check(abs(diam_mm - 80) < 0.6, f'left full-turn circle measures {diam_mm:.1f} mm across (outer edge to outer edge; stated 80 mm)')
        # 30 mm bar on p.1: longest dark horizontal run in the top fifth
        px1 = im1.load(); w1, h1 = im1.size
        longest = 0
        for y in range(int(h1 * 0.12), int(h1 * 0.2)):
            run = 0
            for x in range(w1):
                if px1[x, y] < 128:
                    run += 1; longest = max(longest, run)
                else:
                    run = 0
        R.check(abs(longest / 10 - 30) < 0.6, f'30 mm check bar measures {longest/10:.1f} mm')
except ImportError:
    R.out('PIL not available; scale check skipped')
R.finish()
