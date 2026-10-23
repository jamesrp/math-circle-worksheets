"""Standalone guide build; requires Python 3 and pdflatex on PATH."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='week53-guide-') as work:
        work = Path(work)
        shutil.copy2(source / 'facilitator.tex', work)
        for _ in range(2):
            run = subprocess.run(['pdflatex', '-interaction=nonstopmode',
                '-halt-on-error', 'facilitator.tex'], cwd=work,
                capture_output=True, text=True)
            if run.returncode:
                raise SystemExit(run.stdout + run.stderr)
        log = (work / 'facilitator.log').read_text()
        if 'Overfull' in log:
            lines = log.splitlines()
            details = '\n'.join('\n'.join(lines[i:i+7]) for i,l in enumerate(lines) if 'Overfull' in l)
            raise SystemExit('Overfull box found:\n' + details)
        shutil.copy2(work / 'facilitator.pdf', output / 'facilitator.pdf')
    print(output / 'facilitator.pdf')

if __name__ == '__main__':
    main()
