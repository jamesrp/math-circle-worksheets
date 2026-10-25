#!/usr/bin/env python3
"""Measure the delivered materials.pdf (not the source) and check it against
the student pages.

Run from anywhere:  python3 src/check_materials.py
Exit status is 0 only when every check passes.

What is checked
  * page count, Letter size, header and footer text, 12 mm clearance from
    every paper edge for every drawn path (with half its stroke) and text box;
  * bars, read from the PDF's drawn paths: each bar's fill, heavy outline and
    grid lines; every square 25.0 mm +/- 0.5 in both directions; rows and
    columns equal to the label beside it ("3 by 4" = 3 rows, 4 columns, as on
    the student pages); labels clear of every bar; bars not overlapping;
  * the set of bars against the student PDFs: every bar a packet asks
    children to break (read from the gray bar pictures on those pages) and
    the launch bar are supplied, no "decide without breaking" bar is, and the
    stated print counts cover the guide's per-pair needs;
  * the 2-spot Sprouts boards: size, spot count and spacing, same marks as
    the Grades 4-5 Problem 6 boards, and room for counters;
  * a second, independent measurement by rendering at 300 dpi and measuring
    pixels (bar outlines, grid lines, spot spacing, scale bar);
  * the text on the sheets: labels only, nothing that states an answer;
  * the LaTeX log: no errors, overfull or underfull boxes.
"""
import os
import re
import sys
from itertools import combinations

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
PDF = os.path.join(RUN, "materials.pdf")
LOG = os.path.join(HERE, "build", "materials.log")
DRAFTS = RUN

PT = 25.4 / 72.0          # mm per PDF point
TOL = 0.5                 # mm
EDGE = 12.0               # mm clearance from every paper edge
CELL = 25.0               # mm, outline: "printed grids of 25 mm squares"
COUNTER = 12.0            # mm, guide: counters "no wider than about 12 mm"

failures = []
notes = []


def check(cond, msg):
    (notes if cond else failures).append(("ok   " if cond else "FAIL ") + msg)


def mm(v):
    return v * PT


def gray(c, level, tol=0.02):
    return c is not None and all(abs(x - level) < tol for x in c)


# ---------------------------------------------------------------- basics
doc = fitz.open(PDF)
check(doc.page_count == 3, f"page count is {doc.page_count} (expected 3)")
W, H = 215.9, 279.4
HEADER = "Week NN / Breaking and drawing games / Materials"
FOOTER = "Bellingham Math Circle / Week NN / NN-M-v1"


def spans(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for s in line["spans"]:
                if s["text"].strip():
                    out.append((s["text"].strip(), fitz.Rect(s["bbox"]), line["dir"]))
    return out


for i, page in enumerate(doc, 1):
    r = page.rect
    check(abs(mm(r.width) - W) < 0.1 and abs(mm(r.height) - H) < 0.1,
          f"p{i}: page is US Letter portrait ({mm(r.width):.1f} x {mm(r.height):.1f} mm)")
    texts = [t for t, _, _ in spans(page)]
    check(HEADER in texts, f"p{i}: header reads '{HEADER}'")
    check(FOOTER in texts, f"p{i}: footer reads '{FOOTER}'")
    check(str(i) in texts, f"p{i}: page number {i} printed")
    # clearance from the paper edges
    worst = 1e9
    for d in page.get_drawings():
        half = (d.get("width") or 0) / 2
        R = d["rect"]
        for v in (R.x0 - half, R.y0 - half, r.width - (R.x1 + half), r.height - (R.y1 + half)):
            worst = min(worst, mm(v))
    for _, R, _ in spans(page):
        for v in (R.x0, R.y0, r.width - R.x1, r.height - R.y1):
            worst = min(worst, mm(v))
    check(worst >= EDGE, f"p{i}: nearest ink or text box is {worst:.1f} mm from a paper edge (>= {EDGE:.0f})")


# ---------------------------------------------------------------- bars
def bars_on(page):
    """Return bars measured from paths: dicts with rect (pt), rows, cols, cells (mm)."""
    dr = page.get_drawings()
    fills = [d["rect"] for d in dr if d["type"] == "f" and gray(d.get("fill"), 0.9)
             and len(d["items"]) == 4]
    heavy = [d["rect"] for d in dr if d["type"] == "s" and abs((d.get("width") or 0) - 2.0) < 0.05]
    thin = [d for d in dr if d["type"] == "s" and abs((d.get("width") or 0) - 0.5) < 0.05
            and gray(d.get("color"), 0.35)]
    out = []
    for R in fills:
        outline = [h for h in heavy if all(abs(a - b) < 0.05 for a, b in zip(h, R))]
        xs, ys = [R.x0, R.x1], [R.y0, R.y1]
        for d in thin:
            L = d["rect"]
            if abs(L.x0 - L.x1) < 0.01 and R.x0 + 0.1 < L.x0 < R.x1 - 0.1 \
                    and abs(L.y0 - R.y0) < 0.05 and abs(L.y1 - R.y1) < 0.05:
                xs.append(L.x0)          # full-height vertical grid line
            if abs(L.y0 - L.y1) < 0.01 and R.y0 + 0.1 < L.y0 < R.y1 - 0.1 \
                    and abs(L.x0 - R.x0) < 0.05 and abs(L.x1 - R.x1) < 0.05:
                ys.append(L.y0)          # full-width horizontal grid line
        xs.sort(); ys.sort()
        cw = [mm(b - a) for a, b in zip(xs, xs[1:])]
        ch = [mm(b - a) for a, b in zip(ys, ys[1:])]
        out.append(dict(rect=R, rows=len(ch), cols=len(cw), cw=cw, ch=ch, outlined=bool(outline)))
    return out


LABEL = re.compile(r"^(\d+) by (\d+)$")
supplied = {}            # page number -> list of "r by c"
for pno in (1, 2):
    page = doc[pno - 1]
    bars = bars_on(page)
    labels = [(t, R) for t, R, dirn in spans(page) if LABEL.match(t)]
    check(len(bars) == len(labels), f"p{pno}: {len(bars)} bars and {len(labels)} bar labels")
    allcells = [c for b in bars for c in b["cw"] + b["ch"]]
    check(all(abs(c - CELL) <= TOL for c in allcells),
          f"p{pno}: all {len(allcells)} square sides measure {min(allcells):.2f}-{max(allcells):.2f} mm (25 +/- 0.5)")
    check(all(b["outlined"] for b in bars), f"p{pno}: every bar has its heavy outline on its edge")
    used = set()
    names = []
    for b in bars:
        R = b["rect"]
        # nearest label beside the bar, vertically centred on its rows
        best = None
        for k, (t, LR) in enumerate(labels):
            cy = (LR.y0 + LR.y1) / 2
            if not (R.y0 < cy < R.y1):
                continue
            gap = R.x0 - LR.x1 if LR.x1 <= R.x0 else (LR.x0 - R.x1 if LR.x0 >= R.x1 else -1)
            if gap < 0:
                continue
            if best is None or gap < best[0]:
                best = (gap, k)
        ok = best is not None and mm(best[0]) < 8
        if ok:
            t = labels[best[1]][0]
            used.add(best[1])
            r_, c_ = map(int, LABEL.match(t).groups())
            names.append(t)
            check((r_, c_) == (b["rows"], b["cols"]),
                  f"p{pno}: bar labelled '{t}' is drawn {b['rows']} rows x {b['cols']} columns, "
                  f"{mm(R.width):.1f} x {mm(R.height):.1f} mm, label {mm(best[0]):.1f} mm from it")
        else:
            check(False, f"p{pno}: bar at {mm(R.x0):.1f},{mm(R.y0):.1f} mm has no label beside it")
    check(len(used) == len(labels), f"p{pno}: every label belongs to exactly one bar")
    # labels clear of bars and of each other
    clash = [(t, i) for t, LR in labels for i, b in enumerate(bars)
             if (LR & b["rect"]).get_area() > 0 or
             (mm(max(b['rect'].x0 - LR.x1, LR.x0 - b['rect'].x1)) < TOL and
              mm(max(b['rect'].y0 - LR.y1, LR.y0 - b['rect'].y1)) < 0)]
    check(not clash, f"p{pno}: no label touches a bar (clearance >= {TOL} mm)")
    over = [(i, j) for (i, a), (j, b) in combinations(enumerate(bars), 2)
            if mm(min(a["rect"].x1, b["rect"].x1) - max(a["rect"].x0, b["rect"].x0)) > 0.1
            and mm(min(a["rect"].y1, b["rect"].y1) - max(a["rect"].y0, b["rect"].y0)) > 0.1]
    check(not over, f"p{pno}: bars do not overlap (adjacent bars share an edge only)")
    supplied[pno] = names
    notes.append(f"info p{pno}: bars " + ", ".join(names))


def bag(names, k=1):
    out = {}
    for n in names:
        out[n] = out.get(n, 0) + k
    return out


def add(*bags):
    out = {}
    for b in bags:
        for n, k in b.items():
            out[n] = out.get(n, 0) + k
    return out


def covers(have, need):
    return all(have.get(n, 0) >= k for n, k in need.items())


# ---- bars the student pages ask children to break, read from the student PDFs
def pictured(pdf, pages, cell):
    """Gray bar pictures (fill 0.9) whose squares are `cell` mm, as 'r by c'."""
    d = fitz.open(pdf)
    found = []
    for p in pages:
        for dd in d[p - 1].get_drawings():
            if dd["type"] == "f" and gray(dd.get("fill"), 0.9) and len(dd["items"]) == 4:
                R = dd["rect"]
                r_, c_ = mm(R.height) / cell, mm(R.width) / cell
                if abs(r_ - round(r_)) < 0.03 and abs(c_ - round(c_)) < 0.03:
                    found.append(f"{round(r_)} by {round(c_)}")
    return found


k1 = os.path.join(DRAFTS, "k-1.pdf")
g23 = os.path.join(DRAFTS, "grades-2-3.pdf")
g45 = os.path.join(DRAFTS, "grades-4-5.pdf")
# K-1 Problems 1-3 (pages 1-2) draw their bars at 12 mm squares; Grades 2-3
# Problems 1-2 and Grades 4-5 Problems 1-2 (page 1) at 7 mm. The launch
# picture at the top of each page 1 uses 7 mm (K-1) or 6 mm squares.
break_k1 = pictured(k1, [1, 2], 12)
break_23 = pictured(g23, [1], 7)
break_45 = pictured(g45, [1], 7)
launch = set(pictured(k1, [1], 7)) | set(pictured(g23, [1], 6))
notes.append("info K-1 bars to break: " + ", ".join(break_k1))
notes.append("info Grades 2-3 bars to break: " + ", ".join(break_23))
notes.append("info Grades 4-5 bars to break: " + ", ".join(break_45))
notes.append("info launch picture bars: " + ", ".join(sorted(launch)))
all_supplied = set(supplied[1]) | set(supplied[2])
needed = set(break_k1) | set(break_23) | set(break_45) | {"2 by 3"}   # 4-5 Problem 3 names a 2 by 3 bar
check(needed <= all_supplied, "every bar a packet asks children to break is supplied: "
      + ", ".join(sorted(needed)))
whole = max(launch, key=lambda n: eval(n.replace(" by ", "*")))
check(whole in all_supplied, f"the launch bar ({whole}, the whole bar in the page 1 picture) is supplied")
# bars children must decide about WITHOUT breaking: none may be supplied
d23 = fitz.open(g23)
decide = set(pictured(g23, [2], 6))
decide |= set(re.findall(r"\b\d+ by \d+\b", d23[1].get_text()))
d45 = fitz.open(g45)
decide |= {n for n in re.findall(r"\b\d+ by \d+\b", d45[1].get_text()) if n not in ("2 by 3", "2 by 4")}
notes.append("info decide-without-breaking bars: " + ", ".join(sorted(decide)))
check(not (decide & all_supplied), "no 'decide without breaking' bar is supplied")
check(all(n not in all_supplied for n in ("1 by 1",)), "no single squares are supplied")

# print plan: sheet 1 one per pair (or 4-5 group), sheet 2 one per table
S1, S2 = bag(supplied[1]), bag(supplied[2])
# guide's per-pair lists (Preparation, "Per pair")
need_k1 = {"2 by 2": 1, "2 by 3": 1, "1 by 6": 1, "3 by 4": 2, "3 by 3": 2, "2 by 4": 2}
need_23 = {"3 by 3": 2, "2 by 4": 2, "3 by 4": 1, "1 by 6": 1, "2 by 2": 1}
need_45 = {"3 by 3": 3, "2 by 4": 3, "3 by 4": 2}          # incl. the referee's spare 3x3 and 2x4
for band, need in (("K-1", need_k1), ("Grades 2-3", need_23)):
    have = add(S1, S1, S2)
    check(covers(have, add(need, need)),
          f"{band} table of two pairs: 2 x sheet 1 + 1 x sheet 2 gives {dict(sorted(have.items()))}, "
          f"covering two pairs' needs")
have45 = add(S1, S2)
check(covers(have45, need_45), f"Grades 4-5 group: 1 x sheet 1 + 1 x sheet 2 gives {dict(sorted(have45.items()))}")
check(covers(have45, add(need_45, {"2 by 3": 1})),
      "Grades 4-5 group also has a 2 by 3 for Problem 3 (with the spare 2 by 4)")
spare_k1 = {n: add(S1, S1, S2).get(n, 0) - 2 * need_k1.get(n, 0) for n in ("2 by 3", "3 by 3", "3 by 4")}
check(all(v >= 1 for v in spare_k1.values()),
      f"K-1 table keeps a spare 2 by 3, 3 by 3 and 3 by 4 for checking Problem 8: {spare_k1}")
check(sum(1 for n in supplied[1] + supplied[2] if n == whole) >= 1, "a launch bar on the per-table sheet")


# ---------------------------------------------------------------- boards
def boards_and_spots(page):
    dr = page.get_drawings()
    boards = [d["rect"] for d in dr if d["type"] == "s" and gray(d.get("color"), 0.55)
              and any(it[0] == "c" for it in d["items"])]
    spots = [d["rect"] for d in dr if d["type"] == "f" and gray(d.get("fill"), 0.0)
             and all(it[0] == "c" for it in d["items"]) and mm(d["rect"].width) < 5]
    out = []
    for B in boards:
        inside = [((S.x0 + S.x1) / 2, (S.y0 + S.y1) / 2) for S in spots
                  if B.x0 < S.x0 and S.x1 < B.x1 and B.y0 < S.y0 and S.y1 < B.y1]
        out.append((B, inside))
    return out


def counter_gap(spots):
    """Gap between rows of three 12 mm counters (1 mm apart) centred under two spots."""
    (x1, _), (x2, _) = sorted(spots)
    return mm(x2 - x1) - (3 * COUNTER + 2)


mat = boards_and_spots(doc[2])
check(len(mat) == 2, f"p3: {len(mat)} boards (two games: longest and shortest)")
# the Grades 4-5 Problem 6 page
p6 = next(i for i, p in enumerate(d45) if "Problem 6:" in p.get_text())
stud = boards_and_spots(d45[p6])
check(len(stud) == 2 and all(len(s) == 2 for _, s in stud),
      f"Grades 4-5 Problem 6 (page {p6 + 1}) has 2 boards of 2 spots")
sB, sS = stud[0]
s_gap = counter_gap(sS)
for k, (B, S) in enumerate(mat, 1):
    check(abs(mm(B.width) - 186) <= TOL and abs(mm(B.height) - 102) <= TOL,
          f"p3 board {k}: {mm(B.width):.1f} x {mm(B.height):.1f} mm (186 x 102)")
    check(len(S) == 2, f"p3 board {k}: {len(S)} spots, as on the Problem 6 boards")
    if len(S) == 2:
        (xa, ya), (xb, yb) = sorted(S)
        dist = mm(((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5)
        check(abs(dist - 90) <= TOL and abs(mm(ya - yb)) < 0.1,
              f"p3 board {k}: spots side by side, {dist:.1f} mm apart (90)")
        cy = (B.y0 + B.y1) / 2
        (sxa, sya), (sxb, syb) = sorted(sS)
        check(abs(ya - cy) < 0.3 / PT and abs(((xa + xb) / 2) - (B.x0 + B.x1) / 2) < 0.3 / PT
              and abs(sya - syb) < 0.1 and abs(((sxa + sxb) / 2) - (sB.x0 + sB.x1) / 2) < 0.3 / PT,
              f"p3 board {k}: same layout as the student board (pair centred on the board)")
        edge = min(mm(xa - B.x0), mm(B.x1 - xb), mm(ya - B.y0), mm(B.y1 - ya))
        g = counter_gap(S)
        check(g >= 40 and edge >= 40,
              f"p3 board {k}: rows of three {COUNTER:.0f} mm counters leave {g:.0f} mm between them "
              f"(student board: {s_gap:.0f} mm); spots {edge:.0f} mm from the board edge")
notes.append(f"info Grades 4-5 Problem 6 student board: {mm(sB.width):.1f} x {mm(sB.height):.1f} mm, "
             f"spots {mm(abs(sS[0][0] - sS[1][0])):.1f} mm apart")

# scale bar
sb = [d["rect"] for d in doc[2].get_drawings() if d["type"] == "s" and gray(d.get("color"), 0.0)
      and d["rect"].height < 0.01 and mm(d["rect"].width) > 50]
check(len(sb) == 1 and abs(mm(sb[0].width) - 100) <= TOL,
      f"p3: scale bar measures {mm(sb[0].width):.2f} mm (100)" if sb else "p3: scale bar found")


# ---------------------------------------------------------------- pixels
DPI = 300
PX = 25.4 / DPI


def runs(vals, dark=128):
    """Centres (px) of dark runs in a 1-D list of gray values."""
    out, start = [], None
    for i, v in enumerate(vals + [255]):
        if v < dark and start is None:
            start = i
        elif v >= dark and start is not None:
            out.append((start + i - 1) / 2)
            start = None
    return out


def pix(pno):
    pm = doc[pno - 1].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
    return pm


pm = pix(1)
row = int((31 + 37.5) / PX)              # middle of the second row of squares, strip 1
lo, hi = int(18.5 / PX), int(197.5 / PX)  # between the margin labels
line = [pm.samples[row * pm.stride + x] for x in range(lo, hi)]
xs = runs(line, dark=200)                 # grid lines are 35% gray, outlines black
gaps = [(b - a) * PX for a, b in zip(xs, xs[1:])]
check(len(gaps) == 7 and all(abs(g - CELL) <= TOL for g in gaps),
      f"pixels p1: across strip 1, 8 lines spaced {', '.join(f'{g:.2f}' for g in gaps)} mm")
heavy_x = runs(line, dark=60)
check(len(heavy_x) == 3 and abs((heavy_x[1] - heavy_x[0]) * PX - 100) <= TOL
      and abs((heavy_x[2] - heavy_x[1]) * PX - 75) <= TOL,
      "pixels p1: heavy outlines give the 3 by 4 bar 100 mm and the 3 by 3 bar 75 mm wide "
      f"({(heavy_x[1] - heavy_x[0]) * PX:.2f}, {(heavy_x[2] - heavy_x[1]) * PX:.2f})")
col = int((20.45 + 12.5) / PX)
vline = [pm.samples[y * pm.stride + col] for y in range(pm.height)]
ys = [y for y in runs(vline, dark=200) if 28 / PX < y < 258 / PX]
vg = [(b - a) * PX for a, b in zip(ys, ys[1:])]
check(len(vg) == 9 and all(abs(g - CELL) <= TOL for g in vg),
      f"pixels p1: down the first column, 9 rows of {min(vg):.2f}-{max(vg):.2f} mm")
pm3 = pix(3)
row = int(84 / PX)
line = [pm3.samples[row * pm3.stride + x] for x in range(pm3.width)]
blobs = [x for x in runs(line, dark=60)]
check(len(blobs) == 2 and abs((blobs[1] - blobs[0]) * PX - 90) <= TOL,
      f"pixels p3: spots {(blobs[1] - blobs[0]) * PX:.2f} mm apart" if len(blobs) == 2 else
      f"pixels p3: found {len(blobs)} dark runs on the spot row")
row = int(251 / PX)
line = [pm3.samples[row * pm3.stride + x] for x in range(pm3.width)]
dark = [x for x, v in enumerate(line) if v < 128 and x < 117 / PX]   # stop before the "100 mm" label
check(dark and abs((dark[-1] - dark[0] + 1) * PX - 100 - 0.21) <= TOL,
      f"pixels p3: scale bar {(dark[-1] - dark[0] + 1) * PX:.2f} mm including its 0.6 pt end ticks")


# ---------------------------------------------------------------- text
allowed = [HEADER, FOOTER, "Bars, sheet 1", "Bars, sheet 2", "2-spot Sprouts boards",
           "Grades 4–5 Problem 6", "100 mm", "1", "2", "3"]
extra = [t for p in doc for t, _, _ in spans(p) if t not in allowed and not LABEL.match(t)]
check(not extra, "only short labels on the sheets" + (f": unexpected {extra}" if extra else ""))
banned = re.compile(r"break|move|win|1st|2nd|first|second|line|token|square|even|odd", re.I)
hits = [t for p in doc for t, _, _ in spans(p) if t not in (HEADER, FOOTER) and banned.search(t)]
check(not hits, "no text names a count, a winner or a rule (nothing that answers a problem)")

# ---------------------------------------------------------------- log
if os.path.exists(LOG):
    log = open(LOG, encoding="latin-1").read()
    check(not re.search(r"^!|Overfull|Underfull", log, re.M), "LaTeX log: no errors, overfull or underfull boxes")
else:
    check(False, "LaTeX log present (run ./build.sh first)")

print("\n".join(notes))
print("\n".join(failures))
print(f"\n{len(notes) - sum(n.startswith('info') for n in notes)} checks passed, {len(failures)} failed")
sys.exit(1 if failures else 0)
