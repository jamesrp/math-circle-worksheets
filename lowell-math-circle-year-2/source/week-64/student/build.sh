#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../build
python3 generate.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../build students.tex
cp ../build/students.pdf ../students.pdf
