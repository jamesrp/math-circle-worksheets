"""Locate the repository from this script's own folder.

The committed copy lives in plans/review/checks/week-20/ (four folders below
the repository root); the working copy lives in tmp/review-runs/week-20/
(three below).  Walk upward until the folder holding AGENTS.md and
lowell-math-circle-year-2/.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent


def repo_root():
    for p in [HERE, *HERE.parents]:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository root not found above ' + str(HERE))


ROOT = repo_root()
WEEK = ROOT / 'lowell-math-circle-year-2' / 'week-20'
# The card's shoulds and coulds (d19c46b: K-1 v4, 2-3 v3, 4-5 v4, guide renumbered) moved and redrew the
# pages this review read, so the base packets and guide are read as reviewed from REVIEWED (MD5-identical
# to the review import, bb8a7eb). WEEK stays the current print folder, used for the reference-copy
# hashes and the bonus (unchanged apart from its guide's band labels, 4f66b9d). The current pages are
# checked by source/week-20/editable/review/check_card_fixes.py.
REVIEWED = WEEK / 'archive-before-card-fixes-2026-10-23'
SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-20' / 'editable'
BONUS_SRC = ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-20-bonus'
