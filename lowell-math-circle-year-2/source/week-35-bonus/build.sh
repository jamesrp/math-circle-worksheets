#!/bin/sh
set -eu
TASK_SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec "${PYTHON:-python3}" "$TASK_SOURCE_DIR/build.py" "$@"
