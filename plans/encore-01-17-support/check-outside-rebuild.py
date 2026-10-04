#!/usr/bin/env python3
"""Rebuild a released package outside the repository and compare every PDF page.

Supplemental check for Weeks1–4, whose earlier clean extractions were inside tmp/.
Requires PyMuPDF. Never edits current PDFs, editable sources or ZIP packages.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
for arg in sys.argv[1:]:
    n = int(arg)
    week = f'week-{n:02}'
    archive = ROOT / f'lowell-math-circle-year-2/source/{week}-return-visit-source.zip'
    work = Path(tempfile.mkdtemp(prefix=f'{week}-root-outside-', dir='/tmp'))
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            p = Path(name)
            if p.is_absolute() or '..' in p.parts or '\\' in name:
                raise RuntimeError(f'Unsafe ZIP entry: {name}')
        z.extractall(work)
    source = work / f'{week}-return-visit'
    if not source.is_dir():
        source = work
    output = work / 'output'
    run = subprocess.run(['sh', str(source/'build.sh'), str(output)],
                         cwd='/tmp', capture_output=True, text=True)
    (work/'build-log.txt').write_text(run.stdout+'\n'+run.stderr)
    if run.returncode:
        raise RuntimeError(f'{week} outside build failed: {work}/build-log.txt')
    comparisons = []
    for suffix in ('', '-facilitator'):
        name = f'{week}-return-visit{suffix}.pdf'
        current = ROOT / f'lowell-math-circle-year-2/{week}/{name}'
        rebuilt = output / name
        a, b = pymupdf.open(current), pymupdf.open(rebuilt)
        assert len(a) == len(b)
        pages = []
        for i, (x,y) in enumerate(zip(a,b),1):
            same_text = x.get_text() == y.get_text()
            same_pixels = x.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).samples == y.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).samples
            assert same_text and same_pixels, (week, suffix, i)
            pages.append({'page':i, 'same_text':same_text, 'same_1_5x_pixels':same_pixels})
        comparisons.append({'file':str(current.relative_to(ROOT)),
                            'current_sha256':hashlib.sha256(current.read_bytes()).hexdigest(),
                            'rebuilt_sha256':hashlib.sha256(rebuilt.read_bytes()).hexdigest(),
                            'pages':pages})
    record = {'week':n, 'extraction':str(work), 'build_cwd':'/tmp',
              'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
              'comparisons':comparisons, 'physical_rehearsal':'untested'}
    (Path(__file__).parent/f'week-{n:02}-outside-rebuild.json').write_text(json.dumps(record,indent=2)+'\n')
    print(f'{week}: outside extraction/build passed; {sum(len(x["pages"]) for x in comparisons)} pages text/pixels equal')
