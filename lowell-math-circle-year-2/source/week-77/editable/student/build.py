#!/usr/bin/env python3
"""Build the Week 77 student packet with a local TeX installation.

students.tex is written from the problem files by regenerate.py, which this script
runs first unless --no-regenerate is given (the package's root build.py regenerates
in place, then builds a copy)."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--no-regenerate', action='store_true', help='compile students.tex as it is')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    if not args.no_regenerate:
        subprocess.run([sys.executable, str(root / 'regenerate.py')], check=True)
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(root / 'check_math.py')], check=True)
    if shutil.which('pdflatex') is None:
        raise SystemExit('pdflatex is required, with TikZ, geometry, and fancyhdr.')
    with tempfile.TemporaryDirectory(prefix='week77-build-', dir=out) as temp:
        build = Path(temp)
        shutil.copy2(root / 'students.tex', build / 'students.tex')
        env = os.environ.copy()
        if shutil.which('kpsewhich'):
            fmt = subprocess.run(['kpsewhich', 'pdflatex.fmt'], env=env,
                                 stdout=subprocess.PIPE, text=True).stdout.strip()
            if not fmt:
                if 'TEXMF' not in env:
                    trees = subprocess.check_output(['kpsewhich', '-var-value=TEXMF'], text=True).strip()
                    env['TEXMF'] = trees.replace('!!', '')
                result = subprocess.run(['pdftex', '-ini', '-etex', '-jobname=pdflatex',
                    '-interaction=nonstopmode', '-halt-on-error', 'pdflatex.ini'],
                    cwd=build, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                (out / 'format-build.log').write_text(result.stdout)
                if result.returncode:
                    raise SystemExit(result.stdout[-10000:])
                env['TEXFORMATS'] = str(build) + os.pathsep + env.get('TEXFORMATS', '')
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', 'students.tex'],
            cwd=build, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True)
        (out / 'build.log').write_text(result.stdout, encoding='utf-8')
        if result.returncode:
            print(result.stdout[-10000:], file=sys.stderr)
            raise SystemExit(result.returncode)
        if 'Overfull' in result.stdout:
            raise SystemExit('Overfull TeX box: inspect build.log before delivery.')
        shutil.copy2(build / 'students.pdf', out / 'students.pdf')
    print(out / 'students.pdf')


if __name__ == '__main__':
    main()
