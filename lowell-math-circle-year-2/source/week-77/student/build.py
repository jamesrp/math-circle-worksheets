#!/usr/bin/env python3
"""Build the Week 77 student packet with a local TeX installation."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(root / 'check_math.py')], check=True)
    if shutil.which('pdflatex') is None:
        raise SystemExit('pdflatex is required, with TikZ, geometry, and fancyhdr.')
    with tempfile.TemporaryDirectory(prefix='week77-build-', dir=out) as temp:
        build = Path(temp)
        shutil.copy2(root / 'students.tex', build / 'students.tex')
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', 'students.tex'],
            cwd=build, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
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
