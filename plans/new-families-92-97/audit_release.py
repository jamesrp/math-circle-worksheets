#!/usr/bin/env python3
"""Audit released PDF geometry, archive membership, and local index targets.

Requires PyMuPDF. This records digital properties, not visual/classroom review.
Run from anywhere; output JSON goes to stdout. Build/visual checks are separate.
"""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
YEAR = ROOT / 'lowell-math-circle-year-2'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    results = {'pdfs': [], 'archives': [], 'index_links': []}
    failures = []
    for week in range(92, 98):
        pdfs = sorted((YEAR / f'week-{week}').glob('*.pdf'))
        if len(pdfs) < 2:
            failures.append(f'Week {week}: fewer than two released PDFs')
        for file in pdfs:
            doc = pymupdf.open(file)
            page_data = []
            for i, page in enumerate(doc):
                text = page.get_text()
                page_errors = []
                if abs(page.rect.width-612) > 0.2 or abs(page.rect.height-792) > 0.2:
                    page_errors.append('not US Letter')
                if not text.strip():
                    page_errors.append('empty text')
                for block in page.get_text('dict')['blocks']:
                    for line in block.get('lines', []):
                        for span in line['spans']:
                            x0,y0,x1,y1 = span['bbox']
                            if x0 < -0.5 or y0 < -0.5 or x1 > 612.5 or y1 > 792.5:
                                page_errors.append('text outside page')
                if '\ufffd' in text:
                    page_errors.append('replacement character')
                page_data.append({'page':i+1, 'text_characters':len(text), 'errors':sorted(set(page_errors))})
                failures += [f'{file.name} page {i+1}: {s}' for s in sorted(set(page_errors))]
            results['pdfs'].append({'path':str(file.relative_to(ROOT)), 'sha256':digest(file.read_bytes()),
                                    'pages':page_data})
        archives = sorted((YEAR/'source').glob(f'week-{week}*.zip'))
        if not archives:
            archives = sorted((YEAR/'source'/f'week-{week}').glob('*.zip'))
        if not archives:
            failures.append(f'Week {week}: no portable source archive')
        for file in archives:
            with zipfile.ZipFile(file) as z:
                items = [x for x in z.infolist() if not x.is_dir()]
                for item in items:
                    parts = Path(item.filename).parts
                    if Path(item.filename).is_absolute() or '..' in parts:
                        failures.append(f'{file.name}: unsafe archive path {item.filename}')
                    if any(part in ('.git','__pycache__','external-resources','.DS_Store') for part in parts):
                        failures.append(f'{file.name}: unwanted archive path {item.filename}')
                results['archives'].append({'path':str(file.relative_to(ROOT)),
                    'sha256':digest(file.read_bytes()), 'members':[x.filename for x in items]})
    index = YEAR/'WEEKS-92-97.md'
    if not index.is_file():
        failures.append('Missing release index WEEKS-92-97.md')
    else:
        for target in re.findall(r'\]\(([^)]+)\)', index.read_text()):
            if target.startswith(('http:', 'https:', '#', 'mailto:')):
                continue
            path = (index.parent/target.split('#')[0]).resolve()
            exists = path.exists()
            results['index_links'].append({'target':target,'exists':exists})
            if not exists:
                failures.append('Missing index target: '+target)
    results['failures'] = failures
    results['status'] = 'pass' if not failures else 'fail'
    print(json.dumps(results, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
