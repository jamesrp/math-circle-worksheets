#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
engine="${LATEX_ENGINE:-pdflatex}"
command -v "$engine" >/dev/null || { echo "Install a TeX distribution with pdflatex, TikZ, Helvetica and the standard LaTeX packages." >&2; exit 1; }
mkdir -p build
"$engine" -interaction=nonstopmode -halt-on-error -output-directory=build facilitator.tex
"$engine" -interaction=nonstopmode -halt-on-error -output-directory=build facilitator.tex
cp build/facilitator.pdf facilitator.pdf
