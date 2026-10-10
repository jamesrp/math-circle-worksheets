"""Locate the repository from this script's own folder.

The committed copy lives in plans/review/checks/week-17/ (four folders below
the repository root); the working copy lives in tmp/review-runs/week-17/.
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
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-17'
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-17' / 'editable'
RVSRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-17-return-visit'

PDF = {
    'K1': WEEK / 'week-17-k-1.pdf',
    'G23': WEEK / 'week-17-grades-2-3.pdf',
    'G45': WEEK / 'week-17-grades-4-5.pdf',
    'GUIDE': WEEK / 'week-17-facilitator.pdf',
    'RV': WEEK / 'week-17-return-visit.pdf',
    'RVGUIDE': WEEK / 'week-17-return-visit-facilitator.pdf',
}
