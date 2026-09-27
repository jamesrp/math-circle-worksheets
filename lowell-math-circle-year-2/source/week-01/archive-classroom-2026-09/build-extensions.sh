#!/bin/sh
# The archive rebuild is self-contained and includes the extension PDFs.
set -eu
sh "$(dirname "$0")/build.sh"
