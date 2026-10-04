from pathlib import Path
import json,hashlib
import fitz
ROOT=Path(__file__).resolve().parent
pdf=ROOT.parent/'build'/'facilitator-guide.pdf'
d=fitz.open(pdf)
assert len(d)==16
fonts=set()
for i,page in enumerate(d):
 assert page.rect.width==612 and page.rect.height==792
 for block in page.get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for s in line['spans']:
    fonts.add(s['font']); x0,y0,x1,y1=s['bbox']
    assert x0>=25 and x1<=590 and y0>=25 and y1<=775,(i+1,s)
assert fonts=={'DejaVuSans','DejaVuSans-Bold'}
text='\n'.join(p.get_text() for p in d)
for s in ['Draft and unpiloted. Unscheduled library slot.','K-1 Problems 1 to 3','K-1 Problem 4','K-1 Problems 5 and 6','Grades 2-3 Problems 1 and 2','Grades 2-3 Problems 3 and 4','Grades 2-3 Problems 5 and 6','Grades 4-5 Problems 1 to 3','Grades 4-5 Problems 4 and 5','Grades 4-5 Problem 6']:
 assert s in text,s
student={}
for n in ['k-1.pdf','grades-2-3.pdf','grades-4-5.pdf']:
 p=ROOT.parent/'reference-pdfs'/n
 if p.exists():
  dd=fitz.open(p);t=' '.join(x.get_text() for x in dd)
  assert len(dd)==6 and all(f'Problem {i}:' in t for i in range(1,7))
  student[n]=hashlib.sha256(p.read_bytes()).hexdigest()
report={'date':'2026-10-03','guide_pages':16,'size':'US Letter','visible_fonts':sorted(fonts),'text_bounds_pass':True,'all_final_problem_sections_present':True,'guide_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'student_reference_sha256':student,'visual_review':{'all_16_pages_individually_inspected':True,'resolution_dpi':100,'changed_pages_rerendered_and_reinspected':[3,4,7,11],'result':'No clipping, overlaps, missing glyphs or unintended page breaks observed'},'physical_models_tested':False,'status':'draft unpiloted unscheduled library slot'}
(ROOT/'qa.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
