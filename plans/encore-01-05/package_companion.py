#!/usr/bin/env python3
"""Install only NEW companion sources and package a portable extraction build."""
from pathlib import Path
import shutil,zipfile,json
import argparse
p=argparse.ArgumentParser();p.add_argument('week',type=int);a=p.parse_args();w=a.week
root=Path(__file__).resolve().parents[2]
run=root/f'tmp/worksheet-runs/encore-week-{w:02d}-20261004-v1'
source=root/f'lowell-math-circle-year-2/source/week-{w:02d}-return-visit'
outputs=root/f'lowell-math-circle-year-2/week-{w:02d}'
assert (run/'final/return-visit.pdf').exists()
# First install only; repeat updates allowed only inside this coordinator-owned new dir.
assert not source.exists(), f'Refusing to replace existing source directory: {source}'
source.mkdir()
for sub,src in [('student-src',run/'final/src'),('guide-src',run/'guide-src')]:
 dst=source/sub
 shutil.copytree(src,dst,ignore=shutil.ignore_patterns('*.aux','*.log','*.pdf','*.out','__pycache__','build','render'))
checks=source/'verification';checks.mkdir(exist_ok=True)
for filename in ['verify_kernels.py','verify_triangles.py']:
 text=(root/'plans/encore-01-05'/filename).read_text()
 # Make independent scripts fully portable: write reports beside themselves.
 text=text.replace("'plans/encore-01-05/kernel-checks.json'", "str(__import__('pathlib').Path(__file__).with_name('kernel-checks.json'))").replace("'plans/encore-01-05/triangle-checks.json'", "str(__import__('pathlib').Path(__file__).with_name('triangle-checks.json'))")
 (checks/filename).write_text(text)
actual=root/f'plans/encore-01-05/verify_week{w:02d}.py'
if actual.exists():
 shutil.copyfile(actual,checks/actual.name)
for filename in ['kernel-checks.json','triangle-checks.json']:
 shutil.copyfile(root/'plans/encore-01-05'/filename,checks/filename)
references=source/'reference-pdfs'; references.mkdir(exist_ok=True)
shutil.copyfile(run/'final/return-visit.pdf',references/f'week-{w:02d}-return-visit.pdf')
shutil.copyfile(run/'guide-build/facilitator.pdf',references/f'week-{w:02d}-return-visit-facilitator.pdf')
(source/'build.sh').write_text(f'''#!/bin/sh
set -eu
TASK_SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
TASK_OUTPUT_DIR=${{1:-$(mktemp -d "${{TMPDIR:-/tmp}}/math-circle-week-{w:02d}-return-visit.XXXXXX")}}
mkdir -p "$TASK_OUTPUT_DIR"
TASK_OUTPUT_DIR=$(CDPATH= cd -- "$TASK_OUTPUT_DIR" && pwd)
TASK_TEX_BUILD="$TASK_OUTPUT_DIR/tex-build"
mkdir -p "$TASK_TEX_BUILD/student" "$TASK_TEX_BUILD/guide"
TASK_PDFLATEX=${{PDFLATEX:-pdflatex}}
if ! command -v "$TASK_PDFLATEX" >/dev/null 2>&1; then
  if [ -x /Library/TeX/texbin/pdflatex ]; then TASK_PDFLATEX=/Library/TeX/texbin/pdflatex; else printf '%s\\n' 'pdfLaTeX with TikZ and Latin Modern is required.' >&2; exit 1; fi
fi
export SOURCE_DATE_EPOCH=1791072000
export FORCE_SOURCE_DATE=1
(cd "$TASK_SOURCE_DIR/student-src" && for TASK_TEX_PASS in 1 2; do "$TASK_PDFLATEX" -interaction=nonstopmode -halt-on-error -output-directory="$TASK_TEX_BUILD/student" return-visit.tex > "$TASK_TEX_BUILD/student/compile.txt"; done)
(cd "$TASK_SOURCE_DIR/guide-src" && for TASK_TEX_PASS in 1 2; do "$TASK_PDFLATEX" -interaction=nonstopmode -halt-on-error -output-directory="$TASK_TEX_BUILD/guide" facilitator.tex > "$TASK_TEX_BUILD/guide/compile.txt"; done)
cp "$TASK_TEX_BUILD/student/return-visit.pdf" "$TASK_OUTPUT_DIR/week-{w:02d}-return-visit.pdf"
cp "$TASK_TEX_BUILD/guide/facilitator.pdf" "$TASK_OUTPUT_DIR/week-{w:02d}-return-visit-facilitator.pdf"
printf '%s\\n' "$TASK_OUTPUT_DIR/week-{w:02d}-return-visit.pdf" "$TASK_OUTPUT_DIR/week-{w:02d}-return-visit-facilitator.pdf"
''')
(source/'README.md').write_text(f'''# Week {w} return-visit companion — review draft, unpiloted

These are **three new investigations**, separate from the base Week {w} packets and existing extras. No physical rehearsal or classroom piloting is claimed. The student packet is shared Grades 2–5, with genuine younger entries/readiness limits described in the adult guide.

- Current student PDF: `../../week-{w:02d}/week-{w:02d}-return-visit.pdf`.
- Adult guide: `../../week-{w:02d}/week-{w:02d}-return-visit-facilitator.pdf`.
- Reference PDFs: `reference-pdfs/` (the same local deliverables for comparing a rebuild).
- Student editable source: `student-src/return-visit.tex`.
- Adult editable source: `guide-src/facilitator.tex` and any included vector diagrams.

Print Letter, single-sided at 100% scale. Follow the guide's material/preparation instructions; printed compact sketches are records unless a page explicitly provides a working board. Choose one investigation for a visit and continue later according to interest/readiness.

## Portable build

Requires Python 3 for checks and pdfLaTeX with TikZ, Helvetica and Latin Modern (standard TeX Live/MacTeX). From any extracted directory:

```sh
sh build.sh /absolute/path/to/output-directory
```

The build writes only to the named output directory. With no argument it creates a temporary output directory and prints its path. `PDFLATEX` may name a compiler explicitly. Builds use a fixed PDF timestamp to support comparison. Source paths do not refer to this repository.

Optional independent checks, using only Python's standard library:

```sh
python3 verification/verify_kernels.py
python3 verification/verify_triangles.py
```

These finite checks cover the mathematical kernels of the five-week range and an independent Week 1 triangle-board enumeration. If present, `verification/verify_weekNN.py` checks the represented cases of this week and can be run with Python 3 in the same way. The student's own stage checks in `student-src/` check its actual examples. Review records and inventory are stored locally in `plans/encore-01-05/` and `plans/bonus-weeks-01-05.md`; those are not required to build.

Creation followed the worksheet writer → fresh adversarial critic → fresh independent math critic → fresh reviser workflow. The adult guide was a separate coordinator step and the workflow has not been validated with children. Local source package only; no remote upload/publication.
''')
# Package excludes compile/render outputs. Archive lives beside the source directory.
archive=source.parent/f'week-{w:02d}-return-visit-source.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(source.rglob('*')):
  if f.is_file() and f!=archive and f.suffix not in ['.aux','.log','.out']:
   z.write(f,Path(source.name)/f.relative_to(source))
print(source)
