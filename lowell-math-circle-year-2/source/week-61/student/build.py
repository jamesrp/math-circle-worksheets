#!/usr/bin/env python3
"""Build students.pdf in a supplied output directory; never pollute source."""
from pathlib import Path
import argparse, shutil, subprocess, sys
sys.dont_write_bytecode=True
from geometry import write_figures

p=argparse.ArgumentParser();p.add_argument('output_directory');args=p.parse_args()
source=Path(__file__).resolve().parent
out=Path(args.output_directory).expanduser().resolve();work=out/'build'
work.mkdir(parents=True,exist_ok=True)
write_figures(work/'figures.tex')
for _ in range(2):
    result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
        '-jobname=students','-output-directory='+str(work),str(source/'students.tex')],
        cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (work/'console.log').write_text(result.stdout)
    if result.returncode: raise SystemExit(result.stdout)
shutil.copy2(work/'students.pdf',out/'students.pdf')
print(out/'students.pdf')
