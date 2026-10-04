#!/usr/bin/env python3
from pathlib import Path
import sys,shutil,zipfile,subprocess,tempfile,re
import pymupdf as fitz
R=Path(__file__).resolve().parents[2]
w=int(sys.argv[1]);wn=f'{w:02d}'
run=R/f'tmp/worksheet-runs/encore-week-{wn}-20261004-v1'
base=R/f'lowell-math-circle-year-2/source/week-{wn}-return-visit'
if base.exists():raise SystemExit(f'Refusing initial packaging over existing {base}')
base.mkdir();shutil.copytree(run/'final/src',base/'student',ignore=shutil.ignore_patterns('.build','__pycache__','*.pdf','*.aux','*.log'))
# Builder uses only a chosen output directory; all repository intermediates are in tmp/.
(base/'student/build.sh').unlink(missing_ok=True)
(base/'student/README.md').unlink(missing_ok=True)
pdf_check=base/'student/check_pdf.py'
if pdf_check.exists():
 s=pdf_check.read_text().replace('import sys\n','import sys\nimport tempfile\n')
 s=s.replace('PDF = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "return-visit.pdf"','''if len(sys.argv) < 2:
    raise SystemExit("Usage: python check_pdf.py PDF [QA_OUTPUT_DIR]; requires PyMuPDF")
PDF = Path(sys.argv[1]).resolve()
QA = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path(tempfile.mkdtemp(prefix="return-visit-pdf-qa-"))
QA.mkdir(parents=True, exist_ok=True)''')
 s=s.replace('render=ROOT/"render"','render=QA/"render"').replace('(ROOT/"build")','(QA/"build")').replace('(ROOT/"build"/"layout-check.json")','(QA/"build"/"layout-check.json")')
 pdf_check.write_text(s)
pdf_qa_flag = '--render-dir ' if pdf_check.exists() and '--render-dir' in pdf_check.read_text() else ''
topics={6:'Code breaking',7:'Take-away games',8:'Rook race and Nim',9:'Bouncing paths',10:'Bridges'}
style=(R/'plans/encore-06-10/guide-style.tex').read_text()
body=(R/f'plans/encore-06-10/week-{wn}-guide-body.tex').read_text()
(base/'facilitator.tex').write_text(style.replace('WEEK',str(w)).replace('TOPIC',topics[w]).replace('BODY',body))
tex_sources=(base/'student/return-visit.tex').read_text()+(base/'facilitator.tex').read_text()
latex_packages=sorted({name.strip() for group in re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}',tex_sources) for name in group.split(',')})
latex_package_list=', '.join(latex_packages)
shutil.copy(R/'plans/encore-06-10/verify-kernels.py',base/'verify.py')
for src in ('review.md','review-math.md'):
 if (run/src).exists():shutil.copy(run/src,base/src)
for note_path in (run/'writer-notes.md',run/'draft/writer-notes.md'):
 if note_path.exists():
  shutil.copy(note_path,base/'writer-notes.md')
  break
for note_path in (run/'final/revision-notes.md',run/'revision-notes.md'):
 if note_path.exists():
  shutil.copy(note_path,base/'revision-notes.md')
  break
independent_review=run/'math-review'
if (independent_review/'independent_check.py').exists():
 independent_dir=base/'independent-math';independent_dir.mkdir()
 for filename in ('independent_check.py','towns.json','README.md','independent-check.json'):
  if (independent_review/filename).exists():shutil.copy(independent_review/filename,independent_dir/filename)
build='''#!/bin/sh
set -eu
base_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 0 ]; then
  mkdir -p "$1"
  output_dir=$(CDPATH= cd -- "$1" && pwd)
else
  output_dir=$(mktemp -d "${TMPDIR:-/tmp}/week-WN-return-visit.XXXXXX")
fi
build_dir="$output_dir/.build"
mkdir -p "$build_dir"
student_work="$build_dir/student"
mkdir -p "$student_work"
cp -R "$base_dir/student/." "$student_work/"
if command -v pdflatex >/dev/null 2>&1; then
  tex_command=$(command -v pdflatex)
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  tex_command=/Library/TeX/texbin/pdflatex
else
  echo 'Requires pdfLaTeX, TikZ, lmodern and Source Sans Pro.' >&2
  exit 1
fi
python3 "$base_dir/verify.py"
(cd "$student_work" && if [ -f generate.py ]; then python3 generate.py > "$build_dir/generate.log"; fi)
(cd "$student_work" && for check_script in check*.py; do [ -f "$check_script" ] || continue; case "$check_script" in check_pdf.py|check_independent.py) continue;; esac; python3 "$check_script" > "$build_dir/$check_script.log"; done)
(cd "$student_work" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
(cd "$student_work" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
cp "$build_dir/return-visit.pdf" "$output_dir/week-WN-return-visit.pdf"
(cd "$base_dir" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex > "$build_dir/guide-build.log")
cp "$build_dir/facilitator.pdf" "$output_dir/week-WN-return-visit-facilitator.pdf"
printf '%s\\n' "$output_dir/week-WN-return-visit.pdf" "$output_dir/week-WN-return-visit-facilitator.pdf"
'''.replace('WN',wn)
(base/'build.sh').write_text(build);(base/'build.sh').chmod(0o755)
(base/'README.md').write_text(f'''# Week {w} return visits: {topics[w]}

Prepared October 4, 2026. **Unpiloted; physical material-fit and procedure rehearsal not performed.** Three distinct investigations in one shared student companion, with actual suitable bands on each page. The adult companion opens with precise facts, assumptions and limits, then gives practical entries and checked solutions. These files remain separate from every base packet and guide.

- Current student PDF: [week-{wn}-return-visit.pdf](../../week-{wn}/week-{wn}-return-visit.pdf).
- Adult PDF: [week-{wn}-return-visit-facilitator.pdf](../../week-{wn}/week-{wn}-return-visit-facilitator.pdf).
- Inventory, novelty and verification: [range inventory](../../../plans/bonus-weeks-06-10.md).

## Portable clean build

Requires Python 3.9 or later and pdfLaTeX. The source imports these LaTeX packages: {latex_package_list}. An `extarticle` class, when used by the student source, is provided by the extsizes collection. The Source Sans Pro font package is used for the guide. No external images, network access or repository-relative imports are required. The MacTeX binary is found automatically if it is not on PATH.

From any working directory run `sh /path/to/week-{wn}-return-visit/build.sh /tmp/week-{wn}-rebuild`. With no output argument a fresh system temporary directory is created and printed. The selected output directory holds the two PDFs and `.build/` intermediates. In the repository use an output under `tmp/pdfs/`; the builder never replaces current reviewed PDFs automatically.

`student/return-visit.tex` is editable student source; `facilitator.tex` is the adult source. `verify.py` independently verifies the kernels and every finite domain stated there without importing the student builder. Standard-library writer checks in `student/check*.py`, when present, check represented task instances too; the builder runs them and saves their output in `.build/`. The optional `check_pdf.py` and `check_independent.py` require PDF arguments and PyMuPDF and are excluded from the clean builder. Reviews and writer notes preserve the stage evidence; they are records, not classroom observations.

The builder copies student authoring files into `.build/student/` before working. If `student/generate.py` is present, that standard-library generator regenerates the TeX there from its included data. Edit `generate.py` and its data (for example `towns.json`) for such a packet; the adjacent TeX is the reviewable generated reference. Without a generator, edit the TeX directly. No rebuild changes the editable source directory.

The student source is compiled twice to resolve remembered TikZ page anchors. Copy the PDF only after both passes; a first-pass file can contain empty anchored pages.

When `student/check_pdf.py` is present, it is an optional geometry and render checker requiring PyMuPDF. After building, run `python /path/to/student/check_pdf.py /path/to/built/student.pdf {pdf_qa_flag}/tmp/week-{wn}-pdf-qa` with a Python environment that has PyMuPDF. Its outputs stay in the chosen QA directory. It is deliberately excluded from the standard-library-only clean builder.

When `student/check_independent.py` is present, run it separately with `python /path/to/student/check_independent.py /path/to/built/student.pdf --output /tmp/week-{wn}-independent.json` using that same PyMuPDF environment. It independently checks the mathematics and actual PDF vectors without importing the other checkers.

When `independent-math/` is present, it preserves the fresh mathematics reviewer's separate code and finite-result report. Its README or script argument help gives the optional built-PDF check; PyMuPDF is required. It remains outside the standard-library-only clean builder.

All five outlines and fresh per-week stages were assembled via the worksheet workflow. This week's run is `tmp/worksheet-runs/encore-week-{wn}-20261004-v1/`. Explicit companion scope selects one shared student collection instead of the harness's three copies. The workflow prompt set was unchanged. Guide writing is separate and untested.

Print US Letter at 100%. Give one investigation at a time; repeat, pause or return by readiness. Record the exact examples actually tried before marking material as used. No commits, uploads or remote currentness claims were made.
''')
out=R/f'tmp/pdfs/week-{wn}-return-visit-build'
subprocess.run(['sh',str(base/'build.sh'),str(out)],check=True)
week=R/f'lowell-math-circle-year-2/week-{wn}'
for name in [f'week-{wn}-return-visit.pdf',f'week-{wn}-return-visit-facilitator.pdf']:
 target=week/name
 if target.exists():raise SystemExit(f'Refusing overwrite {target}')
 shutil.copy(out/name,target)
 renderdir=R/f'tmp/encore-06-10/final-renders/{name[:-4]}';renderdir.mkdir(parents=True,exist_ok=True)
 d=fitz.open(target)
 for i,p in enumerate(d):p.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False).save(renderdir/f'page-{i+1:02d}.png')
 print(name,len(d),'pages')
zip_path=base.parent/f'{base.name}-source.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
 for p in base.rglob('*'):
  if p.is_file():z.write(p,p.relative_to(base.parent))
extract=Path(tempfile.mkdtemp(prefix=f'week-{wn}-return-visit-extracted-',dir='/tmp'))
with zipfile.ZipFile(zip_path) as z:z.extractall(extract)
rebuild=extract/'rebuilt';subprocess.run(['sh',str(extract/base.name/'build.sh'),str(rebuild)],check=True,cwd=extract)
checks=[f'Clean extracted build: {extract}; working directory is the unrelated extracted directory.']
for name in [f'week-{wn}-return-visit.pdf',f'week-{wn}-return-visit-facilitator.pdf']:
 a,b=fitz.open(week/name),fitz.open(rebuild/name);assert len(a)==len(b)
 for i,(pa,pb) in enumerate(zip(a,b)):
  assert pa.get_text()==pb.get_text(),(name,i,'text')
  assert pa.get_pixmap(alpha=False).samples==pb.get_pixmap(alpha=False).samples,(name,i,'pixels')
 if name.endswith('-return-visit.pdf'):
  combined='\n'.join(p.get_text() for p in a)
  for n in (1,2,3):assert f'Problem {n}' in combined,(name,'missing investigation',n)
 checks.append(f'{name}: {len(a)} pages, extracted-source text and pixels identical')
report=R/f'plans/encore-06-10/week-{wn}-package-check.txt';report.write_text('\n'.join(checks)+'\n')
print('\n'.join(checks));print(zip_path)
