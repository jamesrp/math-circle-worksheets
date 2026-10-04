#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 make_packets.py
python3 check_math.py
python3 check_examples.py
mkdir -p ../qa
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$f.tex" > "../qa/$f-build.txt"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$f.tex" > "../qa/$f-build.txt"
  cp "../qa/$f.pdf" "../$f.pdf"
  pdftoppm -r 85 -png "../$f.pdf" "../qa/$f" >/dev/null 2>&1
done
