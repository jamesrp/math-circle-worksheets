#!/bin/sh
# Build Week 3: Shuffle machines: three student packets and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-03/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-03-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-03"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
(cd "$build_dir/src" && python3 figures.py && for f in k-1 grades-2-3 grades-4-5; do pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" > /dev/null && pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" > /dev/null && cp "$f.pdf" "../$f.pdf"; done)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-03-$level.pdf"
  printf '%s\n' "Built $output_dir/week-03-$level.pdf"
done
