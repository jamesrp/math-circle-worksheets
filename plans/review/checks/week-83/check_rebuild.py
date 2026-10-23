#!/usr/bin/env python3
"""Confirm the delivered Week 83 PDFs are built from the reviewed sources.

Compiles student/students.tex and guide/facilitator.tex with pdflatex in a
temporary folder, then compares extracted text (pdftotext -layout) and the
80 dpi page renders (pdftoppm) with the delivered PDFs. Needs TeX Live,
Poppler and Pillow.

Run: python3 check_rebuild.py   (writes check_rebuild.py.out beside itself)
"""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

from PIL import Image, ImageChops
import warnings
warnings.filterwarnings('ignore')
try:
    import pymupdf as fitz
except ImportError:
    import fitz

HERE = Path(__file__).resolve().parent


def find_repo(here):
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2/source/week-83'
DEL = REPO / 'lowell-math-circle-year-2/week-83'
OUT, FAIL = [], []


def check(cond, msg):
    OUT.append(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


env = dict(os.environ, SOURCE_DATE_EPOCH='1791504000', FORCE_SOURCE_DATE='1')
with tempfile.TemporaryDirectory() as t:
    t = Path(t)
    for kind, name in [('student', 'students'), ('guide', 'facilitator')]:
        shutil.copy2(SRC / kind / f'{name}.tex', t / f'{name}.tex')
        for _ in range(2):
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', f'{name}.tex'], cwd=t, env=env,
                               capture_output=True, text=True)
        check(r.returncode == 0, f'{name}.tex compiles')
        built, shipped = t / f'{name}.pdf', DEL / f'week-83-{name}.pdf'
        txt = lambda p: subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True).stdout
        check(txt(built) == txt(shipped), f'{name}: extracted text of rebuilt PDF equals delivered PDF')
        subprocess.run(['pdftoppm', '-r', '80', '-png', str(built), str(t / f'{name}-b')], check=True)
        subprocess.run(['pdftoppm', '-r', '80', '-png', str(shipped), str(t / f'{name}-s')], check=True)
        bs, ss = sorted(t.glob(f'{name}-b-*.png')), sorted(t.glob(f'{name}-s-*.png'))
        worst = 0
        for a, b in zip(bs, ss):
            d = ImageChops.difference(Image.open(a).convert('L'), Image.open(b).convert('L'))
            worst = max(worst, d.getextrema()[1])
        check(len(bs) == len(ss) and worst <= 64,
              f'{name}: {len(ss)} rendered pages match at 80 dpi (largest grey-level difference {worst}/255: anti-aliasing only)')
        wb = [pg.get_text('words') for pg in fitz.open(built)]
        ws = [pg.get_text('words') for pg in fitz.open(shipped)]
        same = len(wb) == len(ws) and all(
            len(a) == len(b) and all(x[4] == y[4] and abs(x[0] - y[0]) < 1 and abs(x[1] - y[1]) < 1 for x, y in zip(a, b))
            for a, b in zip(wb, ws))
        check(same, f'{name}: every word at the same position (within 1 pt) in rebuilt and delivered PDF')
OUT.append(f'FAILURES: {len(FAIL)}')
(HERE / 'check_rebuild.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
