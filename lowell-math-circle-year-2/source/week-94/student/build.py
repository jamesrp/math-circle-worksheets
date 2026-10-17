#!/usr/bin/env python3
"""Build the three packets; usage: python3 build.py OUTPUT_DIRECTORY.
Requires pdflatex (TeX Live with TikZ and Latin Modern) on PATH.
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path)
args = parser.parse_args()
source = Path(__file__).resolve().parent
output = args.output.resolve()
output.mkdir(parents=True, exist_ok=True)
build = output / '.build'
build.mkdir(exist_ok=True)
engine = shutil.which('pdflatex')
if not engine:
    raise SystemExit('pdflatex is required on PATH (TeX Live with TikZ and Latin Modern).')
env = os.environ.copy()
env['SOURCE_DATE_EPOCH'] = '1792195200'
env['FORCE_SOURCE_DATE'] = '1'
for tex in source.glob('*.tex'):
    shutil.copy2(tex, build / tex.name)
for name in ['k-1', 'grades-2-3', 'grades-4-5']:
    result = subprocess.run([engine, '-interaction=nonstopmode', '-halt-on-error', name + '.tex'], cwd=build, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (build / (name + '.build.log')).write_text(result.stdout)
    if result.returncode:
        print(result.stdout)
        raise SystemExit(result.returncode)
    shutil.copy2(build / (name + '.pdf'), output / (name + '.pdf'))
    print(output / (name + '.pdf'))
