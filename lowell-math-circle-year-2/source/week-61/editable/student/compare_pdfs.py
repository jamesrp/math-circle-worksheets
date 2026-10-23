#!/usr/bin/env python3
"""Compare PDF dimensions, exact extracted text, and all raster bytes at 144 dpi."""
from pathlib import Path
import argparse,hashlib,json
import pymupdf

p=argparse.ArgumentParser();p.add_argument('pdfs',nargs='+');p.add_argument('--output');args=p.parse_args()
assert len(args.pdfs)>=2,'Supply original and at least one rebuilt PDF.'
def inspect(path):
    doc=pymupdf.open(path);pages=[]
    for n,page in enumerate(doc,1):
        pix=page.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False)
        text=page.get_text()
        pages.append({'page':n,'dimensions_points':list(page.rect),
            'text_sha256':hashlib.sha256(text.encode()).hexdigest(),
            'pixel_dimensions':[pix.width,pix.height,pix.n],
            'pixel_sha256':hashlib.sha256(pix.samples).hexdigest(),
            'text':text})
    return pages
original=inspect(args.pdfs[0]);comparisons=[]
for path in args.pdfs[1:]:
    observed=inspect(path)
    equal=observed==original
    comparisons.append({'pdf':str(Path(path).resolve()),'exact_dimensions_text_pixels':equal})
    assert equal,'Rebuild differs: '+path
report={'status':'all rebuilds identical','dpi':144,'page_count':len(original),
    'original_pdf':str(Path(args.pdfs[0]).resolve()),'comparisons':comparisons,
    'pages':[{k:v for k,v in pg.items() if k!='text'} for pg in original]}
if args.output: Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
