#!/usr/bin/env python3
"""Build the combined packet from students.tex, which regenerate.py writes from the
problem files. All intermediates stay in output/.build."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
sys.dont_write_bytecode=True


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--pdflatex',default='pdflatex')
    a=p.parse_args()
    out=a.output.resolve()
    out.mkdir(parents=True,exist_ok=True)
    work=out/'.build'
    work.mkdir(exist_ok=True)
    src=Path(__file__).resolve().parent
    # students.tex is generated from the problem files, map macros included;
    # regenerate it when they are present (not in a copy of this folder alone).
    if (src.parent/'problem-files'/'week.toml').exists() or (src.parent.parent/'week.toml').exists():
        subprocess.run([sys.executable,str(src/'regenerate.py')],check=True,stdout=subprocess.DEVNULL)
    shutil.copyfile(src/'students.tex',work/'students.tex')
    for _ in range(2):
        r=subprocess.run([a.pdflatex,'-interaction=nonstopmode','-halt-on-error','students.tex'],cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (work/'compile-console.txt').write_text(r.stdout)
        if r.returncode:
            raise RuntimeError(r.stdout[-6000:])
    log=(work/'students.log').read_text(errors='replace')
    if 'Overfull' in log:
        raise RuntimeError('Overfull TeX box: inspect students.log')
    shutil.copyfile(work/'students.pdf',out/'students.pdf')
    print(out/'students.pdf')


if __name__=='__main__': main()
