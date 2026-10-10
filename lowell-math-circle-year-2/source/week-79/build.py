#!/usr/bin/env python3
"""Build both owned PDFs and run the independent mathematical checker."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
WEEK = 79

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT / 'out')
    parser.add_argument('--work', type=Path, help='Build intermediates (default: repo tmp, or package tmp)')
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    repo = ROOT.parents[2] if len(ROOT.parents) > 2 else ROOT
    work = args.work or ((repo / 'tmp/pdf-builds') if (repo / 'AGENTS.md').is_file() else ROOT / 'tmp')
    work = work.resolve()
    work.mkdir(parents=True, exist_ok=True)
    latex = shutil.which('pdflatex')
    if not latex and Path('/Library/TeX/texbin/pdflatex').is_file():
        latex = '/Library/TeX/texbin/pdflatex'
    if not latex:
        raise SystemExit('Install pdfLaTeX with geometry, fancyhdr, TikZ, lmodern, helvet, amsmath and hyperref.')
    env = dict(os.environ, SOURCE_DATE_EPOCH='1791504000', FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix=f'week-{WEEK}-', dir=work) as name:
        temp = Path(name)
        for kind, filename in [('student', 'students'), ('guide', 'facilitator')]:
            folder = temp / kind
            folder.mkdir()
            shutil.copy2(ROOT / kind / (filename + '.tex'), folder / (filename + '.tex'))
            for _ in range(2):
                run = subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error', filename + '.tex'],
                                     cwd=folder, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                (work / f'week-{WEEK}-{filename}-build.log').write_text(run.stdout)
                if run.returncode:
                    raise SystemExit(run.stdout[-6000:])
            if 'Overfull' in run.stdout:
                raise SystemExit('Overfull content: inspect ' + str(work / f'week-{WEEK}-{filename}-build.log'))
            target = out / f'week-{WEEK}-{filename}.pdf'
            shutil.copy2(folder / (filename + '.pdf'), target)
        result = work / f'week-{WEEK}-math-checks.json'
        env['INFINITY_CHECK_OUT'] = str(result)
        command = [sys.executable, str(ROOT / 'check_math.py')]
        if WEEK == 81:
            command += ['--tex', str(ROOT / 'student/students.tex'), '--pdf', str(out / f'week-{WEEK}-students.pdf'), '--output', str(result)]
        elif WEEK == 83:
            command += [str(ROOT / 'student/students.tex')]
        check = subprocess.run(command, cwd=temp, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (work / f'week-{WEEK}-math-checks.log').write_text(check.stdout)
        if check.returncode:
            raise SystemExit(check.stdout)
    print(f'PASS: Week {WEEK}, both PDFs built; independent mathematical checks passed.')
    print('Mathematical evidence:', result)

if __name__ == '__main__':
    main()
