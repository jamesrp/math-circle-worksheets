#!/bin/sh
# Rebuild the Week 8 adult guide: recheck every answer, redraw the answer
# pictures, compile, and move the PDF to ../facilitator.pdf.
set -e
cd "$(dirname "$0")"
python3 check.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -c 'Overfull' facilitator.log || true
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.out
pdfinfo ../facilitator.pdf | grep Pages
