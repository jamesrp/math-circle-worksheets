#!/usr/bin/env python3
"""Build just the adult guide; standard Python and portable pdfLaTeX packages."""
import argparse
from pathlib import Path
import shutil
import subprocess

p = argparse.ArgumentParser()
p.add_argument('--out', type=Path, required=True)
args = p.parse_args()
src = Path(__file__).resolve().parent
out = args.out.resolve()
if out == src:
    raise SystemExit('Use a separate output directory to keep source lean.')
out.mkdir(parents=True, exist_ok=True)
shutil.copy2(src/'facilitator.tex', out/'facilitator.tex')
subprocess.run(['python3', str(src/'verify.py'), '--report', str(out/'math-checks.json')], check=True)
for _ in range(2):
    subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                    '-file-line-error', 'facilitator.tex'], cwd=out, check=True,
                   stdout=subprocess.DEVNULL)
log = (out/'facilitator.log').read_text(errors='replace')
if 'Overfull' in log:
    raise SystemExit('Overfull box detected; inspect facilitator.log.')
print(out/'facilitator.pdf')
