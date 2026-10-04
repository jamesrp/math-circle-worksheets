#!/bin/sh
# Incremental pack: files changed since the last pack (marker genlab/.last_sync), excluding regenerable
# bundles, TeX intermediates, PNG renders, and agents' scratch. Pass "full" for a complete snapshot.
set -e
cd /home/claude
TS=$(date +%Y%m%d-%H%M%S)
mkdir -p /mnt/user-data/outputs/genlab-sync
OUT=/mnt/user-data/outputs/genlab-sync/genlab-$TS.tar.gz
LIST=$(mktemp)
if [ "$1" = "full" ] || [ ! -f genlab/.last_sync ]; then
  find genlab -type f > $LIST
else
  find genlab -type f -newer genlab/.last_sync > $LIST
fi
grep -v -E '^genlab/eval/bundles/|\.aux$|\.log$|__pycache__|\.png$|^genlab/runs/[^/]+/scratch/|^genlab/runs/[^/]+/src/png/' $LIST > $LIST.f || true
tar czf $OUT --mode='u+rw' -T $LIST.f
touch genlab/.last_sync
echo $OUT $(wc -l < $LIST.f) files
