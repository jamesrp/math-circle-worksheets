"""Shared helpers for the Week 33 math check (prime-length necklaces).

Written from scratch for this review; nothing here imports or reads the
packet's own checkers (verify.py, check_math.py, writer-check.py,
independent-check.py).

Conventions taken from the student pages' shared rules:
  * a readout is the clockwise word from a marked start;
  * two rings are the same when a TURN (rotation) makes them match;
  * rings stay face up, so a flip (reversal) is NOT a match,
    except where the bonus Problem 1 explicitly allows flips.
"""
import os
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-33/)
    # rather than the committed plans/review/checks/week-33/.
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-33')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-33')
BONUS_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-33-bonus')

PDFS = {
    'k-1': os.path.join(WEEK, 'week-33-k-1.pdf'),
    'grades-2-3': os.path.join(WEEK, 'week-33-grades-2-3.pdf'),
    'grades-4-5': os.path.join(WEEK, 'week-33-grades-4-5.pdf'),
    'guide': os.path.join(WEEK, 'week-33-facilitator.pdf'),
    'bonus': os.path.join(WEEK, 'week-33-bonus.pdf'),
    'bonus-guide': os.path.join(WEEK, 'week-33-bonus-facilitator.pdf'),
}


def rotations(w):
    """All readouts of the ring w, one per start, in start order."""
    return [w[i:] + w[:i] for i in range(len(w))]


def readouts(w):
    """Set of distinct readouts (the rotation family / orbit)."""
    return set(rotations(w))


def canon(w):
    """Rotation-class representative: least rotation."""
    return min(rotations(w))


def canon_flip(w):
    """Class under rotations and reflections (flips)."""
    return min(rotations(w) + rotations(w[::-1]))


def period(w):
    """Least positive rotation that restores w (brute force)."""
    n = len(w)
    for d in range(1, n + 1):
        if w[d:] + w[:d] == w:
            return d
    raise AssertionError


def words(alphabet, n):
    return [''.join(t) for t in product(alphabet, repeat=n)]


def necklaces(alphabet, n):
    """Distinct rings (rotation classes), by brute force over all words."""
    return sorted({canon(w) for w in words(alphabet, n)})


def families(alphabet, n):
    """Map class representative -> sorted list of member words."""
    fam = {}
    for w in words(alphabet, n):
        fam.setdefault(canon(w), []).append(w)
    return fam


def proper(w):
    """Different kinds at every neighbouring pair, including the closing pair."""
    n = len(w)
    return all(w[i] != w[(i + 1) % n] for i in range(n))


def windows(w, k):
    """Clockwise k-letter window starting at every bead, wrapping around."""
    n = len(w)
    return [''.join(w[(i + j) % n] for j in range(k)) for i in range(n)]


def is_prime(n):
    return n >= 2 and all(n % q for q in range(2, int(n ** 0.5) + 1))


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
