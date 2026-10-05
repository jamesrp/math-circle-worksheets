"""Shared helpers for the Week 43 math check (Shuffling picture cards).

Written from scratch for this review. Nothing here imports or reads the
packet's own checkers (check.py, verify.py, verify_math.py, check_math.py,
student/verify.py).

Conventions taken from the student pages:
  * slots are numbered 1, 2, 3 (, 4, 5) from the left;
  * "swap slot i with ticket t" exchanges the cards in slots i and t
    (t == i is a self-swap, which changes nothing);
  * a "story" is the sequence of tickets drawn.
"""
import os
import re
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_root():
    # Committed location: plans/review/checks/week-43/ -> four folders up.
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    # Fallback for the scratch run folder (tmp/review-runs/week-43/).
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found')


ROOT = _find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-43')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-43', 'editable')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-43-bonus')

PDFS = {
    'k-1': os.path.join(WEEK, 'week-43-k-1.pdf'),
    'grades-2-3': os.path.join(WEEK, 'week-43-grades-2-3.pdf'),
    'grades-4-5': os.path.join(WEEK, 'week-43-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-43-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-43-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-43-bonus-facilitator.pdf'),
}

ROWS3 = [''.join(p) for p in permutations('ABC')]  # ABC ACB BAC BCA CAB CBA


# ---------------------------------------------------------------- shuffles
def swap(row, i, j):
    """Swap 1-based slots i and j of a string row."""
    r = list(row)
    r[i - 1], r[j - 1] = r[j - 1], r[i - 1]
    return ''.join(r)


def run_story(start, story, slots=None):
    """Apply 'swap slot k with ticket story[k-1]' for k = 1, 2, ...

    `slots` lets a caller name which slot each step swaps (default 1, 2, ...).
    """
    row = start
    slots = slots or list(range(1, len(story) + 1))
    for s, t in zip(slots, story):
        row = swap(row, s, t)
    return row


def fisher_yates_stories(n):
    """Left-to-right Fisher-Yates: slot i swaps with a ticket from {i..n}."""
    return list(product(*[range(i, n + 1) for i in range(1, n)]))


def naive_stories(n):
    """Wrong-range rule: every slot 1..n swaps with a ticket from {1..n}."""
    return list(product(range(1, n + 1), repeat=n))


def chooser_stories():
    """Draw first card from 3, second from the 2 left, last is forced."""
    out = []
    for a in 'ABC':
        for b in 'ABC':
            if b != a:
                c = ({'A', 'B', 'C'} - {a, b}).pop()
                out.append((a + b, a + b + c))
    return out


# ---------------------------------------------------------------- reporting
class Report:
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.n = 0
        self.fail = 0

    def check(self, cond, msg):
        self.n += 1
        if not cond:
            self.fail += 1
        self.lines.append(('PASS ' if cond else 'FAIL ') + msg)
        return cond

    def note(self, msg):
        self.lines.append('     ' + msg)

    def head(self, msg):
        self.lines.append('')
        self.lines.append('== ' + msg)

    def finish(self):
        self.lines.append('')
        self.lines.append(f'{self.name}: {self.n} checks, {self.fail} failures')
        text = '\n'.join(self.lines) + '\n'
        print(text, end='')
        with open(os.path.join(HERE, self.name + '.out'), 'w') as f:
            f.write(text)
        return self.fail


def pdf_text(path):
    import pymupdf
    with pymupdf.open(path) as d:
        return [p.get_text() for p in d]


def flat(s):
    """Collapse whitespace and undo the line-break hyphenation of the PDFs."""
    s = s.replace('–', '-').replace('→', '->')
    s = re.sub(r'-\n(?=[a-z])', '', s)
    return re.sub(r'\s+', ' ', s)
