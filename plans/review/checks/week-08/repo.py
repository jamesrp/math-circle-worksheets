"""Locate the repository and the Week 8 files.

The scripts run either from the review run folder (tmp/review-runs/week-08/) or
from their committed copy in plans/review/checks/week-08/.  The committed copy
is four folders below the repository root; otherwise walk upward until the
folder that holds AGENTS.md and lowell-math-circle-year-2/.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _is_root(d):
    return (os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2'))
            and os.path.exists(os.path.join(d, 'AGENTS.md')))


def find_root():
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if _is_root(cand):
        return cand
    d = HERE
    while d != os.path.dirname(d):
        if _is_root(d):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found above ' + HERE)


ROOT = find_root()
PKT = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-08')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-08')
RV_SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-08-return-visit')

STUDENT = {
    'k-1': os.path.join(PKT, 'week-08-k-1.pdf'),
    'grades-2-3': os.path.join(PKT, 'week-08-grades-2-3.pdf'),
    'grades-4-5': os.path.join(PKT, 'week-08-grades-4-5.pdf'),
}
GUIDE = os.path.join(PKT, 'week-08-facilitator.pdf')
RV_STUDENT = os.path.join(PKT, 'week-08-return-visit.pdf')
RV_GUIDE = os.path.join(PKT, 'week-08-return-visit-facilitator.pdf')
