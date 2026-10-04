#!/bin/sh
# Rebuild the adult guide: recheck every answer against the student pages, then compile.
set -e
cd "$(dirname "$0")"
python3 check_answers.py > check_output.txt      # also writes generated.tex
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log facilitator.out
tail -1 check_output.txt
