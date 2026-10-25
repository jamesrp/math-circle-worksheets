#!/bin/sh
# Rebuild figures and the three packets; copies PDFs to final/.
set -e
cd "$(dirname "$0")"
python3 gen.py
python3 check_geom.py > geom-check.txt
python3 check.py > answers-check.txt
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" > "$f.buildlog" 2>&1 || { tail -30 "$f.buildlog"; exit 1; }
  cp "$f.pdf" ../
done
