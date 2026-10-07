#!/usr/bin/env python3
"""Build facilitator.pdf using Python's standard library and a TeX installation."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(command, cwd, env, log):
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True)
    log.write_text(result.stdout + result.stderr)
    if result.returncode:
        print((result.stdout + result.stderr)[-12000:], file=sys.stderr)
        raise SystemExit(f'Build failed; see {log}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    out = args.out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    build = out / '.build-facilitator'
    build.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.update(TEXMFVAR=str(build / 'texmf-var'),
               TEXMFCONFIG=str(build / 'texmf-config'), TEXMFOUTPUT=str(build))
    kpse = shutil.which('kpsewhich')
    if not kpse or not shutil.which('pdflatex'):
        raise SystemExit('Install TeX Live or MacTeX with pdflatex and Latin Modern.')
    found = subprocess.run([kpse, 'article.cls'], env=env, capture_output=True, text=True)
    if not found.stdout.strip():
        for name in ('TEXMF', 'TEXMFDBS'):
            value = subprocess.check_output([kpse, '-var-value=' + name], env=env, text=True).strip()
            env[name] = value.replace('!!', '')
    found = subprocess.run([kpse, 'pdflatex.fmt'], env=env, capture_output=True, text=True)
    if not found.stdout.strip():
        env['TEXFORMATS'] = str(build) + os.pathsep + env.get('TEXFORMATS', '')
        if not (build / 'pdflatex.fmt').exists():
            run(['pdftex', '-ini', '-etex', '-interaction=nonstopmode', '-halt-on-error',
                 '-jobname=pdflatex', 'pdflatex.ini'], build, env, build / 'format-build.log')
    subprocess.run([sys.executable, str(HERE / 'check_math.py')], check=True)
    shutil.copy2(HERE / 'facilitator.tex', build / 'facilitator.tex')
    for n in (1, 2):
        run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
             'facilitator.tex'], build, env, build / f'compile-{n}.log')
    shutil.copy2(build / 'facilitator.pdf', out / 'facilitator.pdf')
    print(out / 'facilitator.pdf')


if __name__ == '__main__':
    main()
