"""The specific towns used on the pages.

Sizes are chosen so that a 1-inch counter sitting in the middle of any bridge
clears every other band and island (Town.counter_check)."""

import math
from towns import Town, S, H3, grid, tri_lattice


def rotate(t, deg, name=None):
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    u = t.copy(name or t.name)
    u.letters = dict(t.letters)

    def rot(p):
        return (c * p[0] - s * p[1], s * p[0] + c * p[1])

    u.isl = {n: rot(p) for n, p in t.isl.items()}
    br = []
    for a_, b_, spec in t.br:
        if spec is not None and spec[0] == 'ctrl':
            spec = ('ctrl', rot(spec[1]), rot(spec[2]))
        br.append((a_, b_, spec))
    u.br = br
    return u


def reading_letters(t, skip=()):
    """Letter islands A, B, C, ... in reading order (top to bottom, left to right)."""
    names = sorted(t.order, key=lambda n: (-round(t.isl[n][1], 1), round(t.isl[n][0], 1)))
    letters = [chr(ord('A') + i) for i in range(26) if chr(ord('A') + i) not in skip]
    t.letters = {n: letters[i] for i, n in enumerate(names)}
    return t


def polar(r, deg):
    return (r * math.cos(math.radians(deg)), r * math.sin(math.radians(deg)))


# ------------------------------------------------------------------ towns with parallel bridges

def triple(name, d=7.0, h=4.0):
    """Two islands joined by three bridges."""
    t = Town(name)
    t.island('A', 0, 0).island('B', d, 0)
    t.bridge('A', 'B').curved('A', 'B', h).curved('A', 'B', -h)
    return t


def row_doubles(name, d=6.2, h=2.0):
    t = Town(name)
    t.island('L', 0, 0).island('M', d, 0).island('R', 2 * d, 0)
    t.double('L', 'M', h).double('M', 'R', h)
    return t


def double_then_single(name, d=6.2, s=S, h=2.0):
    t = Town(name)
    t.island('L', 0, 0).island('M', d, 0).island('R', d + s, 0)
    t.double('L', 'M', h)
    t.bridge('M', 'R')
    return t


def square_double_side(name, a=6.2, b=S, h=2.0):
    """Square whose bottom side is doubled."""
    t = Town(name)
    t.island('A', 0, 0).island('B', a, 0).island('C', a, b + 0.6).island('D', 0, b + 0.6)
    t.double('A', 'B', h)
    t.bridge('B', 'C').bridge('C', 'D').bridge('D', 'A')
    return t


def ladder_double_rung(name, s=S, h=2.0):
    """Two squares side by side; the middle rung is doubled."""
    t = Town(name)
    for i in range(3):
        t.island(f'b{i}', i * (s + 0.9), 0)
        t.island(f't{i}', i * (s + 0.9), s + 0.6)
    for i in range(2):
        t.bridge(f'b{i}', f'b{i + 1}').bridge(f't{i}', f't{i + 1}')
    t.bridge('b0', 't0').bridge('b2', 't2')
    t.double('b1', 't1', h)
    return t


def double_triangle(name, L=6.3, h=3.6):
    """Triangle A (top left), B (bottom left), C (right) whose side A-B is doubled:
    one A-B bridge is straight, the other bulges out to the left."""
    t = Town(name)
    t.island('A', 0, L / 2).island('B', 0, -L / 2).island('C', L * H3, 0)
    t.bridge('A', 'B').curved('A', 'B', -h)
    t.bridge('A', 'C').bridge('B', 'C')
    return t


# ------------------------------------------------------------------ hubs and fans

def fan(name, s=S, with_cd=True):
    """Hub O with five bridges: two triangles O-A-B (lower left) and O-C-D (lower right)
    and a tail O-E straight up.  Without C-D the town has four odd islands
    (O with 5 bridges, and C, D, E with 1)."""
    t = Town(name)
    t.island('O', 0, 0)
    for n, a in zip('ABCDE', [210, 150, 30, -30, 90]):
        t.island(n, *polar(s, a))
        t.bridge('O', n)
    t.bridge('A', 'B')
    if with_cd:
        t.bridge('C', 'D')
    return t


def lollipop(name, s=S):
    """Triangle with a tail: islands with 2, 2, 3 and 1 bridges."""
    t = Town(name)
    t.island('A', 0, 0).island('B', s, 0).island('C', s / 2, s * H3).island('D', s / 2 + s, s * H3)
    t.bridge('A', 'B').bridge('B', 'C').bridge('C', 'A').bridge('C', 'D')
    return t


# ------------------------------------------------------------------ squares with a centre island

def theta_square(name, side=8.4):
    t = Town(name)
    t.island('A', 0, 0).island('B', side, 0).island('C', side, side).island('D', 0, side)
    t.island('O', side / 2, side / 2)
    for u, v in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('O', 'A'), ('O', 'C')]:
        t.bridge(u, v)
    return t


def square_x(name, side=8.4):
    t = Town(name)
    t.island('A', 0, 0).island('B', side, 0).island('C', side, side).island('D', 0, side)
    t.island('O', side / 2, side / 2)
    for u, v in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
                 ('O', 'A'), ('O', 'B'), ('O', 'C'), ('O', 'D')]:
        t.bridge(u, v)
    return t


def square_center3(name, side=8.4):
    t = Town(name)
    t.island('A', 0, 0).island('B', side, 0).island('C', side, side).island('D', 0, side)
    t.island('O', side / 2, side / 2)
    for u, v in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('O', 'A'), ('O', 'B'), ('O', 'C')]:
        t.bridge(u, v)
    return t


# ------------------------------------------------------------------ squares with tails

def square_adjacent_tails(name, s=S, tail=S):
    """Square with tails out of its two top corners."""
    t = Town(name)
    q = tail / math.sqrt(2)
    t.island('A', 0, 0).island('B', s, 0).island('C', s, s).island('D', 0, s)
    t.island('E', -q, s + q).island('F', s + q, s + q)
    for u, v in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'E'), ('C', 'F')]:
        t.bridge(u, v)
    return t


def square_opposite_tails(name, s=S, tail=S):
    """Square with a tail out of its bottom left corner and one out of its top right corner."""
    t = Town(name)
    t.island('A', 0, 0).island('B', s, 0).island('C', s, s).island('D', 0, s)
    t.island('E', -tail, 0).island('F', s + tail, s)
    for u, v in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('E', 'A'), ('C', 'F')]:
        t.bridge(u, v)
    return t


# ------------------------------------------------------------------ ladders and grids

def m_ladder(name, s=6.0):
    """2x3 ladder ring without the middle rung, plus two diagonals from the top middle."""
    t = Town(name)
    for i in range(3):
        t.island(f'b{i}', i * s, 0)
        t.island(f't{i}', i * s, s)
    for u, v in [('b0', 'b1'), ('b1', 'b2'), ('t0', 't1'), ('t1', 't2'), ('b0', 't0'), ('b2', 't2'),
                 ('t1', 'b0'), ('t1', 'b2')]:
        t.bridge(u, v)
    return t


def h_shape(name, s=S):
    t = Town(name)
    for i, y in enumerate([s, 0, -s]):
        t.island(f'l{i}', 0, y)
        t.island(f'r{i}', s, y)
    for u, v in [('l0', 'l1'), ('l1', 'l2'), ('r0', 'r1'), ('r1', 'r2'), ('l1', 'r1')]:
        t.bridge(u, v)
    return t


def grid_diag(name, s=6.0):
    t = grid(name, 3, 3, s)
    t.bridge('01', '10')
    return t


def lee_big(name, s=S):
    """Triangular town of side 3; outside islands lettered A..I anticlockwise from bottom left."""
    t = tri_lattice(name, 3, s)
    outside = ['0_0', '1_0', '2_0', '3_0', '2_1', '1_2', '0_3', '0_2', '0_1']
    t.letters = {n: chr(ord('A') + k) for k, n in enumerate(outside)}
    t.letters['1_1'] = 'J'
    return t
