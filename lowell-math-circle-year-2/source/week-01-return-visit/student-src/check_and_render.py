"""Render the packet and check three-page student-packet invariants."""
from pathlib import Path
import json
import fitz

packet = Path(__file__).resolve().parent.parent
doc = fitz.open(packet / "return-visit.pdf")
assert len(doc) == 3, f"Expected 3 pages, got {len(doc)}"
render_dir = packet / "render"
render_dir.mkdir(exist_ok=True)
for page_no, page in enumerate(doc, 1):
    text = page.get_text()
    assert f"Problem {page_no}:" in text
    assert sum(f"Problem {n}:" in text for n in (1, 2, 3)) == 1
    assert "Pattern-block return visits" in text
    assert "Bellingham Math Circle / Week 1 / W01-RV-v1" in text
    assert abs(page.rect.width - 612) < 0.01
    assert abs(page.rect.height - 792) < 0.01
    for block in page.get_text("dict")["blocks"]:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                assert 0 <= x0 < x1 <= 612, span
                assert 0 <= y0 < y1 <= 792, span
    page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(render_dir / f"page-{page_no}.png")
(render_dir / "text.txt").write_text("\n\f\n".join(p.get_text() for p in doc))
(render_dir / "digital-checks.json").write_text(json.dumps({
    "pages": len(doc), "letter_size": True, "consecutive_problems": True,
    "headers_and_footers": True, "all_text_within_page": True,
    "visual_inspection_required": [f"page-{n}.png" for n in range(1, 4)],
    "physical_fit_and_classroom_piloting": "untested; tabletop construction, printed hexagons are recording sketches"
}, indent=2) + "\n")
print(f"Rendered and digitally checked {len(doc)} pages in {render_dir}")
