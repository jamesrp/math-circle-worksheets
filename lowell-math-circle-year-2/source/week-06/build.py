#!/usr/bin/env python3
"""Portable build of the Week 6 student packets and adult guide; intermediates stay temporary.

    python3 build.py --out output

The student packets are built from the problem files (week.toml, templates/, problems/,
src/common.tex) with the problem-file tools, found in tools/ in the portable ZIP or in
../problem-files/ in the repository. The guide's answer checks then read each packet's
LaTeX as built. The repository build, which also publishes the route packets, menu and
problem list, is build.sh.
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
for tools in (BASE / 'tools', BASE.parent / 'problem-files'):
    if (tools / 'build.py').exists():
        break
else:
    sys.exit('Cannot find the problem-file tools (build.py) in tools/ or ../problem-files/; see README.md.')

p = argparse.ArgumentParser()
p.add_argument('--out', default='output')
a = p.parse_args()
out = Path(a.out).resolve()
out.mkdir(parents=True, exist_ok=True)


def run(args, cwd):
    r = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode:
        raise RuntimeError(r.stdout)


with tempfile.TemporaryDirectory(prefix='worksheet-build-') as tmp:
    work = Path(tmp)
    for name in ['src', 'guide-src']:
        shutil.copytree(BASE / name, work / name)
    run([sys.executable, str(tools / 'build.py'), str(BASE), '--out', str(work / 'views'), '--tex'], work)
    for name in ['k-1', 'grades-2-3', 'grades-4-5']:
        shutil.copy2(work / 'views' / f'{name}.tex', work / 'src' / f'{name}.tex')
        shutil.copy2(work / 'views' / f'{name}.pdf', out / f'week-06-{name}.pdf')
    run([sys.executable, 'check_guide.py'], work / 'guide-src')
    for _ in range(2):
        run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'facilitator.tex'], work / 'guide-src')
    shutil.copy2(work / 'guide-src' / 'facilitator.pdf', out / 'week-06-facilitator.pdf')
print('Built four PDFs; physical rehearsal and classroom piloting remain unperformed.')
