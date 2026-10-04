#!/bin/sh
set -eu
cd "$(dirname "$0")/../../.."
for week in 02 03 04 05 06 07 08 09 10; do
  sh "lowell-math-circle-year-2/source/week-$week/build.sh"
done
python3 lowell-math-circle-year-2/source/fall-weeks-02-10/independent-checks.py
bundle_python="/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
if [ -x "$bundle_python" ]; then
  "$bundle_python" lowell-math-circle-year-2/source/fall-weeks-02-10/assemble.py
else
  python3 lowell-math-circle-year-2/source/fall-weeks-02-10/assemble.py
fi
