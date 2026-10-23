#!/usr/bin/env python3
"""Check the shapes printed on the Week 26 student pages and the finite small-tile answers.

Carried over from the old student builder (archive-before-problem-files-2026-10-23/
build_packets.py in the project). The printed shapes come from the problem files'
figures.py, so this checks what the pages draw. Writes math-checks.json beside this file.
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE
WEEKS = [HERE.parent / 'problem-files', HERE.parent.parent]   # portable ZIP, then repository
week = next((w for w in WEEKS if (w / 'figures.py').exists() and (w / 'week.toml').exists()), None)
if week is None:
    sys.exit('Cannot find the Week 26 problem files (week.toml, figures.py); see README.md.')
spec = importlib.util.spec_from_file_location('week26_figures', week / 'figures.py')
figures = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(figures)
starts, start2, shapes5, shape3 = figures.starts, figures.start2, figures.shapes5, figures.shape3

# Check all supplied shapes and the finite small-tile problems independently.
def edges(cells):
    s=set(cells)
    return sum((x+1,y) in s for x,y in s)+sum((x,y+1) in s for x,y in s)
def per(cells): return 4*len(cells)-2*edges(cells)
def connected(cells):
    s=set(cells)
    if not s:return False
    todo=[next(iter(s))];seen=set(todo)
    while todo:
        x,y=todo.pop()
        for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if p in s and p not in seen:seen.add(p);todo.append(p)
    return seen==s
for q in starts+start2+shapes5+shape3:
    assert connected(q) and len(set(q))==len(q)
assert [len(q) for q in starts]==[6]*3
assert [len(q) for q in shapes5]==[8]*4
assert [per(q) for q in shapes5]==[18,18,12,16]
assert [per(q) for q in shape3]==[16,14,20]

# Enumerate fixed polyominoes through eight cells, enough for K tasks and change minima.
def norm(c):
    a=min(x for x,y in c);b=min(y for x,y in c)
    return tuple(sorted((x-a,y-b) for x,y in c))
polys={((0,0),)}
report={}
for n in range(1,9):
    vals={per(q) for q in polys}
    changes=set()
    for q in polys:
        s=set(q)
        for x,y in s:
            for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if p not in s:changes.add(per(s|{p})-per(s))
    report[n]={'fixed_shapes':len(polys),'perimeters':sorted(vals),'possible_addition_changes':sorted(changes)}
    if n<8:
        nxt=set()
        for q in polys:
            s=set(q)
            for x,y in s:
                for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if p not in s:nxt.add(norm(s|{p}))
        polys=nxt
assert report[4]['perimeters']==[8,10]
assert report[5]['perimeters']==[10,12]
assert report[6]['perimeters']==[10,12,14]
assert report[7]['perimeters']==[12,14,16]
assert report[8]['perimeters']==[12,14,16,18]
mins={d:min(n for n,v in report.items() if d in v['possible_addition_changes']) for d in [2,0,-2,-4]}
assert mins=={2:1,0:3,-2:5,-4:7}
report['fewest_starting_tiles_for_addition_changes']=mins
# Different twelve-square shapes with 4 rows and 5 columns.
a={(x,y) for y,k in enumerate([5,3,2,2]) for x in range(k)}
b=set(a);b.remove((1,3));b.add((4,1))
assert connected(b) and len(b)==12 and per(a)!=per(b)
report['twelve_tiles_four_rows_five_columns']=[per(a),per(b)]
# Best perimeter via row/column bound and corner-started partial rectangle.
for n in [4,5,6,7,8,10,12,13,17,20,21,37,50,73]:
    best=min(2*(r+c) for r in range(1,n+1) for c in range(1,n+1) if r*c>=n)
    report[f'minimum_{n}']=best
# Revision checks: one best result is requested for each one-tile relocation.
def neighboring_empty(cells):
    s=set(cells)
    return {(x+dx,y+dy) for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]}-s
best_moves=[]
for start in starts:
    s=set(start)
    candidates=[]
    for source in s:
        rest=s-{source}
        for destination in neighboring_empty(rest)-{source}:
            result=rest|{destination}
            if connected(result):
                candidates.append(per(result))
    best_moves.append(min(candidates))
assert best_moves==[14,10,12]
report['one_move_minimum_boundaries']=best_moves
report['one_move_can_shorten']=[best<per(start) for start,best in zip(starts,best_moves)]
# The hole question intentionally has answer yes under the stated convention.
# A missing corner permits point contact without an extra shared side; no hint
# or answer belongs on the student pages.
hole_shape={(x,y) for x in range(3) for y in range(3) if (x,y) not in {(0,0),(1,1)}}|{(x,2) for x in range(3,8)}
assert len(hole_shape)==12 and connected(hole_shape)
assert edges(hole_shape)==11 and per(hole_shape)==26
assert all(p in hole_shape for p in [(0,1),(2,1),(1,0),(1,2)])
report['maximum_twelve_tile_shape_with_hole']={'cells':sorted(hole_shape),'shared_sides':edges(hole_shape),'boundary':per(hole_shape),'hole':[1,1]}
(SRC/'math-checks.json').write_text(json.dumps(report,indent=2))
print('Student shape checks pass; wrote src/math-checks.json')
