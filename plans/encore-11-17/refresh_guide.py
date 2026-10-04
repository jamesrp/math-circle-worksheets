"""Guarded guide refresh; punctuation-only mode preserves all existing guide content."""
from pathlib import Path
import subprocess,shutil,zipfile,sys,tempfile,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
punctuation_only='--punctuation-only' in sys.argv
numbers=[int(x) for x in sys.argv[1:] if x!='--punctuation-only']
old_prompt="Start with ``What can you try? and ``What would count as success? Check"
new_prompt="Start with ``What can you try?'' and ``What would count as success?'' Check"
for n in numbers:
 tag=f'week-{n:02}-return-visit';src=ROOT/f'lowell-math-circle-year-2/source/{tag}';cached=ROOT/f'tmp/encore-11-17/guide-drafts/week-{n:02}/facilitator.tex'
 assert (src/'facilitator.tex').read_bytes()==cached.read_bytes(),'Source changed outside this process; do not overwrite'
 old=src/'reference-pdfs'/f'{tag}-facilitator.pdf';dest=ROOT/f'lowell-math-circle-year-2/week-{n:02}/{tag}-facilitator.pdf'
 assert old.read_bytes()==dest.read_bytes(),'Delivered guide changed outside process'
 if punctuation_only:
  text=cached.read_text();assert text.count(old_prompt)==1 and new_prompt not in text
  cached.write_text(text.replace(old_prompt,new_prompt))
 else:subprocess.run(['python3',str(ROOT/'plans/encore-11-17/build_guides.py'),str(n)],check=True)
 shutil.copy2(cached,src/'facilitator.tex')
 build=ROOT/f'tmp/encore-11-17/release-build/{tag}';subprocess.run(['sh',str(src/'build.sh'),str(build)],check=True,capture_output=True,text=True)
 assert old.read_bytes()==dest.read_bytes(),'Delivered guide changed during build'
 shutil.copy2(build/dest.name,dest);shutil.copy2(build/dest.name,old)
 archive=src.parent/f'{tag}-source.zip'
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED)as z:
  for p in sorted(src.rglob('*')):
   if p.is_file()and '__pycache__'not in p.parts:z.write(p,Path(tag)/p.relative_to(src))
 extracted=Path(tempfile.mkdtemp(prefix=tag+'-refreshed-',dir='/tmp'))
 with zipfile.ZipFile(archive)as z:z.extractall(extracted)
 rebuilt=extracted/'rebuilt';subprocess.run(['sh',str(extracted/tag/'build.sh'),str(rebuilt)],check=True,capture_output=True,text=True,cwd='/tmp')
 result=ROOT/f'plans/encore-11-17/week-{n:02}-rebuild-audit.json'
 subprocess.run([str(ROOT/'tmp/example-edit-env/bin/python'),str(ROOT/'tmp/encore-11-17/rebuild_audit.py'),str(build),str(rebuilt),str(result)],check=True)
 (ROOT/f'plans/encore-11-17/week-{n:02}-outside-build.json').write_text(json.dumps({'extracted_from':str(archive.relative_to(ROOT)),'fresh_system_temporary_extraction':str(extracted),'build_working_directory':'/tmp','rebuild_evidence':str(result.relative_to(ROOT)),'all_page_text_and_pixels_equal':True,'refresh':'closing quotations only' if punctuation_only else 'guide content'},indent=2)+'\n')
 shutil.rmtree(extracted)
 subprocess.run([str(ROOT/'tmp/example-edit-env/bin/python'),str(ROOT/'plans/encore-11-17/render_release.py'),str(n)],check=True)
 print('Refreshed',n,'punctuation only' if punctuation_only else 'guide')
