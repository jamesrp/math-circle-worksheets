#!/usr/bin/env python3
"""Compare build PDFs with release references using text and every page rendering."""
from pathlib import Path
import hashlib,json,subprocess,tempfile
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
M=json.loads((ROOT/'review'/'reference-manifest.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix='math-circle-render-check-') as td:
 t=Path(td);total=0
 for name,item in M.items():
  ref=ROOT/'reference-pdfs'/name;built=ROOT/'build'/name
  assert sha(ref)==item['sha256'],(name,'reference changed')
  a,b=PdfReader(ref),PdfReader(built)
  assert len(a.pages)==len(b.pages)==item['pages'],(name,'page count')
  for i,(p,q) in enumerate(zip(a.pages,b.pages),1):
   assert tuple(p.mediabox)==tuple(q.mediabox)==(0,0,612,792),(name,i,'paper size')
   assert p.extract_text()==q.extract_text(),(name,i,'text differs')
  dirs=[]
  for label,pdf in [('reference',ref),('rebuilt',built)]:
   d=t/label/name;d.mkdir(parents=True);dirs.append(d)
   subprocess.run(['pdftoppm','-r','100','-gray',str(pdf),str(d/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
  x,y=[sorted(d.glob('page-*.pgm')) for d in dirs]
  assert len(x)==len(y)==item['pages'],(name,'render count')
  for i,(p,q) in enumerate(zip(x,y),1):assert sha(p)==sha(q),(name,i,'rendered page differs')
  total+=item['pages'];print(f"PASS {name}: {item['pages']} Letter pages; identical extracted text and 100-dpi grayscale pixels.")
print(f'PASS: all {total} pages match. Byte differences from timestamps/document IDs are allowed only because content matches.')
