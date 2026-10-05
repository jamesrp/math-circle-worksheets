"""Shared helpers for the Week 4 math check.

The repository root is four folders up from plans/review/checks/week-04/ (the committed copy);
when run from a scratch run folder instead, walk up until the folder that holds AGENTS.md and
lowell-math-circle-year-2/ is found."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_root():
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    d = HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')) and os.path.exists(os.path.join(d, 'AGENTS.md')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository root not found from ' + HERE)


ROOT = _find_root()
PDFDIR = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-04')
SRCDIR = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-04')
PACKETS = {'K1': 'week-04-k-1.pdf', 'M': 'week-04-grades-2-3.pdf', 'U': 'week-04-grades-4-5.pdf',
           'FAC': 'week-04-facilitator.pdf'}
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift(s, k):
    return ''.join(A[(A.index(c) + k) % 26] if c in A else c for c in s)


def cycles(n, k):
    """Simulate the page rule: start at the lowest dot with no line, hop k until back; repeat."""
    seen, out = set(), []
    for s in range(n):
        if s in seen:
            continue
        cyc, j = [s], (s + k) % n
        seen.add(s)
        while j != s:
            cyc.append(j)
            seen.add(j)
            j = (j + k) % n
        out.append(cyc)
    return out


def chord_set(n, k, restart=True):
    """Unordered chords drawn by hop k on n dots (from dot 0 only when restart=False)."""
    cs = cycles(n, k) if restart else cycles(n, k)[:1]
    out = set()
    for c in cs:
        for i in c:
            j = (i + k) % n
            if i != j:
                out.add(frozenset((i, j)))
    return frozenset(out)
