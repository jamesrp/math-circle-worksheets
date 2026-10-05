"""Shared helpers for the Week 45 math check (The visible side).

Written from scratch for this review; nothing here imports or reads the
packet's own checkers (verify.py, verify_math.py, check.py, check_math.py,
student/verify.py).

Model taken from the student pages' shared rules:
  * three two-sided cards; each of the six face tickets names one face;
  * the drawn ticket's face is set upward; the guesser sees only its colour;
  * the hidden colour is the colour of the other face of the same card;
  * each ticket in the cup (chooser) has the same chance.
The card catalogue itself is NOT hard-coded: check_base.py reads it from the
diagrams extracted out of the delivered PDFs (pdf_geometry.json).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
# Committed location: plans/review/checks/week-45/ -> four folders up.
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-45/).
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-45')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-45')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-45-bonus')

PDFS = {
    'k-1': os.path.join(WEEK, 'week-45-k-1.pdf'),
    'grades-2-3': os.path.join(WEEK, 'week-45-grades-2-3.pdf'),
    'grades-4-5': os.path.join(WEEK, 'week-45-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-45-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-45-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-45-bonus-facilitator.pdf'),
}
REFS = {
    'k-1': os.path.join(SRC, 'editable', 'reference-pdfs', 'k-1.pdf'),
    'grades-2-3': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-2-3.pdf'),
    'grades-4-5': os.path.join(SRC, 'editable', 'reference-pdfs', 'grades-4-5.pdf'),
    'guide': os.path.join(SRC, 'editable', 'reference-pdfs', 'facilitator-guide.pdf'),
    'bonus': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-45-bonus.pdf'),
    'bonus-guide': os.path.join(BONUS_SRC, 'reference-pdfs', 'week-45-bonus-facilitator.pdf'),
}


class Log:
    """Collects PASS/FAIL lines and prints a summary."""

    def __init__(self):
        self.fails = 0
        self.passes = 0

    def check(self, cond, msg):
        if cond:
            self.passes += 1
            print('PASS', msg)
        else:
            self.fails += 1
            print('FAIL', msg)

    def note(self, msg):
        print('NOTE', msg)

    def summary(self):
        print(f'\n{self.passes} passed, {self.fails} failed')
