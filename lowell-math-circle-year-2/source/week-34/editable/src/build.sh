#!/usr/bin/env bash
# Write the band LaTeX from the problem files (regenerate.py), run the finite checks, then
# compile each packet twice into ../build, copy it to the package root and render it.
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1791061200}"
export FORCE_SOURCE_DATE=1
python3 regenerate.py
python3 check_distinguishing.py
python3 check_revised_cases.py
mkdir -p ../build ../render
for name in k-1 grades-2-3 grades-4-5; do
  for pass in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../build "$name.tex" > "../build/$name-console.txt" 2>&1; done
  cp "../build/$name.pdf" "../$name.pdf"
  pdftoppm -scale-to 1100 -png "../$name.pdf" "../render/$name" >/dev/null 2>&1
done
