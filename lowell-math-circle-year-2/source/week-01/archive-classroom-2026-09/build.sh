#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-01-classroom-archive-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-01/archive-classroom-2026-09"
mkdir -p "$build_dir" "$output_dir"
for name in week-01-k-1 week-01-grades-2-3 week-01-grades-4-5 week-01-facilitator week-01-extra-rhombi week-01-extensions week-01-extensions-facilitator; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
  cp "$build_dir/$name.pdf" "$output_dir/$name.pdf"
done
