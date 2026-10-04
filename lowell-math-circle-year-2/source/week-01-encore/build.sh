#!/bin/sh
# Build Week 1 encore: Pattern blocks II: three student packets and the adult guide.
# Builds in a copy under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-01-encore/.
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../.. && pwd)
build_dir="$repo_dir/tmp/pdfs/week-01-encore-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-01-encore"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
(cd "$build_dir/src" && sh build.sh)
# --fast skips the slow exhaustive game search on the 4-by-4 board (many minutes);
# run `sh guide-src/build.sh` without it to repeat that search.
(cd "$build_dir/guide-src" && sh build.sh --fast)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-01-encore-$level.pdf"
  printf '%s\n' "Built $output_dir/week-01-encore-$level.pdf"
done
