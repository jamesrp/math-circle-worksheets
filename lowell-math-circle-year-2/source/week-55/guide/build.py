#!/usr/bin/env python3
"""Standalone guide build; all intermediates live beneath --out and are removed."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH='1791072000', FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix='week55-guide-', dir=output) as folder:
        work = Path(folder)
        shutil.copyfile(ROOT/'facilitator.tex', work/'facilitator.tex')
        for _ in range(2):
            run = subprocess.run(['pdflatex', '-interaction=nonstopmode',
                                  '-halt-on-error', '-file-line-error', 'facilitator.tex'],
                                 cwd=work, env=env, capture_output=True, text=True)
            if run.returncode:
                raise RuntimeError(run.stdout[-12000:] + run.stderr)
        log = (work/'facilitator.log').read_text()
        if 'Overfull' in log:
            raise RuntimeError('Overfull box in guide build: '+
                               '\n'.join(x for x in log.splitlines() if 'Overfull' in x))
        shutil.copyfile(work/'facilitator.pdf', output/'facilitator.pdf')
    print(output/'facilitator.pdf')

if __name__ == '__main__':
    main()
