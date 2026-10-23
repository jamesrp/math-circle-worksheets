"""Standalone guide build; source is never used as an intermediate directory."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess

def main():
    p=argparse.ArgumentParser()
    p.add_argument('output',type=Path)
    a=p.parse_args()
    out=a.output.resolve();out.mkdir(parents=True,exist_ok=True)
    work=out/'.guide-build';work.mkdir(exist_ok=True)
    shutil.copy2(Path(__file__).resolve().with_name('facilitator.tex'),work/'facilitator.tex')
    env=dict(os.environ,SOURCE_DATE_EPOCH='1791072000',FORCE_SOURCE_DATE='1')
    for _ in range(2):
        r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','facilitator.tex'],cwd=work,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (work/'console.txt').write_text(r.stdout)
        if r.returncode: print(r.stdout);raise SystemExit(r.returncode)
    log=(work/'facilitator.log').read_text()
    if 'Overfull' in log: print(log);raise SystemExit('Overfull layout')
    shutil.copy2(work/'facilitator.pdf',out/'facilitator.pdf')
    print(out/'facilitator.pdf')

if __name__=='__main__':main()
