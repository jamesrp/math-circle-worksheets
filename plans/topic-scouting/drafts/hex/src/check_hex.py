"""Mathematical checks for the Hex week.

Coordinates: cell (r, c), row r = 0 at the top, column c = 0 at the left.
Rows are drawn shifted right by half a hexagon per row, so the board is a
rhombus whose sharp corners are (0, 0) and (n-1, n-1).
Red joins row 0 to row n-1; Blue joins column 0 to column n-1.
"""
import itertools
import random
from functools import lru_cache


def neighbours(n, r, c):
    for dr, dc in ((0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, -1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < n and 0 <= cc < n:
            yield rr, cc


def has_chain(n, cells, colour):
    """cells: dict (r,c) -> 'R'/'B'/None.  Red: top-bottom.  Blue: left-right."""
    if colour == 'R':
        start = [(0, c) for c in range(n) if cells.get((0, c)) == 'R']
        goal = lambda r, c: r == n - 1
    else:
        start = [(r, 0) for r in range(n) if cells.get((r, 0)) == 'B']
        goal = lambda r, c: c == n - 1
    seen = set(start)
    stack = list(start)
    while stack:
        r, c = stack.pop()
        if goal(r, c):
            return True
        for nb in neighbours(n, r, c):
            if nb not in seen and cells.get(nb) == colour:
                seen.add(nb)
                stack.append(nb)
    return False


def full_board_check(n):
    allc = [(r, c) for r in range(n) for c in range(n)]
    counts = {'R': 0, 'B': 0, 'both': 0, 'none': 0}
    for bits in range(1 << (n * n)):
        cells = {p: ('R' if bits >> i & 1 else 'B') for i, p in enumerate(allc)}
        rw, bw = has_chain(n, cells, 'R'), has_chain(n, cells, 'B')
        counts['both' if rw and bw else 'R' if rw else 'B' if bw else 'none'] += 1
    return counts


def random_full_check(n, trials):
    allc = [(r, c) for r in range(n) for c in range(n)]
    bad = 0
    for _ in range(trials):
        cells = {p: random.choice('RB') for p in allc}
        if has_chain(n, cells, 'R') == has_chain(n, cells, 'B'):
            bad += 1
    return bad


def solver(n):
    allc = [(r, c) for r in range(n) for c in range(n)]

    @lru_cache(maxsize=None)
    def wins(state, to_move):
        """state: tuple of 'R','B','.'; True if `to_move` can force a win."""
        cells = {p: (s if s != '.' else None) for p, s in zip(allc, state)}
        other = 'B' if to_move == 'R' else 'R'
        if has_chain(n, cells, other):
            return False
        if has_chain(n, cells, to_move):
            return True
        for i, s in enumerate(state):
            if s == '.':
                nxt = state[:i] + (to_move,) + state[i + 1:]
                cn = dict(cells)
                cn[allc[i]] = to_move
                if has_chain(n, cn, to_move):
                    return True
                if not wins(nxt, other):
                    return True
        return False

    return allc, wins


def winning_openings(n, first='R'):
    allc, wins = solver(n)
    second = 'B' if first == 'R' else 'R'
    res = {}
    for i, p in enumerate(allc):
        state = tuple(first if j == i else '.' for j in range(n * n))
        res[p] = not wins(state, second)
    return res


def show(n, marks):
    for r in range(n):
        print('  ' * r + '   '.join(marks[(r, c)] for c in range(n)))


def position_value(n, red, blue, to_move):
    allc, wins = solver(n)
    state = tuple('R' if p in red else 'B' if p in blue else '.' for p in allc)
    return wins(state, to_move)


def best_moves(n, red, blue, to_move):
    """Return the empty cells that win for to_move."""
    allc, wins = solver(n)
    other = 'B' if to_move == 'R' else 'R'
    out = []
    for p in allc:
        if p in red or p in blue:
            continue
        r2 = set(red) | ({p} if to_move == 'R' else set())
        b2 = set(blue) | ({p} if to_move == 'B' else set())
        cells = {q: ('R' if q in r2 else 'B' if q in b2 else None) for q in allc}
        if has_chain(n, cells, to_move):
            out.append(p)
            continue
        state = tuple('R' if q in r2 else 'B' if q in b2 else '.' for q in allc)
        if not wins(state, other):
            out.append(p)
    return out


# ---------- square board (for the contrast problem) ----------

def square_chain(n, cells, colour, corners):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if corners:
        steps += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    if colour == 'R':
        start = [(0, c) for c in range(n) if cells[(0, c)] == 'R']
        goal = lambda r, c: r == n - 1
    else:
        start = [(r, 0) for r in range(n) if cells[(r, 0)] == 'B']
        goal = lambda r, c: c == n - 1
    seen, stack = set(start), list(start)
    while stack:
        r, c = stack.pop()
        if goal(r, c):
            return True
        for dr, dc in steps:
            q = (r + dr, c + dc)
            if 0 <= q[0] < n and 0 <= q[1] < n and q not in seen and cells[q] == colour:
                seen.add(q)
                stack.append(q)
    return False


def square_counts(n, corners):
    allc = [(r, c) for r in range(n) for c in range(n)]
    counts = {'R': 0, 'B': 0, 'both': 0, 'none': 0}
    for bits in range(1 << (n * n)):
        cells = {p: ('R' if bits >> i & 1 else 'B') for i, p in enumerate(allc)}
        rw = square_chain(n, cells, 'R', corners)
        bw = square_chain(n, cells, 'B', corners)
        counts['both' if rw and bw else 'R' if rw else 'B' if bw else 'none'] += 1
    return counts


if __name__ == '__main__':
    for n in (2, 3, 4):
        print(n, 'full boards:', full_board_check(n))
    for n in (5, 7):
        print(n, 'random full boards with 0 or 2 winners:', random_full_check(n, 20000))
    for n in (2, 3):
        w = winning_openings(n)
        print(f'{n}x{n} openings that win for first player Red:', sum(w.values()))
        show(n, {p: ('W' if v else 'L') for p, v in w.items()})
    print('square 3x3 side-touching:', square_counts(3, False))
    print('square 3x3 corner-touching:', square_counts(3, True))
    print('square 4x4 side-touching:', square_counts(4, False))
    print('square 4x4 corner-touching:', square_counts(4, True))


def walk_check(n):
    """Every full n x n board: the walk from the top-left corner ends at the
    bottom-left corner exactly when Red has a chain, at the top-right corner
    exactly when Blue has one, and never at the bottom-right corner."""
    from hexgeom import walk
    allc = [(r, c) for r in range(n) for c in range(n)]
    ends = {}
    for bits in range(1 << (n * n)):
        cells = {p: ('R' if bits >> i & 1 else 'B') for i, p in enumerate(allc)}
        _, end = walk(n, cells)
        winner = 'R' if has_chain(n, cells, 'R') else 'B'
        ends[(end, winner)] = ends.get((end, winner), 0) + 1
    return ends


if __name__ == '__main__':
    for n in (2, 3, 4):
        print(n, 'walk end vs winner:', walk_check(n))
