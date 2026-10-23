#!/usr/bin/env python3
"""Exhaustive checks of every fixed set of counts printed on the student pages.

Carried over unchanged from the old student builder (archived in
archive-before-problem-files-2026-10-23/build_packets.py), which ran these after writing
the LaTeX. Every 0/1 picture on each board is tried; nothing is read from the problem
files. Writes answer-checks.json with each case's pictures.
"""
from pathlib import Path
from itertools import product
import json

ROOT=Path(__file__).resolve().parent

# Independent exhaustive margins checks for every fixed case used in these pages.
def sols(rows,cols):
    out=[]
    for bits in product([0,1],repeat=len(rows)*len(cols)):
        a=[bits[i*len(cols):(i+1)*len(cols)] for i in range(len(rows))]
        if list(map(sum,a))==rows and [sum(row[j] for row in a) for j in range(len(cols))]==cols:
            out.append(a)
    return out
cases=[([1,1],[1,1],2),([1,1],[1,0,1],2),([2,1],[1,1,1],3),([1,2],[1,1,1],3),([1,1,1],[1,1,1],6),([3,1],[2,1,1],1),([2,1,0],[2,1,0],1),([2,1,1],[2,1,1],5),([2,2],[2,1,1],2),([2,2],[1,1,1,1],6),([3,3],[2,1,0,1,1,1],6)]
checks=[]
for rows,cols,n in cases:
    actual=sols(rows,cols)
    assert len(actual)==n,(rows,cols,n,len(actual))
    checks.append({'rows':rows,'columns':cols,'solutions':len(actual),'pictures':['/'.join(''.join(map(str,row)) for row in a) for a in actual]})
assert sum(a=='1' and b=='0' for a,b in zip('111000','000111'))==3
assert sum(a=='1' and b=='0' for a,b in zip('110100','100011'))==2
(ROOT/'answer-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('All fixed-case counts checked.')

# Guidance-revision switch example: occupied diagonals exchange; margins agree.
_example_before = ((1, 0), (0, 1))
_example_after = ((0, 1), (1, 0))
assert _example_before != _example_after
for _example in (_example_before, _example_after):
    assert [sum(row) for row in _example] == [1, 1]
    assert [sum(row[j] for row in _example) for j in range(2)] == [1, 1]
