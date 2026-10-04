#!/bin/bash
# usage: ./build.sh name  -> compiles name.tex, renders png/name-*.png and png/name-sheet.png
cd "$(dirname "$0")"
n=$1
xelatex -interaction=nonstopmode -halt-on-error $n.tex > build-$n.log 2>&1 || { echo FAIL; grep -A3 "^!" $n.log | head -20; exit 1; }
grep -E "Overfull|^!" $n.log | head
pdfinfo $n.pdf | grep Pages
rm -f png/$n-*.png
pdftoppm -r ${2:-50} -png $n.pdf png/$n
python3 - "$n" << 'PY'
import sys, glob
from PIL import Image
n=sys.argv[1]
fs=sorted(glob.glob(f'png/{n}-[0-9]*.png'))
ims=[Image.open(f) for f in fs]
w,h=ims[0].size
cols=3; rows=(len(ims)+cols-1)//cols
out=Image.new('RGB',(w*cols,h*rows),'white')
for k,im in enumerate(ims): out.paste(im,((k%cols)*w,(k//cols)*h))
out.save(f'png/{n}-sheet.png')
PY
