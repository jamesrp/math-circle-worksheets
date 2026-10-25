"""Check the delivered materials.pdf for Graceful labels by measuring it.

Usage: python3 check_materials.py [path/to/materials.pdf]

Everything is read from PDFs, not from the generator:
  * vector paths and text spans of materials.pdf (PyMuPDF), in millimetres;
  * a 300 dpi rendering of materials.pdf, measured in pixels, as a second
    measurement of the card pitch, strip squares and dot diameters;
  * the final student packets, so that each board is compared with the
    drawing of the problem that uses it, and the measured number card is
    tried on every card board the packets print.
Fails (exit status 1) when a key size is off by more than 0.5 mm, when a
board's shape differs from its problem, when anything sits within 12 mm of
a paper edge, or when a page carries text other than its labels.
"""
import math
import os
import subprocess
import sys
import tempfile

import numpy as np
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PACKETS = os.path.dirname(HERE)
MAT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "materials.pdf")

PT = 25.4 / 72.0          # mm per PDF point
TOL = 0.5                 # mm
EDGE = 12.0               # mm
CARD = 20.0
STRIP_SQ = 23.0

failures = []


def check(ok, msg):
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        failures.append(msg)


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


# ------------------------------------------------------------------ geometry
def shapes(page):
    """Rectangles, circles, single lines and filled marks on a page, in mm."""
    rects, circles, lines, fills = [], [], [], []
    for d in page.get_drawings():
        items = d["items"]
        kinds = [it[0] for it in items]
        r = d["rect"]
        if kinds == ["c"] * 4:
            pts = [p for it in items for p in (it[1], it[4])]
            xs = [p.x * PT for p in pts]
            ys = [p.y * PT for p in pts]
            circles.append(dict(cx=(min(xs) + max(xs)) / 2, cy=(min(ys) + max(ys)) / 2,
                                dx=max(xs) - min(xs), dy=max(ys) - min(ys)))
        elif kinds == ["l"] * 4 and d.get("color") is not None:
            pts = [it[1] for it in items] + [items[-1][2]]
            xs = sorted({round(p.x, 2) for p in pts})
            ys = sorted({round(p.y, 2) for p in pts})
            if len(xs) == 2 and len(ys) == 2:
                rects.append(dict(x0=r.x0 * PT, y0=r.y0 * PT, x1=r.x1 * PT, y1=r.y1 * PT,
                                  w=(r.x1 - r.x0) * PT, h=(r.y1 - r.y0) * PT))
        elif kinds == ["l"] and d.get("color") is not None:
            a, b = items[0][1], items[0][2]
            lines.append(((a.x * PT, a.y * PT), (b.x * PT, b.y * PT), d.get("width") or 0))
        if d.get("fill") is not None and d.get("color") is None:
            fills.append(dict(x0=r.x0 * PT, y0=r.y0 * PT, x1=r.x1 * PT, y1=r.y1 * PT,
                              sig=tuple(kinds), fill=d["fill"]))
    return rects, circles, lines, fills


def spans(page):
    t = page.get_text("dict")
    out = []
    for b in t["blocks"]:
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if s["text"].strip():
                    x0, y0, x1, y1 = s["bbox"]
                    out.append(dict(text=s["text"].strip(), x0=x0 * PT, y0=y0 * PT, x1=x1 * PT,
                                    y1=y1 * PT, cx=(x0 + x1) / 2 * PT, size=s["size"]))
    return out


def networks(circles, rects, lines, dot_d, box_s, tol=0.6):
    """Group dots of diameter dot_d joined by centre-to-centre lines into
    networks; return [(dots, edges, boxes)] with boxes of side box_s."""
    dots = [c for c in circles if near(c["dx"], dot_d, tol) and near(c["dy"], dot_d, tol)]
    boxes = [r for r in rects if near(r["w"], box_s, tol) and near(r["h"], box_s, tol)]

    def at(p):
        for i, c in enumerate(dots):
            if math.hypot(p[0] - c["cx"], p[1] - c["cy"]) < 0.6:
                return i
        return None

    edges = set()
    for a, b, _ in lines:
        i, j = at(a), at(b)
        if i is not None and j is not None and i != j:
            edges.add((min(i, j), max(i, j)))
    parent = list(range(len(dots)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, j in edges:
        parent[find(i)] = find(j)
    groups = {}
    for i in range(len(dots)):
        groups.setdefault(find(i), []).append(i)
    nets = []
    for g in groups.values():
        gs = set(g)
        e = [(i, j) for (i, j) in edges if i in gs]
        nets.append(([dots[i] for i in g], [(g.index(i), g.index(j)) for (i, j) in e], g))
    return nets, boxes


def grid_shape(dots, edges):
    """Dot positions and links in grid units (separate x and y units), so that
    a board can be compared with a smaller drawing of the same tree."""
    ux = min((abs(dots[i]["cx"] - dots[j]["cx"]) for i, j in edges
              if abs(dots[i]["cx"] - dots[j]["cx"]) > 1), default=1)
    uy = min((abs(dots[i]["cy"] - dots[j]["cy"]) for i, j in edges
              if abs(dots[i]["cy"] - dots[j]["cy"]) > 1), default=1)
    x0 = min(d["cx"] for d in dots)
    y0 = min(d["cy"] for d in dots)
    g = [(round((d["cx"] - x0) / ux), round((d["cy"] - y0) / uy)) for d in dots]
    off = max(max(abs((d["cx"] - x0) / ux - gx), abs((d["cy"] - y0) / uy - gy))
              for d, (gx, gy) in zip(dots, g))
    return set(g), {frozenset((g[i], g[j])) for i, j in edges}, off


def rect_point_dist(r, x, y):
    return math.hypot(max(r["x0"] - x, 0, x - r["x1"]), max(r["y0"] - y, 0, y - r["y1"]))


def card_room(dots, boxes):
    """For each dot: the largest upright square card centred on it that covers
    no link box and no card on another dot (as check_geom.py defines it), and
    the distance from its centre to the nearest box."""
    out = []
    for i, c in enumerate(dots):
        s = 1e9
        near_box = 1e9
        for b in boxes:
            bx, by = (b["x0"] + b["x1"]) / 2, (b["y0"] + b["y1"]) / 2
            h = max(b["w"], b["h"]) / 2
            s = min(s, 2 * (max(abs(bx - c["cx"]), abs(by - c["cy"])) - h))
            near_box = min(near_box, rect_point_dist(b, c["cx"], c["cy"]))
        for j, o in enumerate(dots):
            if j != i:
                s = min(s, max(abs(o["cx"] - c["cx"]), abs(o["cy"] - c["cy"])))
        out.append((s, near_box))
    return out


# ------------------------------------------------------------------ pixels
def render(path, page, dpi=300):
    tmp = tempfile.mkdtemp()
    base = os.path.join(tmp, "p")
    subprocess.run(["pdftoppm", "-r", str(dpi), "-gray", "-f", str(page), "-l", str(page),
                    "-png", path, base], check=True)
    f = [x for x in os.listdir(tmp) if x.endswith(".png")][0]
    return np.array(Image.open(os.path.join(tmp, f)).convert("L")), 25.4 / dpi


def dark_runs(profile, thresh=128):
    """Centres of the dark runs along a row or column of pixels."""
    dark = profile < thresh
    runs, start = [], None
    for i, v in enumerate(dark):
        if v and start is None:
            start = i
        if not v and start is not None:
            runs.append((start, i - 1))
            start = None
    if start is not None:
        runs.append((start, len(dark) - 1))
    return [((a + b) / 2, a, b) for a, b in runs]


# ================================================================== checks
doc = pymupdf.open(MAT)
print(f"Checking {os.path.relpath(MAT, REPO)}: {doc.page_count} pages\n")
check(doc.page_count == 3, "three pages")

HEADER = "Week NN / Graceful labels / Materials"
FOOTER = "Bellingham Math Circle / Week NN / FNN-M-v1"
EXPECTED_TEXT = {
    1: {HEADER, FOOTER, "1", "Number cards", "Grades 2–3 and 4–5", "50 mm scale check",
        "Strip from 0 to 10", "Grades 4–5 Problem 7"} | {str(i) for i in range(11)},
    2: {HEADER, FOOTER, "2", "Launch sheet", "50 mm scale check"},
    3: {HEADER, FOOTER, "3", "Trees", "Grades 4–5 Problem 9", "cards 0 to 6", "cards 0 to 7",
        "50 mm scale check"},
}

print("== Every page")
for pno, page in enumerate(doc, start=1):
    W, H = page.rect.width * PT, page.rect.height * PT
    check(near(W, 279.4, 0.1) and near(H, 215.9, 0.1), f"p{pno}: US Letter landscape ({W:.1f} x {H:.1f} mm)")
    worst = 1e9
    for d in page.get_drawings():
        r = d["rect"]
        hw = (d.get("width") or 0) / 2 if d.get("color") is not None else 0
        worst = min(worst, (r.x0 - hw) * PT, (r.y0 - hw) * PT, W - (r.x1 + hw) * PT, H - (r.y1 + hw) * PT)
    sp = spans(page)
    for s in sp:
        worst = min(worst, s["x0"], s["y0"], W - s["x1"], H - s["y1"])
    check(worst >= EDGE, f"p{pno}: nearest ink or text box to a paper edge {worst:.1f} mm (>= 12)")
    texts = [s["text"] for s in sp]
    check(texts.count(HEADER) == 1 and min(s["y0"] for s in sp if s["text"] == HEADER) < 25,
          f"p{pno}: header '{HEADER}'")
    foot = [s for s in sp if s["text"] == FOOTER]
    num = [s for s in sp if s["text"] == str(pno) and s["y0"] > H - 25]
    check(len(foot) == 1 and foot[0]["y0"] > H - 25 and len(num) == 1,
          f"p{pno}: footer '{FOOTER}' with page number {pno}")
    extra = sorted(set(texts) - EXPECTED_TEXT[pno])
    check(not extra, f"p{pno}: only labels and numbers, no other text" + (f" (found {extra})" if extra else ""))
    # 50 mm scale check bar
    bars = [l for l in shapes(page)[2] if near(abs(l[1][0] - l[0][0]), 50, 0.3) and near(l[0][1], l[1][1], 0.05)]
    check(len(bars) == 1, f"p{pno}: 50 mm scale check bar measures "
          + (f"{abs(bars[0][1][0] - bars[0][0][0]):.2f} mm" if bars else "missing"))

# ------------------------------------------------------------------ page 1
print("\n== Page 1: number cards")
p1 = doc[0]
rects, circles, lines, fills = shapes(p1)
sp1 = spans(p1)
cards = [r for r in rects if near(r["w"], CARD, 1.5) and near(r["h"], CARD, 1.5)]
check(len(cards) == 55, f"55 card outlines found ({len(cards)})")
ws = [r["w"] for r in cards] + [r["h"] for r in cards]
check(all(near(w, CARD) for w in ws), f"card sides {min(ws):.2f} to {max(ws):.2f} mm (20 +/- 0.5)")
cols = sorted({round(r["x0"], 1) for r in cards})
rows = sorted({round(r["y0"], 1) for r in cards})
check(len(cols) == 11 and len(rows) == 5, f"cards form 5 rows of 11 ({len(rows)} x {len(cols)})")
pitches = [b - a for a, b in zip(cols, cols[1:])] + [b - a for a, b in zip(rows, rows[1:])]
check(all(near(p, CARD) for p in pitches), f"cards share cut lines: pitch {min(pitches):.2f} to {max(pitches):.2f} mm")
digit_spans = [s for s in sp1 if s["text"].isdigit() and s["size"] > 30]
ok_num = True
for ri, y in enumerate(rows):
    for ci, x in enumerate(cols):
        inside = [s for s in digit_spans if x < s["cx"] < x + CARD and y < (s["y0"] + s["y1"]) / 2 < y + CARD]
        if len(inside) != 1 or inside[0]["text"] != str(ci) or abs(inside[0]["cx"] - (x + CARD / 2)) > 1.0:
            ok_num = False
check(ok_num and len(digit_spans) == 55, "each row is one set 0 to 10, one number centred on each card")
und = [l for l in lines if near(abs(l[1][0] - l[0][0]), 7.2, 0.3) and l[0][1] == l[1][1]]
und_cols = sorted(ci for l in und for ci, x in enumerate(cols) if x < l[0][0] < x + CARD)
check(sorted(set(und_cols)) == [6, 9] and len(und) == 10, "6 and 9 underlined on every set, nothing else")
marks = [m for m in fills if (m["x1"] - m["x0"]) < 4]
sig_by_row = {}
for m in marks:
    for ri, y in enumerate(rows):
        if y < m["y0"] < y + CARD:
            sig_by_row.setdefault(ri, set()).add((m["sig"], round(m["x1"] - m["x0"], 1)))
check(len(marks) == 55 and len(sig_by_row) == 5 and all(len(v) == 1 for v in sig_by_row.values())
      and len({next(iter(v)) for v in sig_by_row.values()}) == 5,
      "one small grey set mark per card, a different mark for each of the five sets")

print("\n== Page 1: strip from 0 to 10")
sq = [r for r in rects if near(r["w"], STRIP_SQ, 1.5) and near(r["h"], STRIP_SQ, 1.5)]
sq.sort(key=lambda r: r["x0"])
check(len(sq) == 11, f"11 strip squares ({len(sq)})")
sides = [r["w"] for r in sq] + [r["h"] for r in sq]
check(all(near(s, STRIP_SQ) for s in sides), f"strip squares {min(sides):.2f} to {max(sides):.2f} mm (23 +/- 0.5)")
sp_p = [b["x0"] - a["x0"] for a, b in zip(sq, sq[1:])]
check(all(near(p, STRIP_SQ) for p in sp_p) and len({round(r['y0'], 1) for r in sq}) == 1,
      f"squares in one straight row, touching: pitch {min(sp_p):.2f} to {max(sp_p):.2f} mm")
num_under = []
for i, r in enumerate(sq):
    m = [s for s in sp1 if s["text"] == str(i) and s["size"] < 20 and r["x0"] < s["cx"] < r["x1"]
         and r["y1"] < s["y0"] < r["y1"] + 8]
    num_under.append(len(m) == 1 and abs(m[0]["cx"] - (r["x0"] + r["x1"]) / 2) < 1.0)
check(all(num_under), "numbers 0 to 10 centred under the squares, in order")
inside = [m for m in fills if any(r["x0"] < m["x0"] < r["x1"] and r["y0"] < m["y0"] < r["y1"] for r in sq)]
check(not inside, "no counters or marks drawn on the strip")
# compare with the strip in the problem (Grades 4-5 Problem 7, packet page 7)
pk45 = pymupdf.open(os.path.join(PACKETS, "grades-4-5.pdf"))
r7, _, _, _ = shapes(pk45[6])
s7 = spans(pk45[6])
rowsq = {}
for r in r7:
    if abs(r["w"] - r["h"]) < 0.2:
        rowsq.setdefault((round(r["w"], 1), round(r["y0"], 1)), []).append(r)
page_strips = {k: sorted(v, key=lambda r: r["x0"]) for k, v in rowsq.items()}
big10 = [v for (w, y), v in page_strips.items() if len(v) == 11 and w > 15]
big6 = [v for (w, y), v in page_strips.items() if len(v) == 7 and w > 20]
if big10:
    v = big10[0]
    labels = []
    for r in v:
        m = [s["text"] for s in s7 if r["x0"] < s["cx"] < r["x1"] and r["y1"] < s["y0"] < r["y1"] + 8]
        labels.append(m[0] if m else "?")
    check(labels == [str(i) for i in range(11)],
          f"same as the problem's strip from 0 to 10: 11 squares numbered 0 to 10 underneath "
          f"(problem's squares {v[0]['w']:.1f} mm, too small for 2 cm counters)")
else:
    check(False, "found the strip from 0 to 10 on Grades 4-5 page 7")
if big6:
    print(f"INFO  the packets' strip from 0 to 6 (2-3 Problem 8, 4-5 Problem 7) has {big6[0][0]['w']:.1f} mm "
          f"squares: it already takes counters up to 2 cm, so it is not reprinted")
for name, w in (("snap cube 20 mm", 20.0), ("3/4-inch counter 19.05 mm", 19.05), ("1-inch counter 25.4 mm", 25.4)):
    room = STRIP_SQ - w
    print(f"INFO  strip square 23 mm with a {name}: {'fits, ' + format(room / 2, '.1f') + ' mm each side' if room > 0 else 'does not fit'}")

# ------------------------------------------------------------------ page 2
print("\n== Page 2: launch sheet")
p2 = doc[1]
rects, circles, lines, fills = shapes(p2)
nets, boxes = networks(circles, rects, lines, 30.0, 14.0)
check(len(circles) == 4 and all(near(c["dx"], 30.0) and near(c["dy"], 30.0) for c in circles),
      "4 dots, each " + ", ".join(f"{c['dx']:.2f}" for c in circles) + " mm across (30 +/- 0.5)")
check(len(boxes) == 4 and all(near(b["w"], 14.0) and near(b["h"], 14.0) for b in boxes),
      f"4 link boxes, {len(boxes)} found, 14 mm square")
if len(nets) == 1:
    dots, edges, _ = nets[0]
    deg = sorted(sum(1 for e in edges if i in e) for i in range(len(dots)))
    tri = [e for e in edges if all(sum(1 for f in edges if i in f) >= 2 for i in e)]
    check(len(edges) == 4 and deg == [1, 2, 2, 3] and len(tri) == 3,
          "a triangle with a tail, as in the guide's launch (4 dots, 4 links, degrees 1, 2, 2, 3)")
    sides = [math.hypot(dots[i]["cx"] - dots[j]["cx"], dots[i]["cy"] - dots[j]["cy"]) for i, j in tri]
    check(max(sides) - min(sides) < 0.5, "triangle sides equal: " + ", ".join(f"{s:.1f}" for s in sides) + " mm")
    mids_ok = all(any(math.hypot((b["x0"] + b["x1"]) / 2 - (dots[i]["cx"] + dots[j]["cx"]) / 2,
                                 (b["y0"] + b["y1"]) / 2 - (dots[i]["cy"] + dots[j]["cy"]) / 2) < 0.5
                      for b in boxes) for i, j in edges)
    check(mids_ok, "one box at the middle of each link")
    room = card_room(dots, boxes)
    s_min = min(s for s, _ in room)
    check(s_min >= CARD + 4, f"a 20 mm card or 2 cm tower foot on any dot clears every box (room {s_min:.1f} mm)")
else:
    check(False, f"launch network found as one piece ({len(nets)} pieces)")
check(not [s for s in spans(p2) if s["text"].isdigit() and s["y0"] < 190], "no numbers on the launch network")

# ------------------------------------------------------------------ page 3
print("\n== Page 3: trees for Grades 4-5 Problem 9")
p3 = doc[2]
rects, circles, lines, fills = shapes(p3)
sp3 = spans(p3)
nets3, boxes3 = networks(circles, rects, lines, 25.0, 10.0)
check(all(near(c["dx"], 25.0) and near(c["dy"], 25.0) for c in circles) and len(circles) == 15,
      f"15 dots, {min(c['dx'] for c in circles):.2f} to {max(c['dx'] for c in circles):.2f} mm across (25 +/- 0.5)")
check(len(boxes3) == 13 and all(near(b["w"], 10.0) and near(b["h"], 10.0) for b in boxes3),
      f"13 link boxes, 10 mm square ({len(boxes3)} found)")
# the problem's trees, from the packet
r9, c9, l9, _ = shapes(pk45[8])
s9 = spans(pk45[8])
pnets, _ = networks(c9, r9, l9, 12.0, 6.5)
pnets = [n for n in pnets if len(n[0]) >= 7]
check(len(pnets) == 2, "found the two printed starter trees on Grades 4-5 page 9")


def caption_of(dots, sps, r):
    xs = [d["cx"] for d in dots]
    ys = [d["cy"] for d in dots]
    cx, bottom = (min(xs) + max(xs)) / 2, max(ys) + r
    m = [s for s in sps if s["text"].startswith("cards") and abs(s["cx"] - cx) < 2 and 0 < s["y0"] - bottom < 6]
    return m[0]["text"] if m else None


for dots, edges, _ in sorted(nets3, key=lambda n: len(n[0])):
    g, ge, off = grid_shape(dots, edges)
    match = [n for n in pnets if len(n[0]) == len(dots)]
    if not match:
        check(False, f"tree of {len(dots)} dots has a match in the problem")
        continue
    pg, pge, poff = grid_shape(match[0][0], match[0][1])
    cap, pcap = caption_of(dots, sp3, 12.5), caption_of(match[0][0], s9, 6.0)
    check(g == pg and ge == pge and off < 0.05 and poff < 0.05,
          f"tree of {len(dots)} dots and {len(edges)} links: same dots and links in the same arrangement as the problem's")
    check(cap is not None and cap == pcap, f"caption under it '{cap}' matches the problem's '{pcap}'")
    lens = [math.hypot(dots[i]["cx"] - dots[j]["cx"], dots[i]["cy"] - dots[j]["cy"]) for i, j in edges]
    vis = min(L / 2 - 5.0 - 12.5 for L in lens)
    room = card_room(dots, boxes3)
    s_min = min(s for s, _ in room)
    check(s_min >= CARD + 4, f"links {min(lens):.1f} mm; a 20 mm card clears every box (room {s_min:.1f} mm, "
          f"{(s_min - CARD) / 2:.1f} mm slack); link line visible {vis:.1f} mm each side of a box")
# the two trees' cards never meet
if len(nets3) == 2:
    A, B = nets3[0][0], nets3[1][0]
    gapc = min(max(abs(a["cx"] - b["cx"]), abs(a["cy"] - b["cy"])) - CARD for a in A for b in B)
    gapd = min(math.hypot(a["cx"] - b["cx"], a["cy"] - b["cy"]) - 25.0 for a in A for b in B)
    check(gapc > 5, f"the two trees are apart: dots {gapd:.1f} mm, cards {gapc:.1f} mm at the closest")

# ------------------------------------------------------------------ the card on every packet board
print("\n== The measured 20 mm card on every card board in the packets")
card_side = sum(ws) / len(ws)
worst = (1e9, None)
for pk in ("grades-2-3.pdf", "grades-4-5.pdf"):
    pdoc = pymupdf.open(os.path.join(PACKETS, pk))
    for pno, page in enumerate(pdoc, start=1):
        rr, cc, ll, _ = shapes(page)
        dots = [c for c in cc if near(c["dx"], 25.0, 0.6)]
        if not dots:
            continue
        boxes = [r for r in rr if 5 < r["w"] < 12 and abs(r["w"] - r["h"]) < 0.2]
        room = card_room(dots, boxes)
        s = min(x for x, _ in room)
        rot = min(nb for _, nb in room) - card_side / math.sqrt(2)
        print(f"INFO  {pk[:-4]} page {pno}: {len(dots):2d} card dots; largest upright card {s:.2f} mm "
              f"(slack {(s - card_side) / 2:.1f} mm); turned 45 degrees the card's corner is "
              f"{rot:+.1f} mm from the nearest box")
        if s < worst[0]:
            worst = (s, f"{pk[:-4]} page {pno}")
check(worst[0] >= card_side + 0.4,
      f"a {card_side:.2f} mm card clears every box on every packet card board "
      f"(tightest {worst[0]:.2f} mm, {worst[1]})")

# ------------------------------------------------------------------ pixels
print("\n== Pixel cross-check at 300 dpi")
img, mmpx = render(MAT, 1)
y0 = rows[0]
yline = int((y0 + 2.0) / mmpx)
runs = [c for c, a, b in dark_runs(img[yline, :]) if b - a < 10]
runs_mm = [c * mmpx for c in runs]
card_lines = [x for x in runs_mm if cols[0] - 1 < x < cols[-1] + CARD + 1]
pp = [b - a for a, b in zip(card_lines, card_lines[1:])]
check(len(card_lines) == 12 and all(near(p, CARD) for p in pp),
      f"card cut lines across a row: {len(card_lines)} lines, pitch {min(pp):.2f} to {max(pp):.2f} mm")
xcol = int((cols[0] + 2.0) / mmpx)
vr = [c * mmpx for c, a, b in dark_runs(img[:, xcol]) if b - a < 10]
vlines = [y for y in vr if rows[0] - 1 < y < rows[-1] + CARD + 1]
vp = [b - a for a, b in zip(vlines, vlines[1:])]
check(len(vlines) == 6 and all(near(p, CARD) for p in vp),
      f"card cut lines down a column: {len(vlines)} lines, pitch {min(vp):.2f} to {max(vp):.2f} mm")
# digit height on a card (the 8 of the first set)
x8 = cols[8]
sub = img[int(y0 / mmpx) + 6:int((y0 + CARD) / mmpx) - 6, int(x8 / mmpx) + 6:int((x8 + CARD) / mmpx) - 6]
# drop the set mark at the bottom right by only looking at the middle columns
mid = sub[:, sub.shape[1] // 4: 3 * sub.shape[1] // 4]
ink = np.where((mid < 128).sum(axis=1) > 0)[0]
h8 = (ink.max() - ink.min() + 1) * mmpx
check(8.0 < h8 < 10.0, f"card numbers are large: the 8 stands {h8:.1f} mm tall")
sy = sq[0]["y0"]
yl = int((sy + 3.0) / mmpx)
sr = [c * mmpx for c, a, b in dark_runs(img[yl, :]) if b - a < 12]
slines = [x for x in sr if sq[0]["x0"] - 1 < x < sq[-1]["x1"] + 1]
spp = [b - a for a, b in zip(slines, slines[1:])]
check(len(slines) == 12 and all(near(p, STRIP_SQ) for p in spp),
      f"strip square edges: {len(slines)} lines, pitch {min(spp):.2f} to {max(spp):.2f} mm")
for pno, want in ((2, 30.0), (3, 25.0)):
    img2, mmpx = render(MAT, pno)
    cs = shapes(doc[pno - 1])[1]
    meas = []
    for c in cs:
        # From the centre, walk out in the four axis directions across the white
        # inside to the outline, then across the outline. Links stop at the
        # white-filled dot, so the inside edges are clean; the outline's
        # thickness is the shortest dark run (a direction with no link).
        px, py = int(round(c["cx"] / mmpx)), int(round(c["cy"] / mmpx))
        inner, dark = {}, []
        dirs = {"l": (-1, 0), "r": (1, 0), "u": (0, -1), "d": (0, 1),
                "ul": (-1, -1), "ur": (1, -1), "dl": (-1, 1), "dr": (1, 1)}
        for name, (sx, sy) in dirs.items():
            k = 0
            while img2[py + sy * k, px + sx * k] >= 128:
                k += 1
            inner[name] = k
            j = 0
            while img2[py + sy * (k + j), px + sx * (k + j)] < 128:
                j += 1
            dark.append(j * math.hypot(sx, sy))     # outline thickness in pixels
        stroke = min(dark)
        dh = (inner["l"] + inner["r"] - 1 + 2 * stroke) * mmpx
        dv = (inner["u"] + inner["d"] - 1 + 2 * stroke) * mmpx
        meas += [dh, dv]
    check(len(meas) == 2 * len(cs) and all(near(m, want) for m in meas),
          f"p{pno}: {len(cs)} dots measured across and down, {min(meas):.2f} to {max(meas):.2f} mm "
          f"({want:.0f} +/- 0.5)")

print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed")
