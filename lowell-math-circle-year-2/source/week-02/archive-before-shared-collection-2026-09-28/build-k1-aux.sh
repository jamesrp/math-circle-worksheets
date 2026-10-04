#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo_dir=$(cd ../../../.. && pwd)
aux_python="${AUX_PYTHON:-$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3}"
if [ ! -x "$aux_python" ]; then aux_python=python3; fi
"$aux_python" "$repo_dir/plans/verify-week-02-k1-aux.py"
"$aux_python" build-k1-aux.py
"$aux_python" build-k1-aux-guide.py
