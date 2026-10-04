#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
from pypdf import PdfReader
R=Path(__file__).resolve().parent
pdf=R.parent/'build'/'facilitator-guide.pdf'
r=PdfReader(pdf)
assert len(r.pages)==21
for i,p in enumerate(r.pages,1):
 assert tuple(float(v) for v in p.mediabox)==(0,0,612,792)
 text=p.extract_text()
 assert 'Draft and unpiloted' in text and 'Unscheduled library week' in text
 assert len(text)>500,(i,len(text))
 assert '\ufffd' not in text
(R/'guide-text.txt').write_text('\n\n'.join(f'PAGE {i}\n{p.extract_text()}' for i,p in enumerate(r.pages,1)))
for name,info in json.loads((R/'student-input-manifest.json').read_text()).items():
 p=R.parent/'reference-pdfs'/name
 if p.exists():assert hashlib.sha256(p.read_bytes()).hexdigest()==info['sha256'],f'Student PDF changed: {name}'
report={'guide_pages':21,'page_size':'US Letter','draft_unscheduled_status_all_pages':True,'replacement_glyphs':False,'student_files_match_input_hashes':True,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'visual_review':'See VISUAL-REVIEW.md; automated checks do not replace page inspection.'}
(R/'pdf-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
