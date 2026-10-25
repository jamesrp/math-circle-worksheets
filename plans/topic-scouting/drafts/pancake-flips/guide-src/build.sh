#!/bin/sh
# Rebuild the Pancake flips facilitator guide: recheck answers, draw the launch figure, compile,
# then check page references against the student PDFs and the materials file.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out
tail -n 1 check_guide.out
python3 make_fig.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
grep -E "Overfull|Underfull|Warning" facilitator.log || echo "no overfull boxes or warnings"
mv facilitator.pdf ../facilitator.pdf
python3 check_pdf.py ../facilitator.pdf | tail -n 1
rm -f facilitator.aux facilitator.log
pdfinfo ../facilitator.pdf | grep Pages
