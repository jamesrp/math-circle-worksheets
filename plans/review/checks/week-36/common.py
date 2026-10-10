"""Shared helpers for the Week 36 (Making threes) math check.

Everything here is my own code.  Tiles are (shape, fill) pairs built from the
words on the pages; "allowed three" is implemented exactly as printed:
three different tiles whose shapes are all the same or all different and whose
fills are all the same or all different.  No coordinates mod 3 are assumed;
the affine structure is *derived* in check_math.py, not presupposed.
"""
from itertools import combinations, product
from pathlib import Path

SHAPES = ("circle", "triangle", "square")
FILLS = ("open", "striped", "solid")
TILES = [(s, f) for s in SHAPES for f in FILLS]          # row order = shapes, column order = fills
SHORT = {"circle": "C", "triangle": "T", "square": "S", "open": "O", "striped": "H", "solid": "F"}


def name(t):
    return SHORT[t[0]] + SHORT[t[1]]


def all_same_or_all_different(values):
    return len(set(values)) in (1, 3)


def allowed(trio):
    """The printed rule, for any number of attributes."""
    trio = list(trio)
    if len(trio) != 3 or len(set(trio)) != 3:
        return False
    return all(all_same_or_all_different([t[k] for t in trio]) for k in range(len(trio[0])))


LINES = [frozenset(c) for c in combinations(TILES, 3) if allowed(c)]


def is_cap(collection):
    return not any(allowed(c) for c in combinations(collection, 3))


def completions(a, b, universe=TILES):
    return [c for c in universe if c not in (a, b) and allowed((a, b, c))]


def find_repo():
    """Four folders up from plans/review/checks/week-NN/, else walk up to the repo root."""
    here = Path(__file__).resolve().parent
    candidates = [here.parents[3]] if len(here.parents) > 3 else []
    candidates += [here] + list(here.parents)
    for c in candidates:
        if (c / "AGENTS.md").exists() and (c / "lowell-math-circle-year-2").is_dir():
            return c
    raise SystemExit("repository root not found")


REPO = find_repo()
PRINT = REPO / "lowell-math-circle-year-2" / "week-36"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-36" / "editable" / "src"
BONUS_SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-36-bonus"
HERE = Path(__file__).resolve().parent

FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)
    return cond


def note(msg):
    print("  note " + msg)


def finish():
    print()
    print("FAILURES: %d" % len(FAIL))
    for f in FAIL:
        print("  - " + f)
