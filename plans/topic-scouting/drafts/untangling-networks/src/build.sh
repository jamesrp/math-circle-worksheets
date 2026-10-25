#!/bin/sh
# Rebuild the three student packets from these sources.
set -e
cd "$(dirname "$0")"
python3 nets.py
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > /dev/null
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > /dev/null
  mv $f.pdf ../$f.pdf
done
rm -f *.aux *.log
