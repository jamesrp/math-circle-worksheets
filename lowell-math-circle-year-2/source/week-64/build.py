#!/usr/bin/env python3
"""Build all Week64 PDFs without repository paths or network access."""
import argparse,shutil,subprocess,tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--out',default='output');args=p.parse_args()
out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
if not shutil.which('pdflatex'):raise SystemExit('Install TeX Live or MacTeX with TikZ before rebuilding.')
with tempfile.TemporaryDirectory(prefix='week64-rebuild-') as td:
 td=Path(td)
 for kind in ['student','guide']:
  src=td/kind;shutil.copytree(BASE/kind,src)
  result=subprocess.run(['bash','build.sh'],cwd=src,capture_output=True,text=True)
  if result.returncode:
   print(result.stdout);print(result.stderr);raise SystemExit(f'{kind} build failed')
  built=td/'students.pdf' if kind=='student' else src/'facilitator.pdf'
  target=out/('week-64-students.pdf' if kind=='student' else 'week-64-facilitator.pdf')
  shutil.copy2(built,target);print(target)
