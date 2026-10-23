#!/usr/bin/env python3
"""Measure the delivered Week 93 PDFs: page furniture, diagram sizes and
scales, labels, cards, and the guide text quoted in math.md.

Run: python3 check_pdf93.py > check_pdf93.out
"""
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
import pymupdf as fitz  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repo_path import STUDENT_PDF, GUIDE_PDF, SRC  # noqa: E402

FAIL = 0
MM = 72 / 25.4


def check(cond, msg):
    global FAIL
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL += 1


def cluster(vals, tol=0.3):
    out = []
    for v in sorted(vals):
        if not out or v - out[-1] > tol:
            out.append(v)
    return out


def words(page):
    return [(w[0], w[1], w[2], w[3], w[4]) for w in page.get_text("words")]


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip()


def thick_rects(page, minw=0.5):
    out = []
    for d in page.get_drawings():
        r = d["rect"]
        if d.get("width") and d["width"] >= minw and r.width > 20 and r.height > 20:
            out.append(r)
    return out


def labels_near(ws, r, tol=18):
    """Words just above, below, left of, right of a rectangle, centred on it."""
    cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
    res = {"above": [], "below": [], "left": [], "right": []}
    for x0, y0, x1, y1, t in ws:
        wx, wy = (x0 + x1) / 2, (y0 + y1) / 2
        if abs(wx - cx) < 12 and r.y0 - tol < y1 <= r.y0 + 1:
            res["above"].append(t)
        if abs(wx - cx) < 12 and r.y1 - 1 <= y0 < r.y1 + tol:
            res["below"].append(t)
        if abs(wy - cy) < 10 and r.x0 - tol < x1 <= r.x0 + 1:
            res["left"].append(t)
        if abs(wy - cy) < 10 and r.x1 - 1 <= x0 < r.x1 + tol:
            res["right"].append(t)
    return res


doc = fitz.open(STUDENT_PDF)
print("student PDF:", STUDENT_PDF.name, "pages", len(doc))
check(len(doc) == 5 and all(p.rect.width == 612 and p.rect.height == 792 for p in doc), "5 US Letter pages")

# ---- furniture and numbering
nums = []
for i, p in enumerate(doc, 1):
    t = norm(p.get_text())
    head = "Week 93 / Squaring a rectangle / " + ("Grades 3–5" if i < 5 else "Grades 4–5, ready for general reasoning")
    check(t.startswith(head), f"p{i} header '{head}'")
    check("Bellingham Math Circle / Week 93 / W93-S-v2" in t, f"p{i} footer")
    nums += [int(n) for n in re.findall(r"Problem (\d+):", t)]
check(nums == list(range(1, 8)), f"problems numbered consecutively {nums}")

# ---- p1 grid
p = doc[0]
grid = [d for d in p.get_drawings() if d["rect"].width > 400 and d["rect"].height > 300]
r = grid[0]["rect"]
lines = [it for d in grid for it in d["items"] if it[0] == "l"]
vert = cluster(it[1].x for it in lines if abs(it[1].x - it[2].x) < 0.01)
horz = cluster(it[1].y for it in lines if abs(it[1].y - it[2].y) < 0.01)
check(len(vert) == 25 and len(horz) == 21, f"p1 grid has {len(vert)-1} x {len(horz)-1} cells")
check(abs(r.width / MM - 168) < 0.1 and abs(r.height / MM - 140) < 0.1,
      f"p1 grid {r.width/MM:.2f} x {r.height/MM:.2f} mm = 7 mm cells (guide)")
t1 = norm(p.get_text())
print("   p1 text:", t1[t1.index("Each grid"):t1.index("square?") + 7])

# ---- p2 cutting diagrams
p = doc[1]
ws = words(p)
rects = sorted(thick_rects(p), key=lambda r: (round(r.y0), r.x0))
check(len(rects) == 4, "p2 has four outlined shapes")
expected = {}
scales = []
for r in rects:
    lab = labels_near(ws, r)
    name = "".join(lab["above"])
    w = int("".join(lab["below"]))
    h = int("".join(lab["left"]))
    sx, sy = r.width / w, r.height / h
    scales += [sx, sy]
    # inner grid lines must be at unit spacing
    inner = [d for d in p.get_drawings() if d["rect"] == r and d.get("width", 1) < 0.5]
    segs = [it for d in inner for it in d["items"] if it[0] == "l"]
    vx = sorted({round(it[1].x, 2) for it in segs if abs(it[1].x - it[2].x) < .01})
    hy = sorted({round(it[1].y, 2) for it in segs if abs(it[1].y - it[2].y) < .01})
    print(f"   {name}: labels {w} x {h}; outline {r.width/MM:.2f} x {r.height/MM:.2f} mm; "
          f"{sx/MM:.3f} mm/unit across, {sy/MM:.3f} mm/unit up; grid lines {len(vx)}x{len(hy)}")
    check(len(vx) == w + 1 and len(hy) == h + 1, f"   {name} {w}x{h}: one grid cell per unit")
    expected.setdefault(name, []).append((w, h))
check(max(scales) - min(scales) < 0.05 and abs(scales[0] / MM - 15) < 0.01,
      "p2 all four shapes at 15 mm per unit in both directions (equal scaling)")
check(expected == {"A": [(4, 4), (6, 2)], "B": [(3, 3), (4, 2)]} or
      sorted(expected["A"]) == [(4, 4), (6, 2)] and sorted(expected["B"]) == [(3, 3), (4, 2)],
      f"p2 labels pair 6x2 with the 4x4 square (A) and 4x2 with the 3x3 square (B): {expected}")
t2 = norm(p.get_text())
print("   p2 text:", t2[t2.index("Problem 2"):t2.index("uncovered square.") + 17])

# ---- p3 worked example and number lines
p = doc[2]
dr = p.get_drawings()
boxes = [d["rect"] for d in dr if d["type"] == "fs" and d["rect"].width > 20]
check(len(boxes) == 2, "p3 example has input and output rectangles")
inp, outp = sorted(boxes, key=lambda r: r.x0)
u = inp.height  # 1 unit
check(abs(inp.width / u - 3) < 1e-3 and abs(outp.width / u - 2) < 1e-3 and abs(outp.height / u - 1.5) < 1e-3,
      f"p3 example drawn to one scale: input 3 x 1, output {outp.width/u:.3f} x {outp.height/u:.3f} units")
hsegs = [d["rect"] for d in dr if d["type"] == "s" and d["rect"].height == 0 and 20 < d["rect"].width < 100]
lens = sorted(round(r.width / u, 2) for r in hsegs)
check(1.0 in lens and 3.0 in lens, f"p3 joined segments of 1 and 3 units: {lens}")
arrow_heads = [d["rect"] for d in dr if d["type"] == "f" and d["rect"].width < 6 and abs(d["rect"].y0 - 143.86) < 1]
if len(arrow_heads) == 2:
    span = (max(a.x1 for a in arrow_heads) - min(a.x0 for a in arrow_heads)) / u
    check(abs(span - 2) < 0.03, f"p3 double arrow spans {span:.3f} units = half of 1+3")
nlines = sorted([d for d in dr if d["type"] == "s" and 400 < d["rect"].width < 500 and d["rect"].height == 0],
                key=lambda d: d["rect"].y0)
check(len(nlines) == 3, "p3 three number lines")
ws = words(p)
for d in nlines:
    y = d["rect"].y0
    ticks = sorted(round(dd["rect"].x0, 2) for dd in dr if dd["rect"].width == 0 and abs((dd["rect"].y0 + dd["rect"].y1) / 2 - y) < 1
                   and 4 < dd["rect"].height < 8)
    gl = [b - a for a, b in zip(ticks, ticks[1:])]
    gaps = {round(sum(gl) / len(gl), 2)} if gl and max(gl) - min(gl) < 0.05 else set(gl)
    labs = [t for x0, y0, x1, y1, t in sorted(ws) if y < y0 < y + 15 and t.isdigit()]
    check(len(ticks) == 11 and len(gaps) == 1 and labs == [str(n) for n in range(11)],
          f"   number line at y={y:.0f}: 11 equally spaced ticks ({gaps} pt) labelled 0..10")
t3 = norm(p.get_text())
for s in ["2 by 6 area 12", "3 by 6 area 18", "2 by 10 area 20"]:
    check(s in t3, f"p3 case '{s}'")

# ---- p4 cards
p = doc[3]
ws = words(p)
cards = sorted(thick_rects(p, 0.3), key=lambda r: (round(r.y0), r.x0))
check(len(cards) == 4 and all(abs(r.width / MM - 70) < .1 and abs(r.height / MM - 20) < .1 for r in cards),
      "p4 four cards 70 x 20 mm")
read = {}
for r in cards:
    inside = sorted([w for w in ws if r.x0 < w[0] and w[2] < r.x1 and r.y0 < w[1] and w[3] < r.y1], key=lambda w: (w[0], w[1]))
    letter = [w[4] for w in inside if w[4] in "ABCD"][0]
    nums = [w for w in inside if w[4].isdigit()]
    # group numerals into columns: numerator above denominator
    cols = []
    for w in nums:
        if cols and abs((cols[-1][0][0] + cols[-1][0][2]) / 2 - (w[0] + w[2]) / 2) < 6:
            cols[-1].append(w)
        else:
            cols.append([w])
    vals = []
    for c in cols:
        c.sort(key=lambda w: w[1])
        vals.append(c[0][4] if len(c) == 1 else f"{c[0][4]}/{c[1][4]}")
    read[letter] = vals
print("   cards read from PDF:", read)
check(read == {"A": ["24/7", "7/2"], "B": ["2", "6"], "C": ["336/97", "97/28"], "D": ["3", "4"]},
      "p4 card values match the source and the guide")

# ---- p5 schematic diagrams
p = doc[4]
rs = sorted(thick_rects(p), key=lambda r: r.x0)
rect, sq = rs
check(abs(sq.width - sq.height) < 0.01, f"p5 square drawn square ({sq.width/MM:.1f} mm)")
ratio = rect.width / rect.height
avg = (rect.width + rect.height) / 2
check(abs(ratio - 7 / 3) < 1e-3 and abs(avg - sq.width) < 0.05,
      f"p5 rectangle 7:3 and square side = average of its sides (so the pair is in fact in proportion)")

# ---- guide text used in the report
g = fitz.open(GUIDE_PDF)
print("guide PDF:", GUIDE_PDF.name, "pages", len(g))
gt = norm(" ".join(pg.get_text() for pg in g))
for s in ["The four whole-tile rectangles, ignoring rotation, are",
          "The uncovered square has side 2 and area 4.",
          "leaving a 1×1 square",
          "The order is B, D, A, C",
          "The decimal bracket is 3.46 < s < 3.47.",
          "such as 3.455 and 3.465",
          "rectangle A is 90 × 30 mm and its target square is 60 × 60 mm",
          "Rectangle B is 60 × 30 mm and its target is 45 × 45 mm",
          "24-by-20 grid with 7 mm cells"]:
    check(norm(s) in gt, f"guide contains '{s}'")
tex = (SRC / "guide" / "facilitator.tex").read_text()
for s in [r"If $d=b-a$, then", r"Put $m=(a+b)/2$ and $d=(b-a)/2$",
          r"Using Problem 6,", r"m-h=\frac{m^2-A}{m}=\frac{d^2}{m}=\frac{(b-a)^2}{2(a+b)}"]:
    check(s in tex, f"guide source contains '{s}'")
print("   guide p1 vs p4 use of d: overview d = b-a (old gap); Problem 6/7 d = (b-a)/2 (half the old gap)")

print("FAILURES:", FAIL)
sys.exit(1 if FAIL else 0)
