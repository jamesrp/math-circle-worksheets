#!/bin/sh
# Rebuild the three final PDFs from these sources.
set -e
cd "$(dirname "$0")"
python3 gen.py
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > $f.log || { tail -30 $f.log; exit 1; }
  cp $f.pdf ../$f.pdf
done
