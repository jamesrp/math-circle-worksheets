#!/usr/bin/env python3
"""Usage: python3 build.py [output-directory]; needs pdflatex or PDFLATEX."""
from pathlib import Path
import os, shutil, subprocess, sys
here=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else here.parent
out.mkdir(parents=True,exist_ok=True)
tex=os.environ.get('PDFLATEX') or shutil.which('pdflatex')
if not tex: raise SystemExit('Install a TeX distribution or set PDFLATEX.')
build=out/'build'; build.mkdir(exist_ok=True)
subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error',f'-output-directory={build}',str(here/'bonus.tex')],cwd=here,check=True)
shutil.copy2(build/'bonus.pdf',out/'bonus.pdf')
