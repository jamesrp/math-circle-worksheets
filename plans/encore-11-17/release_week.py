#!/usr/bin/env python3
"""Assemble new companions only, with portable sources and extracted rebuild audit."""
from pathlib import Path
import shutil,subprocess,zipfile,json,sys,hashlib,os,tempfile
ROOT=Path(__file__).resolve().parents[2]
for n in [int(x)for x in sys.argv[1:]]:
 tag=f'week-{n:02}-return-visit';run=ROOT/f'tmp/worksheet-runs/encore-week-{n:02}-20261004-v1'
 src=ROOT/f'lowell-math-circle-year-2/source/{tag}';week=ROOT/f'lowell-math-circle-year-2/week-{n:02}'
 if not (run/'final/return-visit.pdf').exists():raise SystemExit('final student missing')
 if src.exists():raise SystemExit('Refusing to replace existing source folder: '+str(src))
 src.mkdir(parents=True);shutil.copytree(run/'final/src',src/'student')
 for p in list((src/'student').rglob('*')):
  if p.is_file() and p.suffix in ('.pdf','.aux','.log','.out','.png','.pyc'):p.unlink()
 guide=ROOT/f'tmp/encore-11-17/guide-drafts/week-{n:02}/facilitator.tex';shutil.copy2(guide,src/'facilitator.tex')
 shutil.copy2(ROOT/'plans/encore-11-17/independent_checks.py',src/'independent_checks.py')
 shutil.copy2(ROOT/f'plans/encore-11-17/week-{n:02}-outline.md',src/'outline.md')
 provenance=src/'workflow';provenance.mkdir()
 for name in ('PROMPT.md','CRITIC.md','CRITIC-MATH.md','REVISE.md','review.md','review-math.md'):
  if (run/name).exists():shutil.copy2(run/name,provenance/name)
 build=r'''#!/bin/sh
set -eu
SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
OUTPUT_DIR=${1:-}
if [ -z "$OUTPUT_DIR" ]; then
  OUTPUT_DIR=$(mktemp -d "${TMPDIR:-/tmp}/WEEKTAG-build.XXXXXX")
fi
mkdir -p "$OUTPUT_DIR"
OUTPUT_DIR=$(CDPATH= cd -- "$OUTPUT_DIR" && pwd)
if [ -x /Library/TeX/texbin/pdflatex ]; then TEX=/Library/TeX/texbin/pdflatex; else TEX=pdflatex; fi
(cd "$SOURCE_DIR/student" && for PASS in 1 2; do "$TEX" -halt-on-error -interaction=nonstopmode -output-directory="$OUTPUT_DIR" return-visit.tex > "$OUTPUT_DIR/student-compile-$PASS.txt"; done)
mv "$OUTPUT_DIR/return-visit.pdf" "$OUTPUT_DIR/WEEKTAG.pdf"
(cd "$SOURCE_DIR" && for PASS in 1 2; do "$TEX" -halt-on-error -interaction=nonstopmode -output-directory="$OUTPUT_DIR" facilitator.tex > "$OUTPUT_DIR/guide-compile-$PASS.txt"; done)
mv "$OUTPUT_DIR/facilitator.pdf" "$OUTPUT_DIR/WEEKTAG-facilitator.pdf"
python3 "$SOURCE_DIR/independent_checks.py" WEEKNUM
printf '%s\n' "$OUTPUT_DIR/WEEKTAG.pdf" "$OUTPUT_DIR/WEEKTAG-facilitator.pdf"
'''.replace('WEEKTAG',tag).replace('WEEKNUM',str(n))
 (src/'build.sh').write_text(build);(src/'build.sh').chmod(0o755)
 readme=f'''# Week {n} return visits\n\nThree investigations within the Week {n} theme. Separate draft/unpiloted companions; existing base packets and guides are untouched. Readiness is labeled on each student page; the adult guide states prerequisites, precise facts, assumptions, materials, a common launch, first routes, flexible return-visit pacing, solutions, hints and extensions. Physical counter fit, preparation stock, procedures and classroom response are untested.\n\n- Student: `../../week-{n:02}/{tag}.pdf`\n- Adult: `../../week-{n:02}/{tag}-facilitator.pdf`\n\n## Clean build\n\nRequires Python3 standard library and pdfLaTeX with ordinary LaTeX packages including TikZ, extarticle, Latin Modern, Helvetica, fancyhdr, geometry and amsmath. No Python packages, custom fonts or figure assets outside this folder are needed to build.\n\nFrom this folder: `sh build.sh /absolute/output/directory`. Without an argument, a fresh system-temporary output folder is used and printed. This never copies into printable week folders or overwrites base files. In the repository, use a folder under `tmp/`.\n\nEditable student sources are in `student/`; `facilitator.tex` is the editable adult guide. `independent_checks.py {n}` recomputes the finite audit and writes local JSON. `workflow/` preserves the generated writer, critic, math and reviser instructions and reviews. `outline.md` records mathematical kernels and physical constraints. Reference PDFs preserve the delivered version. The ZIP is portable and has been rebuilt after extraction; page text and rendered pixel hashes were compared.\n\nThe tested worksheet workflow applies to student pages only. The adult guide was written separately and checked against the final student instances. All materials remain unpiloted, and no remote copy has been uploaded. Record which investigation/examples children actually use before choosing a future return visit.\n'''
 (src/'README.md').write_text(readme)
 built=ROOT/f'tmp/encore-11-17/release-build/{tag}';built.mkdir(parents=True,exist_ok=True)
 subprocess.run(['sh',str(src/'build.sh'),str(built)],check=True,capture_output=True,text=True)
 refs=src/'reference-pdfs';refs.mkdir()
 for suffix in ('','-facilitator'):
  name=f'{tag}{suffix}.pdf';dest=week/name
  if dest.exists():raise SystemExit('Refusing existing PDF '+str(dest))
  shutil.copy2(built/name,dest);shutil.copy2(built/name,refs/name)
 archive=src.parent/f'{tag}-source.zip'
 if archive.exists():raise SystemExit('Refusing existing source ZIP '+str(archive))
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED)as z:
  for p in sorted(src.rglob('*')):
   if p.is_file()and p!=archive and '__pycache__'not in p.parts:z.write(p,Path(tag)/p.relative_to(src))
 extracted=Path(tempfile.mkdtemp(prefix=f'{tag}-extracted-',dir='/tmp'))
 with zipfile.ZipFile(archive)as z:z.extractall(extracted)
 rebuild=extracted/'rebuilt'
 subprocess.run(['sh',str(extracted/tag/'build.sh'),str(rebuild)],check=True,capture_output=True,text=True,cwd='/tmp')
 # Pixel audit done by a separate runtime that supplies PyMuPDF.
 audit=ROOT/'tmp/encore-11-17/rebuild_audit.py'
 audit.write_text('''import sys,json,hashlib\nfrom pathlib import Path\nimport fitz\na,b,out=map(Path,sys.argv[1:]);res=[]\nfor p in sorted(a.glob('*.pdf')):\n q=b/p.name;d=fitz.open(p);e=fitz.open(q);assert len(d)==len(e)\n for i,(x,y)in enumerate(zip(d,e)):\n  assert x.get_text()==y.get_text(),(p.name,i,'text')\n  px=x.get_pixmap(matrix=fitz.Matrix(1.4,1.4));py=y.get_pixmap(matrix=fitz.Matrix(1.4,1.4))\n  h=hashlib.sha256(px.samples).hexdigest();assert h==hashlib.sha256(py.samples).hexdigest(),(p.name,i,'pixels')\n  res.append({'file':p.name,'page':i+1,'text_equal':True,'pixels_equal':True,'pixel_sha256':h})\nout.write_text(json.dumps(res,indent=2)+'\\n');print(len(res),'pages match after extracted-source rebuild')\n''')
 result=ROOT/f'plans/encore-11-17/week-{n:02}-rebuild-audit.json'
 subprocess.run([str(ROOT/'tmp/example-edit-env/bin/python'),str(audit),str(built),str(rebuild),str(result)],check=True)
 (ROOT/f'plans/encore-11-17/week-{n:02}-outside-build.json').write_text(json.dumps({'extracted_from':str(archive.relative_to(ROOT)),'fresh_system_temporary_extraction':str(extracted),'build_working_directory':'/tmp','rebuild_evidence':str(result.relative_to(ROOT)),'all_page_text_and_pixels_equal':True},indent=2)+'\n')
 shutil.rmtree(extracted)
 print('DELIVERED',tag)
