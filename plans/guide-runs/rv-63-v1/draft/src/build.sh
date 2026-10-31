#!/bin/sh
set -eu
cd "$(dirname "$0")"
build_dir=$(mktemp -d)
trap 'rm -rf "$build_dir"' EXIT HUP INT TERM
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex >"$build_dir/console.txt" 2>&1 || { cat "$build_dir/console.txt"; exit 1; }
done
if grep -E 'Overfull \\[hv]box|LaTeX Error|^!' "$build_dir/facilitator.log"; then
  echo 'Build rejected: TeX error or overfull box.' >&2
  exit 1
fi
cp "$build_dir/facilitator.pdf" ../facilitator.pdf
rm -rf "$build_dir"
trap - EXIT HUP INT TERM
python3 check_guide.py
