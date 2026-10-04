#!/usr/bin/env python3
"""Render all PDF pages and reject content extending outside page margins."""
from pathlib import Path
import argparse,pymupdf as fitz,json
p=argparse.ArgumentParser()
p.add_argument("pdf",type=Path)
p.add_argument("--out",required=True,type=Path)
a=p.parse_args()
a.out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(a.pdf)
report=[]
for i,page in enumerate(doc,1):
    assert abs(page.rect.width-612)<0.1 and abs(page.rect.height-792)<0.1
    text=page.get_text()
    assert "Week 62 / Conflict networks / Grades" in text,(i,text[:100])
    assert "Bellingham Math Circle / Week 62 / W62-S-v1" in text
    for block in page.get_text("dict")["blocks"]:
        if block["type"]==0:
            for line in block["lines"]:
                x0,y0,x1,y1=line["bbox"]
                assert x0>=40 and x1<=574 and y0>=24 and y1<=780,(i,line["bbox"])
    page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(a.out/f"page-{i:02}.png")
    report.append({"page":i,"dimensions_pt":[page.rect.width,page.rect.height],"text_characters":len(text)})
(a.out/"render-checks.json").write_text(json.dumps(report,indent=2)+"\n")
(a.out/"students.txt").write_text("\n\n".join(p.get_text() for p in doc))
print(f"Rendered and checked {len(doc)} pages.")
