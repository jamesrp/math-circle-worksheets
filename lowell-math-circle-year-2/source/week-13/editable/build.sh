#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export DEJAVU_FONT_DIR="${DEJAVU_FONT_DIR:-$PWD/fonts}"
export LIBERATION_FONT_DIR="${LIBERATION_FONT_DIR:-$PWD/fonts/liberation}"
PYTHON="${PYTHON:-python3}"
for tool in "$PYTHON" pdflatex; do command -v "$tool" >/dev/null || { echo "Missing tool: $tool" >&2; exit 1; }; done
mkdir -p build
case "${1:-}" in
 "") "$PYTHON" "src/build_packets.py" > build/student-checks.txt ;;
 --from-tex) ;;
 *) echo "Usage: bash build.sh [--from-tex]" >&2; exit 2 ;;
esac
"$PYTHON" "facilitator-src/check_math.py" > build/facilitator-checks.txt
"$PYTHON" facilitator-src/build_guide.py
for tex in src/k-1.tex src/grades-2-3.tex src/grades-4-5.tex; do
 name="$(basename "$tex" .tex)"
 for pass in 1 2; do
  if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$tex" >"build/$name-console.txt" 2>&1; then cat "build/$name-console.txt" >&2; exit 1; fi
 done
done
printf '\nBuilt four PDFs in build/. Run python3 verify_rebuild.py for reference comparison.\n'

"$PYTHON" facilitator-src/add_route_note.py
