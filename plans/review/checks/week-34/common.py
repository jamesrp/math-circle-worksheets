"""Shared helpers for the Week 34 math check (Hidden turns).

The scripts live (when committed) in <repo>/plans/review/checks/week-34/, so the
repository is four folders up.  While they are being written they sit in a run
folder under <repo>/tmp/, so fall back to searching upward.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2" / "week-34").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2" / "week-34").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-34"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-34"
BONUS_SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-34-bonus"
PT_PER_MM = 72 / 25.4
