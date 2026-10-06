#!/usr/bin/env python3
"""Compare PDF text, dimensions and rendered pixels; PDF timestamps may differ."""
import argparse,hashlib,json
from pathlib import Path
import fitz
p=argparse.ArgumentParser();p.add_argument('original');p.add_argument('rebuilt');p.add_argument('--out');a=p.parse_args()
x,y=fitz.open(a.original),fitz.open(a.rebuilt)
report={'original':Path(a.original).name,'rebuilt':Path(a.rebuilt).name,'page_count_equal':len(x)==len(y),'pages':[]}
for i in range(min(len(x),len(y))):
 p,q=x[i],y[i];r={'page':i+1,'dimensions_equal':list(p.rect)==list(q.rect),'text_equal':p.get_text()==q.get_text(),'render_equal':p.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples==q.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples};report['pages'].append(r)
report['passed']=report['page_count_equal'] and all(all(v for k,v in r.items() if k!='page') for r in report['pages'])
s=json.dumps(report,indent=2)
if a.out:Path(a.out).write_text(s+'\n')
print(s)
raise SystemExit(0 if report['passed'] else 1)
