#!/bin/sh
# Rebuild the three student PDFs from gen.py (run from this folder).
set -e
cd "$(dirname "$0")"
python3 gen.py
for n in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error "$n.tex" >/dev/null
  pdflatex -interaction=nonstopmode -halt-on-error "$n.tex" >/dev/null
done
rm -f *.aux *.log
