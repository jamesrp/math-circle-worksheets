#!/usr/bin/env python3
"""Portable Week 55 student build. Intermediates never enter the source folder."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
out = args.out.resolve()
out.mkdir(parents=True, exist_ok=True)
env = dict(os.environ, SOURCE_DATE_EPOCH='1791072000', FORCE_SOURCE_DATE='1')
with tempfile.TemporaryDirectory(prefix='week55-build-', dir=out) as work:
    work = Path(work)
    shutil.copy2(ROOT / 'students.tex', work / 'students.tex')
    for _ in range(2):
        p = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            '-file-line-error', 'students.tex'], cwd=work, env=env,
                           capture_output=True, text=True)
        if p.returncode:
            raise RuntimeError(p.stdout[-10000:] + p.stderr)
    log = (work / 'students.log').read_text()
    if 'Overfull' in log:
        raise RuntimeError('Overfull box in build log')
    shutil.copy2(work / 'students.pdf', out / 'students.pdf')
print(out / 'students.pdf')
