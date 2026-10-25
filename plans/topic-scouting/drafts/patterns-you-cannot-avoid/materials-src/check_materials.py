"""Measure the delivered materials PDF and compare it with the student pages.

Run: python3 check_materials.py ../materials.pdf

Two independent measurements:
  1. Drawn paths and text read from the PDF with PyMuPDF (exact geometry, in mm).
  2. A 300 dpi render (pdftoppm) measured in pixels, for comb windows, strip squares and cards.
Every key size must be within 0.5 mm of its target. The script also measures the student pages
(K-1 strip squares and gaps, upper-band Problem 1 strips, the six-dot boards, the number rows)
so that every object is checked against the problem that uses it. Exit status 1 on any failure.
"""
import math
import subprocess
import sys
import tempfile
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
import pymupdf
from PIL import Image

MM = 25.4 / 72          # mm per PDF point
TOL = 0.5               # mm
EDGE = 12.0             # minimum distance from every paper edge, mm
COUNTER = 22.0          # widest counter the guide allows, mm
HERE = Path(__file__).resolve().parent
STUDENT = HERE.parent

failures = []
lines_out = []


def check(ok, msg):
    lines_out.append(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        failures.append(msg)


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


def mm(v):
    return v * MM


# ---------------------------------------------------------------- PDF helpers
def drawings(page):
    return page.get_drawings()


def is_square_path(d, side):
    return (len(d['items']) == 4 and all(i[0] == 'l' for i in d['items'])
            and near(mm(d['rect'].width), side) and near(mm(d['rect'].height), side))


def squares(page, side=25.0):
    return [d['rect'] for d in drawings(page) if is_square_path(d, side)]


def words(page):
    """(text, bbox in mm) for every word on the page."""
    return [(w[4], pymupdf.Rect(w[:4]) * MM) for w in page.get_text('words')]


def spans(page):
    out = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for sp in line['spans']:
                if sp['text'].strip():
                    out.append((sp['text'], pymupdf.Rect(sp['bbox']) * MM))
    return out


def rows_of(rects, key=lambda r: r.y0):
    rows = defaultdict(list)
    for r in rects:
        rows[round(mm(key(r)), 1)].append(r)
    return [sorted(rows[k], key=lambda r: r.x0) for k in sorted(rows)]


def numbers_under(page, row):
    """The number printed under each square of a strip row, read from the page text."""
    ws = words(page)
    got = []
    for r in row:
        x0, x1, bottom = mm(r.x0), mm(r.x1), mm(r.y1)
        found = [t for t, b in ws if x0 < (b.x0 + b.x1) / 2 < x1 and bottom < b.y0 < bottom + 8]
        got.append(found[0] if len(found) == 1 else None)
    return got


def circles(page, dmin, dmax, filled=None):
    """Closed curve paths (circles) with a diameter between dmin and dmax mm."""
    out = []
    for d in drawings(page):
        if not d['items'] or any(i[0] != 'c' for i in d['items']):
            continue
        w, h = mm(d['rect'].width), mm(d['rect'].height)
        if not (dmin <= w <= dmax and abs(w - h) < 0.05):
            continue
        if filled is True and d['fill'] is None:
            continue
        if filled is False and d['fill'] is not None:
            continue
        out.append(d['rect'])
    return out


def segments(page, colour=None):
    out = []
    for d in drawings(page):
        if colour is not None and (d['color'] is None or any(abs(a - b) > 0.02 for a, b in zip(d['color'], colour))):
            continue
        for it in d['items']:
            if it[0] == 'l':
                out.append(((mm(it[1].x), mm(it[1].y)), (mm(it[2].x), mm(it[2].y)), d))
    return out


def render(pdf, pno, dpi=300):
    with tempfile.TemporaryDirectory() as td:
        stem = Path(td) / 'p'
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(pno), '-l', str(pno), '-gray', '-png',
                        str(pdf), str(stem)], check=True)
        png = next(Path(td).glob('p*.png'))
        return np.array(Image.open(png).convert('L')), dpi / 25.4


def runs(row, dark=128):
    """(start, end) pixel runs of dark pixels along one row of a greyscale image."""
    d = row < dark
    edges = np.flatnonzero(np.diff(d.astype(int)))
    out, start = [], None
    for e in edges:
        if not d[e] and d[e + 1]:
            start = e + 1
        elif d[e] and not d[e + 1] and start is not None:
            out.append((start, e))
            start = None
    return out


def stroke_centres(row, dark=128):
    return [(a + b) / 2 for a, b in runs(row, dark)]


# ---------------------------------------------------------------- whole-document checks
def check_frame(doc):
    expected = [('landscape', 'Combs'), ('landscape', 'Strips of 6, 7, 8 and 9 squares'),
                ('portrait', 'Cards 1 to 15'), ('landscape', 'Boards of six dots')]
    check(len(doc) == 4, f'page count {len(doc)} (expected 4)')
    for pno, page in enumerate(doc, 1):
        w, h = mm(page.rect.width), mm(page.rect.height)
        orient = 'landscape' if w > h else 'portrait'
        exp_orient, title = expected[pno - 1]
        check(near(min(w, h), 215.9) and near(max(w, h), 279.4) and orient == exp_orient,
              f'p{pno}: US Letter {orient} ({w:.1f} x {h:.1f} mm)')
        text = [t for t, _ in spans(page)]
        check(text[0] == 'Week NN / Patterns you cannot avoid / Materials', f'p{pno}: header "{text[0]}"')
        check('Bellingham Math Circle / Week NN / NN-M-v1' in text and str(pno) in text,
              f'p{pno}: footer and page number {pno}')
        check(title in text, f'p{pno}: title "{title}"')
        # every mark at least 12 mm from every edge (strokes include half their width)
        worst = 1e9
        for d in drawings(page):
            r = d['rect'] * MM
            hw = mm(d.get('width') or 0) / 2 if d['type'] != 'f' else 0
            worst = min(worst, r.x0 - hw, r.y0 - hw, w - r.x1 - hw, h - r.y1 - hw)
        for _, r in spans(page):
            worst = min(worst, r.x0, r.y0, w - r.x1, h - r.y1)
        check(worst >= EDGE, f'p{pno}: nearest mark {worst:.1f} mm from a paper edge (minimum {EDGE:.0f})')


def check_text_inventory(doc):
    """Only the header, footer, title and object labels: no instructions, colours or answers."""
    frame = {'Week NN / Patterns you cannot avoid / Materials', 'Bellingham Math Circle / Week NN / NN-M-v1'}
    allowed = {
        1: frame | {'1', 'Combs', 'Comb 1', 'Comb 2', 'Comb 3', 'Comb 4', '100 mm'},
        2: frame | {'2', 'Strips of 6, 7, 8 and 9 squares'} | {str(i) for i in range(1, 10)},
        3: frame | {'Cards 1 to 15', 'Launch strip of 5 squares'} | {str(i) for i in range(1, 16)},
        4: frame | {'4', 'Boards of six dots'},
    }
    for pno, page in enumerate(doc, 1):
        extra = sorted({t for t, _ in spans(page)} - allowed[pno])
        check(not extra, f'p{pno}: text is labels only' + (f' (unexpected: {extra})' if extra else ''))
        fills = [d['fill'] for d in drawings(page) if d['fill'] is not None]
        coloured = [c for c in fills if max(c) - min(c) > 0.01]
        check(not coloured, f'p{pno}: no coloured fills (no counters or colourings printed)')


# ---------------------------------------------------------------- page 1: combs
def comb_polygons(page):
    out = []
    for d in drawings(page):
        if d['fill'] is None or d['type'] != 'fs':
            continue
        if not all(i[0] == 'l' for i in d['items']):
            continue
        pts = [(mm(i[1].x), mm(i[1].y)) for i in d['items']]
        out.append((d['rect'] * MM, pts))
    return out


def comb_geometry(rect, pts):
    """Length, height, notch intervals and notch depth of one comb outline."""
    top, bottom = rect.y0, rect.y1
    inner = sorted({round(x, 3) for x, y in pts if top + 0.5 < y < bottom - 0.5})
    notch_y = sorted({round(y, 3) for x, y in pts if top + 0.5 < y < bottom - 0.5})
    windows = [(inner[k] - rect.x0, inner[k + 1] - rect.x0) for k in range(0, len(inner), 2)]
    depth = bottom - notch_y[0] if len(notch_y) == 1 else None
    return rect.width, rect.height, windows, depth


def check_combs(doc, k1_pitch, k1_min_gap):
    page = doc[0]
    polys = comb_polygons(page)
    check(len(polys) == 4, f'p1: four comb outlines found ({len(polys)})')
    labels = {t: r for t, r in spans(page)}
    found = {}
    for rect, pts in polys:
        L, H, windows, depth = comb_geometry(rect, pts)
        d = round((L - 10) / 25 - 1) // 2
        label = labels.get(f'Comb {d}')
        found[d] = (rect, windows, depth)
        exp_L = (2 * d + 1) * 25 + 10
        check(near(L, exp_L), f'Comb {d}: length {L:.2f} mm (target {exp_L:.1f})')
        check(near(H, 34.0), f'Comb {d}: height {H:.2f} mm (target 34.0)')
        check(depth is not None and near(depth, 27.0) and depth > 25 + TOL,
              f'Comb {d}: notch depth {depth:.2f} mm (target 27.0; deeper than a 25 mm square)')
        if d == 1:
            wd = windows[0][1] - windows[0][0]
            check(len(windows) == 1 and near(wd, 73.0),
                  f'Comb 1: one notch {wd:.2f} mm wide over three squares (target 73.0 = 75 less 1 mm each side)')
            centres = [(windows[0][0] + windows[0][1]) / 2 - k1_pitch, (windows[0][0] + windows[0][1]) / 2,
                       (windows[0][0] + windows[0][1]) / 2 + k1_pitch]
        else:
            widths = [b - a for a, b in windows]
            check(len(windows) == 3 and all(near(wd, 23.0) for wd in widths),
                  f'Comb {d}: three windows {", ".join(f"{wd:.2f}" for wd in widths)} mm wide (target 23.0)')
            centres = [(a + b) / 2 for a, b in windows]
            pitch = [centres[1] - centres[0], centres[2] - centres[1]]
            check(all(near(p, d * k1_pitch) for p in pitch),
                  f'Comb {d}: window centres {pitch[0]:.2f} and {pitch[1]:.2f} mm apart = {d} K-1 squares '
                  f'({d} x {k1_pitch:.2f} mm)')
        # laid with its left end 5 mm before square 1, each window is centred on its square
        offs = [c - (5.0 + 12.5 + k * d * 25.0) for k, c in enumerate(centres)]
        check(all(abs(o) <= TOL for o in offs) and near(windows[0][0], 6.0) and near(L - windows[-1][1], 6.0),
              f'Comb {d}: windows centred on squares 1, {1 + d}, {1 + 2 * d} (off by {max(map(abs, offs)):.2f} mm); '
              f'end posts {windows[0][0]:.2f} and {L - windows[-1][1]:.2f} mm (target 6.0)')
        spine_bottom = rect.y1 - depth
        check(label is not None and rect.x0 < label.x0 and label.x1 < rect.x1 and rect.y0 < label.y0
              and label.y1 < spine_bottom + 0.3, f'Comb {d}: label "Comb {d}" lies on its spine')
    check(sorted(found) == [1, 2, 3, 4], f'p1: combs for spacings {sorted(found)} (expected 1-4)')
    # reach above a strip when the tooth tips rest on the strip's lower edge
    reach = 34.0 - 25.0
    room = k1_min_gap + (25.0 - COUNTER) / 2
    check(reach < room, f'Comb reach {reach:.1f} mm above a strip < {room:.1f} mm to the counters of the strip above '
                        f'(closest K-1 strips {k1_min_gap:.1f} mm apart, counters <= {COUNTER:.0f} mm)')
    # every equally spaced three on 9 squares is seen by exactly one comb position
    triples = {(a, a + s, a + 2 * s) for s in range(1, 5) for a in range(1, 10 - 2 * s)}
    check(len(triples) == 16, f'four combs on a strip of 9 show all {len(triples)} equally spaced threes')
    # scale bar
    bars = [s for s in segments(page, (0, 0, 0)) if s[2]['fill'] is None and near(s[0][1], s[1][1], 0.01)
            and abs(s[1][0] - s[0][0]) > 50]
    check(len(bars) == 1 and near(abs(bars[0][1][0] - bars[0][0][0]), 100.0) and '100 mm' in labels,
          f'p1: scale bar {abs(bars[0][1][0] - bars[0][0][0]):.2f} mm labelled 100 mm')
    return found


def check_combs_pixels(pdf, found):
    img, px = render(pdf, 1)
    for d, (rect, windows, depth) in sorted(found.items()):
        y = int((rect.y1 - depth / 2) * px)         # halfway up the notches
        x0, x1 = int((rect.x0 - 2) * px), int((rect.x1 + 2) * px)
        row = img[y, x0:x1]
        # light pixels inside the comb's outer outline are the notches (the card is grey)
        white = row > 245
        edges = np.flatnonzero(np.diff(white.astype(int)))
        spans_px = [(edges[k] + 1, edges[k + 1]) for k in range(len(edges) - 1) if not white[edges[k]] and white[edges[k] + 1]]
        widths = [(b - a + 1) / px for a, b in spans_px if (b - a + 1) / px > 10]
        exp = [73.0] if d == 1 else [23.0] * 3
        # the 0.6 pt outline is centred on the cut line, so each notch shows 0.21 mm less paper
        ok = len(widths) == len(exp) and all(near(w + 0.21, e) for w, e in zip(widths, exp))
        check(ok, f'Comb {d} at 300 dpi: notch widths {", ".join(f"{w + 0.21:.2f}" for w in widths)} mm '
                  f'(cut line to cut line; target {exp[0]:.0f})')


# ---------------------------------------------------------------- page 2: strips
def check_strips(doc, upper_p1_lengths):
    page = doc[1]
    rows = rows_of(squares(page))
    lengths = [len(r) for r in rows]
    check(lengths == [6, 7, 8, 9], f'p2: strips of {lengths} squares (expected 6, 7, 8, 9)')
    check(lengths == upper_p1_lengths, f'p2: same lengths as Problem 1 of Grades 2-3 and 4-5 ({upper_p1_lengths})')
    for row in rows:
        sizes = [(mm(r.width), mm(r.height)) for r in row]
        pitch = [mm(row[i + 1].x0 - row[i].x0) for i in range(len(row) - 1)]
        check(all(near(a, 25) and near(b, 25) for a, b in sizes) and all(near(p, 25) for p in pitch),
              f'p2: strip of {len(row)}: squares {min(a for a, _ in sizes):.2f}-{max(a for a, _ in sizes):.2f} mm, '
              f'pitch {min(pitch):.2f}-{max(pitch):.2f} mm (target 25.0)')
        nums = numbers_under(page, row)
        check(nums == [str(i) for i in range(1, len(row) + 1)], f'p2: strip of {len(row)} numbered {nums}')
    tops = [mm(r[0].y0) for r in rows]
    gaps = [tops[i + 1] - tops[i] - 25 for i in range(len(tops) - 1)]
    check(all(g > 34.0 - 25.0 + (25 - COUNTER) / 2 for g in gaps) or all(g >= 11 for g in gaps),
          f'p2: {min(gaps):.1f} mm between strips (combs clear the strip above)')
    return rows


def check_strip_pixels(pdf, pno, rows, label):
    img, px = render(pdf, pno)
    for row in rows:
        y = int((mm(row[0].y0) + 12.5) * px)
        x0, x1 = int((mm(row[0].x0) - 3) * px), int((mm(row[-1].x1) + 3) * px)
        cents = stroke_centres(img[y, x0:x1])
        pitch = [(cents[i + 1] - cents[i]) / px for i in range(len(cents) - 1)]
        ok = len(pitch) == len(row) and all(near(p, 25.0) for p in pitch)
        check(ok, f'{label}: strip of {len(row)} at 300 dpi: square widths {min(pitch):.2f}-{max(pitch):.2f} mm')


# ---------------------------------------------------------------- page 3: cards and launch strip
def check_cards(doc, max_number_on_pages):
    page = doc[2]
    segs = [s for s in segments(page, (0, 0, 0)) if near(mm(s[2]['width']), 0.5 * MM, 0.01)]
    xs = sorted({round(s[0][0], 2) for s in segs if near(s[0][0], s[1][0], 0.01)})
    ys = sorted({round(s[0][1], 2) for s in segs if near(s[0][1], s[1][1], 0.01)})
    cw = [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
    ch = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
    check(len(cw) == 5 and len(ch) == 3 and all(near(c, 36) for c in cw) and all(near(c, 48) for c in ch),
          f'p3: {len(cw)} x {len(ch)} cards on shared cut lines, {min(cw):.2f}-{max(cw):.2f} x '
          f'{min(ch):.2f}-{max(ch):.2f} mm (target 36 x 48)')
    spots = circles(page, 20, 30, filled=False)
    ws = [(t, b) for t, b in words(page) if t.isdigit() and b.y1 < ys[-1] + 1]
    seen = []
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            cell = pymupdf.Rect(xs[i], ys[j], xs[i + 1], ys[j + 1])
            cs = [c * MM for c in spots if cell.contains(c * MM)]
            ns = [(t, b) for t, b in ws if cell.contains(b)]
            if len(cs) != 1 or len(ns) != 1:
                check(False, f'p3: card at column {i + 1}, row {j + 1} has {len(cs)} counter spots and {len(ns)} numbers')
                continue
            c, (t, b) = cs[0], ns[0]
            seen.append(int(t))
            if not (near(c.width, 26) and c.width > COUNTER + 1 and not c.intersects(b)):
                check(False, f'p3: card {t}: spot {c.width:.2f} mm, clear of its number: {not c.intersects(b)}')
    check(sorted(seen) == list(range(1, 16)), f'p3: cards numbered {sorted(seen)}')
    check(len(seen) == 15 and all(near(c.width * MM, 26) for c in spots),
          f'p3: every card has a {mm(spots[0].width):.2f} mm counter spot (fits a {COUNTER:.0f} mm counter) above its number')
    check(max(seen) == max_number_on_pages, f'p3: cards go to {max(seen)}, as far as the longest number row on the pages '
                                           f'({max_number_on_pages})')
    # launch strip
    rows = rows_of(squares(page))
    check(len(rows) == 1 and len(rows[0]) == 5, f'p3: launch strip of {len(rows[0]) if rows else 0} squares (expected 5)')
    sizes = [mm(r.width) for r in rows[0]]
    check(all(near(s, 25) for s in sizes), f'p3: launch strip squares {min(sizes):.2f}-{max(sizes):.2f} mm')
    check(numbers_under(page, rows[0]) == ['1', '2', '3', '4', '5'], 'p3: launch strip numbered 1-5')
    return xs, ys, rows


def check_card_pixels(pdf, xs, ys):
    img, px = render(pdf, 3)
    y = int((ys[0] + 46.0) * px)            # below the numbers, inside the first row of cards
    cents = stroke_centres(img[y, int((xs[0] - 3) * px):int((xs[-1] + 3) * px)])
    pitch = [(cents[i + 1] - cents[i]) / px for i in range(len(cents) - 1)]
    check(len(pitch) == 5 and all(near(p, 36) for p in pitch),
          f'p3 at 300 dpi: card widths {min(pitch):.2f}-{max(pitch):.2f} mm (target 36)')
    x = int((xs[0] + 2.0) * px)
    cents = stroke_centres(img[int((ys[0] - 3) * px):int((ys[-1] + 3) * px), x])
    pitch = [(cents[i + 1] - cents[i]) / px for i in range(len(cents) - 1)]
    check(len(pitch) == 3 and all(near(p, 48) for p in pitch),
          f'p3 at 300 dpi: card heights {min(pitch):.2f}-{max(pitch):.2f} mm (target 48)')


# ---------------------------------------------------------------- page 4: boards of six dots
def boards(page, dmin=1.5, dmax=4.0):
    """Dots grouped into boards: two dots are on one board when a drawn line joins them."""
    dots = [c * MM for c in circles(page, dmin, dmax, filled=True)]
    centres = [((c.x0 + c.x1) / 2, (c.y0 + c.y1) / 2) for c in dots]
    segs = segments(page)
    parent = list(range(len(centres)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for a, b, _ in segs:
        ia = [i for i, p in enumerate(centres) if math.dist(p, a) < TOL]
        ib = [i for i, p in enumerate(centres) if math.dist(p, b) < TOL]
        if ia and ib:
            parent[find(ia[0])] = find(ib[0])
    groups = defaultdict(list)
    for i, p in enumerate(centres):
        groups[find(i)].append(p)
    return sorted(groups.values(), key=lambda g: min(g)), segs


def board_shape(pts):
    cx, cy = np.mean(pts, axis=0)
    radii = [math.dist(p, (cx, cy)) for p in pts]
    # angles measured counterclockwise from the right, y up
    ang = sorted((math.degrees(math.atan2(cy - y, x - cx)) % 360) for x, y in pts)
    return (cx, cy), radii, ang


def check_boards(doc, student_angles):
    page = doc[3]
    groups, segs = boards(page)
    check(len(groups) == 2 and all(len(g) == 6 for g in groups),
          f'p4: {len(groups)} boards of {[len(g) for g in groups]} dots (expected 2 of 6)')
    for k, pts in enumerate(groups, 1):
        (cx, cy), radii, ang = board_shape(pts)
        diam = 2 * np.mean(radii)
        check(near(diam, 120) and max(radii) - min(radii) < 0.1,
              f'p4 board {k}: dots on a circle {diam:.2f} mm across (target 120; outline: about 12 cm)')
        gaps = [(ang[(i + 1) % 6] - ang[i]) % 360 for i in range(6)]
        sides = sorted(math.dist(a, b) for a, b in combinations(pts, 2))[:6]
        check(all(abs(g - 60) < 0.2 for g in gaps) and max(sides) - min(sides) < 0.1,
              f'p4 board {k}: regular hexagon, angles {min(gaps):.2f}-{max(gaps):.2f} deg, sides '
              f'{min(sides):.2f}-{max(sides):.2f} mm')
        check(all(min(abs(a - s), 360 - abs(a - s)) < 0.5 for a, s in zip(ang, student_angles)),
              f'p4 board {k}: dots at {[round(a) for a in ang]} deg, as on the student boards {[round(a) for a in student_angles]}')
        pairs = set()
        for a, b, _ in segs:
            ia = [i for i, p in enumerate(pts) if math.dist(p, a) < TOL]
            ib = [i for i, p in enumerate(pts) if math.dist(p, b) < TOL]
            if ia and ib:
                pairs.add(tuple(sorted((ia[0], ib[0]))))
        lines = [s for s in segs if any(math.dist(p, s[0]) < TOL for p in pts)]
        check(len(pairs) == 15 and len(lines) == 15,
              f'p4 board {k}: {len(lines)} lines joining all {len(pairs)} pairs of dots (expected 15)')


# ---------------------------------------------------------------- student pages
def student_facts():
    k1 = pymupdf.open(STUDENT / 'k-1.pdf')
    sq, gaps, pitch = [], [], []
    for page in k1:
        rows = rows_of(squares(page))
        if not rows:
            continue
        for row in rows:
            sq += [mm(r.width) for r in row]
            pitch += [mm(row[i + 1].x0 - row[i].x0) for i in range(len(row) - 1)]
        tops = [mm(r[0].y0) for r in rows]
        gaps += [tops[i + 1] - tops[i] - 25 for i in range(len(tops) - 1)]
    check(all(near(s, 25) for s in sq), f'K-1 pages: {len(sq)} strip squares, {min(sq):.2f}-{max(sq):.2f} mm')
    k1_pitch = float(np.mean(pitch))
    check(near(k1_pitch, 25), f'K-1 pages: square pitch {min(pitch):.2f}-{max(pitch):.2f} mm')
    lengths = {}
    for band in ('grades-2-3', 'grades-4-5'):
        page = pymupdf.open(STUDENT / f'{band}.pdf')[0]
        rows = rows_of(squares(page, 15.0))
        lengths[band] = [len(r) for r in rows]
    check(lengths['grades-2-3'] == lengths['grades-4-5'],
          f'Problem 1 strips: Grades 2-3 {lengths["grades-2-3"]}, Grades 4-5 {lengths["grades-4-5"]}')
    # six-dot boards on the student pages: Grades 2-3 page 6 (Problem 7), Grades 4-5 page 5 (Problems 6-7)
    angles = []
    for band, pno in (('grades-2-3', 5), ('grades-4-5', 4), ('grades-4-5', 5)):
        page = pymupdf.open(STUDENT / f'{band}.pdf')[pno]
        groups, segs = boards(page, 1.5, 3.0)
        for g in groups:
            if len(g) == 6:
                angles.append(board_shape(g)[2])
    check(len(angles) >= 3 and all(all(abs(a - b) < 0.5 for a, b in zip(angles[0], x)) for x in angles),
          f'student six-dot boards ({len(angles)} measured) all have dots at {[round(a) for a in angles[0]]} deg')
    # longest number row on the pages
    biggest = 0
    for band in ('grades-2-3', 'grades-4-5'):
        for page in pymupdf.open(STUDENT / f'{band}.pdf'):
            ws = words(page)
            for c in circles(page, 7.5, 9.5, filled=False):
                c = c * MM
                under = [int(t) for t, b in ws if t.isdigit() and c.x0 < (b.x0 + b.x1) / 2 < c.x1
                         and c.y1 < b.y0 < c.y1 + 6]
                biggest = max([biggest] + under)
    check(biggest == 15, f'student number rows go up to {biggest}')
    # cards 1-4 and 1-5 are named on Grades 2-3 page 4
    txt = pymupdf.open(STUDENT / 'grades-2-3.pdf')[3].get_text()
    check('cards 1, 2, 3 and 4' in txt.replace('\n', ' ') and 'cards 1, 2, 3, 4 and 5' in txt.replace('\n', ' '),
          'Grades 2-3 page 4 names "cards 1, 2, 3 and 4" and "cards 1, 2, 3, 4 and 5"')
    return k1_pitch, min(gaps), lengths['grades-2-3'], angles[0], biggest


def main():
    pdf = Path(sys.argv[1] if len(sys.argv) > 1 else HERE.parent / 'materials.pdf').resolve()
    doc = pymupdf.open(pdf)
    k1_pitch, k1_gap, upper_lengths, student_angles, biggest = student_facts()
    check_frame(doc)
    check_text_inventory(doc)
    found = check_combs(doc, k1_pitch, k1_gap)
    check_combs_pixels(pdf, found)
    rows = check_strips(doc, upper_lengths)
    check_strip_pixels(pdf, 2, rows, 'p2')
    xs, ys, launch = check_cards(doc, biggest)
    check_card_pixels(pdf, xs, ys)
    check_strip_pixels(pdf, 3, launch, 'p3 launch')
    check_boards(doc, student_angles)
    print('\n'.join(lines_out))
    print(f'\n{len(lines_out) - len(failures)} passed, {len(failures)} failed')
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
