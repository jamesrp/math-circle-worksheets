#!/bin/sh
set -eu
task_src=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
task_out=${1:-"$task_src/.."}
mkdir -p "$task_out"
task_out=$(CDPATH= cd -- "$task_out" && pwd)
task_build=$(mktemp -d "${TMPDIR:-/tmp}/week58-guide.XXXXXX")
trap 'rm -rf "$task_build"' EXIT HUP INT TERM
export SOURCE_DATE_EPOCH=1791072000
export FORCE_SOURCE_DATE=1
cd "$task_src"
if ! pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$task_build" guide.tex > "$task_build/build.log"; then
  cat "$task_build/build.log" >&2
  exit 1
fi
cp "$task_build/guide.pdf" "$task_out/facilitator.pdf"
