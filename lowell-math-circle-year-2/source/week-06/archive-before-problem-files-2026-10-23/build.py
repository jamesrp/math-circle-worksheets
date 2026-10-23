#!/usr/bin/env python3
"""Portable build of the student packets and guide; intermediates stay temporary."""
import argparse, subprocess, shutil, tempfile, sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--out',default='output');a=p.parse_args()
out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='worksheet-build-') as tmp:
 work=Path(tmp)
 for name in ['src','guide-src']:shutil.copytree(BASE/name,work/name)
 def run(args,cwd):
  r=subprocess.run(args,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  if r.returncode:raise RuntimeError(r.stdout)
 for name in ['k-1','grades-2-3','grades-4-5']:
  for _ in range(2):run(['xelatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],work/'src')
  shutil.copy2(work/'src'/(name+'.pdf'),out/('week-06'+'-'+name+'.pdf'))
 run([sys.executable]+['check_guide.py'],work/'guide-src')
 for _ in range(2):run(['pdflatex','-interaction=nonstopmode','-halt-on-error','facilitator.tex'],work/'guide-src')
 shutil.copy2(work/'guide-src/facilitator.pdf',out/'week-06-facilitator.pdf')
print('Built four PDFs; physical rehearsal and classroom piloting remain unperformed.')
