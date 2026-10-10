#!/usr/bin/env python3
"""Diagram check for Week 41 (torus portals) and its bonus companion.

Reads the delivered PDFs with pdfplumber (letters, rectangles, arrowheads) and the
generated TeX in source/week-41/editable/src for exact TikZ coordinates (portal marks,
edge arrows, example paths).  Written for the review; imports none of the packet's code.

Run from anywhere:  python3 check_diagrams.py   (output saved to out_check_diagrams.txt)
"""
import re
import sys
from collections import Counter
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[4] if len(HERE.parents) > 4 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in HERE.parents:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found")


REPO = find_repo()
Y2 = REPO / "lowell-math-circle-year-2"
OUT, FAIL = [], []
MM = 72 / 25.4


def log(s=""):
    OUT.append(s)
    print(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


BOARD = [["A", "B", "C"], ["D", "H", "E"], ["F", "G", "I"]]  # rows top to bottom
NUM = r"(-?[\d.]+)"


def letters_in(page, x0, top, w, h, size_min=0):
    """Single capital letters whose centre lies inside the box, as (letter, cx, cy)."""
    res = []
    for ch in page.chars:
        if len(ch["text"]) == 1 and ch["text"] in "ABCDEFGHIX" and ch["size"] >= size_min:
            cx = (ch["x0"] + ch["x1"]) / 2
            cy = (ch["top"] + ch["bottom"]) / 2
            if x0 < cx < x0 + w and top < cy < top + h:
                # skip letters that are part of a word (e.g. "Problem", "H" inside text)
                res.append((ch["text"], cx, cy, ch))
    return res


def isolated(page, ch):
    """True if the char is not adjacent to other letters on its line (i.e. a label)."""
    for o in page.chars:
        if o is ch:
            continue
        if abs(o["top"] - ch["top"]) < 1 and (0 <= o["x0"] - ch["x1"] < 1.5 or 0 <= ch["x0"] - o["x1"] < 1.5):
            if o["text"].strip():
                return False
    return True


def board_layout(page, r):
    """Map each 3x3 cell of rect r to the isolated letter labels inside it."""
    x0, top, w, h = r["x0"], r["top"], r["width"], r["height"]
    cells = {}
    for t, cx, cy, ch in letters_in(page, x0, top, w, h):
        if not isolated(page, ch):
            continue
        c = int((cx - x0) // (w / 3))
        rr = int((cy - top) // (h / 3))
        cells.setdefault((rr, c), []).append(t)
    return cells


# ======================================================================= base packets
log("== Base student packets: boards found in the PDFs")
bands = {"k-1": "week-41-k-1.pdf", "grades-2-3": "week-41-grades-2-3.pdf", "grades-4-5": "week-41-grades-4-5.pdf"}
for band, fn in bands.items():
    pdf = pdfplumber.open(Y2 / "week-41" / fn)
    for pn, page in enumerate(pdf.pages, 1):
        boards = [r for r in page.rects if abs(r["linewidth"] - 0.8966) < 0.01 and r["width"] > 60]
        for r in boards:
            sq = abs(r["width"] - r["height"]) < 0.05
            cells = board_layout(page, r)
            full = all(cells.get((i, j)) == [BOARD[i][j]] for i in range(3) for j in range(3))
            only_h = cells == {(1, 1): ["H"]}
            kind = "lettered board" if full else ("copy with H only" if only_h else f"OTHER {cells}")
            ok = sq and (full or only_h)
            check(ok, f"{band} p.{pn}: {r['width'] / MM:.1f} mm square={sq}; {kind}")

# ---------------------------------------------------------------- TeX: portal marks and arrows per board
log("")
log("== Base TeX: portal marks on every lettered board (shape pairs and arrow directions)")
for band in bands:
    tex = (Y2 / f"source/week-41/editable/src/{band}.tex").read_text()
    pages = tex.split(r"\newpage")
    for pn, pg in enumerate(pages, 1):
        rects = [tuple(map(float, m)) for m in re.findall(
            r"\\draw\[line width=\.9pt\] \(" + NUM + "," + NUM + r"\) rectangle \+\+\(" + NUM + "," + NUM + r"\);", pg)]
        circles = [tuple(map(float, m)) for m in re.findall(r"\\draw\[fill=white,line width=\.7pt\] \(" + NUM + "," + NUM + r"\) circle \(1\.7\);", pg)]
        diamonds = [tuple(map(float, m)) for m in re.findall(
            r"\\draw\[fill=white,line width=\.7pt\] \(" + NUM + "," + NUM + r"\)--\(" + NUM + "," + NUM + r"\)--\(" + NUM + "," + NUM + r"\)--\(" + NUM + "," + NUM + r"\)--cycle;", pg)]
        arrows = [tuple(map(float, m)) for m in re.findall(
            r"\\draw\[-\{Stealth\[length=2\.4mm\]\},line width=1\.3pt\] \(" + NUM + "," + NUM + r"\)--\(" + NUM + "," + NUM + r"\);", pg)]
        for (x, y, w, h) in rects:
            if w != h:
                check(False, f"{band} p.{pn} board at ({x},{y}) not square")
                continue
            # marks on this board
            cl = [c for c in circles if abs(c[0] - x) < 1e-6 or abs(c[0] - (x + w)) < 1e-6 if y <= c[1] <= y + h]
            dm = [((d[0] + d[4]) / 2, d[3]) for d in diamonds if y - 0.01 <= d[3] <= y + h + 0.01 and x <= d[0] <= x + w
                  and (abs(d[3] - y) < 1e-6 or abs(d[3] - (y + h)) < 1e-6)]
            ar = [a for a in arrows if x - 0.01 <= min(a[0], a[2]) and max(a[0], a[2]) <= x + w + 0.01
                  and y - 0.01 <= min(a[1], a[3]) and max(a[1], a[3]) <= y + h + 0.01]
            if not (cl or dm or ar):
                continue  # copy tiles without portal marks
            lr = sorted(cl)
            circ_ok = len(lr) == 2 and abs(lr[0][1] - lr[1][1]) < 1e-6 and {round(lr[0][0], 3), round(lr[1][0], 3)} == {round(x, 3), round(x + w, 3)}
            dia_ok = len(dm) == 2 and abs(dm[0][0] - dm[1][0]) < 1e-6 and {round(dm[0][1], 3), round(dm[1][1], 3)} == {round(y, 3), round(y + h, 3)}
            vert = [a for a in ar if a[0] == a[2]]
            horz = [a for a in ar if a[1] == a[3]]
            v_ok = len(vert) == 2 and {a[0] for a in vert} == {x, x + w} and len({(a[1], a[3]) for a in vert}) == 1
            h_ok = len(horz) == 2 and {a[1] for a in horz} == {y, y + h} and len({(a[0], a[2]) for a in horz}) == 1
            vdir = "up" if vert and vert[0][3] < vert[0][1] else "down"
            hdir = "right" if horz and horz[0][2] > horz[0][0] else "left"
            check(circ_ok and dia_ok and v_ok and h_ok,
                  f"{band} p.{pn} board {w:.0f} mm: circles at same height on left/right ({circ_ok}), diamonds at same x on top/bottom ({dia_ok}), "
                  f"side arrows same position and direction ({v_ok}, {vdir}), top/bottom arrows same ({h_ok}, {hdir})")

# ---------------------------------------------------------------- TeX: repeated maps and coordinates
log("")
log("== Base TeX: repeated maps (original frame, coordinate labels)")
for band in ["grades-2-3", "grades-4-5"]:
    tex = (Y2 / f"source/week-41/editable/src/{band}.tex").read_text()
    for pn, pg in enumerate(tex.split(r"\newpage"), 1):
        thick = [tuple(map(float, m)) for m in re.findall(
            r"\\draw\[line width=1\.7pt\] \(" + NUM + "," + NUM + r"\) rectangle \+\+\(" + NUM + "," + NUM + r"\);", pg)]
        rects = [tuple(map(float, m)) for m in re.findall(
            r"\\draw\[line width=\.9pt\] \(" + NUM + "," + NUM + r"\) rectangle \+\+\(" + NUM + "," + NUM + r"\);", pg)]
        coords = [(float(a), float(b), int(c), int(d)) for a, b, c, d in re.findall(
            r"at \(" + NUM + "," + NUM + r"\) \{\$\((-?\d+),(-?\d+)\)\$\}", pg)]
        for (tx, ty, s, _) in thick:
            tiles = [r for r in rects if r[2] == s and tx - s - 1e-6 <= r[0] <= tx + s + 1e-6 and ty - s - 1e-6 <= r[1] <= ty + s + 1e-6]
            centre = (tx, ty, s, s) in tiles
            check(len(tiles) == 9 and centre, f"{band} p.{pn}: 3x3 array of {s:.0f} mm copies with the bold frame on the centre copy")
            if coords:
                good = True
                for (lx, ly, m, n) in coords:
                    c = int((lx - (tx - s)) // s)
                    r = int((ly - (ty - s)) // s)
                    if (m, n) != (c - 1, 1 - r):
                        good = False
                check(len(coords) == 9 and good, f"{band} p.{pn}: the nine (m,n) labels sit in their copies (right = +m, up = +n)")

# ---------------------------------------------------------------- TeX: page-1 example and the slide example
log("")
log("== Base TeX: page-1 worked example and the Grades 4-5 square-slide example")
for band in bands:
    tex = (Y2 / f"source/week-41/editable/src/{band}.tex").read_text()
    pg = tex.split(r"\newpage")[0]
    labs = {(float(a), float(b)): t for a, b, t in re.findall(r"at \(" + NUM + "," + NUM + r"\) \{([A-I])\};", pg)}
    dots = [(float(a), float(b)) for a, b in re.findall(r"\\fill\[gray\] \(" + NUM + "," + NUM + r"\) circle \(\.55\);", pg)]

    def dot_label(p):
        # label is 4 mm above its dot
        for (lx, ly), t in labs.items():
            if abs(lx - p[0]) < 1e-6 and abs(ly - (p[1] - 4)) < 1e-6:
                return t
        return None

    blue = [tuple(map(float, m)) for m in re.findall(
        r"\\draw\[-\{Stealth\[length=2mm\]\},blue!65!black,line width=1\.1pt\] \(" + NUM + "," + NUM + r"\)--\(" + NUM + "," + NUM + r"\);", pg)]
    # input board 17..65, output copies 106..151..196
    a1, a2, a3 = blue
    ok_in = dot_label((a1[0], a1[1])) == "H" and a1[2] == 65 and a1[1] == a1[3] and \
        any(abs(d[0] - 57) < 1e-6 and abs(d[1] - 97) < 1e-6 for d in dots) and dot_label((57.0, 97.0)) == "E"
    ok_in2 = a2[0] == 17 and dot_label((a2[2], a2[3])) == "D" and a2[1] == a1[1]
    ok_out = dot_label((a3[0], a3[1])) == "H" and dot_label((a3[2], a3[3])) == "D" and a3[0] < 151 < a3[2]
    check(ok_in and ok_in2 and ok_out, f"{band} p.1: input arrow H→(through E)→right edge, left edge→D at the same height; output arrow original H → D of next copy")

tex = (Y2 / "source/week-41/editable/src/grades-4-5.tex").read_text()
pg = tex.split(r"\newpage")[3]
paths = re.findall(r"\\draw\[-\{\{?Stealth\[length=2\.5mm\]\}?\},blue!65!black,line width=1\.4pt\] ((?:\(-?[\d.]+,-?[\d.]+\)(?:--)?)+);", pg)
labs = [(float(a), float(b), t) for a, b, t in re.findall(r"at \(" + NUM + "," + NUM + r"\) \{([DHFG])\};", pg)]
vertex_dots = [(float(a), float(b)) for a, b in re.findall(r"\\fill \(" + NUM + "," + NUM + r"\) circle \(\.7\);", pg)]


def name_of(p):
    for (lx, ly, t) in labs:
        if abs(lx + 5 - p[0]) < 1e-6 and abs(ly + 5 - p[1]) < 1e-6:
            return t
    return None


got = []
for pth in paths:
    pts = [tuple(map(float, q)) for q in re.findall(r"\((-?[\d.]+),(-?[\d.]+)\)", pth)]
    got.append("→".join(name_of(p) or "?" for p in pts))
log(f"   slide example paths: {got}")
check(got == ["F→G→H", "F→D→H"], "slide example: input F→G→H, output F→D→H, endpoints fixed")
# geometry: D upper-left, H upper-right, F lower-left, G lower-right in each panel
pos = {}
for (lx, ly, t) in labs:
    pos.setdefault(t, []).append((lx + 5, ly + 5))
ok = all(pos["D"][i][0] == pos["F"][i][0] and pos["H"][i][0] == pos["G"][i][0] and pos["D"][i][1] == pos["H"][i][1]
         and pos["F"][i][1] == pos["G"][i][1] and pos["D"][i][0] < pos["H"][i][0] and pos["D"][i][1] < pos["F"][i][1] for i in range(2))
check(ok, "slide example labels: D H on top, F G below, matching the lower-left block of the portal map")

# ======================================================================= bonus
log("")
log("== Bonus student PDF")
pdf = pdfplumber.open(Y2 / "week-41/week-41-bonus.pdf")
BOT = [["A", "B", "C"], ["D", "H", "E"], ["F", "G", "I"]]
for pn in (1, 2):
    page = pdf.pages[pn - 1]
    cells78 = [r for r in page.rects if abs(r["width"] - 78) < 0.1 and abs(r["height"] - 78) < 0.1]
    x0 = min(r["x0"] for r in cells78)
    t0 = min(r["top"] for r in cells78)
    box = {"x0": x0, "top": t0, "width": 234, "height": 234}
    cells = board_layout(page, box)
    full = all(cells.get((i, j)) == [BOT[i][j]] for i in range(3) for j in range(3))
    check(len(cells78) == 9 and full, f"bonus p.{pn}: 3x3 portal board with 27.5 mm square cells, labels A B C / D H E / F G I")
    heads = [c for c in page.curves if c["fill"] and len(c["pts"]) == 4]
    side = [c for c in heads if (c["pts"][0][0] < x0 or c["pts"][0][0] > x0 + 234) and t0 <= c["pts"][0][1] <= t0 + 234]
    topbot = [c for c in heads if (c["pts"][0][1] < t0 or c["pts"][0][1] > t0 + 234) and x0 <= c["pts"][0][0] <= x0 + 234]
    log(f"   bonus p.{pn}: seam arrowheads beside the left/right edges: {len(side)}; above/below the top/bottom edges: {len(topbot)}")
    check(len(side) == 6, f"bonus p.{pn}: each row has a right-pointing arrow on both sides")
    check(len(topbot) > 0, f"bonus p.{pn}: the top/bottom seam is marked on the board (the text says columns also wrap)")
    # example strip
    strip = [r for r in page.rects if abs(r["width"] - 38) < 0.1]
    seq = []
    for r in sorted(strip, key=lambda r: r["x0"]):
        ls = [t for t, *_ in letters_in(page, r["x0"], r["top"], r["width"], r["height"])]
        seq.append("".join(ls))
    want = ["H", "E", "H"] if pn == 1 else ["H", "E", "D"]
    check(seq == want, f"bonus p.{pn}: example strip {seq} (RL gives H,E,H; RR gives H,E,D)")

page = pdf.pages[1]
small = [r for r in page.rects if abs(r["width"] - 24) < 0.1 and abs(r["height"] - 24) < 0.1]
x0 = min(r["x0"] for r in small)
t0 = min(r["top"] for r in small)
ok = len(small) == 81
for r in small:
    ls = [t for t, *_ in letters_in(page, r["x0"], r["top"], 24, 24)]
    i = round((r["top"] - t0) / 24)
    j = round((r["x0"] - x0) / 24)
    if ls != [BOT[i % 3][j % 3]]:
        ok = False
check(ok, "bonus p.2: repeated map is nine copies of A B C / D H E / F G I with 8.5 mm cells")
thick = [r for r in page.rects if r["linewidth"] >= 1.9]
check(len(thick) == 1 and abs(thick[0]["x0"] - (x0 + 72)) < 0.1 and abs(thick[0]["top"] - (t0 + 72)) < 0.1 and abs(thick[0]["width"] - 72) < 0.1,
      "bonus p.2: bold frame on the centre copy")

page = pdf.pages[2]
cells64 = [r for r in page.rects if abs(r["width"] - 64) < 0.1 and abs(r["height"] - 64) < 0.1]
x0 = min(r["x0"] for r in cells64)
t0 = min(r["top"] for r in cells64)
grid = {}
for r in cells64:
    j = round((r["x0"] - x0) / 64)
    i = round((r["top"] - t0) / 64)
    ls = [t for t, *_ in letters_in(page, r["x0"], r["top"], 64, 64, size_min=13)]
    grid[(i, j)] = (ls, r["fill"])
# original H at row 4 col 2 (from the top-left); lifted (x, y) = (j-2, 4-i)
ok = len(grid) == 49
for (i, j), (ls, fill) in grid.items():
    x, y = j - 2, 4 - i
    true = BOT[2 - ((y + 1) % 3)][(x + 1) % 3]
    shown = "X" if true in "BE" else true
    if ls != [shown] or fill != (true in "BE"):
        ok = False
check(ok, "bonus p.3: 7x7 patch matches the periodic labels; exactly the B and E cells are shaded and marked X")
circles = [c for c in page.curves if not c["fill"] and len(c["pts"]) >= 4]
centres = []
for c in circles:
    xs = [p[0] for p in c["pts"]]
    ys = [p[1] for p in c["pts"]]
    centres.append(((max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2))
targets = set()
for cx, cy in centres:
    j = int((cx - x0) // 64)
    i = int((cy - t0) // 64)
    targets.add((j - 2, 4 - i))
check(targets == {(3, 0), (0, 3), (3, 3)}, f"bonus p.3: circled cells are lifted {sorted(targets)} = right, up, right+up copies of H")
words = page.extract_words()
orig = [w for w in words if w["text"] == "original" and w["top"] > t0]
check(len(orig) == 1 and int((orig[0]["x0"] + orig[0]["x1"]) / 2 - x0) // 64 == 2 and int(((orig[0]["top"] + orig[0]["bottom"]) / 2 - t0) // 64) == 4,
      "bonus p.3: 'original' sits in the H cell at row 5, column 3 of the patch")

log("")
log(f"TOTAL: {len(FAIL)} failures")
(HERE / "out_check_diagrams.txt").write_text("\n".join(OUT) + "\n")
