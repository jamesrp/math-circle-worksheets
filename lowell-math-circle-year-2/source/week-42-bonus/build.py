#!/usr/bin/env python3
"""Build this standalone bonus packet and adult guide. No repository required."""
import argparse,subprocess,sys,shutil
from pathlib import Path
from guide_renderer import render
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'output');args=ap.parse_args()
out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
student_out=out/'student-build';student_out.mkdir(exist_ok=True)
subprocess.run([sys.executable,str(HERE/'student/build.py'),'--out',str(student_out)],check=True)
pdf=student_out/'bonus.pdf'
if not pdf.exists():raise RuntimeError('Student builder did not produce bonus.pdf')
shutil.copy(pdf,out/'week-42-bonus.pdf')
render(HERE/'guide.md',out/'week-42-bonus-facilitator.pdf',42,'Fair results from a bag')
print('Built week-42-bonus.pdf and week-42-bonus-facilitator.pdf in',out)
