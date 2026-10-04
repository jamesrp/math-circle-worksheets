#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_guide.py
python3 build_guide.py
python3 render_guide.py
