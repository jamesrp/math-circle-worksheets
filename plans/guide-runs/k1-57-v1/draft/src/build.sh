#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$work" k1-guide.tex >"$work/build.stdout"; then
  cat "$work/build.stdout" >&2
  exit 1
fi
if grep -Eq 'Overfull \\[hv]box|^!' "$work/k1-guide.log"; then
  cat "$work/build.stdout" >&2
  echo 'LaTeX error or overfull box; refusing output.' >&2
  exit 1
fi
cp "$work/k1-guide.pdf" ../k1-guide.pdf
rm -rf "$work"
trap - EXIT
python3 check_guide.py
