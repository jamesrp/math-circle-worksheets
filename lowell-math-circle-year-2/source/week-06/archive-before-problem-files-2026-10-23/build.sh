#!/bin/sh
# Build Week 6: Code breaking: three student packets and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-06/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-06-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-06"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
(cd "$build_dir/src" && sh build.sh)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-06-$level.pdf"
  printf '%s\n' "Built $output_dir/week-06-$level.pdf"
done
