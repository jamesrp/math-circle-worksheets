"""Independent ball simulator for the Week 9 math check (bouncing paths).

Written from scratch for this review; it does not import or read the packet's
gen.py or check.py.  Everything is computed step by step on the grid, not
from the lcm formula, so the formula the pages and the guide state can be
tested against it.

Rules (from the student pages): the ball starts at a bottom corner of a
w-by-h table (w squares wide, h high), moves one square across and one up per
step, reverses its horizontal direction at a side wall and its vertical
direction at the top or bottom wall, and stops when it lands on a corner.
A bounce is each wall contact before the final corner.
"""
from fractions import Fraction
from math import gcd


def corner_name(x, y, w, h):
    return ('T' if y == h else 'B') + ('R' if x == w else 'L')


def ball(w, h, start='BL', max_steps=None):
    """Walk the ball. Returns dict(points, corner, bounces, hits, steps).

    hits: list of (point, wall, (dx, dy) just before the bounce).
    """
    if start == 'BL':
        x, y, dx, dy = 0, 0, 1, 1
    elif start == 'BR':
        x, y, dx, dy = w, 0, -1, 1
    else:
        raise ValueError(start)
    pts = [(x, y)]
    hits = []
    while True:
        x += dx
        y += dy
        pts.append((x, y))
        if max_steps is not None and len(pts) - 1 >= max_steps:
            return dict(points=pts, corner=None, bounces=len(hits), hits=hits, steps=len(pts) - 1)
        side = x in (0, w)
        end = y in (0, h)
        if side and end:
            break
        if side:
            hits.append(((x, y), 'L' if x == 0 else 'R', (dx, dy)))
            dx = -dx
        if end:
            hits.append(((x, y), 'B' if y == 0 else 'T', (dx, dy)))
            dy = -dy
    return dict(points=pts, corner=corner_name(x, y, w, h), bounces=len(hits), hits=hits,
                steps=len(pts) - 1)


def segments(points):
    return [frozenset((a, b)) for a, b in zip(points, points[1:])]


def crossings(w, h, start='BL'):
    """Self-crossings of the path: interior lattice points visited twice
    (an X), and squares whose two diagonals are both used (an X at the centre).
    Also reports retraced segments."""
    r = ball(w, h, start)
    pts = r['points']
    seen = {}
    for p in pts[1:-1]:
        seen[p] = seen.get(p, 0) + 1
    lattice = sorted(p for p, n in seen.items() if n >= 2 and 0 < p[0] < w and 0 < p[1] < h)
    segs = segments(pts)
    retraced = len(segs) - len(set(segs))
    squares = {}
    for s in set(segs):
        a, b = sorted(s)
        sq = (min(a[0], b[0]), min(a[1], b[1]))
        squares.setdefault(sq, set()).add((a, b))
    centre = sorted(sq for sq, d in squares.items() if len(d) == 2)
    return dict(lattice=lattice, centre=centre, retraced=retraced, count=len(lattice) + len(centre))


def fold(X, period):
    """Fold the unfolded coordinate X back onto [0, period] (mirror copies)."""
    r = X % (2 * period)
    return r if r <= period else 2 * period - r


def sheet_line(w, h, cols, rows, stop):
    """Straight 45-degree line from (0,0) on a sheet of cols x rows copies of a w x h table.

    stop = 'first-crossing': stop at the first point after the start where a
            vertical copy line (x multiple of w) meets a horizontal one;
    stop = 'opposite-corner': stop at (cols*w, cols*w) (the sheet must be square).
    Returns dict(end, inner_lines_crossed (in order), panels (in order), connected,
    folded_segments, fits).
    """
    W, H = cols * w, rows * h
    x = y = 0
    panels = []
    crossed = []
    while True:
        pan = (x // w, y // h)
        if not panels or panels[-1] != pan:
            panels.append(pan)
        x += 1
        y += 1
        if stop == 'first-crossing' and x % w == 0 and y % h == 0:
            break
        if stop == 'opposite-corner' and x == W:
            break
        if x % w == 0:
            crossed.append(('x', x))
        if y % h == 0:
            crossed.append(('y', y))
    fits = x <= W and y <= H
    # connectivity of the panels (edge neighbours only)
    pset = set(panels)
    seen = {panels[0]}
    todo = [panels[0]]
    while todo:
        a, b = todo.pop()
        for n in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
            if n in pset and n not in seen:
                seen.add(n)
                todo.append(n)
    folded = segments([(fold(t, w), fold(t, h)) for t in range(x + 1)])
    return dict(end=(x, y), crossed=crossed, panels=panels, connected=seen == pset,
                folded=folded, fits=fits)


# ---------------------------------------------------------------- 3-D and slopes
def box_home(w, h, d, limit=10 ** 6):
    """45-degree ball in a w x h x d box from the origin: the first time all three
    coordinates are on walls at once, and whether that corner is the origin."""
    t = 0
    while t < limit:
        t += 1
        if t % w == 0 and t % h == 0 and t % d == 0:
            return t, ((t // w) % 2 == 0 and (t // h) % 2 == 0 and (t // d) % 2 == 0)
    return None, None


def slope_ball(w, h, a, b, limit=10 ** 5):
    """Direction (b, a): b across for every a up (integers), table w x h, from (0,0).
    Exact simulation with Fractions: returns (corner, number of wall contacts).
    Points are visited at times where some coordinate meets a grid line."""
    # Parametrise by t: unfolded position (b t, a t). Corner when b t in wZ and a t in hZ.
    # Wall contacts: b t in wZ (side) or a t in hZ (top/bottom), before the corner.
    events = set()
    T = None
    k = 1
    # the first t > 0 with b t = m w and a t = n h
    for m in range(1, limit):
        t = Fraction(m * w, b)
        if (a * t) % h == 0:
            T = t
            break
    for m in range(1, int(T * b / w)):
        events.add(('side', Fraction(m * w, b)))
    for n in range(1, int(T * a / h)):
        events.add(('end', Fraction(n * h, a)))
    X, Y = b * T, a * T
    corner = ('T' if (Y / h) % 2 == 1 else 'B') + ('R' if (X / w) % 2 == 1 else 'L')
    return corner, len(events)


def cutting_word(w, h):
    """Order of side (S) and end (E) hits along the 45-degree path."""
    return ''.join('S' if wall in 'LR' else 'E' for _, wall, _ in ball(w, h)['hits'])


def christoffel_lower(a, b):
    """Lower Christoffel word with a letters 'x' (steps across) and b letters 'y'
    (steps up), a and b coprime: letter i (1..a+b) is 'x' when i*b mod (a+b)
    exceeds (i-1)*b mod (a+b), else 'y' (the standard definition)."""
    n = a + b
    return ''.join('x' if (i * b) % n > ((i - 1) * b) % n else 'y' for i in range(1, n + 1))


if __name__ == '__main__':
    # quick self-test: the simulation stops for every table up to 40 x 40
    for w in range(1, 41):
        for h in range(1, 41):
            r = ball(w, h)
            assert r['corner'] is not None
    print('billiards.py: simulation terminates for all tables up to 40 x 40')
