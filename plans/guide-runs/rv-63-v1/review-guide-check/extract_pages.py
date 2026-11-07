"""Reviewer's own extraction of boards and grids from the FINAL student PDFs.

Reads only the compiled PDFs (not any build script or the guide writer's checker).
Prints every forbidden board (card -> refused homes) and every shaded grid,
and writes them to pages.json beside this script for check_answers.py.

Usage: python3 -I extract_pages.py [student_pdf_dir]
"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import collections
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")
import fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = _REPO + "/plans/return-visit-drafts/week-63"
SRC = sys.argv[1] if len(sys.argv) > 1 else DEFAULT


def spans(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                t = s["text"].strip()
                if len(t) == 1 and t.isupper():
                    x0, y0, x1, y1 = s["bbox"]
                    out.append(dict(t=t, x=(x0 + x1) / 2, y=y0, size=round(s["size"], 1)))
    return out


def boards(pdf, pageno, label_size, crossed_size):
    """Return list of boards on a page; each is {home: sorted refused cards}."""
    p = fitz.open(os.path.join(SRC, pdf))[pageno - 1]
    sp = spans(p)
    labels = [s for s in sp if s["size"] == label_size]
    crossed = [s for s in sp if s["size"] in crossed_size]
    rows = collections.defaultdict(list)
    for s in labels:
        rows[round(s["y"])].append(s)
    result = []
    for y in sorted(rows):
        homes = sorted(rows[y], key=lambda s: s["x"])
        names = "".join(h["t"] for h in homes)
        if names not in ("ABC", "ABCD", "ABCDE"):
            continue
        refuse = {h["t"]: [] for h in homes}
        for c in crossed:
            dy = y - c["y"]
            if 20 < dy < 60:
                h = min(homes, key=lambda h: abs(h["x"] - c["x"]))
                refuse[h["t"]].append(c["t"])
        if any(refuse.values()):
            result.append({k: sorted(v) for k, v in refuse.items()})
    return result


def grids(pdf, pageno):
    """Group grey squares into grids; map each to (card row label, home column label)."""
    p = fitz.open(os.path.join(SRC, pdf))[pageno - 1]
    sp = [s for s in spans(p)]
    # small letters used as grid labels: all single capitals on the page
    shaded = []
    dots = []
    for dr in p.get_drawings():
        f = dr.get("fill")
        r = dr["rect"]
        if f is not None and abs(f[0] - 0.77) < 0.02 and abs(r.width - r.height) < 0.5:
            shaded.append(r)
        if f is not None and f[0] < 0.05 and 7 < r.width < 10:
            dots.append(r)
    # cluster by cell size then by proximity
    out = []
    used = [False] * len(shaded)
    for i, r in enumerate(shaded):
        if used[i]:
            continue
        group = [r]
        used[i] = True
        changed = True
        while changed:
            changed = False
            for j, q in enumerate(shaded):
                if used[j] or abs(q.width - r.width) > 0.3:
                    continue
                if any(abs(q.x0 - g.x0) < 5.5 * r.width and abs(q.y0 - g.y0) < 5.5 * r.width for g in group):
                    group.append(q)
                    used[j] = True
                    changed = True
        out.append(group)

    def label_for(rect, size_tol=None):
        cx, cy = (rect.x0 + rect.x1) / 2, (rect.y0 + rect.y1) / 2
        w = rect.width
        # row label: to the left, same y
        left = [s for s in sp if s["x"] < rect.x0 and abs((s["y"] + 3) - cy) < w * 0.6 and rect.x0 - s["x"] < 6 * w]
        up = [s for s in sp if s["y"] < rect.y0 and abs(s["x"] - cx) < w * 0.45 and rect.y0 - s["y"] < 6 * w]
        rl = max(left, key=lambda s: s["x"])["t"] if left else "?"
        cl = max(up, key=lambda s: s["y"])["t"] if up else "?"
        return rl, cl

    res = []
    for g in out:
        cells = sorted(label_for(r) for r in g)
        gdots = [d for d in dots if min(abs(d.x0 - r.x0) for r in g) < 6 * g[0].width and min(abs(d.y0 - r.y0) for r in g) < 6 * g[0].width]
        res.append(dict(cell=round(g[0].width, 1), x=round(min(r.x0 for r in g)), y=round(min(r.y0 for r in g)),
                        shaded=cells, dots=sorted(label_for(fitz.Rect(d.x0 - 4, d.y0 - 4, d.x1 + 4, d.y1 + 4)) for d in gdots)))
    res.sort(key=lambda d: (d["y"] // 40, d["x"]))
    return res


def main():
    data = {}
    data["K1_P6"], = boards("k-1.pdf", 4, 12.0, (9.0, 10.0)) or [None]
    data["K1_P7"], data["K1_P8"] = boards("k-1.pdf", 5, 12.0, (9.0, 10.0))
    data["M_P8"] = boards("grades-2-3.pdf", 5, 10.0, (9.0,))
    data["U_P10"], = boards("grades-4-5.pdf", 7, 12.0, (10.0,))
    data["U_P11"] = boards("grades-4-5.pdf", 8, 12.0, (10.0,))
    data["U_grids_p9"] = grids("grades-4-5.pdf", 9)
    data["U_grids_p10"] = grids("grades-4-5.pdf", 10)
    for k, v in data.items():
        print(k)
        if isinstance(v, list):
            for item in v:
                print("   ", item)
        else:
            print("   ", v)
    with open(os.path.join(HERE, "pages.json"), "w") as fh:
        json.dump(data, fh, indent=1)


if __name__ == "__main__":
    main()
