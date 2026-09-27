#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-03-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-03"
mkdir -p "$build_dir" "$output_dir"
python3 verify.py
for level in k-1 grades-2-3 grades-4-5 extra-grades-6-7 facilitator; do
 name="week-03-$level"
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
 cp "$build_dir/$name.pdf" "$output_dir/$name.pdf"
 printf '%s\n' "Built $output_dir/$name.pdf"
done
