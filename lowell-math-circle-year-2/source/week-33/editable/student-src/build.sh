#!/usr/bin/env bash
# Write the band LaTeX from the problem files, then compile each packet twice into ../qa
# and copy it to the package root, as the old make_packets.py did.
set -euo pipefail
cd "$(dirname "$0")"
python3 regenerate.py
mkdir -p ../qa
for f in k-1 grades-2-3 grades-4-5; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$f.tex" > "../qa/$f-build-1.log"
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../qa "$f.tex" > "../qa/$f-build-2.log"
  cp "../qa/$f.pdf" "../$f.pdf"
  pdftoppm -r 60 -png "../$f.pdf" "../qa/$f" >/dev/null 2>&1
done
