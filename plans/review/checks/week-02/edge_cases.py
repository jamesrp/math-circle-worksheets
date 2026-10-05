#!/usr/bin/env python3
"""Edge-case readings used as evidence in math.md."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import importlib.util, io, contextlib

spec = importlib.util.spec_from_file_location("solve", _os.path.join(HERE, 'solve.py'))
with contextlib.redirect_stdout(io.StringIO()):
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)

# Compact P3 without the dropped "keep ONE lamp ON" rule: press-and-undo also "visits" every lamp.
presses = [(2, 3), (4, 5), (6, 1), (6, 1), (4, 5), (2, 3)]
fin, seen = S.play("ring6", [1], presses)
print("Compact P3 press-and-undo:", presses, "final", fin, "every lamp lit at some time:", seen == set(range(1, 7)))
s = {1}
for a, b in presses:
    s ^= {a, b}
    print("   after", f"{a}-{b}", sorted(s))

# Upper P3B: 'a different first line' satisfied by reordering the same set.
fin, _ = S.play("ring5", [1], [(2, 3), (1, 2)])
print("Upper P3B reorder 2-3 then 1-2 ->", fin, "(same set as 1-2, 2-3)")
# Using a line outside the first set forces the complement on a cycle
sols = S.subsets_solving("ring5", [1], [3])
print("Upper P3B solutions:", sols, "-> any solution containing 3-4, 4-5 or 5-1 is", [s for s in sols if (3, 4) in s])

# Upper P3A / P6D if the empty set is not counted
for lbl, name, st, t in [("3A", "ring4", [], []), ("6C", "tree8", [1, 7], [5]), ("6D", "path6", [2, 5], [2, 5])]:
    sols = S.subsets_solving(name, st, t)
    nonempty = [x for x in sols if x]
    print(f"Upper {lbl}: all subsets {len(sols)}; excluding the empty set {len(nonempty)}")

# Compact P10: freely drawn puzzles can be impossible, e.g. square all OFF -> one lamp
d = S.bfs("square", [])
print("square all OFF -> {1} reachable:", S.mask([1]) in d)
d = S.bfs("islands8", [])
print("two islands all OFF -> {1,5} reachable:", S.mask([1, 5]) in d)
