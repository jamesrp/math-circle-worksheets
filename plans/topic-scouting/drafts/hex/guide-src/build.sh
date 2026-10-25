#!/bin/sh
# Rebuild ../facilitator.pdf: build.py runs the answer checks, writes the figures and compiles.
set -e
cd "$(dirname "$0")"
python3 build.py
