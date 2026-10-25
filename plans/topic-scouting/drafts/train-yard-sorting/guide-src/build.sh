#!/bin/sh
# Build the facilitator guide: checks, figure, two pdflatex passes, copy to ../facilitator.pdf.
set -e
cd "$(dirname "$0")"
python3 check_guide.py > check_guide.out
tail -1 check_guide.out
python3 figures.py
mkdir -p build
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory build facilitator.tex > build/pdflatex.out
done
if grep -E "Overfull|Underfull \\\\hbox \(badness 10000\)|LaTeX Warning" build/facilitator.log; then
  echo "warnings above"
fi
cp build/facilitator.pdf ../facilitator.pdf
pdfinfo ../facilitator.pdf | grep Pages
