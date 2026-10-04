#!/usr/bin/env python3
"""Build both bonus PDFs without changing the supplied reference PDFs."""
from pathlib import Path
import argparse,os,shutil,subprocess,sys,json
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--out',default='build');args=ap.parse_args()
out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
meta=json.loads((root/'package.json').read_text());week=meta['week']
src=root/'student-src';sout=out/'student';sout.mkdir(exist_ok=True)
if (src/'build.py').exists():cmd=[sys.executable,str(src/'build.py'),str(sout)]
elif (src/'build.sh').exists():cmd=['bash',str(src/'build.sh'),str(sout)]
else:raise SystemExit('Missing portable student builder')
with (out/'student-build.log').open('w') as log:subprocess.run(cmd,cwd=src,stdout=log,stderr=subprocess.STDOUT,check=True)
shutil.copy2(sout/'bonus.pdf',out/f'week-{week:02}-bonus.pdf')
cmd=[sys.executable,str(root/'guide-src/build_guide.py'),str(root/'guide-src/guide.json'),str(out/f'week-{week:02}-bonus-facilitator.pdf')]
with (out/'guide-build.log').open('w') as log:subprocess.run(cmd,cwd=root,stdout=log,stderr=subprocess.STDOUT,check=True)
for f in sorted(out.glob('*.pdf')):print(f)
