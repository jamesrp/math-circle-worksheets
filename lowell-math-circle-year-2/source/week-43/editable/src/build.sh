#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 regenerate.py
python3 common.py
