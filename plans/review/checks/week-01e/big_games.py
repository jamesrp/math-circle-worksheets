"""Exhaustive game search on the two largest Problem 9 boards (4-by-4 and hexagon 3,3,3),
as an independent confirmation of the copying argument.  Writes big_games_<board>.out.
Run with a board name and an optional time bound in seconds:
    python3 big_games.py 4x4          python3 big_games.py hex333 600
The search stops at the bound and records that it did not finish."""
import os, sys, time, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
from fastgame import Board
which = sys.argv[1] if len(sys.argv) > 1 else '4x4'
bound = int(sys.argv[2]) if len(sys.argv) > 2 else 900
want = {'4x4': 32, 'hex333': 54}[which]
b = [o for o in stroked_boards('grades-4-5', 9) if len(o.R) == want][0]
ht = half_turn_centre(b.R)


class Stop(Exception):
    pass


def alarm(*_):
    raise Stop


signal.signal(signal.SIGALRM, alarm)
signal.alarm(bound)
t = time.time()
Bd = Board(b.R)
try:
    w, good, moves = Bd.solve()
    signal.alarm(0)
    msg = (f'{which}: {BD.classify(b)}; half-turn centre {ht[1] if ht else None}; {len(moves)} first moves; '
           f'winner {w}; winning first moves {len(good)}; memo {len(Bd.memo)}; {time.time() - t:.0f} s')
except Stop:
    msg = (f'{which}: {BD.classify(b)}; half-turn centre {ht[1] if ht else None}; exhaustive search stopped at the '
           f'{bound} s bound without finishing (memo {len(Bd.memo)} component values); no result. '
           f'The answer rests on the copying proof, whose hypothesis (half-turn centre at a lattice point) is checked here.')
print(msg)
with open(os.path.join(HERE, f'big_games_{which}.out'), 'w') as fh:
    fh.write(msg + '\n')
