#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 make_packets.py
