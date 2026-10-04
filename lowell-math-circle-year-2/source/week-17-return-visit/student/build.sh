#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build
tex_command=${PDFLATEX:-pdflatex}
for pass in 1 2; do
  "$tex_command" -interaction=nonstopmode -halt-on-error -output-directory=build return-visit.tex > "build/pass-$pass.log"
done
cp build/return-visit.pdf ../return-visit.pdf
