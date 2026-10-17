#!/usr/bin/env python3
"""Build the three portable Week 85 writer PDFs with fixed metadata."""
import argparse, os, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, default=ROOT.parent)
    ap.add_argument('--work', type=Path, default=ROOT.parent/'build')
    a=ap.parse_args(); a.out.mkdir(parents=True,exist_ok=True); a.work.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,str(ROOT/'generate.py')],check=True)
    subprocess.run([sys.executable,str(ROOT/'check_math.py')],check=True)
    latex=shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
    env=dict(os.environ,SOURCE_DATE_EPOCH='1792195200',FORCE_SOURCE_DATE='1')
    for name in ('shared','upper','materials'):
        with tempfile.TemporaryDirectory(prefix=name+'-',dir=a.work.resolve()) as d:
            shutil.copy2(ROOT/(name+'.tex'),Path(d)/(name+'.tex'))
            for _ in range(2):
                p=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=d,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                (a.work/(name+'.log')).write_text(p.stdout)
                if p.returncode or 'Overfull' in p.stdout: raise SystemExit(p.stdout[-7000:])
            shutil.copy2(Path(d)/(name+'.pdf'),a.out/(name+'.pdf'))
    print('Built shared.pdf, upper.pdf, materials.pdf')
if __name__=='__main__': main()
