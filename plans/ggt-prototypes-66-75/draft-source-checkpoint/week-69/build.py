#!/usr/bin/env python3
"""Build the standalone student packet; requires Python 3 and pdflatex."""
from pathlib import Path
import argparse, subprocess, shutil, tempfile, os
p=argparse.ArgumentParser(); p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent)
a=p.parse_args(); src=Path(__file__).resolve().parent; out=a.out.resolve(); out.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='latex-', dir=out) as td:
    build=Path(td)
    for f in src.iterdir():
        if f.is_file() and f.suffix in ('.tex','.sty','.png','.pdf','.jpg'):
            shutil.copy2(f,build/f.name)
    env=dict(os.environ, TEXMFVAR=str(build/'texmf-var'), TEXMFCONFIG=str(build/'texmf-config'))
    # Some minimal TeX Live installations omit ls-R and prebuilt formats.
    # Discover the installed distribution instead of relying on a machine path.
    dist=subprocess.check_output(['kpsewhich','-var-value=TEXMFDIST'],text=True).strip()
    if dist and Path(dist).is_dir() and not subprocess.run(['kpsewhich','article.cls'],capture_output=True,text=True).stdout.strip():
        for key,sub in [('TEXINPUTS','tex'),('TFMFONTS','fonts/tfm'),('T1FONTS','fonts/type1'),('ENCFONTS','fonts/enc'),('TEXFONTMAPS','fonts/map')]:
            env[key]='.:'+str(Path(dist)/sub)+'//:'
    if not subprocess.run(['kpsewhich','pdflatex.fmt'],env=env,capture_output=True,text=True).stdout.strip():
        result=subprocess.run(['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex','pdflatex.ini'],cwd=build,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if result.returncode: print(result.stdout); raise SystemExit(result.returncode)
        env['TEXFORMATS']=str(build)+':'
    for _ in range(2):
        result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','students.tex'],cwd=build,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if result.returncode:
            print(result.stdout); raise SystemExit(result.returncode)
    shutil.copy2(build/'students.pdf',out/'students.pdf')
    shutil.copy2(build/'students.log',out/'build.log')
print(out/'students.pdf')
