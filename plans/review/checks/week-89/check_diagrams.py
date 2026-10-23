#!/usr/bin/env python3
"""Week 89 diagram and page check for the review (independent of the package's checker).

Reads the delivered PDFs with PyMuPDF and the TikZ source of Problem 19 for exact cube
coordinates. Finds the repository by walking up from this file.
"""
import re
from pathlib import Path
import pymupdf as fitz

HERE = Path(__file__).resolve().parent


def find_repo():
    for p in [HERE, *HERE.parents]:
        if (p / 'AGENTS.md').exists() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-89'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-89'
if (SRC / 'editable').is_dir():   # the package moved to editable/ at the problem-file conversion
    SRC = SRC / 'editable'
MM = 72 / 25.4
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def note(msg):
    print('NOTE ' + msg)


stu = fitz.open(WEEK / 'week-89-students.pdf')
mat = fitz.open(WEEK / 'week-89-materials.pdf')
fac = fitz.open(WEEK / 'week-89-facilitator.pdf')

print('== Pages, headers, footers, problem numbers ==')
nums = []
for i, p in enumerate(stu):
    t = p.get_text()
    check('Week 89 / Growing shapes and totals / Grades K–5' in t and 'Bellingham Math Circle / Week 89 / W89-S-v2' in t,
          f'student p{i+1}: header and footer')
    nums += [int(m) for m in re.findall(r'Problem (\d+):', t)]
check(nums == list(range(1, 21)), f'problems numbered consecutively: {nums}')
check(len(stu) == 11 and len(mat) == 2 and len(fac) == 8, 'page counts 11 / 2 / 8')
for d in (stu, mat, fac):
    r = d[0].rect
    check(abs(r.width - 612) < 1 and abs(r.height - 792) < 1, 'US Letter')

print('== Tile figures (pp. 1-3, 8) read from the PDF ==')


def tiles(page):
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if d.get('fill') is not None and d['type'] == 'fs' and len(d['items']) == 4 and abs(r.width - r.height) < 0.05 and 10 < r.width < 25:
            shade = 'grey' if d['fill'][0] < 0.9 else 'white'
            out.append((r, shade))
    return out


def figures(tl):
    # connected components by touching rectangles
    n = len(tl)
    parent = list(range(n))

    def f(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i in range(n):
        for j in range(i + 1, n):
            a, b = tl[i][0], tl[j][0]
            if a.x0 <= b.x1 + 0.1 and b.x0 <= a.x1 + 0.1 and a.y0 <= b.y1 + 0.1 and b.y0 <= a.y1 + 0.1:
                parent[f(i)] = f(j)
    groups = {}
    for i in range(n):
        groups.setdefault(f(i), []).append(tl[i])
    figs = []
    for g in groups.values():
        s = g[0][0].width
        x0 = min(r.x0 for r, _ in g)
        y1 = max(r.y1 for r, _ in g)
        cells = {(round((r.x0 - x0) / s), round((y1 - r.y1) / s)): sh for r, sh in g}
        bbox = fitz.Rect(x0, min(r.y0 for r, _ in g), max(r.x1 for r, _ in g), y1)
        figs.append((bbox, cells, s))
    # rows of figures: cluster by vertical centre (tabular rows centre their pictures), then left to right
    figs.sort(key=lambda t: (t[0].y0 + t[0].y1) / 2)
    rows, last = [], None
    for f_ in figs:
        cy = (f_[0].y0 + f_[0].y1) / 2
        if last is None or cy - last > 30:
            rows.append([])
        rows[-1].append(f_)
        last = cy
    return [f_ for r in rows for f_ in sorted(r, key=lambda t: t[0].x0)]


def caption(page, bbox):
    words = page.get_text('words')
    below = [w for w in words if bbox.y1 < w[1] < bbox.y1 + 30 and w[0] < bbox.x1 + 5 and w[2] > bbox.x0 - 5]
    return ' '.join(w[4] for w in sorted(below, key=lambda w: w[0]))


def kind(cells):
    pts = set(cells)
    w = max(x for x, _ in pts) + 1
    h = max(y for _, y in pts) + 1
    if len(pts) == w * h:
        return f'{h}x{w} block'  # rows x columns
    st = {(x, h - k) for k in range(1, h + 1) for x in range(k)}
    if pts == st:
        return f'{h}-row stairs'
    return f'other {sorted(pts)}'


expected = {
    1: ['1x2 block', '2x3 block', '2x3 block', '1x1 block', '2x2 block', '3x3 block', '4x4 block', '5x5 block'],
    2: ['1x1 block', '2-row stairs', '3-row stairs', '4-row stairs', '3-row stairs', '3-row stairs'],
    3: ['1x2 block', '2x3 block', '3x4 block', '4x5 block'],
    8: ['1x1 block', '2x2 block', '3x3 block', '4x4 block'],
}
for pg, exp in expected.items():
    page = stu[pg - 1]
    figs = figures(tiles(page))
    got = [kind(c) for _, c, _ in figs]
    caps = [caption(page, b) for b, _, _ in figs]
    sizes = sorted({round(s / MM, 2) for _, _, s in figs})
    print(f'  p{pg}:', list(zip(got, caps)), 'cell mm', sizes)
    check(got == exp, f'p{pg} tile figures are {exp}')
    if pg == 1:
        old, mid, new = figs[0][1], figs[1][1], figs[2][1]
        grey = {c for c, s in mid.items() if s == 'grey'}
        white = {c for c, s in mid.items() if s == 'white'}
        check(white == set(old) and set(mid) == set(new) and len(grey) == 4,
              'p1 opening: white = old 1x2, white+grey = new 2x3, 4 shaded')
        note('p1 opening example (1x2 -> 2x3, add 4) is the first growth of Problem 5 and the "1 to 2" rectangle entry of Problem 6')

print('== Slips and tables (text inside boxes) ==')


def boxed_digits(page):
    out = []
    rects = [d['rect'] for d in page.get_drawings() if d['type'] == 's' and len(d['items']) in (1, 4)
             and 20 < d['rect'].width < 30 and 18 < d['rect'].height < 26]
    for w in page.get_text('words'):
        if re.fullmatch(r'\d+', w[4]):
            for r in rects:
                if r.contains(fitz.Rect(w[:4])):
                    out.append((round(r.y0), r.x0, w[4]))
    return [d for _, _, d in sorted(set(out))]


print('  p4 slips', boxed_digits(stu[3]))
print('  p6 slips', boxed_digits(stu[5]))
print('  p7 slips', boxed_digits(stu[6]))
check(boxed_digits(stu[3])[:5] == ['0', '1', '2', '3', '4'], 'P7 slips 0 1 2 3 4')
check(boxed_digits(stu[5])[:5] == ['2', '2', '1', '0', '0'], 'P11 slips 2 2 1 0 0')
check(boxed_digits(stu[6])[:4] == ['1', '3', '0', '0'], 'P12 slips 1 3 0 0')
t4 = stu[3].get_text()
t5 = stu[4].get_text()
check(re.search(r'total\s+5\s+5\s+9\s+12', t4) is not None and 'The tray starts at 2' in t4, 'P8 table: start 2, totals 5 5 9 12')
check(re.search(r'total\s+4\s+7\s+7\s+12', t5) is not None, 'P9 table: totals 4 7 7 12')

print('== Materials ==')
for i, (w_mm, h_mm) in enumerate(((120, 120), (140, 120))):
    p = mat[i]
    boards = [d for d in p.get_drawings() if d['type'] == 's' and (d.get('width') or 0) > 0.7 and d['rect'].width > 200]
    r = boards[0]['rect']
    check(abs(r.width / MM - w_mm) < 0.1 and abs(r.height / MM - h_mm) < 0.1,
          f'material p{i+1}: board {r.width / MM:.2f} x {r.height / MM:.2f} mm')
    grid = [d for d in p.get_drawings() if d['type'] == 's' and abs((d.get('width') or 0) - 0.299) < 0.01]
    xs = sorted({round(it[1].x, 2) for it in grid[0]['items'] for _ in [0] if it[0] == 'l'} |
                {round(it[2].x, 2) for it in grid[0]['items'] if it[0] == 'l'})
    steps = sorted({round((b - a) / MM, 2) for a, b in zip(xs, xs[1:]) if b - a > 1})
    check(steps == [20.0], f'material p{i+1}: grid spacing {steps} mm')
words = [w[4] for w in mat[0].get_text('words')]
cards = [w for w in words[words.index('mm', words.index('20')) + 1:] if re.fullmatch(r'\d', w)][:7]
check(sorted(cards) == ['0', '0', '1', '2', '2', '3', '4'], f'input cards {cards}')

print('== Problem 19 picture: drawing order vs true depth (from TikZ source) ==')
tex = (SRC / 'student' / 'students.tex').read_text()
seg = tex[tex.index('\\problem{19}'):tex.index('\\problem{20}')]
# walk scopes: 2D figure scopes have shift={(a,b)}, 3D sub-scopes shift={(a,b,c)}
tok = re.finditer(r'\\begin\{scope\}\[shift=\{\(([^)]*)\)\}[^\]]*\]|\\end\{scope\}|\\filldraw\[[^\]]*\]\s*([^;]*);', seg)
figs, stack, cur = [], [], None
for m in tok:
    s = m.group(0)
    if s.startswith('\\begin'):
        vals = [float(v) for v in m.group(1).split(',')]
        if len(vals) == 2:
            cur = []
            figs.append(cur)
            stack.append(('2d', None))
        else:
            stack.append(('3d', vals))
    elif s.startswith('\\end'):
        stack.pop()
    else:
        off = [0.0, 0.0, 0.0]
        for k, v in stack:
            if k == '3d':
                off = [a + b for a, b in zip(off, v)]
        pts = [tuple(float(v) + o for v, o in zip(t.split(','), off)) for t in re.findall(r'\(([^)]*)\)', m.group(2))]
        cur.append(pts)
boxes_per_fig = []
for faces in figs:
    boxes = []
    for i in range(0, len(faces), 3):
        pts = [p for f in faces[i:i + 3] for p in f]
        boxes.append(tuple((min(p[k] for p in pts), max(p[k] for p in pts)) for k in range(3)))
    boxes_per_fig.append(boxes)
names = ['step-1 pile', 'middle (placing)', 'step-2 pile']
for nm, bx in zip(names, boxes_per_fig):
    print(f'  {nm}: boxes in drawing order', bx)
check(boxes_per_fig[2] and sorted(boxes_per_fig[2]) == sorted([((0, 1), (1, 2), (0, 1)), ((1, 2), (0, 1), (0, 1)), ((0, 1), (0, 1), (0, 2))]),
      'step-2 pile = cubes (0,1,0), (1,0,0) and a column of two at the square corner: {i+j+k<2}, 4 cubes')

# projection used by the picture: x -> (7,0) mm, y -> (3.5,2.6) mm, z -> (0,7) mm
D = (-0.5, 1.0, -2.6 / 7)  # direction that projects to a point; +t moves away from the viewer


def entry(box, sx, sy):
    p0 = (sx / 7.0, 0.0, sy / 7.0)
    lo, hi = -1e9, 1e9
    for k in range(3):
        a, b = box[k]
        if abs(D[k]) < 1e-12:
            if not (a < p0[k] < b):
                return None
            continue
        t1, t2 = (a - p0[k]) / D[k], (b - p0[k]) / D[k]
        lo, hi = max(lo, min(t1, t2)), min(hi, max(t1, t2))
    return lo if lo < hi - 1e-9 else None


for nm, bx in zip(names, boxes_per_fig):
    wrong, total = 0, 0
    pairs = set()
    step = 0.05
    xs = [i * step for i in range(-10, int(25 / step))]
    ys = [i * step for i in range(-10, int(25 / step))]
    for sx in xs:
        for sy in ys:
            hits = [(entry(b, sx, sy), i) for i, b in enumerate(bx)]
            hits = [(t, i) for t, i in hits if t is not None]
            if not hits:
                continue
            total += 1
            nearest = min(hits)[1]
            painted = max(i for _, i in hits)  # painter: last drawn box covering the point
            if nearest != painted:
                wrong += 1
                pairs.add((bx[painted], bx[nearest]))
    area = wrong * step * step
    check(wrong == 0, f'{nm}: {area:.1f} mm^2 of picture painted by a box that is actually behind another')
    for a, b in sorted(pairs):
        note(f'  {nm}: box {a} drawn over box {b}, which is nearer the viewer')


def wrong_area(bx, step=0.05):
    wrong = 0
    for i in range(-10, int(25 / step)):
        for j in range(-10, int(25 / step)):
            hits = [(entry(b, i * step, j * step), k) for k, b in enumerate(bx)]
            hits = [(t, k) for t, k in hits if t is not None]
            if hits and min(hits)[1] != max(k for _, k in hits):
                wrong += 1
    return wrong * step * step


for nm, bx in zip(names, boxes_per_fig):
    fixed = sorted(bx, key=lambda b: (-b[1][0], b[0][0], b[2][0]))  # back rows first, then left to right, then upward
    check(wrong_area(fixed) == 0, f'{nm}: proposed order (back to front, left to right, bottom up) {fixed} paints correctly')

# the smallest source edit: move the cube at (1,0,0) to just after the corner cube / column, leave the rest
for nm, bx in zip(names[1:], boxes_per_fig[1:]):
    right = [b for b in bx if b[0][0] == 1.0]
    rest = [b for b in bx if b[0][0] != 1.0]
    corner_idx = max(i for i, b in enumerate(rest) if b[0][0] == 0.0 and b[1][0] == 0.0 and b[2][0] == 0.0)
    edited = rest[:corner_idx + 1] + right + rest[corner_idx + 1:]
    check(wrong_area(edited) == 0, f'{nm}: minimal edit order {edited} paints correctly')

print('== Guide page references ==')
g = '\n'.join(p.get_text() for p in fac)
gflat = ' '.join(g.split())
where = {}
for i, p in enumerate(stu):
    for m in re.findall(r'Problem (\d+):', p.get_text()):
        where[int(m)] = i + 1
print('  problem -> page', where)
claims = [('Problems 1–4 (student pages 1–2)', [1, 2, 3, 4], {1, 2}), ('Problems 5–6 (page 3)', [5, 6], {3}),
          ('Problems 7–10 (pages 4–5)', [7, 8, 9, 10], {4, 5}), ('Problems 11–13 (pages 6–7)', [11, 12, 13], {6, 7}),
          ('14–15 (page 8)', [14, 15], {8}), ('16–17 (page 9)', [16, 17], {9}), ('18–20 (pages 10–11)', [18, 19, 20], {10, 11})]
for text, probs, pages in claims:
    check(text in gflat and {where[k] for k in probs} == pages, f'guide says "{text}"')

print()
print('FAILURES:', len(FAILS))
for f in FAILS:
    print('  ', f)
