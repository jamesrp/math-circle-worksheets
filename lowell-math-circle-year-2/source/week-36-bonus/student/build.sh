#!/bin/sh
set -eu
TASK_SRC=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 "$TASK_SRC/verify.py"
python3 "$TASK_SRC/build.py" --out "${1:-$TASK_SRC/..}"
