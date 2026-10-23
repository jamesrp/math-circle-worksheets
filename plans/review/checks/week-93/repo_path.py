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
# Re-pointed on 2026-10-23: the problem-file conversion (215e5ae) and the card's shoulds and small coulds (2aa59b1)
# changed the packet and moved its sources, so the review checks read the copies as reviewed:
# week-93/archive-before-card-fixes-2026-10-23/ and the reviewed sources in
# source/week-93/archive-before-problem-files-2026-10-23/week-93-source.zip (identical to the reviewed files).
DELIVERED = {"students": STUDENT_PDF, "guide": GUIDE_PDF}
REVIEWED_WEEK = WEEK / "archive-before-card-fixes-2026-10-23"
REVIEWED_ZIP = SRC / "archive-before-problem-files-2026-10-23" / "week-93-source.zip"
STUDENT_PDF = REVIEWED_WEEK / STUDENT_PDF.name
GUIDE_PDF = REVIEWED_WEEK / GUIDE_PDF.name
