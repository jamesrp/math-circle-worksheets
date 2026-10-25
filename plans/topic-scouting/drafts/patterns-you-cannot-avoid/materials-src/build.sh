#!/bin/sh
# Rebuild materials.pdf: generate the LaTeX, compile twice (overlay pictures need it), reject errors
# and overfull boxes, put the PDF in the folder above, then measure the delivered PDF.
set -e
cd "$(dirname "$0")"
python3 make_materials.py
pdflatex -interaction=nonstopmode -halt-on-error materials.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error materials.tex > /dev/null
if grep -E "^!|Overfull|Underfull|Warning" materials.log; then
  echo "materials.log has errors or warnings" >&2
  exit 1
fi
mv materials.pdf ../materials.pdf
rm -f materials.aux materials.log
python3 check_materials.py ../materials.pdf
