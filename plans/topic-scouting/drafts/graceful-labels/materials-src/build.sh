#!/bin/sh
# Rebuild materials.pdf from gen_materials.py and check the delivered PDF.
set -e
cd "$(dirname "$0")"
python3 gen_materials.py
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error materials.tex > materials.buildlog 2>&1 || { tail -30 materials.buildlog; exit 1; }
done
if grep -E "Overfull|Underfull|Warning" materials.log; then echo "build warnings above"; exit 1; fi
cp materials.pdf ../materials.pdf
python3 check_materials.py ../materials.pdf | tee check-materials.txt
