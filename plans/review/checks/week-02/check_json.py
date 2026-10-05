#!/usr/bin/env python3
"""Compare the edge sets/minima in plans/week-02-catalog-upper-checks.json
(which the upper guide cites for exact solutions) with my own enumeration."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import json
import sys

sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location("solve", _os.path.join(HERE, 'solve.py'))
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)

D = json.load(open(_os.path.join(ROOT, 'plans/week-02-catalog-upper-checks.json')))
bad = 0
for c in D["cases"]:
    name = c["graph"]
    if name not in S.G:
        print("unknown graph", name)
        continue
    mine = S.subsets_solving(name, c["start"], c["target"])
    mine_set = {frozenset(frozenset(e) for e in s) for s in mine}
    theirs = {frozenset(frozenset(e) for e in s) for s in c["solutions"]}
    d = S.bfs(name, c["start"])
    m = d.get(S.mask(c["target"]))
    ok = mine_set == theirs and c["solution_count"] == len(mine) and c["minimum"] == m
    bad += not ok
    print(("OK  " if ok else "DIFF"), c["case"], name, "count", len(mine), "min", m)
print("hardest_rings:", D.get("hardest_rings"))
print("mismatches:", bad)
