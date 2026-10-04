#!/bin/sh
# Rebuild the Week 9 adult guide: check every printed answer, regenerate the
# simulation-drawn pictures and chart, compile, and copy the PDF into final/.
set -e
cd "$(dirname "$0")"
python3 check.py
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error facilitator.tex > /dev/null
cp facilitator.pdf ../facilitator.pdf
pdfinfo ../facilitator.pdf | grep Pages
