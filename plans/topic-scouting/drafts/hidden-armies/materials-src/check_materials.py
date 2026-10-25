#!/usr/bin/env python3
"""Check the delivered Hidden armies materials PDF against its specification.

Reads the PDF itself (not the LaTeX source): first its drawn paths and text,
then a raster rendered at 254 dpi (10 pixels per mm), measuring the key sizes
both ways. Also reads the three student packets to confirm that the hill mat
matches the mat the problems use (three hills, numbered 1, 2, 3 from left to
right, numbers below the hills).

Usage: python3 check_materials.py [materials.pdf]
"""
import math
import os
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
STUDENT = RUN
PDF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RUN, "materials.pdf")

MM = 25.4 / 72  # mm per PDF point
TOL = 0.5  # mm

# Specification (from the outline: hill circles about 7 cm across, numbered 1, 2, 3)
PAGE_W, PAGE_H = 279.4, 215.9
HILL_D = 70.0
HILL_X = [54.7, 139.7, 224.7]  # centres, 85 mm apart
CUT_Y = PAGE_H / 2  # the two mats are the two halves of the sheet
LANE_W = 76.0
EDGE = 12.0  # nothing closer than this to a paper edge
HEADER = "Week NN / Hidden armies / Materials"
FOOTER = "Bellingham Math Circle / Week NN / HA-M-v1"
ALLOWED_TEXT = {HEADER, FOOTER, "Hill mat", "1", "2", "3", "100 mm scale check", "✂"}
CUBE, TOKEN = 20.0, 19.05  # interlocking cube face, US penny (guide's materials)

failures = []
notes = []


def check(cond, msg):
    (notes if cond else failures).append(("ok   " if cond else "FAIL ") + msg)


def mm_rect(r):
    return (r.x0 * MM, r.y0 * MM, r.x1 * MM, r.y1 * MM)


doc = pymupdf.open(PDF)
check(doc.page_count == 1, f"page count is {doc.page_count} (expected 1)")
page = doc[0]
pw, ph = page.rect.width * MM, page.rect.height * MM
check(abs(pw - PAGE_W) < 0.1 and abs(ph - PAGE_H) < 0.1,
      f"page is {pw:.1f} x {ph:.1f} mm (US Letter landscape)")

# ---------------- vector checks ----------------
drawings = page.get_drawings()
circles, lanes, lines = [], [], []
for d in drawings:
    kinds = [it[0] for it in d["items"]]
    r = mm_rect(d["rect"])
    if kinds == ["c"] * 4:
        circles.append((r, d))
    elif d["type"] == "f" and kinds.count("l") == 4 or d["type"] == "f" and kinds == ["re"]:
        lanes.append(r)
    elif kinds == ["l"]:
        lines.append((r, d))

check(len(circles) == 6, f"{len(circles)} hill circles drawn (expected 6: two mats of three)")
hills = []
for r, d in circles:
    w, h = r[2] - r[0], r[3] - r[1]
    cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
    hills.append((cx, cy, w, h))
    check(abs(w - HILL_D) <= TOL and abs(h - HILL_D) <= TOL,
          f"hill at ({cx:.1f}, {cy:.1f}) is {w:.2f} x {h:.2f} mm (spec {HILL_D:.0f} mm, outline 'about 7 cm')")
    check(abs(w - h) < 0.05, f"hill at ({cx:.1f}, {cy:.1f}) has equal scaling (w - h = {w - h:.3f} mm)")

top = sorted([c for c in hills if c[1] < CUT_Y], key=lambda c: c[0])
bot = sorted([c for c in hills if c[1] > CUT_Y], key=lambda c: c[0])
check(len(top) == 3 and len(bot) == 3, "three hills on each mat")
for name, mat in (("upper mat", top), ("lower mat", bot)):
    if len(mat) != 3:
        continue
    xs = [c[0] for c in mat]
    check(all(abs(x - e) <= TOL for x, e in zip(xs, HILL_X)),
          f"{name} hill centres at x = {', '.join(f'{x:.2f}' for x in xs)} mm")
    gaps = [xs[1] - xs[0], xs[2] - xs[1]]
    check(all(abs(g - 85) <= TOL for g in gaps), f"{name} centre spacing {gaps[0]:.2f}, {gaps[1]:.2f} mm")
    check(max(c[1] for c in mat) - min(c[1] for c in mat) < 0.05, f"{name} hills in one row")
    clear = gaps[0] - HILL_D
    check(clear >= 10, f"{name} gap between neighbouring hills {clear:.1f} mm")
check(all(abs(a[0] - b[0]) < 0.05 for a, b in zip(top, bot)),
      "upper and lower mats have identical hill columns (hill 1 above hill 1 when lined up)")
# each mat lies inside its own half of the sheet
for name, mat, lo, hi in (("upper mat", top, 19.5, CUT_Y), ("lower mat", bot, CUT_Y, 196.4)):
    if not mat:
        continue
    y0 = min(c[1] - c[3] / 2 for c in mat)
    y1 = max(c[1] + c[3] / 2 for c in mat)
    check(lo + 1 <= y0 and y1 <= hi - 1, f"{name} hills lie within y {lo:.1f}..{hi:.1f} mm (span {y0:.1f}..{y1:.1f})")
# a cube tower and a win token fit side by side on a hill
check(CUBE + TOKEN + 6 <= HILL_D,
      f"a {CUBE:.0f} mm cube tower and a {TOKEN:.2f} mm token fit side by side on a {HILL_D:.0f} mm hill")

# lanes
lanes = sorted(lanes, key=lambda r: r[0])
check(len(lanes) == 3, f"{len(lanes)} hill lanes (expected 3)")
for i, r in enumerate(lanes):
    w = r[2] - r[0]
    cx = (r[0] + r[2]) / 2
    check(abs(w - LANE_W) <= TOL, f"lane {i + 1} is {w:.2f} mm wide")
    check(abs(cx - HILL_X[i]) <= TOL, f"lane {i + 1} centred on hill {i + 1} (x = {cx:.2f} mm)")
    check(r[1] < CUT_Y < r[3], f"lane {i + 1} runs unbroken across the cut line ({r[1]:.1f}..{r[3]:.1f} mm)")
    inside = [c for c in hills if r[0] <= c[0] - c[2] / 2 and c[0] + c[2] / 2 <= r[2]
              and r[1] <= c[1] - c[3] / 2 and c[1] + c[3] / 2 <= r[3]]
    check(len(inside) == 2, f"lane {i + 1} contains hill {i + 1} of both mats")
if len(lanes) == 3:
    check(lanes[1][0] - lanes[0][2] >= 5 and lanes[2][0] - lanes[1][2] >= 5,
          "white gap of at least 5 mm between lanes")

# cut line and scale bar
cut = [(r, d) for r, d in lines if d.get("dashes") not in (None, "[] 0") and abs(r[1] - r[3]) < 0.01]
check(len(cut) == 1, f"{len(cut)} dashed cut line(s)")
for r, d in cut:
    check(abs(r[1] - CUT_Y) <= 0.1, f"cut line at y = {r[1]:.2f} mm (half the sheet height, {CUT_Y:.2f})")
    check(r[0] <= 25 and r[2] >= PAGE_W - 25, f"cut line spans x {r[0]:.1f}..{r[2]:.1f} mm")
bars = [r for r, d in lines if abs(r[1] - r[3]) < 0.01 and d.get("dashes") in (None, "[] 0")
        and 90 < r[2] - r[0] < 110]
check(len(bars) == 1 and abs(bars[0][2] - bars[0][0] - 100) <= TOL,
      f"scale check bar {bars[0][2] - bars[0][0]:.2f} mm (expected 100)" if bars else "scale check bar found")

# text
spans = []
for b in page.get_text("dict")["blocks"]:
    for l in b.get("lines", []):
        for s in l["spans"]:
            if s["text"].strip():
                spans.append((s["text"].strip(), s["size"], s["flags"], mm_rect(pymupdf.Rect(s["bbox"]))))
texts = {t for t, *_ in spans}
check(texts <= ALLOWED_TEXT, f"only object labels on the sheet (extra text: {sorted(texts - ALLOWED_TEXT)})")
check(any(t == HEADER for t, *_ in spans), "header reads " + HEADER)
check(any(t == FOOTER for t, *_ in spans), "footer reads " + FOOTER)
pageno = [s for s in spans if s[0] == "1" and s[1] < 12]
check(len(pageno) == 1 and pageno[0][3][2] > PAGE_W - 20 and pageno[0][3][1] > 195,
      "page number 1 at the right of the footer")

big = [s for s in spans if s[0] in "123" and s[1] > 15]
check(len(big) == 6, f"{len(big)} hill numbers (expected 6)")


def dist_rect_point(r, x, y):
    dx = max(r[0] - x, 0, x - r[2])
    dy = max(r[1] - y, 0, y - r[3])
    return math.hypot(dx, dy)


def far_corner(r, x, y):
    return max(math.hypot(px - x, py - y) for px in (r[0], r[2]) for py in (r[1], r[3]))


for name, mat in (("upper mat", top), ("lower mat", bot)):
    labels = []
    for i, (cx, cy, w, h) in enumerate(mat):
        mine = [s for s in big if abs((s[3][0] + s[3][2]) / 2 - cx) <= TOL
                and cy + h / 2 < s[3][1] < cy + h / 2 + 10]
        if len(mine) != 1:
            check(False, f"{name} hill {i + 1}: one number centred under it")
            continue
        t, size, flags, r = mine[0]
        labels.append(t)
        gap = dist_rect_point(r, cx, cy) - w / 2
        check(gap >= 1.0, f"{name} hill {i + 1}: number '{t}' sits {gap:.1f} mm outside the hill (clear of pieces)")
        check(r[1] - (cy + h / 2) <= 6, f"{name} hill {i + 1}: number directly below its hill")
        check(flags & 16, f"{name} hill {i + 1}: number is bold")
    check(labels == ["1", "2", "3"], f"{name} hills numbered {' '.join(labels)} from left to right")
for t, size, flags, r in spans:
    if t == "Hill mat":
        clear = min(dist_rect_point(r, c[0], c[1]) - c[2] / 2 for c in hills)
        check(clear >= 3, f"'Hill mat' label at y {r[1]:.1f} mm is {clear:.1f} mm clear of the nearest hill")
        same_half = [c for c in hills if (c[1] < CUT_Y) == (r[1] < CUT_Y)]
        check(len(same_half) == 3, "'Hill mat' label lies on its own mat")
check(sum(1 for t, *_ in spans if t == "Hill mat") == 2, "each mat carries the label 'Hill mat'")

# margins: every mark at least 12 mm from every paper edge
worst = (1e9, "")
for d in drawings:
    r = mm_rect(d["rect"])
    hw = (d.get("width") or 0) * MM / 2
    m = min(r[0] - hw, r[1] - hw, PAGE_W - r[2] - hw, PAGE_H - r[3] - hw)
    worst = min(worst, (m, f"path {tuple(round(v, 1) for v in r)}"))
for t, size, flags, r in spans:
    m = min(r[0], r[1], PAGE_W - r[2], PAGE_H - r[3])
    worst = min(worst, (m, f"text '{t}'"))
check(worst[0] >= EDGE, f"closest mark to a paper edge: {worst[0]:.2f} mm ({worst[1]})")

# ---------------- raster checks (254 dpi = 10 px per mm) ----------------
PX = 10.0
pix = page.get_pixmap(dpi=254, colorspace=pymupdf.csGRAY, alpha=False)
W, H, S = pix.width, pix.height, pix.samples
check(abs(W / PX - PAGE_W) < 0.2 and abs(H / PX - PAGE_H) < 0.2, f"raster {W} x {H} px at 10 px/mm")


def gray(x, y):
    return S[y * W + x]


def runs(values):
    """Centres (px) of runs of dark pixels in a sequence of (pos, value)."""
    out, cur = [], []
    for pos, v in values:
        if v < 128:
            cur.append(pos)
        elif cur:
            out.append(sum(cur) / len(cur)); cur = []
    if cur:
        out.append(sum(cur) / len(cur))
    return out


for name, cy in (("upper mat", 21.5 + 40), ("lower mat", CUT_Y + 40)):
    y = round(cy * PX)
    row = runs((x, gray(x, y)) for x in range(W))
    # expect the outline crossings: left and right edge of each of three hills
    edges = [p / PX for p in row]
    check(len(edges) == 6, f"{name}: {len(edges)} outline crossings on the centre row (expected 6)")
    if len(edges) == 6:
        cxs = []
        for i in range(3):
            dia = edges[2 * i + 1] - edges[2 * i]
            cxs.append((edges[2 * i] + edges[2 * i + 1]) / 2)
            check(abs(dia - HILL_D) <= TOL, f"{name} hill {i + 1}: measured width {dia:.2f} mm (raster)")
        sp = [cxs[1] - cxs[0], cxs[2] - cxs[1]]
        check(all(abs(s - 85) <= TOL for s in sp), f"{name}: measured centre spacing {sp[0]:.2f}, {sp[1]:.2f} mm (raster)")
        for i, cx in enumerate(cxs):
            x = round(cx * PX)
            up = runs((yy, gray(x, yy)) for yy in range(y, max(y - 450, 0), -1))
            dn = runs((yy, gray(x, yy)) for yy in range(y, min(y + 450, H)))
            if up and dn:
                dia = (dn[0] - up[0]) / PX
                check(abs(dia - HILL_D) <= TOL, f"{name} hill {i + 1}: measured height {dia:.2f} mm (raster)")
            else:
                check(False, f"{name} hill {i + 1}: vertical outline found")
# scale bar
y = round(201.0 * PX)
xs = [x for x in range(W) if gray(x, y) < 128 and 900 < x < 2070]  # between footer text and bar label
if xs:
    length = (xs[-1] - xs[0] + 1) / PX - 0.6 * MM  # minus one stroke width (half at each end tick)
    check(abs(length - 100) <= TOL, f"scale check bar measures {length:.2f} mm (raster)")
# lanes visible in print (grey, not white)
lane_px = gray(round(HILL_X[0] * PX), round(CUT_Y * PX) + 30)  # inside lane 1, just below the cut
check(200 <= lane_px <= 245, f"lane grey level {lane_px} (visible but light)")

# ---------------- match against the student pages ----------------
for f in ("k-1.pdf", "grades-2-3.pdf", "grades-4-5.pdf"):
    path = os.path.join(STUDENT, f)
    if not os.path.exists(path):
        check(False, f"student packet {f} found")
        continue
    sp = pymupdf.open(path)[0]
    txt = " ".join(sp.get_text().split())
    check("three hills of your mat" in txt, f"{f}: rules use 'the three hills of your mat'")
    words = [w for w in sp.get_text("words") if w[4] in ("1", "2", "3")]
    rows = {}
    for w in words:
        rows.setdefault(round(w[1], 1), []).append(w)
    hill_rows = [sorted(r, key=lambda w: w[0]) for r in rows.values() if len(r) == 3]
    pics = [r for r in hill_rows if [w[4] for w in r] == ["1", "2", "3"]]
    check(len(pics) >= 1, f"{f}: rules picture numbers its hills 1, 2, 3 from left to right ({len(pics)} row(s))")
    if f == "k-1.pdf":
        # two mats one above the other, hill 1 above hill 1, as the lanes line them up
        cols = len(pics) == 2 and all(abs(a[0] - b[0]) < 0.5 for a, b in zip(pics[0], pics[1]))
        check(cols, f"{f}: rules picture shows two mats lined up hill 1 above hill 1")

for n in notes:
    print(n)
for f in failures:
    print(f)
print(f"\n{len(notes)} checks passed, {len(failures)} failed")
sys.exit(1 if failures else 0)
