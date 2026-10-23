#!/bin/sh
# Build Week 8: Rook race and Nim: three student packets, the separate game
# boards (materials) and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-08/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-08-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-08"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src materials "$build_dir/"
(cd "$build_dir/src" && python3 build.py)
(cd "$build_dir/materials" && python3 materials.py && python3 check_materials.py ../materials.pdf)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 materials facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-08-$level.pdf"
  printf '%s\n' "Built $output_dir/week-08-$level.pdf"
done
