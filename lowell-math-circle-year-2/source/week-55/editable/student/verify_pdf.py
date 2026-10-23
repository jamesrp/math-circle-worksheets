#!/usr/bin/env python3
"""Check delivered text, card labels, counter-cell geometry and array labels."""
from pathlib import Path
import argparse
import hashlib
import json
import pymupdf as fitz

MM = 72 / 25.4
parser = argparse.ArgumentParser()
parser.add_argument('--pdf', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
parser.add_argument('--render', type=Path)
args = parser.parse_args()
doc = fitz.open(args.pdf)
assert len(doc) == 10

def size(rect, w, h):
    return abs(rect.width-w*MM)<.03 and abs(rect.height-h*MM)<.03

def labels(page, rect):
    return ' '.join(w[4] for w in page.get_text('words')
                    if rect.contains(fitz.Point((w[0]+w[2])/2,(w[1]+w[3])/2)))

card_values = {
    1:['1','4','0','3','0','2','1','3','0','2','1','4'],
    2:['0','1','2','0','1','2','0','1','3','0','1','3','0','1','2','0','3','6'],
    3:['']*24, 4:['']*18, 5:['0','3','6']+['']*16,
    6:['1','3','5','2','4','0','2','4','0','3','0','2','4','1','3','0','3','6','1','4'],
    7:['4','0','1','3','2','0','2','4','0','1','4','6','9'],
    8:['1','5','0','2','6'], 9:['1','4','0','2','5','8'], 10:[]}
lane_counts = [2,3,4,3,1,4,3,0,0,0]
pages = []
for number,page in enumerate(doc,1):
    assert tuple(page.rect) == (0,0,792,612)
    text = page.get_text()
    assert text.splitlines()[0] == 'Week 55 / Few sums and equal spacing / Grades 3–5'
    assert f'Problem {number}:' in text
    assert 'Bellingham Math Circle / Week 55 / W55-S-v2' in text
    assert text.splitlines()[-1] == str(number)
    assert 'Name' not in text and 'Date' not in text
    if number == 6:
        assert 'neighboring numbers in increasing order have the same difference' in text
        assert text.index('neighboring numbers') < text.index('Problem 6:')
    if number == 9:
        assert 'Card counts' in text and 'Substitute counts' in text
        assert text.index('Substitute counts') < text.index('Problem 9:')
        assert 'each input has at least' in text and 'one card.' in text
    if number == 10:
        assert 'Each input has at least two cards.' in text
    drawings = page.get_drawings()
    cells = [d['rect'] for d in drawings if size(d['rect'],12,18)]
    assert len(cells) == 19*lane_counts[number-1]
    cells.sort(key=lambda r:(round(r.y0,1),r.x0))
    for index,rect in enumerate(cells):
        assert labels(page,rect) == str(index % 19)
        assert rect.width*25.4/72 >= 11.99
    cards = [d['rect'] for d in drawings if size(d['rect'],13,14)]
    cards.sort(key=lambda r:(round(r.y0,1),r.x0))
    assert [labels(page,r) for r in cards] == card_values[number]
    circles = [d['rect'] for d in drawings if size(d['rect'],9,9)]
    if number == 8:
        circles.sort(key=lambda r:(round(r.y0,1),r.x0))
        # Top to bottom, then left to right: example grid, two task grids.
        expected = ['5','7','11','1','3','7',
                    '6','8','9','5','7','9','11',
                    '3','5','6','3','5','7','9',
                    '1','3','4','1','3','5','7']
        assert [labels(page,r) for r in circles] == expected
    for w in page.get_text('words'):
        assert w[0] >= 16*MM and w[2] <= page.rect.width-16*MM
        assert w[1] > 10*MM and w[3] < page.rect.height-5*MM
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
    if args.render:
        args.render.mkdir(parents=True,exist_ok=True)
        pix.save(args.render/f'page-{number:02}.png')
    pages.append({'page':number,'dimensions_points':list(page.rect),
                  'result_cells_12x18mm':len(cells),'input_slots_13x14mm':len(cards),
                  'grid_nodes':len(circles) if number == 8 else 0,
                  'render_108dpi_sha256':hashlib.sha256(pix.samples).hexdigest()})
result = {'status':'pass', 'pages':pages,
          'total_result_cells':sum(p['result_cells_12x18mm'] for p in pages),
          'visual_review':'Required separately: inspect every latest rendered page.',
          'physical_readiness':'Not rehearsed or classroom piloted.'}
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 10 headers/footers/problems; every printed input, lane and array value; 380 physical-size result cells')
