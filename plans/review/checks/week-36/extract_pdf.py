#!/usr/bin/env python3
"""Read every tile glyph from the delivered Week 36 student PDFs.

Shapes come from the PDF vector data (pdfplumber): a closed path of four Bezier
arcs is a circle, a closed three-segment polyline is a triangle, a filled black-
outlined rectangle is a square.  Fills are classified twice: from the vector fill
colour/pattern, and independently from pixels of a 150-dpi pdftoppm rendering
(open = no ink inside, solid = all ink, striped = mixed).  The two must agree.

Tiles are then grouped into 3x3 boards (nine centres on a square lattice) and
into loose groups (launch examples, pairs, number examples) by row band and page
half.  Numbers printed under tiles are attached to the tile directly above.

Run: python3 extract_pdf.py > out_extract_pdf.txt   (writes extracted.json)
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pdfplumber
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import PRINT, HERE, ok, note, finish  # noqa: E402

DPI = 150
STUDENT = ["week-36-k-1.pdf", "week-36-grades-2-3.pdf", "week-36-grades-4-5.pdf", "week-36-bonus.pdf"]
RENDER = Path(tempfile.mkdtemp(prefix="w36-render-"))   # renderings are not kept


def is_black(c):
    if c is None:
        return False
    if isinstance(c, (int, float)):
        return c == 0
    return isinstance(c, (tuple, list)) and all(abs(v) < 1e-6 for v in c)


def vector_fill(col):
    if isinstance(col, str):
        return "pattern"
    if isinstance(col, (int, float)):
        col = (col,)
    if col is None:
        return "none"
    v = sum(col) / len(col)
    if v > 0.99:
        return "white"
    if v < 0.01:
        return "black"
    return "gray%.2f" % v


def render(pdf):
    stem = RENDER / Path(pdf).stem
    subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", str(PRINT / pdf), str(stem)], check=True)
    pages = sorted(RENDER.glob(Path(pdf).stem + "-*.pgm"))
    return [Image.open(p).convert("L") for p in pages]


def pixel_fill(img, shape, x0, top, x1, bottom):
    """Fraction of dark and light pixels in an interior region of the glyph."""
    s = DPI / 72.0
    w, h = x1 - x0, bottom - top
    if shape == "triangle":
        cx, cy, r = (x0 + x1) / 2, top + 0.66 * h, 0.22 * w
    else:
        cx, cy, r = (x0 + x1) / 2, (top + bottom) / 2, 0.30 * w
    px = img.load()
    dark = light = n = 0
    X0, X1 = int((cx - r) * s), int((cx + r) * s)
    Y0, Y1 = int((cy - r) * s), int((cy + r) * s)
    for X in range(X0, X1 + 1):
        for Y in range(Y0, Y1 + 1):
            if (X / s - cx) ** 2 + (Y / s - cy) ** 2 > r * r:
                continue
            v = px[X, Y]
            n += 1
            dark += v < 170
            light += v > 225
    return dark / n, light / n


def classify_pixels(fd, fl):
    if fd > 0.85:
        return "solid"
    if fl > 0.95:
        return "open"
    if fd > 0.04 and fl > 0.15:
        return "striped"
    return "unclear(%.2f,%.2f)" % (fd, fl)


def glyphs(page):
    out = []
    for c in page.curves:
        if not (c["fill"] and c["stroke"] and is_black(c["stroking_color"])):
            continue
        ops = [seg[0] for seg in c["path"]]
        w, h = c["x1"] - c["x0"], c["bottom"] - c["top"]
        if max(w, h) < 7:          # arrowheads
            continue
        if ops.count("c") == 4 and ops.count("l") == 0:
            shape = "circle"
        elif ops.count("l") in (2, 3) and ops.count("c") == 0:
            pts = [seg[1] for seg in c["path"] if seg[0] in "ml"]
            uniq = []
            for p in pts:
                if all(abs(p[0] - q[0]) > 1e-3 or abs(p[1] - q[1]) > 1e-3 for q in uniq):
                    uniq.append(p)
            if len(uniq) == 3:
                shape = "triangle"
            elif len(uniq) == 4:
                shape = "square"
            else:
                continue
        else:
            continue
        out.append(dict(shape=shape, x0=c["x0"], x1=c["x1"], top=c["top"], bottom=c["bottom"],
                        vfill=vector_fill(c["non_stroking_color"]), path=[list(map(list, seg[1:])) for seg in c["path"]]))
    for r in page.rects:
        if not (r["fill"] and r["stroke"] and is_black(r["stroking_color"])):
            continue
        out.append(dict(shape="square", x0=r["x0"], x1=r["x1"], top=r["top"], bottom=r["bottom"],
                        vfill=vector_fill(r["non_stroking_color"]), path=None))
    return out


def hatch_lines(page):
    """ReportLab draws its stripes as separate gray lines clipped to the tile."""
    return [l for l in page.lines if abs((l["x1"] - l["x0"]) - (l["bottom"] - l["top"])) < 0.5
            and l["x1"] - l["x0"] > 5]


def lattice_boards(tiles):
    """Find 3x3 boards: nine centres at (x0 + i p, y0 + j p)."""
    used, boards = set(), []
    cen = [((t["x0"] + t["x1"]) / 2, (t["top"] + t["bottom"]) / 2) for t in tiles]
    order = sorted(range(len(tiles)), key=lambda i: (round(cen[i][1]), cen[i][0]))
    for i in order:
        if i in used:
            continue
        # candidate pitch: nearest tile to the right on (roughly) the same row
        right = [j for j in range(len(tiles)) if j not in used and j != i and abs(cen[j][1] - cen[i][1]) < 2
                 and cen[j][0] > cen[i][0] + 5 and tiles[j]["shape"] == tiles[i]["shape"]]
        if not right:
            continue
        j = min(right, key=lambda j: cen[j][0])
        p = cen[j][0] - cen[i][0]
        grid = []
        for row in range(3):
            line = []
            for col in range(3):
                want = (cen[i][0] + col * p, cen[i][1] + row * p)
                tol = 0.12 * p
                hit = [k for k in range(len(tiles)) if k not in used and abs(cen[k][0] - want[0]) < tol
                       and abs(cen[k][1] - want[1]) < tol]
                line.append(hit[0] if hit else None)
            grid.append(line)
        if all(k is not None for line in grid for k in line):
            boards.append(dict(pitch=p, grid=grid))
            used.update(k for line in grid for k in line)
    return boards, used


def main():
    data = {}
    for pdf in STUDENT:
        imgs = render(pdf)
        doc = pdfplumber.open(str(PRINT / pdf))
        data[pdf] = []
        print("==", pdf, "pages:", len(doc.pages))
        for pno, page in enumerate(doc.pages, 1):
            img = imgs[pno - 1]
            tiles = glyphs(page)
            hatch = hatch_lines(page)
            for t in tiles:
                fd, fl = pixel_fill(img, t["shape"], t["x0"], t["top"], t["x1"], t["bottom"])
                t["pix"] = [round(fd, 3), round(fl, 3)]
                t["fill_pixels"] = classify_pixels(fd, fl)
                cx, cy = (t["x0"] + t["x1"]) / 2, (t["top"] + t["bottom"]) / 2
                # gray stripe segments passing through the glyph's interior (ReportLab pages)
                n_h = 0
                for l in hatch:
                    # line through (l.x0, l.bottom) with slope -1 in top-based coordinates
                    # (it rises to the right); distance from centre to the line:
                    a = (l["x0"] - cx) + (l["bottom"] - cy)
                    if abs(a) / 2 ** 0.5 < 0.35 * (t["x1"] - t["x0"]) and l["x0"] - 2 < cx + 30 and l["x1"] + 2 > cx - 30 \
                            and l["top"] - 2 < cy and l["bottom"] + 2 > cy:
                        n_h += 1
                t["stripes_through"] = n_h
                if t["vfill"] == "pattern":
                    vf = "striped"
                elif t["vfill"] == "black" or t["vfill"].startswith("gray"):
                    vf = "solid"
                elif t["vfill"] == "white":
                    vf = "striped" if n_h >= 2 else "open"
                else:
                    vf = "?"
                t["fill_vector"] = vf
                t["fill"] = vf if vf == t["fill_pixels"] else "MISMATCH(%s/%s)" % (vf, t["fill_pixels"])
                t["cx"], t["cy"] = round(cx, 2), round(cy, 2)
                t["w"], t["h"] = round(t["x1"] - t["x0"], 3), round(t["bottom"] - t["top"], 3)
            ok(all(not t["fill"].startswith("MISMATCH") for t in tiles),
               "%s p%d: vector and pixel fill classifications agree for all %d glyphs" % (pdf, pno, len(tiles)))
            # numbers printed under tiles (bonus page 3)
            words = [w for w in page.extract_words() if w["text"] in ("1", "2", "3")]
            for w in words:
                wx, wy = (w["x0"] + w["x1"]) / 2, w["top"]
                under = [t for t in tiles if abs(t["cx"] - wx) < 6 and 0 < wy - t["cy"] < 30]
                if under:
                    t = min(under, key=lambda t: wy - t["cy"])
                    t.setdefault("numbers", []).append(int(w["text"]))
            boards, used = lattice_boards(tiles)
            loose = [i for i in range(len(tiles)) if i not in used]
            # loose groups: same row band (within 35 pt) and same page half
            groups = []
            for i in sorted(loose, key=lambda i: (tiles[i]["cy"], tiles[i]["cx"])):
                t = tiles[i]
                half = t["cx"] >= 306
                for g in groups:
                    if g["half"] == half and g["small"] == (t["w"] < 15) and abs(g["cy"] - t["cy"]) < (15 if t["w"] < 15 else 35):
                        g["members"].append(i)
                        break
                else:
                    groups.append(dict(half=half, cy=t["cy"], small=t["w"] < 15, members=[i]))
            def tdesc(t):
                d = dict(shape=t["shape"], fill=t["fill"], cx=t["cx"], cy=t["cy"], w=t["w"], h=t["h"],
                         vfill=t["vfill"], pix=t["pix"], stripes=t["stripes_through"])
                if "numbers" in t:
                    d["numbers"] = t["numbers"]
                if t["path"] is not None:
                    d["path"] = t["path"]
                return d
            pg = dict(page=pno,
                      boards=[dict(pitch=round(b["pitch"], 2),
                                   cells=[[tdesc(tiles[k]) for k in row] for row in b["grid"]]) for b in boards],
                      groups=[[tdesc(tiles[k]) for k in sorted(g["members"], key=lambda k: tiles[k]["cx"])]
                              for g in groups])
            # gray cell frames (base: line width .65 gray!70; bonus: gray .8 frames) for size claims
            frames = [r for r in page.rects if not r["fill"] and r["stroke"] and not is_black(r["stroking_color"])]
            pg["frame_sizes_pt"] = sorted({(round(r["x1"] - r["x0"], 1), round(r["bottom"] - r["top"], 1)) for r in frames})
            data[pdf].append(pg)
            print("  p%d: %d glyphs, %d boards (pitches %s), %d loose groups, frames %s" % (
                pno, len(tiles), len(boards), [round(b["pitch"], 1) for b in boards], len(groups), pg["frame_sizes_pt"]))
            for g in pg["groups"]:
                print("     group:", ", ".join("%s %s%s" % (t["fill"], t["shape"], (" #" + "".join(map(str, t["numbers"]))) if "numbers" in t else "") for t in g))
            for b in pg["boards"]:
                print("     board pitch %.1f:" % b["pitch"])
                for row in b["cells"]:
                    print("        " + " | ".join("%-7s %-8s%s" % (t["fill"], t["shape"], (" #" + "".join(map(str, t["numbers"]))) if "numbers" in t else "") for t in row))
    (HERE / "extracted.json").write_text(json.dumps(data, indent=1))
    for f in RENDER.glob("*.pgm"):
        f.unlink()
    RENDER.rmdir()
    finish()


if __name__ == "__main__":
    main()
