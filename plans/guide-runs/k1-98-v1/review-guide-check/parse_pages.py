"""Independent reviewer parser for the Week 98 K-1 student pages.

Reads the final student PDF's vector drawings (not the writer's sources or
checker) and reports, per page, every working board (thick outline) and record
board (thin outline): its size in squares, square size in mm, and the
(row, column) squares holding a printed seed (grey circle or black dot).

Usage: python3 -I parse_pages.py [path/to/k-1.pdf]  (writes JSON to stdout)
"""
import json
import sys

import fitz

PT_PER_MM = 72 / 25.4


def boards_on_page(page):
    drawings = page.get_drawings()
    outlines = []  # (rect, kind)
    lines = []
    circles = []
    for d in drawings:
        kinds = {it[0] for it in d["items"]}
        w = round(d.get("width") or 0, 2)
        if kinds == {"c"} and d.get("fill") is not None:
            circles.append(d["rect"])
            continue
        if kinds == {"l"}:
            r = d["rect"]
            if w in (1.69, 1.1) and r.width > 20 and r.height > 20:
                outlines.append((r, "working" if w == 1.69 else "record"))
            elif w in (0.9, 0.6):
                for it in d["items"]:
                    lines.append((it[1], it[2], w))
    boards = []
    for r, kind in outlines:
        inner_w = 0.9 if kind == "working" else 0.6
        xs, ys = set(), set()
        for p, q, w in lines:
            if w != inner_w:
                continue
            if abs(p.x - q.x) < 0.01 and r.x0 - 0.5 < p.x < r.x1 + 0.5 and \
                    min(p.y, q.y) >= r.y0 - 0.5 and max(p.y, q.y) <= r.y1 + 0.5:
                xs.add(round(p.x, 1))
            if abs(p.y - q.y) < 0.01 and r.y0 - 0.5 < p.y < r.y1 + 0.5 and \
                    min(p.x, q.x) >= r.x0 - 0.5 and max(p.x, q.x) <= r.x1 + 0.5:
                ys.add(round(p.y, 1))
        xs = sorted(x for x in xs if r.x0 + 1 < x < r.x1 - 1)
        ys = sorted(y for y in ys if r.y0 + 1 < y < r.y1 - 1)
        cols, rows = len(xs) + 1, len(ys) + 1
        cw = r.width / cols
        ch = r.height / rows
        seeds = []
        for c in circles:
            cx, cy = (c.x0 + c.x1) / 2, (c.y0 + c.y1) / 2
            if r.x0 < cx < r.x1 and r.y0 < cy < r.y1:
                seeds.append((int((cy - r.y0) // ch) + 1, int((cx - r.x0) // cw) + 1,
                              round(c.width / PT_PER_MM, 1)))
        boards.append({
            "kind": kind,
            "rows": rows, "cols": cols,
            "square_mm": [round(cw / PT_PER_MM, 2), round(ch / PT_PER_MM, 2)],
            "top_left_mm": [round(r.x0 / PT_PER_MM, 1), round(r.y0 / PT_PER_MM, 1)],
            "seeds": sorted(seeds),
        })
    boards.sort(key=lambda b: (b["kind"] != "working", round(b["top_left_mm"][1] / 20),
                               b["top_left_mm"][0]))
    return boards


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "k-1.pdf"
    doc = fitz.open(path)
    out = {}
    for pno, page in enumerate(doc, start=1):
        text = page.get_text()
        prob = [ln for ln in text.splitlines() if ln.startswith("Problem")]
        out[pno] = {"problem_lines": prob, "boards": boards_on_page(page)}
    json.dump(out, sys.stdout, indent=1)


if __name__ == "__main__":
    main()
