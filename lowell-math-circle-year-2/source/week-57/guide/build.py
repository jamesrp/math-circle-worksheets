#!/usr/bin/env python3
"""Build the authored Week 57 guide without repository-relative dependencies."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output-dir',required=True)
    args=ap.parse_args()
    src=Path(__file__).resolve().parent
    out=Path(args.output_dir).resolve();out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,SOURCE_DATE_EPOCH='1791072000',FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix='week57-guide-') as temporary:
        temp=Path(temporary)
        for run in range(2):
            p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',
                '-output-directory',str(temp),str(src/'facilitator.tex')],
                cwd=src,env=env,capture_output=True,text=True)
            (out/'guide-compile.log').write_text(p.stdout+p.stderr)
            if p.returncode: raise SystemExit(p.stdout+p.stderr)
        log=(temp/'facilitator.log').read_text()
        (out/'guide-tex.log').write_text(log)
        if 'Overfull' in log: raise SystemExit('Overfull TeX boxes; inspect guide-tex.log')
        shutil.copy2(temp/'facilitator.pdf',out/'facilitator.pdf')
    print(out/'facilitator.pdf')

if __name__=='__main__': main()
