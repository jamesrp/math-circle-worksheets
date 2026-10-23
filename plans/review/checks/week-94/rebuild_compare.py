#!/usr/bin/env python3
"""Rebuild the Week 94 PDFs from the editable sources into a temporary folder
and compare them byte for byte with the delivered PDFs, so the source data the
math check reads are the data on the printed pages. Needs pdflatex.

Run: python3 rebuild_compare.py   (writes rebuild_compare.py.out beside itself)
"""
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-94'
PDF = REPO / 'lowell-math-circle-year-2' / 'week-94'
lines = []
if not shutil.which('pdflatex'):
    lines.append('SKIP pdflatex not on PATH')
else:
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        r = subprocess.run([sys.executable, str(SRC / 'build.py'), '--out', str(t / 'out'), '--work', str(t / 'work')],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        lines.append('build: ' + r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'build: (no output)')
        for name in ('k-1', 'grades-2-3', 'grades-4-5', 'facilitator'):
            a = hashlib.sha256((PDF / f'week-94-{name}.pdf').read_bytes()).hexdigest()
            bp = t / 'out' / f'week-94-{name}.pdf'
            b = hashlib.sha256(bp.read_bytes()).hexdigest() if bp.exists() else 'missing'
            lines.append(('same bytes ' if a == b else 'bytes differ ') + f'week-94-{name}.pdf {a[:16]} rebuilt {b[:16]}')
            if a != b and bp.exists():
                # different TeX Live builds give different bytes; compare what is printed
                try:
                    import pymupdf
                except ImportError:
                    import fitz as pymupdf
                da, db = pymupdf.open(str(PDF / f'week-94-{name}.pdf')), pymupdf.open(str(bp))
                same_pages = len(da) == len(db)
                def words(page):
                    # whitespace-normalised page text; sub-point kerning differences between
                    # TeX Live versions move word boxes by under 1 pt and are ignored
                    return ''.join(page.get_text().split())
                same_text = same_pages and all(words(x) == words(y) for x, y in zip(da, db))

                def geom(page):
                    def nums(pt):
                        if hasattr(pt, 'x'):
                            return (pt.x, pt.y)
                        if hasattr(pt, 'x0'):
                            return (pt.x0, pt.y0, pt.x1, pt.y1)
                        return (float(pt),)
                    return sorted((it[0],) + tuple(round(v, 1) for pt in it[1:] for v in nums(pt))
                                  for d in page.get_drawings() for it in d['items'])
                same_geom = same_pages and all(geom(x) == geom(y) for x, y in zip(da, db))
                lines.append(f'   pages {len(da)}/{len(db)}; page text identical: {same_text}; vector geometry identical (0.1 pt): {same_geom}')
text = '\n'.join(lines) + '\n'
(HERE / 'rebuild_compare.py.out').write_text(text)
print(text)
