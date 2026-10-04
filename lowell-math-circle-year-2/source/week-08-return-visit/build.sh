#!/bin/sh
set -eu
base_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 0 ]; then
  mkdir -p "$1"
  output_dir=$(CDPATH= cd -- "$1" && pwd)
else
  output_dir=$(mktemp -d "${TMPDIR:-/tmp}/week-08-return-visit.XXXXXX")
fi
build_dir="$output_dir/.build"
mkdir -p "$build_dir"
if command -v pdflatex >/dev/null 2>&1; then
  tex_command=$(command -v pdflatex)
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  tex_command=/Library/TeX/texbin/pdflatex
else
  echo 'Requires pdfLaTeX, TikZ, lmodern and Source Sans Pro.' >&2
  exit 1
fi
python3 "$base_dir/verify.py"
(cd "$base_dir/student" && for check_script in check*.py; do [ -f "$check_script" ] || continue; [ "$check_script" != check_pdf.py ] || continue; python3 "$check_script" > "$build_dir/$check_script.log"; done)
(cd "$base_dir/student" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
(cd "$base_dir/student" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
cp "$build_dir/return-visit.pdf" "$output_dir/week-08-return-visit.pdf"
(cd "$base_dir" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex > "$build_dir/guide-build.log")
cp "$build_dir/facilitator.pdf" "$output_dir/week-08-return-visit-facilitator.pdf"
printf '%s\n' "$output_dir/week-08-return-visit.pdf" "$output_dir/week-08-return-visit-facilitator.pdf"
