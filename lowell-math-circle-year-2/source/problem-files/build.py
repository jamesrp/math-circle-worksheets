#!/usr/bin/env python3
"""Build every view of a week from its problem files.

    python3 build.py week-50 --out output/week-50 [--tables K-1=3,2-3=4,4-5=3] [--tex]

Views written to --out:
  <band>.pdf          the full packet for a band (same pages as today's packets)
  <band>-first.pdf    the first-route problems only
  <band>-return.pdf   the return-visit problems only
  menu.pdf            one page: every problem once, with its number in each band
  guide-keys.pdf      the adult key, one entry per problem, cross-referenced by band
  session-pack.pdf    first-route packets for each table, in copies (with --tables)
  <band>.tex          the LaTeX of each full packet (with --tex)

With --publish DIR, the menu, the key and the route packets are also copied to DIR
as week-NN-menu.pdf, week-NN-key.pdf and week-NN-<band>-first.pdf / -return.pdf.
The same files always give byte-identical PDFs (SOURCE_DATE_EPOCH is fixed).
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter

import atoms
from atoms import ProblemFileError

BAND_NAMES = {'K-1': 'K--1', '2-3': 'Grades 2--3', '4-5': 'Grades 4--5'}
ENGINES = ('pdflatex', 'xelatex')   # week.toml `engine` compiles the student packets; the menu and key use pdflatex
FILE_NAMES = {'K-1': 'k-1', '2-3': 'grades-2-3', '4-5': 'grades-4-5'}


def file_name(week, band):
    name = week.bands[band].get('file', FILE_NAMES.get(band))
    if not name:
        raise ProblemFileError(f'week.toml: band "{band}" needs file = "..." for its PDF name')
    return name


def band_name(week, band):
    return BAND_NAMES.get(band, week.bands[band]['header'])


def latex_errors(log: str) -> str:
    """The '!' error lines of a pdfLaTeX log with the source line TeX stopped at."""
    lines, out = log.splitlines(), []
    for i, line in enumerate(lines):
        if line.startswith('!'):
            out.append(line)
            out += [m for m in lines[i + 1:i + 12] if re.match(r'l\.\d+', m)][:1]
    return '\n'.join(out[:6]) or log[-1500:]


def pdflatex(tex: str, out: Path, extra=(), inputs=(), week=None, engine='pdflatex'):
    """Compile twice in a scratch folder. The `inputs` folders (the week folder and
    week.toml's inputs) are searched for files the LaTeX inputs, such as a shared
    preamble or figure files. `engine` is pdflatex unless week.toml sets
    engine = "xelatex" for a week whose template loads fontspec."""
    env = os.environ.copy()
    env.setdefault('SOURCE_DATE_EPOCH', '1767225600')   # 2026-01-01: the same files give the same PDF
    if engine == 'xelatex':
        env.setdefault('FORCE_SOURCE_DATE', '1')        # XeTeX also stamps the time in its output unless forced
    if inputs:
        env['TEXINPUTS'] = os.pathsep.join(map(str, inputs)) + os.pathsep + env.get('TEXINPUTS', '')
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / 'doc.tex').write_text(tex)
        for f in extra:
            shutil.copy(f, tmp / Path(f).name)
        for _ in range(2):
            r = subprocess.run([engine, '-interaction=nonstopmode', '-halt-on-error', 'doc.tex'],
                               cwd=tmp, capture_output=True, text=True, env=env)
            if r.returncode:
                out.with_suffix('.log').write_text(r.stdout)
                out.with_suffix('.failed.tex').write_text(tex)
                hint = ''
                m = re.search(r'^l\.(\d+)', r.stdout, re.M)
                if m and week is not None:
                    hint = source_of_line(week, tex, int(m.group(1)))
                raise ProblemFileError(f'{engine} failed for {out.name}:\n{latex_errors(r.stdout)}\n{hint}'
                                       f'Full log: {out.with_suffix(".log")}; LaTeX: {out.with_suffix(".failed.tex")}')
        shutil.copy(tmp / 'doc.pdf', out)
    return out


def source_of_line(week, tex: str, n: int) -> str:
    """Name the problem file whose text produced line n of the generated LaTeX."""
    lines = tex.splitlines()
    if not 0 < n <= len(lines):
        return ''
    target = lines[n - 1].strip()
    if len(target) < 8:
        return ''
    for a in week.atoms:
        for s in a.sections:
            if target in s.raw or target in s.body:
                return f'That line comes from {a.where_in_file(s)}.\n'
    return 'That line comes from the template, figures.py or the canvas page template.\n'


def pages(pdf: Path) -> int:
    return len(PdfReader(pdf).pages)


def compact(nums):
    """P1--P3, P5 for [1, 2, 3, 5]."""
    out, run = [], []
    for n in nums + [None]:
        if run and (n is None or n != run[-1] + 1):
            out.append(f'P{run[0]}' if len(run) == 1 else f'P{run[0]}--P{run[-1]}')
            run = []
        if n is not None:
            run.append(n)
    return ', '.join(out) or 'none'


def numbers_line(week, atom):
    w = atoms.where(week, atom)
    return r' \textperiodcentered{} '.join(f'{band_name(week, b)} P{n}' for b, n in w.items())


def guide_tex(week) -> str:
    g = week.meta.get('guide', {})
    read = lambda key: (week.folder / g[key]).read_text() if key in g else ''
    m = week.meta
    bands = list(week.bands)
    rows = ''
    for a in week.atoms:
        if not a.numbered:
            continue
        w = atoms.where(week, a)
        cells = ' & '.join(f'P{w[b]}' if b in w else '' for b in bands)
        rows += f'{a.title} & {cells} & {a.route_label(bands)} \\\\\n'
    body = ''
    for a in week.atoms:
        if not a.numbered:
            continue
        body += f'\\subsection*{{{a.title}}}\n{{\\small {numbers_line(week, a)} \\textperiodcentered{{}} {a.route_label(bands)} route'
        if a.varies():
            body += r' \textperiodcentered{} wording differs by band'
        body += '}\\par\\smallskip\n'
        if a.meta.get('kernel'):
            body += f'\\emph{{Idea.}} {a.kernel}\\par\n'
        for s in [s for s in a.sections if s.kind in atoms.ADULT_KINDS]:
            if s.kind == 'key-figure':
                body += ('\\begin{center}\\begin{tikzpicture}[x=0.42mm,y=-0.42mm,line width=.5pt,'
                         'every node/.style={scale=0.8}]\n' + atoms.figure(week, a, s) +
                         '\\end{tikzpicture}\\par{\\footnotesize Guide diagram, not to scale}\\end{center}\n')
            else:
                tag = (f'\\textbf{{{", ".join(band_name(week, b) for b in bands if b in s.bands)}:}} '
                       if s.bands else '')
                body += f'{tag}{s.raw}\\par\n'
    if not any(a.meta.get('kernel') or any(s.kind in atoms.ADULT_KINDS for s in a.sections) for a in week.atoms):
        body = "These problem files hold no keys; the week's adult guide has them.\n"
    first = {b: [p.number for p in atoms.compose(week, b, 'first') if p.number] for b in bands}
    ret = {b: [p.number for p in atoms.compose(week, b, 'return') if p.number] for b in bands}
    route = '; '.join(f'{band_name(week, b)} {compact(first[b])}' for b in bands)
    route_r = '; '.join(f'{band_name(week, b)} {compact(ret[b])}' for b in bands)
    cols = ' & '.join(band_name(week, b).replace('Grades ', '') for b in bands)
    mixed = any(';' in a.route_label(bands) for a in week.atoms)
    width, route_col = ('62mm', r'>{\raggedright\arraybackslash}p{42mm}') if mixed else ('78mm', 'l')
    section = lambda title, key, size='': (f'\\section*{{{title}}}\n{{{size}{read(key)}}}\n' if size else
                                          f'\\section*{{{title}}}\n{read(key)}\n') if key in g else ''
    note = f'{g["note"]}\\par\n' if 'note' in g else ''
    return rf'''\documentclass[10pt,letterpaper]{{article}}
\usepackage[margin=17mm,top=20mm]{{geometry}}
\usepackage[T1]{{fontenc}}\usepackage{{helvet}}\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{tikz,fancyhdr,array,booktabs,amsmath}}\usetikzlibrary{{arrows.meta}}
\pagestyle{{fancy}}\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}
\fancyhead[L]{{\small Week {m['week']} / {m['topic']} / Adult guide}}
\fancyfoot[L]{{\small Bellingham Math Circle / Week {m['week']} / {m['packet']}-G-{m['version']}}}
\fancyfoot[R]{{\small\thepage}}
\setlength{{\parindent}}{{0pt}}\setlength{{\parskip}}{{5pt}}
\begin{{document}}
{{\Large\bfseries Week {m['week']}: {m['topic']}}}\par
{{\small Adult guide built from the problem files \textperiodcentered{{}} {m.get('status', '')}}}\par
{note}{section('Mathematical overview', 'overview')}{section('Prepare and launch', 'prepare')}\section*{{Problems and routes}}
\begin{{tabular}}{{@{{}}>{{\raggedright}}p{{{width}}}{'c' * len(bands)} {route_col}@{{}}}}
\toprule Problem & {cols} & route\\\midrule
{rows}\bottomrule\end{{tabular}}\par
\textbf{{First route.}} {route}. \textbf{{Return visits.}} {route_r}.
\section*{{Key, one entry per problem}}
{body}
{section('Optional hints and facilitation checks', 'hints')}{section('Source and verification', 'sources', '\\small ')}\end{{document}}
'''


def find_page(pdf: Path, number: int) -> int:
    """The first page of a flowing packet that prints "Problem <number>"."""
    for i in range(1, pages(pdf) + 1):
        txt = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), str(pdf), '-'],
                             capture_output=True, text=True).stdout
        if re.search(rf'Problem\s+{number}\b', txt):
            return i
    print(f'warning: "Problem {number}" not found in {pdf.name}; the menu shows its first page', file=sys.stderr)
    return 1


def menu_grid(n):
    """Columns, cell width and thumbnail height (mm) and caption size that fit n problems on one page."""
    if n <= 9:
        return 3, 56, 52, r'\footnotesize'
    for cols in range(4, 9):
        width = (186 - 3 * (cols - 1)) / cols
        height = min(52, round(width * 1.29, 1))
        if -(-n // cols) * (height + 20) <= 240:
            return cols, round(width, 1), height, r'\scriptsize'
    return 8, 21, 27, r'\tiny'


def menu_tex(week, thumbs) -> str:
    m = week.meta
    bands = list(week.bands)
    numbered = [a for a in week.atoms if a.numbered]
    cols, width, height, size = menu_grid(len(numbered))
    cells = []
    for a in numbered:
        nums = numbers_line(week, a)
        mark = r'\\\emph{wording differs by band}' if a.varies() else ''
        cells.append(rf'''\begin{{minipage}}[t]{{{width}mm}}\centering
\fbox{{\includegraphics[height={height}mm]{{{thumbs[a.id].name}}}}}\\[2pt]
{{{size}\raggedright\textbf{{{a.title}}}\\{nums}\\{a.route_label(bands)} route{mark}\par}}
\end{{minipage}}''')
    grid = ''
    for i in range(0, len(cells), cols):
        row = cells[i:i + cols]
        row += [rf'\begin{{minipage}}[t]{{{width}mm}}\mbox{{}}\end{{minipage}}'] * (cols - len(row))
        grid += '\\noindent' + '\\hfill'.join(row) + '\\par\\vspace{4mm}\n'
    return rf'''\documentclass[10pt,letterpaper]{{article}}
\usepackage[margin=12mm,top=16mm,bottom=14mm]{{geometry}}
\usepackage[T1]{{fontenc}}\usepackage{{helvet}}\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{graphicx}}\pagestyle{{empty}}\setlength{{\parindent}}{{0pt}}\setlength{{\fboxsep}}{{0pt}}
\begin{{document}}
{{\large\bfseries Week {m['week']} / {m['topic']} / Problem menu}}\hfill{{\small for adults: pick, then print}}\par\vspace{{3mm}}
{grid}
\end{{document}}
'''


def build(args):
    week = atoms.load_week(Path(args.week))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    compile_ = lambda tex, path, extra=(): pdflatex(tex, path, extra, week.inputs, week)
    engine = week.meta.get('engine', 'pdflatex')
    if engine not in ENGINES:
        raise ProblemFileError(f'week.toml: engine = {engine!r}; use one of {", ".join(map(repr, ENGINES))}')
    student = lambda tex, path: pdflatex(tex, path, (), week.inputs, week, engine)
    built = {}
    for band in week.bands:
        name = file_name(week, band)
        tex = atoms.student_tex(week, band)
        if args.tex:
            (out / f'{name}.tex').write_text(tex)
        built[band] = student(tex, out / f'{name}.pdf')
        for route in ('first', 'return'):
            if atoms.compose(week, band, route):
                student(atoms.student_tex(week, band, route, f'-{route}'), out / f'{name}-{route}.pdf')
    compile_(guide_tex(week), out / 'guide-keys.pdf')
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        thumbs = {}
        for a in week.atoms:
            if not a.numbered:
                continue
            band = '2-3' if '2-3' in a.grades else a.grades[0]
            p = next(p for p in atoms.compose(week, band) if p.atom is a)
            page = p.page if week.layout == 'canvas' else find_page(built[band], p.number)
            stem = tmp / a.id.replace('.', '-')
            subprocess.run(['pdftoppm', '-r', '90', '-png', '-singlefile', '-f', str(page), '-l', str(page),
                            str(built[band]), str(stem)], check=True)
            thumbs[a.id] = stem.with_suffix('.png')
        compile_(menu_tex(week, thumbs), out / 'menu.pdf', thumbs.values())
    if args.tables:
        writer = PdfWriter()
        for item in args.tables.split(','):
            band, copies = item.split('=')
            if band not in week.bands:
                raise ProblemFileError(f'--tables names band "{band}"; this week has {", ".join(week.bands)}')
            src = out / f'{file_name(week, band)}-first.pdf'
            if not src.exists():
                raise ProblemFileError(f'--tables: band {band} has no first-route problems')
            for _ in range(int(copies)):
                writer.append(str(src))
        writer.write(out / 'session-pack.pdf')
    for f in sorted(out.glob('*.pdf')):
        print(f'{pages(f):3d} pages  {f}')
    if args.publish:
        publish(week, out, Path(args.publish))


def publish(week, out: Path, dest: Path):
    """Copy the views that are not the print packets into dest as week-NN-<view>.pdf:
    the menu, the key and each band's first-route and return packets."""
    stem = f"week-{int(week.meta['week']):02d}"
    dest.mkdir(parents=True, exist_ok=True)
    for old in dest.glob(f'{stem}-*.pdf'):
        old.unlink()
    names = {'menu.pdf': 'menu', 'guide-keys.pdf': 'key'}
    for band in week.bands:
        for route in ('first', 'return'):
            names[f'{file_name(week, band)}-{route}.pdf'] = f'{file_name(week, band)}-{route}'
    for src, name in names.items():
        if (out / src).exists():
            shutil.copy(out / src, dest / f'{stem}-{name}.pdf')
            print(f'published {dest / f"{stem}-{name}.pdf"}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('week', help='the week folder holding week.toml and problems/')
    ap.add_argument('--out', required=True, help='folder for the built views, under tmp/')
    ap.add_argument('--tables', help='copies of the first-route packet per band, e.g. K-1=3,2-3=4,4-5=3')
    ap.add_argument('--tex', action='store_true', help="also write each band packet's LaTeX")
    ap.add_argument('--publish', help='also copy the menu, key and route packets here as week-NN-<view>.pdf, '
                                      'e.g. lowell-math-circle-year-2/band-views/week-43')
    args = ap.parse_args()
    try:
        build(args)
    except ProblemFileError as e:
        sys.exit(f'error: {e}')


if __name__ == '__main__':
    main()
