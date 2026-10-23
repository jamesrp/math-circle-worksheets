#!/bin/sh
# Build Week 4: Stars and secret wheels: the three student packets from the problem
# files, their route packets, menu and key (published to band-views/week-04/), and the
# adult guide. Builds under tmp/ so the source folder stays clean, then copies the
# PDFs into lowell-math-circle-year-2/week-04/.
set -eu
cd "$(dirname "$0")"
week_dir=$(pwd)
repo_dir=$(cd ../../.. && pwd)
tools="$repo_dir/lowell-math-circle-year-2/source/problem-files"
build_dir="$repo_dir/tmp/pdfs/week-04-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-04"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src "$build_dir/"
# the builder's answer checks: pieces, codes, cracking (stops on a failed assertion)
python3 -B src/check.py > "$build_dir/src/check-output.txt"
python3 "$tools/build.py" "$week_dir" --out "$build_dir/views" --tex \
  --publish "$repo_dir/lowell-math-circle-year-2/band-views/week-04" > "$build_dir/views.log"
for level in k-1 grades-2-3 grades-4-5; do
  cp "$build_dir/views/$level.pdf" "$build_dir/$level.pdf"
  # the guide's answer checks read each packet's LaTeX in ../src
  cp "$build_dir/views/$level.tex" "$build_dir/src/$level.tex"
done
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-04-$level.pdf"
  printf '%s\n' "Built $output_dir/week-04-$level.pdf"
done
