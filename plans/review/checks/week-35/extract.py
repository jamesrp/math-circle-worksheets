"""Read the delivered Week 35 student PDFs (not the sources) with pdfplumber.

For every page it records: polygons (closed curves) with fill colours, small
filled curves (arrowheads, circles), straight lines with dash/colour/width,
rectangles, single words and the page text.  Coordinates are PDF points with
pdfplumber's top-left origin.  Output: extracted.json and out_extract.txt.
"""
import json
import re
import pdfplumber
from common import HERE, STUDENT, GUIDES, Tee

out = Tee(HERE / "out_extract.txt")


def r(v):
    return round(float(v), 3)


def colour(c):
    if c is None:
        return None
    if isinstance(c, (int, float)):
        return [r(c)]
    return [r(v) for v in c]


data = {}
for band, path in STUDENT.items():
    pages = []
    with pdfplumber.open(path) as pdf:
        for i, p in enumerate(pdf.pages):
            pg = {"page": i + 1, "curves": [], "lines": [], "rects": [], "words": [],
                  "text": p.extract_text() or ""}
            for c in p.curves:
                pg["curves"].append({
                    "pts": [[r(x), r(y)] for x, y in c["pts"]],
                    "fill": bool(c.get("fill")),
                    "fill_colour": colour(c.get("non_stroking_color")),
                    "stroke_colour": colour(c.get("stroking_color")),
                })
            for l in p.lines:
                d = l.get("dash")
                pg["lines"].append({
                    "x0": r(l["x0"]), "y0": r(l["top"]), "x1": r(l["x1"]), "y1": r(l["bottom"]),
                    "pts": [[r(x), r(y)] for x, y in l["pts"]],
                    "dashed": bool(d and d[0]),
                    "colour": colour(l.get("stroking_color")),
                    "width": r(l.get("linewidth", 0)),
                })
            for b in p.rects:
                pg["rects"].append({"x0": r(b["x0"]), "y0": r(b["top"]), "x1": r(b["x1"]), "y1": r(b["bottom"])})
            for w in p.extract_words():
                pg["words"].append({"text": w["text"], "x0": r(w["x0"]), "x1": r(w["x1"]),
                                    "top": r(w["top"]), "bottom": r(w["bottom"])})
            pages.append(pg)
    data[band] = pages
    out(f"== {band}: {path.name}, {len(pages)} pages")
    for pg in pages:
        probs = re.findall(r"Problem (\d+):", pg["text"])
        polys = [c for c in pg["curves"] if len(c["pts"]) >= 11]
        small = [c for c in pg["curves"] if len(c["pts"]) < 11]
        out(f"  p{pg['page']}: problems {probs}; polygons {len(polys)}; small curves {len(small)}; "
            f"lines {len(pg['lines'])} (dashed {sum(l['dashed'] for l in pg['lines'])}); rects {len(pg['rects'])}")

for name, path in GUIDES.items():
    with pdfplumber.open(path) as pdf:
        data[name] = [{"page": i + 1, "text": p.extract_text() or ""} for i, p in enumerate(pdf.pages)]
    out(f"== {name}: {path.name}, {len(data[name])} pages (text only)")

(HERE / "extracted.json").write_text(json.dumps(data, indent=1))
out("wrote extracted.json")
out.save()
