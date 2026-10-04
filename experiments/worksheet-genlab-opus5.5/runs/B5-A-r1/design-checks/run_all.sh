#!/bin/sh
# Runs every design check and saves the output next to the script.
cd "$(dirname "$0")"
python3 check_k1.py > check_k1.out 2>&1; echo "check_k1: exit $?"
python3 check_23.py > check_23.out 2>&1; echo "check_23: exit $?"
python3 check_45.py > check_45.out 2>&1; echo "check_45: exit $?"
python3 render.py > render.out 2>&1; echo "render: exit $?"
grep -h "FAIL" check_k1.out check_23.out check_45.out || echo "no FAIL lines"
grep -h "PASSED\|FIT AT" check_k1.out check_23.out check_45.out render.out
