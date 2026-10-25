"""Independent checks for every answer printed in the Hex facilitator guide.

Written for the guide; it does not import the student build or its checkers.
Positions were read off the rendered final student PDFs (and agree with the
student build's data).

Coordinates: (row, column), row 0 at the top, column 0 at the left.  Each row
is drawn half a hexagon to the right of the row above, so the sharp (60
degree) corners are (0,0) and (n-1,n-1).  Red joins row 0 to row n-1, Blue
joins column 0 to column n-1.  Neighbours of (r,c): (r,c-1) (r,c+1) (r-1,c)
(r-1,c+1) (r+1,c) (r+1,c-1).

Run:  python3 check_guide.py      (about a minute)
"""
import itertools
import random
import sys
from functools import lru_cache

OFFS = ((0, -1), (0, 1), (-1, 0), (-1, 1), (1, 0), (1, -1))
FAIL = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def nbrs(n, r, c):
    for dr, dc in OFFS:
        rr, cc = r + dr, c + dc
        if 0 <= rr < n and 0 <= cc < n:
            yield rr, cc


def chain(n, colour_of, col):
    """Does colour col join its two edges?  colour_of: dict cell -> 'R'/'B'."""
    if col == 'R':
        todo = [(0, c) for c in range(n) if colour_of.get((0, c)) == 'R']
        done = lambda p: p[0] == n - 1
    else:
        todo = [(r, 0) for r in range(n) if colour_of.get((r, 0)) == 'B']
        done = lambda p: p[1] == n - 1
    seen = set(todo)
    while todo:
        p = todo.pop()
        if done(p):
            return True
        for q in nbrs(n, *p):
            if q not in seen and colour_of.get(q) == col:
                seen.add(q)
                todo.append(q)
    return False


def cells(n):
    return [(r, c) for r in range(n) for c in range(n)]


# ---------------------------------------------------------------- solver

class Game:
    """Exact solver for small boards by bitmask minimax."""

    def __init__(self, n):
        self.n = n
        self.idx = {p: i for i, p in enumerate(cells(n))}
        self.cell = cells(n)
        self.nb = [sum(1 << self.idx[q] for q in nbrs(n, *p)) for p in self.cell]
        self.top = sum(1 << self.idx[(0, c)] for c in range(n))
        self.bot = sum(1 << self.idx[(n - 1, c)] for c in range(n))
        self.left = sum(1 << self.idx[(r, 0)] for r in range(n))
        self.right = sum(1 << self.idx[(r, n - 1)] for r in range(n))
        self.full = (1 << (n * n)) - 1
        self.win = lru_cache(maxsize=None)(self._win)

    def mask(self, ps):
        return sum(1 << self.idx[p] for p in ps)

    def spread(self, seed, allowed):
        reach = seed & allowed
        while True:
            new = reach
            m = reach
            while m:
                b = m & -m
                new |= self.nb[b.bit_length() - 1] & allowed
                m ^= b
            if new == reach:
                return reach
            reach = new

    def red_won(self, R):
        return bool(self.spread(self.top, R) & self.bot)

    def blue_won(self, B):
        return bool(self.spread(self.left, B) & self.right)

    def _win(self, R, B, red_to_move):
        """True when the player to move can force a win."""
        empty = self.full & ~(R | B)
        m = empty
        while m:
            b = m & -m
            m ^= b
            if red_to_move:
                if self.red_won(R | b) or not self.win(R | b, B, False):
                    return True
            else:
                if self.blue_won(B | b) or not self.win(R, B | b, True):
                    return True
        return False

    def good_moves(self, red, blue, red_to_move):
        R, B = self.mask(red), self.mask(blue)
        out = []
        for p in self.cell:
            b = 1 << self.idx[p]
            if (R | B) & b:
                continue
            if red_to_move:
                if self.red_won(R | b) or not self.win(R | b, B, False):
                    out.append(p)
            else:
                if self.blue_won(B | b) or not self.win(R, B | b, True):
                    out.append(p)
        return out

    def empties(self, red, blue):
        return [p for p in self.cell if p not in red and p not in blue]


# ---------------------------------------------------------------- boundary path

def outside_colour(n, p):
    r, c = p
    if 0 <= r < n and 0 <= c < n:
        return None
    return 'R' if (r < 0 or r >= n) else 'B'


def walk(n, colour_of, vertices=False):
    """Path from the top-left corner along red/blue boundaries.

    A vertex is the set of three mutually touching cells (cells off the board
    take the colour of the band they lie in).  Returns (end corner, sides),
    or with vertices=True (end corner, list of vertices visited)."""
    col = lambda p: colour_of.get(p) or outside_colour(n, p)
    TL = frozenset([(0, 0), (0, -1), (-1, 0)])
    corners = {
        frozenset([(0, n - 1), (0, n), (-1, n)]): 'top-right',
        frozenset([(n - 1, n - 1), (n - 1, n), (n, n - 1)]): 'bottom-right',
        frozenset([(n - 1, 0), (n - 1, -1), (n, -1)]): 'bottom-left',
    }

    def adj(a, b):
        return (b[0] - a[0], b[1] - a[1]) in OFFS

    def common(a, b):
        return [(a[0] + dr, a[1] + dc) for dr, dc in OFFS if adj((a[0] + dr, a[1] + dc), b)]

    # leave TL along the side of (0,0) that separates it from the other colour
    a = (0, 0)
    b = (-1, 0) if col(a) == 'B' else (0, -1)
    V = TL
    sides = 0
    seen = {V}
    visited = [V]
    while True:
        # cross the edge (a,b) from vertex V to the other vertex on it
        third = [x for x in common(a, b) if x not in V]
        assert len(third) == 1
        V = frozenset([a, b, third[0]])
        sides += 1
        assert V not in seen, "path revisited a vertex"
        seen.add(V)
        visited.append(V)
        if V in corners:
            return corners[V], (visited if vertices else sides)
        t = third[0]
        # of the two other edges at V, exactly one separates red from blue
        if col(t) == col(a):
            a, b = t, b
        else:
            a, b = t, a
        assert col(a) != col(b)


# ---------------------------------------------------------------- checks

def full_boards():
    print("\n== Full boards: exactly one winner (Hex theorem instances)")
    for n in (2, 3, 4):
        cs = cells(n)
        tally = {'R': 0, 'B': 0, 'both': 0, 'none': 0}
        ends = {}
        for bits in range(1 << (n * n)):
            col = {p: ('R' if bits >> i & 1 else 'B') for i, p in enumerate(cs)}
            r, b = chain(n, col, 'R'), chain(n, col, 'B')
            tally['both' if r and b else 'R' if r else 'B' if b else 'none'] += 1
            end, _ = walk(n, col)
            key = (end, 'R' if r else 'B')
            ends[key] = ends.get(key, 0) + 1
        check(tally['both'] == 0 and tally['none'] == 0,
              f"{n}x{n}: {1 << n*n} full boards, none with 0 or 2 winners {tally}")
        check(set(ends) == {('bottom-left', 'R'), ('top-right', 'B')},
              f"{n}x{n}: path from top-left ends bottom-left exactly when Red wins, "
              f"top-right exactly when Blue wins, never bottom-right {ends}")
    random.seed(1)
    for n in (5, 7, 11):
        bad = 0
        for _ in range(20000):
            col = {p: random.choice('RB') for p in cells(n)}
            if chain(n, col, 'R') == chain(n, col, 'B'):
                bad += 1
        check(bad == 0, f"{n}x{n}: 20000 random full boards, all with exactly one winner")


def square_board():
    print("\n== 4x4 square board (2-3 P3, 4-5 P4)")
    n = 4
    cs = cells(n)

    def sq_chain(col, c, diag):
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if diag:
            steps += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        if c == 'R':
            todo = [(0, j) for j in range(n) if col[(0, j)] == 'R']
            done = lambda p: p[0] == n - 1
        else:
            todo = [(i, 0) for i in range(n) if col[(i, 0)] == 'B']
            done = lambda p: p[1] == n - 1
        seen = set(todo)
        while todo:
            p = todo.pop()
            if done(p):
                return True
            for dr, dc in steps:
                q = (p[0] + dr, p[1] + dc)
                if q in col and q not in seen and col[q] == c:
                    seen.add(q)
                    todo.append(q)
        return False

    none_side = both_diag = 0
    for bits in range(1 << 16):
        col = {p: ('R' if bits >> i & 1 else 'B') for i, p in enumerate(cs)}
        if not sq_chain(col, 'R', False) and not sq_chain(col, 'B', False):
            none_side += 1
        if sq_chain(col, 'R', True) and sq_chain(col, 'B', True):
            both_diag += 1
    check(none_side == 21150, f"side-touching: {none_side} of 65536 fillings have no winner")
    check(both_diag == 21150, f"corner-touching counts: {both_diag} fillings have two winners")
    cb = {(i, j): ('R' if (i + j) % 2 == 0 else 'B') for i, j in cs}
    check(not sq_chain(cb, 'R', False) and not sq_chain(cb, 'B', False)
          and sq_chain(cb, 'R', True) and sq_chain(cb, 'B', True),
          "checkerboard: nobody wins with sides, both win with corners")


def openings_3x3(g3):
    print("\n== 3x3 first moves (K-1 P6, 2-3 P8, 4-5 P3)")
    win = [p for p in g3.cell if not g3.win(g3.mask([p]), 0, False)]
    check(win == [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)],
          f"Red's winning first moves: {win} (5 of 9)")
    lose = [p for p in g3.cell if p not in win]
    for p in lose:
        rep = g3.good_moves([p], [], False)
        print(f"     Red opens {p}: Blue's winning replies {rep}")
    check(g3.good_moves([(0, 0)], [], False) == [(1, 1)],
          "K-1 P6 corner star (0,0): Blue stops Red only by answering in the centre")
    check(g3.win(g3.mask([(1, 1)]), 0, False) is False,
          "K-1 P6 centre star: Blue cannot stop Red")
    # Red's replies after each winning opening, for the adult's table
    for p in win:
        row = []
        for q in g3.empties([p], []):
            reps = g3.good_moves([p], [q], True)
            row.append(f"B{q}->R{reps}")
        print(f"     Red opens {p}: " + "; ".join(row))
    return win


def two_way_centre(g3):
    """After Red's centre opening, the pairing (0,1)/(0,2) and (2,0)/(2,1) wins."""
    print("\n== Centre opening: pairing strategy")
    pairs = {(0, 1): (0, 2), (0, 2): (0, 1), (2, 0): (2, 1), (2, 1): (2, 0)}
    ok = True

    def play(red, blue):
        nonlocal ok
        R, B = g3.mask(red), g3.mask(blue)
        if g3.red_won(R):
            return
        if g3.blue_won(B):
            ok = False
            return
        for q in g3.empties(red, blue):            # every Blue move
            b2 = blue + [q]
            if g3.blue_won(g3.mask(b2)):
                ok = False
                return
            reply = pairs.get(q)
            if reply is None or reply in red or reply in b2:
                rest = g3.empties(red, b2)
                untouched = [x for x in ((0, 1), (0, 2), (2, 0), (2, 1)) if x in rest]
                reply = untouched[0] if untouched else (rest[0] if rest else None)
            if reply is None:
                ok = ok and g3.red_won(R)
                continue
            play(red + [reply], b2)

    play([(1, 1)], [])
    check(ok, "Red at the centre, answering (0,1)<->(0,2) and (2,0)<->(2,1), wins against every Blue play")


def fewest_blue(n, fixed_red=()):
    cs = cells(n)
    free = [p for p in cs if p not in fixed_red]
    for k in range(0, len(free) + 1):
        sets = []
        for blue in itertools.combinations(free, k):
            col = {p: ('B' if p in blue else 'R') for p in cs}
            if not chain(n, col, 'R'):
                sets.append(blue)
        if sets:
            return k, sets


def blockers():
    print("\n== Fewest blue counters (K-1 P7, 2-3 P4, 2-3 P5)")
    for n, want in ((3, 3), (4, 4), (5, 5)):
        k, sets = fewest_blue(n)
        allchains = all(chain(n, {p: ('B' if p in s else 'R') for p in cells(n)}, 'B') for s in sets)
        onepercol = all(sorted(c for _, c in s) == list(range(n)) for s in sets)
        check(k == want and allchains and onepercol,
              f"{n}x{n}: fewest = {k}, {len(sets)} sets; each is a blue left-right chain "
              f"with one counter in each slanted column")
    red5 = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 0)]
    k, sets = fewest_blue(5, red5)
    check(k == 6, f"2-3 P5 (red at {red5}): fewest = {k}, {len(sets)} different sets")
    print("     e.g.", sets[0])
    check(((3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)) in [tuple(sorted(s)) for s in sets],
          "2-3 P5 example set (3,0),(3,1),(4,1),(4,2),(4,3),(4,4) works")
    # six red routes that share no empty hexagon: a lower-bound certificate
    routes = [
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 0)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
    ]
    okr = True
    for rt in routes:
        okr &= rt[0][0] == 0 and rt[-1][0] == 4
        okr &= all((b[0] - a[0], b[1] - a[1]) in OFFS for a, b in zip(rt, rt[1:]))
    empties = [[p for p in rt if p not in red5] for rt in routes]
    flat = [p for e in empties for p in e]
    okr &= len(flat) == len(set(flat))
    check(okr, "2-3 P5: six top-to-bottom routes sharing no empty hexagon (so 6 are needed)")


def puzzles(g4):
    print("\n== 2-3 P6 and P7: Blue to move")
    games = [
        ("P6 top", [(0, 1), (1, 1), (2, 1)], [(3, 0), (0, 3)], [(3, 1)]),
        ("P6 bottom", [(0, 2), (1, 1), (3, 0)], [(1, 2), (2, 2)], []),
        ("P7 top", [(1, 1), (2, 2)], [(0, 0)], []),
        ("P7 bottom", [(0, 0), (1, 1), (2, 2)], [(2, 3), (3, 2)], [(2, 1)]),
    ]
    for name, red, blue, want in games:
        R, B = g4.mask(red), g4.mask(blue)
        legal = len(red) == len(blue) + 1 and not g4.red_won(R) and not g4.blue_won(B)
        got = g4.good_moves(red, blue, False)
        check(legal and got == want, f"{name}: Blue's stopping moves {got or 'none'}")
        if not got:
            # Red's answer to every Blue move
            print("     Red's winning answers:",
                  "; ".join(f"B{q}->R{g4.good_moves(red, blue + [q], True)}"
                            for q in g4.empties(red, blue)))
        else:
            m = got[0]
            # after Blue's stop, Blue's winning answers to each Red move
            print("     after Blue", m, "Blue's answers:",
                  "; ".join(f"R{q}->B{g4.good_moves(red + [q], blue + [m], False)}"
                            for q in g4.empties(red, blue + [m])))
    # one-move threats in P6 bottom
    red, blue = [(0, 2), (1, 1), (3, 0)], [(1, 2), (2, 2)]
    imm = [q for q in g4.empties(red, blue) if g4.red_won(g4.mask(red + [q]))]
    check(imm == [(2, 0), (2, 1)], f"P6 bottom: Red's one-move wins {imm}")
    red, blue = [(0, 1), (1, 1), (2, 1)], [(3, 0), (0, 3)]
    imm = [q for q in g4.empties(red, blue) if g4.red_won(g4.mask(red + [q]))]
    check(imm == [(3, 1)], f"P6 top: Red threatens to win at once only at {imm}")


def extra_counter(g4):
    print("\n== 4-5 P9: Red to move, then one extra red counter")
    red, blue = [(1, 1), (3, 1)], [(0, 1), (2, 3)]
    R, B = g4.mask(red), g4.mask(blue)
    check(len(red) == len(blue) and not g4.red_won(R) and not g4.blue_won(B), "position legal, Red's turn")
    wm = g4.good_moves(red, blue, True)
    check(wm == [(1, 2)], f"Red's winning moves: {wm}")
    print("     after R(1,2), Red's answers:",
          "; ".join(f"B{q}->R{g4.good_moves(red + [(1, 2)], blue + [q], True)}"
                    for q in g4.empties(red + [(1, 2)], blue)))
    allok = True
    for e in g4.empties(red, blue):
        r2 = red + [e]
        w = g4.red_won(g4.mask(r2)) or bool(g4.good_moves(r2, blue, True))
        allok &= w
    check(allok, "with one extra red counter on any of the 12 empty hexagons, Red (to move) still wins")
    bw = g4.good_moves(red, blue, False)
    print(f"     (if it were Blue's turn instead, Blue would win at {bw})")
    # monotonicity on all small positions: an extra red counter never turns a red win into a loss
    g3 = Game(3)
    bad = 0
    for code in itertools.product((0, 1, 2), repeat=9):
        red = [p for p, v in zip(g3.cell, code) if v == 1]
        blue = [p for p, v in zip(g3.cell, code) if v == 2]
        R, B = g3.mask(red), g3.mask(blue)
        if g3.red_won(R) or g3.blue_won(B):
            continue
        for tomove in (True, False):
            red_wins = g3.win(R, B, True) if tomove else not g3.win(R, B, False)
            if not red_wins:
                continue
            for e in g3.empties(red, blue):
                R2 = R | g3.mask([e])
                still = g3.red_won(R2) or (g3.win(R2, B, True) if tomove else not g3.win(R2, B, False))
                bad += not still
    check(bad == 0, "3x3, every position: adding a red counter never spoils a Red win")


def walk_boards():
    print("\n== 4-5 P6: boundary paths on the two printed boards")
    boards = [
        ["BRBBR", "BRRRB", "RBBRB", "BRRBR", "BRBRB"],
        ["RRBRB", "BRRBR", "RBRBB", "BBRBR", "RBBRB"],
    ]
    want = [('bottom-left', 'R'), ('top-right', 'B')]
    for rows, w in zip(boards, want):
        col = {(r, c): rows[r][c] for r in range(5) for c in range(5)}
        end, sides = walk(5, col)
        winner = 'R' if chain(5, col, 'R') else 'B'
        check((end, winner) == w and chain(5, col, 'R') != chain(5, col, 'B'),
              f"board {''.join(rows[0])}...: ends {end} after {sides} sides; winner {winner}")
        _, verts = walk(5, col, vertices=True)
        side = lambda k: verts[k - 1] & verts[k]          # the two cells on either side of side k
        on = lambda e: [p for p in e if 0 <= p[0] < 5 and 0 <= p[1] < 5]
        check(all(on(side(k)) == [(2, 0)] and len(side(k)) == 2 for k in (7, 8)),
              "   sides 7 and 8 run along the left edge beside (2,0), 1-based (3,1)")


def first_player_small():
    print("\n== First player wins on small boards (strategy-stealing instances)")
    for n in (2, 3, 4):
        g = Game(n)
        check(g.win(0, 0, True), f"{n}x{n}: Red moving first can force a win")
        nwin = sum(not g.win(g.mask([p]), 0, False) for p in g.cell)
        print(f"     {n}x{n}: {nwin} of {n*n} first moves win")


def example_and_launch():
    print("\n== Rules example (6x6) and the guide's launch pictures")
    red = [(0, 2), (1, 2), (2, 1), (3, 1), (3, 2), (4, 2), (5, 1)]
    blue = [(1, 1), (2, 2), (2, 3), (4, 1), (4, 3), (1, 4)]
    col = {p: 'R' for p in red}
    col.update({p: 'B' for p in blue})
    check(chain(6, col, 'R') and not chain(6, col, 'B') and len(red) == len(blue) + 1,
          "rules example: Red has a chain, Blue has none, 7 red and 6 blue")
    # Launch panels (6x6, a size no task uses), leading up to the rules example.
    p1r = [(0, 2), (1, 2), (2, 1), (3, 1)]
    p1b = [(1, 1), (2, 2), (2, 3), (4, 1)]
    p2r, p2b = p1r + [(3, 2)], p1b                 # Red steps sideways past Blue's (4,1)
    panels = (("input", p1r, p1b), ("one step", p2r, p2b), ("output", red, blue))
    for name, r, b in panels:
        cc = {p: 'R' for p in r}
        cc.update({p: 'B' for p in b})
        seen = {p for p in r if p[0] == 0}
        todo = list(seen)
        while todo:
            p = todo.pop()
            for q in nbrs(6, *p):
                if q in r and q not in seen:
                    seen.add(q)
                    todo.append(q)
        won = chain(6, cc, 'R') or chain(6, cc, 'B')
        print(f"     launch {name}: red {len(r)} blue {len(b)}; every red joined to the top: {seen == set(r)}; "
              f"someone has won: {won}")
    check(len(p1r) == len(p1b) and len(p2r) == len(p2b) + 1 and set(p2r) <= set(red) and set(p1b) <= set(blue),
          "launch panels: legal counts with Red first, and they lead to the rules example")
    check(not chain(6, {**{p: 'R' for p in p2r}, **{p: 'B' for p in p2b}}, 'R'),
          "launch step: Red has not yet won after the sideways step")
    check((3, 2) in set(nbrs(6, 3, 1)) and (4, 1) in set(nbrs(6, 3, 1)),
          "launch: (3,2) shares a side with (3,1); Blue's (4,1) is one of (3,1)'s lower neighbours")


def rect_winner(rows, cols):
    """Exact solver on a board with rows x cols hexagons (Red joins top and
    bottom, crossing `rows` rows; Blue joins the sides, crossing `cols`)."""
    cs = [(r, c) for r in range(rows) for c in range(cols)]
    idx = {p: i for i, p in enumerate(cs)}
    nb = [0] * len(cs)
    for (r, c), i in idx.items():
        for dr, dc in OFFS:
            q = (r + dr, c + dc)
            if q in idx:
                nb[i] |= 1 << idx[q]
    top = sum(1 << idx[(0, c)] for c in range(cols))
    bot = sum(1 << idx[(rows - 1, c)] for c in range(cols))
    left = sum(1 << idx[(r, 0)] for r in range(rows))
    right = sum(1 << idx[(r, cols - 1)] for r in range(rows))
    full = (1 << len(cs)) - 1

    def spread(seed, allowed):
        reach = seed & allowed
        while True:
            new = reach
            m = reach
            while m:
                b = m & -m
                new |= nb[b.bit_length() - 1] & allowed
                m ^= b
            if new == reach:
                return reach
            reach = new

    @lru_cache(maxsize=None)
    def win(R, B, red):
        m = full & ~(R | B)
        while m:
            b = m & -m
            m ^= b
            if red:
                if spread(top, R | b) & bot or not win(R | b, B, False):
                    return True
            else:
                if spread(left, B | b) & right or not win(R, B | b, True):
                    return True
        return False
    return win(0, 0, True), win(0, 0, False)


def extensions(g4):
    print("\n== Extensions printed in the guide")
    w4 = [p for p in g4.cell if not g4.win(g4.mask([p]), 0, False)]
    check(w4 == [(0, 3), (1, 2), (2, 1), (3, 0)],
          f"4x4: winning first moves {w4} = 1-based (1,4) (2,3) (3,2) (4,1), the short diagonal")
    for rows, cols in ((2, 3), (3, 4)):
        red_first, blue_first = rect_winner(rows, cols)
        check(red_first and not blue_first,
              f"{rows} rows x {cols} columns: Red (crossing {rows} rows) wins moving first and moving second")


def guide_coordinates(g3, g4):
    """The guide prints (row, column) counted from 1.  Re-check every move it
    names, in those coordinates."""
    print("\n== Moves named in the guide, 1-based coordinates")
    z = lambda *ps: [(r - 1, c - 1) for r, c in ps]       # 1-based -> 0-based
    o = lambda ps: sorted((r + 1, c + 1) for r, c in ps)   # 0-based -> 1-based

    def red_wins_after(red, blue, g):
        """Red has just moved: Red has won, or Blue to move cannot force a win."""
        return g.red_won(g.mask(red)) or not g.win(g.mask(red), g.mask(blue), False)

    def blue_wins_after(red, blue, g):
        return g.blue_won(g.mask(blue)) or not g.win(g.mask(red), g.mask(blue), True)

    # 3x3 openings
    win = o(p for p in g3.cell if not g3.win(g3.mask([p]), 0, False))
    check(win == [(1, 3), (2, 1), (2, 2), (2, 3), (3, 1)], f"3x3 winning first moves {win}")
    for op in [(1, 1), (1, 2), (3, 2), (3, 3)]:
        check(o(g3.good_moves(z(op), [], False)) == [(2, 2)], f"opening {op}: Blue's only good reply is (2,2)")
    check(sorted(o(q for q in nbrs(3, 1, 1) if q[1] == 0)) == [(2, 1), (3, 1)] and
          sorted(o(q for q in nbrs(3, 1, 1) if q[1] == 2)) == [(1, 3), (2, 3)] and
          sorted(o(q for q in nbrs(3, 1, 1) if q[0] == 0)) == [(1, 2), (1, 3)] and
          sorted(o(q for q in nbrs(3, 1, 1) if q[0] == 2)) == [(3, 1), (3, 2)],
          "middle (2,2): top (1,2)/(1,3), bottom (3,1)/(3,2), left (2,1)/(3,1), right (1,3)/(2,3)")
    # opening (1,3)
    R0 = z((1, 3))
    ok = True
    for q in g3.empties(R0, []):
        q1 = o([q])[0]
        if q1 in [(2, 2), (3, 1), (3, 2)]:
            continue
        ok &= red_wins_after(R0 + z((2, 2)), [q], g3)
    ok &= red_wins_after(R0 + z((2, 3)), z((2, 2)), g3)
    ok &= red_wins_after(R0 + z((3, 2)), z((3, 1)), g3)
    ok &= red_wins_after(R0 + z((3, 1)), z((3, 2)), g3)
    ok &= red_wins_after(R0 + z((3, 1), (2, 1)), z((3, 2), (2, 2)), g3)
    ok &= not red_wins_after(R0 + z((2, 2)), z((3, 2)), g3)   # the middle fails against (3,2)
    check(ok, "opening (1,3): the guide's answers to every Blue reply win")
    # opening (2,1)
    R0 = z((2, 1))
    ok = True
    for q in g3.empties(R0, []):
        if o([q])[0] in [(2, 2), (3, 1), (3, 2)]:
            continue
        ok &= red_wins_after(R0 + z((2, 2)), [q], g3)
    ok &= red_wins_after(R0 + z((3, 1)), z((2, 2)), g3)
    ok &= red_wins_after(R0 + z((3, 1)), z((3, 2)), g3)
    ok &= o(g3.good_moves(R0, z((3, 1)), True)) == [(2, 3)]
    check(ok, "opening (2,1): the guide's answers win; against (3,1) only (2,3) wins")
    # 2-3 P5
    red5 = z((1, 3), (2, 3), (3, 3), (4, 3), (5, 1))
    k, sets = fewest_blue(5, red5)
    got = sorted(tuple(o(s_)) for s_ in sets)
    want = sorted(tuple(sorted([(4, 1), (4, 2), (5, 2), (5, 3)] + extra)) for extra in
                  ([(5, 4), (5, 5)], [(5, 4), (4, 5)], [(4, 4), (4, 5)], [(4, 4), (3, 5)]))
    check(k == 6 and got == want, "2-3 P5: the four best sets named in the guide, and no others")
    # 2-3 P6 and P7
    g1r, g1b = z((1, 2), (2, 2), (3, 2)), z((4, 1), (1, 4))
    check(o(g4.good_moves(g1r, g1b, False)) == [(4, 2)], "P6 top: stop at (4,2)")
    B = g1b + z((4, 2))
    check(blue_wins_after(g1r + z((3, 3)), B + z((4, 3)), g4) and
          blue_wins_after(g1r + z((4, 3)), B + z((3, 3)), g4),
          "P6 top: after (4,2), Blue answers (3,3) with (4,3) and (4,3) with (3,3)")
    g2r, g2b = z((1, 3), (2, 2), (4, 1)), z((2, 3), (3, 3))
    check(o(q for q in g4.empties(g2r, g2b) if g4.red_won(g4.mask(g2r + [q]))) == [(3, 1), (3, 2)],
          "P6 bottom: Red wins at once at (3,1) or (3,2)")
    g3r, g3b = z((2, 2), (3, 3)), z((1, 1))
    pairs = [((1, 2), (1, 3)), ((2, 3), (3, 2)), ((4, 2), (4, 3))]
    check(all(red_wins_after(g3r + z(b_), g3b + z(a), g4) and red_wins_after(g3r + z(a), g3b + z(b_), g4)
              for a, b_ in pairs), "P7 top: Red answers each pair cell with its partner")
    g4r, g4b = z((1, 1), (2, 2), (3, 3)), z((3, 4), (4, 3))
    check(o(g4.good_moves(g4r, g4b, False)) == [(3, 2)], "P7 bottom: stop at (3,2)")
    B = g4b + z((3, 2))
    pairs = [((3, 1), (4, 1)), ((4, 2), (2, 3))]
    check(all(blue_wins_after(g4r + z(a), B + z(b_), g4) and blue_wins_after(g4r + z(b_), B + z(a), g4)
              for a, b_ in pairs), "P7 bottom: after (3,2), Blue pairs (3,1)/(4,1) and (4,2)/(2,3)")
    check(red_wins_after(g4r + z((4, 1)), g4b + z((4, 2)), g4) and
          red_wins_after(g4r + z((3, 2)), g4b + z((2, 3)), g4),
          "P7 bottom: Blue (4,2) loses to Red (4,1); Blue (2,3) loses to Red (3,2)")
    # 4-5 P9
    pr, pb = z((2, 2), (4, 2)), z((1, 2), (3, 4))
    check(o(g4.good_moves(pr, pb, True)) == [(2, 3)], "4-5 P9: Red's only winning move (2,3)")
    check(o(g4.good_moves(pr, pb, False)) == [(1, 3), (1, 4), (2, 3), (3, 2), (3, 3)],
          "4-5 P9: Blue to move would win at (1,3) (1,4) (2,3) (3,2) (3,3)")
    R2 = pr + z((2, 3))
    pairs = [((1, 3), (1, 4)), ((3, 2), (3, 3))]
    check(all(red_wins_after(R2 + z(b_), pb + z(a), g4) and red_wins_after(R2 + z(a), pb + z(b_), g4)
              for a, b_ in pairs), "4-5 P9: after (2,3), Red pairs (1,3)/(1,4) and (3,2)/(3,3)")
    # 4-5 P6 chains
    b1 = ["BRBBR", "BRRRB", "RBBRB", "BRRBR", "BRBRB"]
    b2 = ["RRBRB", "BRRBR", "RBRBB", "BBRBR", "RBBRB"]
    red_chain = z((1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (5, 2))
    blue_chain = z((4, 1), (4, 2), (5, 2), (5, 3), (4, 4), (3, 4), (3, 5))

    def is_chain(cells_, rows, col, a_edge, b_edge):
        okc = all(rows[r][c] == col for r, c in cells_)
        okc &= all((q[0] - p_[0], q[1] - p_[1]) in OFFS for p_, q in zip(cells_, cells_[1:]))
        return okc and a_edge(cells_[0]) and b_edge(cells_[-1])
    check(is_chain(red_chain, b1, 'R', lambda p_: p_[0] == 0, lambda p_: p_[0] == 4),
          "4-5 P6 board 1: the guide's red chain is a chain from top to bottom")
    check(is_chain(blue_chain, b2, 'B', lambda p_: p_[1] == 0, lambda p_: p_[1] == 4),
          "4-5 P6 board 2: the guide's blue chain is a chain from left to right")
    check(b1[2][0] == 'R' and b2[2][0] == 'R', "4-5 P6: (3,1) is red on both boards")


def rect_full(rows, cols):
    """Every full colouring of a board with rows x cols hexagons: count how
    many have no winner and how many have two (Theorem 1 on unequal boards)."""
    cs = [(r, c) for r in range(rows) for c in range(cols)]
    idx = {p: i for i, p in enumerate(cs)}
    nb = [0] * len(cs)
    for (r, c), i in idx.items():
        for dr, dc in OFFS:
            q = (r + dr, c + dc)
            if q in idx:
                nb[i] |= 1 << idx[q]
    top = sum(1 << idx[(0, c)] for c in range(cols))
    bot = sum(1 << idx[(rows - 1, c)] for c in range(cols))
    left = sum(1 << idx[(r, 0)] for r in range(rows))
    right = sum(1 << idx[(r, cols - 1)] for r in range(rows))
    full = (1 << len(cs)) - 1

    def joins(seed, goal, allowed):
        reach = seed & allowed
        while True:
            new = reach
            m = reach
            while m:
                b = m & -m
                new |= nb[b.bit_length() - 1] & allowed
                m ^= b
            if new == reach:
                return bool(reach & goal)
            reach = new
    none = both = 0
    for R in range(full + 1):
        r, b = joins(top, bot, R), joins(left, right, full & ~R)
        none += not r and not b
        both += r and b
    return none, both


def revision_checks(g4):
    """Answers added or changed in the revision (final/src)."""
    print("\n== Revision: answers added or changed")
    z = lambda *ps: [(r - 1, c - 1) for r, c in ps]
    o = lambda ps: sorted((r + 1, c + 1) for r, c in ps)

    def blue_wins_after(red, blue):
        """Blue has just moved: Blue has won, or Red to move cannot force a win."""
        return g4.blue_won(g4.mask(blue)) or not g4.win(g4.mask(red), g4.mask(blue), True)

    # S1: 2-3 P6 top, Blue's follow-up after the stop at (4,2), against every Red reply.
    red, blue = z((1, 2), (2, 2), (3, 2)), z((4, 1), (1, 4), (4, 2))
    ok = True
    for q in g4.empties(red, blue):
        answer = z((4, 3)) if o([q]) == [(3, 3)] else z((3, 3))
        ok &= blue_wins_after(red + [q], blue + answer)
    check(ok, "2-3 P6 top: after Blue (4,2), Blue wins by answering (3,3), or (4,3) if Red took (3,3)")
    fin = lambda B: o(q for q in g4.empties(red, B) if g4.blue_won(g4.mask(B + [q])))
    check(fin(blue + z((3, 3))) == [(2, 3), (2, 4), (3, 4)],
          "2-3 P6 top: from (3,3) Blue finishes at once at (2,3), (2,4) or (3,4)")
    check(fin(blue + z((4, 3))) == [(3, 4), (4, 4)],
          "2-3 P6 top: from (4,3) Blue finishes at once at (3,4) or (4,4)")
    check(o(g4.good_moves(red + z((3, 4)), blue, False)) == [(3, 3), (4, 3), (4, 4)],
          "2-3 P6 top: after Red (3,4), Blue's winning replies are (3,3), (4,3), (4,4)")
    R34, B33 = red + z((3, 4)), blue + z((3, 3))
    check(o(q for q in g4.empties(R34, B33) if g4.blue_won(g4.mask(B33 + [q]))) == [(2, 3), (2, 4)],
          "2-3 P6 top: after Red (3,4) and Blue (3,3), Blue still has two finishes, (2,3) and (2,4)")

    # Minor 2: a 3-rows-by-4-columns board made from a 4x4 board with its bottom row red.
    row4 = g4.mask(z((4, 1), (4, 2), (4, 3), (4, 4)))
    red_first = g4.win(row4, 0, True)
    blue_first = g4.win(row4, 0, False)
    rf, bf = rect_winner(3, 4)
    check(red_first and not blue_first and (red_first, blue_first) == (rf, bf),
          "4x4 with its bottom row red = 3 rows x 4 columns: Red wins moving first and moving second")

    # Minor 3: Theorem 1 holds on unequal boards; strategy stealing does not carry over.
    for rows, cols in ((2, 3), (2, 4), (3, 4), (3, 5)):
        none, both = rect_full(rows, cols)
        check(none == 0 and both == 0,
              f"{rows} rows x {cols} columns: all {1 << rows * cols} full boards have exactly one winner")
    for rows, cols in ((2, 4), (3, 5)):
        red_first, blue_first = rect_winner(rows, cols)
        check(red_first and not blue_first,
              f"{rows} rows x {cols} columns: Red (crossing {rows} rows) wins moving first and moving second")

    # Minor 1: counter supply.  Red moves first, so a full 7x7 game has 25 red and 24 blue;
    # every fill or blocker board has at most 25 hexagons.
    check((49 + 1) // 2 == 25 and 49 // 2 == 24, "full 7x7 game: at most 25 red and 24 blue counters")
    # hexagons (or squares) a pair may fill with counters at once, per page; 2-3 p5 has 5 printed red
    pages = {"K-1 p1": 9, "K-1 p2 (two 3x3)": 18, "K-1 p3": 16, "K-1 p4": 16, "K-1 p5 (two 3x3)": 18,
             "K-1 p6 (3x3 + 4x4)": 25, "2-3 p1": 25, "2-3 p2": 16, "2-3 p3 squares": 16, "2-3 p4": 25,
             "2-3 p5": 20, "4-5 p1": 25, "4-5 p2": 25, "4-5 p3": 9, "4-5 p4 squares": 16}
    check(max(pages.values()) <= 25, "every page except the 7x7 needs at most 25 counters in all")
    check(max(max(pages.values()), (49 + 1) // 2) <= 25,
          "so no page needs more than 25 counters of one colour (the 7x7 game: 25 red at most)")
    check(6 * 25 == 150, "five pair bags and a launch set of 25 per colour: 150 of each colour")


def column_argument():
    print("\n== Every slanted column is a red route; a blue chain meets every column")
    for n in (3, 4, 5, 7, 11):
        ok = all(((r + 1, c) in set(nbrs(n, r, c))) for c in range(n) for r in range(n - 1))
        ok &= all(abs(dc) <= 1 for _, dc in OFFS)
        check(ok, f"{n}x{n}: column c is a top-bottom chain; a step changes the column by at most 1")


if __name__ == "__main__":
    full_boards()
    square_board()
    g3, g4 = Game(3), Game(4)
    openings_3x3(g3)
    two_way_centre(g3)
    blockers()
    puzzles(g4)
    extra_counter(g4)
    walk_boards()
    first_player_small()
    example_and_launch()
    column_argument()
    extensions(g4)
    guide_coordinates(g3, g4)
    revision_checks(g4)
    print("\nFAILURES:", FAIL if FAIL else "none")
    sys.exit(1 if FAIL else 0)
