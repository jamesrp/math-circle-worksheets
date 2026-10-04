"""Synchronize relocated build instructions and recheck affected portable ZIPs."""
import argparse,hashlib,json,subprocess,tempfile,zipfile
from pathlib import Path
from inspect_pdfs import fingerprint
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('weeks',nargs='+',type=int);a=ap.parse_args()
for n in a.weeks:
 package=root/f'lowell-math-circle-year-2/source/week-{n:02}'
 archive=package.parent/f'week-{n:02}-source.zip'
 for p in [package/'student/README.md',package/'guide/README.md']:
  content=p.read_text().replace('guide-src/', 'guide/').replace('/path/to/src/', '/path/to/student/')
  if 'Package note:' not in content:
   content+='\nPackage note: this README records the authored stage. External QA paths and\nprocess-status descriptions are historical; current verification is recorded in\n`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the\npackage root `python3 build.py --out output` to build every delivered PDF.\n'
  p.write_text(content)
 with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
  for p in sorted(package.rglob('*')):
   if p.is_file():z.write(p,p.relative_to(package.parent))
 with tempfile.TemporaryDirectory(prefix=f'week-{n}-doc-refresh-') as work:
  work=Path(work)
  with zipfile.ZipFile(archive) as z:z.extractall(work/'extract')
  rebuilt=work/'out';subprocess.run(['python3',str(work/'extract'/package.name/'build.py'),'--out',str(rebuilt)],check=True)
  for doc in json.loads((package/'build-manifest.json').read_text())['documents']:
   f=doc['output_file'];actual=fingerprint(rebuilt/f);expected=fingerprint(root/f'lowell-math-circle-year-2/week-{n:02}'/f)
   assert actual['pages']==expected['pages'] and actual['page_evidence']==expected['page_evidence']
 evidence=root/f'plans/new-themes-52-63/week-{n:02}/release-checks.json';record=json.loads(evidence.read_text())
 record.update(zip_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),relocated_readme_paths_synchronized=True,post_documentation_clean_extraction_rebuild='exact text/dimensions/pixels')
 evidence.write_text(json.dumps(record,indent=2)+'\n')
 print(f'Week {n}: README paths, source ZIP and exact clean rebuild synchronized')
