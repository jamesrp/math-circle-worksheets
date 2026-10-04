#!/usr/bin/env python3
"""Compare rebuilt PDFs with the included release references.
Uses standard-library Python, pypdf, and Poppler's pdftoppm. Rendering is temporary.
Matching PDF bytes are not required because producer timestamps can change.
"""
from pathlib import Path
import hashlib, subprocess, tempfile
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
counts={'k-1':8,'grades-2-3':8,'grades-4-5':8,'facilitator-guide':15}
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix='nearest-sites-verify-') as temp:
    temp=Path(temp)
    for name,count in counts.items():
        ref=ROOT/'reference-pdfs'/f'{name}.pdf'
        built=ROOT/'build'/f'{name}.pdf'
        a,b=PdfReader(ref),PdfReader(built)
        assert len(a.pages)==len(b.pages)==count,(name,'page count')
        for i,(p,q) in enumerate(zip(a.pages,b.pages),1):
            assert tuple(p.mediabox)==tuple(q.mediabox)==(0,0,612,792),(name,i,'paper size')
            assert p.extract_text()==q.extract_text(),(name,i,'text differs')
        for label,pdf in [('reference',ref),('rebuilt',built)]:
            d=temp/label/name;d.mkdir(parents=True)
            subprocess.run(['pdftoppm','-r','100','-gray',str(pdf),str(d/'page')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        ra=sorted((temp/'reference'/name).glob('page-*.pgm'))
        rb=sorted((temp/'rebuilt'/name).glob('page-*.pgm'))
        assert len(ra)==len(rb)==count,(name,'rendered page count')
        for i,(p,q) in enumerate(zip(ra,rb),1):
            assert digest(p)==digest(q),(name,i,'rendered image differs')
        print(f'PASS {name}: {count} Letter pages, identical extracted text and 100-dpi grayscale renderings.')
print('PASS: all 39 rebuilt pages match the release references visually and in text.')
