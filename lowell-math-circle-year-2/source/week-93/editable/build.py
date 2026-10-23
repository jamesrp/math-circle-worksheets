#!/usr/bin/env python3
"""Rebuild this week's owned student and facilitator PDFs, then check its mathematics.

student/students.tex is written from the problem files first (student/regenerate.py)."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
WEEK=93

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'out')
    parser.add_argument('--work',type=Path)
    args=parser.parse_args()
    out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    repo=next((p for p in ROOT.parents if (p/'AGENTS.md').exists()),None)
    work=(args.work or (repo/'tmp/pdf-builds' if repo else ROOT/'tmp')).resolve()
    work.mkdir(parents=True,exist_ok=True)
    latex=shutil.which('pdflatex')
    if not latex and Path('/Library/TeX/texbin/pdflatex').is_file():latex='/Library/TeX/texbin/pdflatex'
    if not latex:raise SystemExit('Install pdfLaTeX with TikZ, geometry, fancyhdr, lmodern, amsmath and hyperref.')
    env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1',TZ='UTC')
    # The student LaTeX is generated from the problem files (week.toml, figures.py, problems/).
    subprocess.run([sys.executable,str(ROOT/'student'/'regenerate.py')],check=True,stdout=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory(prefix=f'week-{WEEK}-',dir=work) as name:
        temp=Path(name)
        for folder,stem in [('student','students'),('guide','facilitator')]:
            dest=temp/folder;shutil.copytree(ROOT/folder,dest)
            for _ in range(2):
                run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=dest,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                (work/f'week-{WEEK}-{stem}.log').write_text(run.stdout)
                if run.returncode:raise SystemExit(run.stdout[-7000:])
            if 'Overfull' in run.stdout:raise SystemExit(f'Overfull content in week-{WEEK}-{stem}.log')
            shutil.copy2(dest/(stem+'.pdf'),out/f'week-{WEEK}-{stem}.pdf')
        check=subprocess.run([sys.executable,str(ROOT/'check_math.py')],cwd=temp,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (work/f'week-{WEEK}-math-checks.json').write_text(check.stdout)
        if check.returncode:raise SystemExit(check.stdout)
    print(f'PASS Week {WEEK}: both PDFs built and exact mathematical checks passed.')

if __name__=='__main__':main()
