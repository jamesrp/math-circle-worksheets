#!/bin/sh
# Rebuild the Week 5 adult guide: check every printed answer, then typeset.
set -e
cd "$(dirname "$0")"
python3 check.py > /dev/null        # writes answers.tex and check-report.txt; fails on any mismatch
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
mv facilitator.pdf ../facilitator.pdf
rm -f facilitator.aux facilitator.log
pdfinfo ../facilitator.pdf | grep Pages
