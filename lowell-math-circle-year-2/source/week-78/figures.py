"""Week 78 (Three-armed lines): the grid boards for the problem files.

The coordinates are student/data.py's, which both checkers read; this module loads that
file and draws the boards as the old student builder did (its boards() function, carried
over unchanged), so each board's LaTeX is the old build's cases.tex macro written inline.
The board, junction and target commands are defined in template.tex.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location('week78_data', Path(__file__).resolve().parent / 'student' / 'data.py')
data = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(data)


def point_macro(kind, xy, label):
    return rf"\{kind}{{{xy[0]}}}{{{xy[1]}}}{{{label}}}"


def boards(pairs, scale, kind, columns=2):
    chunks=[]
    for row_start in range(0,len(pairs),columns):
        row=[]
        for pair in pairs[row_start:row_start+columns]:
            labels = ('A','B') if kind == 'junction' else ('P','Q')
            commands=[point_macro(kind,p,labels[i]) for i,p in enumerate(pair)]
            commands+=['']*(2-len(commands))
            row.append(rf"\board{{{scale}}}{{{commands[0]}}}{{{commands[1]}}}")
        chunks.append(r"\noindent " + r"\hfill ".join(row))
    return "\n\\par\\vspace{7pt}\n".join(chunks)


def trial_boards():
    """Problem 1: two boards with only A = TRIAL_JUNCTION, then the two fixed pairs."""
    return boards(((data.TRIAL_JUNCTION,),)*2 + data.TRIAL_FIXED_PAIRS, .78, 'junction')


def _then(tex, then):
    """`then` is LaTeX that followed the boards inside the same paragraph in the old source
    (a \\vspace before the next problem). Keeping it there keeps the old line ends, and so
    the old horizontal placement of the boards, exactly."""
    return tex + ('\n' + then if then else '')


def intersection_boards(then=''):
    return _then(boards(data.INTERSECTION_PAIRS, .82, 'junction'), then)


def general_boards(then=''):
    return _then(boards(data.INVERSE_GENERAL, .83, 'target'), then)


def aligned_boards():
    return boards(data.INVERSE_ALIGNED, .66, 'target', columns=3)


def cropped_board(then=''):
    """Problem 6: A alone on the board (B is off it), with writing space beside."""
    return _then(boards(((data.CROPPED_PAIR[0],),), .76, 'junction')
                 + '\n' + r'\hfill\begin{minipage}[b][2.65in][t]{3.7in}\strut\end{minipage}', then)
