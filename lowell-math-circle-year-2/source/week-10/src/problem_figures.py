"""The towns and pictures the Week 10 problem files draw, by band and problem number.

check.py checks them. For one band, every figure section that band prints is
evaluated in ../figures.py, in packet order, which records each town in T and each
one-stroke picture in PICS under the problem number its figure code gives, as the
old builders did.
"""
import sys
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WEEK.parent / "problem-files"))
import atoms  # noqa: E402


def towns_and_pictures(band):
    week = atoms.load_week(WEEK)
    T, PICS = week.figures["T"], week.figures["PICS"]
    T.clear()
    PICS.clear()
    for p in atoms.compose(week, band):
        for s in p.atom.resolve(band):
            if s.kind == "figure":
                atoms.figure(week, p.atom, s)
    return dict(T), dict(PICS)
