#!/usr/bin/env python3
"""Build all four owned Week91 PDFs without external assets or private inputs."""
import argparse, os, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
NAMES=('students','return-visit','materials')
def main():
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--out',type=Path,default=ROOT/'out'); ap.add_argument('--work',type=Path); a=ap.parse_args()
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 repo=ROOT.parents[2] if len(ROOT.parents)>2 else ROOT
 work=(a.work or (repo/'tmp/pdf-builds' if (repo/'AGENTS.md').exists() else ROOT/'tmp')).resolve();work.mkdir(parents=True,exist_ok=True)
 latex=shutil.which('pdflatex') or ('/Library/TeX/texbin/pdflatex' if Path('/Library/TeX/texbin/pdflatex').exists() else None)
 if not latex:raise SystemExit('Install TeX Live/pdfLaTeX with the packages named in README.md.')
 env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1',W91_PDFLATEX=latex)
 check=subprocess.run([sys.executable,str(ROOT/'check_math.py')],env=env,text=True,capture_output=True)
 (work/'week-91-math.txt').write_text(check.stdout+check.stderr)
 if check.returncode:raise SystemExit(check.stdout+check.stderr)
 with tempfile.TemporaryDirectory(prefix='week-91-',dir=work) as t:
  t=Path(t)
  run=subprocess.run([sys.executable,str(ROOT/'student/generate.py'),str(t/'student')],env=env,text=True,capture_output=True)
  (work/'week-91-student-build.log').write_text(run.stdout+run.stderr)
  if run.returncode:raise SystemExit(run.stdout+run.stderr)
  for name in NAMES:
   emitted=t/'student/src'/f'{name}.tex'; snapshot=ROOT/'student'/f'{name}.tex'
   if emitted.read_bytes()!=snapshot.read_bytes():raise SystemExit(f'Stale generated snapshot: {snapshot}. See README.md to refresh.')
   log=(t/'student/src'/f'{name}-build.log').read_text()
   if 'Overfull' in log:raise SystemExit(f'Overfull content in {name}')
   shutil.copy2(t/'student'/f'{name}.pdf',out/f'week-91-{name}.pdf')
  g=t/'guide';g.mkdir();shutil.copy2(ROOT/'guide/facilitator.tex',g/'facilitator.tex')
  for _ in range(2):
   run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=g,env=env,text=True,capture_output=True)
   (work/'week-91-facilitator-build.log').write_text(run.stdout+run.stderr)
   if run.returncode:raise SystemExit(run.stdout+run.stderr)
  if 'Overfull' in run.stdout:raise SystemExit('Overfull content in facilitator')
  shutil.copy2(g/'facilitator.pdf',out/'week-91-facilitator.pdf')
 print('PASS: Week91, four PDFs; independent finite math and source-snapshot checks passed.')
if __name__=='__main__':main()
