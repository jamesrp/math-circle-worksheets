#!/usr/bin/env python3
"""Render every guide page and compare a copied-source rebuild.

PyMuPDF is a QA dependency only. Mathematical verification uses verify.py.
"""
import argparse
import json
from pathlib import Path
import pymupdf

p = argparse.ArgumentParser()
p.add_argument('pdf', type=Path)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--compare', type=Path)
args = p.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
d = pymupdf.open(args.pdf)
assert len(d) == 10, len(d)
other = pymupdf.open(args.compare) if args.compare else None
if other:
    assert len(other) == len(d)
report = []
for i, page in enumerate(d):
    assert (page.rect.width, page.rect.height) == (612, 792)
    text = page.get_text()
    assert 'Week 62 / Conflict networks / Adult guide' in text
    assert 'Bellingham Math Circle / Week 62 / W62-FAC-v1' in text
    assert '\ufffd' not in text
    spans = [s for b in page.get_text('dict')['blocks'] if b['type'] == 0
             for ln in b['lines'] for s in ln['spans'] if s['text'].strip()]
    assert all(s['bbox'][0] >= 35 and s['bbox'][2] <= 577 for s in spans)
    assert all(s['bbox'][1] >= 18 and s['bbox'][3] <= 770 for s in spans)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False)
    pix.save(args.out/f'page-{i+1:02d}.png')
    row = {'page': i+1, 'dimensions': [612, 792], 'span_bounds_pass': True}
    if other:
        second = other[i]
        assert text == second.get_text(), ('text', i+1)
        assert page.rect == second.rect, ('dimensions', i+1)
        p2 = second.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False)
        assert pix.samples == p2.samples, ('pixels', i+1)
        row.update(text_equal=True, dimensions_equal=True, pixels_equal=True)
    report.append(row)
(args.out/'checks.json').write_text(json.dumps(report, indent=2)+'\n')
(args.out/'facilitator.txt').write_text('\n\f\n'.join(p.get_text() for p in d))
print(f'PASS: {len(d)} US Letter pages rendered; text/bounds checked'
      + ('; every copied-source rebuild page equal in text, dimensions and pixels.' if other else '.'))
