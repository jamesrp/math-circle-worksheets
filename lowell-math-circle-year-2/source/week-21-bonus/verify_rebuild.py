#!/usr/bin/env python3
"""Compare all rebuilt page text, Letter dimensions and rendered pixels to references."""
from pathlib import Path
import argparse,json,hashlib
import pymupdf as fitz
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--out',default='build');args=ap.parse_args()
build=Path(args.out).resolve();records=[]
for ref in sorted((root/'reference-pdfs').glob('*.pdf')):
 rebuilt=build/ref.name
 if not rebuilt.exists():raise SystemExit(f'Missing rebuilt {rebuilt}')
 a=fitz.open(ref);b=fitz.open(rebuilt)
 assert len(a)==len(b),(ref.name,len(a),len(b))
 for i,(p,q) in enumerate(zip(a,b)):
  assert tuple(round(x,4) for x in p.rect)==(0.0,0.0,612.0,792.0)
  assert p.rect==q.rect,(ref.name,i+1,'dimensions')
  assert p.get_text()==q.get_text(),(ref.name,i+1,'text')
  pp=p.get_pixmap(dpi=110,alpha=False);qq=q.get_pixmap(dpi=110,alpha=False)
  assert pp.samples==qq.samples,(ref.name,i+1,'pixels')
  for block in q.get_text('dict')['blocks']:
   for line in block.get('lines',[]):
    for span in line.get('spans',[]):
     x0,y0,x1,y1=span['bbox']
     assert x0>=-0.5 and y0>=-0.5 and x1<=612.5 and y1<=792.5,(ref.name,i+1,'offpage',span['text'])
 records.append({'file':ref.name,'pages':len(a),'page_text_match':True,'110dpi_pixels_match':True,'letter':True,'off_page_text':False,'reference_sha256':hashlib.sha256(ref.read_bytes()).hexdigest()})
(build/'rebuild-checks.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'packets':len(records),'pages':sum(r['pages'] for r in records),'passed':True}))
