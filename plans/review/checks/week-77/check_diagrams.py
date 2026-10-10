#!/usr/bin/env python3
"""Read the boards back from the delivered Week 77 student PDF and check them.

For every board it finds the vertex dots, names each dot by the nearest
single-letter label, and records which pairs of dots are joined by a solid or
a dashed segment.  It then compares that with the text of each problem
(which edges are already present, which are places for edges), the printed
sizes the guide relies on for tiles and yarn strips (6.2 cm square, 8.8 cm
diagonal, 5.8 cm joined-board edges, 8 cm fan) and equal x/y scaling.
Run: python3 check_diagrams.py   (writes check_diagrams.py.out beside itself)
"""
import itertools
import math
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PDF = REPO / "lowell-math-circle-year-2/week-77/week-77-students.pdf"
OUT = HERE / (Path(__file__).name + ".out")
LINES, FAILS = [], []
CM = 72 / 2.54


def log(*a):
    s = " ".join(str(x) for x in a)
    LINES.append(s)
    print(s)


def check(cond, msg):
    log(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


def page_geometry(page):
    segs, dots = [], []
    for d in page.get_drawings():
        dashed = d.get("dashes") not in (None, "[] 0")
        items = d["items"]
        if d.get("fill") == (0.0, 0.0, 0.0) and items and all(it[0] == "c" for it in items):
            r = d["rect"]
            dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
            continue
        if d.get("type") not in ("s", "fs") or d.get("width", 0) < 0.8:
            continue  # token outlines, answer lines and arrows are thinner/grey
        for it in items:
            if it[0] == "l":
                segs.append(((it[1].x, it[1].y), (it[2].x, it[2].y), dashed, d["width"]))
            elif it[0] == "re":
                r = it[1]
                c = [(r.x0, r.y0), (r.x1, r.y0), (r.x1, r.y1), (r.x0, r.y1)]
                for k in range(4):
                    segs.append((c[k], c[(k + 1) % 4], dashed, d["width"]))
    return segs, dots


def on_seg(p, a, b, tol=0.6):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2
    if t < -0.01 or t > 1.01:
        return False
    return math.hypot(p[0] - ax - t * dx, p[1] - ay - t * dy) < tol


def joined(p, q, segs):
    """Return 'solid'/'dashed'/None for the straight segment p-q: every sample
    point along it must lie on a drawn segment parallel to p-q."""
    styles = set()
    n = 60
    ux, uy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(ux, uy)
    for k in range(1, n):
        m = (p[0] + ux * k / n, p[1] + uy * k / n)
        st = []
        for a, b, dashed, _w in segs:
            vx, vy = b[0] - a[0], b[1] - a[1]
            parallel = abs(vx * uy - vy * ux) < 0.01 * L * math.hypot(vx, vy)
            if parallel and on_seg(m, a, b):
                st.append(dashed)
        if not st:
            return None
        # a solid stroke drawn over a dashed edge place reads as solid
        styles.add("solid" if False in st else "dashed")
    if styles == {"solid"}:
        return "solid"
    if styles == {"dashed"}:
        return "dashed"
    return "mixed"


def labelled(page, dots, letters):
    words = [w for w in page.get_text("words") if w[4] in letters]
    names = {}
    for dot in dots:
        best = min(words, key=lambda w: math.dist(dot, ((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)))
        dist = math.dist(dot, ((best[0] + best[2]) / 2, (best[1] + best[3]) / 2))
        names[best[4]] = (dot, dist)
    return names


# Stroke order matters for p2/p4: the dashed outline is drawn first and the
# solid present edges are stroked over it (1.5 pt black over 0.9 pt grey).


def board(page, letters, region):
    segs, dots = page_geometry(page)
    x0, y0, x1, y1 = region
    dots = [d for d in dots if x0 <= d[0] <= x1 and y0 <= d[1] <= y1]
    names = labelled(page, dots, letters)
    pos = {k: v[0] for k, v in names.items()}
    edges = {}
    for a, b in itertools.combinations(sorted(pos), 2):
        j = joined(pos[a], pos[b], segs)
        if j:
            edges[a + b] = j
    return pos, edges, {k: v[1] for k, v in names.items()}


def main():
    doc = pymupdf.open(PDF)
    log("PDF:", PDF.relative_to(REPO), "pages", doc.page_count)
    check(doc.page_count == 5, "student packet has 5 pages")
    for p in doc:
        check(abs(p.rect.width - 612) < 1 and abs(p.rect.height - 792) < 1, f"page {p.number+1} is US Letter")

    sq_present = {1: set(), 2: {"AB", "BC", "CD"}, 4: {"AB", "BC", "CD"}}
    for pn, solid in sq_present.items():
        page = doc[pn - 1]
        pos, edges, dist = board(page, {"A", "B", "C", "D"}, (0, 300 if pn == 1 else 0, 612, 792))
        log(f"p{pn} square dots {({k: (round(v[0], 1), round(v[1], 1)) for k, v in pos.items()})} edges {edges}")
        check(set(pos) == {"A", "B", "C", "D"} and max(dist.values()) < 16, f"p{pn}: four dots labelled A-D next to their dots")
        want = {e: ("solid" if e in solid else "dashed") for e in ["AB", "BC", "CD", "AD", "AC"]}
        check(edges == want, f"p{pn}: present edges {sorted(solid) or 'none'} solid, the rest dashed; no BD")
        sides = [math.dist(pos[a], pos[b]) / CM for a, b in ["AB", "BC", "CD", "DA"]]
        check(all(abs(s - 6.2) < 0.02 for s in sides), f"p{pn}: square sides {[round(s, 3) for s in sides]} cm (6.2)")
        check(abs(math.dist(pos["A"], pos["C"]) / CM - 6.2 * math.sqrt(2)) < 0.03, f"p{pn}: diagonal AC {math.dist(pos['A'], pos['C'])/CM:.2f} cm")
        check(pos["A"][1] < pos["D"][1] and pos["A"][0] < pos["B"][0], f"p{pn}: A top-left, B top-right, C bottom-right, D bottom-left")

    page = doc[2]
    pos, edges, dist = board(page, {"A", "B", "C", "D", "E"}, (0, 0, 612, 792))
    log(f"p3 joined dots {({k: (round(v[0], 1), round(v[1], 1)) for k, v in pos.items()})} edges {edges}")
    check(set(pos) == set("ABCDE") and max(dist.values()) < 16, "p3: five dots labelled A-E")
    want = {"AC": "solid", "BC": "solid", "CD": "solid", "CE": "solid", "AB": "dashed", "DE": "dashed"}
    # A-C-E and B-C-D are collinear, so AE and BD read back as solid lines through C.
    extra = {k: v for k, v in edges.items() if k not in want}
    check({k: edges.get(k) for k in want} == want, "p3: AC, BC, CD, CE solid; AB, DE dashed (matches text and guide)")
    log("p3: other dot pairs joined by a straight drawn line:", extra, "(A-C-E and B-C-D are straight lines through C)")
    check(abs(math.dist(pos["A"], pos["B"]) / CM - 5.8) < 0.02 and abs(math.dist(pos["D"], pos["E"]) / CM - 5.8) < 0.02,
          "p3: AB = DE = 5.8 cm (guide's yarn strips)")
    check(abs((pos["D"][0] - pos["A"][0]) / CM - 11.6) < 0.02, "p3: board 11.6 cm wide")

    page = doc[4]
    pos, edges, dist = board(page, {"A", "B", "C", "D", "O"}, (0, 0, 612, 792))
    log(f"p5 fan dots {({k: (round(v[0], 1), round(v[1], 1)) for k, v in pos.items()})} edges {edges}")
    check(set(pos) == set("ABCDO") and max(dist.values()) < 16, "p5: five dots labelled A-D and O")
    want = {e: "solid" for e in ["AB", "BC", "CD", "AD", "AO", "BO", "CO", "DO"]}
    check({k: edges.get(k) for k in want} == want, "p5: all eight edges solid (matches 'Start with all eight edges')")
    log("p5: other pairs:", {k: v for k, v in edges.items() if k not in want}, "(AC, BD are straight through O)")
    sides = [math.dist(pos[a], pos[b]) / CM for a, b in ["AB", "BC", "CD", "DA"]]
    check(all(abs(s - 8) < 0.02 for s in sides), f"p5: fan square sides {[round(s, 3) for s in sides]} cm (8)")
    ctr = ((pos["A"][0] + pos["C"][0]) / 2, (pos["A"][1] + pos["C"][1]) / 2)
    check(math.dist(ctr, pos["O"]) < 0.3, "p5: O at the centre")

    # p1 launch triangle XYZ
    page = doc[0]
    tri = [d for d in page.get_drawings() if d.get("fill") and d["fill"][0] < 0.95 and d["fill"][0] > 0.5]
    check(len(tri) == 1, "p1: one shaded (filled) launch triangle")
    pts = [(it[1].x, it[1].y) for it in tri[0]["items"]]
    words = {w[4]: ((w[0] + w[2]) / 2, (w[1] + w[3]) / 2) for w in page.get_text("words") if w[4] in ("X", "Y", "Z")}
    near = {k: min(range(3), key=lambda i: math.dist(pts[i], v)) for k, v in words.items()}
    check(len(set(near.values())) == 3, "p1: X, Y, Z each label a different corner of the shaded triangle")
    ty = sum(p[1] for p in pts) / 3
    toks = [w[4] for w in sorted(page.get_text("words"), key=lambda w: w[0])
            if w[4] in ("XY", "YZ", "XZ") and abs((w[1] + w[3]) / 2 - ty) < 25]
    log("p1 token row:", toks)
    check(toks == ["XY", "YZ", "XY", "YZ", "XY", "YZ", "XZ", "XZ"], "p1: tokens XY YZ -> XY YZ XY YZ XZ -> XZ")

    log(f"\n{sum(l.startswith('PASS') for l in LINES)} passed, {len(FAILS)} failed")
    OUT.write_text("\n".join(LINES) + "\n")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
