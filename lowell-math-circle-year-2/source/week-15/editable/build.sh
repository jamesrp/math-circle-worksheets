#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PYTHON:-python3}"
case "${1:-}" in
  "") "$PYTHON" src/build_packets.py; "$PYTHON" facilitator-src/build_guide.py ;;
  --from-tex) ;; # Preserve manual changes to the supplied .tex files.
  *) echo "Usage: bash build.sh [--from-tex]" >&2; exit 2 ;;
esac
for tool in "$PYTHON" pdflatex; do
  command -v "$tool" >/dev/null || { echo "Missing required tool: $tool" >&2; exit 1; }
done
mkdir -p build
for tex in src/k-1.tex src/grades-2-3.tex src/grades-4-5.tex facilitator-src/facilitator-guide.tex; do
  name="$(basename "$tex" .tex)"
  for pass in 1 2; do
    if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$tex" >"build/$name-console.txt" 2>&1; then
      cat "build/$name-console.txt" >&2; exit 1
    fi
  done
done
"$PYTHON" src/check_geometry.py
"$PYTHON" facilitator-src/check_solutions.py
printf '\nBuilt and checked four PDFs in build/. Run python3 verify_rebuild.py for reference comparison.\n'
