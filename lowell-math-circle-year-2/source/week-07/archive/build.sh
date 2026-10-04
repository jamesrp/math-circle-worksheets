#!/bin/sh
# Archived October 3, 2026: builds the superseded version into week-07/archive/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-07-archive-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-07/archive"
mkdir -p "$build_dir" "$output_dir"
python3 "$repo_dir/plans/verify-week-07.py"
for suffix in k-1 grades-2-3 grades-4-5 extra-grades-6-7 facilitator; do
 name="week-07-$suffix"
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
 pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$name.tex" > "$build_dir/$name.console.txt"
 cp "$build_dir/$name.pdf" "$output_dir/$name.pdf"
 printf '%s\n' "Built $output_dir/$name.pdf"
done
