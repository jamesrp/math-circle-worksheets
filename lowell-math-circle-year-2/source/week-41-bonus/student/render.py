#!/usr/bin/env python3
from pathlib import Path
import argparse
import pymupdf
p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
with pymupdf.open(a.pdf) as doc:
 for i,page in enumerate(doc):page.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(a.out/f'page-{i+1:02d}.png')
