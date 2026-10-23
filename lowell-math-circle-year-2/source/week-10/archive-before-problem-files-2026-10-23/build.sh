#!/bin/sh
# Build Week 10: Bridges and one-stroke drawings: three student packets and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-10/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-10-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-10"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
(cd "$build_dir/src" && python3 build_k1.py && python3 build_23.py && python3 build_45.py && python3 check.py > check-output.txt)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-10-$level.pdf"
  printf '%s\n' "Built $output_dir/week-10-$level.pdf"
done
