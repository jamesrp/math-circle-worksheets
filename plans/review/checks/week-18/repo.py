"""Locate the repository from this script's own folder.

The committed copy lives in plans/review/checks/week-18/ (four folders below
the repository root); the working copy lives in tmp/review-runs/week-18/.
Walk upward until the folder holding AGENTS.md and lowell-math-circle-year-2/.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repo_root():
    for p in [HERE, *HERE.parents]:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository root not found above ' + str(HERE))


ROOT = repo_root()
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-18'
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-18' / 'editable'
