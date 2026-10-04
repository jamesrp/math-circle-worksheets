#!/usr/bin/env python3
"""Stage a reviewed new week and test an extracted portable source package.

Run only after the coordinator has accepted every final PDF page and guide review.
Uses the project PyMuPDF/Pillow environment for the final comparison.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote

from inspect_pdfs import fingerprint

ROOT = Path(__file__).resolve().parents[2]
YEAR = ROOT / 'lowell-math-circle-year-2'
EXCLUDED = {'.aux', '.log', '.out', '.toc', '.pdf', '.pyc', '.fls', '.fdb_latexmk', '.synctex.gz'}


def copy_authored(src, dest):
    dest.mkdir(parents=True, exist_ok=False)
    for p in sorted(src.rglob('*')):
        rel = p.relative_to(src)
        if any(x in {'__pycache__', 'renders', 'rendered', 'output', 'build', 'qa', 'guide-qa', '.DS_Store'} for x in rel.parts):
            continue
        if not p.is_file() or p.suffix in EXCLUDED:
            continue
        if p.name in {'students.txt', 'facilitator.txt', 'materials.txt'}:
            continue
        q = dest / rel
        q.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, q)
        if p.name == 'README.md':
            text = q.read_text().replace('guide-src/', 'guide/').replace('/path/to/src/', '/path/to/student/')
            q.write_text(text + '\nPackage note: this README records the authored stage. External QA paths and\nprocess-status descriptions are historical; current verification is recorded in\n`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the\npackage root `python3 build.py --out output` to build every delivered PDF.\n')


def comparable(record):
    return {'pages': record['pages'], 'page_evidence': record['page_evidence']}


def rebase_note(path, destination):
    """Keep repository reference links valid after moving original source notes."""
    def link(match):
        label, raw = match.group(1), match.group(2)
        url = raw.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url) or url.startswith('#'):
            return match.group(0)
        local, _, anchor = url.partition('#')
        resolved = (path.parent / unquote(local)).resolve()
        # Included note-to-note links use their portable filenames.
        if resolved in RESEARCH_NOTES:
            rebased = resolved.name
        else:
            rebased = os.path.relpath(resolved, destination.parent)
        if anchor:
            rebased += '#' + anchor
        return f'[{label}](<{rebased}>)' if ' ' in rebased else f'[{label}]({rebased})'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, path.read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('week', type=int)
    ap.add_argument('--guide-tex', default='facilitator.tex')
    ap.add_argument('--notes', nargs='+', required=True, help='Repository-relative original research/provenance notes')
    ap.add_argument('--checked', action='store_true', help='Confirm final visual and independent guide review accepted')
    a = ap.parse_args()
    if not a.checked:
        raise SystemExit('Review final pages and independent guide review before staging.')
    n = f'{a.week:02d}'
    run = ROOT / f'tmp/worksheet-runs/week-{n}-new-v1'
    final = run / 'final'
    target = YEAR / f'week-{n}'
    source = YEAR / f'source/week-{n}'
    archive = YEAR / f'source/week-{n}-source.zip'
    if any(p.exists() for p in [target, source, archive]):
        raise SystemExit('Existing output conflict; inspect before changing anything.')
    global RESEARCH_NOTES
    RESEARCH_NOTES = {(ROOT / note).resolve() for note in a.notes}
    documents = [dict(kind='student', source_directory='student', tex_file='students.tex', output_file=f'week-{n}-students.pdf'),
                 dict(kind='guide', source_directory='guide', tex_file=a.guide_tex, output_file=f'week-{n}-facilitator.pdf')]
    if (final / 'materials.pdf').exists():
        documents.insert(1, dict(kind='materials', source_directory='student', tex_file='materials.tex', output_file=f'week-{n}-materials.pdf'))
    # These authored builders generate vector assets from mathematical data.
    # Preserve that work rather than assuming every source is a single TeX file.
    authored_commands = {53: ['python3', 'build.py', '--output', '.built'],
                         57: ['python3', 'build.py', '--output-dir', '.built'],
                         59: ['python3', 'build.py', '.built'],
                         61: ['python3', 'build.py', '.built']}
    if a.week in authored_commands:
        for item in documents:
            if item['source_directory'] == 'student':
                item.update(build_command=authored_commands[a.week],
                            built_pdf='.built/' + ('students.pdf' if item['kind'] == 'student' else 'materials.pdf'))
    with tempfile.TemporaryDirectory(prefix=f'week-{n}-release-') as stage_dir:
        stage = Path(stage_dir)
        package = stage / f'week-{n}'
        package.mkdir()
        copy_authored(final / 'src', package / 'student')
        copy_authored(final / 'guide-src', package / 'guide')
        shutil.copy2(Path(__file__).with_name('portable_build.py'), package / 'build.py')
        (package / 'build-manifest.json').write_text(json.dumps({'week': a.week, 'documents': documents}, indent=2) + '\n')
        provenance = package / 'provenance'
        provenance.mkdir()
        for note in a.notes:
            p = ROOT / note
            # Compute links for the actual final package location, not /tmp staging.
            (provenance / p.name).write_text(rebase_note(p, source / 'provenance' / p.name))
        (package / 'README.md').write_text(f'''# Week {a.week}: portable editable source

Current original student and facilitator sources, plus any necessary authored assets.
The student and guide READMEs give exact prerequisites, preparation, source references,
and any verification dependencies. Research/provenance notes are in `provenance/`.
Those notes record the research stage; the current PDFs are listed in the build manifest.
Their repository-relative reference links were updated for this package's local
location. Downloaded books, older packets and research caches are reference inputs
outside the ZIP; they are not required to build or check the included sources.
These adaptations are unpiloted. Digital diagram checks do not establish physical fit.

Build every delivered PDF from a fresh directory with Python 3 and TeX Live/MacTeX
(including TikZ, geometry, fancyhdr and the fonts named in the sources):

```sh
python3 build.py --out output
```

The build uses temporary directories and requires no repository paths or network.
Optional student/guide mathematical verifiers may require the packages documented in
their READMEs. No generated prompts, copied style exemplars, third-party books,
reference PDFs, rendered review images or old versions are included.

Outputs were verified against a clean ZIP extraction for exact text, dimensions and
rendered pixels in the production TeX/PyMuPDF environment. A later TeX/font version
can change rendering. Physical pretests and classroom piloting remain unperformed.
''')
        staged_zip = stage / archive.name
        with zipfile.ZipFile(staged_zip, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for p in sorted(package.rglob('*')):
                if p.is_file():
                    z.write(p, p.relative_to(stage))
        extracted = stage / 'clean-extraction'
        with zipfile.ZipFile(staged_zip) as z:
            z.extractall(extracted)
        rebuilt = stage / 'rebuilt'
        subprocess.run(['python3', str(extracted / f'week-{n}/build.py'), '--out', str(rebuilt)], check=True)
        records = []
        for item in documents:
            kind = item['kind']
            original = final / ('students.pdf' if kind == 'student' else f'{kind if kind == "materials" else "facilitator"}.pdf')
            fresh = rebuilt / item['output_file']
            expected, actual = fingerprint(original), fingerprint(fresh)
            if comparable(expected) != comparable(actual):
                raise SystemExit(f'Clean extraction differs: {item["output_file"]}')
            records.append({'output_file': item['output_file'], 'original': expected, 'extracted_rebuild': actual, 'exact_text_dimensions_pixels': True})
        target.mkdir()
        shutil.copytree(package, source)
        shutil.copy2(staged_zip, archive)
        for item in documents:
            kind = item['kind']
            original = final / ('students.pdf' if kind == 'student' else 'materials.pdf' if kind == 'materials' else 'facilitator.pdf')
            shutil.copy2(original, target / item['output_file'])
        evidence = ROOT / f'plans/new-themes-52-63/week-{n}/release-checks.json'
        evidence.write_text(json.dumps({'week': a.week, 'documents': records, 'source_zip': str(archive.relative_to(ROOT)),
                                       'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                                       'physical_pretests': 'unperformed', 'classroom_piloting': 'unperformed'}, indent=2) + '\n')
        print(json.dumps({'week': a.week, 'pdfs': len(documents), 'pages': sum(r['original']['pages'] for r in records), 'evidence': str(evidence.relative_to(ROOT))}))


if __name__ == '__main__':
    main()
