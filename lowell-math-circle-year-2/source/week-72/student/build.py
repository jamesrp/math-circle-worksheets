#!/usr/bin/env python3
"""Build this self-contained student packet. Requires Python 3 and pdflatex/TikZ."""
import argparse, pathlib, shutil, subprocess, tempfile
HERE=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser(); p.add_argument('--out',type=pathlib.Path,default=HERE.parent)
a=p.parse_args(); out=a.out.resolve(); out.mkdir(parents=True,exist_ok=True)
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
