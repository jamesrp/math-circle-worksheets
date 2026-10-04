#!/usr/bin/env python3
"""Render every page and check text, page size, and page-band coverage."""
from pathlib import Path
import argparse
import json
import pymupdf

parser = argparse.ArgumentParser()
parser.add_argument("pdf", type=Path)
parser.add_argument("--render-dir", type=Path, required=True)
args = parser.parse_args()
args.render_dir.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(args.pdf)
assert len(doc) == 7, f"Expected 7 pages, got {len(doc)}"
report = []
bands = ["Grades 2–5", "Grades 2–5", "Grades 2–5", "Grades 4–5", "Grades 4–5", "Grades 2–5", "Grades 2–5"]
expected_boards = [
    [(4,4,12.5)]*4, [(4,4,12.5)]*6, [(4,4,12.5)]*6,
    [(6,4,22)], [(6,4,18)]*2,
    [(2,3,12.5),(3,4,12.5),(4,5,12.5),(4,6,12.5)], []]
for i, page in enumerate(doc):
    assert abs(page.rect.width-612) < 0.01 and abs(page.rect.height-792) < 0.01
    text = page.get_text()
    normalized = text.replace("--", "–").replace("−", "–").replace("-", "–")
    assert bands[i] in normalized, (i+1, text[:150])
    assert "Bellingham Math Circle / Week 9 / F09-RV-v1" in text
    if i == 5:
        assert "For diagonal paths, move one square across and one square up or down each step." in text.replace("\n", " ")
    boards = [d for d in page.get_drawings()
              if d.get("color") == (0.0,0.0,0.0)
              and 0.8 < d.get("width",0) < 1
              and len(d["items"]) == 4 and all(item[0] == "l" for item in d["items"])]
    assert len(boards) == len(expected_boards[i]), (i+1, len(boards))
    dimensions = []
    for drawing, (w,h,unit_mm) in zip(boards, expected_boards[i]):
        rect = drawing["rect"]
        x_unit, y_unit = rect.width/w, rect.height/h
        assert abs(x_unit-y_unit) < 0.005, (i+1, "unequal scaling")
        assert abs(x_unit*25.4/72-unit_mm) < 0.01, (i+1, "wrong printed size")
        # Each board is a closed quadrilateral with horizontal/vertical sides.
        for j, item in enumerate(drawing["items"]):
            a,b = item[1], item[2]
            assert (abs(a.x-b.x)<0.001) != (abs(a.y-b.y)<0.001)
            nxt = drawing["items"][(j+1)%4][1]
            assert abs(b.x-nxt.x)<0.001 and abs(b.y-nxt.y)<0.001
        dimensions.append({"width_units":w,"height_units":h,"unit_mm":unit_mm,"sides":4})
    if i == 6:
        grid = [d for d in page.get_drawings()
                if 0.34 < (d.get("width") or 0) < 0.36
                and d["rect"].width > 400 and d["rect"].height > 400]
        assert len(grid) == 1
        assert abs(grid[0]["rect"].width-grid[0]["rect"].height) < 0.005
        assert abs(grid[0]["rect"].width*25.4/72-150) < 0.02
        dimensions.append({"width_units":12,"height_units":12,"unit_mm":12.5,"sides":"unbounded workspace"})
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                assert 0 <= x0 < x1 <= 612 and 0 <= y0 < y1 <= 792, (i+1, span)
    image = args.render_dir/f"page-{i+1:02d}.png"
    page.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3), alpha=False).save(image)
    report.append({"page": i+1, "band": bands[i], "render": image.name,"boards":dimensions,
                   "text": text})
(args.render_dir/"pdf-checks.json").write_text(json.dumps(report, indent=2)+"\n")
print(f"Rendered and text-checked all {len(doc)} Letter pages.")
