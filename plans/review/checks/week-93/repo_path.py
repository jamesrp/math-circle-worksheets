"""Locate the repository from this script's own folder.

Committed copies live in plans/review/checks/week-93/, four folders below the
repository root. The run-folder copy (tmp/review-runs/week-93/) is three below,
so fall back to walking upward until the repository markers appear.
"""
from pathlib import Path


def repo_root():
    here = Path(__file__).resolve().parent
    candidates = []
    if len(here.parents) > 3:
        candidates.append(here.parents[3])  # four folders up from week-93/
    candidates.extend(here.parents)
    for c in candidates:
        if (c / "AGENTS.md").is_file() and (c / "lowell-math-circle-year-2").is_dir():
            return c
    raise SystemExit("repository root not found above " + str(here))


ROOT = repo_root()
WEEK = ROOT / "lowell-math-circle-year-2" / "week-93"
SRC = ROOT / "lowell-math-circle-year-2" / "source" / "week-93"
STUDENT_PDF = WEEK / "week-93-students.pdf"
GUIDE_PDF = WEEK / "week-93-facilitator.pdf"
