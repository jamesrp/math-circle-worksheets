#!/bin/sh
set -eu
atlas_source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
atlas_bundled_python=/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
if [ -n "${ATLAS_PYTHON:-}" ]; then
    atlas_python=$ATLAS_PYTHON
elif [ -x "$atlas_bundled_python" ]; then
    atlas_python=$atlas_bundled_python
else
    atlas_python=python3
fi
export PYTHONDONTWRITEBYTECODE=1
exec "$atlas_python" "$atlas_source_dir/build.py" "$@"
