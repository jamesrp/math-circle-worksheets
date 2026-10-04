#!/usr/bin/env python3
"""Build bonus.pdf; python build.py [output-directory]. Set PDFLATEX if needed."""
from pathlib import Path
import os, shutil, subprocess, sys
src = Path(__file__).resolve().parent
out = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else src.parent
out.mkdir(parents=True, exist_ok=True)
build = out / 'build'
build.mkdir(exist_ok=True)
tex = os.environ.get('PDFLATEX') or shutil.which('pdflatex')
if not tex:
    raise SystemExit('pdflatex missing: put it on PATH or set PDFLATEX')
subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','-output-directory',str(build),str(src/'bonus.tex')], cwd=src, check=True, stdout=subprocess.DEVNULL)
shutil.copy2(build/'bonus.pdf',out/'bonus.pdf')
print(out/'bonus.pdf')
