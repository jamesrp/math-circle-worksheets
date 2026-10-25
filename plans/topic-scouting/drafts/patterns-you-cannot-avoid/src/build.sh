#!/bin/sh
# Rebuild the three packets: check the mathematics, generate LaTeX, compile, move the PDFs to the folder above (final/).
set -e
cd "$(dirname "$0")"
python3 verify.py
python3 gen.py
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > /dev/null
  mv $f.pdf ../$f.pdf
  rm -f $f.aux $f.log
done
