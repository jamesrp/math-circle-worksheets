#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../qa
python3 make.py
for file in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$file.tex" > "../qa/$file-build.txt"
  cp "../qa/$file.pdf" "../$file.pdf"
  pdftoppm -r 70 -png "../$file.pdf" "../qa/$file" >/dev/null 2>&1
done
