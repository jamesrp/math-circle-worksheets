#!/usr/bin/env python3
"""Write the portable source ZIP of a week stored as problem files.

    python3 package.py lowell-math-circle-year-2/source/week-43 \
        --zip shuffling-picture-cards-week43-editable-source.zip --top shuffling-picture-cards-week43-source

The ZIP is written beside week.toml and holds:
  <top>/                 the week's editable/ package: guide source, fonts, reference
                         PDFs, student LaTeX generated from the problem files, verifiers
  <top>/problem-files/   week.toml, figures.py, template.tex, problems/, guide/ and the
                         week's own scripts: the student pages' source
  <top>/problem-files/tools/   these tools (atoms.py, canvas.py, flow.py, build.py, compare.py)

Build intermediates (build/, build-state/, render/, __pycache__/, verification
results and built PDFs outside reference-pdfs/) are left out. Entries are sorted and
dated 2026-01-01 so the same files give the same ZIP.
"""
import argparse
import sys
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
TOOL_FILES = ('README.md', 'atoms.py', 'canvas.py', 'flow.py', 'build.py', 'compare.py')
SKIP_DIRS = {'build', 'build-state', 'render', '__pycache__'}
SKIP_FILES = {'verification-result.json', 'verification-revision-result.json'}
WEEK_SKIP = {'editable', '__pycache__'}


def editable_files(editable: Path):
    for f in sorted(editable.rglob('*')):
        rel = f.relative_to(editable)
        if f.is_dir() or SKIP_DIRS & set(rel.parts) or f.name in SKIP_FILES:
            continue
        if f.suffix in ('.pdf', '.log', '.aux') and rel.parts[0] not in ('reference-pdfs', 'approved-examples'):
            continue
        yield rel, f


def week_files(week: Path):
    for f in sorted(week.rglob('*')):
        rel = f.relative_to(week)
        if f.is_dir() or WEEK_SKIP & set(rel.parts) or rel.parts[0].startswith('archive') or f.suffix == '.zip':
            continue
        if rel.parts[0] == 'README.md':
            continue
        yield rel, f


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('week', help='the week folder holding week.toml, problems/ and editable/')
    ap.add_argument('--zip', required=True, help='ZIP file name, written beside week.toml')
    ap.add_argument('--top', required=True, help='top folder name inside the ZIP')
    args = ap.parse_args()
    week = Path(args.week).resolve()
    editable = week / 'editable'
    for need in (week / 'week.toml', editable):
        if not need.exists():
            sys.exit(f'error: {need} is missing; package.py packs a problem-file week with an editable/ package')
    entries = [(Path(args.top) / rel, f) for rel, f in editable_files(editable)]
    entries += [(Path(args.top) / 'problem-files' / rel, f) for rel, f in week_files(week)]
    entries += [(Path(args.top) / 'problem-files' / 'tools' / n, TOOLS / n) for n in TOOL_FILES]
    out = week / args.zip
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for arc, f in sorted(entries, key=lambda e: str(e[0])):
            info = zipfile.ZipInfo(str(arc), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if f.suffix in ('.py', '.sh') else 0o644) << 16
            z.writestr(info, f.read_bytes())
    print(f'{len(entries)} files -> {out}')


if __name__ == '__main__':
    main()
