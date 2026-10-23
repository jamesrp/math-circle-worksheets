#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../build
# students.tex is written from the problem files (../week.toml, ../figures.py, ../problems/).
if [ -f ../week.toml ]; then python3 regenerate.py; fi
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../build students.tex
cp ../build/students.pdf ../students.pdf
