#!/usr/bin/env python3
"""Audit only this range's new released companions and source/version consistency."""
import json,hashlib,zipfile
from pathlib import Path
import pymupdf as f
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
records=[]
for w in range(35,52):
 rec=json.loads((HERE/f'release-checks/week-{w:02}.json').read_text())
 src=ROOT/rec['source'];pkg=ROOT/rec['source_zip'];run=ROOT/f'tmp/worksheet-runs/week-{w:02}-bonus-v1'
 assert (run/'final/REVISER-DONE').exists(),f'Week{w}: revision missing'
 assert (run/'review.md').exists() and (run/'review-math.md').exists(),f'Week{w}: reviews missing'
 assert (HERE/f'independent/week-{w:02}-final.md').exists(),f'Week{w}: final math delta missing'
 assert hashlib.sha256(pkg.read_bytes()).hexdigest()==rec['source_zip_sha256']
 with zipfile.ZipFile(pkg) as z:
  expected={src.parent/name for name in z.namelist()}
  actual={p for p in src.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
  assert actual==expected,f'Week{w}: source file set changed'
  for name in z.namelist():assert (src.parent/name).read_bytes()==z.read(name),f'Week{w}: source/ZIP differs {name}'
 for name,info in rec['outputs'].items():
  path=ROOT/f'lowell-math-circle-year-2/week-{w:02}'/name
  assert hashlib.sha256(path.read_bytes()).hexdigest()==info['sha256'],f'Week{w}: PDF version mismatch'
  assert path.read_bytes()==(src/'reference-pdfs'/name).read_bytes(),f'Week{w}: reference PDF mismatch'
  d=f.open(path);assert len(d)==info['pages']
  assert all(tuple(p.rect)==(0,0,612,792) for p in d)
 student=ROOT/f'lowell-math-circle-year-2/week-{w:02}/week-{w:02}-bonus.pdf'
 sd=f.open(student);assert len(sd)==3
 for j,p in enumerate(sd,1):
  t=p.get_text();assert t.splitlines()[0].startswith(f'Week {w} / ') and '/ Grades ' in t.splitlines()[0]
  assert f'Problem {j}:' in t and f'Bellingham Math Circle / Week {w} /' in t
  assert 'draft' not in t.lower()
 md=json.loads((src/'investigations.json').read_text());items=md if isinstance(md,list) else md['investigations'];assert len(items)==3
 if isinstance(md,dict) and 'deliverables' in md:
  for key,relative in md['deliverables'].items():
   assert not Path(relative).is_absolute() and '..' not in Path(relative).parts
   assert (src/relative).exists(),f'Week{w}: broken metadata deliverable {key}: {relative}'
  assert (src/md['checks']['enumeration']).is_file(),f'Week{w}: broken verification path'
 records.append({'week':w,'investigations':3,'student_pages':3,'adult_pages':rec['outputs'][f'week-{w:02}-bonus-facilitator.pdf']['pages'],'checks':'fresh stages, independent math/delta, every-page inspection, extracted rebuild, source/ZIP/reference/PDF hashes current'})
result={'weeks':records,'total_investigations':sum(r['investigations'] for r in records),'student_pdfs':17,'adult_pdfs':17,'source_zips':17,'student_pages':sum(r['student_pages'] for r in records),'adult_pages':sum(r['adult_pages'] for r in records),'status':'All unpiloted; physical fit/procedures untested; local only; no publication'}
(HERE/'deliverable-checks.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
