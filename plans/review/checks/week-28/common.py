"""Shared helpers for the Week 28 (single-vertex flat folding) math check.

The repository is found from this file's location: four folders up from
plans/review/checks/week-28/ (its committed home).  When run from another
folder (such as tmp/review-runs/week-28/), we walk upward until we find the
folder that holds lowell-math-circle-year-2/ and AGENTS.md.
"""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    parents = list(HERE.parents)
    cand = parents[3] if len(parents) > 3 else None  # four folders up from week-28/
    if cand and (cand / 'lowell-math-circle-year-2').is_dir() and (cand / 'AGENTS.md').is_file():
        return cand
    for p in [HERE] + parents:
        if (p / 'lowell-math-circle-year-2').is_dir() and (p / 'AGENTS.md').is_file():
            return p
    sys.exit('cannot find repository from ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-28'
SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-28' / 'editable'
BONUS_SRC = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-28-bonus'
PDFS = {
    'k-1': WEEK / 'week-28-k-1.pdf',
    'grades-2-3': WEEK / 'week-28-grades-2-3.pdf',
    'grades-4-5': WEEK / 'week-28-grades-4-5.pdf',
    'guide': WEEK / 'week-28-facilitator.pdf',
    'bonus': WEEK / 'week-28-bonus.pdf',
    'bonus-guide': WEEK / 'week-28-bonus-facilitator.pdf',
}
REFS = {
    'k-1': SRC / 'reference-pdfs' / 'k-1.pdf',
    'grades-2-3': SRC / 'reference-pdfs' / 'grades-2-3.pdf',
    'grades-4-5': SRC / 'reference-pdfs' / 'grades-4-5.pdf',
    'guide': SRC / 'reference-pdfs' / 'facilitator-guide.pdf',
    'bonus': BONUS_SRC / 'reference-pdfs' / 'week-28-bonus.pdf',
    'bonus-guide': BONUS_SRC / 'reference-pdfs' / 'week-28-bonus-facilitator.pdf',
}
TEX = {
    'k-1': SRC / 'src' / 'k-1.tex',
    'grades-2-3': SRC / 'src' / 'grades-2-3.tex',
    'grades-4-5': SRC / 'src' / 'grades-4-5.tex',
    'bonus': BONUS_SRC / 'student-src' / 'bonus.tex',
}
CM = 72 / 2.54  # points per centimetre


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()


def pdf_text(key, layout=False):
    """Plain text of a delivered PDF (via pdfplumber, no external process)."""
    import pdfplumber
    with pdfplumber.open(str(PDFS[key])) as pdf:
        pages = [p.extract_text(layout=layout) or '' for p in pdf.pages]
    return pages


def norm(s):
    """Collapse whitespace and unify dashes/arrows for text matching."""
    import re
    s = s.replace('–', '-').replace('—', '-').replace('−', '-')
    s = s.replace('→', '->').replace('◦', '°').replace('°', '°')
    return re.sub(r'\s+', ' ', s)


class Log:
    def __init__(self):
        self.n = 0
        self.fail = 0

    def check(self, ok, msg):
        self.n += 1
        if not ok:
            self.fail += 1
        print(('PASS ' if ok else 'FAIL ') + msg)
        return ok

    def info(self, msg):
        print('     ' + msg)

    def head(self, msg):
        print('\n== ' + msg)

    def done(self):
        print(f'\n{self.n} checks, {self.fail} failures')
