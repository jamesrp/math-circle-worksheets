#!/usr/bin/env python3
"""Render all PDF pages and record text/geometry; uses PyMuPDF and Pillow."""
from pathlib import Path
import argparse,json,hashlib
import pymupdf as fitz
from PIL import Image,ImageOps,ImageDraw

def fingerprint(path):
 d=fitz.open(path)
 return {'file':str(path),'pages':len(d),'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'page_evidence':[{'size':[p.rect.width,p.rect.height],'text_sha256':hashlib.sha256(p.get_text().encode()).hexdigest(),'pixel_sha256':hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples).hexdigest()} for p in d]}

def render(files,out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 record=[];shots=[]
 for path in files:
  d=fitz.open(path);r=fingerprint(path);r['outside_page_spans']=[]
  for i,p in enumerate(d):
   png=out/(Path(path).stem+f'-p{i+1:02}.png')
   p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(png)
   for b in p.get_text('dict')['blocks']:
    for line in b.get('lines',[]):
     for span in line.get('spans',[]):
      # Text extraction coordinates remain unrotated on /Rotate pages.
      bounds=fitz.Rect(span['bbox'])*p.rotation_matrix
      x0,y0,x1,y1=bounds
      if x0<10 or y0<10 or x1>p.rect.width-10 or y1>p.rect.height-10:
       r['outside_page_spans'].append({'page':i+1,'text':span['text'],'bbox':list(bounds)})
   shots.append((png,f'{Path(path).name} / page {i+1}'))
  record.append(r)
 for i in range(0,len(shots),2):
  c=Image.new('RGB',(1244,844),'#d9dee5');draw=ImageDraw.Draw(c)
  for j,(png,label) in enumerate(shots[i:i+2]):
   im=Image.open(png);im.thumbnail((606,784));x=8+j*622+(606-im.width)//2;c.paste(im,(x,36));draw.text((8+j*622,10),label,fill='black')
  c.save(out/f'contact-{i//2+1:03}.png')
 (out/'render-report.json').write_text(json.dumps(record,indent=2)+'\n')
 return record

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('pdfs',nargs='+');a=ap.parse_args();r=render(a.pdfs,a.out)
 print(json.dumps({'pdfs':len(r),'pages':sum(x['pages'] for x in r),'outside_spans':sum(len(x['outside_page_spans']) for x in r),'report':str(Path(a.out)/'render-report.json')}))
