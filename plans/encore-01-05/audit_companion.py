#!/usr/bin/env python3
from pathlib import Path
import subprocess,shutil,zipfile,hashlib,json,sys,tempfile
import pymupdf
w=int(sys.argv[1]);root=Path(__file__).resolve().parents[2]
s=root/f'lowell-math-circle-year-2/source/week-{w:02d}-return-visit'
task=root/f'tmp/encore-01-05/delivery/week-{w:02d}'
task.mkdir(parents=True,exist_ok=True)
localbuild=task/'local-build'
prior_owned_hashes={f.name:hashlib.sha256(f.read_bytes()).digest() for f in localbuild.glob('week-*-return-visit*.pdf')}
subprocess.run(['sh',str(s/'build.sh'),str(localbuild)],check=True,capture_output=True,text=True)
# Synchronize reference PDFs and delivered finals from the same reproducible build.
for kind in ['return-visit','return-visit-facilitator']:
 n=f'week-{w:02d}-{kind}.pdf';dst=root/f'lowell-math-circle-year-2/week-{w:02d}'/n
 if dst.exists():
  assert n in prior_owned_hashes and hashlib.sha256(dst.read_bytes()).digest()==prior_owned_hashes[n],f'Refusing to overwrite a preexisting or user-edited deliverable {dst}'
 shutil.copyfile(localbuild/n,dst);shutil.copyfile(localbuild/n,s/'reference-pdfs'/n)
archive=s.parent/f'week-{w:02d}-return-visit-source.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(s.rglob('*')):
  if f.is_file() and f!=archive and f.suffix not in ['.aux','.log','.out'] and '__pycache__' not in f.parts:z.write(f,Path(s.name)/f.relative_to(s))
extract=Path(tempfile.mkdtemp(prefix=f'math-circle-week-{w:02d}-return-visit-',dir='/tmp')) if w==5 else task/'unrelated-extraction';extract.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:z.extractall(extract)
es=extract/s.name;rebuild=extract/'rebuild-output' if w==5 else task/'extracted-build'
subprocess.run(['sh',str(es/'build.sh'),str(rebuild)],check=True,cwd='/tmp',capture_output=True,text=True)
# Verification scripts require only standard Python.
for check in ['verify_kernels.py','verify_triangles.py'] + ([f'verify_week{w:02d}.py'] if (es/'verification'/f'verify_week{w:02d}.py').exists() else []):
 subprocess.run(['python3',str(es/'verification'/check)],check=True,cwd='/tmp',capture_output=True,text=True)
records=[]
for kind in ['return-visit','return-visit-facilitator']:
 n=f'week-{w:02d}-{kind}.pdf';a=localbuild/n;b=rebuild/n;da=pymupdf.open(a);db=pymupdf.open(b)
 assert len(da)==len(db)
 assert da.metadata==db.metadata and da.xref_length()==db.xref_length()
 different_objects=[i for i in range(1,da.xref_length()) if da.xref_object(i)!=db.xref_object(i) or da.xref_stream_raw(i)!=db.xref_stream_raw(i)]
 for i in different_objects:
  assert '/Type /XRef' in da.xref_object(i) and '/Type /XRef' in db.xref_object(i)
 import re
 assert re.sub(r'/ID \[.*?\]','/ID [path-dependent]',da.pdf_trailer(),flags=re.S)==re.sub(r'/ID \[.*?\]','/ID [path-dependent]',db.pdf_trailer(),flags=re.S)
 byte_reason='All nontrailer objects/streams and metadata equal; only trailer /ID can differ across build paths.'
 rd=task/'final-render'/kind;rd.mkdir(parents=True,exist_ok=True)
 pages=[]
 for i,(pa,pb) in enumerate(zip(da,db),1):
  assert pa.get_text()==pb.get_text()
  ia=pa.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5));ib=pb.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5));assert ia.samples==ib.samples
  ia.save(rd/f'page-{i}.png')
  text=pa.get_text();assert f'Week {w} /' in text and f'Bellingham Math Circle / Week {w} /' in text
  assert abs(pa.rect.width-612)<.01 and abs(pa.rect.height-792)<.01
  for block in pa.get_text('dict')['blocks']:
   for line in block.get('lines',[]):
    for span in line['spans']:
     x0,y0,x1,y1=span['bbox'];assert x0>=0 and y0>=0 and x1<=612.05 and y1<=792.05,(n,i,span)
  if kind=='return-visit':assert f'Problem {i}:' in text
  pages.append({'page':i,'header_footer':True,'Letter':True,'text_within_page':True,'image_sha256':hashlib.sha256(ia.samples).hexdigest(),'visual_inspection':'pending'})
 records.append({'path':str((root/f'lowell-math-circle-year-2/week-{w:02d}'/n).relative_to(root)),'pages':len(da),'source_extraction_text_and_pixels_equal':True,'source_extraction_bytes_equal':hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest(),'byte_difference_reason':byte_reason,'sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'page_checks':pages})
statusfile=root/'plans/encore-01-05/delivery-checks.json'
statuses=json.loads(statusfile.read_text()) if statusfile.exists() else {}
statuses[str(w)]={'outputs':records,'source_zip':str(archive.relative_to(root)),'unrelated_extraction_rebuild':True,'extracted_source_directory':str(es),'build_working_directory':'/tmp','rebuild_output_directory':str(rebuild),'extraction_outside_repository':not es.resolve().is_relative_to(root.resolve()),'standalone_independent_checks_passed':True,'student_stages':'fresh per-week writer, critic, independent math critic, reviser','adult_guide':'separate coordinator drafting; mathematical checks and all-page inspection','physical_rehearsal':'untested','classroom_piloting':'unpiloted','summary':'Rebuilt from extracted source, all output text/pixels matched; final page visual review pending'}
statusfile.write_text(json.dumps(statuses,indent=2)+'\n')
print(json.dumps({'week':w,'outputs':[(r['path'],r['pages'],r['source_extraction_bytes_equal']) for r in records],'renders':str(task/'final-render')},indent=2))
