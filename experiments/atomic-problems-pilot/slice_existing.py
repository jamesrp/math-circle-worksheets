#!/usr/bin/env python3
"""Band views of an existing shared packet, without touching its source.

Weeks 52-93 print one shared student packet whose page headers name a grade
range ("Grades K-1", "Grades 3-5", ...). This reads those headers into a page
index and writes one PDF per band from the existing pages.

    python3 slice_existing.py ../../lowell-math-circle-year-2/week-52/week-52-students.pdf \
        --index week-52/pages.toml --out output/week-52
    python3 slice_existing.py --survey ../../lowell-math-circle-year-2
"""
import argparse
import re
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter

GRADES = 'K12345'
VIEWS = {'k-1': set('K1'), 'grades-2-3': set('23'), 'grades-4-5': set('45')}
HEADER = re.compile(r'^Week \d+ / .* / (?:Grades )?([K1-5])[–-]([1-5])\b')


def page_text(pdf, n):
    return subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), str(pdf), '-'],
                          capture_output=True, text=True).stdout


def index(pdf):
    rows, last = [], None
    for n in range(1, len(PdfReader(pdf).pages) + 1):
        text = page_text(pdf, n)
        m = next((HEADER.match(l.strip()) for l in text.splitlines() if HEADER.match(l.strip())), None)
        grades = set(GRADES[GRADES.index(m[1]):GRADES.index(m[2]) + 1]) if m else last
        problems = [int(p) for p in re.findall(r'Problem (\d+):', text)]
        rows.append({'page': n, 'grades': grades, 'label': f'{m[1]}–{m[2]}' if m else '(none)',
                     'problems': problems})
        last = grades
    return rows


def write_index(rows, path, pdf):
    lines = [f'# Draft page index read from page headers of {pdf}', '# Check by eye before relying on it.', '']
    for r in rows:
        lines += ['[[page]]', f'page = {r["page"]}', f'grades = "{r["label"]}"',
                  f'problems = {r["problems"]}', '']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines))


def slices(rows):
    return {v: [r['page'] for r in rows if r['grades'] and r['grades'] & want] for v, want in VIEWS.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf', nargs='?')
    ap.add_argument('--index')
    ap.add_argument('--out')
    ap.add_argument('--survey')
    a = ap.parse_args()
    if a.survey:
        print('week  pages  K-1  2-3  4-5   (pages in each band view)')
        for pdf in sorted(Path(a.survey).glob('week-*/week-*-students.pdf')):
            rows = index(pdf)
            if not any(r['label'] != '(none)' for r in rows):
                continue
            s = slices(rows)
            labels = sorted({r['label'] for r in rows})
            print(f'{pdf.parent.name[5:]:>4}  {len(rows):5d}  {len(s["k-1"]):3d}  {len(s["grades-2-3"]):3d}  '
                  f'{len(s["grades-4-5"]):3d}   {", ".join(labels)}')
        return
    rows = index(a.pdf)
    if a.index:
        write_index(rows, Path(a.index), a.pdf)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(a.pdf)
    for view, pages in slices(rows).items():
        if not pages:
            continue
        w = PdfWriter()
        for n in pages:
            w.add_page(reader.pages[n - 1])
        w.write(out / f'{view}.pdf')
        probs = [p for r in rows if r['page'] in pages for p in r['problems']]
        print(f'{view:11s} pages {pages}  problems {probs}')


if __name__ == '__main__':
    main()
