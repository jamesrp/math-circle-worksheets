#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
cd "$ROOT"
ATLAS_BUNDLED_PYTHON=/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
if [ -n "${ATLAS_PYTHON:-}" ]; then
    ATLAS_RUNTIME=$ATLAS_PYTHON
elif [ -x "$ATLAS_BUNDLED_PYTHON" ]; then
    ATLAS_RUNTIME=$ATLAS_BUNDLED_PYTHON
else
    ATLAS_RUNTIME=python3
fi
"$ATLAS_RUNTIME" plans/atlas/build_index.py
"$ATLAS_RUNTIME" plans/atlas/build_seed_queue.py
"$ATLAS_RUNTIME" lowell-math-circle-year-2/source/atlas/build_plans.py --render --dpi 90
"$ATLAS_RUNTIME" lowell-math-circle-year-2/source/atlas/build_research_map.py
"$ATLAS_RUNTIME" lowell-math-circle-year-2/source/atlas/verify_print.py
"$ATLAS_RUNTIME" plans/atlas/release_check.py
