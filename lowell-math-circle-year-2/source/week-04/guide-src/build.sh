#!/bin/sh
# Check every printed answer against the student-page sources, then build ../facilitator.pdf.
set -e
cd "$(dirname "$0")"
python3 check_answers.py > check_answers.out
tail -1 check_answers.out
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
! grep -q Overfull facilitator.log
cp facilitator.pdf ../facilitator.pdf
pdfinfo ../facilitator.pdf | grep Pages
