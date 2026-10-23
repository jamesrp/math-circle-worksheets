#!/usr/bin/env python3
"""Render every page and check text bounds, headers, dimensions and numbering."""
import argparse
import json
from pathlib import Path
import re
import pymupdf

parser = argparse.ArgumentParser()
parser.add_argument("pdf", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
doc = pymupdf.open(args.pdf)
assert len(doc) == 12, len(doc)
bands = ["K–1"] * 2 + ["2–3"] * 2 + ["3–5"] * 5 + ["4–5"] * 3
problems = []
report = []
for i, page in enumerate(doc, 1):
    text = page.get_text()
    assert (page.rect.width, page.rect.height) == (612, 792)
    assert f"Week 52 / Hinged frames and braces / Grades {bands[i-1]}" in text
    assert "Bellingham Math Circle / Week 52 / F52-S-v2" in text
    numbers = list(map(int, re.findall(r"Problem (\d+):", text)))
    assert numbers, f"page {i} has no problem"
    problems.extend(numbers)
    for word in page.get_text("words"):
        x0, y0, x1, y1 = word[:4]
        assert 35 <= x0 <= x1 <= 581, (i, word)
        assert 15 <= y0 <= y1 <= 778, (i, word)
    page.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False).save(args.output / f"page-{i:02}.png")
    report.append({"page": i, "band": bands[i-1], "problems": numbers, "page_size_points": list(page.rect)})
assert problems == list(range(1, 15)), problems
(args.output / "text.txt").write_text("\n\n".join(f"PAGE {i+1}\n" + p.get_text() for i, p in enumerate(doc)))
(args.output / "digital-checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(f"Rendered and checked {len(doc)} pages; all headers, text bounds and problem numbers pass.")
