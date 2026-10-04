#!/usr/bin/env bash
# The whole-bundle build supplies student PDFs for the guide checks.
set -euo pipefail
exec bash "$(dirname "$0")/../build.sh" "$@"
