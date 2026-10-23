#!/usr/bin/env python3
"""Clean copied-source and extracted-ZIP builds; compare both PDFs exactly.

Usage: python3 clean_rebuild.py OUTPUT_DIR QA_DIR
Requires pdflatex and PyMuPDF. Writes all evidence outside the source package.
"""
from pathlib import Path
import sys, zipfile, subprocess, json, hashlib, shutil
import pymupdf

src = Path(__file__).resolve().parent
delivered = Path(sys.argv[1]).resolve()
qa = Path(sys.argv[2]).resolve()
assert qa != src and src not in qa.parents, 'QA must be outside src'
qa.mkdir(parents=True, exist_ok=True)
members = [p for p in sorted(src.iterdir())
           if p.is_file() and p.suffix in ('.tex', '.py', '.sh', '.md', '.json')]
assert all(p.is_file() for p in src.iterdir()), 'Source package must stay lean'
archive = qa / 'revised-source-check.zip'
copied = qa / 'copied' / 'src'
extracted = qa / 'extracted'
if copied.parent.exists():
    shutil.rmtree(copied.parent)
if extracted.exists():
    shutil.rmtree(extracted)
copied.mkdir(parents=True)
for p in members:
    shutil.copy2(p, copied / p.name)
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in members:
        z.write(p, 'src/' + p.name)
with zipfile.ZipFile(archive) as z:
    assert z.namelist() == ['src/' + p.name for p in members]
    z.extractall(extracted)

def compare(output):
    report = {}
    for name in ('students', 'materials'):
        a = pymupdf.open(delivered / (name + '.pdf'))
        b = pymupdf.open(output / (name + '.pdf'))
        assert len(a) == len(b)
        digests = []
        for i, (pa, pb) in enumerate(zip(a, b)):
            assert pa.rect == pb.rect and pa.get_text() == pb.get_text(), (name, i+1, 'text/dimensions')
            xa = pa.get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3), alpha=False)
            xb = pb.get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3), alpha=False)
            assert xa.samples == xb.samples, (name, i+1, 'pixels')
            digests.append(hashlib.sha256(xa.samples).hexdigest())
        report[name] = dict(pages=len(a), text_equal=True,
                            dimensions_equal=True, pixels_equal=True,
                            pixel_sha256=digests)
    return report

report = {'source_members': [p.name for p in members],
          'comparison_scale': 1.3, 'builds': {}}
for label, source in [('copied_source', copied), ('extracted_zip', extracted / 'src')]:
    output = qa / (label + '-rebuilt')
    if output.exists():
        shutil.rmtree(output)
    subprocess.run(['sh', str(source / 'build.sh'), str(output)], check=True)
    report['builds'][label] = compare(output)
(qa / 'clean-rebuild-check.json').write_text(json.dumps(report, indent=2) + '\n')
print('Copied source and extracted lean ZIP each rebuilt both PDFs with identical text, dimensions and every rendered pixel.')
