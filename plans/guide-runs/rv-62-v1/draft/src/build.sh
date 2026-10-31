#!/bin/sh
set -eu
cd "$(dirname "$0")"
builddir=$(mktemp -d)
trap 'rm -rf "$builddir"' EXIT HUP INT TERM
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$builddir" facilitator.tex > "$builddir/pass1.txt"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$builddir" facilitator.tex > "$builddir/pass2.txt"
if grep -E 'Overfull \\[hv]box' "$builddir/facilitator.log"; then
  echo 'Overfull box in guide; refusing delivery.' >&2
  exit 1
fi
cp "$builddir/facilitator.pdf" ../facilitator.pdf
python3 check_guide.py
