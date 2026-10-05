#!/usr/bin/env python3
"""Week 39 math check: extract, from the delivered student PDFs, everything the
mathematics depends on: problem text, each road map (node labels, centres,
radii, drawn edges), the worked step-tile example (arrow direction on each
mini map, struck-out tiles), and every printed route string.

Writes extracted.json next to this script.  Needs PyMuPDF (pip install pymupdf).
Run: python3 extract.py > out_extract.txt
"""
import json
import math
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def find_repo():
    # Committed copy lives in plans/review/checks/week-39/: four folders up.
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-39"
BANDS = {"k-1": "week-39-k-1.pdf", "grades-2-3": "week-39-grades-2-3.pdf",
         "grades-4-5": "week-39-grades-4-5.pdf"}
LETTERS = set("ABCDEFH")


def close(a, b, tol):
    return math.dist(a, b) <= tol


def text_lines(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"])
            sp = l["spans"][0]
            out.append({"text": t, "bbox": [round(v, 2) for v in l["bbox"]],
                        "font": sp["font"], "size": round(sp["size"], 2)})
    return out


def problems(lines):
    """Join the large-type problem paragraphs (LMRoman12 at >= 12.4 pt)."""
    probs, cur = [], None
    for l in lines:
        big = l["font"].startswith("LMRoman12") and l["size"] >= 12.4
        if big and l["text"].startswith("Problem "):
            cur = {"text": l["text"], "top": l["bbox"][1]}
            probs.append(cur)
        elif big and cur is not None and abs(l["bbox"][1] - last) < 22:
            # Re-join hyphenated line breaks.
            if cur["text"].endswith("-"):
                cur["text"] = cur["text"][:-1] + l["text"]
            else:
                cur["text"] += " " + l["text"]
        else:
            if not big:
                cur = None if l["size"] < 12 else cur
            continue
        last = l["bbox"][1]
    return probs


def maps(page, lines):
    """Big road maps: circles drawn with 0.7pt black outline and coloured fill."""
    dr = page.get_drawings()
    circles = []
    for d in dr:
        if d["type"] == "fs" and abs((d.get("width") or 0) - 0.7) < 0.05 and all(i[0] == "c" for i in d["items"]):
            r = d["rect"]
            circles.append({"c": ((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2),
                            "rx": (r.x1 - r.x0) / 2, "ry": (r.y1 - r.y0) / 2})
    labels = [l for l in lines if l["text"].strip() in LETTERS and abs(l["size"] - 12) < 0.3]
    for c in circles:
        hits = []
        for l in labels:
            b = l["bbox"]
            mid = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
            if close(mid, c["c"], c["rx"]):
                hits.append(l["text"].strip())
        c["label"] = hits[0] if len(hits) == 1 else hits
    edges, underlays = [], []
    for d in dr:
        if d["type"] != "s" or len(d["items"]) != 1 or d["items"][0][0] != "l":
            continue
        w = d.get("width") or 0
        p, q = d["items"][0][1], d["items"][0][2]
        col = d.get("color")
        if abs(w - 0.7) < 0.05 and col and max(col) < 0.05:
            edges.append(((p.x, p.y), (q.x, q.y)))
        elif abs(w - 8.5) < 0.2:
            underlays.append(((p.x, p.y), (q.x, q.y)))

    def name(pt):
        for c in circles:
            if close(pt, c["c"], 1.0):
                return c["label"]
        return None

    # Group circles into separate maps by connectivity through edges.
    named_edges = []
    for p, q in edges:
        a, b = name(p), name(q)
        named_edges.append({"a": a, "b": b, "p": [round(v, 2) for v in p], "q": [round(v, 2) for v in q]})
    named_under = []
    for p, q in underlays:
        named_under.append({"a": name(p), "b": name(q)})
    return {"nodes": [{"label": c["label"], "x": round(c["c"][0], 2), "y": round(c["c"][1], 2),
                       "rx": round(c["rx"], 2), "ry": round(c["ry"], 2)} for c in circles],
            "edges": named_edges, "underlays": named_under}


def step_tiles(page, lines):
    """Worked example: mini maps inside 0.3pt grey card rectangles."""
    dr = page.get_drawings()
    cards = []
    for d in dr:
        if d["type"] == "s" and abs((d.get("width") or 0) - 0.3) < 0.05 and len(d["items"]) == 4:
            if d["rect"].width < 100:  # step tiles are 31 x 26 mm; answer boxes are wide
                cards.append(d["rect"])
    if not cards:
        return []
    minis = [l for l in lines if l["text"].strip() in LETTERS and abs(l["size"] - 7) < 0.3]
    dots = []
    for d in dr:
        if d["type"] == "f" and all(i[0] == "c" for i in d["items"]):
            r = d["rect"]
            if r.width < 8:  # mini-map dots are 2.4 mm across
                dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    out = []
    for r in sorted(cards, key=lambda r: (round(r.y0), r.x0)):
        inside = lambda pt: r.x0 - 0.5 <= pt[0] <= r.x1 + 0.5 and r.y0 - 0.5 <= pt[1] <= r.y1 + 0.5
        cdots = [p for p in dots if inside(p)]
        # Each dot's label sits about 4 mm (11.3 pt) above it.
        named = {}
        for p in cdots:
            best = None
            for l in minis:
                b = l["bbox"]
                mid = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
                if inside(mid) and abs(mid[0] - p[0]) < 2 and 6 < p[1] - mid[1] < 16:
                    best = l["text"].strip()
            named[best] = p
        shafts, heads, strikes, roads = [], [], [], []
        for d in dr:
            it = d["items"]
            if not all(inside((pt.x, pt.y)) for i in it for pt in i[1:] if hasattr(pt, "x")):
                continue
            w = d.get("width") or 0
            col = d.get("color")
            if d["type"] == "s" and len(it) == 1 and it[0][0] == "l":
                p, q = (it[0][1].x, it[0][1].y), (it[0][2].x, it[0][2].y)
                if abs(w - 1.0) < 0.05 and col and max(col) < 0.05:
                    shafts.append((p, q))
                elif abs(w - 0.7) < 0.05:
                    strikes.append((p, q))
                elif abs(w - 2.83) < 0.1:
                    roads.append((p, q))
            elif d["type"] == "fs" and abs(w - 1.0) < 0.05:
                pts = [pt for i in it for pt in i[1:] if hasattr(pt, "x")]
                heads.append((sum(p.x for p in pts) / len(pts), sum(p.y for p in pts) / len(pts)))

        def lab(pt):
            k = min(named, key=lambda k: math.dist(named[k], pt))
            return k, round(math.dist(named[k], pt), 2)

        arrows = []
        for p, q in shafts:
            h = min(heads, key=lambda h: min(math.dist(h, p), math.dist(h, q)))
            tail, tip = (p, q) if math.dist(h, q) < math.dist(h, p) else (q, p)
            # The shaft is drawn to the node centre; report node names of tail and tip.
            arrows.append({"from": lab(tail), "to": lab(tip)})
        road_names = sorted("".join(sorted([lab(p)[0], lab(q)[0]])) for p, q in roads)
        out.append({"card": [round(r.x0, 1), round(r.y0, 1)], "arrows": arrows,
                    "struck": len(strikes) > 0, "roads": road_names})
    return out


def routes(lines):
    out = []
    for l in lines:
        if "→" in l["text"] and l["font"].startswith("LMMath"):
            t = l["text"].replace("−→", "").replace("→", " ").split()
            out.append({"route": "".join(t), "y": l["bbox"][1]})
    return out


def main():
    data = {}
    for band, fn in BANDS.items():
        doc = pymupdf.open(WEEK / fn)
        pages = []
        for i, page in enumerate(doc):
            lines = text_lines(page)
            pg = {"page": i + 1,
                  "header": lines[0]["text"],
                  "footer": [l["text"] for l in lines if l["text"].startswith("Bellingham")],
                  "rules": " ".join(l["text"] for l in lines if l["font"].startswith("LMRoman12") and abs(l["size"] - 11) < 0.2),
                  "problems": problems(lines),
                  "map": maps(page, lines),
                  "tiles": step_tiles(page, lines),
                  "routes": routes(lines)}
            pages.append(pg)
        data[band] = pages
    (HERE / "extracted.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
    for band, pages in data.items():
        print("==", band)
        for pg in pages:
            print(" page", pg["page"], "|", pg["header"], "|", pg["footer"])
            if pg["rules"]:
                print("   rules:", pg["rules"])
            for t in pg["tiles"]:
                print("   tile", t["card"], [(a["from"][0], a["to"][0]) for a in t["arrows"]],
                      "struck" if t["struck"] else "", "roads", t["roads"])
            for p in pg["problems"]:
                print("   ", p["text"])
            if pg["map"]["nodes"]:
                print("    nodes:", [(n["label"], n["x"], n["y"]) for n in pg["map"]["nodes"]])
                print("    edges:", sorted("".join(sorted([e["a"], e["b"]])) if isinstance(e["a"], str) and isinstance(e["b"], str) else str((e["a"], e["b"])) for e in pg["map"]["edges"]))
            for r in pg["routes"]:
                print("    route:", r["route"])


if __name__ == "__main__":
    main()
