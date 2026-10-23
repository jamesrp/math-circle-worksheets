#!/usr/bin/env python3
"""Week 90: measure printed cell, piece and ring sizes in the delivered PDFs (PyMuPDF).
Finds the repository from its own location; writes check_scale.py.out beside itself."""
from pathlib import Path
from collections import Counter
import pymupdf as fitz
HERE = Path(__file__).resolve().parent
def find_repo(here):
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file():
        return here.parents[3]
    for p in [here, *here.parents]:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repo not found')
REPO = find_repo(HERE)
W = REPO / 'lowell-math-circle-year-2' / 'week-90'
out = []
MM = 72 / 25.4
for name in ['students', 'materials']:
    doc = fitz.open(W / f'week-90-{name}.pdf')
    for i, page in enumerate(doc, 1):
        sizes = Counter()
        for d in page.get_drawings():
            r = d['rect']
            w, h = r.width / MM, r.height / MM
            if w > 3 and abs(w - h) < 0.3:
                sizes[(round(w, 1), round(h, 1))] += 1
        out.append(f'{name} p{i} page {page.rect.width/MM:.1f}x{page.rect.height/MM:.1f} mm; square items (mm): ' + ', '.join(f'{k[0]}x{k[1]}:{v}' for k, v in sorted(sizes.items())))
text = '\n'.join(out) + '\n'
(HERE / 'check_scale.py.out').write_text(text)
print(text)
