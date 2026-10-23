#!/usr/bin/env python3
"""Compare page text, dimensions, and rendered pixels of two clean builds."""
from pathlib import Path
import argparse,hashlib,json,pymupdf
p=argparse.ArgumentParser()
p.add_argument("first",type=Path)
p.add_argument("second",type=Path)
p.add_argument("--report",type=Path)
a=p.parse_args()
first=pymupdf.open(a.first)
second=pymupdf.open(a.second)
assert len(first)==len(second)==9
results=[]
for i,(x,y) in enumerate(zip(first,second),1):
    assert x.rect==y.rect
    assert x.get_text()==y.get_text()
    px=x.get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False)
    py=y.get_pixmap(matrix=pymupdf.Matrix(1.35,1.35),alpha=False)
    assert px.samples==py.samples
    results.append({"page":i,"text_equal":True,"dimensions_equal":True,"pixels_equal":True,"render_sha256":hashlib.sha256(px.samples).hexdigest()})
if a.report:
    a.report.write_text(json.dumps(results,indent=2)+"\n")
print("All 9 pages reproduce identical text, page dimensions and rendered pixels.")
