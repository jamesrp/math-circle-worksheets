#!/usr/bin/env python3
"""Build a portable adult guide with Python 3 and a standard pdflatex install."""
from pathlib import Path
import argparse, os, shutil, subprocess, sys, tempfile
p=argparse.ArgumentParser()
p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
a=p.parse_args(); src=Path(__file__).resolve().parent; out=a.out.resolve()
out.mkdir(parents=True,exist_ok=True)
subprocess.run([sys.executable,str(src/'check_math.py')],check=True)
with tempfile.TemporaryDirectory(prefix='guide-build-',dir=out) as td:
    work=Path(td)
    for f in src.iterdir():
        if f.is_file() and f.suffix in ('.tex','.sty','.png','.pdf','.jpg'):
            shutil.copy2(f,work/f.name)
    env=dict(os.environ,TEXMFVAR=str(work/'texmf-var'),TEXMFCONFIG=str(work/'texmf-config'))
    dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
    if dist and Path(dist).is_dir() and not subprocess.run(['kpsewhich','article.cls'],capture_output=True,text=True).stdout.strip():
        for key,sub in [('TEXINPUTS','tex'),('TFMFONTS','fonts/tfm'),('T1FONTS','fonts/type1'),('ENCFONTS','fonts/enc'),('TEXFONTMAPS','fonts/map')]:
            env[key]='.:'+str(Path(dist)/sub)+'//:'
    if not subprocess.run(['kpsewhich','pdflatex.fmt'],env=env,capture_output=True,text=True).stdout.strip():
        r=subprocess.run(['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex','pdflatex.ini'],cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if r.returncode: print(r.stdout); raise SystemExit(r.returncode)
        env['TEXFORMATS']=str(work)+':'
    for _ in range(2):
        r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','facilitator.tex'],cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if r.returncode: print(r.stdout); raise SystemExit(r.returncode)
    shutil.copy2(work/'facilitator.pdf',out/'facilitator.pdf')
    shutil.copy2(work/'facilitator.log',out/'guide-build.log')
print(out/'facilitator.pdf')
