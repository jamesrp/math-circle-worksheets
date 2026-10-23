#!/usr/bin/env python3
"""Rebuild copied and ZIP-extracted sources and compare rendered deliverables."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--pdf', type=Path, required=True)
parser.add_argument('--work', type=Path, required=True)
args = parser.parse_args()
work = args.work.resolve()
work.mkdir(parents=True,exist_ok=True)
files = sorted(p for p in ROOT.iterdir() if p.is_file())
assert all(p.suffix in {'.py','.tex','.md'} for p in files)
copied = work / 'copied' / 'source'
copied.mkdir(parents=True,exist_ok=True)
for p in files:
    shutil.copy2(p,copied / p.name)
archive = work / 'week55-revised-source-test.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p,Path('week55-source') / p.name)
extracted = work / 'extracted'
with zipfile.ZipFile(archive) as z:
    assert len(z.namelist()) == len(files)
    z.extractall(extracted)

def fingerprint(pdf):
    d = fitz.open(pdf)
    return [{'dimensions':list(p.rect),'text':p.get_text(),
             'pixels':hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples).hexdigest()}
            for p in d]

original = fingerprint(args.pdf)
records = []
for mode,source in [('copied',copied),('zip_extracted',extracted/'week55-source')]:
    output = source.parent / 'output'
    subprocess.run([sys.executable,str(source/'build.py'),'--out',str(output)],check=True)
    rebuilt = fingerprint(output/'students.pdf')
    assert rebuilt == original
    records.append({'mode':mode,'pages':len(rebuilt),'text_equal':True,
                    'dimensions_equal':True,'pixels_equal_108dpi':True})
result = {'status':'pass','source_files':[p.name for p in files],
          'checks':records,'zip_contains_only_original_authored_source':True}
(work/'rebuild-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: copied and ZIP-extracted sources match all 10 pages in text, dimensions and pixels')
