#!/usr/bin/env python3
"""Digital page/geometry audit; requires PyMuPDF. This is not a physical pretest."""
from pathlib import Path
import itertools
import json
import math
import sys
import pymupdf

source = Path(__file__).resolve().parent
pdf = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else source.parent / 'return-visit.pdf'
render = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else source.parent / 'render'
render.mkdir(parents=True, exist_ok=True)
document = pymupdf.open(pdf)
assert len(document) == 3
mm_per_pt = 25.4/72
results = []
for i,page in enumerate(document, 1):
    assert page.rect == pymupdf.Rect(0,0,612,792)
    text = page.get_text()
    assert 'Week 4 / Stars-and-wheels return visits / Grades 2–5' in text
    assert f'Problem {i}:' in text
    assert 'Bellingham Math Circle / Week 4 / F04-RV-v1' in text
    assert text.rstrip().endswith(str(i))
    for block in page.get_text('blocks'):
        assert block[0] >= 25 and block[1] >= 20 and block[2] <= 590 and block[3] <= 774, block
    working = []
    records = []
    for drawing in page.get_drawings():
        rect = drawing['rect']
        width, height = rect.width*mm_per_pt, rect.height*mm_per_pt
        if len(drawing['items']) != 4 or not all(item[0] == 'c' for item in drawing['items']):
            continue
        if abs(width-21) < 0.03 and abs(height-21) < 0.03:
            working.append(((rect.x0+rect.x1)/2, (rect.y0+rect.y1)/2))
        if abs(width-7) < 0.03 and abs(height-7) < 0.03:
            records.append(((rect.x0+rect.x1)/2, (rect.y0+rect.y1)/2))
    assert len(working) == (12 if i < 3 else 6), (i, working)
    center = tuple(sum(point[k] for point in working)/len(working) for k in range(2))
    radii = [math.dist(center,point)*mm_per_pt for point in working]
    expected_radius = 46 if i < 3 else 26.5
    assert all(abs(radius-expected_radius) < 0.03 for radius in radii), radii
    closest = min(math.dist(a,b)*mm_per_pt for a,b in itertools.combinations(working,2))
    expected_closest = 2*46*math.sin(math.pi/12) if i<3 else 26.5
    assert abs(closest-expected_closest) < 0.03
    if i == 3:
        assert len(records) == 36
    page.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(render/f'page-{i}.png')
    results.append({'page': i, 'working_slots': len(working), 'working_diameter_mm': 21,
                    'minimum_center_distance_mm': closest, 'edge_gap_mm': closest-21,
                    'record_slots': len(records) if i==3 else 0, 'text_inside_letter': True})
(source/'page-checks.json').write_text(json.dumps(results, indent=2)+'\n')
print('PASS: all three Letter pages, headers/footers, text bounds, physical slot geometry, and render generation.')
