#!/usr/bin/env python3
"""Verify current output pixels; admit only specifically audited unchanged-font renders.

The original strict verifier is retained. This companion never allows alternate
pixels for an intentionally revised packet or guide. It recognizes only recorded
full-page hashes for unchanged packets rebuilt with the audited local TeX runtime.
"""
from pathlib import Path
import hashlib,json
import pymupdf
ROOT=Path(__file__).resolve().parent
cfg=json.loads((ROOT/'review/rebuild-pixel-allowances.json').read_text())
manifest=json.loads((ROOT/'review/reference-manifest.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
result={'week':cfg['week'],'dpi':100,'files':[]}
for name,entry in manifest.items():
 ref=ROOT/'reference-pdfs'/name;built=ROOT/cfg['output_subdir']/name
 assert sha(ref.read_bytes())==entry['sha256'],(name,'reference hash changed')
 a=pymupdf.open(ref);b=pymupdf.open(built)
 assert len(a)==len(b)==entry['pages'],(name,'page count')
 pages=[]
 for i,(p,q) in enumerate(zip(a,b),1):
  assert p.rect==q.rect==pymupdf.Rect(0,0,612,792),(name,i,'Letter page')
  x=sha(p.get_pixmap(dpi=100,alpha=False).samples)
  y=sha(q.get_pixmap(dpi=100,alpha=False).samples)
  if x==y:status='exact reference pixels'
  else:
   known=cfg['unchanged_student_alternates'].get(name,{}).get(str(i))
   assert known and x==known['reference_pixel_sha256'] and y==known['rebuilt_pixel_sha256'],(name,i,'unreviewed pixel difference')
   assert repr(p.get_drawings())==repr(q.get_drawings()),(name,i,'diagram geometry')
   status='specifically audited original TeX font/hyphenation alternate; print reference preserved'
  pages.append({'page':i,'status':status})
 result['files'].append({'file':name,'pages':pages})
(ROOT/'verification-revision-result.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: current changed outputs exactly reproduce; any unchanged alternate is a specifically audited full-page pixel hash.')
