#!/bin/sh
# Rebuild ../materials.pdf, then measure it.
set -e
cd "$(dirname "$0")"
python3 make_materials.py
python3 check_materials.py | tail -1
