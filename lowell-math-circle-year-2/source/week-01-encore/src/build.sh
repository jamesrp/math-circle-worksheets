#!/bin/sh
# Build the three packets: figures from Python, then pdflatex.
set -e
cd "$(dirname "$0")"
python3 figs.py
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error $f.tex > /dev/null || { tail -30 $f.log; exit 1; }
  cp $f.pdf ../$f.pdf
done
