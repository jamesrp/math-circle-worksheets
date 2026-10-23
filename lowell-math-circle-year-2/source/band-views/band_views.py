#!/usr/bin/env python3
"""Band slices and one-page menus for the shared student packets.

Weeks 52-84, 88-93 and 97 print one shared packet whose page headers name a
grade range. Each week has a checked page index in indexes/. This script

  draft  writes an index for a week from its page headers (never overwrites);
  build  checks every index against its PDF, then writes the band slices,
         a page menu per week and the folder README in ../../band-views/;
  readme rewrites only the folder README.

    python3 band_views.py draft week-52
    python3 band_views.py build

The README also lists the views published here for weeks stored as problem files
(their week-NN/ folders hold a week-NN-menu.pdf and have no index); the problem-file
tools write those (../problem-files/build.py --publish), and build leaves them alone.

A slice holds the pages whose range includes the band, plus any earlier page
whose opening rules the index lists for that band (`rules_for`). Pages are
copied unchanged, so printed problem and page numbers match the full packet
and its guide. A slice is written only when it is shorter than the packet.

An index may also list `guide_routes`, for example `guide_routes = { "K-1" = [1, 6] }`:
the pages an adult-led route in the week's guide uses for a band whose pages are
headed for older children. Those pages join that band's slice, and the menu and
README say the route is the guide's.
"""
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
YEAR2 = HERE.parents[1]
OUT = YEAR2 / 'band-views'
INDEXES = HERE / 'indexes'
ORDER = 'K12345'
BANDS = {'K-1': ('k-1', 'K–1'), '2-3': ('grades-2-3', 'Grades 2–3'), '4-5': ('grades-4-5', 'Grades 4–5')}
HEADER = re.compile(r'^Week (\d+) / (.*) / (?:Grades )?([K1-5])[–-]([1-5])\b')
FOOTER = re.compile(r'Bellingham Math Circle / Week \d+ / (\S+)')


def page_text(pdf, n):
    return subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), str(pdf), '-'],
                          capture_output=True, text=True, check=True).stdout


def read_pages(pdf):
    """Header range, problem numbers and footer id of every page."""
    rows, topic, footer, last = [], None, None, None
    for n in range(1, len(PdfReader(pdf).pages) + 1):
        text = page_text(pdf, n)
        m = next((HEADER.match(l.strip()) for l in text.splitlines() if HEADER.match(l.strip())), None)
        label = f'{m[3]}-{m[4]}' if m else last
        topic = topic or (m[2] if m else None)
        f = FOOTER.search(text)
        footer = footer or (f[1] if f else None)
        rows.append({'page': n, 'grades': label, 'problems': [int(p) for p in re.findall(r'Problem (\d+):', text)]})
        last = label
    return topic, footer, rows


def span(label):
    lo, hi = label.split('-')
    return set(ORDER[ORDER.index(lo):ORDER.index(hi) + 1])


def slice_pages(index, band):
    want = span(band)
    pages = [p['page'] for p in index['page'] if span(p['grades']) & want]
    routed = guide_route(index, band)
    if not pages:
        return sorted(routed)
    rules = [p['page'] for p in index['page'] if band in p.get('rules_for', []) and p['page'] < pages[-1]]
    return sorted(set(pages) | set(rules) | set(routed))


def guide_route(index, band):
    """Pages an adult-led route in the guide uses for this band (index key guide_routes)."""
    return index.get('guide_routes', {}).get(band, [])


def ranges(pages):
    out, start = [], None
    for i, p in enumerate(pages):
        start = p if start is None else start
        if i + 1 == len(pages) or pages[i + 1] != p + 1:
            out.append(f'{start}' if start == p else f'{start}–{p}')
            start = None
    return ', '.join(out)


def draft(week):
    target = INDEXES / f'{week}.toml'
    if target.exists():
        sys.exit(f'{target} exists; edit it by hand or delete it first')
    pdf = YEAR2 / week / f'{week}-students.pdf'
    topic, footer, rows = read_pages(pdf)
    lines = [f'# Page index for {week}, read from its page headers. Check each page by eye,',
             '# then add rules_for to any page whose opening rules a later band needs.',
             f'week = {int(week[5:])}', f'topic = "{topic}"', f'source = "{week}/{pdf.name}"',
             f'footer = "{footer}"', 'checked = ""', '']
    for r in rows:
        lines += ['[[page]]', f'page = {r["page"]}', f'grades = "{r["grades"]}"', f'problems = {r["problems"]}', '']
    INDEXES.mkdir(exist_ok=True)
    target.write_text('\n'.join(lines))
    print(f'wrote {target}')


def check(index):
    """The index must still describe the PDF: same pages, ranges and problems."""
    topic, footer, rows = read_pages(YEAR2 / index['source'])
    problems = []
    if footer != index['footer']:
        problems.append(f'footer {footer} != {index["footer"]}')
    if len(rows) != len(index['page']):
        problems.append(f'{len(rows)} pages, index has {len(index["page"])}')
    for r, p in zip(rows, index['page']):
        if (r['page'], r['grades'], r['problems']) != (p['page'], p['grades'], p['problems']):
            problems.append(f'page {r["page"]}: PDF {r["grades"]} {r["problems"]}, index {p["grades"]} {p["problems"]}')
    if not index.get('checked'):
        problems.append('index not yet checked by eye')
    return problems


def pdflatex(tex, out, files):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for name, f in files.items():
            shutil.copy(f, tmp / name)
        (tmp / 'menu.tex').write_text(tex)
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'menu.tex'],
                           cwd=tmp, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f'pdflatex failed for {out}:\n{r.stdout[-2000:]}')
        shutil.copy(tmp / 'menu.pdf', out)


def tex_escape(s):
    return s.replace('&', r'\&').replace('%', r'\%').replace('#', r'\#').replace('_', r'\_')


def menu(index, pdf, slices, out):
    week, topic = index['week'], tex_escape(index['topic'])
    SEP = r' \textperiodcentered{} '
    total = len(index['page'])
    summary = []
    for band, (_, name) in BANDS.items():
        pages = slices.get(band, [])
        if not pages:
            summary.append(f'{name}: no pages')
        elif len(pages) == total:
            summary.append(f'{name}: whole packet')
        else:
            summary.append(f'{name}: pp.~{ranges(pages)} ({len(pages)} of {total})')
        if guide_route(index, band):
            summary[-1] += r", the guide's adult-led route"
    cells = []
    for p in index['page']:
        probs = p['problems']
        plabel = ('P' + (str(probs[0]) if len(probs) == 1 else f'{probs[0]}–{probs[-1]}')) if probs else 'no numbered problem'
        extra = (r'\\rules for ' + ', '.join(BANDS[b][1] for b in p['rules_for'])) if p.get('rules_for') else ''
        routed = [BANDS[b][1] for b in BANDS if p['page'] in guide_route(index, b)]
        extra += (r'\\guide route for ' + ', '.join(routed)) if routed else ''
        grades = p['grades'].replace('-', '–')
        cells.append(rf'''\begin{{minipage}}[t]{{43mm}}\centering
\fbox{{\includegraphics[page={p['page']},width=42mm]{{packet.pdf}}}}\\[1pt]
{{\scriptsize page {p["page"]} \textperiodcentered{{}} {grades} \textperiodcentered{{}} {plabel}{extra}\par}}
\end{{minipage}}''')
    grid = ''
    for i in range(0, len(cells), 4):
        row = cells[i:i + 4] + [r'\begin{minipage}[t]{43mm}\mbox{}\end{minipage}'] * (4 - len(cells[i:i + 4]))
        grid += r'\noindent' + r'\hfill'.join(row) + '\\par\\vspace{3mm}\n'
    tex = rf'''\documentclass[10pt,letterpaper]{{article}}
\usepackage[margin=12mm,top=14mm,bottom=16mm]{{geometry}}
\usepackage[T1]{{fontenc}}\usepackage{{helvet}}\renewcommand{{\familydefault}}{{\sfdefault}}
\usepackage{{graphicx,fancyhdr}}\pagestyle{{fancy}}\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}
\fancyfoot[L]{{\footnotesize Bellingham Math Circle / Week {week} / page menu for {index["footer"]}}}
\setlength{{\parindent}}{{0pt}}\setlength{{\fboxsep}}{{0pt}}
\pdfinfoomitdate=1 \pdftrailerid{{}} \pdfsuppressptexinfo=-1
\begin{{document}}
{{\large\bfseries Week {week} / {topic} / Page menu}}\par\vspace{{1mm}}
{{\small For adults. Band slices print the pages whose range includes the band, with page and problem numbers unchanged.\\
{SEP.join(summary)}\par}}\vspace{{3mm}}
{grid}
\end{{document}}
'''
    pdflatex(tex, out, {'packet.pdf': pdf})


def problem_file_rows(indexed):
    """README rows for views published from problem files: week-NN/ folders without an index."""
    rows = []
    for folder in sorted(OUT.glob('week-*'), key=lambda p: int(p.name[5:])):
        n = int(folder.name[5:])
        menu_pdf = folder / f'{folder.name}-menu.pdf'
        toml = YEAR2 / 'source' / f'week-{n:02d}' / 'week.toml'
        if n in indexed or not menu_pdf.exists() or not toml.exists():
            continue
        meta = tomllib.loads(toml.read_text())
        topic = meta['topic']
        # The week's own bands, in week.toml order; a band outside K-1, 2-3, 4-5, or one that sets
        # file (Week 86's 4-5 band prints week-86-upper.pdf), names its file.
        bands = [BANDS[b] if b in BANDS and 'file' not in style else (style.get('file', f'grades-{b}'), style['header'].replace('--', '–'))
                 for b, style in meta.get('bands', {}).items()] or list(BANDS.values())
        cells = []
        for route in ('first', 'return'):
            links = [f'[{name}]({folder.name}/{folder.name}-{fname}-{route}.pdf)'
                     for fname, name in bands if (folder / f'{folder.name}-{fname}-{route}.pdf').exists()]
            cells.append(' · '.join(links) or '—')
        packets = ' · '.join(f'[{name}](../week-{n:02d}/week-{n:02d}-{fname}.pdf)' for fname, name in bands
                             if (YEAR2 / f'week-{n:02d}' / f'week-{n:02d}-{fname}.pdf').exists())
        rows.append(f'| {n} | {topic} | {packets} | {cells[0]} | {cells[1]} | [menu]({folder.name}/{menu_pdf.name}) | '
                    f'[key]({folder.name}/{folder.name}-key.pdf) |')
    return rows


def build(write=True):
    OUT.mkdir(exist_ok=True)
    table, failures, indexed = [], [], set()
    for path in sorted(INDEXES.glob('week-*.toml'), key=lambda p: int(p.stem[5:])):
        index = tomllib.loads(path.read_text())
        problems = check(index)
        if problems:
            failures.append(f'{path.name}: ' + '; '.join(problems))
            continue
        week = f'week-{index["week"]}'
        indexed.add(index['week'])
        pdf = YEAR2 / index['source']
        reader = PdfReader(pdf)
        folder = OUT / week
        if write:
            if folder.exists():
                shutil.rmtree(folder)
            folder.mkdir()
        total = len(index['page'])
        slices = {b: slice_pages(index, b) for b in BANDS}
        cells = []
        for band, (fname, name) in BANDS.items():
            pages = slices[band]
            if not pages:
                cells.append('—')
            elif len(pages) == total:
                cells.append('whole packet')
            else:
                out = folder / f'{week}-{fname}.pdf'
                if write:
                    w = PdfWriter()
                    for n in pages:
                        w.add_page(reader.pages[n - 1])
                    w.add_metadata({'/Title': f'Week {index["week"]} {index["topic"]}, {name} pages'})
                    w.write(out)
                cells.append(f'[{len(pages)} of {total}]({week}/{out.name}): pp. {ranges(pages)}'
                             + (", the guide's adult-led route" if guide_route(index, band) else ''))
        if write:
            menu(index, pdf, slices, folder / f'{week}-menu.pdf')
        table.append(f'| {index["week"]} | {index["topic"]} | [{total} pages](../{index["source"]}) | '
                     + ' | '.join(cells) + f' | [menu]({week}/{week}-menu.pdf) |')
    readme = OUT / 'README.md'
    readme.write_text(README_HEAD + '\n'.join(table) + '\n' + README_TAIL
                      + PROBLEM_FILES_HEAD + '\n'.join(problem_file_rows(indexed)) + '\n')
    print(f'{len(table)} weeks {"built" if write else "listed"}; {len(failures)} failed')
    for f in failures:
        print('  ' + f)
    return not failures


README_HEAD = '''# Band views of the shared packets

Weeks 52–84, 88–93 and 97 print one shared student packet whose page headers name a grade range. This folder gives each band its own pages and each week a one-page menu of its pages, without changing the packets. Built by [source/band-views/](../source/band-views/README.md) from checked page indexes.

A slice holds the pages whose range includes the band (a Grades 3–5 page is in both the 2–3 and 4–5 slices), plus an earlier page whose opening rules that band needs. Pages are copied unchanged, so problem numbers, page numbers and the guide's references all match the full packet. Print at 100%. A slice exists only when it is shorter than the packet; otherwise print the packet. Weeks 85–87 already print a shared and an upper packet, so they are not repeated here.

The packets and these views are unpiloted, as their weeks are.

| Week | Topic | Packet | K–1 | Grades 2–3 | Grades 4–5 | Menu |
|---|---|---|---|---|---|---|
'''
README_TAIL = '''
Rebuild after any change to a listed packet: `python3 lowell-math-circle-year-2/source/band-views/band_views.py build`. The build stops for a week whose index no longer matches its PDF.
'''
PROBLEM_FILES_HEAD = '''
## Weeks stored as problem files

A week stored as [problem files](../source/problem-files/README.md) has separate band packets, printed from its week folder. Its other views are built from the same files and published here: first-route and return packets for each band, which keep the full packet's problem numbers; a one-page problem menu; and a key arranged by problem, which repeats the answers of the week's adult guide. The guide remains the adult text to print. Rebuild with `python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-NN --out tmp/week-NN-views --publish lowell-math-circle-year-2/band-views/week-NN`, then `python3 lowell-math-circle-year-2/source/band-views/band_views.py readme`.

| Week | Topic | Packets | First route | Return visits | Menu | Key |
|---|---|---|---|---|---|---|
'''


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'draft':
        for w in sys.argv[2:]:
            draft(w)
    elif sys.argv[1:] == ['build']:
        sys.exit(0 if build() else 1)
    elif sys.argv[1:] == ['readme']:
        sys.exit(0 if build(write=False) else 1)
    else:
        sys.exit(__doc__)
