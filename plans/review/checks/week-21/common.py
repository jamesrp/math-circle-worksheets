"""Shared helpers for the Week 21 math check.

The repository is found from this file's location: four folders up from
plans/review/checks/week-21/ when committed. When run from the scratch run
folder (tmp/review-runs/week-21/) we fall back to searching upward.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repo_root():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand is not None and (cand / 'lowell-math-circle-year-2').is_dir():
        return cand
    for p in HERE.parents:
        if (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(HERE))


REPO = repo_root()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-21'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-21'
BONUS_SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-21-bonus'
PT_PER_CM = 72 / 2.54
