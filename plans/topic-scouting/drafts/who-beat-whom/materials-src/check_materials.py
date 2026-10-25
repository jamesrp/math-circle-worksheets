"""Measure the delivered materials PDF and compare it with the student pages.

Usage:  python3 check_materials.py [../materials.pdf]

Reads the drawn paths of the PDF (PyMuPDF), not the TeX source, and cross-checks the
card grids by rendering at 300 dpi and measuring pixels. Every size must be within
0.5 mm of its target. Exit status 1 if any check fails.
"""
import math
import os
import sys

import numpy as np
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
STUDENT_K1 = os.environ.get('WBW_STUDENT_K1', os.path.join(HERE, '..', 'k-1.pdf'))
PDF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'materials.pdf')

MM = 25.4 / 72
ANIMAL_ORDER = ['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig']
TOL = 0.5
FAILS = []


def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


# ------------------------------------------------------------------ path helpers
FILLS = {
    'cat': (247, 196, 140), 'dog': (226, 200, 160), 'bear': (176, 128, 88),
    'rabbit': (238, 238, 238), 'frog': (150, 205, 120), 'pig': (248, 190, 200),
}


def rgb(c):
    return tuple(round(v * 255) for v in c) if c else None


def bbox(d):
    r = d['rect']
    return (r.x0 * MM, r.y0 * MM, r.x1 * MM, r.y1 * MM)


def size(d):
    b = bbox(d)
    return b[2] - b[0], b[3] - b[1]


def kinds(d):
    return [it[0] for it in d['items']]


def verts(d):
    pts = []
    for it in d['items']:
        if it[0] == 're':
            r = it[1]
            return [(r.x0 * MM, r.y0 * MM), (r.x1 * MM, r.y0 * MM), (r.x1 * MM, r.y1 * MM), (r.x0 * MM, r.y1 * MM)]
        if it[0] == 'qu':
            q = it[1]
            return [(q.ul.x * MM, q.ul.y * MM), (q.ur.x * MM, q.ur.y * MM), (q.lr.x * MM, q.lr.y * MM), (q.ll.x * MM, q.ll.y * MM)]
        if it[0] == 'l':
            for p in (it[1], it[2]):
                q = (p.x * MM, p.y * MM)
                if not pts or math.hypot(q[0] - pts[-1][0], q[1] - pts[-1][1]) > 1e-3:
                    pts.append(q)
    if len(pts) > 1 and math.hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1]) < 1e-3:
        pts.pop()
    return pts


def is_plain_rect(d, w, h):
    """Stroked, unfilled, axis-aligned four-line rectangle of w x h mm."""
    if d['type'] != 's' or kinds(d) != ['l'] * 4:
        return False
    sw, sh = size(d)
    return near(sw, w) and near(sh, h)


def is_rounded_box(d, s, filled=None):
    k = kinds(d)
    if 'c' not in k or len(k) < 8:
        return False
    sw, sh = size(d)
    if not (near(sw, s) and near(sh, s)):
        return False
    if filled is None:
        return d['type'] == 's'
    return d['type'] == 'fs' and rgb(d.get('fill')) == filled


def is_dashed(d):
    return bool(d.get('dashes')) and d['dashes'].strip() not in ('[] 0', '')


def inside(b, outer, margin=0.0):
    return (b[0] >= outer[0] + margin - 1e-6 and b[1] >= outer[1] + margin - 1e-6
            and b[2] <= outer[2] - margin + 1e-6 and b[3] <= outer[3] - margin + 1e-6)


def centre(b):
    return ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)


def contains_pt(b, p):
    return b[0] <= p[0] <= b[2] and b[1] <= p[1] <= b[3]


def arrowheads(ds):
    """Filled black four-point notched arrowheads."""
    out = []
    for d in ds:
        if d['type'] == 'f' and rgb(d.get('fill')) == (0, 0, 0) and kinds(d) == ['l'] * 4:
            v = verts(d)
            if len(v) == 4:
                out.append((d, v))
    return out


def head_dir(v):
    """Direction of a notched arrowhead [tip, barb, notch, barb]: from notch to tip."""
    tip, notch = v[0], v[2]
    dx, dy = tip[0] - notch[0], tip[1] - notch[1]
    D = math.hypot(dx, dy)
    return dx / D, dy / D


# convex polygon clipping (Sutherland-Hodgman) for overlap tests
def orient(poly):
    a = sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
            for i in range(len(poly)))
    return poly if a > 0 else poly[::-1]


def clip(subject, clipper):
    subject, clipper = orient(subject), orient(clipper)

    def inside_e(p, a, b):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= 0

    def inter(p, q, a, b):
        x1, y1 = p; x2, y2 = q; x3, y3 = a; x4, y4 = b
        dd = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / dd
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    out = subject
    for i in range(len(clipper)):
        a, b = clipper[i], clipper[(i + 1) % len(clipper)]
        inp, out = out, []
        if not inp:
            break
        s = inp[-1]
        for e in inp:
            if inside_e(e, a, b):
                if not inside_e(s, a, b):
                    out.append(inter(s, e, a, b))
                out.append(e)
            elif inside_e(s, a, b):
                out.append(inter(s, e, a, b))
            s = e
    return out


def area(poly):
    if len(poly) < 3:
        return 0.0
    return 0.5 * abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
                         for i in range(len(poly))))


def box_poly(b, grow=0.0):
    return [(b[0] - grow, b[1] - grow), (b[2] + grow, b[1] - grow), (b[2] + grow, b[3] + grow), (b[0] - grow, b[3] + grow)]


def lane_shape(v):
    """For a 4-vertex lane polygon return (width, length, end1, end2, axis) where the
    ends are the midpoints of the two short sides."""
    sides = [(v[i], v[(i + 1) % 4]) for i in range(4)]
    lens = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in sides]
    # right angles
    angs = []
    for i in range(4):
        a, b, c = v[i - 1], v[i], v[(i + 1) % 4]
        u = (a[0] - b[0], a[1] - b[1]); w = (c[0] - b[0], c[1] - b[1])
        angs.append(math.degrees(math.acos(max(-1, min(1, (u[0] * w[0] + u[1] * w[1]) / (math.hypot(*u) * math.hypot(*w)))))))
    short = [i for i in range(4) if lens[i] <= min(lens) + 1e-6 or near(lens[i], min(lens), 0.01)]
    i0 = lens.index(min(lens))
    s1 = sides[i0]; s2 = sides[(i0 + 2) % 4]
    m1 = ((s1[0][0] + s1[1][0]) / 2, (s1[0][1] + s1[1][1]) / 2)
    m2 = ((s2[0][0] + s2[1][0]) / 2, (s2[0][1] + s2[1][1]) / 2)
    width = (lens[i0] + lens[(i0 + 2) % 4]) / 2
    length = (lens[(i0 + 1) % 4] + lens[(i0 + 3) % 4]) / 2
    return width, length, m1, m2, angs


def seg_dist(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def poly_dist(A, B):
    """Distance between two disjoint convex polygons (0 if they overlap)."""
    if area(clip(A, B)) > 1e-6:
        return 0.0
    d = min(seg_dist(p, B[i], B[(i + 1) % len(B)]) for p in A for i in range(len(B)))
    return min(d, min(seg_dist(p, A[i], A[(i + 1) % len(A)]) for p in B for i in range(len(A))))


def dist_to_box(p, b):
    dx = max(b[0] - p[0], 0, p[0] - b[2])
    dy = max(b[1] - p[1], 0, p[1] - b[3])
    return math.hypot(dx, dy)


# ------------------------------------------------------------------ raster helper
def grid_lines_px(page, region, dpi=300, axis=0, frac=0.8):
    """Positions (mm) of dark lines running across `region` (mm bbox) in a 300 dpi render.
    axis=0 finds vertical lines, axis=1 horizontal lines."""
    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    s = dpi / 25.4
    x0, y0, x1, y1 = [int(round(v * s)) for v in region]
    sub = a[y0:y1, x0:x1] < 110
    prof = sub.mean(axis=0) if axis == 0 else sub.mean(axis=1)
    idx = np.where(prof >= frac)[0]
    lines, run = [], []
    for i in idx:
        if run and i != run[-1] + 1:
            lines.append(np.mean(run)); run = []
        run.append(i)
    if run:
        lines.append(np.mean(run))
    off = x0 if axis == 0 else y0
    return [(v + off) / s for v in lines]


# ------------------------------------------------------------------ student pages
stu = pymupdf.open(STUDENT_K1)
board = stu[0].get_drawings()
b_squares = [d for d in board if d['type'] in ('s', 'fs') and near(size(d)[0], 40) and near(size(d)[1], 40) and 'c' in kinds(d)]
b_lanes = [lane_shape(verts(d)) for d in board if is_dashed(d) and len(verts(d)) == 4]
side_lanes = [l for l in b_lanes if l[1] < 130]
diag_lanes = [l for l in b_lanes if l[1] >= 130]
print(f"Student K-1 page 1 big board: {len(b_squares)} animal squares "
      f"{sorted(set(round(size(d)[0], 1) for d in b_squares))} mm; lanes "
      f"{[(round(w, 1), round(L, 1)) for w, L, *_ in b_lanes]}")
check(len(b_squares) == 4 and len(side_lanes) == 4 and len(diag_lanes) == 2
      and all(near(w, 23) for w, *_ in b_lanes) and all(near(L, 108) for _, L, *_ in side_lanes),
      "student big board has 4 animal squares, 4 side lanes and 2 diagonal lanes")

# K-1 Problem 2 pictures: boxes, newcomer and dashed lanes, split into left/right picture
p2 = stu[1].get_drawings()
pw = stu[1].rect.width * MM
p2_pics = {}
for side, name in (('L', 'frog'), ('R', 'pig')):
    def on_side(d):
        cx = centre(bbox(d))[0]
        return cx < pw / 2 if side == 'L' else cx >= pw / 2
    lanes = [d for d in p2 if is_dashed(d) and on_side(d) and len(verts(d)) == 4 and bbox(d)[1] < 100]
    ylane_top = min(bbox(d)[1] for d in lanes)
    ylane_bot = max(bbox(d)[3] for d in lanes)
    rowboxes = [d for d in p2 if on_side(d) and d['type'] == 's' and 'c' in kinds(d)
                and near(size(d)[0], size(d)[1], 0.2) and bbox(d)[3] <= ylane_top + 1]
    newbox = [d for d in p2 if on_side(d) and 'c' in kinds(d) and bbox(d)[1] > ylane_top + 5
              and near(size(d)[0], size(d)[1], 0.2) and size(d)[0] > 15 and bbox(d)[1] < ylane_bot + 5]
    nbb = bbox(newbox[0])
    face = {k for d in p2 if contains_pt(nbb, centre(bbox(d))) for k, v in FILLS.items() if rgb(d.get('fill')) == v}
    heads = [h for h in arrowheads(p2) if on_side(h[0]) and bbox(h[0])[3] <= ylane_top + 1]
    p2_pics[name] = dict(n=len(rowboxes), lanes=len(lanes), new=len(newbox), face=face, heads=len(heads))
    check(len(newbox) == 1, f"student K-1 Problem 2 {name} picture: one newcomer square")
    print(f"Student K-1 Problem 2 {name} picture: {len(rowboxes)} line-up boxes, {len(heads)} arrows between them, "
          f"{len(lanes)} dashed lanes, newcomer square showing {sorted(face)}")

# ------------------------------------------------------------------ materials
doc = pymupdf.open(PDF)
check(doc.page_count == 5, f"materials.pdf has 5 pages (found {doc.page_count})")
HEADER = "Week NN / Who beat whom / Materials"
FOOTER = "Bellingham Math Circle / Week NN / FNN-M-v1"
LABELS = {1: {"Animal cards", "100 mm scale check"}, 2: {"Arrow cards"},
          3: {"Line-up strip (K–1)", "left part", "right part"},
          4: {"K–1 Problem 2: frog"}, 5: {"K–1 Problem 2: pig"}}

for i, page in enumerate(doc):
    n = i + 1
    W, H = page.rect.width * MM, page.rect.height * MM
    check(near(W, 279.4, 0.1) and near(H, 215.9, 0.1), f"p{n}: landscape US Letter ({W:.1f} x {H:.1f} mm)")
    lines = []
    for blk in page.get_text('dict')['blocks']:
        for ln in blk.get('lines', []):
            t = ''.join(sp['text'] for sp in ln['spans']).strip()
            if t:
                lines.append((t, [v * MM for v in ln['bbox']]))
    texts = [t for t, _ in lines]
    check(HEADER in texts and FOOTER in texts and str(n) in texts, f"p{n}: header, footer and page number present")
    extra = set(texts) - {HEADER, FOOTER, str(n)} - LABELS[n]
    check(not extra, f"p{n}: only short object labels on the sheet (unexpected text: {sorted(extra)})")
    # 12 mm from every paper edge: drawings (plus half their line width) and text
    worst = 99
    for d in page.get_drawings():
        hw = (d.get('width') or 0) * MM / 2
        b = bbox(d)
        worst = min(worst, b[0] - hw, b[1] - hw, W - b[2] - hw, H - b[3] - hw)
    for t, b in lines:
        worst = min(worst, b[0], b[1], W - b[2], H - b[3])
    check(worst >= 12.0, f"p{n}: everything at least 12 mm from the paper edges (closest {worst:.1f} mm)")

# ---------------- page 1: animal cards
p = doc[0]
ds = p.get_drawings()
cards = [d for d in ds if is_plain_rect(d, 40, 40)]
check(len(cards) == 18, f"p1: 18 animal cards found ({len(cards)})")
sz = [size(d) for d in cards]
check(all(near(w, 40) and near(h, 40) for w, h in sz),
      f"p1: every animal card 40 x 40 mm (measured {min(min(s) for s in sz):.2f} to {max(max(s) for s in sz):.2f} mm)")
check(all(near(size(d)[0], size(cards[0])[0]) for d in b_squares),
      "p1: animal cards are the size of the big board's animal squares (40 mm)")
xs = sorted(set(round(bbox(d)[0], 1) for d in cards)); ys = sorted(set(round(bbox(d)[1], 1) for d in cards))
check(len(xs) == 6 and len(ys) == 3 and all(near(b - a, 40) for a, b in zip(xs, xs[1:])) and all(near(b - a, 40) for a, b in zip(ys, ys[1:])),
      "p1: cards form a 6 x 3 grid with shared cut lines (one set of six per row)")
order_ok, face_margin = True, 99
for r, y in enumerate(ys):
    row = sorted([d for d in cards if near(bbox(d)[1], y, 0.2)], key=lambda d: bbox(d)[0])
    names = []
    for c in row:
        cb = bbox(c)
        parts = [d for d in ds if d is not c and contains_pt(cb, centre(bbox(d))) and not is_plain_rect(d, 40, 40)]
        fb = (min(bbox(d)[0] for d in parts), min(bbox(d)[1] for d in parts), max(bbox(d)[2] for d in parts), max(bbox(d)[3] for d in parts))
        face_margin = min(face_margin, fb[0] - cb[0], fb[1] - cb[1], cb[2] - fb[2], cb[3] - fb[3])
        found = [k for k, v in FILLS.items() if any(rgb(d.get('fill')) == v for d in parts)]
        names.append(found[0] if len(found) == 1 else '?')
    print(f"   row {r + 1}: {names}")
    order_ok &= names == ['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig']
check(order_ok, "p1: each row is one set: cat, dog, bear, rabbit, frog, pig")


def face_size(page_ds, cb):
    parts = [d for d in page_ds if contains_pt(cb, centre(bbox(d))) and size(d)[0] < cb[2] - cb[0] - 1]
    return (round(max(bbox(d)[2] for d in parts) - min(bbox(d)[0] for d in parts), 2),
            round(max(bbox(d)[3] for d in parts) - min(bbox(d)[1] for d in parts), 2))


same = True
row1 = sorted([d for d in cards if near(bbox(d)[1], ys[0], 0.2)], key=lambda d: bbox(d)[0])
for sqd in b_squares:
    sb = bbox(sqd)
    kind = [k for k, v in FILLS.items() if any(rgb(d.get('fill')) == v and contains_pt(sb, centre(bbox(d))) for d in board)]
    if len(kind) != 1:
        same = False
        continue
    card = row1[ANIMAL_ORDER.index(kind[0])]
    same &= face_size(board, sb) == face_size(ds, bbox(card))
check(same, "p1: each card's face is drawn at the same size as on the big board's animal squares")
check(face_margin >= 2.0, f"p1: every face clear of the cut lines (closest {face_margin:.1f} mm)")
bars = [d for d in ds if d['type'] == 's' and kinds(d) == ['l'] and size(d)[1] < 0.01 and 50 < size(d)[0] < 200]
check(len(bars) == 1 and near(size(bars[0])[0], 100), f"p1: scale check bar 100 mm ({size(bars[0])[0]:.2f} mm)")
grid = (min(bbox(d)[0] for d in cards), min(bbox(d)[1] for d in cards), max(bbox(d)[2] for d in cards), max(bbox(d)[3] for d in cards))
vx = grid_lines_px(p, (grid[0] - 1, grid[1] + 1, grid[2] + 1, grid[3] - 1), axis=0)
hy = grid_lines_px(p, (grid[0] + 1, grid[1] - 1, grid[2] - 1, grid[3] + 1), axis=1)
dvx = [b - a for a, b in zip(vx, vx[1:])]; dhy = [b - a for a, b in zip(hy, hy[1:])]
check(len(vx) == 7 and len(hy) == 4 and all(near(v, 40) for v in dvx + dhy),
      f"p1: 300 dpi render: card pitch {min(dvx + dhy):.2f} to {max(dvx + dhy):.2f} mm")
bb = bbox(bars[0])
bx = grid_lines_px(p, (bb[0] - 1, bb[1] - 2.4, bb[2] + 1, bb[1] + 2.4), axis=0, frac=0.9)
check(len(bx) == 2 and near(bx[1] - bx[0], 100), f"p1: 300 dpi render: scale bar {bx[1] - bx[0]:.2f} mm between end ticks")

# ---------------- page 2: arrow cards
p = doc[1]
ds = p.get_drawings()
acards = [d for d in ds if is_plain_rect(d, 75, 20)]
check(len(acards) == 18, f"p2: 18 arrow cards found ({len(acards)})")
sz = [size(d) for d in acards]
check(all(near(w, 75) and near(h, 20) for w, h in sz),
      f"p2: every arrow card 75 x 20 mm (measured {min(s[0] for s in sz):.2f}-{max(s[0] for s in sz):.2f} x {min(s[1] for s in sz):.2f}-{max(s[1] for s in sz):.2f} mm)")
heads = arrowheads(ds)
ok = True
for c in acards:
    cb = bbox(c)
    hs = [h for h in heads if inside(bbox(h[0]), cb, 1.5)]
    shafts = [d for d in ds if d['type'] == 'f' and inside(bbox(d), cb, 1.5) and size(d)[0] > 30]
    ok &= len(hs) == 1 and len(shafts) == 1 and near(head_dir(hs[0][1])[0], 1, 0.01)
check(ok, "p2: each arrow card carries one arrow (shaft and head), at least 1.5 mm inside its cut lines")
L_card = max(s[0] for s in sz); W_card = max(s[1] for s in sz)
check(all(L_card <= L - 2 and W_card <= w - 2 for w, L, *_ in side_lanes),
      f"p2: arrow card fits the big board's side lanes ({min(L for _, L, *_ in side_lanes):.1f} x {min(w for w, *_ in side_lanes):.1f} mm) with 2 mm to spare")
check(all(L_card <= L - 2 and W_card <= w - 2 for w, L, *_ in diag_lanes),
      f"p2: arrow card fits the big board's diagonal lanes ({min(L for _, L, *_ in diag_lanes):.1f} mm)")
check(L_card <= 108.0, "p2: arrow card no longer than about 10.8 cm")
agrid = (min(bbox(d)[0] for d in acards), min(bbox(d)[1] for d in acards), max(bbox(d)[2] for d in acards), max(bbox(d)[3] for d in acards))
vx = grid_lines_px(p, (agrid[0] - 1, agrid[1] + 0.5, agrid[2] + 1, agrid[3] - 0.5), axis=0, frac=0.95)
hy = grid_lines_px(p, (agrid[0] + 0.5, agrid[1] - 1, agrid[0] + 2.5, agrid[3] + 1), axis=1, frac=0.95)
dvx = [b - a for a, b in zip(vx, vx[1:])]; dhy = [b - a for a, b in zip(hy, hy[1:])]
check(len(vx) == 4 and all(near(v, 75) for v in dvx) and len(hy) == 7 and all(near(v, 20) for v in dhy),
      f"p2: 300 dpi render: card length {min(dvx):.2f}-{max(dvx):.2f} mm, width {min(dhy):.2f}-{max(dhy):.2f} mm")

# ---------------- page 3: line-up strip
p = doc[2]
ds = p.get_drawings()
parts = sorted([d for d in ds if d['type'] == 's' and kinds(d) == ['l'] * 4 and near(size(d)[1], 50)], key=lambda d: bbox(d)[1])
check(len(parts) == 2, f"p3: line-up strip in two parts ({len(parts)})")
boxes = [d for d in ds if is_rounded_box(d, 44)]
heads = arrowheads(ds)
check(len(boxes) == 6, f"p3: six line-up boxes in all ({len(boxes)})")
check(all(near(size(d)[0], 44) and near(size(d)[1], 44) for d in boxes),
      f"p3: every box 44 x 44 mm, holding a 40 mm card with 2 mm to spare on each side")
info = []
for k, part in enumerate(parts):
    pb = bbox(part)
    bx = sorted([d for d in boxes if inside(bbox(d), pb)], key=lambda d: bbox(d)[0])
    hs = [h for h in heads if inside(bbox(h[0]), pb, 0.3)]
    gaps = [bbox(b)[0] - bbox(a)[2] for a, b in zip(bx, bx[1:])]
    lead, trail = bbox(bx[0])[0] - pb[0], pb[2] - bbox(bx[-1])[2]
    info.append((bx, hs, gaps, lead, trail, pb))
    print(f"   part {k + 1}: {len(bx)} boxes, gaps {[round(g, 2) for g in gaps]} mm, lead {lead:.2f} mm, trail {trail:.2f} mm, "
          f"{len(hs)} arrows, size {pb[2] - pb[0]:.1f} x {pb[3] - pb[1]:.1f} mm")
(bl, hl, gl, _, trail_l, _), (br, hr, gr, lead_r, _, _) = info
check(len(bl) == 3 and len(br) == 3, "p3: three boxes on each part")
check(all(near(g, 12) for g in gl + gr), "p3: 12 mm between neighbouring boxes on each part")
check(near(trail_l + lead_r, 12), f"p3: parts butted end to end leave the same 12 mm gap ({trail_l + lead_r:.2f} mm)")
check(len(hl) == 3 and len(hr) == 2 and all(near(head_dir(v)[0], 1, 0.01) for _, v in hl + hr),
      "p3: arrows point right between boxes 1-2, 2-3, 3-4 (left part) and 4-5, 5-6 (right part)")
gap_ok = all(any(bbox(a)[2] < bbox(h[0])[0] and bbox(h[0])[2] < (bbox(b)[0] if b is not None else 1e9)
                 for a, b in zip(bx, bx[1:] + [None])) for bx, hs, *_ in info for h in hs)
check(gap_ok, "p3: every arrow lies in a gap, clear of the boxes")

# ---------------- pages 4-5: Problem 2 mats
for pn, name, n in ((3, 'frog', 4), (4, 'pig', 5)):
    p = doc[pn]
    ds = p.get_drawings()
    rows = sorted([d for d in ds if is_rounded_box(d, 44)], key=lambda d: bbox(d)[0])
    newsq = [d for d in ds if is_rounded_box(d, 40, filled=(255, 255, 255))]
    lanes = [d for d in ds if is_dashed(d) and len(verts(d)) == 4]
    heads = arrowheads(ds)
    pic = p2_pics[name]
    tag = f"p{pn + 1} ({name} mat)"
    check(len(rows) == n == pic['n'], f"{tag}: {len(rows)} line-up boxes, as in the K-1 Problem 2 picture ({pic['n']})")
    check(all(near(size(d)[0], 44) and near(size(d)[1], 44) for d in rows), f"{tag}: line-up boxes 44 x 44 mm")
    pitch = [bbox(b)[0] - bbox(a)[0] for a, b in zip(rows, rows[1:])]
    check(all(near(v, 52) for v in pitch), f"{tag}: box pitch {min(pitch):.2f}-{max(pitch):.2f} mm (8 mm gaps)")
    check(len(newsq) == 1 and near(size(newsq[0])[0], 40), f"{tag}: one 40 mm newcomer square, as on the big board")
    nb = bbox(newsq[0])
    face = {k for d in ds if contains_pt(nb, centre(bbox(d))) for k, v in FILLS.items() if rgb(d.get('fill')) == v}
    check(face == {name} == pic['face'], f"{tag}: newcomer square shows the {name}, as in the picture ({sorted(face)})")
    row_bottom = max(bbox(d)[3] for d in rows)
    rheads = [h for h in heads if bbox(h[0])[3] <= row_bottom]
    check(len(rheads) == n - 1 == pic['heads'] and all(near(head_dir(v)[0], 1, 0.01) for _, v in rheads)
          and all(any(bbox(a)[2] < bbox(h)[0] and bbox(h)[2] < bbox(b)[0] for a, b in zip(rows, rows[1:])) for h, _ in rheads),
          f"{tag}: {len(rheads)} right-pointing arrows between the line-up boxes, as in the picture")
    check(len(lanes) == n == pic['lanes'], f"{tag}: {len(lanes)} arrow-card lanes, as in the picture ({pic['lanes']})")
    shapes = [lane_shape(verts(d)) for d in lanes]
    check(all(near(w, 23) for w, *_ in shapes), f"{tag}: lanes 23 mm wide ({min(s[0] for s in shapes):.2f}-{max(s[0] for s in shapes):.2f} mm)")
    check(all(all(near(a, 90, 0.5) for a in s[4]) for s in shapes), f"{tag}: lanes are rectangles")
    Ls = [s[1] for s in shapes]
    check(all(L >= L_card + 3 for L in Ls), f"{tag}: every lane holds a {L_card:.0f} mm arrow card with 3 mm to spare (lanes {min(Ls):.1f}-{max(Ls):.1f} mm)")
    # each lane joins one line-up box to the newcomer square
    served = []
    gaps = []
    clear_ok = True
    for d, (w, L, m1, m2, _) in zip(lanes, shapes):
        top, bot = (m1, m2) if m1[1] < m2[1] else (m2, m1)
        dists = [dist_to_box(top, bbox(r)) for r in rows]
        j = dists.index(min(dists))
        served.append(j)
        poly = verts(d)
        gap_row = poly_dist(poly, box_poly(bbox(rows[j])))
        gap_new = poly_dist(poly, box_poly(nb))
        gaps.append((round(gap_row, 1), round(gap_new, 1)))
        clear_ok &= 1.0 <= gap_row <= 3 and 1.0 <= gap_new <= 3
        for r in rows + newsq:
            clear_ok &= area(clip(poly, box_poly(bbox(r), 1.0))) < 0.01
    check(sorted(served) == list(range(n)) and clear_ok,
          f"{tag}: one lane from each line-up box to the newcomer, 1-3 mm from each (gaps {gaps} mm) and at least 1 mm clear of every box")
    # nothing printed in the lanes (no arrows that could suggest results)
    lane_polys = [verts(d) for d in lanes]
    stray = [h for h in heads if h not in rheads]
    check(not stray, f"{tag}: no arrowheads anywhere except between the line-up boxes (lanes are blank)")
    # information: lane overlaps near the newcomer, and worst-case arrowhead cover
    ext = []
    for a, (w, L, m1, m2, _) in zip(lane_polys, shapes):
        bot = m1 if m1[1] > m2[1] else m2
        top = m2 if bot is m1 else m1
        ux, uy = (top[0] - bot[0]) / L, (top[1] - bot[1]) / L
        e = 0
        for b in lane_polys:
            if b is a:
                continue
            ov = clip(a, b)
            if area(ov) > 0.01:
                e = max(e, max((q[0] - bot[0]) * ux + (q[1] - bot[1]) * uy for q in ov))
        ext.append(round(e, 1))
    # cards centred in their lanes and pushed against the newcomer, head pointing at it
    cards, cheads = [], []
    for v, (w, L, m1, m2, _) in zip(lane_polys, shapes):
        bot, top = (m1, m2) if m1[1] > m2[1] else (m2, m1)
        ux, uy = (top[0] - bot[0]) / L, (top[1] - bot[1]) / L
        nx, ny = -uy, ux
        a = (bot[0] + ux * 1.5, bot[1] + uy * 1.5)
        b = (a[0] + ux * L_card, a[1] + uy * L_card)
        hw = W_card / 2
        cards.append([(a[0] + nx * hw, a[1] + ny * hw), (b[0] + nx * hw, b[1] + ny * hw),
                      (b[0] - nx * hw, b[1] - ny * hw), (a[0] - nx * hw, a[1] - ny * hw)])
        tip = (a[0] + ux * 3, a[1] + uy * 3)
        base = (tip[0] + ux * 15, tip[1] + uy * 15)
        cheads.append([tip, (base[0] + nx * 6.5, base[1] + ny * 6.5), (base[0] - nx * 6.5, base[1] - ny * 6.5)])
    cc = max(area(clip(cards[i], cards[j])) for i in range(n) for j in range(n) if i != j)
    hc = max(area(clip(cheads[i], cards[j])) for i in range(n) for j in range(n) if i != j)
    check(hc < 0.01, f"{tag}: cards centred in their lanes never cover a neighbour's arrowhead, even pushed against the "
          f"newcomer (largest card-on-card overlap {cc:.1f} mm2)")
    print(f"   info {tag}: lane lengths {[round(L, 1) for L in Ls]} mm; neighbouring lanes overlap up to "
          f"{ext} mm from the newcomer end (like the big board's crossing diagonals)")

print()
if FAILS:
    print(f"{len(FAILS)} check(s) FAILED")
    sys.exit(1)
print("All checks passed.")
