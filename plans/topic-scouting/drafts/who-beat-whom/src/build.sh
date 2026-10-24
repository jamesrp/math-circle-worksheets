#!/bin/sh
# Rebuild the three packets from scratch: python3 gen.py checks every answer and writes figs/.
set -e
cd "$(dirname "$0")"
rm -rf figs __pycache__
python3 gen.py > answers-check.txt
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > /dev/null
  cp $f.pdf ../$f.pdf
done
rm -f *.aux *.log
