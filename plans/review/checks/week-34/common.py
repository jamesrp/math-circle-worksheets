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
# The card's shoulds and coulds (f708ade) changed the base packets and guide this review read, so
# extract.py reads them as reviewed from REVIEWED (MD5-identical to the review import, bb8a7eb) and
# compare_source.py reads the reviewed TeX from the source ZIP archived before the problem-file
# conversion (b45bb66; identical to the reviewed src/*.tex). The bonus is unchanged and read from WEEK.
# check_card_fixes.py and card_checks.py here check the current pages.
REVIEWED = WEEK / "archive-before-card-fixes-2026-10-23"
REVIEWED_TEX_ZIP = SRC / "archive-before-problem-files-2026-10-23" / "symmetry-breaking-week34-editable-source.zip"


def reviewed_tex(band):
    import zipfile
    with zipfile.ZipFile(REVIEWED_TEX_ZIP) as z:
        return z.read(f"symmetry-breaking-week34-source/src/{band}.tex").decode("utf-8")
PT_PER_MM = 72 / 25.4
