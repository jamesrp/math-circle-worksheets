#!/usr/bin/env python3
"""Independent check of materials.pdf, read from the finished PDF only.

Checks every page's header, footer, 10 cm scale line and print counts; that the
net's solid and dashed lines bound four equilateral faces of edge 90 mm joined as
a tetrahedron net, with exactly one tab on each of the three seams; that each
letter cap is three equilateral triangles round one point (so it wraps a corner,
whose three face angles are 60 degrees) with the letter on all three; that the
caps share straight cut lines; that the cap letters A, A, B, B, C, C, D on one
model can build every labelling the student pages ask for; and that each pose
mat footprint is a model face with its corners named.
Writes materials-checks.json beside materials.pdf.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math
import re
import sys

import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'materials.pdf'
MM = 72 / 25.4
TOL = 0.3 * MM
checks = []


def ok(name, cond, detail=''):
    checks.append({'check': name, 'pass': bool(cond), 'detail': str(detail)})
    if not cond:
        print('FAIL', name, detail)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def same(a, b, tol=TOL):
    return dist(a, b) < tol


def segments(page):
    """All straight segments as (p, q, dashed, closed_path_id)."""
    out = []
    for k, d in enumerate(page.get_drawings()):
        dashed = d.get('dashes') not in (None, '[] 0', '[] 0.0')
        for it in d['items']:
            if it[0] == 'l':
                out.append(((it[1].x, it[1].y), (it[2].x, it[2].y), dashed, k))
            elif it[0] == 're':
                r = it[1]
                pts = [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
                for i in range(4):
                    out.append((pts[i], pts[(i + 1) % 4], dashed, k))
    return out


def words(page):
    return [(w[4], ((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)) for w in page.get_text('words')]


def counts_line(text):
    m = re.search(r'Print on (card stock|copy paper), at 100%: (.*?)\.', text.replace('\n', ' '))
    if not m:
        return None, None
    found = dict(re.findall(r'(K–1|Grades 2–3|Grades 4–5|adults) (\d+)', m.group(2)))
    return m.group(1), tuple(int(found.get(t, 0)) for t in ('K–1', 'Grades 2–3', 'Grades 4–5', 'adults'))


doc = fitz.open(PDF)
ok('three pages', len(doc) == 3, len(doc))
GROUP = (4, 4, 3)                     # worksheet-workflow/context.md: eleven children
pages = {}
for i, page in enumerate(doc, 1):
    text = page.get_text()
    ok(f'p{i} US Letter', (round(page.rect.width), round(page.rect.height)) == (612, 792), page.rect)
    ok(f'p{i} header', text.startswith('Week 37 / Mirror twins / Materials'), text[:40])
    ok(f'p{i} footer', 'Bellingham Math Circle / Week 37 / W37-M-v1 / physically unrehearsed' in text)
    segs = segments(page)
    scale = [s for s in segs if abs(s[0][1] - s[1][1]) < .01 and abs(dist(s[0], s[1]) - 100 * MM) < .05]
    ok(f'p{i} 10 cm scale line', len(scale) == 1 and '10 cm check' in text,
       [round(dist(s[0], s[1]) / MM, 3) for s in scale])
    paper, counts = counts_line(text)
    pages[i] = (page, text, segs, paper, counts)

# ---- page 1: the net ------------------------------------------------------
page, text, segs, paper, nets = pages[1]
ok('net on card stock', paper == 'card stock', paper)
ok('one model per child at each table, two for adults', nets is not None and nets[:3] == GROUP and nets[3] >= 2, nets)
body = [s for s in segs if not (abs(s[0][1] - s[1][1]) < .01 and abs(dist(s[0], s[1]) - 100 * MM) < .05)
        and min(s[0][1], s[1][1]) > 120 and max(s[0][1], s[1][1]) < 715]   # between heading and scale line
dashed = [s for s in body if s[2]]
solid = [s for s in body if not s[2]]
edges90 = [s for s in body if abs(dist(s[0], s[1]) - 90 * MM) < TOL]
ok('six dashed fold lines, all 90 mm', len(dashed) == 6 and all(abs(dist(s[0], s[1]) - 90 * MM) < TOL for s in dashed),
   [round(dist(s[0], s[1]) / MM, 2) for s in dashed])
ok('nine 90 mm edges in all', len(edges90) == 9, len(edges90))


def key(p):
    return (round(p[0], 1), round(p[1], 1))


verts = []
for s in edges90:
    for p in s[:2]:
        if not any(same(p, v) for v in verts):
            verts.append(p)


def vid(p):
    return next(k for k, v in enumerate(verts) if same(p, v))


E = {frozenset((vid(s[0]), vid(s[1]))): s for s in edges90}
tris = [t for t in combinations(range(len(verts)), 3)
        if all(frozenset(e) in E for e in combinations(t, 2))]
ok('four faces', len(tris) == 4, tris)
for t in tris:
    sides = [dist(verts[a], verts[b]) / MM for a, b in combinations(t, 2)]
    ok(f'face {t} equilateral, 90 mm', all(abs(x - 90) < .3 for x in sides), [round(x, 2) for x in sides])
centre = [t for t in tris if all(len(set(t) & set(u)) == 2 for u in tris if u != t)]
ok('one central face sharing an edge with each other face', len(centre) == 1, centre)
outer = [e for e in E if sum(e <= set(t) for t in tris) == 1]
ok('six outer half-sides', len(outer) == 6, len(outer))
# Folding closes the net: two outer half-sides of different corner faces that share
# an end form one seam of the tetrahedron.
corner_faces = [t for t in tris if t not in centre]
seams = []
for e, f in combinations(outer, 2):
    fe = [t for t in corner_faces if e <= set(t)]
    ff = [t for t in corner_faces if f <= set(t)]
    if e & f and fe and ff and fe != ff:
        seams.append((e, f))
ok('three seams', len(seams) == 3, len(seams))
cut_outline = [s for s in solid if abs(dist(s[0], s[1]) - 90 * MM) >= TOL]
for e, f in seams:
    tabbed = []
    for half in (e, f):
        a, b = (verts[k] for k in half)
        if not E[half][2]:          # a cut edge, not a fold: no tab
            continue
        ux, uy = (b[0] - a[0]) / dist(a, b), (b[1] - a[1]) / dist(a, b)
        face = next(t for t in tris if half <= set(t))
        apex = verts[next(k for k in face if k not in half)]

        def off(p):
            return (p[0] - a[0]) * uy - (p[1] - a[1]) * ux

        def along(p):
            return (p[0] - a[0]) * ux + (p[1] - a[1]) * uy
        # a tab: a cut segment parallel to the fold, outside the face, joined to both ends of the fold
        for f1, f2, *_ in cut_outline:
            if abs(off(f1) - off(f2)) > .5 or off(f1) * off(apex) >= 0:
                continue
            if not (0 < along(f1) < dist(a, b) and 0 < along(f2) < dist(a, b)):
                continue
            joined = all(any((same(s[0], end) and (same(s[1], f1) or same(s[1], f2)))
                             or (same(s[1], end) and (same(s[0], f1) or same(s[0], f2))) for s in cut_outline)
                         for end in (a, b))
            if joined:
                tabbed.append((half, [abs(off(f1)) / MM, abs(off(f2)) / MM], True))
    ok(f'seam {sorted(map(sorted, (e, f)))} has exactly one tab', len(tabbed) == 1, tabbed)
    if tabbed:
        ok('tab 9 mm deep, outside its face', all(abs(x - 9) < .3 for x in tabbed[0][1]) and tabbed[0][2], tabbed[0])
ok('net fits inside the page margins', all(28 < p[0] < 584 and 70 < p[1] < 722 for s in body for p in s[:2]))
ok('net tells how to close it', 'tape each of the three open edges' in text.replace('\n', ' '))

# ---- page 2: letter caps --------------------------------------------------
page, text, segs, paper, caps_sheets = pages[2]
ok('caps on card stock', paper == 'card stock', paper)
CAP = 26 * MM
quads = {}
for s in segs:
    if s[3] not in quads:
        quads[s[3]] = []
    quads[s[3]].append(s)
caps = []
for k, ss in quads.items():
    if len(ss) != 4 or ss[0][2]:
        continue
    pts = [s[0] for s in ss]
    lens = sorted(dist(s[0], s[1]) for s in ss)
    if abs(lens[-1] - 2 * CAP) < TOL and all(abs(x - CAP) < TOL for x in lens[:3]):
        long = max(ss, key=lambda s: dist(s[0], s[1]))
        o = ((long[0][0] + long[1][0]) / 2, (long[0][1] + long[1][1]) / 2)
        short = [p for p in pts if not (same(p, long[0]) or same(p, long[1]))]
        caps.append({'o': o, 'long': long, 'short': short, 'pts': pts})
ok('28 caps of three 26 mm triangles', len(caps) == 28, len(caps))
dash = [s for s in segs if s[2]]
w2 = words(page)
letters = Counter()
for c in caps:
    o = c['o']
    folds = [s for s in dash if (same(s[0], o) and any(same(s[1], q) for q in c['short']))
             or (same(s[1], o) and any(same(s[0], q) for q in c['short']))]
    ok('cap: two dashed folds from the corner point, 26 mm', len(folds) == 2
       and all(abs(dist(s[0], s[1]) - CAP) < TOL for s in folds), len(folds))
    # three triangles, each equilateral, so three 60-degree angles meet at o: a tetrahedron corner
    corners = [c['long'][0], c['short'][0], c['short'][1], c['long'][1]]
    corners = sorted(corners, key=lambda p: math.atan2(p[1] - o[1], p[0] - o[0]))
    angs = []
    for p in corners:
        angs.append(math.degrees(math.atan2(p[1] - o[1], p[0] - o[0])) % 360)
    tri_ok = all(abs(dist(o, p) - CAP) < TOL for p in corners)
    ok('cap: all four outer points 26 mm from the corner point', tri_ok)
    ok('cap: face angles 60, 60, 60 at the corner point, total 180 (a tetrahedron corner)',
       abs(dist(c['short'][0], c['short'][1]) - CAP) < TOL
       and all(abs(dist(c['short'][j], c['long'][m]) - CAP) < TOL or abs(dist(c['short'][j], c['long'][m]) - CAP * math.sqrt(3)) < TOL
               for j in (0, 1) for m in (0, 1)))
    inside = []
    mid = ((c['short'][0][0] + c['short'][1][0]) / 2, (c['short'][0][1] + c['short'][1][1]) / 2)
    for wtxt, (x, y) in w2:
        on_cap_side = (x - o[0]) * (mid[0] - o[0]) + (y - o[1]) * (mid[1] - o[1]) > 0
        if wtxt in 'ABCD' and len(wtxt) == 1 and dist((x, y), o) < CAP and on_cap_side:
            # which of the three triangles?
            ang = math.degrees(math.atan2(y - o[1], x - o[0]))
            inside.append((wtxt, ang))
    labs = {t for t, _ in inside}
    sectors = sorted(round(((a % 360) // 60)) for _, a in inside)
    ok('cap: one letter in each of its three triangles', len(inside) == 3 and len(labs) == 1
       and len(set(sectors)) == 3, inside)
    if len(labs) == 1:
        letters[labs.pop()] += 1
ok('8 A, 8 B, 8 C, 4 D caps per sheet', letters == Counter({'A': 8, 'B': 8, 'C': 8, 'D': 4}), dict(letters))
# straight cut lines: caps in a row share their slanted sides and both long edges are straight lines
rows = {}
for c in caps:
    ys = sorted({round(p[1], 1) for p in c['pts']})
    rows.setdefault(tuple(ys), []).append(c)
ok('seven rows of four caps', len(rows) == 7 and all(len(r) == 4 for r in rows.values()), [len(r) for r in rows.values()])
for ys, row in rows.items():
    row.sort(key=lambda c: c['o'][0])
    shared = 0
    for a, b in zip(row, row[1:]):
        pa = {key(p) for p in a['pts']}
        pb = {key(p) for p in b['pts']}
        shared += len(pa & pb) == 2
    ok(f'row at y={ys}: neighbours share a slanted cut, long edges on two straight lines',
       shared == 3 and len(ys) == 2, (shared, ys))
# every problem's labelling can be built from one model's caps
KIT = Counter('AABBCCD')
need = {
    'K-1 P1, 2-3 P1, 4-5 P1: A, B, C, D': ['ABCD'],
    'K-1 P2, 2-3 P2, 4-5 P2-P3: mirror pair A, B, C, D': ['ABCD'],
    'K-1 P3, 2-3 P4 first trial: D changed to C': ['ABCC'],
    'K-1 P4, 2-3 P5: A, A, B, C': ['AABC'],
    '2-3 P6: A, A, B, C, then one A changed to D': ['AABC', 'ABCD'],
    '4-5 P6: four different letters': ['ABCD'],
}
for x, y in combinations('ABCD', 2):
    # merge x and y: keep one of the two names on both corners
    options = []
    for keep in (x, y):
        lab = Counter('ABCD')
        lab[x] -= 1
        lab[y] -= 1
        lab[keep] += 2
        options.append(''.join(sorted(lab.elements())))
    need[f'2-3 P4, 4-5 P4: merge {x}{y} (keep either name)'] = [options]
for prob, labellings in need.items():
    good = True
    for lab in labellings:
        alts = lab if isinstance(lab, list) else [lab]
        good &= any(all(Counter(a)[ch] <= KIT[ch] for ch in a) for a in alts)
    ok(f'caps build {prob}', good, labellings)
OLD = Counter('AABCCD')                # the earlier guide: spare A and C only
ok('the BD merge needs the second B: spare A and C alone cannot make it',
   not any(all(Counter(a)[ch] <= OLD[ch] for ch in a) for a in ('ABBC', 'ACDD')))
ok('caps title lists A, A, B, B, C, C, D', 'A, A, B, B, C, C, D for each model' in text)
models = nets
ok('cap sheets per table cover its models (four models a sheet)', caps_sheets is not None and models is not None
   and all(4 * c >= m for c, m in zip(caps_sheets, models)), (caps_sheets, models))

# ---- page 3: pose mat -----------------------------------------------------
page, text, segs, paper, mats = pages[3]
ok('pose mat on copy paper', paper == 'copy paper', paper)
w3 = words(page)
tri = {}
for s in segs:
    tri.setdefault(s[3], []).append(s)
foot = [ss for ss in tri.values() if len(ss) == 3 and all(abs(dist(s[0], s[1]) - 90 * MM) < TOL for s in ss)]
ok('two footprints, equilateral with 90 mm sides (one model face)', len(foot) == 2, len(foot))
for ss in foot:
    pts = [s[0] for s in ss]
    back = min(pts, key=lambda p: p[1])          # farthest from the reader (top of page)
    fl, fr = sorted([p for p in pts if p is not back], key=lambda p: p[0])

    def near(word, p):
        return any(t == word and dist(c, p) < 50 for t, c in w3)
    ok('footprint corners named back, front left, front right',
       near('back', back) and near('left', fl) and near('right', fr))
ok('a footprint per model at each table', mats is not None and all(2 * m >= n for m, n in zip(mats, models)),
   (mats, models))

# the guide's materials section quotes the same sheet totals
guide = PDF.parent / 'facilitator-guide.pdf'
if guide.exists():
    g = ' '.join(fitz.open(guide)[1].get_text().split())
    for what, n in (('Models, sheet 1, card stock', sum(nets)), ('Letter caps, sheet 2, card stock', sum(caps_sheets)),
                    ('Pose mat, sheet 3, copy paper', sum(mats))):
        ok(f'guide p. 2 gives {n} sheets for {what}', f'{what}, {n} sheets' in g, n)
    ok('guide p. 2 points to week-37-materials.pdf', 'week-37-materials.pdf' in g)

fails = [c for c in checks if not c['pass']]
(PDF.parent / 'materials-checks.json').write_text(json.dumps(
    {'pdf': PDF.name, 'checks': len(checks), 'failures': len(fails), 'results': checks}, indent=1, ensure_ascii=False) + '\n')
print(f'{len(checks)} checks, {len(fails)} failures')
sys.exit(1 if fails else 0)
