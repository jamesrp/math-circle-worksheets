#!/usr/bin/env python3
"""Portable guide builder. Requires Python 3 and standard TeX Live packages."""
import argparse
import os
from pathlib import Path
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    src = Path(__file__).resolve().parent
    out = args.out.resolve()
    if out == src or src in out.parents:
        parser.error('--out must be outside the source directory')
    out.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env['SOURCE_DATE_EPOCH'] = '946684800'
    env['FORCE_SOURCE_DATE'] = '1'
    with (out/'facilitator-build.log').open('w') as stream:
        for _ in range(2):
            subprocess.run(['pdflatex', '-halt-on-error', '-interaction=nonstopmode',
                            '-file-line-error', f'-output-directory={out}', 'facilitator.tex'],
                           cwd=src, env=env, stdout=stream, stderr=subprocess.STDOUT,
                           check=True, timeout=60)
    print(out/'facilitator.pdf')

if __name__ == '__main__':
    main()
