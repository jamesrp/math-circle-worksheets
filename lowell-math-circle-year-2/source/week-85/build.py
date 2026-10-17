#!/usr/bin/env python3
"""Rebuild the owned Week WEEK PDFs; no private files or network needed."""
import argparse,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
WEEK=85
NAMES=['shared','upper','materials']
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'out');p.add_argument('--work',type=Path);p.add_argument('--verify-only',action='store_true');a=p.parse_args()
 subprocess.run([sys.executable,str(ROOT/'check_math.py')],check=True)
 if a.verify_only:return
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 repo=ROOT.parents[2] if len(ROOT.parents)>2 else ROOT
 work=(a.work or (repo/'tmp/pdf-builds' if (repo/'AGENTS.md').exists() else ROOT/'tmp')).resolve();work.mkdir(parents=True,exist_ok=True)
 latex=shutil.which('pdflatex') or ('/Library/TeX/texbin/pdflatex' if Path('/Library/TeX/texbin/pdflatex').exists() else None)
 if not latex:raise SystemExit('Install TeX Live/MacTeX with pdfLaTeX, TikZ, geometry, fancyhdr, AMS and Latin Modern.')
 env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
 with tempfile.TemporaryDirectory(prefix=f'week-{WEEK}-',dir=work) as td:
  temp=Path(td); studentout=temp/'student-pdfs';studentout.mkdir()
  shutil.copytree(ROOT/'student',temp/'student')
  run=subprocess.run([sys.executable,str(temp/'student'/'build.py'),'--out',str(studentout),'--work',str(temp/'student-work')],env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (work/f'week-{WEEK}-students-build.log').write_text(run.stdout)
  if run.returncode:raise SystemExit(run.stdout[-7000:])
  for name in NAMES:shutil.copy2(studentout/(name+'.pdf'),out/f'week-{WEEK}-{name}.pdf')
  folder=temp/'guide';folder.mkdir()
  for file in (ROOT/'guide').iterdir():
   if file.is_file() and file.suffix in ('.tex','.sty','.cls'):shutil.copy2(file,folder/file.name)
  for _ in range(2):
   run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=folder,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
   (work/f'week-{WEEK}-facilitator-build.log').write_text(run.stdout)
   if run.returncode or 'Overfull' in run.stdout:raise SystemExit(run.stdout[-7000:])
  shutil.copy2(folder/'facilitator.pdf',out/f'week-{WEEK}-facilitator.pdf')
 print(f'PASS: Week {WEEK}; {len(NAMES)+1} PDFs built; finite checks passed.')
if __name__=='__main__':main()
