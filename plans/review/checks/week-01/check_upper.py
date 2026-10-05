"""Grades 4-5: H122 board, all lozenge tilings, cards A-F, ribbons, flips, routes, parity."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import re, sys
from collections import deque
from itertools import permutations
sys.path.insert(0, HERE)
from lattice import *

s = open(SRC + 'tilings.tex').read()
defs = {}
for m in re.finditer(r'\\newcommand\{\\(\w+)\}\{', s):
    start = m.end(); depth = 1; k = start
    while depth:
        if s[k] == '{': depth += 1
        elif s[k] == '}': depth -= 1
        k += 1
    defs[m.group(1)] = s[start:k - 1]

common = open(SRC + 'common.tex').read()
bp = re.search(r'\\newcommand\{\\BoardPath\}\{([^}]*)\}', common).group(1).replace('\\hh', str(H))
# evaluate expressions like 2*0.866
def ev(t):
    return eval(t.replace('{', '').replace('}', ''))
board_xy = [(ev(a), ev(b)) for a, b in re.findall(r'\(([^,()]+),([^()]+)\)', bp)]
board = cells_in_poly(board_xy)
print('Board vertices (lattice):', [tuple(int(x) for x in to_lattice(*p)) for p in board_xy])
up = sum(1 for c in board if c[0] == 'U')
print('Board cells:', len(board), 'up', up, 'down', len(board) - up)

grid_cells = set(cell_from_vertices([to_lattice(*p) for p in parse_points(seg)])
                 for seg in re.findall(r'\\draw\[gridline\]\s*([^;]*);', defs['BoardGrid']))
print('BoardGrid cells == board interior cells:', grid_cells == board)

blue_pls = placements(BLUE, board)
all_tilings = [frozenset(t) for t in count_tilings(board, blue_pls)]
print('Number of blue tilings of the board:', len(all_tilings))

cards = {}
for L in 'ABCDEF':
    tiles = []
    for seg in re.findall(r'\\draw\[tile\]\s*([^;]*);', defs['Tiling' + L]):
        tiles.append(frozenset(cells_in_poly(parse_points(seg))))
    t = frozenset(tiles)
    ok = all(len(x) == 2 and normalize(x) in all_orientations(BLUE) for x in tiles)
    cards[L] = t
    print(f'Card {L}: {len(tiles)} tiles, all blue={ok}, is a tiling={t in set(all_tilings)}')
print('Cards distinct:', len(set(cards.values())) == 6, ' cards cover all tilings:', set(cards.values()) == set(all_tilings))


def orient(t):
    """'R': U(i,j)+D(i,j) ; 'L': U(i,j)+D(i-1,j) ; 'V': U(i,j)+D(i,j-1)."""
    u = [c for c in t if c[0] == 'U'][0]; d = [c for c in t if c[0] == 'D'][0]
    _, i, j = u
    if d == ('D', i, j): return 'R', u
    if d == ('D', i - 1, j): return 'L', u
    if d == ('D', i, j - 1): return 'V', u
    raise ValueError(t)


def ribbon(tiling):
    """Start at the bottom boundary horizontal edge; follow rhombi with horizontal edges upward."""
    # bottom edge: lattice (0,0)-(1,0) -> up cell U(0,0)
    by_cell = {c: t for t in tiling for c in t}
    cur = ('U', 0, 0)
    code = ''; pts = [(Fraction(1, 2), 0)]
    while cur in by_cell:
        o, u = orient(by_cell[cur])
        assert o in 'RL', (o, cur)
        _, i, j = u
        code += o
        # top edge of the rhombus
        if o == 'R':   # top edge (i,j+1)-(i+1,j+1) -> next up cell U(i,j+1)
            nxt = ('U', i, j + 1)
            pts.append((i + Fraction(1, 2), j + 1))
        else:          # D(i-1,j) top edge (i-1,j+1)-(i,j+1) -> next U(i-1,j+1)
            nxt = ('U', i - 1, j + 1)
            pts.append((i - Fraction(1, 2), j + 1))
        cur = nxt
    return code, pts

codes = {}
for L in 'ABCDEF':
    code, pts = ribbon(cards[L])
    codes[L] = code
    drawn = []
    segs = re.findall(r'\\draw\[[^\]]*\]\s*([^;]*);', defs['Path' + L])
    for seg in segs:
        a, b = parse_points(seg)
        drawn.append((to_lattice(*a), to_lattice(*b)))
    computed = list(zip(pts, pts[1:]))
    # convert lattice midpoints to compare
    same = [ (tuple(a), tuple(b)) for a, b in computed] == [ (tuple(a), tuple(b)) for a, b in drawn]
    nh = sum(1 for t in cards[L] if orient(t)[0] in 'RL')
    print(f'Card {L}: ribbon {code}  drawn path matches computed: {same};  horizontal-edge rhombi in tiling: {nh}')

print('All 6 orders of RRLL realized:', sorted(codes.values()) == sorted(set(''.join(p) for p in permutations('RRLL'))))

# Geometric flips: unit hexagon around interior lattice point covered by exactly 3 tiles of the tiling
interior_pts = set()
for c in board:
    for p in cell_vertices(c):
        if hex_around(*p) <= board:
            interior_pts.add(p)
print('Interior lattice points (potential flip centres):', sorted(interior_pts))

def flips(t):
    out = []
    for p in interior_pts:
        hx = hex_around(*p)
        inside = [x for x in t if x <= hx]
        if len(inside) == 3:
            other = [frozenset(x) for x in count_tilings(hx, placements(BLUE, hx)) if frozenset(x) != frozenset(inside)]
            assert len(other) == 1
            new = (t - frozenset(inside)) | other[0]
            out.append((p, new))
    return out

name = {v: k for k, v in cards.items()}
edges = set()
deg = {}
for L in 'ABCDEF':
    fl = flips(cards[L])
    deg[L] = len(fl)
    for p, new in fl:
        edges.add(tuple(sorted((L, name[new]))))
print('Flip edges:', sorted(edges))
print('Degrees:', deg)
turns = {L: sum(1 for k in range(3) if codes[L][k] != codes[L][k + 1]) for L in 'ABCDEF'}
print('Adjacent RL/LR counts:', turns)
# each flip swaps one adjacent pair in the code?
for a, b in sorted(edges):
    ca, cb = codes[a], codes[b]
    diff = [k for k in range(4) if ca[k] != cb[k]]
    print(f'  {a}-{b}: {ca} -> {cb} differ at positions {[d+1 for d in diff]}')

# BFS distances and shortest routes
adj = {L: set() for L in 'ABCDEF'}
for a, b in edges:
    adj[a].add(b); adj[b].add(a)
def all_shortest(src, dst):
    dist = {src: 0}; q = deque([src])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in dist:
                dist[y] = dist[x] + 1; q.append(y)
    routes = []
    def rec(path):
        if path[-1] == dst:
            routes.append(''.join(path)); return
        for y in adj[path[-1]]:
            if dist.get(y, 99) == dist[path[-1]] + 1:
                rec(path + [y])
    rec([src])
    return dist, routes
dist, routes = all_shortest('A', 'F')
print('Distances from A:', dist, ' shortest A->F routes:', routes)
# bipartite
col = {'A': 0}; q = deque('A'); bip = True
while q:
    x = q.popleft()
    for y in adj[x]:
        if y not in col: col[y] = 1 - col[x]; q.append(y)
        elif col[y] == col[x]: bip = False
print('Bipartite:', bip, 'classes:', sorted(k for k in col if col[k] == 0), sorted(k for k in col if col[k] == 1))
# closed walks from A of length 1..8 (pure Python)
L6 = 'ABCDEF'
idx = {L: k for k, L in enumerate(L6)}
M = [[0]*6 for _ in range(6)]
for x, y in edges:
    M[idx[x]][idx[y]] = M[idx[y]][idx[x]] = 1
def matmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
Pw = [[int(i == j) for j in range(6)] for i in range(6)]
walks = []
for n in range(1, 9):
    Pw = matmul(Pw, M); walks.append(Pw[0][0])
print('Closed walks A->A of length n=1..8:', walks)

# Highlighted flip patch in Problem 2 (A <-> B)
gr = open(SRC + 'week-01-grades-4-5.tex').read()
i0 = gr.index('\\newcommand{\\FlipPatch}{') + len('\\newcommand{\\FlipPatch}{')
dep = 1; k = i0
while dep:
    dep += {'{': 1, '}': -1}.get(gr[k], 0); k += 1
fp = gr[i0:k - 1].replace('\\hh', str(H))
print('FlipPatch source:', fp)
fp_xy = [(ev(a), ev(b)) for a, b in re.findall(r'\(([^,()]+),([^()]+)\)', fp)]
patch = cells_in_poly(fp_xy)
print('Flip patch lattice vertices:', [tuple(int(x) for x in to_lattice(*p)) for p in fp_xy], 'cells', len(patch),
      'is unit hexagon:', any(patch == hex_around(*p) for p in interior_pts))
diffA = cards['A'] - cards['B']; diffB = cards['B'] - cards['A']
print('A\\B tiles inside patch:', all(t <= patch for t in diffA), len(diffA), ' B\\A inside patch:', all(t <= patch for t in diffB), len(diffB))

# Random walks with exact fractions
def solve(A, bvec):
    n = len(A); A = [row[:] + [bvec[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0); A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [A[r][k] - f * A[c][k] for k in range(n + 1)]
    return [A[i][n] / A[i][i] for i in range(n)]
def stationary(P):
    n = len(P)
    # solve pi (P - I) = 0, sum pi = 1  -> replace last equation
    A = [[P[j][i] - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    A[-1] = [Fraction(1)] * n
    return solve(A, [Fraction(0)] * (n - 1) + [Fraction(1)])
def mean_return(P, a=0):
    n = len(P); others = [k for k in range(n) if k != a]
    A = [[(1 if i == j else 0) - P[others[i]][others[j]] for j in range(n - 1)] for i in range(n - 1)]
    h = solve(A, [Fraction(1)] * (n - 1))
    return 1 + sum(P[a][others[k]] * h[k] for k in range(n - 1))
P = [[Fraction(M[i][j], sum(M[i])) for j in range(6)] for i in range(6)]
pi = stationary(P)
print('Simple random walk stationary x12:', [p * 12 for p in pi], ' mean return to A:', mean_return(P))
nc = len(interior_pts)
Q = [[Fraction(M[i][j], nc) for j in range(6)] for i in range(6)]
for i in range(6):
    Q[i][i] = 1 - sum(Q[i])
pi2 = stationary(Q)
print('Lazy centre-choice chain stationary:', pi2, ' mean return to A:', mean_return(Q))

# R-position sums
for L in 'ABCDEF':
    print(L, codes[L], 'R-sum', sum(k + 1 for k, ch in enumerate(codes[L]) if ch == 'R'))

# Scaled hexagon side 2: number of blue tilings
hex2_xy = [(2, 0), (1, 2 * H), (-1, 2 * H), (-2, 0), (-1, -2 * H), (1, -2 * H)]
h2 = cells_in_poly(hex2_xy)
print('Side-2 hexagon cells', len(h2), 'blue tilings', len(count_tilings(h2, placements(BLUE, h2))))

# Bottleneck reserve
bn = {'A': ('U', 0, 0), 'B': ('U', 1, 0), 'C': ('U', 0, 1), 'D': ('D', 0, 0), 'E': ('D', -1, 1), 'F': ('D', 0, 1)}
cells = set()
for seg in re.findall(r'\\draw\[tile\]\s*([^;]*);', defs['Bottleneck']):
    cells.add(cell_from_vertices([to_lattice(*p) for p in parse_points(seg)]))
labels = re.findall(r'\\node\[[^\]]*\] at \(([^)]*)\) \{(\w)\};', defs['Bottleneck'])
lab = {}
for pos, l in labels:
    x, y = map(float, pos.split(','))
    for c in cells:
        cx, cy = centroid(c)
        if abs(cx - x) < 1e-6 and abs(cy - y) < 1e-6:
            lab[l] = c
print('Bottleneck labels:', lab)
inv = {c: l for l, c in lab.items()}
for l in 'ABC':
    print('  ', l, 'neighbours in region:', [inv[n] for n in neighbors(lab[l]) if n in cells])
mb, wit = max_packing(cells, placements(BLUE, cells))
print('  max blues', mb, 'gaps', len(cells) - 2 * mb)
