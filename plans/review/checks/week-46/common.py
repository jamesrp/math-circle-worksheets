"""Shared helpers for the Week 46 math check (Two boards forget their starts).

Written from scratch for this review. Nothing here imports or reads the packet's
own checkers (check.py, verify_math.py, facilitator-src/check_math.py,
week-46-bonus/student/verify.py).

Model, taken from the student pages' shared rules:
  * a board is three slots, 1, 2, 3 from left to right, each R or B;
  * a colour-setting instruction (i, c) sets slot i to c on both boards;
  * a toggle (i) flips slot i on both boards;
  * bonus: COPY i to j copies each board's own slot i into its slot j,
    RESET i to R makes slot i red; S sets slot 1 to R, T rotates the row one
    place left (old left colour goes to the right end).
"""
from pathlib import Path
import itertools
import subprocess

HERE = Path(__file__).resolve().parent
# Committed location: plans/review/checks/week-46/ -> four folders up.
ROOT = HERE.parents[3] if len(HERE.parents) > 3 else HERE
if not (ROOT / 'lowell-math-circle-year-2').is_dir():
    # Fallback when run from the scratch run folder (tmp/review-runs/week-46/).
    d = HERE
    while d != d.parent and not (d / 'lowell-math-circle-year-2').is_dir():
        d = d.parent
    ROOT = d

Y2 = ROOT / 'lowell-math-circle-year-2'
WEEK = Y2 / 'week-46'
SRC = Y2 / 'source' / 'week-46' / 'editable'
BONUS_SRC = Y2 / 'source' / 'week-46-bonus'

PDFS = {
    'k-1': WEEK / 'week-46-k-1.pdf',
    'grades-2-3': WEEK / 'week-46-grades-2-3.pdf',
    'grades-4-5': WEEK / 'week-46-grades-4-5.pdf',
    'guide': WEEK / 'week-46-facilitator.pdf',
    'bonus': WEEK / 'week-46-bonus.pdf',
    'bonus-guide': WEEK / 'week-46-bonus-facilitator.pdf',
}
TEX = {
    'k-1': SRC / 'src' / 'k-1.tex',
    'grades-2-3': SRC / 'src' / 'grades-2-3.tex',
    'grades-4-5': SRC / 'src' / 'grades-4-5.tex',
}

BOARDS = [''.join(p) for p in itertools.product('RB', repeat=3)]
SETS = [(i, c) for i in (1, 2, 3) for c in 'RB']          # the six cards
TOGGLES = [('T', i) for i in (1, 2, 3)]


def apply(board, ins):
    """Apply one instruction to one board (a 3-letter string)."""
    b = list(board)
    if ins[0] == 'T':                 # toggle
        i = ins[1] - 1
        b[i] = 'B' if b[i] == 'R' else 'R'
    else:                             # colour-setting (i, c)
        i, c = ins
        b[i - 1] = c
    return ''.join(b)


def run(board, story):
    for ins in story:
        board = apply(board, ins)
    return board


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def pdftext(path, layout=True, first=None, last=None):
    cmd = ['pdftotext']
    if layout:
        cmd.append('-layout')
    if first:
        cmd += ['-f', str(first)]
    if last:
        cmd += ['-l', str(last)]
    cmd += [str(path), '-']
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


class Report:
    def __init__(self):
        self.n = 0
        self.fail = 0
        self.lines = []

    def check(self, ok, msg):
        self.n += 1
        if not ok:
            self.fail += 1
        line = ('PASS ' if ok else 'FAIL ') + msg
        self.lines.append(line)
        print(line)
        return ok

    def note(self, msg):
        self.lines.append('     ' + msg)
        print('     ' + msg)

    def summary(self, name):
        s = f'{name}: {self.n} checks, {self.fail} failures'
        print(s)
        return s
