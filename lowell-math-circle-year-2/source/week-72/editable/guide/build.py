#!/usr/bin/env python3
"""Build the standalone adult guide; Python 3 and a normal pdfLaTeX install."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile
HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--out', type=Path, default=HERE.parent)
args = parser.parse_args()
out = args.out.resolve()
out.mkdir(parents=True, exist_ok=True)
subprocess.run(['python3', str(HERE/'check_math.py')], check=True)
with tempfile.TemporaryDirectory(prefix='guide-build-', dir=out) as name:
    work = Path(name)
    for source in HERE.iterdir():
        if source.is_file():
            shutil.copy2(source, work/source.name)
    for _ in range(2):
        result = subprocess.run(['pdflatex', '-halt-on-error', '-interaction=nonstopmode', 'facilitator.tex'], cwd=work, capture_output=True, text=True)
        if result.returncode:
            print(result.stdout)
            raise SystemExit(result.returncode)
    shutil.copy2(work/'facilitator.pdf', out/'facilitator.pdf')
    shutil.copy2(work/'facilitator.log', out/'guide-build.log')
print(out/'facilitator.pdf')
