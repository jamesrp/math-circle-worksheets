#!/bin/sh
# Rebuild materials.pdf from scratch and check it:  sh build.sh
set -e
cd "$(dirname "$0")"
python3 make_materials.py
pdflatex -interaction=nonstopmode -halt-on-error materials.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error materials.tex > /dev/null
grep -E "Overfull|Underfull|Warning" materials.log || true
cp materials.pdf ../materials.pdf
rm -f materials.aux materials.log materials.pdf
python3 check_materials.py ../materials.pdf
