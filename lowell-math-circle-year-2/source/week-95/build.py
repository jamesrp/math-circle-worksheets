#!/usr/bin/env python3
"""Rebuild Week 95 students and guide with no private inputs or runtime downloads.

The student packets come from the problem files: week.toml, template.tex, figures.py
and problems/*.md. The problem-file tools (stdlib only) are read from tools/ in the
portable ZIP, or from ../problem-files/ in the repository."""
import argparse,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TOOLS=ROOT/'tools' if (ROOT/'tools').is_dir() else ROOT.parent/'problem-files'
sys.dont_write_bytecode=True
sys.path.insert(0,str(TOOLS))
import atoms
FILES={'K-1':'k-1','2-3':'grades-2-3','4-5':'grades-4-5'}
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'out');p.add_argument('--work',type=Path,default=ROOT/'tmp');a=p.parse_args()
out=a.out.resolve();work=a.work.resolve();out.mkdir(parents=True,exist_ok=True);work.mkdir(parents=True,exist_ok=True)
engine=shutil.which('pdflatex')
if not engine and Path('/Library/TeX/texbin/pdflatex').exists():engine='/Library/TeX/texbin/pdflatex'
if not engine:raise SystemExit('Install pdfLaTeX with TikZ, Latin Modern, geometry, fancyhdr, array, amsmath/amssymb and hyperref.')
with tempfile.TemporaryDirectory(prefix='week95-',dir=work) as t:
 temp=Path(t);students=temp/'student';students.mkdir()
 try:week=atoms.load_week(ROOT)
 except atoms.ProblemFileError as e:raise SystemExit(f'error: {e}')
 env=dict(os.environ,SOURCE_DATE_EPOCH='1760572800',FORCE_SOURCE_DATE='1',TZ='UTC')
 for band in week.bands:
  name=week.bands[band].get('file',FILES.get(band))
  (students/(name+'.tex')).write_text(atoms.student_tex(week,band))
  for _ in range(2):
   r=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-output-directory',str(students),str(students/(name+'.tex'))],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   (work/f'student-{name}-build.txt').write_text(r.stdout)
   if r.returncode:raise SystemExit(r.stdout[-6000:])
  if 'Overfull' in r.stdout:raise SystemExit('Overfull student content: '+name)
  shutil.copy2(students/(name+'.pdf'),out/('week-95-'+name+'.pdf'))
 guide=temp/'guide';guide.mkdir();shutil.copy2(ROOT/'guide/facilitator.tex',guide/'facilitator.tex')
 env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
 for _ in range(2):
  r=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=guide,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  (work/'guide-build.txt').write_text(r.stdout)
  if r.returncode:raise SystemExit(r.stdout[-6000:])
 if 'Overfull' in r.stdout:raise SystemExit('Overfull guide content')
 shutil.copy2(guide/'facilitator.pdf',out/'week-95-facilitator.pdf')
 for script,log in [(ROOT/'check_math.py','math-check.txt'),(ROOT/'student/verify.py','student-verify.txt')]:
  check=subprocess.run([sys.executable,str(script)],cwd=temp,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
  (work/log).write_text(check.stdout)
  if check.returncode:raise SystemExit(check.stdout)
print('PASS: two Week 95 student PDFs, facilitator PDF and independent math checks.')
