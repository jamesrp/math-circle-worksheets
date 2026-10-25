#!/usr/bin/env python3
"""Measure the delivered Pancake flips materials PDF (../materials.pdf).

Checks, on the PDF itself (not the generator):
  1. one US Letter page;
  2. vector: six dark-brown discs, 40, 50, 60, 70, 80 and 90 mm across (within
     0.5 mm), round (equal width and height; Bezier points within 0.5 mm of the
     circle), each with a matching black cut line; one spatula about 145 x 42 mm
     with an 18 mm handle; a 100 mm scale bar;
  3. text: each disc carries its number (1 in the 40 mm disc ... 6 in the 90 mm
     disc), and the page holds no other words than header, title, scale label,
     "spatula" and footer (so no stack, count or answer is printed);
  4. raster at 600 dpi: the same diameters, spatula, handle and scale bar
     measured in pixels (ink extent minus the 0.6 pt cut line), within 0.5 mm,
     and no ink within 12 mm of any paper edge;
  5. spacing: at least 5 mm between pieces (cut line to cut line) and at least
     3 mm between any piece and any label or rule;
  6. coverage: the pancake numbers and dark sides drawn in the student pages'
     sources are all supplied.
Prints a report and exits non-zero on any failure.
"""
import math
import os
import re
import sys

import numpy as np
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(os.path.dirname(HERE), "materials.pdf")
STUDENT_SRC = os.path.join(os.path.dirname(HERE), "src")

MM = 25.4 / 72.0                    # mm per pt
TOL = 0.5                           # mm
STROKE = 0.6 * 25.4 / 72.27          # cut-line width (0.6 TeX pt), mm
EXPECT_D = {1: 40.0, 2: 50.0, 3: 60.0, 4: 70.0, 5: 80.0, 6: 90.0}
BROWN = (85 / 255, 50 / 255, 20 / 255)
SPATULA = dict(length=145.0, blade=42.0, handle=18.0)
EXPECT_TEXT = {
    "Week NN / Pancake flips / Materials",
    "Pancakes and spatula",
    "100 mm",
    "1", "2", "3", "4", "5", "6",
    "spatula",
    "Bellingham Math Circle / Week NN / NN-M-v1",
}

fails = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        fails.append(msg)


def close(a, b, tol=0.02):
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def bezier(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0.x + 3 * u * u * t * p1.x + 3 * u * t * t * p2.x + t**3 * p3.x,
            u**3 * p0.y + 3 * u * u * t * p1.y + 3 * u * t * t * p2.y + t**3 * p3.y)


def path_points(d, n=24):
    """Sample a drawing's outline (pt)."""
    pts = []
    for it in d["items"]:
        if it[0] == "l":
            a, b = it[1], it[2]
            pts += [(a.x + (b.x - a.x) * k / n, a.y + (b.y - a.y) * k / n) for k in range(n + 1)]
        elif it[0] == "c":
            pts += [bezier(it[1], it[2], it[3], it[4], k / n) for k in range(n + 1)]
        elif it[0] == "re":
            r = it[1]
            pts += [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
    return pts


def main():
    doc = pymupdf.open(PDF)
    print(f"Checking {PDF}")
    print("1. Page")
    ok(doc.page_count == 1, f"page count {doc.page_count} (expected 1)")
    page = doc[0]
    w, h = page.rect.width, page.rect.height
    ok(abs(w - 612) < 0.5 and abs(h - 792) < 0.5, f"page size {w:.1f} x {h:.1f} pt (US Letter 612 x 792)")

    print("2. Vector paths")
    draws = page.get_drawings()
    discs = [d for d in draws if d.get("fill") and close(d["fill"], BROWN)]
    ok(len(discs) == 6, f"{len(discs)} dark-brown discs (expected 6)")
    circles = []      # (diameter mm, cx pt, cy pt, r pt)
    for d in discs:
        r = d["rect"]
        wd, ht = r.width * MM, r.height * MM
        cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        rad = r.width / 2
        dev = max(abs(math.hypot(x - cx, y - cy) - rad) for x, y in path_points(d)) * MM
        circles.append((wd, cx, cy, rad))
        ok(abs(wd - ht) <= 0.05 and dev <= TOL,
           f"disc at ({cx*MM:.1f}, {cy*MM:.1f}) mm: {wd:.2f} x {ht:.2f} mm, outline within {dev:.3f} mm of a circle")
        # the cut line is the disc's own stroke (PyMuPDF merges fill and stroke) or a separate path
        cut = [c for c in draws if c.get("color") and close(c["color"], (0, 0, 0))
               and abs(c["rect"].x0 - r.x0) < 0.1 and abs(c["rect"].y0 - r.y0) < 0.1
               and abs(c["rect"].width - r.width) < 0.1]
        ok(len(cut) >= 1 and all(abs(c["width"] - 0.6 * 72 / 72.27) < 0.01 for c in cut),
           f"  black 0.6 pt cut line on the {wd:.1f} mm disc, on the disc's edge")
    dias = sorted(round(c[0], 2) for c in circles)
    ok(all(abs(a - b) <= TOL for a, b in zip(dias, sorted(EXPECT_D.values()))) and len(dias) == 6,
       f"vector diameters {dias} mm vs {sorted(EXPECT_D.values())} (tolerance {TOL} mm)")
    steps = [b - a for a, b in zip(dias, dias[1:])]
    ok(all(s >= 10 - TOL for s in steps), f"neighbouring sizes differ by {steps} mm (at least 1 cm)")

    spat = [d for d in draws if d.get("fill") and close(d["fill"], (0.88, 0.88, 0.88))]
    ok(len(spat) == 1, f"{len(spat)} spatula shape (expected 1)")
    sp = spat[0]
    sr = sp["rect"]
    ok(abs(sr.width * MM - SPATULA["length"]) <= TOL and abs(sr.height * MM - SPATULA["blade"]) <= TOL,
       f"spatula {sr.width*MM:.2f} x {sr.height*MM:.2f} mm (expected {SPATULA['length']} x {SPATULA['blade']})")
    sp_pts = path_points(sp)
    hx0 = sr.x0 + (80 + 12 + 5) / MM          # inside the straight part of the handle
    hx1 = sr.x1 - 12 / MM
    hy = [y for x, y in sp_pts if hx0 <= x <= hx1]
    hw = (max(hy) - min(hy)) * MM
    ok(abs(hw - SPATULA["handle"]) <= TOL, f"spatula handle {hw:.2f} mm wide (expected {SPATULA['handle']})")

    bars = []
    for d in draws:
        for it in d["items"]:
            if it[0] == "l" and abs(it[1].y - it[2].y) < 0.01:
                bars.append((abs(it[2].x - it[1].x) * MM, it[1], it[2], d))
    scale = [b for b in bars if abs(b[0] - 100) <= 2]
    ok(len(scale) == 1 and abs(scale[0][0] - 100) <= TOL,
       f"scale bar {scale[0][0]:.2f} mm (expected 100)" if scale else "scale bar found")

    print("3. Text")
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if txt:
                spans.append((txt, ln["spans"][0]["color"], pymupdf.Rect(ln["bbox"])))
    texts = {t for t, _, _ in spans}
    page_no = [t for t in texts if t == "1"]
    ok(texts == EXPECT_TEXT, f"page text is exactly the expected labels: {sorted(texts)}")
    for t, col, bb in spans:
        if col == 0xFFFFFF:
            k = int(t)
            c = min(circles, key=lambda c: math.hypot(c[1] - (bb.x0 + bb.x1) / 2, c[2] - (bb.y0 + bb.y1) / 2))
            inside = math.hypot(c[1] - (bb.x0 + bb.x1) / 2, c[2] - (bb.y0 + bb.y1) / 2) < c[3] / 3
            ok(inside and abs(c[0] - EXPECT_D[k]) <= TOL,
               f"white number {k} sits in the {c[0]:.1f} mm disc (expected {EXPECT_D[k]:.0f} mm)")
    whites = sorted(int(t) for t, col, _ in spans if col == 0xFFFFFF)
    ok(whites == [1, 2, 3, 4, 5, 6], f"numbers on the discs: {whites}")
    labels = [bb for t, col, bb in spans if col != 0xFFFFFF and t != "spatula"]

    print("4. Raster at 600 dpi")
    dpi = 600
    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    ink = img < 200
    pxmm = dpi / 25.4
    ys, xs = np.nonzero(img < 250)
    m = {"left": xs.min() / pxmm, "right": (pix.width - 1 - xs.max()) / pxmm,
         "top": ys.min() / pxmm, "bottom": (pix.height - 1 - ys.max()) / pxmm}
    ok(min(m.values()) >= 12.0, "ink to paper edges: " + ", ".join(f"{k} {v:.1f} mm" for k, v in m.items())
       + " (at least 12 mm)")

    def extent(line, lo, hi):
        idx = np.nonzero(line[lo:hi])[0]
        return (idx.max() - idx.min() + 1) / pxmm if idx.size else 0.0

    for dmm, cx, cy, rad in sorted(circles):
        X, Y = cx / 72 * dpi, cy / 72 * dpi
        win = int((rad * MM + 3) * pxmm)
        row = ink[int(round(Y)), :]
        col = ink[:, int(round(X))]
        hx = extent(row, int(X) - win, int(X) + win) - STROKE
        vy = extent(col, int(Y) - win, int(Y) + win) - STROKE
        # diagonal: ink extent along the 45 degree line through the centre
        t = np.arange(-win, win + 1)
        dg = ink[(Y + t / math.sqrt(2)).astype(int), (X + t / math.sqrt(2)).astype(int)]
        idx = np.nonzero(dg)[0]
        dd = (idx.max() - idx.min() + 1) / pxmm - STROKE
        k = [n for n, v in EXPECT_D.items() if abs(v - dmm) < 1][0]
        e = EXPECT_D[k]
        ok(max(abs(hx - e), abs(vy - e), abs(dd - e)) <= TOL,
           f"pancake {k}: {hx:.2f} across, {vy:.2f} down, {dd:.2f} diagonal (expected {e:.0f} mm)")

    x0, y0, x1, y1 = (int(v / 72 * dpi) for v in (sr.x0, sr.y0, sr.x1, sr.y1))
    pad = int(3 * pxmm)
    sub = ink[y0 - pad:y1 + pad, x0 - pad:x1 + pad]
    yy, xx = np.nonzero(sub)
    sl = (xx.max() - xx.min() + 1) / pxmm - STROKE
    sb = (yy.max() - yy.min() + 1) / pxmm - STROKE
    hcol = ink[y0 - pad:y1 + pad, int((x1 - 25 * pxmm))]
    hh = extent(hcol, 0, hcol.size) - STROKE
    ok(abs(sl - SPATULA["length"]) <= TOL and abs(sb - SPATULA["blade"]) <= TOL and abs(hh - SPATULA["handle"]) <= TOL,
       f"spatula {sl:.2f} long, blade {sb:.2f}, handle {hh:.2f} mm (expected 145, 42, 18)")
    if scale:
        _, a, b, _ = scale[0]
        Y = int(round(a.y / 72 * dpi))
        lo, hi = int(min(a.x, b.x) / 72 * dpi) - pad, int(max(a.x, b.x) / 72 * dpi) + pad
        sc = extent(ink[Y, :], lo, hi) - STROKE
        ok(abs(sc - 100) <= TOL, f"scale bar {sc:.2f} mm in pixels (expected 100)")

    print("5. Spacing")
    gaps = []
    names = {}
    for dmm, cx, cy, rad in circles:
        k = [n for n, v in EXPECT_D.items() if abs(v - dmm) < 1][0]
        names[k] = (cx, cy, rad)
    for a in names:
        for b in names:
            if a < b:
                (xa, ya, ra), (xb, yb, rb) = names[a], names[b]
                gaps.append(((math.hypot(xa - xb, ya - yb) - ra - rb) * MM, f"pancakes {a} and {b}"))
        xa, ya, ra = names[a]
        gs = min(math.hypot(x - xa, y - ya) for x, y in sp_pts) - ra
        gaps.append((gs * MM, f"pancake {a} and spatula"))
    g, what = min(gaps)
    ok(g >= 5.0, f"closest pieces: {what}, {g:.1f} mm apart (at least 5 mm)")
    # labels and rules against pieces
    rules = [pymupdf.Rect(min(it[1].x, it[2].x), it[1].y, max(it[1].x, it[2].x), it[1].y)
             for d in draws if d.get("color") and not d.get("fill") for it in d["items"]
             if it[0] == "l" and abs(it[1].y - it[2].y) < 0.01]
    obstacles = labels + rules
    lab_gap = []
    for k, (cx, cy, rad) in names.items():
        for bb in obstacles:
            dx = max(bb.x0 - cx, 0, cx - bb.x1)
            dy = max(bb.y0 - cy, 0, cy - bb.y1)
            lab_gap.append(((math.hypot(dx, dy) - rad) * MM, f"pancake {k}"))
    for bb in obstacles:
        gs = min(math.hypot(max(bb.x0 - x, 0, x - bb.x1), max(bb.y0 - y, 0, y - bb.y1)) for x, y in sp_pts)
        lab_gap.append((gs * MM, "spatula"))
    g, what = min(lab_gap)
    ok(g >= 3.0, f"closest label or rule to a piece: {what}, {g:.1f} mm (at least 3 mm)")

    print("6. Coverage of the student pages")
    need_all, need_dark = set(), set()
    for band in ("k-1", "grades-2-3", "grades-4-5"):
        tex = open(os.path.join(STUDENT_SRC, band + ".tex")).read()
        nums = [int(n) for n in re.findall(r"bfseries, inner sep=0pt\] at \([^)]*\) \{(\d+)\}", tex)]
        # a dark-side pancake is drawn with \fill[burnt] inside a clip just before its number node
        dark = [int(n) for n in re.findall(
            r"\\fill\[burnt\][^\n]*\n\\end\{scope\}\n\\draw\[cakedraw\][^\n]*\n\\node\[font=[^\]]*\] at \([^)]*\) \{(\d+)\}",
            tex)]
        need_all |= set(nums)
        need_dark |= set(dark)
        print(f"  {band}: pancakes drawn {sorted(set(nums))}, with dark sides {sorted(set(dark))}")
    ok(need_all <= set(whites), f"every pancake number drawn in a packet ({sorted(need_all)}) is supplied")
    ok(need_dark <= set(whites), f"every dark-sided pancake drawn ({sorted(need_dark)}) is supplied with a dark face")

    print()
    print("ALL CHECKS PASSED" if not fails else f"{len(fails)} CHECK(S) FAILED")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
