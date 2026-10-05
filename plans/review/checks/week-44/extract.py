#!/usr/bin/env python3
"""Week 44 math check: read the delivered PDFs (not the sources).

For every page of the six delivered PDFs this records, from the PDF vector
data (PyMuPDF):
  * every counter disc: centre, width, height, fill colour and its label;
  * every stroked box (answer box, bag box, story cell, history card);
  * every straight line segment (arrows, ruled answer lines);
  * which discs lie inside which boxes;
  * the page text.
It also compares the delivered PDFs with the reference copies in the sources
by SHA-256.  Output: extracted.json (data) and out_extract.txt (summary).

Run: python3 extract.py > out_extract.txt
"""
import hashlib
import json

import pymupdf

from common import BONUS_SRC, HERE, PDFS, SRC


def colour_name(fill):
    if fill is None:
        return None
    r, g, b = fill[:3]
    if r > g + 0.05 and r > b + 0.05:
        return "R"
    if b > r + 0.05 and b > g + 0.05:
        return "B"
    if g > r + 0.05 and g > b + 0.05:
        return "G"
    return "other"


def inside(pt, rect, pad=0.5):
    x, y = pt
    return rect[0] - pad <= x <= rect[2] + pad and rect[1] - pad <= y <= rect[3] + pad


def page_data(page):
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for sp in line["spans"]:
                t = sp["text"].strip()
                if t:
                    x0, y0, x1, y1 = sp["bbox"]
                    spans.append({"text": t, "cx": (x0 + x1) / 2, "cy": (y0 + y1) / 2,
                                  "bbox": [x0, y0, x1, y1]})
    discs, boxes, segs = [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d["items"]]
        r = d["rect"]
        if kinds and all(k == "c" for k in kinds) and d.get("fill") is not None:
            cx, cy = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
            lab = [s["text"] for s in spans
                   if abs(s["cx"] - cx) < r.width / 2 and abs(s["cy"] - cy) < r.height / 2]
            discs.append({"cx": round(cx, 2), "cy": round(cy, 2), "w": round(r.width, 3),
                          "h": round(r.height, 3), "colour": colour_name(d["fill"]),
                          "label": " ".join(lab)})
        elif r.width > 15 and r.height > 15 and d.get("fill") is None and (
                "re" in kinds or ("l" in kinds and "c" in kinds) or kinds.count("l") == 4):
            boxes.append([round(r.x0, 2), round(r.y0, 2), round(r.x1, 2), round(r.y1, 2)])
        else:
            for it in d["items"]:
                if it[0] == "l":
                    p, q = it[1], it[2]
                    segs.append([round(p.x, 2), round(p.y, 2), round(q.x, 2), round(q.y, 2)])
    # PyMuPDF may report a ReportLab rectangle twice (stroke and path); dedupe.
    boxes = sorted({tuple(b) for b in boxes}, key=lambda b: (round(b[1]), b[0]))
    bags = []
    for b in boxes:
        members = [dd for dd in discs if inside((dd["cx"], dd["cy"]), b)]
        members.sort(key=lambda dd: (round(dd["cy"]), dd["cx"]))
        bags.append({"box": list(b), "discs": [dd["label"] or dd["colour"] for dd in members],
                     "colours": "".join(dd["colour"] for dd in members)})
    return {"text": page.get_text("text"), "discs": discs, "boxes": [list(b) for b in boxes],
            "bags": bags, "segments": segs}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = {}
    for key, path in PDFS.items():
        with pymupdf.open(path) as doc:
            out[key] = [page_data(p) for p in doc]
    (HERE / "extracted.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

    print("Delivered PDFs vs reference copies in the sources (SHA-256):")
    refs = {
        "k-1": SRC / "editable" / "reference-pdfs" / "k-1.pdf",
        "grades-2-3": SRC / "editable" / "reference-pdfs" / "grades-2-3.pdf",
        "grades-4-5": SRC / "editable" / "reference-pdfs" / "grades-4-5.pdf",
        "guide": SRC / "editable" / "reference-pdfs" / "facilitator-guide.pdf",
        "bonus": BONUS_SRC / "reference-pdfs" / "week-44-bonus.pdf",
        "bonus-guide": BONUS_SRC / "reference-pdfs" / "week-44-bonus-facilitator.pdf",
    }
    for key, ref in refs.items():
        same = ref.exists() and sha(ref) == sha(PDFS[key])
        print(f"  {key:12s} {'identical' if same else 'DIFFERENT or missing'}  ({ref.relative_to(SRC.parents[1])})")

    for key, pages in out.items():
        print()
        print(f"== {key} ({len(pages)} pages)")
        for i, pg in enumerate(pages, 1):
            nonround = [d for d in pg["discs"] if abs(d["w"] - d["h"]) > 0.01]
            radii = sorted({round(d["w"] / 2, 2) for d in pg["discs"]})
            print(f" page {i}: {len(pg['discs'])} discs (radii pt {radii}; non-round {len(nonround)}), "
                  f"{len(pg['boxes'])} boxes, {len(pg['segments'])} line segments")
            free = [d for d in pg["discs"]
                    if not any(inside((d['cx'], d['cy']), b) for b in pg["boxes"])]
            if free:
                rows = {}
                for d in free:
                    rows.setdefault(round(d["cy"]), []).append(d)
                for y, ds in sorted(rows.items()):
                    ds.sort(key=lambda d: d["cx"])
                    print(f"   loose discs at y={y}: " + ", ".join(
                        f"{d['label'] or '?'}({d['colour']})@x{round(d['cx'])}" for d in ds))
            for bag in pg["bags"]:
                if bag["discs"]:
                    x0, y0, x1, y1 = bag["box"]
                    print(f"   box [{x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f}] holds "
                          f"{' '.join(bag['discs'])}  -> R={bag['colours'].count('R')} "
                          f"B={bag['colours'].count('B')} G={bag['colours'].count('G')}")
            mismatch = [d for d in pg["discs"] if d["label"] and d["colour"] != d["label"][0]]
            if mismatch:
                print("   COLOUR/LABEL MISMATCH:", mismatch)


if __name__ == "__main__":
    main()
