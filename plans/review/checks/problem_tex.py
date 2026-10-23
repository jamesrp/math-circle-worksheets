"""Band LaTeX for review checks, from wherever the week keeps it now.

Review checks written before October 23, 2026 read each band's LaTeX from
lowell-math-circle-year-2/source/week-NN/src/<band>.tex. Weeks stored as problem files
no longer keep that file: the problem-file tools generate it. band_tex() returns the
committed file when it exists and otherwise the LaTeX the tools generate for the band
whose file name matches (k-1, grades-2-3, grades-4-5 or the band's `file`).

    from problem_tex import band_tex
    tex = band_tex('week-07', 'grades-2-3.tex')
    parts = band_parts('week-11', 'k-1')   # [(problem number or None, kind, text), ...]
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'lowell-math-circle-year-2' / 'source'
TOOLS = SOURCE / 'problem-files'
FILE_NAMES = {'K-1': 'k-1', '2-3': 'grades-2-3', '4-5': 'grades-4-5'}


def _week_and_band(week, filename):
    folder = SOURCE / week
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    import atoms
    w = atoms.load_week(folder)
    stem = filename[:-4] if filename.endswith('.tex') else filename
    for band, spec in w.bands.items():
        if spec.get('file', FILE_NAMES.get(band)) == stem:
            return atoms, w, band
    raise FileNotFoundError(f'{week}: no band writes {filename}')


def band_parts(week, filename):
    """What a child in one band reads, from the problem files: a list of
    (printed problem number or None, section kind, section text as written)."""
    atoms, w, band = _week_and_band(week, filename)
    out = []
    for p in atoms.compose(w, band):
        for sec in p.atom.resolve(band):
            out.append((p.number, sec.kind, sec.raw))
    return out


def band_tex(week, filename, subdir='src'):
    """The LaTeX of one band packet; week is 'week-07', filename 'grades-2-3.tex'."""
    folder = SOURCE / week
    committed = folder / subdir / filename
    if committed.exists():
        return committed.read_text()
    if not (folder / 'week.toml').exists():
        raise FileNotFoundError(committed)
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    import atoms
    w = atoms.load_week(folder)
    stem = filename[:-4] if filename.endswith('.tex') else filename
    for band, spec in w.bands.items():
        if spec.get('file', FILE_NAMES.get(band)) == stem:
            here = os.getcwd()
            try:
                os.chdir(folder)  # templates and figures resolve against the week folder
                return atoms.student_tex(w, band)
            finally:
                os.chdir(here)
    raise FileNotFoundError(f'{week}: no band writes {filename}')
