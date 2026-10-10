"""Shared helpers for the Week 38 (Seams and cuts) math check.

Finds the repository from this file's own location: four folders up from
plans/review/checks/week-38/ in the committed copy; falls back to searching
upward (so it also runs from tmp/review-runs/week-38/).

Contains a small PDF vector extractor built on pypdf (no PyMuPDF needed) and a
word-box extractor using Poppler's pdftotext -bbox.  Coordinates are returned
in millimetres from the top-left page corner, the same frame as the TikZ
sources (x=1mm, y=-1mm, shifted to the page's north-west corner).
"""
import math
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2" / "week-38").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2" / "week-38").is_dir() and (p / "AGENTS.md").is_file():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-38"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-38" / "editable" / "src"
BONUS_SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-38-bonus"
BANDS = {"k-1": "week-38-k-1.pdf", "grades-2-3": "week-38-grades-2-3.pdf",
         "grades-4-5": "week-38-grades-4-5.pdf"}
BONUS = "week-38-bonus.pdf"
PT2MM = 25.4 / 72.0
PAGE_H = 792.0


def to_mm(x, y):
    return (x * PT2MM, (PAGE_H - y) * PT2MM)


def _mul(m, n):
    # PDF matrices [a b c d e f]; returns m x n
    a, b, c, d, e, f = m
    A, B, C, D, E, F = n
    return [a * A + b * C, a * B + b * D, c * A + d * C, c * B + d * D,
            e * A + f * C + E, e * B + f * D + F]


def _apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


def extract_paths(pdf_path):
    """Return a list of pages; each page is a list of painted path dicts:
    {op, fill, stroke, lw, dash, subpaths:[[(kind,(xmm,ymm)),...]], clip}
    kind is 'm','l','c' (Bezier end point), 'cp' (control point)."""
    import pypdf
    reader = pypdf.PdfReader(str(pdf_path))
    out = []
    for page in reader.pages:
        cs = pypdf.generic.ContentStream(page.get_contents(), reader)
        st = {"ctm": [1, 0, 0, 1, 0, 0], "fill": (0, 0, 0), "stroke": (0, 0, 0),
              "lw": 1.0, "dash": [], "clip": None}
        stack = []
        subpaths = []
        cur = None
        pending_clip = False
        items = []

        def pt(x, y):
            return to_mm(*_apply(st["ctm"], float(x), float(y)))

        for operands, op in cs.operations:
            op = op.decode() if isinstance(op, bytes) else op
            if op == "q":
                stack.append(dict(st, ctm=list(st["ctm"])))
            elif op == "Q":
                st = stack.pop()
            elif op == "cm":
                st["ctm"] = _mul([float(v) for v in operands], st["ctm"])
            elif op in ("g",):
                v = float(operands[0]); st["fill"] = (v, v, v)
            elif op in ("G",):
                v = float(operands[0]); st["stroke"] = (v, v, v)
            elif op == "rg":
                st["fill"] = tuple(float(v) for v in operands)
            elif op == "RG":
                st["stroke"] = tuple(float(v) for v in operands)
            elif op == "w":
                st["lw"] = float(operands[0])
            elif op == "d":
                st["dash"] = [float(v) for v in operands[0]]
            elif op == "m":
                cur = [("m", pt(*operands))]; subpaths.append(cur)
            elif op == "l":
                cur.append(("l", pt(*operands)))
            elif op == "c":
                x1, y1, x2, y2, x3, y3 = operands
                cur.append(("cp", pt(x1, y1))); cur.append(("cp", pt(x2, y2)))
                cur.append(("c", pt(x3, y3)))
            elif op in ("v", "y"):
                pts = operands
                cur.append(("cp", pt(pts[0], pts[1])))
                cur.append(("c", pt(pts[2], pts[3])))
            elif op == "re":
                x, y, w, h = [float(v) for v in operands]
                cur = [("m", pt(x, y)), ("l", pt(x + w, y)), ("l", pt(x + w, y + h)),
                       ("l", pt(x, y + h)), ("l", pt(x, y))]
                subpaths.append(cur)
            elif op == "h":
                if cur:
                    cur.append(("h", cur[0][1]))
            elif op in ("W", "W*"):
                pending_clip = True
            elif op in ("S", "s", "f", "F", "f*", "B", "B*", "b", "b*", "n"):
                if pending_clip:
                    allp = [p for sp in subpaths for _, p in sp]
                    if allp:
                        xs = [p[0] for p in allp]; ys = [p[1] for p in allp]
                        st["clip"] = (min(xs), min(ys), max(xs), max(ys))
                    pending_clip = False
                if op != "n" and subpaths:
                    items.append({"op": op, "fill": st["fill"], "stroke": st["stroke"],
                                  "lw": st["lw"], "dash": list(st["dash"]),
                                  "subpaths": subpaths, "clip": st["clip"]})
                subpaths = []; cur = None
        out.append(items)
    return out


def bbox(points):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    return (min(xs), min(ys), max(xs), max(ys))


def onpts(sp):
    return [p for k, p in sp if k != "cp"]


def is_curved(sp):
    return any(k == "c" for k, _ in sp)


def describe(item):
    """Classify a painted path: 'dot' (filled dark closed curve), 'ellipse'
    (stroked closed curve), 'square'/'rect' (closed 4-corner polygon),
    'line' (open polyline) or 'other'."""
    res = []
    fills = item["op"] in ("f", "F", "f*", "B", "B*", "b", "b*")
    strokes = item["op"] in ("S", "s", "B", "B*", "b", "b*")
    for sp in item["subpaths"]:
        on = onpts(sp)
        bb = bbox([p for _, p in sp])
        cx = (bb[0] + bb[2]) / 2; cy = (bb[1] + bb[3]) / 2
        rx = (bb[2] - bb[0]) / 2; ry = (bb[3] - bb[1]) / 2
        d = {"bbox": bb, "c": (cx, cy), "rx": rx, "ry": ry, "fill": item["fill"] if fills else None,
             "stroke": item["stroke"] if strokes else None, "dash": bool(item["dash"]),
             "lw": item["lw"], "clip": item["clip"], "pts": on}
        if is_curved(sp):
            d["kind"] = "curve"
        elif len(on) >= 4 and math.dist(on[0], on[-1]) < 1e-6 and len(on) <= 6:
            d["kind"] = "poly4" if len({(round(p[0], 3), round(p[1], 3)) for p in on}) == 4 else "poly"
        else:
            d["kind"] = "line"
        res.append(d)
    return res


def page_shapes(pdf_path):
    return [[d for it in items for d in describe(it)] for items in extract_paths(pdf_path)]


def words(pdf_path):
    """Word boxes per page via pdftotext -bbox, in mm from top-left."""
    html = subprocess.run(["pdftotext", "-bbox", str(pdf_path), "-"], capture_output=True,
                          text=True, check=True).stdout
    pages = []
    for block in html.split("<page ")[1:]:
        ws = []
        for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', block):
            x0, y0, x1, y1 = (float(v) * PT2MM for v in m.groups()[:4])
            ws.append({"t": m.group(5), "bbox": (x0, y0, x1, y1), "c": ((x0 + x1) / 2, (y0 + y1) / 2)})
        pages.append(ws)
    return pages


def page_text(pdf_path):
    return subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"], capture_output=True,
                          text=True, check=True).stdout.split("\f")


class Checker:
    def __init__(self):
        self.fails = 0
        self.passes = 0

    def ok(self, cond, msg):
        if cond:
            self.passes += 1
            print("PASS", msg)
        else:
            self.fails += 1
            print("FAIL", msg)
        return cond

    def note(self, msg):
        print("NOTE", msg)

    def summary(self):
        print(f"\n{self.passes} passed, {self.fails} failed")
