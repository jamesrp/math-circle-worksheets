#!/bin/sh
# Build Week 8: Rook race and Nim: the three student packets from the problem files,
# their route packets, menu and key (published to band-views/week-08/), the separate
# game boards (materials) and the adult guide. Builds under tmp/ so the source folder
# stays clean, then copies the PDFs into lowell-math-circle-year-2/week-08/.
set -eu
cd "$(dirname "$0")"
week_dir=$(pwd)
repo_dir=$(cd ../../.. && pwd)
tools="$repo_dir/lowell-math-circle-year-2/source/problem-files"
build_dir="$repo_dir/tmp/pdfs/week-08-build"
output_dir="$repo_dir/lowell-math-circle-year-2/week-08"
rm -rf "$build_dir"
mkdir -p "$build_dir" "$output_dir"
cp -R src guide-src materials "$build_dir/"
python3 "$tools/build.py" "$week_dir" --out "$build_dir/views" --tex \
  --publish "$repo_dir/lowell-math-circle-year-2/band-views/week-08" > "$build_dir/views.log"
for level in k-1 grades-2-3 grades-4-5; do
  cp "$build_dir/views/$level.pdf" "$build_dir/$level.pdf"
  # the guide's answer checks read each packet's LaTeX in ../src
  cp "$build_dir/views/$level.tex" "$build_dir/src/$level.tex"
done
(cd "$build_dir/materials" && python3 materials.py && python3 check_materials.py ../materials.pdf)
(cd "$build_dir/guide-src" && sh build.sh)
for level in k-1 grades-2-3 grades-4-5 materials facilitator; do
  cp "$build_dir/$level.pdf" "$output_dir/week-08-$level.pdf"
  printf '%s\n' "Built $output_dir/week-08-$level.pdf"
done
