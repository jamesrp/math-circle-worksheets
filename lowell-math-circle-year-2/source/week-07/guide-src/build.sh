#!/bin/sh
# Build the Week 7 adult guide: check every answer, compile, copy the PDF.
set -e
cd "$(dirname "$0")"
python3 check.py > check.log
tail -1 check.log
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
cp facilitator.pdf ../facilitator.pdf
grep -E "Overfull|Underfull .*badness 10000|Warning" facilitator.log || true
pdfinfo ../facilitator.pdf | grep Pages
