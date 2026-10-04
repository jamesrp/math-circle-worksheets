#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v pdflatex >/dev/null 2>&1; then
  TEX=pdflatex
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  TEX=/Library/TeX/texbin/pdflatex
else
  echo "pdfLaTeX is required." >&2
  exit 1
fi
mkdir -p ../build
"$TEX" -halt-on-error -interaction=nonstopmode -output-directory=../build return-visit.tex
cp ../build/return-visit.pdf ../return-visit.pdf
