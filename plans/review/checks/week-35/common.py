"""Shared helpers for the Week 35 math check (Footprint borders).

When committed, these scripts live in <repo>/plans/review/checks/week-35/, so the
repository is four folders up.  While they are being written they sit in a run
folder under <repo>/tmp/, so fall back to searching upward.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    cand = HERE.parents[3] if len(HERE.parents) > 3 else None
    if cand and (cand / "lowell-math-circle-year-2" / "week-35").is_dir():
        return cand
    for p in [HERE] + list(HERE.parents):
        if (p / "lowell-math-circle-year-2" / "week-35").is_dir():
            return p
    sys.exit("repository not found above " + str(HERE))


REPO = find_repo()
WEEK = REPO / "lowell-math-circle-year-2" / "week-35"
SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-35" / "editable"
BONUS_SRC = REPO / "lowell-math-circle-year-2" / "source" / "week-35-bonus"
PT_PER_CM = 72 / 2.54

STUDENT = {
    "k-1": WEEK / "week-35-k-1.pdf",
    "2-3": WEEK / "week-35-grades-2-3.pdf",
    "4-5": WEEK / "week-35-grades-4-5.pdf",
    "bonus": WEEK / "week-35-bonus.pdf",
}
GUIDES = {
    "guide": WEEK / "week-35-facilitator.pdf",
    "bonus-guide": WEEK / "week-35-bonus-facilitator.pdf",
}


class Tee:
    """Print to stdout and collect lines for a saved output file."""

    def __init__(self, path):
        self.path = Path(path)
        self.lines = []

    def __call__(self, *args):
        s = " ".join(str(a) for a in args)
        print(s)
        self.lines.append(s)

    def save(self):
        self.path.write_text("\n".join(self.lines) + "\n")
