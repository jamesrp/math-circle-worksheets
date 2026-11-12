#!/bin/sh
set -eu
cd "$(dirname "$0")"
build_dir=$(mktemp -d)
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex > "$build_dir/console.txt"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex >> "$build_dir/console.txt"
if grep -Eq 'Overfull \\[hv]box|LaTeX Error' "$build_dir/facilitator.log"; then
  cat "$build_dir/facilitator.log"
  exit 1
fi
cp "$build_dir/facilitator.pdf" ../facilitator.pdf
rm -rf "$build_dir"
trap - EXIT HUP INT TERM
python3 check_guide.py
