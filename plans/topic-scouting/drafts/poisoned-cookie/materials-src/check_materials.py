"""Check the delivered Poisoned cookie materials PDF (not its source).

1. Vector check: reads every drawn path and text span of ../materials.pdf with
   PyMuPDF, finds the boards (clusters of square cells), the bite card and the
   scale bar, and measures them in millimetres.  Every drawing on a page must
   be one of these or the header/footer rules, so nothing else (an X, a
   highlighted cell, a stray note) can be printed.
2. Raster check: renders each page at 300 dpi and measures grid-line spacing,
   card sides and the scale bar from the pixels.
3. Problem match: reads the three final student PDFs the same way, lists every
   board pictured in a problem and every "R by C board" named in the text, and
   confirms each can be played at 25 mm with that band's packet plus these
   materials, with rectangles available in exactly their shape, and that the
   materials hold nothing a band's own packet already prints at 25 mm.
4. Card reach: on each page, a 150 mm card set on any non-poison cell of a
   board (corner up to 3 mm off) must not reach another board.
Run:  python3 -I check_materials.py   (exit status 1 on any failure)
"""
import os
import re
import sys

import pymupdf as fitz

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(RUN, "..", "..", ".."))
MATERIALS = os.path.join(RUN, "materials.pdf")
STUDENT = RUN
OUTLINE = os.path.join(RUN, "..", "..", "poisoned-cookie.md")
PACKETS = {"K-1": "k-1.pdf", "2-3": "grades-2-3.pdf", "4-5": "grades-4-5.pdf"}

MM = 25.4 / 72.0
TOL = 0.5            # mm, required accuracy of key dimensions
CELL = 25.0
CARD = 150.0
SLACK = 3.0
MARGIN = 12.0
DPI = 300

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    return cond


def mm(v):
    return v * MM


# ---------------------------------------------------------------- vector parsing
class Item:
    def __init__(self, d):
        r = d["rect"]
        self.x0, self.y0, self.x1, self.y1 = mm(r.x0), mm(r.y0), mm(r.x1), mm(r.y1)
        self.kinds = [it[0] for it in d["items"]]
        self.stroke = d.get("color")
        self.fill = d.get("fill")
        self.width = mm(d["width"]) if d.get("width") else 0.0
        self.type = d["type"]
        self.used = False

    @property
    def w(self):
        return self.x1 - self.x0

    @property
    def h(self):
        return self.y1 - self.y0

    @property
    def cx(self):
        return (self.x0 + self.x1) / 2

    @property
    def cy(self):
        return (self.y0 + self.y1) / 2

    def is_circle(self):
        return self.kinds and all(k == "c" for k in self.kinds) and abs(self.w - self.h) < 0.2

    def is_rect(self):
        return self.kinds in (["l", "l", "l", "l"], ["re"], ["l", "l", "l"]) and self.w > 0.5 and self.h > 0.5

    def is_hline(self):
        return self.kinds == ["l"] and self.h < 0.01

    def is_vline(self):
        return self.kinds == ["l"] and self.w < 0.01


def page_items(page):
    return [Item(d) for d in page.get_drawings()]


def gray(c):
    return None if c is None else round(sum(c) / len(c), 2)


def find_boards(items):
    """Clusters of stroked square cells; each board records shape and marks."""
    cells = []
    seen = set()
    for it in items:
        if it.type == "s" and it.is_rect() and abs(it.w - it.h) < 0.2 and 4 < it.w < 40:
            key = (round(it.x0, 1), round(it.y0, 1), round(it.w, 1))
            if key in seen:          # a recording grid's corner is drawn twice
                it.used = True
                continue
            seen.add(key)
            cells.append(it)
    parent = list(range(len(cells)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i, a in enumerate(cells):
        for j in range(i + 1, len(cells)):
            b = cells[j]
            if abs(a.w - b.w) > 0.2:
                continue
            s = a.w
            dx, dy = abs(a.x0 - b.x0), abs(a.y0 - b.y0)
            if (abs(dx - s) < 0.2 and dy < 0.2) or (abs(dy - s) < 0.2 and dx < 0.2):
                parent[find(i)] = find(j)
    groups = {}
    for i, c in enumerate(cells):
        groups.setdefault(find(i), []).append(c)
    circles = [it for it in items if it.is_circle()]
    boards = []
    for cs in groups.values():
        s = sum(c.w for c in cs) / len(cs)
        minx = min(c.x0 for c in cs)
        maxy = max(c.y1 for c in cs)
        grid = {}
        for c in cs:
            col = round((c.x0 - minx) / s)
            row = round((maxy - c.y1) / s)          # 0 = bottom row
            grid[(row, col)] = c
        nrows = max(r for r, _ in grid) + 1
        rows = tuple(sum(1 for (r, _) in grid if r == k) for k in range(nrows))
        staircase = all(all((k, c) in grid for c in range(rows[k])) for k in range(nrows)) and \
            all(rows[k] >= rows[k + 1] for k in range(nrows - 1))
        marks = {}
        for ci in circles:
            for (r, col), c in grid.items():
                if c.x0 < ci.cx < c.x1 and c.y0 < ci.cy < c.y1:
                    marks.setdefault((r, col), []).append(ci)
        boards.append(dict(cells=cs, grid=grid, size=s, rows=rows, staircase=staircase, marks=marks,
                           x0=minx, x1=max(c.x1 for c in cs), y0=min(c.y0 for c in cs), y1=maxy,
                           every_cell_marked=all(len(marks.get(k, [])) == 1 for k in grid)))
    return boards


def is_play_board(b):
    """A board children play on or mark: a cookie or poison circle in every cell,
    a filled poison disc in the bottom-left cell and outline cookies elsewhere."""
    if not (b["staircase"] and b["every_cell_marked"]):
        return False
    poison = b["marks"][(0, 0)][0]
    others = [m[0] for k, m in b["marks"].items() if k != (0, 0)]
    return poison.fill is not None and all(o.fill is None and o.type == "s" for o in others)


def is_rectangle(rows):
    return len(set(rows)) == 1


def shape_name(rows):
    if is_rectangle(rows):
        return f"{len(rows)} by {rows[0]}"
    return "(" + ",".join(str(x) for x in rows) + ")"


def spans(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["text"].strip():
                    x0, y0, x1, y1 = s["bbox"]
                    out.append(dict(text=s["text"].strip(), x0=mm(x0), y0=mm(y0), x1=mm(x1), y1=mm(y1),
                                    size=s["size"]))
    return out


# ---------------------------------------------------------------- 1. materials, vector
def check_materials_vector(doc):
    report = []
    all_boards = []
    for pno, page in enumerate(doc, start=1):
        W, H = mm(page.rect.width), mm(page.rect.height)
        check(abs(min(W, H) - 215.9) < 0.3 and abs(max(W, H) - 279.4) < 0.3,
              f"page {pno}: not US Letter ({W:.1f} x {H:.1f} mm)")
        items = page_items(page)
        texts = spans(page)

        # header and footer
        head = [t for t in texts if t["text"] == "Week NN / Poisoned cookie / Materials"]
        foot = [t for t in texts if t["text"] == "Bellingham Math Circle / Week NN / NN-M-v1"]
        num = [t for t in texts if t["text"] == str(pno) and t["y0"] > H - 30]
        check(len(head) == 1 and head[0]["y0"] < 25, f"page {pno}: header missing or misplaced")
        check(len(foot) == 1 and foot[0]["y0"] > H - 30, f"page {pno}: footer missing or misplaced")
        check(len(num) == 1, f"page {pno}: page number missing")
        for it in items:
            if (it.is_hline() and it.w > 150 and gray(it.stroke) == 0.5
                    and (it.y0 < 25 or it.y0 > H - 25)):
                it.used = True      # header / footer rules

        # boards
        boards = find_boards(items)
        for b in boards:
            for c in b["cells"]:
                c.used = True
            for ms in b["marks"].values():
                for m in ms:
                    m.used = True
            name = f"{len(b['rows'])} by {b['rows'][0]}"
            ok = check(is_play_board(b) and is_rectangle(b["rows"]),
                       f"page {pno}: board {shape_name(b['rows'])} is not a full rectangle with "
                       f"one poison disc bottom-left and a cookie circle in every other cell")
            sizes = [c.w for c in b["cells"]] + [c.h for c in b["cells"]]
            check(all(abs(s - CELL) <= TOL for s in sizes),
                  f"page {pno}: {name} cells {min(sizes):.2f}-{max(sizes):.2f} mm, want {CELL}")
            # equal scaling on both axes: every cell square to 0.1 mm
            check(all(abs(c.w - c.h) < 0.1 for c in b["cells"]), f"page {pno}: {name} cells not square")
            # cookie marks sized as on the student boards (radius 0.34 cell)
            radii = [m[0].w / 2 for m in b["marks"].values()]
            check(all(abs(r - 0.34 * CELL) < 0.3 for r in radii), f"page {pno}: {name} circle radius off")
            # label directly above, naming rows by columns
            lab = [t for t in texts if t["text"].endswith("board") and abs(t["x0"] - b["x0"]) < 1.0
                   and 0 < b["y0"] - t["y1"] < 6]
            check(len(lab) == 1 and lab[0]["text"] == f"{name} board",
                  f"page {pno}: board {name} label {[t['text'] for t in lab]}")
            # nothing else inside the board: no text, no extra paths
            inside_text = [t["text"] for t in texts if t["x0"] < b["x1"] and t["x1"] > b["x0"]
                           and t["y0"] < b["y1"] and t["y1"] > b["y0"]]
            check(not inside_text, f"page {pno}: text inside {name}: {inside_text}")
            for it in items:
                if not it.used and it.x0 < b["x1"] and it.x1 > b["x0"] and it.y0 < b["y1"] and it.y1 > b["y0"]:
                    check(False, f"page {pno}: extra mark inside {name}: {it.kinds} at {it.x0:.1f},{it.y0:.1f}")
            if ok:
                cw = sum(c.w for c in b["cells"]) / len(b["cells"])
                report.append(f"page {pno}: {name} board, {len(b['cells'])} cells, cell {cw:.2f} mm, "
                              f"outer {b['x1'] - b['x0']:.2f} x {b['y1'] - b['y0']:.2f} mm, "
                              f"label '{lab[0]['text'] if lab else '?'}'")
            all_boards.append((pno, name, b))

        # bite card
        cards = [it for it in items if it.type == "s" and it.is_rect() and abs(it.w - CARD) < 5 and abs(it.h - CARD) < 5]
        if cards:
            c = cards[0]
            c.used = True
            check(abs(c.w - CARD) <= TOL and abs(c.h - CARD) <= TOL,
                  f"page {pno}: bite card {c.w:.2f} x {c.h:.2f} mm, want {CARD}")
            fills = [it for it in items if it.type == "f" and it.is_rect()
                     and it.x0 >= c.x0 - 0.05 and it.x1 <= c.x1 + 0.05 and it.y0 >= c.y0 - 0.05 and it.y1 <= c.y1 + 0.05]
            left = [f_ for f_ in fills if abs(f_.x0 - c.x0) < 0.05 and abs(f_.h - c.h) < 0.05]
            bottom = [f_ for f_ in fills if abs(f_.y1 - c.y1) < 0.05 and abs(f_.w - c.w) < 0.05]
            check(len(left) == 1 and len(bottom) == 1 and len(fills) == 2,
                  f"page {pno}: bite card should carry exactly a thick L on its left and bottom edges")
            for f_ in fills:
                f_.used = True
            lw = left[0].w if left else 0
            bw = bottom[0].h if bottom else 0
            check(lw >= 1.5 and bw >= 1.5, f"page {pno}: thick L too thin ({lw:.2f}, {bw:.2f} mm)")
            labs = [t["text"] for t in texts if c.x0 < t["x0"] and t["x1"] < c.x1 and c.y0 < t["y0"] and t["y1"] < c.y1]
            check(labs == ["Bite card"], f"page {pno}: text on the bite card {labs}")
            for it in items:
                if not it.used and it.x0 < c.x1 and it.x1 > c.x0 and it.y0 < c.y1 and it.y1 > c.y0:
                    check(False, f"page {pno}: extra mark on the bite card")
            for _, name, b in [x for x in all_boards if x[0] == pno]:
                check(b["y0"] > c.y1 + 5 or b["y1"] < c.y0 - 5,
                      f"page {pno}: {name} board too close to the card's cut line")
            report.append(f"page {pno}: bite card {c.w:.2f} x {c.h:.2f} mm, thick L {lw:.2f} mm (left) and "
                          f"{bw:.2f} mm (bottom), label 'Bite card'")

        # scale bar: one 100 mm line with end ticks
        bars = [it for it in items if not it.used and it.is_hline() and 90 < it.w < 110]
        for bar in bars:
            bar.used = True
            ticks = [it for it in items if it.is_vline() and not it.used and abs(it.cy - bar.y0) < 0.1
                     and (abs(it.x0 - bar.x0) < 0.05 or abs(it.x0 - bar.x1) < 0.05)]
            for t in ticks:
                t.used = True
            check(abs(bar.w - 100) <= TOL and len(ticks) == 2, f"page {pno}: scale bar {bar.w:.2f} mm")
            labs = [t["text"] for t in texts if abs((t["y0"] + t["y1"]) / 2 - bar.y0) < 3 and t["x0"] > bar.x1]
            check(labs == ["100 mm"], f"page {pno}: scale bar label {labs}")
            report.append(f"page {pno}: scale bar {bar.w:.2f} mm")

        # every drawing accounted for
        for it in items:
            check(it.used, f"page {pno}: unexplained drawing {it.kinds} at ({it.x0:.1f}, {it.y0:.1f}) mm")

        # margins (paths include half their line width; text by its box)
        for it in items:
            hw = it.width / 2
            check(it.x0 - hw >= MARGIN and it.y0 - hw >= MARGIN and it.x1 + hw <= W - MARGIN
                  and it.y1 + hw <= H - MARGIN, f"page {pno}: drawing within {MARGIN} mm of an edge")
        for t in texts:
            check(t["x0"] >= MARGIN and t["y0"] >= MARGIN and t["x1"] <= W - MARGIN and t["y1"] <= H - MARGIN,
                  f"page {pno}: text '{t['text']}' within {MARGIN} mm of an edge")
        edge = min([it.x0 - it.width / 2 for it in items] + [it.y0 - it.width / 2 for it in items]
                   + [W - it.x1 - it.width / 2 for it in items] + [H - it.y1 - it.width / 2 for it in items]
                   + [t["x0"] for t in texts] + [t["y0"] for t in texts]
                   + [W - t["x1"] for t in texts] + [H - t["y1"] for t in texts])
        report.append(f"page {pno}: {'landscape' if W > H else 'portrait'}, closest ink to an edge {edge:.1f} mm")

        # text on the page: labels only
        allowed = {"Week NN / Poisoned cookie / Materials", "Bellingham Math Circle / Week NN / NN-M-v1",
                   str(pno), "Bite card", "100 mm"}
        for t in texts:
            check(t["text"] in allowed or re.fullmatch(r"\d by \d board", t["text"]),
                  f"page {pno}: unexpected text '{t['text']}'")
    return report, all_boards


# ---------------------------------------------------------------- 2. raster
def runs(line, thresh=170):
    out, start = [], None
    for i, v in enumerate(line):
        if v < thresh and start is None:
            start = i
        elif v >= thresh and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(line) - 1))
    return out


def check_raster(doc, all_boards):
    report = []
    px = 25.4 / DPI
    for pno, page in enumerate(doc, start=1):
        pix = page.get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
        w, h, data = pix.width, pix.height, pix.samples

        def row(yp):
            return [data[yp * w + x] for x in range(w)]

        def col(xp):
            return [data[y * w + xp] for y in range(h)]

        for p2, name, b in all_boards:
            if p2 != pno:
                continue
            nrows, ncols = len(b["rows"]), b["rows"][0]
            # horizontal scan 2 mm below the board's top edge, clear of the cookie circles
            yp = round((b["y0"] + 2.0) / px)
            xs = [r for r in runs(row(yp)) if b["x0"] - 1 < r[0] * px < b["x1"] + 1]
            centres = [(a + c) / 2 * px for a, c in xs]
            gaps = [centres[i + 1] - centres[i] for i in range(len(centres) - 1)]
            # vertical scan 2 mm right of the left edge
            xp = round((b["x0"] + 2.0) / px)
            ys = [r for r in runs(col(xp)) if b["y0"] - 1 < r[0] * px < b["y1"] + 1]
            vcentres = [(a + c) / 2 * px for a, c in ys]
            vgaps = [vcentres[i + 1] - vcentres[i] for i in range(len(vcentres) - 1)]
            ok = check(len(gaps) == ncols and len(vgaps) == nrows,
                       f"raster page {pno}: {name} grid lines found {len(gaps) + 1} x {len(vgaps) + 1}")
            if ok:
                check(all(abs(g - CELL) <= TOL for g in gaps + vgaps),
                      f"raster page {pno}: {name} cell spacing {min(gaps + vgaps):.2f}-{max(gaps + vgaps):.2f} mm")
                report.append(f"raster page {pno}: {name} board, column spacing {min(gaps):.2f}-{max(gaps):.2f} mm, "
                              f"row spacing {min(vgaps):.2f}-{max(vgaps):.2f} mm, outer "
                              f"{centres[-1] - centres[0]:.2f} x {vcentres[-1] - vcentres[0]:.2f} mm")

        if pno == 1:
            # bite card: the scan 20 mm below the card's centre meets the thick left edge and the thin right edge
            cards = [it for it in page_items(page) if it.type == "s" and it.is_rect() and abs(it.w - CARD) < 5]
            c = cards[0]
            yp = round((c.cy + 20) / px)
            xs = [r for r in runs(row(yp)) if c.x0 - 2 < r[0] * px < c.x1 + 2]
            xp = round((c.cx + 20) / px)
            ys = [r for r in runs(col(xp)) if c.y0 - 2 < r[0] * px < c.y1 + 2]
            ok = check(len(xs) == 2 and len(ys) == 2, f"raster page 1: card edges found {len(xs)}, {len(ys)}")
            if ok:
                thick_l = (xs[0][1] - xs[0][0] + 1) * px
                thick_b = (ys[1][1] - ys[1][0] + 1) * px
                width = (xs[1][1] + 1 - xs[0][0]) * px        # outer edge to outer edge
                height = (ys[1][1] + 1 - ys[0][0]) * px
                check(abs(width - CARD) <= TOL and abs(height - CARD) <= TOL,
                      f"raster page 1: card {width:.2f} x {height:.2f} mm")
                check(thick_l > 1.5 and thick_b > 1.5 and (xs[1][1] - xs[1][0] + 1) * px < 0.5
                      and (ys[0][1] - ys[0][0] + 1) * px < 0.5,
                      "raster page 1: card should be thick on the left and bottom, thin on the right and top")
                report.append(f"raster page 1: bite card {width:.2f} x {height:.2f} mm outer, thick L "
                              f"{thick_l:.2f} / {thick_b:.2f} mm")
        for it in page_items(page):
            if it.is_hline() and 90 < it.w < 110:
                yp = round(it.y0 / px)
                xs = [r for r in runs(row(yp)) if it.x0 - 2 < r[0] * px < it.x1 + 2]
                if check(len(xs) >= 1, f"raster page {pno}: scale bar not found"):
                    length = (xs[0][1] + 1 - xs[0][0]) * px - it.width
                    check(abs(length - 100) <= TOL, f"raster page {pno}: scale bar {length:.2f} mm")
                    report.append(f"raster page {pno}: scale bar {length:.2f} mm")
    return report


# ---------------------------------------------------------------- 3. problem match
def student_boards(path):
    """[(page, problem, rows, cell size)] for every board pictured in a problem,
    plus the 'R by C board' names in the text, by problem."""
    doc = fitz.open(path)
    found, named = [], []
    problem = None
    for pno, page in enumerate(doc, start=1):
        words = page.get_text("words")
        heads = []
        for i, w_ in enumerate(words[:-1]):
            if w_[4] == "Problem" and re.fullmatch(r"\d+:", words[i + 1][4]):
                heads.append((mm(w_[1]), int(words[i + 1][4][:-1])))
        heads.sort()
        text = page.get_text()
        for b in find_boards(page_items(page)):
            if not is_play_board(b):
                continue            # recording grids and answer boxes
            above = [n for y, n in heads if y < b["y0"]]
            prob = above[-1] if above else problem
            if prob is None:
                continue            # the rules picture above Problem 1
            found.append((pno, prob, b["rows"], b["size"]))
        # names in the text, assigned to the heading they follow
        flat = " ".join(w_[4] for w_ in words)
        cur = problem
        for tok in re.finditer(r"Problem (\d+):|(\d+) by (\d+) board", flat):
            if tok.group(1):
                cur = int(tok.group(1))
            else:
                named.append((pno, cur, int(tok.group(2)), int(tok.group(3))))
        if heads:
            problem = heads[-1][1]
    return found, named


def fits(rows, R, C):
    return len(rows) <= R and all(x <= C for x in rows)


def outline_boards():
    """The printed boards the outline promises: 'Printed boards of 25 mm squares
    at 100%: 2 by 3, 2 by 4, ... and 3 by 5, poison square marked ...'."""
    text = open(OUTLINE).read()
    m = re.search(r"Printed boards of 25 mm squares at 100%:(.*?), poison", text, re.S)
    return {(int(a), int(b)) for a, b in re.findall(r"(\d+) by (\d+)", m.group(1))}


def check_problem_match(mat_boards):
    """Starting rectangles (the outline's list) and boards named in a problem's text
    need a 25 mm board of exactly that shape; every other pictured board (a position
    in mid-game, such as (4,2) or a 2 by 2) is built with counters on part of a
    25 mm board that contains it, starting at the poison."""
    report = []
    mat = {}
    for pno, name, b in mat_boards:
        mat[(len(b["rows"]), b["rows"][0])] = pno
    starting = outline_boards()
    report.append(f"outline's printed boards: {', '.join(f'{r} by {c}' for r, c in sorted(starting))}")
    needed = set()
    for band, fname in PACKETS.items():
        found, named = student_boards(os.path.join(STUDENT, fname))
        own = {(len(r), r[0]): (p, prob) for p, prob, r, s in found if is_rectangle(r) and abs(s - CELL) <= TOL}
        avail = dict(((k, f"own packet page {v[0]}") for k, v in own.items()))
        if band != "K-1":
            for k, p in mat.items():
                avail.setdefault(k, f"materials page {p}")
        lines = []
        for p, prob, rows, s in found:
            if abs(s - CELL) <= TOL:
                lines.append(f"P{prob} {shape_name(rows)} at {s:.0f} mm on page {p} (played on the page)")
                continue
            if rows == (10,) * 10:
                lines.append(f"P{prob} 10 by 10 at {s:.0f} mm: explanation only; 250 mm cannot print at 25 mm "
                             f"on Letter, so not supplied")
                continue
            key = (len(rows), rows[0])
            if is_rectangle(rows) and key in starting:
                where = avail.get(key)
                check(where is not None, f"{band} P{prob}: no 25 mm {shape_name(rows)} board")
                if key not in own:
                    needed.add(key)
                lines.append(f"P{prob} {shape_name(rows)} drawn at {s:.0f} mm -> {shape_name(rows)} board, {where}")
            else:
                hosts = sorted((k for k in avail if fits(rows, *k)), key=lambda k: k[0] * k[1])
                check(bool(hosts), f"{band} P{prob}: no 25 mm board holds {shape_name(rows)}")
                if hosts:
                    k = hosts[0]
                    lines.append(f"P{prob} {shape_name(rows)} drawn at {s:.0f} mm -> built on the "
                                 f"{k[0]} by {k[1]} board, {avail[k]}")
        for p, prob, R, C in named:
            where = avail.get((R, C))
            check(where is not None, f"{band} P{prob}: names the {R} by {C} board, not printed at 25 mm")
            if (R, C) not in own:
                needed.add((R, C))
            lines.append(f"P{prob} text names '{R} by {C} board' -> {where}")
        report.append(f"{band}:")
        report += ["   " + l for l in lines]
    for k, p in sorted(mat.items()):
        check(k in needed, f"materials page {p}: {k[0]} by {k[1]} board is not needed by any band "
                           f"(already in a packet or unused)")
    check(needed <= set(mat), f"boards needed but missing: {sorted(needed - set(mat))}")
    report.append(f"needed 25 mm boards not in any band's own packet: "
                  f"{', '.join(f'{r} by {c}' for r, c in sorted(needed))}")
    report.append(f"materials boards: {', '.join(f'{r} by {c}' for r, c in sorted(mat))}")
    return report


# ---------------------------------------------------------------- 4. card reach
def check_card_reach(mat_boards):
    report = []
    by_page = {}
    for pno, name, b in mat_boards:
        by_page.setdefault(pno, []).append((name, b))
    for pno, bs in sorted(by_page.items()):
        worst = None
        for i, (na, a) in enumerate(bs):
            for (r, c), cell in a["grid"].items():
                if (r, c) == (0, 0):
                    continue
                left, bottom = cell.x0 - SLACK, cell.y1 + SLACK
                card = (left, bottom - CARD, left + CARD, bottom)
                for j, (nb, b) in enumerate(bs):
                    if i == j:
                        continue
                    for other in b["cells"]:
                        hit = other.x1 > card[0] and other.x0 < card[2] and other.y1 > card[1] and other.y0 < card[3]
                        check(not hit, f"page {pno}: a card on the {na} board reaches the {nb} board")
                    # clearance between the card and the other board's outline (axis-aligned gap)
                    dx = max(card[0] - b["x1"], b["x0"] - card[2], 0.0)
                    dy = max(card[1] - b["y1"], b["y0"] - card[3], 0.0)
                    clear = max(dx, dy)
                    worst = clear if worst is None else min(worst, clear)
        if len(bs) > 1 and worst is None:
            check(False, f"page {pno}: boards with no biteable cells")
        elif len(bs) > 1:
            report.append(f"page {pno}: {' and '.join(n for n, _ in bs)} on a falling diagonal; a 150 mm card "
                          f"with its corner 3 mm off still clears the other board by {worst:.1f} mm or more")
    return report


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else MATERIALS
    doc = fitz.open(path)
    print(f"{path}: {len(doc)} pages")
    vec, boards = check_materials_vector(doc)
    print("\n-- vector measurements")
    print("\n".join(vec))
    print("\n-- raster measurements at", DPI, "dpi")
    print("\n".join(check_raster(doc, boards)))
    print("\n-- boards against the problems")
    print("\n".join(check_problem_match(boards)))
    print("\n-- bite card reach")
    print("\n".join(check_card_reach(boards)))
    print()
    if failures:
        print("FAILED:")
        print("\n".join("  " + f_ for f_ in failures))
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
