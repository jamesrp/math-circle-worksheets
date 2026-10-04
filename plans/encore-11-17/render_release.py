#!/usr/bin/env python3
from pathlib import Path
import fitz,json,sys
ROOT=Path(__file__).resolve().parents[2]
for n in map(int,sys.argv[1:]):
 folder=ROOT/f'tmp/encore-11-17/final-render/week-{n:02}';folder.mkdir(parents=True,exist_ok=True)
 results=[]
 for kind in ('student','guide'):
  tag=f'week-{n:02}-return-visit'+(''if kind=='student'else'-facilitator')
  pdf=ROOT/f'lowell-math-circle-year-2/week-{n:02}/{tag}.pdf';d=fitz.open(pdf)
  for i,page in enumerate(d):
   pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5));path=folder/f'{kind}-{i+1:02}.png';pix.save(path)
   spans=[span for block in page.get_text('dict')['blocks'] if 'lines'in block for line in block['lines']for span in line['spans']]
   outside=[span['text']for span in spans if span['bbox'][0]<20 or span['bbox'][2]>592 or span['bbox'][1]<12 or span['bbox'][3]>780]
   assert not outside,(pdf.name,i+1,outside)
   text=page.get_text();assert '\ufffd'not in text
   results.append({'file':str(pdf.relative_to(ROOT)),'page':i+1,'render':str(path.relative_to(ROOT)),'bounds_checked':True,'page_dimensions':list(page.rect),'visual_review':'pending owner full-page inspection'})
  print(n,kind,len(d),'pages')
 (ROOT/f'plans/encore-11-17/week-{n:02}-page-audit.json').write_text(json.dumps(results,indent=2)+'\n')
