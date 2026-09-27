"""Independent print checks. Image review is still required.

Checks all page character boxes and family prose against the editable source.
The JSON report deliberately retains unmatched fields for human adjudication.
"""
from pathlib import Path
import hashlib
import json
import re
import unicodedata

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'tmp/pdfs/atlas'


def normalized(text):
    text = unicodedata.normalize('NFKC', text)
    text = text.translate(str.maketrans({'−':'-', '–':'-', '—':'-', '‑':'-',
                                       '‘':"'", '’':"'", '“':'"', '”':'"'}))
    return re.sub(r'[\s`*]', '', text).casefold()


def leaves(obj, prefix=''):
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield from leaves(value, f'{prefix}.{key}'.strip('.'))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            yield from leaves(value, f'{prefix}.{i}')
    elif isinstance(obj, str):
        yield prefix, obj


def inspect(path):
    reader = PdfReader(path)
    texts = []
    bad_boxes = []
    blank = []
    bad_chars = []
    with pdfplumber.open(path) as doc:
        for i, page in enumerate(doc.pages, 1):
            text = page.extract_text() or ''
            texts.append(text)
            if not text.strip():
                blank.append(i)
            for ch in page.chars:
                if (ch['x0'] < -0.5 or ch['x1'] > page.width+0.5
                        or ch['top'] < -0.5 or ch['bottom'] > page.height+0.5):
                    bad_boxes.append({'page':i, 'text':ch['text'],
                                      'box':[ch['x0'],ch['top'],ch['x1'],ch['bottom']]})
                if any(c in ch['text'] for c in ('\x00','\ufffd','\u25a0')):
                    bad_chars.append({'page':i,'text':ch['text']})
    uris = set()
    for page in reader.pages:
        for ref in page.get('/Annots', []):
            action = ref.get_object().get('/A', {})
            if action.get('/URI'):
                uris.add(str(action['/URI']))
    return dict(path=str(path.relative_to(ROOT)), pages=len(reader.pages),
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                blank_pages=blank, out_of_page_character_boxes=bad_boxes,
                suspect_characters=bad_chars, source_link_count=len(uris),
                texts=texts, uris=sorted(uris))


def main():
    reports = {}
    for key, name in [('plans','math-atlas-investigation-plans.pdf'),
                      ('map','math-atlas-research-map.pdf')]:
        path = ROOT/'lowell-math-circle-year-2/combined'/name
        result = inspect(path)
        text = normalized('\n'.join(result.pop('texts')))
        if key == 'plans':
            unmatched = []
            checked = 0
            for source in sorted((ROOT/'plans/atlas/families').glob('*.json')):
                for family in json.loads(source.read_text()):
                    for field, value in leaves(family):
                        if field == 'msc_primary' or field.startswith('msc_secondary'):
                            continue
                        if field == 'bridge.type':
                            continue  # A human-readable label is legitimate.
                        checked += 1
                        found = value in result['uris'] if field.endswith('.url') else normalized(value) in text
                        if not found:
                            unmatched.append({'family':family['id'],'field':field,'source':value})
            result['source_strings_checked'] = checked
            result['unmatched_source_fields'] = unmatched
        reports[key] = result
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'independent-print-check.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
    for key, report in reports.items():
        print(key, {k:v for k,v in report.items() if k not in ('uris','unmatched_source_fields')})
        if key == 'plans':
            print('Unmatched source fields:', len(report['unmatched_source_fields']))
    assert not any(r['blank_pages'] or r['out_of_page_character_boxes'] or r['suspect_characters'] for r in reports.values())
    assert not reports['plans']['unmatched_source_fields'], 'Source/PDF differences need review; see independent-print-check.json'


if __name__ == '__main__':
    main()
