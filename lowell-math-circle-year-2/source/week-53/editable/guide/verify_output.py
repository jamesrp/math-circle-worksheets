"""Check guide text/bounds; optionally compare an independent clean rebuild."""
import argparse
import hashlib
import json
from pathlib import Path
import pymupdf

EXPECTED = [
    'Mathematical overview: the destination',
    'Preparation, staffing and launch',
    'Complete small-map keys:',
    'Fixed-input swaps and forced choices:',
    'Inverse design and enumeration:',
    'Loops and local tests:',
    'From local tests to all competitors',
    'Source evidence, authorship and use limits',
]

def inspect(file):
    doc = pymupdf.open(file)
    assert len(doc) == 8, len(doc)
    pages = []
    for i,page in enumerate(doc):
        text = page.get_text()
        assert EXPECTED[i] in text, (i+1,EXPECTED[i])
        assert 'Week 53 / Connecting networks / Facilitator' in text
        assert 'W53-guide-v1' in text
        assert tuple(page.rect) == (0.,0.,612.,792.), page.rect
        spans = [s for b in page.get_text('dict')['blocks'] if b['type']==0
                 for l in b['lines'] for s in l['spans']]
        assert all(s['bbox'][0] >= 36 and s['bbox'][2] <= 576
                   and s['bbox'][1] >= 25 and s['bbox'][3] <= 775 for s in spans), i+1
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False)
        pages.append({'page':i+1,'size':list(page.rect),
                      'text':text,'pixel_sha256':hashlib.sha256(pix.samples).hexdigest()})
    alltext = '\n'.join(p['text'] for p in pages)
    for needle in ['1956','2140','4096','no bridges','37.5 mm','51.0 mm',
                   'unperformed','Exercise 15','Creative Problem 33']:
        assert needle in alltext, needle
    return pages

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf',type=Path)
    parser.add_argument('--compare',type=Path)
    parser.add_argument('--report',type=Path,required=True)
    args = parser.parse_args()
    pages = inspect(args.pdf)
    if args.compare:
        comparison = inspect(args.compare)
        assert pages == comparison, 'Text, page dimensions or 144-dpi pixels differ'
    output = {'pdf':str(args.pdf),'pages':len(pages),'all_bounds_pass':True,
        'compared':str(args.compare) if args.compare else None,
        'text_dimensions_pixels_match':True if args.compare else None,
        'page_checks':[{k:v for k,v in p.items() if k!='text'} for p in pages]}
    args.report.parent.mkdir(parents=True,exist_ok=True)
    args.report.write_text(json.dumps(output,indent=2)+'\n')
    print('PASS: eight Letter pages, required text and bounds' +
          ('; exact clean-rebuild text/dimensions/144-dpi pixels' if args.compare else ''))

if __name__ == '__main__':
    main()
