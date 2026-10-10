"""Independent check of the five Week 56 paper nets (materials pp.1-3).

Written for this review; nothing is imported from make_assets.py, verify.py,
audit_math.py or check_answers.py.  For each *-net.tex in the editable source
it parses the TikZ (faces, tabs, dashed folds, solid cuts, letter, face and
blue corner labels) and checks:
  * every face is a regular polygon with 30 mm sides (equal x/y scaling);
  * the in-net fold edges form a spanning tree of the faces, and no two faces,
    tabs or face/tab pairs overlap on the sheet;
  * each face corner carries exactly one blue label, and both sides of every
    fold carry the same two labels;
  * every cut edge carries a letter; each letter occurs on exactly two cut
    edges with the same pair of corner labels, exactly one of which has a tab;
  * the glued label complex is a closed oriented surface (each edge in two
    faces, traversed once each way, each vertex star one cycle) and is
    isomorphic, face by face and with matching face sizes, to the convex
    hull of the intended solid;
  * the delivered materials PDF prints the same labels at the same relative
    positions as the source (pdftotext -bbox).
Run: python3 check_nets.py   (writes out_check_nets.txt beside itself)
"""
import itertools
import math
import os
import re
import subprocess
from collections import defaultdict, Counter

import sys
sys.dont_write_bytecode = True  # keep the check folder free of __pycache__
from common56 import (HERE, SRC, MATERIALS_PDF, Report, convex_hull, solid)

R = Report(os.path.join(HERE, 'out_check_nets.txt'))
NUM = r'(-?\d+(?:\.\d+)?)'
PT = re.compile(r'\(' + NUM + ',' + NUM + r'\)')

NETS = [
    ('cube-net.tex', 'cube', 1),
    ('tetrahedron-net.tex', 'tetrahedron', 1),
    ('octahedron-net.tex', 'octahedron', 2),
    ('triangular-prism-net.tex', 'triangular prism', 2),
    ('square-pyramid-net.tex', 'square pyramid', 3),
]


def pts(s):
    return [(float(a), float(b)) for a, b in PT.findall(s)]


def key(p):
    return (round(p[0], 3), round(p[1], 3))


def parse(path):
    faces, tabs, dashed, solid_lines, letters, facenums, corners = [], [], [], [], [], [], []
    for line in open(path):
        line = line.strip()
        if line.startswith('\\fill[blue!5]'):
            faces.append(pts(line))
        elif line.startswith('\\fill[gray!17]'):
            tabs.append(pts(line))
        elif line.startswith('\\draw[dashed]'):
            dashed.append(pts(line))
        elif line.startswith('\\draw '):
            solid_lines.append(pts(line))
        elif line.startswith('\\node[fill=white'):
            m = re.search(r'at ' + r'\(' + NUM + ',' + NUM + r'\) \{(\w)\}', line)
            letters.append(((float(m.group(1)), float(m.group(2))), m.group(3)))
        elif line.startswith('\\node[font=\\sffamily\\small]'):
            m = re.search(r'at \(' + NUM + ',' + NUM + r'\) \{(\d+)\}', line)
            facenums.append(((float(m.group(1)), float(m.group(2))), int(m.group(3))))
        elif line.startswith('\\node[text=blue'):
            m = re.search(r'at \(' + NUM + ',' + NUM + r'\) \{(\d+)\}', line)
            corners.append(((float(m.group(1)), float(m.group(2))), int(m.group(3))))
    return faces, tabs, dashed, solid_lines, letters, facenums, corners


def inside(p, poly):
    # strict point-in-convex-polygon (poly CCW or CW)
    s = []
    for a, b in zip(poly, poly[1:] + poly[:1]):
        s.append((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]))
    return all(x > 1e-9 for x in s) or all(x < -1e-9 for x in s)


def signed_area(poly):
    return sum(a[0] * b[1] - a[1] * b[0] for a, b in zip(poly, poly[1:] + poly[:1])) / 2


def clip(subject, clipper):
    """Sutherland-Hodgman; clipper must be convex and CCW."""
    out = list(subject)
    for a, b in zip(clipper, clipper[1:] + clipper[:1]):
        inp, out = out, []
        if not inp:
            break
        def side(p):
            return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        prev = inp[-1]
        for cur in inp:
            sc, sp = side(cur), side(prev)
            if (sc >= 0) != (sp >= 0):
                t = sp / (sp - sc)
                out.append((prev[0] + t * (cur[0] - prev[0]), prev[1] + t * (cur[1] - prev[1])))
            if sc >= 0:
                out.append(cur)
            prev = cur
    return out


def overlap_area(p, q):
    if signed_area(q) < 0:
        q = q[::-1]
    c = clip(p, q)
    return abs(signed_area(c)) if len(c) >= 3 else 0.0


def seg_dist(p, a, b):
    ax, ay = b[0] - a[0], b[1] - a[1]
    t = max(0, min(1, ((p[0] - a[0]) * ax + (p[1] - a[1]) * ay) / (ax * ax + ay * ay)))
    return math.hypot(p[0] - a[0] - t * ax, p[1] - a[1] - t * ay)


def pdf_words(page):
    xml = subprocess.run(['pdftotext', '-bbox', '-f', str(page), '-l', str(page), MATERIALS_PDF, '-'],
                         check=True, capture_output=True, text=True).stdout
    words = []
    for m in re.finditer(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', xml):
        x0, y0, x1, y1 = map(float, m.groups()[:4])
        words.append(((x0 + x1) / 2, (y0 + y1) / 2, y1 - y0, m.group(5)))
    return words


summary = []
for fname, solid_name, page in NETS:
    R.out('')
    R.out('=' * 70)
    R.out(f'{fname}  ->  {solid_name}  (materials p.{page})')
    faces, tabs, dashed, solids, letters, facenums, corners = parse(os.path.join(SRC, 'student', fname))
    F = len(faces)

    # 1. regular faces, 30 mm
    reg_ok = True
    for i, f in enumerate(faces):
        n = len(f)
        sides = [math.dist(a, b) for a, b in zip(f, f[1:] + f[:1])]
        angs = []
        for t in range(n):
            u, v, w = f[t - 1], f[t], f[(t + 1) % n]
            a = (u[0] - v[0], u[1] - v[1]); b = (w[0] - v[0], w[1] - v[1])
            angs.append(math.degrees(math.acos((a[0] * b[0] + a[1] * b[1]) / (math.hypot(*a) * math.hypot(*b)))))
        target = 180 * (n - 2) / n
        if not (all(abs(s - 30) < 0.01 for s in sides) and all(abs(x - target) < 0.05 for x in angs)):
            reg_ok = False
            R.out('   face', i + 1, 'sides', [round(s, 3) for s in sides], 'angles', [round(x, 2) for x in angs])
    R.check(reg_ok, f'all {F} faces are regular polygons with 30 mm sides')

    # 2. face numbers: one per face, inside it
    fn = {}
    for p, num in facenums:
        hit = [i for i, f in enumerate(faces) if inside(p, f)]
        if len(hit) == 1:
            fn[hit[0]] = num
    R.check(sorted(fn.values()) == list(range(1, F + 1)) and len(fn) == F,
            f'face numbers 1..{F}, one inside each face')

    # 3. corner labels
    face_labels = []
    corner_ok = True
    used = Counter()
    for i, f in enumerate(faces):
        labs = []
        for v in f:
            cand = [(math.dist(p, v), lab, idx) for idx, (p, lab) in enumerate(corners)
                    if inside(p, f) and math.dist(p, v) < 6]
            cand.sort()
            if len(cand) != 1:
                corner_ok = False
                R.out('   face', i + 1, 'corner', v, 'candidates', cand)
                labs.append(None)
                continue
            labs.append(cand[0][1]); used[cand[0][2]] += 1
        face_labels.append(labs)
    corner_ok = corner_ok and len(used) == len(corners) and all(c == 1 for c in used.values())
    R.check(corner_ok, 'every face corner has exactly one blue label inside its face; every label used once')
    for i, labs in enumerate(face_labels):
        R.out(f'   face {fn.get(i)}: corner labels {labs}')
    R.check(all(len(set(l)) == len(l) for l in face_labels), 'no face repeats a corner label')

    # 4. net edges: shared (fold) versus boundary
    edge_faces = defaultdict(list)
    for i, f in enumerate(faces):
        for t in range(len(f)):
            a, b = f[t], f[(t + 1) % len(f)]
            edge_faces[frozenset((key(a), key(b)))].append((i, t))
    folds = {e: v for e, v in edge_faces.items() if len(v) == 2}
    bound = {e: v[0] for e, v in edge_faces.items() if len(v) == 1}
    R.check(all(len(v) <= 2 for v in edge_faces.values()), 'no net segment belongs to three faces')
    dashed_set = {frozenset((key(s[0]), key(s[1]))) for s in dashed}
    R.check(all(e in dashed_set for e in folds), f'all {len(folds)} in-net shared edges are drawn dashed')
    # spanning tree of faces
    parent = list(range(F))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for e, ((i, _), (j, _)) in folds.items():
        parent[find(i)] = find(j)
    R.check(len(folds) == F - 1 and len({find(i) for i in range(F)}) == 1,
            f'fold edges ({len(folds)}) form a spanning tree of the {F} faces')
    fold_ok = True
    for e, ((i, ti), (j, tj)) in folds.items():
        fi, fj = faces[i], faces[j]
        la = {key(fi[ti]): face_labels[i][ti], key(fi[(ti + 1) % len(fi)]): face_labels[i][(ti + 1) % len(fi)]}
        lb = {key(fj[tj]): face_labels[j][tj], key(fj[(tj + 1) % len(fj)]): face_labels[j][(tj + 1) % len(fj)]}
        if la != lb:
            fold_ok = False
            R.out('   fold mismatch', la, lb)
    R.check(fold_ok, 'both sides of every fold carry the same two corner labels')

    # 5. tabs
    tab_edge = {}
    tab_ok = True
    for t in tabs:
        tk = [key(p) for p in t]
        hits = [e for e in bound if all(any(math.dist(q, p) < 1e-3 for p in t) for q in e)]
        if len(hits) != 1:
            tab_ok = False
            continue
        tab_edge[hits[0]] = t
    R.check(tab_ok and len(tab_edge) == len(tabs), f'each of the {len(tabs)} tabs hinges on one cut face edge')

    # 6. letters on boundary edges
    letter_of = {}
    let_ok = True
    for p, L in letters:
        cand = sorted((seg_dist(p, e_pts[0], e_pts[1]), e) for e in bound
                      for e_pts in [list(e)])
        d, e = cand[0]
        if d > 3.6 or (len(cand) > 1 and cand[1][0] - d < 0.5):
            let_ok = False
            R.out('   ambiguous letter', L, p, cand[:2])
        if e in letter_of:
            let_ok = False
        letter_of[e] = L
    R.check(let_ok and set(letter_of) == set(bound), f'every one of the {len(bound)} cut edges carries exactly one letter')
    by_letter = defaultdict(list)
    for e, L in letter_of.items():
        i, t = bound[e]
        f = faces[i]
        by_letter[L].append((e, frozenset((face_labels[i][t], face_labels[i][(t + 1) % len(f)]))))
    pair_ok = True
    for L, items in sorted(by_letter.items()):
        ntab = sum(1 for e, _ in items if e in tab_edge)
        good = len(items) == 2 and items[0][1] == items[1][1] and ntab == 1
        pair_ok &= good
        R.out(f'   letter {L}: corner pairs {[sorted(x[1]) for x in items]}, tabs {ntab}' + ('' if good else '  <-- problem'))
    R.check(pair_ok, f'{len(by_letter)} letters: each on two cut edges joining the same corner labels, one tab per letter')

    # 7. overlaps
    ov = []
    polys = [(f'face {fn.get(i)}', f) for i, f in enumerate(faces)] + [(f'tab {k}', t) for k, t in enumerate(tabs)]
    for (na, a), (nb, b) in itertools.combinations(polys, 2):
        if overlap_area(a, b) > 1e-3:
            ov.append((na, nb, round(overlap_area(a, b), 3)))
    R.check(not ov, 'no two faces/tabs overlap on the printed sheet' + (f' {ov}' if ov else ''))

    # 8. glued complex
    cycles = []
    for i, f in enumerate(faces):
        labs = face_labels[i]
        if signed_area(f) < 0:
            labs = labs[::-1]
        cycles.append(labs)
    dir_edges = Counter()
    und = defaultdict(int)
    for c in cycles:
        for a, b in zip(c, c[1:] + c[:1]):
            dir_edges[(a, b)] += 1
            und[frozenset((a, b))] += 1
    V = len({v for c in cycles for v in c}); E = len(und)
    R.check(all(x == 2 for x in und.values()), 'every glued edge lies in exactly two faces')
    R.check(all(dir_edges[(a, b)] == 1 and dir_edges[(b, a)] == 1 for (a, b) in dir_edges),
            'the two copies of every glued edge run in opposite directions (consistent orientation)')
    link_ok = True
    for v in {v for c in cycles for v in c}:
        # star of v: faces around v linked through shared edges
        nbr = []
        for c in cycles:
            if v in c:
                k = c.index(v)
                nbr.append((c[k - 1], c[(k + 1) % len(c)]))
        # follow the cycle
        succ = {a: b for a, b in nbr}
        start = nbr[0][0]; x = start; steps = 0
        while True:
            x = succ.get(x)
            steps += 1
            if x is None or steps > len(nbr):
                break
            if x == start:
                break
        if x != start or steps != len(nbr):
            link_ok = False
    R.check(link_ok, 'the faces around every vertex form a single cycle (closed surface)')

    P = solid(solid_name)
    hf, he = convex_hull(P)
    R.out(f'   net glues to V,E,F = {V},{E},{F}; hull of {solid_name}: {len(P)},{len(he)},{len(hf)}')
    # isomorphism by brute force over vertex relabellings
    hull_faces = {frozenset(f): len(f) for f in hf}
    labs = sorted({v for c in cycles for v in c})
    iso = None
    if V == len(P):
        for perm in itertools.permutations(range(V)):
            m = dict(zip(labs, perm))
            if all(frozenset(m[v] for v in c) in hull_faces for c in cycles):
                iso = m
                break
    R.check(iso is not None and F == len(hf) and E == len(he),
            f'glued net is isomorphic face-by-face to the {solid_name}')
    # face size per matched face, and vertex configurations
    conf = Counter(tuple(sorted(len(c) for c in cycles if v in c)) for v in labs)
    R.out(f'   vertex configurations (face sizes at a vertex): {dict(conf)}')

    # 9. delivered PDF labels match the source positions
    words = pdf_words(page)
    k = 72 / 25.4
    nodes = [(p, str(L)) for p, L in letters] + [(p, str(n)) for p, n in facenums] + [(p, str(n)) for p, n in corners]
    # fit translation with the face-number nodes (unique on the page per net size class)
    best = None
    single = [w for w in words if re.fullmatch(r'[A-G0-9]', w[3])]
    for w in single:
        p0, t0 = facenums[0]
        if w[3] != str(t0):
            continue
        ox, oy = w[0] - p0[0] * k, w[1] + p0[1] * k
        hits = 0
        for p, t in nodes:
            x, y = ox + p[0] * k, oy - p[1] * k
            if any(abs(x - q[0]) < 1.2 and abs(y - q[1]) < 1.6 and q[3] == t for q in single):
                hits += 1
        if best is None or hits > best[0]:
            best = (hits, ox, oy)
    R.check(best is not None and best[0] == len(nodes),
            f'materials PDF p.{page}: all {len(nodes)} source labels found at their source positions ({best[0] if best else 0} matched)')
    summary.append((solid_name, V, E, F, len(tabs), len(by_letter)))

R.out('')
R.out('Summary (solid, V, E, F, tabs, seam letters):')
for s in summary:
    R.out('  ', s)
R.check(sum(s[4] for s in summary) == 24, 'one five-model set has 24 tabbed closing seams (guide: 72 for three sets)')
R.check(sum(s[3] for s in summary) == 28, 'one five-model set has 28 faces (guide: 84 for 15 models)')
R.finish()
