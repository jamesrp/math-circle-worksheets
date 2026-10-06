#!/usr/bin/env python3
"""Portable adult-guide build with Python 3 and ordinary pdfLaTeX."""
import argparse,subprocess,tempfile,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--output',default=str(ROOT.parent/'facilitator.pdf'));a=p.parse_args()
out=Path(a.output).resolve();out.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='week65-guide-') as t:
 w=Path(t);shutil.copy2(ROOT/'facilitator.tex',w/'facilitator.tex')
 for _ in range(2):
  r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=w,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  if r.returncode:print(r.stdout);raise SystemExit(r.returncode)
 shutil.copy2(w/'facilitator.pdf',out)
 print(out)
