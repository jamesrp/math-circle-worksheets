#!/usr/bin/env python3
"""Read back every strip, row diagram, label and answer box from the delivered
Week 54 student PDF and compare it with my own transcription of the rendered
pages (made by looking at 100 dpi renders, not taken from the TeX source).

Run: python3 check_diagrams.py > out_check_diagrams.txt
"""
from collections import defaultdict

import pdfgeom

REPO = pdfgeom.find_repo()
PDF = REPO / "lowell-math-circle-year-2/week-54/week-54-students.pdf"
PAGES = pdfgeom.read_pdf(PDF)

# My transcription of the rendered pages: (page, label, strips top to bottom).
EXPECTED = [
    (1, "demo 'Strips' loose 1-strip", [1]),
    (1, "demo 'Strips' loose 2-strip", [2]),
    (1, "demo 'Longest first'", [2, 1]),
    (3, "demo Before", [3, 3, 1, 1, 1, 1]),
    (3, "demo One join", [6, 1, 1, 1, 1]),
    (3, "demo All sizes different", [6, 4]),
    (3, "P3 case 1", [1] * 9),
    (3, "P3 case 2", [5, 5, 3, 3, 3, 1, 1]),
    (3, "P3 case 3", [5, 3, 1]),
    (4, "demo Before", [4, 3, 2]),
    (4, "demo One split", [3, 2, 2, 2]),
    (4, "demo Only odd sizes", [3, 1, 1, 1, 1, 1, 1]),
    (4, "P4 case 1", [10, 7, 4, 2, 1]),
    (4, "P4 case 2", [12, 6, 3]),
    (4, "P4 case 3", [7, 3, 1]),
    (6, "P6 input", [3, 3, 3, 3, 1, 1, 1, 1, 1, 1]),
    (7, "demo Rows", [5, 3, 3, 1]),
    (7, "demo Read columns (squares)", [5, 3, 3, 1]),
    (7, "demo New rows", [4, 3, 3, 1, 1]),
    (7, "P7 case 1", [5, 2, 1]),
    (7, "P7 case 2", [4, 4]),
    (7, "P7 case 3", [3, 3, 1, 1]),
]
# Answer areas: page -> list of (description, expected cell counts per box, top to bottom)
EXPECTED_BOXES = {
    1: [("4 units", 6), ("5 units", 8)],
    2: [("Only odd sizes", 6), ("All sizes different", 6)],
}
EXPECTED_BOX_ROWS = {5: 8, 8: 12}   # number of paired box rows


def strips_on_page(rects):
    """Group gray unit squares (fill 0.94) into horizontal runs of touching squares."""
    sq = [r for r in rects if abs(r["fill"] - 0.94) < 1e-6 and r["op"] == "B"]
    rows = defaultdict(list)
    for r in sq:
        rows[(round(r["y"] + r["h"], 1), round(r["h"], 2))].append(r)
    strips = []
    for (top, h), rs in rows.items():
        rs.sort(key=lambda r: r["x"])
        run = [rs[0]]
        for r in rs[1:]:
            if abs(r["x"] - (run[-1]["x"] + run[-1]["w"])) < 0.05:
                run.append(r)
            else:
                strips.append(run)
                run = [r]
        strips.append(run)
    out = []
    for run in strips:
        out.append({"left": run[0]["x"], "right": run[-1]["x"] + run[-1]["w"],
                    "top": run[0]["y"] + run[0]["h"], "bottom": run[0]["y"],
                    "n": len(run), "size": run[0]["w"],
                    "aspect": [round(r["w"] / r["h"], 4) for r in run]})
    return out


def diagrams(strips):
    """Strips sharing a left edge and square size, stacked closely, form one diagram."""
    groups = defaultdict(list)
    for s in strips:
        groups[(round(s["left"], 1), round(s["size"], 2))].append(s)
    out = []
    for (left, size), ss in groups.items():
        ss.sort(key=lambda s: -s["top"])
        cur = [ss[0]]
        for s in ss[1:]:
            if cur[-1]["bottom"] - s["top"] < size * 1.5:
                cur.append(s)
            else:
                out.append(cur)
                cur = [s]
        out.append(cur)
    out.sort(key=lambda d: (-round(d[0]["top"] / 40), d[0]["left"]))
    return out


def label_for(strip, texts):
    """Digit text immediately right of a strip and vertically centred on it."""
    cy = (strip["top"] + strip["bottom"]) / 2
    best = None
    for t in texts:
        if not t["s"].strip().isdigit():
            continue
        dx = t["x"] - strip["right"]
        if 0 < dx < 12 and abs(t["y"] + 3.3 - cy) < strip["size"] * 0.6 + 2:
            if best is None or dx < best[0]:
                best = (dx, t["s"].strip())
    return best[1] if best else None


def main():
    found = defaultdict(list)
    print("== Strip diagrams read from the PDF ==")
    for pno, (rects, texts, lines) in enumerate(PAGES, 1):
        ss = strips_on_page(rects)
        if not ss:
            continue
        for d in diagrams(ss):
            sizes = [s["n"] for s in d]
            labels = [label_for(s, texts) for s in d]
            sq = d[0]["size"]
            aspects = sorted(set(a for s in d for a in s["aspect"]))
            gaps = [round(d[i]["bottom"] - d[i + 1]["top"], 2) for i in range(len(d) - 1)]
            lefts = sorted(set(round(s["left"], 2) for s in d))
            found[pno].append(sizes)
            print(f"p{pno} left={d[0]['left']:.1f} top={d[0]['top']:.1f} unit={sq / 72 * 25.4:.2f} mm "
                  f"sizes={sizes} total={sum(sizes)} labels={labels} "
                  f"w/h={aspects} row gaps(pt)={sorted(set(gaps))} left edges={lefts}")
            lab_ok = all(l is None or l == str(n) for l, n in zip(labels, sizes))
            if not lab_ok:
                print("   LABEL MISMATCH")

    print()
    print("== Comparison with my transcription of the rendered pages ==")
    bad = 0
    for pno, name, want in EXPECTED:
        if want in found[pno]:
            found[pno].remove(want)
            print(f"ok   p{pno} {name}: {want} (total {sum(want)})")
        else:
            bad += 1
            print(f"MISS p{pno} {name}: {want}")
    for pno, rest in found.items():
        for r in rest:
            print(f"EXTRA p{pno}: {r}")
            bad += 1
    print("mismatches:", bad)

    print()
    print("== Page 1 'Strips' demo (loose squares) ==")
    rects, texts, _ = PAGES[0]
    ss = strips_on_page(rects)
    for s in sorted(ss, key=lambda s: (-s["top"], s["left"])):
        print(f"  strip of {s['n']} at left={s['left']:.1f} top={s['top']:.1f}")
    print("  record text:", [t["s"] for t in texts if "+" in t["s"] or t["s"].strip() in ("2", "1")])

    print()
    print("== Page 7: Read-columns outlines (thick, unfilled) and column labels ==")
    rects, texts, lines = PAGES[6]
    cols = [r for r in rects if r["op"] == "S" and r["w"] < 15]
    cols.sort(key=lambda r: r["x"])
    unit = 0.15 * 72
    heights = [round(r["h"] / unit, 3) for r in cols]
    print("  column outline heights (units):", heights)
    labs = sorted([t for t in texts if t["s"].strip().isdigit() and 250 < t["x"] < 340 and 560 < t["y"] < 580],
                  key=lambda t: t["x"])
    print("  labels under columns:", [t["s"] for t in labs])
    # conjugate of the drawn rows
    rows = [5, 3, 3, 1]
    conj = [sum(1 for r in rows if r > j) for j in range(max(rows))]
    print("  conjugate of (5,3,3,1):", conj, "matches outlines:", conj == [round(h) for h in heights])

    print()
    print("== Page 7 tiny answer grids ==")
    segs = [(a, b) for a, b in lines if abs(a[0] - b[0]) < 0.01 or abs(a[1] - b[1]) < 0.01]
    # tiny grids: segments of length 1.08 in = 77.76 pt
    tiny = [(a, b) for a, b in segs if abs(abs(a[0] - b[0]) + abs(a[1] - b[1]) - 77.76) < 0.05]
    print("  grid segments of length 1.08 in:", len(tiny), "(6 grids x 14 = 84 expected)")
    xs = sorted(set(round(a[0], 1) for a, b in tiny if abs(a[0] - b[0]) < 0.01))
    print("  vertical grid line x positions:", xs)

    print()
    print("== Answer boxes ==")
    for pno, want in EXPECTED_BOXES.items():
        rects, texts, lines = PAGES[pno - 1]
        boxes = sorted([r for r in rects if r["op"] == "S" and r["w"] > 200],
                       key=lambda r: (-r["y"], r["x"]))
        for (desc, ncells), b in zip(want, boxes):
            hl = [1 for a, c in lines if abs(a[1] - c[1]) < 0.01 and b["y"] + 1 < a[1] < b["y"] + b["h"] - 1
                  and min(a[0], c[0]) <= b["x"] + 0.5 and max(a[0], c[0]) >= b["x"] + b["w"] - 0.5]
            vl = [1 for a, c in lines if abs(a[0] - c[0]) < 0.01 and b["x"] + 1 < a[0] < b["x"] + b["w"] - 1
                  and min(a[1], c[1]) <= b["y"] + 0.5 and max(a[1], c[1]) >= b["y"] + b["h"] - 0.5]
            cells = (len(hl) + 1) * (len(vl) + 1)
            print(f"  p{pno} {desc}: {cells} cells (expected {ncells})", "ok" if cells == ncells else "MISMATCH")
    for pno, nrows in EXPECTED_BOX_ROWS.items():
        rects, _, _ = PAGES[pno - 1]
        boxes = [r for r in rects if r["op"] == "S" and 200 < r["w"] < 260]
        ys = sorted(set(round(r["y"], 0) for r in boxes))
        print(f"  p{pno}: {len(boxes)} boxes in {len(ys)} rows (expected {nrows} rows)",
              "ok" if len(ys) == nrows and len(boxes) == 2 * nrows else "MISMATCH")


if __name__ == "__main__":
    main()
