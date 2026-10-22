#!/usr/bin/env python3
"""Build every view of a week from its problem files.

    python3 build.py week-50 --out output/week-50 [--tables K-1=3,2-3=4,4-5=3]

Views written to --out:
  <band>.pdf          the full packet for a band (same pages as today's packets)
  <band>-first.pdf    the first-route problems only
  <band>-return.pdf   the return-visit problems only
  menu.pdf            one page: every problem once, with its number in each band
  guide-keys.pdf      the adult key, one entry per problem, cross-referenced by band
  session-pack.pdf    first-route packets for each table, in copies (with --tables)
"""
import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter

import atoms

BAND_NAMES = {'K-1': 'K--1', '2-3': 'Grades 2--3', '4-5': 'Grades 4--5'}
FILE_NAMES = {'K-1': 'k-1', '2-3': 'grades-2-3', '4-5': 'grades-4-5'}


def pdflatex(tex: str, out: Path, extra=()):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / 'doc.tex').write_text(tex)
        for f in extra:
            shutil.copy(f, tmp / Path(f).name)
        for _ in range(2):
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'doc.tex'],
                               cwd=tmp, capture_output=True, text=True)
            if r.returncode:
                (out.with_suffix('.log')).write_text(r.stdout)
                raise SystemExit(f'pdflatex failed for {out.name}; see {out.with_suffix(".log")}')
        shutil.copy(tmp / 'doc.pdf', out)
    return out


def pages(pdf: Path) -> int:
    return len(PdfReader(pdf).pages)


def numbers_line(week, atom):
    w = atoms.where(week, atom)
    return r' \textperiodcentered{} '.join(f'{BAND_NAMES[b]} P{n}' for b, n in w.items())


def guide_tex(week) -> str:
    g = week.meta['guide']
    read = lambda key: (week.folder / g[key]).read_text()
    m = week.meta
    rows = ''
    for a in week.atoms:
        if not a.numbered:
            continue
        w = atoms.where(week, a)
        cells = ' & '.join(f'P{w[b]}' if b in w else '' for b in week.bands)
        rows += f'{a.title} & {cells} & {a.route} \\\\\n'
    body = ''
    for a in week.atoms:
        if not a.numbered:
            continue
        body += f'\\subsection*{{{a.title}}}\n{{\\small {numbers_line(week, a)} \\textperiodcentered{{}} {a.route} route'
        if a.varies():
            body += r' \textperiodcentered{} wording differs by band'
        body += '}\\par\\smallskip\n'
        if a.meta.get('kernel'):
            body += f'\\emph{{Idea.}} {a.kernel}\\par\n'
        for s in [s for s in a.sections if s.kind in atoms.ADULT_KINDS]:
            if s.kind == 'key-figure':
                body += ('\\begin{center}\\begin{tikzpicture}[x=0.42mm,y=-0.42mm,line width=.5pt,'
                         'every node/.style={scale=0.8}]\n' + eval(s.body, dict(week.figures)) +
                         '\\end{tikzpicture}\\par{\\footnotesize Guide diagram, not to scale}\\end{center}\n')
            else:
                tag = f'\\textbf{{{", ".join(BAND_NAMES[b] for b in sorted(s.bands))}:}} ' if s.bands else ''
                body += f'{tag}{s.body}\\par\n'
    first = {b: [f'P{p.number}' for p in atoms.compose(week, b, 'first') if p.number] for b in week.bands}
    ret = {b: [f'P{p.number}' for p in atoms.compose(week, b, 'return') if p.number] for b in week.bands}
    route = '; '.join(f'{BAND_NAMES[b]} {"--".join([first[b][0], first[b][-1]])}' for b in week.bands)
    route_r = '; '.join(f'{BAND_NAMES[b]} {", ".join(ret[b])}' for b in week.bands)
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
{{\small Adult guide built from the problem files \textperiodcentered{{}} {m['status']}}}
\section*{{Mathematical overview}}
{read('overview')}
\section*{{Prepare and launch}}
{read('prepare')}
\section*{{Problems and routes}}
\begin{{tabular}}{{@{{}}>{{\raggedright}}p{{78mm}}ccc l@{{}}}}
\toprule Problem & K--1 & 2--3 & 4--5 & route\\\midrule
{rows}\bottomrule\end{{tabular}}\par
\textbf{{First route.}} {route}. \textbf{{Return visits.}} {route_r}.
\section*{{Key, one entry per problem}}
{body}
\section*{{Optional hints and facilitation checks}}
{read('hints')}
\section*{{Source and verification}}
{{\small {read('sources')}}}
\end{{document}}
'''


def menu_tex(week, thumbs) -> str:
    m = week.meta
    cells = []
    for a in week.atoms:
        if not a.numbered:
            continue
        w = atoms.where(week, a)
        nums = numbers_line(week, a)
        mark = r'\\\emph{wording differs by band}' if a.varies() else ''
        cells.append(rf'''\begin{{minipage}}[t]{{56mm}}\centering
\fbox{{\includegraphics[height=52mm]{{{thumbs[a.id].name}}}}}\\[2pt]
{{\footnotesize\raggedright\textbf{{{a.title}}}\\{nums}\\{a.route} route{mark}\par}}
\end{{minipage}}''')
    grid = ''
    for i in range(0, len(cells), 3):
        grid += '\\noindent' + '\\hfill'.join(cells[i:i + 3]) + '\\par\\vspace{4mm}\n'
    return rf'''\documentclass[10pt,letterpaper]{{article}}
\usepackage[margin=12mm,top=16mm,bottom=14mm]{{geometry}}
\usepackage[T1]{{fontenc}}\usepackage{{helvet}}\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{graphicx}}\pagestyle{{empty}}\setlength{{\parindent}}{{0pt}}\setlength{{\fboxsep}}{{0pt}}
\begin{{document}}
{{\large\bfseries Week {m['week']} / {m['topic']} / Problem menu}}\hfill{{\small for adults: pick, then print}}\par\vspace{{3mm}}
{grid}
\end{{document}}
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('week')
    ap.add_argument('--out', required=True)
    ap.add_argument('--tables', help='copies of the first-route packet per band, e.g. K-1=3,2-3=4,4-5=3')
    args = ap.parse_args()
    week = atoms.load_week(Path(args.week))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    built = {}
    for band in week.bands:
        name = FILE_NAMES[band]
        built[band] = pdflatex(atoms.student_tex(week, band), out / f'{name}.pdf')
        for route in ('first', 'return'):
            if atoms.compose(week, band, route):
                pdflatex(atoms.student_tex(week, band, route, f'-{route}'), out / f'{name}-{route}.pdf')
    pdflatex(guide_tex(week), out / 'guide-keys.pdf')
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        thumbs = {}
        for a in week.atoms:
            if not a.numbered:
                continue
            band = '2-3' if '2-3' in a.grades else a.grades[0]
            page = next(p.page for p in atoms.compose(week, band) if p.atom is a)
            stem = tmp / a.id.replace('.', '-')
            subprocess.run(['pdftoppm', '-r', '90', '-png', '-singlefile', '-f', str(page), '-l', str(page),
                            str(built[band]), str(stem)], check=True)
            thumbs[a.id] = stem.with_suffix('.png')
        pdflatex(menu_tex(week, thumbs), out / 'menu.pdf', thumbs.values())
    if args.tables:
        writer = PdfWriter()
        for item in args.tables.split(','):
            band, copies = item.split('=')
            src = out / f'{FILE_NAMES[band]}-first.pdf'
            for _ in range(int(copies)):
                writer.append(str(src))
        writer.write(out / 'session-pack.pdf')
    for f in sorted(out.glob('*.pdf')):
        print(f'{pages(f):3d} pages  {f}')


if __name__ == '__main__':
    main()
