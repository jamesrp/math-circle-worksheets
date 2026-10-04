#!/usr/bin/env python3
"""Render all writer-stage pages and check their digital geometry.

Requires PyMuPDF. Geometry checks do not replace inspecting every PNG and do
not constitute a physical cube-fit rehearsal.
"""
from pathlib import Path
import json
import re
import pymupdf as fitz

HERE=Path(__file__).resolve().parent
PDF=HERE.parent/'return-visit.pdf'
OUT=HERE.parent/'render'
OUT.mkdir(exist_ok=True)
for previous in OUT.iterdir():
    if re.fullmatch(r'page-\d+\.(png|txt)', previous.name):
        previous.unlink()
doc=fitz.open(PDF)
assert len(doc)==3
MM=72/25.4
report={'pages':[], 'working_grid_cell_mm':25, 'physical_rehearsal':'untested',
        'classroom_piloting':'unpiloted'}
for i,page in enumerate(doc,1):
    assert abs(page.rect.width-612)<.01 and abs(page.rect.height-792)<.01
    text=page.get_text()
    assert 'Week 5 / Tower-city return visits / Grades 2–5' in text
    assert 'Bellingham Math Circle / Week 5 / F05-RV-v1' in text
    assert f'Problem {i}:' in text
    assert sum(f'Problem {j}:' in text for j in range(1,4))==1
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                rect=fitz.Rect(span['bbox'])
                assert rect.x0>=40 and rect.x1<=573 and rect.y0>=10 and rect.y1<=780, (i,span)
    squares=[]
    for drawing in page.get_drawings():
        items=drawing['items']
        rectangles=[fitz.Rect(item[1]) for item in items if item[0]=='re']
        # pdfTeX/TikZ sometimes emits a rectangle as four closed line segments.
        if (len(items)==4 and all(item[0]=='l' for item in items)
            and items[0][1]==items[-1][2]
            and all(abs(item[1].x-item[2].x)<.01 or abs(item[1].y-item[2].y)<.01 for item in items)):
            rectangles.append(fitz.Rect(drawing['rect']))
        for rect in rectangles:
            w,h=rect.width/MM,rect.height/MM
            if w>20 and abs(w-h)<.05:
                squares.append(round(w,3))
    # Outer working boards, not individual cell lines, are rectangle paths.
    if i==2:
        assert sum(abs(w-75)<.05 for w in squares)==1
        assert sum(abs(w-100)<.05 for w in squares)==1
    if i==3:
        assert sum(abs(w-75)<.05 for w in squares)==2
    image=OUT/f'page-{i}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(image)
    (OUT/f'page-{i}.txt').write_text(text)
    report['pages'].append({'page':i,'outer_square_side_mm':squares,'png':image.name})
(HERE.parent/'digital-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 3 Letter pages, all headers/footers, text bounds, 25 mm working grids; rendered all pages.')
