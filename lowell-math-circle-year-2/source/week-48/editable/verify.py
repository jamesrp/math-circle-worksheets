#!/usr/bin/env python3
"""All-page text, geometry and 100-dpi raster comparison against approved PDFs."""
from pathlib import Path
import fitz,json,hashlib
ROOT=Path(__file__).resolve().parent
out={"dpi":100,"files":[]}
for name in ['k-1','grades-2-3','grades-4-5','facilitator-guide']:
 a=fitz.open(ROOT/'reference-pdfs'/(name+'.pdf'));b=fitz.open(ROOT/(name+'.pdf'))
 assert len(a)==len(b),(name,'page count')
 pages=[]
 for i,(x,y) in enumerate(zip(a,b),1):
  assert x.rect==y.rect,(name,i,'page geometry')
  assert x.get_text()==y.get_text(),(name,i,'text')
  px=x.get_pixmap(dpi=100,alpha=False);py=y.get_pixmap(dpi=100,alpha=False)
  assert (px.width,px.height,px.samples)==(py.width,py.height,py.samples),(name,i,'pixels')
  pages.append({"page":i,"text_sha256":hashlib.sha256(x.get_text().encode()).hexdigest(),"pixels_sha256":hashlib.sha256(px.samples).hexdigest()})
 out['files'].append({"file":name+'.pdf',"pages":pages,"status":"PASS"})
(ROOT/'verification-result.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all',sum(len(x['pages']) for x in out['files']),'pages match in text, geometry and pixels at 100 dpi.')
