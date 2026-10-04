#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
out_dir="${1:-..}"
mkdir -p "$out_dir"
"${PDFLATEX:-pdflatex}" -interaction=nonstopmode -halt-on-error -output-directory="$out_dir" bonus.tex
