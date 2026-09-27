#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-01-extensions-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-01"
mkdir -p "$build_dir" "$output_dir"
python3 generate-extensions.py
for name in week-01-extensions week-01-extensions-facilitator; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
  cp "$build_dir/$name.pdf" "$output_dir/$name.pdf"
  printf '%s\n' "Built $output_dir/$name.pdf"
done
