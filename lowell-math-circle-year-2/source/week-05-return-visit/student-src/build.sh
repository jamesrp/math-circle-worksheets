#!/bin/sh
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
out=${1:-"$here/../build"}
mkdir -p "$out"
out=$(CDPATH= cd -- "$out" && pwd)
if [ -n "${PDFLATEX:-}" ]; then
  engine=$PDFLATEX
elif command -v pdflatex >/dev/null 2>&1; then
  engine=$(command -v pdflatex)
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  engine=/Library/TeX/texbin/pdflatex
else
  echo 'pdflatex is required (TeX Live with TikZ and Latin Modern).' >&2
  exit 1
fi
cd "$here"
"$engine" -interaction=nonstopmode -halt-on-error -output-directory="$out" return-visit.tex > "$out/compile-pass-1.txt"
"$engine" -interaction=nonstopmode -halt-on-error -output-directory="$out" return-visit.tex > "$out/compile-pass-2.txt"
cp "$out/return-visit.pdf" "$here/../return-visit.pdf"
