#!/bin/sh
set -eu
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$work" k1-guide.tex > "$work/build-1.txt"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$work" k1-guide.tex > "$work/build-2.txt"
if grep -q 'Overfull \\[hv]box' "$work/k1-guide.log"; then
  cat "$work/k1-guide.log"
  exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$work"
trap - EXIT HUP INT TERM
python3 check_guide.py
