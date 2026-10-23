#!/usr/bin/env python3
"""Build the owned Week WEEK PDFs and run the independent finite checks."""
import argparse, os, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
WEEK=96
TARGETS=[('student','grades-2-3'),('student','grades-4-5'),('guide','facilitator')]
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--out',type=Path,default=ROOT/'out')
 ap.add_argument('--work',type=Path)
 args=ap.parse_args(); out=args.out.resolve(); out.mkdir(parents=True,exist_ok=True)
 repo=ROOT.parents[2] if len(ROOT.parents)>2 else ROOT
 work=(args.work or (repo/'tmp/pdf-builds' if (repo/'AGENTS.md').exists() else ROOT/'tmp')).resolve()
 work.mkdir(parents=True,exist_ok=True)
 latex=shutil.which('pdflatex') or ('/Library/TeX/texbin/pdflatex' if Path('/Library/TeX/texbin/pdflatex').exists() else None)
 if not latex:raise SystemExit('Install TeX Live with pdfLaTeX, TikZ, geometry, fancyhdr and standard fonts.')
 env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
 result=subprocess.run([sys.executable,str(ROOT/'check_math.py')],text=True,capture_output=True,env=env)
 (work/f'week-{WEEK}-math.txt').write_text(result.stdout+result.stderr)
 if result.returncode:raise SystemExit(result.stdout+result.stderr)
 with tempfile.TemporaryDirectory(prefix=f'week-{WEEK}-',dir=work) as temp:
  for kind,name in TARGETS:
   folder=Path(temp)/kind; folder.mkdir(exist_ok=True)
   for source in (ROOT/kind).iterdir():
    if source.is_file() and source.suffix in ('.tex','.sty','.cls'):shutil.copy2(source,folder/source.name)
   for _ in range(2):
    run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=folder,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (work/f'week-{WEEK}-{name}-build.log').write_text(run.stdout)
    if run.returncode:raise SystemExit(run.stdout[-6000:])
   if 'Overfull' in run.stdout:raise SystemExit('Overfull content in '+name)
   shutil.copy2(folder/(name+'.pdf'),out/f'week-{WEEK}-{name}.pdf')
 print(f'PASS: Week {WEEK}; {len(TARGETS)} PDFs; mathematical checks passed.')
if __name__=='__main__':main()
