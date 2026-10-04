"""Assemble the shared Week 2 library and check its numbering and print geometry."""
from pathlib import Path
import json
import re
from pypdf import PdfReader, PdfWriter
import pdfplumber

ROOT = Path(__file__).resolve().parents[3]
BUILD = ROOT / 'tmp/pdfs/week-02-shared'
OUT = ROOT / 'lowell-math-circle-year-2/week-02/week-02-shared.pdf'
MANIFEST = json.loads((ROOT / 'plans/week-02-shared-manifest.json').read_text())
EXPECTED_PROBLEMS = json.loads((ROOT / 'plans/week-02-shared-data.json').read_text())['student_pages']


def check(path, student=False):
    reader = PdfReader(path)
    found = set()
    for i, page in enumerate(reader.pages, 1):
        assert tuple(round(float(v)) for v in page.mediabox[2:]) == (612, 792)
        text = page.extract_text()
        assert len(text.strip()) > 80, (path, i, 'empty page')
        assert '\ufffd' not in text, (path, i, 'replacement glyph')
        if student:
            assert 'Shared collection' in text, (i, 'missing shared header')
            assert 'F02-S-v1' in text, (i, 'missing shared ID')
            for obsolete in ['Grades', 'K-1', 'Name:', 'Date:', 'Go further:']:
                assert obsolete not in text, (i, obsolete)
            numbers = re.findall(r'Problem\s+(\d+)(?:\s*\(continued\))?\s*:', text)
            assert numbers, (i, 'missing numbered problem')
            assert list(map(int, numbers)) == EXPECTED_PROBLEMS[i - 1], (i, numbers)
            found.update(map(int, numbers))
    with pdfplumber.open(path) as doc:
        for i, page in enumerate(doc.pages, 1):
            for char in page.chars:
                if char['text'].strip():
                    assert 24 <= char['x0'] <= char['x1'] <= 588 and 20 <= char['top'] <= char['bottom'] <= 775, (path, i, char)
    if student:
        assert len(reader.pages) == MANIFEST['pages']
        assert found == set(range(1, MANIFEST['problems'] + 1)), sorted(found)
    return len(reader.pages)


def main():
    writer = PdfWriter()
    expected = 1
    for section in MANIFEST['sections']:
        assert section['first_page'] == expected
        start, end = section['slice']
        reader = PdfReader(BUILD / section['file'])
        assert end <= len(reader.pages), section
        writer.append(reader, pages=(start, end), outline_item=section['title'])
        expected += end - start
    assert expected - 1 == MANIFEST['pages']
    writer.add_metadata({'/Title': 'Week 2 / Lamps, paths, and rooms / Shared collection',
                         '/Author': 'Bellingham Math Circle',
                         '/Subject': '50 investigations; choose by interest and readiness'})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('wb') as output:
        writer.write(output)
    print(f'Built and structurally checked {OUT}: {check(OUT, student=True)} pages')


if __name__ == '__main__':
    main()
