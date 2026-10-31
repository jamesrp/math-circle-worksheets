"""Measure the working-home boards on the final student PDFs (reviewer's check).

For each page, report the boards built from home cells, in mm, so the guide's
"35 x 45 mm working homes" and "small reference boards" claims can be checked.
Usage: python3 -I measure_boards.py [student_pdf_dir]
"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import os
import sys
import warnings

warnings.filterwarnings("ignore")
import fitz

SRC = sys.argv[1] if len(sys.argv) > 1 else _REPO + "/plans/return-visit-drafts/week-63"
MM = 25.4 / 72

for pdf in ("k-1.pdf", "grades-2-3.pdf", "grades-4-5.pdf"):
    doc = fitz.open(os.path.join(SRC, pdf))
    for pno, page in enumerate(doc, 1):
        cells = set()
        for dr in page.get_drawings():
            r = dr["rect"]
            w, h = r.width * MM, r.height * MM
            if w > 20 and h > 9 and len(dr["items"]) >= 1:
                cells.add((round(r.x0 * MM, 1), round(r.y0 * MM, 1), round(w, 1), round(h, 1)))
        big = sorted(c for c in cells if c[3] >= 9)
        if big:
            sizes = sorted({(c[2], c[3]) for c in big})
            print(pdf, "p%d" % pno, "cell sizes (w x h mm):", sizes)
