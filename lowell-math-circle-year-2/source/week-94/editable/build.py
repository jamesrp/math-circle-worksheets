#!/usr/bin/env python3
"""Build Week 94 packets and facilitator guide deterministically.

student/*.tex are written from the problem files first (student/regenerate.py)."""
import argparse,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'out');p.add_argument('--work',type=Path,default=ROOT/'tmp');a=p.parse_args()
out=a.out.resolve();work=a.work.resolve();out.mkdir(parents=True,exist_ok=True);work.mkdir(parents=True,exist_ok=True)
engine=shutil.which('pdflatex')
if not engine and Path('/Library/TeX/texbin/pdflatex').exists():engine='/Library/TeX/texbin/pdflatex'
if not engine:raise SystemExit('Install pdfLaTeX with TikZ, Latin Modern, geometry, fancyhdr, array, amsmath/amssymb and hyperref.')
env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
# The student LaTeX is generated from the problem files (week.toml, template.tex, problems/).
subprocess.run([sys.executable,str(ROOT/'student'/'regenerate.py')],check=True,stdout=subprocess.DEVNULL)
with tempfile.TemporaryDirectory(prefix='week94-',dir=work) as t:
 temp=Path(t)
 for kind,names in [('student',['k-1','grades-2-3','grades-4-5']),('guide',['facilitator'])]:
  here=temp/kind;here.mkdir()
  for f in (ROOT/kind).glob('*.tex'):shutil.copy2(f,here/f.name)
  for name in names:
   for _ in range(2):
    r=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=here,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (work/(name+'.log')).write_text(r.stdout)
    if r.returncode:raise SystemExit(r.stdout[-6000:])
   if 'Overfull' in r.stdout:raise SystemExit('Overfull content; inspect '+str(work/(name+'.log')))
   shutil.copy2(here/(name+'.pdf'),out/('week-94-'+name+'.pdf'))
 check=subprocess.run([sys.executable,str(ROOT/'check_math.py')],cwd=temp,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (work/'math-check.txt').write_text(check.stdout)
 if check.returncode:raise SystemExit(check.stdout)
print('PASS: three Week 94 student PDFs, facilitator PDF and independent math checks.')
