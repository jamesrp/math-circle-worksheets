#!/bin/sh
# Build Week 5: Tower cities: the three student packets from the problem files, their
# route packets, menu and key (published to band-views/week-05/), and the adult guide.
# Builds under tmp/ so the source folder stays clean, then copies the PDFs into
# lowell-math-circle-year-2/week-05/.
set -eu
cd "$(dirname "$0")"
week_dir=$(pwd)
repo_dir=$(cd ../../.. && pwd)
tools="$repo_dir/lowell-math-circle-year-2/source/problem-files"
build_dir="$repo_dir/tmp/pdfs/week-05-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-05"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
# the puzzle checks (stops on a failed assertion); the report must match src/answers-check.txt
python3 -B src/check.py > "$build_dir/src/answers-check.txt"
cmp "$build_dir/src/answers-check.txt" src/answers-check.txt
python3 "$tools/build.py" "$week_dir" --out "$build_dir/views" --tex \
  --publish "$repo_dir/lowell-math-circle-year-2/band-views/week-05" > "$build_dir/views.log"
for level in k-1 grades-2-3 grades-4-5; do
  cp "$build_dir/views/$level.pdf" "$build_dir/$level.pdf"
done
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-05-$level.pdf"
  printf '%s\n' "Built $output_dir/week-05-$level.pdf"
done
