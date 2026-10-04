#!/usr/bin/env python3
"""Portable guide build, with all intermediates outside source."""
from pathlib import Path
import shutil
import subprocess
import sys

source = Path(__file__).resolve().parent
if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 build.py OUTPUT_DIRECTORY')
output = Path(sys.argv[1]).resolve()
if output == source or source in output.parents:
    raise SystemExit('Output directory must be outside guide-src')
output.mkdir(parents=True, exist_ok=True)
work = output / '.guide-build'
work.mkdir(exist_ok=True)
cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
       '-output-directory=' + str(work), str(source / 'facilitator.tex')]
for _ in range(2):
    run = subprocess.run(cmd, cwd=source, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if run.returncode:
        print(run.stdout)
        raise SystemExit(run.returncode)
log = (work / 'facilitator.log').read_text()
if 'Overfull' in log:
    raise SystemExit('Overfull TeX box; inspect ' + str(work / 'facilitator.log'))
shutil.copyfile(work / 'facilitator.pdf', output / 'facilitator.pdf')
print(output / 'facilitator.pdf')
