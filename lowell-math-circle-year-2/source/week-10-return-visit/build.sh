#!/bin/sh
set -eu
base_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 0 ]; then
  mkdir -p "$1"
  output_dir=$(CDPATH= cd -- "$1" && pwd)
else
  output_dir=$(mktemp -d "${TMPDIR:-/tmp}/week-10-return-visit.XXXXXX")
fi
build_dir="$output_dir/.build"
mkdir -p "$build_dir"
student_work="$build_dir/student"
mkdir -p "$student_work"
cp -R "$base_dir/student/." "$student_work/"
if command -v pdflatex >/dev/null 2>&1; then
  tex_command=$(command -v pdflatex)
elif [ -x /Library/TeX/texbin/pdflatex ]; then
  tex_command=/Library/TeX/texbin/pdflatex
else
  echo 'Requires pdfLaTeX, TikZ, lmodern and Source Sans Pro.' >&2
  exit 1
fi
python3 "$base_dir/verify.py"
(cd "$student_work" && if [ -f generate.py ]; then python3 generate.py > "$build_dir/generate.log"; fi)
(cd "$student_work" && for check_script in check*.py; do [ -f "$check_script" ] || continue; case "$check_script" in check_pdf.py|check_independent.py) continue;; esac; python3 "$check_script" > "$build_dir/$check_script.log"; done)
(cd "$student_work" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
(cd "$student_work" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" return-visit.tex > "$build_dir/student-build.log")
cp "$build_dir/return-visit.pdf" "$output_dir/week-10-return-visit.pdf"
(cd "$base_dir" && "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory="$build_dir" facilitator.tex > "$build_dir/guide-build.log")
cp "$build_dir/facilitator.pdf" "$output_dir/week-10-return-visit-facilitator.pdf"
printf '%s\n' "$output_dir/week-10-return-visit.pdf" "$output_dir/week-10-return-visit-facilitator.pdf"
