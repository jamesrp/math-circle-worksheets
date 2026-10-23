#!/usr/bin/env python3
"""Build the student packet. Requires Python 3.11+ and pdflatex/TikZ.

students.tex is written from the problem files by regenerate.py, which this script
runs first unless --no-regenerate is given (the package's root build.py regenerates
in place, then builds a copy)."""
import argparse, pathlib, shutil, subprocess, sys, tempfile
HERE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser(); p.add_argument('--out',type=pathlib.Path,default=HERE.parent)
p.add_argument('--no-regenerate',action='store_true',help='compile students.tex as it is')
a=p.parse_args(); out=a.out.resolve(); out.mkdir(parents=True,exist_ok=True)
if not a.no_regenerate:
    subprocess.run([sys.executable,str(HERE/'regenerate.py')],check=True)
with tempfile.TemporaryDirectory(prefix='worksheet-',dir=out) as t:
    tmp=pathlib.Path(t)
    for source in HERE.iterdir():
        if source.is_file(): shutil.copy2(source,tmp/source.name)
    for _ in range(2):
        run=subprocess.run(['pdflatex','-halt-on-error','-interaction=nonstopmode','students.tex'],cwd=tmp,capture_output=True,text=True)
        if run.returncode:
            print(run.stdout); raise SystemExit(run.returncode)
    shutil.copy2(tmp/'students.pdf',out/'students.pdf')
    shutil.copy2(tmp/'students.log',out/'build.log')
print(out/'students.pdf')
