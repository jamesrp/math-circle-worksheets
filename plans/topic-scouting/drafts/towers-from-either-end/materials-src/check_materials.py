"""Check the delivered materials.pdf for 'Towers from either end'.

Usage:  python3 src/check_materials.py   (exit status 0 = every check passed)

Measures the PDF itself, not the TeX source, in two independent ways:
  1. the drawn paths (PyMuPDF get_drawings): every strip's cut outline, each
     slot square, each column's fill colour, and every slot number's position;
  2. a 300 dpi rendering: dark-line positions along scanlines through each
     strip, converted to millimetres.
Tolerance 0.5 mm throughout.

It also reads the three final student PDFs, finds every row a problem asks
children to build (drawn rows of slots, and rows written as lists of heights),
and confirms the materials supply exactly those strip lengths, plain and
colored, with the pages' slot colours and slot numbering; that plain and
colored strips never share a page; that every mark is 12 mm or more from the
paper edge; and that the only words on the sheets are labels (so no heights,
totals or other answers appear).
"""
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
import pymupdf

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
MAT = RUN / "materials.pdf"
STUDENT = RUN
PACKETS = {"K-1": "k-1.pdf", "2-3": "grades-2-3.pdf", "4-5": "grades-4-5.pdf"}

PT = 25.4 / 72          # mm per PDF point
TOL = 0.5               # mm
SLOT, BAND = 25.0, 9.0  # outline: square slots about 25 mm; number band below
CUBE = 20.0             # 2 cm snap cubes
EDGE = 12.0             # minimum distance from every paper edge, mm
WHITE = (1.0, 1.0, 1.0)

HEADER = "Week NN / Towers from either end / Materials"
FOOTER = "Bellingham Math Circle / Week NN / NN-M-v1"
TITLES = {1: "Strips of slots", 2: "Strips of slots / Grades 4–5", 3: "Colored strips"}
SCALE_LABEL = "100 mm scale check"
EXPECT_PAGES = {1: "portrait", 2: "portrait", 3: "landscape"}

failures = []
lines_out = []


def check(ok, msg):
    lines_out.append(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        failures.append(msg)


def rng(vals):
    return f"{min(vals):.2f} to {max(vals):.2f}" if vals else "(none found)"


def mm(v):
    return v * PT


def near(a, b, tol=TOL):
    return abs(a - b) <= tol


def rgb(c):
    return tuple(round(v, 3) for v in c) if c else None


# ---------------------------------------------------------------- student pages
def student_slot_colours():
    """RGB of the red and blue slot fills used on the student pages."""
    found = set()
    for f in PACKETS.values():
        for pg in pymupdf.open(STUDENT / f):
            for d in pg.get_drawings():
                c = rgb(d.get("fill"))
                # slot cells are stroked and filled; cubes are grey (equal channels)
                if d["type"] == "fs" and c and len(set(c)) > 1:
                    found.add(c)
    return found


def student_rows():
    """Every row a problem asks children to build, as (band, page, n, tinted)."""
    rows = []
    for band, f in PACKETS.items():
        for pno, pg in enumerate(pymupdf.open(STUDENT / f), 1):
            cells = []
            for d in pg.get_drawings():
                c = rgb(d.get("fill"))
                if d["type"] != "fs" or c is None:
                    continue
                if c == rgb(WHITE) or len(set(c)) > 1:     # white, red or blue slot cell
                    r = d["rect"]
                    cells.append((round(r.y0, 1), round(r.height, 1), r.x0, r.x1, c))
            cells.sort()
            runs = []
            for cell in cells:
                y, hgt, x0, x1, c = cell
                if runs and runs[-1][-1][0] == y and runs[-1][-1][1] == hgt and abs(runs[-1][-1][3] - x0) < 0.5:
                    runs[-1].append(cell)
                else:
                    runs.append([cell])
            for run in runs:
                cols = [c for *_, c in run]
                tinted = any(c != rgb(WHITE) for c in cols)
                rows.append((band, pno, len(run), tinted, cols))
            # rows written as lists of heights (4-5 Problems 1, 2, 11 and the intros)
            for m in re.finditer(r"\b\d(?:,\s*\d){2,}\b", pg.get_text()):
                n = len(re.findall(r"\d", m.group()))
                rows.append((band, pno, n, False, None))
    return rows


# ---------------------------------------------------------------- materials
def strips_on(pg):
    """Group the page's drawn paths into strips."""
    draws = pg.get_drawings()
    outlines, squares, fills = [], [], []
    for d in draws:
        r = d["rect"]
        w, h = mm(r.width), mm(r.height)
        if d["type"] == "f" and d.get("fill") is not None:
            fills.append((r, rgb(d["fill"])))
        elif d["type"] == "s":
            if near(w, SLOT, 1.5) and near(h, SLOT, 1.5):
                squares.append(r)
            elif near(h, SLOT + BAND, 1.5) and w > SLOT * 2.5:
                outlines.append((r, d.get("width")))
    strips = []
    for o, lw in outlines:
        inside = lambda r: (r.x0 >= o.x0 - 1 and r.x1 <= o.x1 + 1 and r.y0 >= o.y0 - 1 and r.y1 <= o.y1 + 1)
        sq = sorted([r for r in squares if inside(r)], key=lambda r: r.x0)
        fl = sorted([(r, c) for r, c in fills if inside(r)], key=lambda t: t[0].x0)
        strips.append({"outline": o, "lw": lw, "squares": sq, "fills": fl})
    strips.sort(key=lambda s: (round(s["outline"].y0), s["outline"].x0))
    return strips


def render_lines(pix, y_px=None, x_px=None, lo=0, hi=None):
    """Centres (in px) of dark runs along a row (y_px) or column (x_px)."""
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    line = a[y_px, :, :] if y_px is not None else a[:, x_px, :]
    dark = line.max(axis=1) < 90
    hi = hi or len(dark)
    centres, start = [], None
    for i in range(lo, hi):
        if dark[i] and start is None:
            start = i
        if not dark[i] and start is not None:
            centres.append((start + i - 1) / 2)
            start = None
    return centres


def main():
    doc = pymupdf.open(MAT)
    check(doc.page_count == 3, f"materials.pdf has {doc.page_count} pages (expected 3)")
    student_red_blue = student_slot_colours()
    check(len(student_red_blue) == 2, f"student pages use two slot tints: {sorted(student_red_blue)}")
    red = max(student_red_blue, key=lambda c: c[0])
    blue = min(student_red_blue, key=lambda c: c[0])

    supplied = {}          # (n, tinted) -> list of pages
    for pno, pg in enumerate(doc, 1):
        W, H = mm(pg.rect.width), mm(pg.rect.height)
        orient = "portrait" if H > W else "landscape"
        check(near(min(W, H), 215.9, 0.2) and near(max(W, H), 279.4, 0.2) and orient == EXPECT_PAGES[pno],
              f"p{pno}: US Letter {orient} ({W:.1f} x {H:.1f} mm)")

        # ---- text: header, footer, title, labels only
        words = pg.get_text("words")
        text_lines = {}
        for x0, y0, x1, y1, wd, b, l, _ in words:
            text_lines.setdefault((b, l), []).append((x0, y0, x1, y1, wd))
        lines = []
        for k, ws in text_lines.items():
            ws.sort()
            lines.append((" ".join(w[4] for w in ws), min(w[0] for w in ws), min(w[1] for w in ws),
                          max(w[2] for w in ws), max(w[3] for w in ws)))
        texts = [t for t, *_ in lines]
        check(HEADER in texts, f"p{pno}: header '{HEADER}'")
        check(FOOTER in texts and str(pno) in texts, f"p{pno}: footer '{FOOTER}' with page number {pno}")
        check(TITLES[pno] in texts, f"p{pno}: object label '{TITLES[pno]}'")
        allowed = {HEADER, FOOTER, TITLES[pno], SCALE_LABEL} | {str(i) for i in range(1, 9)}
        extra = [t for t in texts if t not in allowed]
        check(not extra, f"p{pno}: no words beyond labels and slot numbers (extra: {extra})")

        # ---- every mark at least 12 mm from every edge
        worst = 1e9
        for d in pg.get_drawings():
            r = d["rect"]
            pad = (d.get("width") or 0) / 2
            worst = min(worst, mm(r.x0 - pad), mm(r.y0 - pad), W - mm(r.x1 + pad), H - mm(r.y1 + pad))
        for t, x0, y0, x1, y1 in lines:
            worst = min(worst, mm(x0), mm(y0), W - mm(x1), H - mm(y1))
        check(worst >= EDGE, f"p{pno}: nearest mark to a paper edge is {worst:.1f} mm (>= {EDGE} mm)")

        # ---- scale bar
        lab = [l for l in lines if l[0] == SCALE_LABEL]
        bar = None
        if lab:
            ly = (lab[0][2] + lab[0][4]) / 2
            for d in pg.get_drawings():
                for it in d["items"]:
                    if it[0] == "l" and abs(it[1].y - it[2].y) < 0.1 and abs(it[1].y - ly) < 3 / PT \
                            and it[2].x <= lab[0][1] + 1:
                        L = mm(abs(it[2].x - it[1].x))
                        if L > 50:
                            bar = L
        check(bar is not None and near(bar, 100), f"p{pno}: scale bar measures {bar if bar is None else round(bar, 2)} mm (100)")

        # ---- strips from drawn paths
        strips = strips_on(pg)
        pix = pg.get_pixmap(dpi=300)
        px_mm = 25.4 / 300
        for s in strips:
            o = s["outline"]
            n = len(s["squares"])
            ow, oh = mm(o.width), mm(o.height)
            tag = f"p{pno} strip of {n} at ({mm(o.x0):.1f}, {mm(o.y0):.1f}) mm"
            check(n >= 3 and near(ow, n * SLOT) and near(oh, SLOT + BAND),
                  f"{tag}: cut outline {ow:.2f} x {oh:.2f} mm (expected {n * SLOT:.0f} x {SLOT + BAND:.0f})")
            sizes = [(mm(r.width), mm(r.height)) for r in s["squares"]]
            check(n >= 3 and all(near(w, SLOT) and near(h, SLOT) for w, h in sizes),
                  f"{tag}: slot squares {rng([v for wh in sizes for v in wh])} mm (25)")
            pitch = [mm(b.x0 - a.x0) for a, b in zip(s["squares"], s["squares"][1:])]
            check(n >= 3 and all(near(p, SLOT) for p in pitch) and near(mm(s["squares"][0].x0 - o.x0), 0)
                  and all(near(mm(r.y0 - o.y0), 0) for r in s["squares"]),
                  f"{tag}: slots contiguous from the left end, pitch {rng(pitch)} mm")
            band = oh - SLOT
            check(near(band, BAND), f"{tag}: number band {band:.2f} mm below the squares")
            check(SLOT - CUBE >= 4, f"{tag}: a 2 cm cube leaves {(SLOT - CUBE) / 2:.1f} mm each side in a slot")
            cols = [c for r, c in s["fills"]]
            check(len(cols) == n and all(near(mm(r.width), SLOT) and near(mm(r.height), SLOT + BAND) for r, _ in s["fills"]),
                  f"{tag}: {len(cols)} column fills of 25 x 34 mm")
            tinted = any(c != rgb(WHITE) for c in cols)
            if tinted:
                want = [red if i % 2 == 0 else blue for i in range(n)]
                check(cols == want, f"{tag}: slot 1 red, then alternating blue/red, in the pages' exact RGB")
            else:
                check(all(c == rgb(WHITE) for c in cols), f"{tag}: plain (no tint)")
            # slot numbers 1..n, each centred in its own slot's band
            ok = True
            for i, r in enumerate(s["squares"]):
                band_rect = pymupdf.Rect(r.x0, r.y1, r.x1, o.y1)
                inside = [w for w in words if pymupdf.Rect(w[:4]).intersects(band_rect)]
                if [w[4] for w in inside] != [str(i + 1)]:
                    ok = False
                    continue
                wx = mm((inside[0][0] + inside[0][2]) / 2 - (r.x0 + r.x1) / 2)
                if abs(wx) > 1.5 or pymupdf.Rect(inside[0][:4]).intersects(r + (1, 1, -1, -1)):
                    ok = False
            check(ok, f"{tag}: numbered 1 to {n} from the left, each number centred in the band, clear of the square")
            # rendered measurement: vertical lines along a scanline through the squares
            y_px = int(round((mm(o.y0) + SLOT / 2) / px_mm))
            lo = int(mm(o.x0) / px_mm) - 10
            hi = int(mm(o.x1) / px_mm) + 10
            xs = render_lines(pix, y_px=y_px, lo=lo, hi=hi)
            gaps = [(b - a) * px_mm for a, b in zip(xs, xs[1:])]
            check(len(xs) == n + 1 and all(near(g, SLOT) for g in gaps),
                  f"{tag}: rendered 300 dpi, {len(xs)} slot lines, spacing {rng(gaps)} mm")
            x_px = int(round((mm(s["squares"][0].x0) + 4) / px_mm))
            ys = render_lines(pix, x_px=x_px, lo=int(mm(o.y0) / px_mm) - 10, hi=int(mm(o.y1) / px_mm) + 10)
            vg = [(b - a) * px_mm for a, b in zip(ys, ys[1:])]
            check(len(ys) == 3 and near(vg[0], SLOT) and near(vg[1], BAND),
                  f"{tag}: rendered 300 dpi, square then band {[round(v, 2) for v in vg]} mm tall")
            supplied.setdefault((n, tinted), []).append(pno)
        kinds = {t for (n, t) in supplied for p in supplied[(n, t)] if p == pno}
        check(len(kinds) == 1, f"p{pno}: plain and colored strips never share a page ({'colored' if True in kinds else 'plain'})")
        # strips do not overlap each other
        rects = [s["outline"] for s in strips]
        overl = any(a.intersects(b) for i, a in enumerate(rects) for b in rects[i + 1:])
        check(not overl, f"p{pno}: {len(strips)} strips, none overlapping")

    # ---------------------------------------------------- against the student pages
    rows = student_rows()
    need = {}
    for band, pno, n, tinted, cols in rows:
        need.setdefault((n, tinted), set()).add(f"{band} p{pno}")
        if tinted:
            want = [red if i % 2 == 0 else blue for i in range(n)]
            check(cols == want, f"student {band} p{pno}: colored row of {n} starts red and alternates")
    need = {k: v for k, v in need.items() if k[0] >= 3}
    for (n, t), where in sorted(need.items()):
        kind = "colored" if t else "plain"
        check((n, t) in supplied, f"needed: {kind} strip of {n} ({', '.join(sorted(where))}) -> materials p{supplied.get((n, t))}")
    for (n, t), pages in sorted(supplied.items()):
        kind = "colored" if t else "plain"
        check((n, t) in need, f"supplied: {kind} strip of {n} on p{pages} is used by a student page")
    # tint must not reach a page given out before the plain-strip problems
    check(all(not t for (n, t), pages in supplied.items() if 1 in pages or 2 in pages)
          and all(t for (n, t), pages in supplied.items() if 3 in pages),
          "pages 1-2 are plain only; page 3 is colored only")
    # names: the pages call them strips of slots / colored strips
    alltext = " ".join(pg.get_text() for f in PACKETS.values() for pg in pymupdf.open(STUDENT / f)).replace("\n", " ")
    check("strip of slots" in alltext and "colored strip" in alltext,
          "student pages use the names 'strip of slots' and 'colored strip'")

    print("\n".join(lines_out))
    print()
    print("supplied:", {f"{'colored' if t else 'plain'} {n}": p for (n, t), p in sorted(supplied.items())})
    print("FAILED:" if failures else "ALL CHECKS PASSED", len(failures) if failures else len(lines_out))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
