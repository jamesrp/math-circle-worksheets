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

# The intro follow-up (aa01c74), the card's shoulds and coulds (70a26ca, v4) and the critic coulds
# (36a239b, v5) redrew the pages this review read, so the base packets and guide are read as reviewed,
# MD5-identical to the review import (bb8a7eb): K-1 from archive-before-card-shoulds, Grades 2-3 and 4-5
# and the guide from archive-before-intro-followup; compare_source.py reads the TeX of that version from
# the source ZIP in source/week-35/archive-before-intro-followup/. The bonus is unchanged; its guide
# changed only in band labels (4f66b9d). DELIVERED keeps the current print copies for the reference-copy
# hashes; source/week-35/editable/review/verify_card_fixes_2026_10_23.py and
# verify_critic_coulds_2026_10_23.py check the current pages.
DELIVERED = {
    "k-1": WEEK / "week-35-k-1.pdf",
    "2-3": WEEK / "week-35-grades-2-3.pdf",
    "4-5": WEEK / "week-35-grades-4-5.pdf",
    "bonus": WEEK / "week-35-bonus.pdf",
    "guide": WEEK / "week-35-facilitator.pdf",
    "bonus-guide": WEEK / "week-35-bonus-facilitator.pdf",
}
STUDENT = {
    "k-1": WEEK / "archive-before-card-shoulds-2026-10-23" / "week-35-k-1.pdf",
    "2-3": WEEK / "archive-before-intro-followup" / "week-35-grades-2-3.pdf",
    "4-5": WEEK / "archive-before-intro-followup" / "week-35-grades-4-5.pdf",
    "bonus": WEEK / "week-35-bonus.pdf",
}
GUIDES = {
    "guide": WEEK / "archive-before-intro-followup" / "week-35-facilitator.pdf",
    "bonus-guide": WEEK / "week-35-bonus-facilitator.pdf",
}
REVIEWED_TEX_ZIP = REPO / "lowell-math-circle-year-2" / "source" / "week-35" / "archive-before-intro-followup" / "glide-borders-week35-editable-source.zip"


def reviewed_tex(name):
    import zipfile
    with zipfile.ZipFile(REVIEWED_TEX_ZIP) as z:
        return z.read("glide-borders-week35-source/src/" + name).decode("utf-8")


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
