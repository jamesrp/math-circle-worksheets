#!/bin/sh
# Build Week 4: Stars and secret wheels: three student packets and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-04/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-04-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-04"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
(cd "$build_dir/src" && python3 gen.py)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-04-$level.pdf"
  printf '%s\n' "Built $output_dir/week-04-$level.pdf"
done
