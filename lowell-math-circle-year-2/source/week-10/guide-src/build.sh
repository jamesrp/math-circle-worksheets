#!/bin/sh
# Rebuild the adult guide: check every answer, draw the K-1 answer pictures, compile, copy to final/.
set -e
cd "$(dirname "$0")"
python3 check_answers.py > /dev/null      # writes check-output.txt; fails if any printed answer is wrong
python3 make_figures.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -E "Overfull|Underfull|Warning" facilitator.log || true
cp facilitator.pdf ../facilitator.pdf
pdfinfo ../facilitator.pdf | grep Pages
