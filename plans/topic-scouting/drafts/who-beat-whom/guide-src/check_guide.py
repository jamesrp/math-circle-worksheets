"""Independent check of every answer printed in the Who beat whom facilitator guide.

Reads the student figures (the TikZ files that the final PDFs were compiled from) and
recovers each printed tournament from the geometry alone: player circles and labels,
link segments, and the direction of each arrowhead. It does not use the page author's
gen.py, tourn.py or answers-check.txt. Then it recomputes line-ups, kings, win counts and
joining places, checks the general facts by enumeration, and builds every construction
the guide describes.

Run:  python3 check_guide.py   (prints a report; any failed assertion stops it)
"""
import math
import re
import sys
from itertools import combinations, permutations, product, combinations_with_replacement

import os
DRAFT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(DRAFT, 'src', 'figs')
ANIMALS = {'cat', 'dog', 'bear', 'rabbit', 'frog', 'pig'}
NUM = r'(-?[\d.]+)'
PT = rf'\({NUM},{NUM}\)'


# ------------------------------------------------------------------ figure parser
def parse_fig(name):
    src = open(f'{FIGS}/{name}.tex').read()
    nodes = []
    for m in re.finditer(rf'\\filldraw\[fill=white[^\]]*\] {PT} circle \({NUM}\);', src):
        nodes.append([float(m[1]), float(m[2]), float(m[3]), None])
    for m in re.finditer(rf'\\node\[[^\]]*\] at {PT} \{{([^}}]*)\}};', src):
        x, y, lab = float(m[1]), float(m[2]), m[3]
        for n in nodes:
            if abs(n[0] - x) < 1e-6 and abs(n[1] - y) < 1e-6:
                n[3] = lab
    for m in re.finditer(rf'\\pic\[[^\]]*\] at {PT} \{{(\w+)\}};', src):
        x, y, lab = float(m[1]), float(m[2]), m[3]
        for n in nodes:
            if abs(n[0] - x) < 1e-6 and abs(n[1] - y) < 1e-6:
                n[3] = lab
    segs = []
    for m in re.finditer(rf'\\draw\[([^\]]*)\] {PT} -- {PT};', src):
        if 'gray' in m[1] or 'dashed' in m[1]:
            continue
        segs.append(((float(m[2]), float(m[3])), (float(m[4]), float(m[5]))))
    heads = []
    for m in re.finditer(rf'\\fill\[black\] {PT} -- {PT} -- {PT} -- {PT} -- cycle;', src):
        p = [(float(m[2 * i + 1]), float(m[2 * i + 2])) for i in range(4)]
        heads.append(p)  # tip, barb, notch, barb
    return nodes, segs, heads


def nearest_node(nodes, p):
    best = min(nodes, key=lambda n: math.hypot(n[0] - p[0], n[1] - p[1]))
    d = math.hypot(best[0] - p[0], best[1] - p[1])
    assert d <= best[2] + 0.2, ('segment end not at a circle', p)
    return best


def read_tournament(name, expect_complete=True):
    """Return (labels in file order, set of (winner, loser)) read from arrowheads."""
    nodes, segs, heads = parse_fig(name)
    labels = [n[3] for n in nodes]
    links = {}
    for s, e in segs:
        a, b = nearest_node(nodes, s)[3], nearest_node(nodes, e)[3]
        assert a != b
        key = frozenset((a, b))
        assert key not in links, (name, 'pair linked twice', key)
        links[key] = (s, e)
    beats = set()
    used = set()
    for tip, b1, notch, b2 in heads:
        c = ((tip[0] + notch[0]) / 2, (tip[1] + notch[1]) / 2)
        d = (tip[0] - notch[0], tip[1] - notch[1])
        dn = math.hypot(*d)
        d = (d[0] / dn, d[1] / dn)
        best, bestdist = None, 9e9
        for key, (s, e) in links.items():
            vx, vy = e[0] - s[0], e[1] - s[1]
            L = math.hypot(vx, vy)
            ux, uy = vx / L, vy / L
            if abs(ux * d[1] - uy * d[0]) > 0.05:   # not parallel
                continue
            t = (c[0] - s[0]) * ux + (c[1] - s[1]) * uy
            if not (0 <= t <= L):
                continue
            dist = abs((c[0] - s[0]) * uy - (c[1] - s[1]) * ux)
            if dist < bestdist:
                best, bestdist = key, dist
        assert best is not None and bestdist < 0.05, (name, 'arrowhead off every link', tip)
        assert best not in used, (name, 'two arrowheads on one link')
        used.add(best)
        s, e = links[best]
        toward_e = (e[0] - s[0]) * d[0] + (e[1] - s[1]) * d[1] > 0
        loser_pt, winner_pt = (e, s) if toward_e else (s, e)
        beats.add((nearest_node(nodes, winner_pt)[3], nearest_node(nodes, loser_pt)[3]))
    if expect_complete:
        n = len(labels)
        assert len(links) == n * (n - 1) // 2, (name, 'not every pair linked')
        assert used == set(links), (name, 'a link has no arrowhead')
    return labels, beats


# ------------------------------------------------------------------ tournament tools
def lineups(players, beats):
    return [p for p in permutations(players)
            if all((p[i], p[i + 1]) in beats for i in range(len(p) - 1))]


def wins(players, beats):
    return {x: sum((x, y) in beats for y in players) for x in players}


def kings(players, beats):
    out = []
    for x in players:
        reach = {y for y in players if (x, y) in beats}
        reach |= {z for y in list(reach) for z in players if (y, z) in beats}
        if reach | {x} == set(players):
            out.append(x)
    return out


def places(results, line='ABCDE'):
    """results[i] = 'W' if X beat line[i]. Gaps 0..n, gap i is before line[i]."""
    n = len(line)
    out = []
    for i in range(n + 1):
        if (i == 0 or results[i - 1] == 'L') and (i == n or results[i] == 'W'):
            out.append('front' if i == 0 else 'back' if i == n else f'{line[i-1]}-{line[i]}')
    return out


def all_tournaments(n):
    pairs = list(combinations(range(n), 2))
    for bits in product((0, 1), repeat=len(pairs)):
        yield frozenset((a, b) if x == 0 else (b, a) for (a, b), x in zip(pairs, bits))


def out_masks(n, t):
    m = [0] * n
    for a, b in t:
        m[a] |= 1 << b
    return m


def count_paths(n, m):
    full = (1 << n) - 1
    total = 0
    firsts = 0
    for s in range(n):
        stack = [(s, 1 << s)]
        c = 0
        while stack:
            v, used = stack.pop()
            if used == full:
                c += 1
                continue
            nxt = m[v] & ~used
            while nxt:
                low = nxt & -nxt
                w = low.bit_length() - 1
                stack.append((w, used | low))
                nxt ^= low
        total += c
        firsts |= (1 << s) if c else 0
    return total, firsts


def king_mask(n, m):
    full = (1 << n) - 1
    k = 0
    for x in range(n):
        r = m[x] | (1 << x)
        y = m[x]
        while y:
            low = y & -y
            r |= m[low.bit_length() - 1]
            y ^= low
        if r == full:
            k |= 1 << x
    return k


def reach_mask(n, m, x):
    seen = 1 << x
    frontier = [x]
    while frontier:
        v = frontier.pop()
        new = m[v] & ~seen
        seen |= new
        while new:
            low = new & -new
            frontier.append(low.bit_length() - 1)
            new ^= low
    return seen


def canon(n, t):
    return min(tuple(sorted((p[a], p[b]) for a, b in t)) for p in permutations(range(n)))


def landau_ok(scores):
    s = sorted(scores)
    n = len(s)
    return sum(s) == n * (n - 1) // 2 and all(sum(s[:k]) >= k * (k - 1) // 2 for k in range(1, n + 1))


def landau_paths(target, beat, rng):
    """The guide's proof idea for 'a passing list always happens', with every choice random.
    target[i] is the wins player i should get; beat is any tournament on players 0..n-1.
    From the players with too many wins, follow arrows forward (in random order). If a player
    with too few is reached, reverse every arrow on that path. If none can be reached, return
    the reached group R: it then won exactly its own games, more than the list gives it.
    Returns ('done', beat) or ('stuck', R)."""
    n = len(target)
    beat = set(beat)
    while True:
        w = [sum((i, j) in beat for j in range(n)) for i in range(n)]
        if w == list(target):
            return 'done', beat
        dist_before = sum(abs(a - b) for a, b in zip(w, target))
        start = [i for i in range(n) if w[i] > target[i]]
        rng.shuffle(start)
        parent = {i: None for i in start}
        queue = list(start)
        found = None
        while queue and found is None:
            u = queue.pop(rng.randrange(len(queue)))       # any order of search
            outs = [v for v in range(n) if (u, v) in beat and v not in parent]
            rng.shuffle(outs)
            for v in outs:
                parent[v] = u
                if w[v] < target[v]:
                    found = v
                    break
                queue.append(v)
        if found is None:
            R = set(parent)
            # nobody outside R lost to anyone in R, so R won exactly its own games
            assert not any((u, v) in beat for u in R for v in range(n) if v not in R)
            assert sum(w[i] for i in R) == len(R) * (len(R) - 1) // 2
            assert sum(target[i] for i in R) < len(R) * (len(R) - 1) // 2
            return 'stuck', R
        path = [found]
        while parent[path[-1]] is not None:
            path.append(parent[path[-1]])
        path.reverse()                                     # surplus player ... deficit player
        for a, b in zip(path, path[1:]):
            beat.remove((a, b))
            beat.add((b, a))
        w2 = [sum((i, j) in beat for j in range(n)) for i in range(n)]
        changed = [i for i in range(n) if w2[i] != w[i]]
        assert sorted(changed) == sorted({path[0], path[-1]})   # only the two ends change
        assert sum(abs(a - b) for a, b in zip(w2, target)) == dist_before - 2


def from_spec(spec):
    out = set()
    for tok in spec.split():
        a, b = tok.split('>')
        out.add((a, b))
    return out


def is_complete(players, beats):
    return all(((a, b) in beats) != ((b, a) in beats) for a, b in combinations(players, 2)) \
        and len(beats) == len(players) * (len(players) - 1) // 2


OK = []


def check(label, got, want):
    assert got == want, f'{label}: got {got!r}, want {want!r}'
    OK.append(label)
    print(f'  ok  {label}: {got}')


def fmt(lus):
    return sorted(' '.join(p) for p in lus)


# ------------------------------------------------------------------ K-1 pages
print('== K-1 ==')
# Problem 3 (page 2): the two triangles.
labs, b = read_tournament('k1_p2a')
check('K1 P3 left: line-ups', fmt(lineups(labs, b)), ['frog pig rabbit'])
labs, b = read_tournament('k1_p2b')
check('K1 P3 right: line-ups', fmt(lineups(labs, b)), ['bear dog cat', 'cat bear dog', 'dog cat bear'])

# Problem 4 (page 3): positions are top-left, top-right, bottom-right, bottom-left in file order.
want4 = {
    'k1_p3a': ['pig cat dog frog'],
    'k1_p3b': ['rabbit bear frog cat', 'rabbit cat bear frog', 'rabbit frog cat bear'],
    'k1_p3c': ['cat rabbit pig dog', 'pig cat rabbit dog', 'rabbit pig cat dog'],
    'k1_p3d': ['bear dog frog rabbit', 'dog frog rabbit bear', 'dog rabbit bear frog',
               'frog rabbit bear dog', 'rabbit bear dog frog'],
}
for fig, want in want4.items():
    labs, b = read_tournament(fig)
    print('     ', fig, 'players TL,TR,BR,BL =', labs, 'wins', wins(labs, b))
    check(f'K1 P4 {fig}: line-ups', fmt(lineups(labs, b)), want)

# Problem 7 (page 4): which animals can be first.
want7 = {'k1_p8a': ['dog'], 'k1_p8b': ['cat', 'pig', 'rabbit'], 'k1_p8c': ['bear', 'dog', 'frog', 'pig']}
for fig, want in want7.items():
    labs, b = read_tournament(fig)
    lus = lineups(labs, b)
    print('     ', fig, 'players TL,TR,BR,BL =', labs, 'wins', wins(labs, b), 'line-ups', fmt(lus))
    check(f'K1 P7 {fig}: can be first', sorted({p[0] for p in lus}), want)
labs, b = read_tournament('k1_p8a')
check('K1 P7 left: dog beat all three', wins(labs, b)['dog'], 3)
labs, b = read_tournament('k1_p8b')
check('K1 P7 middle: bear lost every game', wins(labs, b)['bear'], 0)
labs, b = read_tournament('k1_p8c')
circle = [('frog', 'pig'), ('pig', 'dog'), ('dog', 'bear'), ('bear', 'frog')]
check('K1 P7 right: frog>pig>dog>bear>frog is a circle', all(e in b for e in circle), True)

# Board-wide facts for Problems 5, 6, 8, 9, 10 (all 64 four-animal boards).
cnt = {}
for t in all_tournaments(4):
    c, _ = count_paths(4, out_masks(4, t))
    cnt[c] = cnt.get(c, 0) + 1
check('K1 P5/P6/P10: line-up counts over the 64 boards', dict(sorted(cnt.items())), {1: 24, 3: 16, 5: 24})
# Every board whose arrows make a circle through all four animals has exactly 5 line-ups, and
# conversely.
five_boards = 0
for t in all_tournaments(4):
    m = out_masks(4, t)
    c, _ = count_paths(4, m)
    has_circle = any(all((p[i], p[(i + 1) % 4]) in t for i in range(4)) for p in permutations(range(4)))
    assert (c == 5) == has_circle
    five_boards += c == 5
check('K1 P6: 5 line-ups exactly when the arrows make a four-animal circle', five_boards, 24)
# The guide's example for P6: around the outside cat>dog>bear>rabbit>cat, diagonals either way.
P = ['cat', 'dog', 'bear', 'rabbit']
for d1, d2 in product([('cat', 'bear'), ('bear', 'cat')], [('dog', 'rabbit'), ('rabbit', 'dog')]):
    bb = from_spec('cat>dog dog>bear bear>rabbit rabbit>cat') | {d1, d2}
    assert is_complete(P, bb) and len(lineups(P, bb)) == 5
bb = from_spec('cat>dog dog>bear bear>rabbit rabbit>cat cat>bear dog>rabbit')
check('K1 P6 guide example (diagonals cat>bear, dog>rabbit): line-ups', fmt(lineups(P, bb)),
      ['bear rabbit cat dog', 'cat dog bear rabbit', 'dog bear rabbit cat', 'dog rabbit cat bear',
       'rabbit cat dog bear'])
# The guide's example for P5: a strict ranking.
bb = from_spec('cat>dog cat>bear cat>rabbit dog>bear dog>rabbit bear>rabbit')
check('K1 P5 guide example: line-ups', fmt(lineups(P, bb)), ['cat dog bear rabbit'])
eq3 = [t for t in all_tournaments(3) if len(set(out_masks(3, t)[i].bit_count() for i in range(3))) == 1]
check('K1 P8: boards where cat, dog, bear win equally', len(eq3), 2)
eq4 = [t for t in all_tournaments(4) if len(set(out_masks(4, t)[i].bit_count() for i in range(4))) == 1]
check('K1 P8: boards where four animals win equally', len(eq4), 0)
two = [t for t in all_tournaments(4) if sum(x.bit_count() == 3 for x in out_masks(4, t)) >= 2]
check('K1 P9: boards with two animals that won every game', len(two), 0)

# Board geometry: lanes and squares (for the materials list).
src = open(f'{FIGS}/k1_board.tex').read()
lanes = []
for m in re.finditer(rf'rectangle', src):
    pass
for m in re.finditer(rf'\\draw\[gray!70, dashed[^\]]*\] {PT} rectangle {PT};', src):
    x0, y0, x1, y1 = map(float, m.groups())
    lanes.append((round(x1 - x0, 2), round(y1 - y0, 2)))
sq = [m for m in re.finditer(rf'\\filldraw\[fill=white, line width=1.2pt, rounded corners=3pt\] {PT} rectangle {PT};', src)]
sqsize = {round(float(m[3]) - float(m[1]), 2) for m in sq}
check('K1 board: lane sizes (length, width) in cm', sorted(set(lanes)), [(10.8, 2.3), (15.27, 2.3)])
check('K1 board: lanes', len(lanes), 6)
check('K1 board: animal squares (cm)', sqsize, {4.0})
check('K1 board: diagonal lanes cross at their middles, so two 10 cm cards there overlap',
      10 > 15.27 / 2, True)

# ------------------------------------------------------------------ Grades 2-3
print('== Grades 2-3 ==')
want = {
    'g23_p2a': ['A C B D', 'B D A C', 'C B D A', 'C D A B', 'D A C B'],
    'g23_p2b': ['D B A C'],
    'g23_p2c': ['C E A D B'],
    'g23_p2d': ['B E A C D', 'B E C D A', 'B E D A C'],
}
for fig, w in want.items():
    labs, b = read_tournament(fig)
    print('     ', fig, 'wins', wins(labs, b))
    check(f'2-3 P2 {fig}: line-ups', fmt(lineups(labs, b)), w)
labs, b = read_tournament('g23_p2b')
check('2-3 P2 top right: win counts form a ranking 3,2,1,0', sorted(wins(labs, b).values()), [0, 1, 2, 3])
labs, b = read_tournament('g23_p2c')
check('2-3 P2 bottom left: win counts 4,3,2,1,0', sorted(wins(labs, b).values()), [0, 1, 2, 3, 4])


def newcomer_results(fig):
    labs, b = read_tournament(fig, expect_complete=False)
    line = 'ABCDE'
    for i in range(4):
        assert (line[i], line[i + 1]) in b, (fig, 'line-up arrow')
    res = ''
    for c in line:
        if ('X', c) in b:
            res += 'W'
        else:
            assert (c, 'X') in b
            res += 'L'
    return res


want = {'g23_p4_0': ['C-D'], 'g23_p4_1': ['back'], 'g23_p4_2': ['A-B', 'back'],
        'g23_p4_3': ['front', 'C-D', 'back']}
for fig, w in want.items():
    res = newcomer_results(fig)
    print('     ', fig, 'X vs A..E:', res)
    check(f'2-3 P4 {fig}: places', places(res), w)
# Problem 5 and the general claim: every pattern of results leaves a place, for 1..9 players.
for n in range(1, 10):
    for res in product('WL', repeat=n):
        assert places(''.join(res), line='ABCDEFGHI'[:n])
check('2-3 P5 / 4-5 P3: X can always join (all patterns, up to 9 in the line)', True, True)

want = {'g23_p7a': ['A', 'C', 'D'], 'g23_p7b': ['C'], 'g23_p7c': ['A', 'C', 'D', 'E'],
        'g23_p7d': ['A', 'B', 'C', 'D', 'E']}
for fig, w in want.items():
    labs, b = read_tournament(fig)
    print('     ', fig, 'wins', wins(labs, b))
    check(f'2-3 P7 {fig}: kings', sorted(kings(labs, b)), w)
labs, b = read_tournament('g23_p7c')
check('2-3 P7 bottom left: B beat only A', sorted(y for (x, y) in b if x == 'B'), ['A'])
check('2-3 P7 bottom left: A beat C and E', sorted(y for (x, y) in b if x == 'A'), ['C', 'E'])
labs, b = read_tournament('g23_p7a')
w = wins(labs, b)
check('2-3 P7 top left: the kings are exactly the top scorers (2 wins each)',
      (sorted(kings(labs, b)), sorted(x for x in labs if w[x] == max(w.values())), max(w.values())),
      (['A', 'C', 'D'], ['A', 'C', 'D'], 2))
labs, b = read_tournament('g23_p7c')
w = wins(labs, b)
check('2-3 P7 bottom left: wins', w, {'A': 2, 'B': 1, 'C': 2, 'D': 3, 'E': 2})
check('2-3 P7 bottom left: kings who are not top scorers', sorted(k for k in kings(labs, b) if w[k] < 3),
      ['A', 'C', 'E'])
for fig in ('g23_p7a', 'g23_p7b', 'g23_p7d'):
    labs, b = read_tournament(fig)
    w = wins(labs, b)
    assert all(w[k] == max(w.values()) for k in kings(labs, b)), fig
check('2-3 P7: only the bottom left shows a king who is not a top scorer', True, True)
labs, b = read_tournament('g23_p7d')
check('2-3 P7 bottom right: every player won 2', set(wins(labs, b).values()), {2})
star = ['A', 'C', 'E', 'B', 'D']
check('2-3 P7 bottom right: along the star A, C, E, B, D each beat the next two',
      all((star[i], star[(i + 1) % 5]) in b and (star[i], star[(i + 2) % 5]) in b for i in range(5)), True)
ring = ['A', 'B', 'C', 'D', 'E']
for r in (ring, ring[::-1]):
    assert not any((r[i], r[(i + 1) % 5]) in b and (r[i], r[(i + 2) % 5]) in b for i in range(5))
check('2-3 P7 bottom right: around the drawn pentagon (either way) nobody beats the next two', True, True)
labs, b = read_tournament('king_example', expect_complete=True)
check('Kings example (P, Q, R circle): kings', sorted(kings(labs, b)), ['P', 'Q', 'R'])
check('Return-visit launch on the P, Q, R circle: each won 1; Q gets to P by Q>R>P',
      (set(wins(labs, b).values()), ('Q', 'R') in b and ('R', 'P') in b), ({1}, True))

# ------------------------------------------------------------------ Grades 4-5
print('== Grades 4-5 ==')
want = {
    'g45_p2a': ['A C B D', 'A D C B', 'B A D C', 'C B A D', 'D C B A'],
    'g45_p2b': ['B D C A', 'C B D A', 'D C B A'],
    'g45_p2c': ['C A D B'],
    'g45_p2d': ['D A C B', 'D B A C', 'D C B A'],
}
shapes = set()
for fig, w in want.items():
    labs, b = read_tournament(fig)
    idx = {c: i for i, c in enumerate(labs)}
    shapes.add(canon(4, {(idx[x], idx[y]) for x, y in b}))
    print('     ', fig, 'wins', wins(labs, b), 'kings', kings(labs, b))
    check(f'4-5 P2 {fig}: line-ups', fmt(lineups(labs, b)), w)
check('4-5 P2: the four tournaments are the four different shapes', len(shapes), 4)

want = {'g45_p3_0': ['B-C', 'D-E'], 'g45_p3_1': ['D-E'], 'g45_p3_2': ['front', 'back']}
for fig, w in want.items():
    res = newcomer_results(fig)
    print('     ', fig, 'X vs A..E:', res)
    check(f'4-5 P3 {fig}: places', places(res), w)

want = {'g45_p5a': ['A', 'C', 'D'], 'g45_p5b': ['B', 'C', 'D', 'E'],
        'g45_p5c': ['A', 'B', 'C', 'D', 'E', 'F'], 'g45_p5d': ['A', 'D', 'F']}
for fig, w in want.items():
    labs, b = read_tournament(fig)
    print('     ', fig, 'wins', wins(labs, b))
    check(f'4-5 P5 {fig}: kings', sorted(kings(labs, b)), w)
labs, b = read_tournament('g45_p5d')
check('4-5 P5 hexagon 2: F beat only D', sorted(y for (x, y) in b if x == 'F'), ['D'])
check('4-5 P5 hexagon 2: D beat A, B, C, E', sorted(y for (x, y) in b if x == 'D'), ['A', 'B', 'C', 'E'])
check('4-5 P5 hexagon 2: only D beat A', sorted(x for (x, y) in b if y == 'A'), ['D'])
check('4-5 P5 hexagon 2: B won 3 and is not a king', (wins(labs, b)['B'], 'B' in kings(labs, b)), (3, False))
labs, b = read_tournament('g45_p5b')
check('4-5 P5 pentagon 2: A beat only E', sorted(y for (x, y) in b if x == 'A'), ['E'])
check('4-5 P5 pentagon 2: E beat B and D', sorted(y for (x, y) in b if x == 'E'), ['B', 'D'])


def win_list(fig):
    nodes, segs, heads = parse_fig(fig)
    assert not heads
    n = len(nodes)
    assert len(segs) == n * (n - 1) // 2
    return [int(nd[3]) for nd in nodes]   # file order: top, then clockwise


def realizable(scores):
    n = len(scores)
    for t in all_tournaments(n):
        m = out_masks(n, t)
        if [x.bit_count() for x in m] == list(scores):
            return True
    return False


want9 = [((1, 3, 1, 4, 1), True), ((0, 3, 4, 0, 3), False), ((2, 2, 2, 2, 2), True),
         ((4, 1, 0, 4, 1), False), ((3, 0, 3, 1, 3), True)]
for k, (lst, ok) in enumerate(want9):
    got = tuple(win_list(f'g45_p9_{k}'))
    check(f'4-5 P9 picture {k+1}: printed list (top, then clockwise)', got, lst)
    check(f'4-5 P9 picture {k+1}: possible', (realizable(got), landau_ok(got)), (ok, ok))
want10 = [((4, 1, 4, 1, 4, 1), True), ((0, 4, 1, 5, 1, 4), False), ((2, 3, 2, 3, 2, 3), True),
          ((5, 0, 2, 4, 2, 2), True)]
for k, (lst, ok) in enumerate(want10):
    got = tuple(win_list(f'g45_p10_{k}'))
    check(f'4-5 P10 picture {k+1}: printed list (top, then clockwise)', got, lst)
    check(f'4-5 P10 picture {k+1}: possible', (realizable(got), landau_ok(got)), (ok, ok))
    check(f'4-5 P10 picture {k+1}: total 15', sum(got), 15)


# The guide's constructions, in printed positions 0 = top, then clockwise.
def build_check(label, lst, beats):
    n = len(lst)
    players = list(range(n))
    assert is_complete(players, beats), label
    got = [sum((i, j) in beats for j in players) for i in players]
    check(label, tuple(got), tuple(lst))


def circle(ps):
    return {(ps[i], ps[(i + 1) % len(ps)]) for i in range(len(ps))}


# P9 #1 (1,3,1,4,1): the 4 beat everyone; the 3 beat the three 1s; the 1s go round in a circle.
b = {(3, j) for j in range(5) if j != 3} | {(1, j) for j in (0, 2, 4)} | circle([0, 2, 4])
build_check('4-5 P9 #1 construction', (1, 3, 1, 4, 1), b)
# P9 #3: everyone beats the next two clockwise.
b = {(i, (i + 1) % 5) for i in range(5)} | {(i, (i + 2) % 5) for i in range(5)}
build_check('4-5 P9 #3 construction', (2, 2, 2, 2, 2), b)
# P9 #5 (3,0,3,1,3): everyone beats the 0; the three 3s beat the 1 and go round in a circle.
b = {(j, 1) for j in (0, 2, 3, 4)} | {(j, 3) for j in (0, 2, 4)} | circle([0, 2, 4])
build_check('4-5 P9 #5 construction', (3, 0, 3, 1, 3), b)
# P10 #1 (4,1,4,1,4,1): 4s beat all 1s; 4s circle; 1s circle.
b = {(i, j) for i in (0, 2, 4) for j in (1, 3, 5)} | circle([0, 2, 4]) | circle([1, 3, 5])
build_check('4-5 P10 #1 construction', (4, 1, 4, 1, 4, 1), b)
# P10 #3 (2,3,2,3,2,3): everyone beats the next two clockwise; across, the 3 beats the 2.
b = {(i, (i + 1) % 6) for i in range(6)} | {(i, (i + 2) % 6) for i in range(6)} | {(1, 4), (3, 0), (5, 2)}
build_check('4-5 P10 #3 construction', (2, 3, 2, 3, 2, 3), b)
# P10 #4 (5,0,2,4,2,2): the 5 beats all; all beat the 0; the 4 beats the three 2s; the 2s circle.
b = {(0, j) for j in range(1, 6)} | {(j, 1) for j in (2, 3, 4, 5)} | {(3, j) for j in (2, 4, 5)} | circle([2, 4, 5])
build_check('4-5 P10 #4 construction', (5, 0, 2, 4, 2, 2), b)

# P11: every sorted list for 4 and 5 players, and the near misses.
for n, want_n in ((4, 4), (5, 9), (6, 22)):
    cands = [c for c in combinations_with_replacement(range(n), n) if sum(c) == n * (n - 1) // 2]
    ok = [c for c in cands if landau_ok(c)]
    real = sorted({tuple(sorted(x.bit_count() for x in out_masks(n, t))) for t in all_tournaments(n)})
    assert real == ok, n
    check(f'4-5 P11: possible sorted lists for {n} players', len(ok), want_n)
    if n < 6:
        print('      lists:', ok)
        print('      right total but impossible:', [c for c in cands if c not in ok])

# Landau's sufficiency, by the guide's path-reversal proof idea. For every list with the right
# total and up to 8 players: random assignment of the numbers to players, random starting
# tournament (the first run starts from a ranking), random search order. A passing list must
# always be reached; a failing list must get stuck, with the reached group failing the test.
import random
rng = random.Random(1953)
nlists = nfail = runs = 0
for n in range(1, 9):
    for c in combinations_with_replacement(range(n), n):
        if sum(c) != n * (n - 1) // 2:
            continue
        ok = landau_ok(c)
        nlists += ok
        nfail += not ok
        for trial in range(6):
            tgt = list(c)
            rng.shuffle(tgt)
            if trial == 0:
                start = {(i, j) for i in range(n) for j in range(i)}       # a ranking
            else:
                start = {(a, b) if rng.random() < .5 else (b, a) for a, b in combinations(range(n), 2)}
            res, out = landau_paths(tgt, start, rng)
            runs += 1
            if ok:
                assert res == 'done', (c, tgt)
                assert [sum((i, j) in out for j in range(n)) for i in range(n)] == tgt
                assert is_complete(list(range(n)), out)
            else:
                assert res == 'stuck', (c, tgt)
check('Landau path idea reaches every passing list, 1-8 players (lists)', nlists, 1 + 1 + 2 + 4 + 9 + 22 + 59 + 167)
check('Landau path idea gets stuck on a failing group for every failing list with the right total',
      nfail > 0, True)
print(f'      ({runs} random runs, {nfail} failing lists)')

# The reviewer's example: the draft's one-or-two-arrow move gets stuck on 1,1,1,4,4,4 from here,
# while the path P2 -> P0 -> P5 -> P3 finishes it.
tgt = [1, 1, 1, 4, 4, 4]
st = {(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3),
      (5, 1), (5, 2), (5, 3), (5, 4), (0, 5)}
assert is_complete(list(range(6)), st)
w = [sum((i, j) in st for j in range(6)) for i in range(6)]
check('stuck example: current wins', w, [1, 1, 2, 3, 4, 4])
rich = [i for i in range(6) if w[i] > tgt[i]]
poor = [i for i in range(6) if w[i] < tgt[i]]
one_or_two = any((p, q) in st or any((p, r) in st and (r, q) in st for r in range(6))
                 for p in rich for q in poor)
check('stuck example: no one- or two-arrow move from too many to too few', (rich, poor, one_or_two),
      ([2], [3], False))
path = [2, 0, 5, 3]
assert all((a, b) in st for a, b in zip(path, path[1:]))
st2 = (st - set(zip(path, path[1:]))) | {(b, a) for a, b in zip(path, path[1:])}
check('stuck example: reversing P2 > P0 > P5 > P3 reaches the list',
      [sum((i, j) in st2 for j in range(6)) for i in range(6)], tgt)

# ------------------------------------------------------------------ general facts
print('== General facts by enumeration ==')
for n in range(1, 7):
    lucounts, kcounts = set(), set()
    for t in all_tournaments(n):
        m = out_masks(n, t)
        c, firsts = count_paths(n, m)
        km = king_mask(n, m)
        w = [x.bit_count() for x in m]
        assert c % 2 == 1                                  # Redei: odd, so at least one
        transitive = sorted(w) == list(range(n))
        assert (c == 1) == transitive                      # unique exactly for a ranking
        top = max(w)
        assert all(km >> i & 1 for i in range(n) if w[i] == top)   # Landau: top scorer is king
        unbeaten = [i for i in range(n) if w[i] == n - 1]
        if unbeaten:
            assert km == 1 << unbeaten[0]                  # an unbeaten player is the only king
        elif n > 1:
            assert km.bit_count() >= 3                     # otherwise at least three kings
        for x in range(n):                                 # can start a line-up iff reaches all
            assert bool(firsts >> x & 1) == (reach_mask(n, m, x) == (1 << n) - 1)
        # Camion: the players who reach everyone go round in one circle (when there are 3 or
        # more of them), and each of them beat every player outside that group.
        topc = [x for x in range(n) if reach_mask(n, m, x) == (1 << n) - 1]
        assert len(topc) != 2
        assert all(m[x] >> y & 1 for x in topc for y in range(n) if y not in topc)
        if len(topc) >= 3:
            assert any(all(m[p[i]] >> p[(i + 1) % len(p)] & 1 for i in range(len(p)))
                       for p in ((topc[0],) + q for q in permutations(topc[1:])))
        lucounts.add(c)
        kcounts.add(km.bit_count())
    print(f'  n={n}: line-up counts {sorted(lucounts)}; king counts {sorted(kcounts)}')
    if n == 4:
        check('n=4 line-up counts', sorted(lucounts), [1, 3, 5])
        check('n=4 king counts', sorted(kcounts), [1, 3])
    if n == 5:
        check('n=5 king counts', sorted(kcounts), [1, 3, 4, 5])
    if n == 6:
        check('n=6 king counts', sorted(kcounts), [1, 3, 4, 5, 6])
check('odd line-up counts, unique iff ranking, top scorer is king, two kings never, '
      'first player iff reaches all, Camion circle (n <= 6)', True, True)

classes = {}
for t in all_tournaments(4):
    w = tuple(sorted(x.bit_count() for x in out_masks(4, t)))
    classes.setdefault(w, set()).add(canon(4, t))
check('n=4: each possible win list has exactly one shape', {k: len(v) for k, v in classes.items()},
      {(0, 1, 2, 3): 1, (0, 2, 2, 2): 1, (1, 1, 1, 3): 1, (1, 1, 2, 2): 1})

# The guide's five-player king examples (letters A-E = 0-4).
ex = {
    1: {(i, j) for i in range(5) for j in range(i + 1, 5)},                   # A beat all, B beat C, D, E, ...
    3: circle([0, 1, 2]) | {(i, j) for i in (0, 1, 2) for j in (3, 4)} | {(3, 4)},
    5: {(i, (i + 1) % 5) for i in range(5)} | {(i, (i + 2) % 5) for i in range(5)},
}
for k, bb in ex.items():
    assert is_complete(list(range(5)), bb)
    m = out_masks(5, bb)
    check(f'five-player example with {k} king(s)', king_mask(5, m).bit_count(), k)
# Four kings among five players: the guide points to Problem 5's second pentagon (checked above).
lists4 = {tuple(sorted(x.bit_count() for x in out_masks(5, t))) for t in all_tournaments(5)
          if king_mask(5, out_masks(5, t)).bit_count() == 4}
check('five players with four kings: the only win list', sorted(lists4), [(1, 2, 2, 2, 3)])

# The launch example is three volunteers (people, not animals or letters): a ranking with one
# legal row and one illegal row shown.
launch = {('Kai', 'Lu'), ('Lu', 'Mo'), ('Kai', 'Mo')}
L3 = ['Kai', 'Lu', 'Mo']
check('launch: legal rows', fmt(lineups(L3, launch)), ['Kai Lu Mo'])
check('launch: players are not page labels', set(L3) & (ANIMALS | set('ABCDEFPQRX')), set())


# ------------------------------------------------------------------ the materials file
# The guide cites materials.pdf by page number and object name, with sizes and counts. Read
# the page titles from the PDF and the shapes from its source (positions in mm).
print('== Materials file cited in the guide ==')
import subprocess
info = subprocess.run(['pdfinfo', f'{DRAFT}/materials.pdf'], capture_output=True, text=True).stdout
check('materials.pdf: pages', int(re.search(r'Pages:\s+(\d+)', info)[1]), 5)
check('materials.pdf: landscape Letter', re.search(r'Page size:\s+([\d. x]+) pts', info)[1].strip(), '792 x 612')
titles = {}
for pg in range(1, 6):
    txt = subprocess.run(['pdftotext', '-f', str(pg), '-l', str(pg), f'{DRAFT}/materials.pdf', '-'],
                         capture_output=True, text=True).stdout
    for t in ('Animal cards', 'Arrow cards', 'Line-up strip (K–1)', 'K–1 Problem 2: frog', 'K–1 Problem 2: pig'):
        if t in txt:
            titles[pg] = t
check('materials.pdf: page titles', titles, {1: 'Animal cards', 2: 'Arrow cards', 3: 'Line-up strip (K–1)',
                                             4: 'K–1 Problem 2: frog', 5: 'K–1 Problem 2: pig'})
mtex = open(f'{DRAFT}/materials-src/materials.tex').read().split(r'\newpage')[:5]


def rects(page_src, style_pat):
    out = []
    for m in re.finditer(rf'\\draw\[{style_pat}\] {PT} rectangle {PT};', page_src):
        x0, y0, x1, y1 = map(float, m.groups())
        out.append((round(abs(x1 - x0), 2), round(abs(y1 - y0), 2)))
    return out


def pics(page_src):
    return re.findall(r'\\pic\[[^\]]*\] at \([^)]*\) \{(\w+)\};', page_src)


def lanes(page_src):
    return len(re.findall(r'\\draw\[gray!70, dashed[^\]]*\] \([^)]*\)( -- \([^)]*\)){3} -- cycle;', page_src))


p1 = rects(mtex[0], r'line width=0.6pt')
check('materials p1: animal cards, 40 x 40 mm', (p1.count((40.0, 40.0)), set(p1)), (18, {(40.0, 40.0)}))
check('materials p1: three sets of the six animals', sorted(pics(mtex[0])),
      sorted(['cat', 'dog', 'bear', 'rabbit', 'frog', 'pig'] * 3))
p2 = rects(mtex[1], r'line width=0.6pt')
check('materials p2: arrow cards, 75 x 20 mm', (p2.count((75.0, 20.0)), set(p2)), (18, {(75.0, 20.0)}))
p3 = rects(mtex[2], r'line width=1.0pt, rounded corners=2pt')
check('materials p3: line-up strip boxes, 44 mm', (len(p3), set(p3)), (6, {(44.0, 44.0)}))
for k, (animal, nbox) in enumerate((('frog', 4), ('pig', 5))):
    pg = mtex[3 + k]
    boxes = rects(pg, r'line width=1.0pt, rounded corners=2pt')
    check(f'materials p{4 + k}: {animal} mat boxes and lanes, printed newcomer',
          (len(boxes), set(boxes), lanes(pg), pics(pg)), (nbox, {(44.0, 44.0)}, nbox, [animal]))
# Counts the guide prints.
k1_cards = 6 + 4 + 5            # big board lanes, frog mat lanes, pig mat lanes
check('K-1 pair: arrow cards in use at once (board 6, frog 4, pig 5) and spare on one sheet',
      (k1_cards, 18 - k1_cards), (15, 3))
check('arrow card fits the big board side lane (108 mm) and an animal card fits a 44 mm box',
      (75 < 108, 40 < 44), (True, True))
check('older pairs: 6 arrow cards for four players, 10 for five, 15 for six',
      [n * (n - 1) // 2 for n in (4, 5, 6)], [6, 10, 15])
# Example meeting: three K-1 pairs and two older tables of three pairs.
sheets = {'animal': 1 + 2, 'arrow': 3, 'strip': 3, 'frog mat': 3, 'pig mat': 3}
cut_minutes = 5 * (sheets['animal'] + sheets['arrow']) + 2 * sheets['strip']
check('example meeting: sheets to print and minutes of cutting (5 per card sheet, 2 per strip)',
      (sheets, cut_minutes), ({'animal': 3, 'arrow': 3, 'strip': 3, 'frog mat': 3, 'pig mat': 3}, 36))

# ------------------------------------------------------------------ guide citations vs the PDFs
print('== Problem and page numbers cited in the guide ==')
DRAFTS = DRAFT
where = {}
for band, pdf in (('K', 'k-1'), ('23', 'grades-2-3'), ('45', 'grades-4-5')):
    info = subprocess.run(['pdfinfo', f'{DRAFTS}/{pdf}.pdf'], capture_output=True, text=True).stdout
    pages = int(re.search(r'Pages:\s+(\d+)', info)[1])
    for pg in range(1, pages + 1):
        txt = subprocess.run(['pdftotext', '-f', str(pg), '-l', str(pg), f'{DRAFTS}/{pdf}.pdf', '-'],
                             capture_output=True, text=True).stdout
        for m in re.finditer(r'Problem (\d+):', txt):
            where[(band, int(m[1]))] = pg
    print(f'  {pdf}: {pages} pages, problems', sorted(n for (b, n) in where if b == band))
tex = open('facilitator.tex').read()
cited = {}
for band, start, end in (('K', r'\head{Grades K--1', r'\head{Grades 2--3'),
                         ('23', r'\head{Grades 2--3', r'\head{Grades 4--5'),
                         ('45', r'\head{Grades 4--5', r'\head{Sources')):
    part = tex[tex.index(start):tex.index(end)]
    for m in re.finditer(r'\\sub\{Problem (\d+), page (\d+)', part):
        cited[(band, int(m[1]))] = int(m[2])
check('every problem has a guide entry', sorted(cited), sorted(where))
check('every cited page matches the PDF', {k: v for k, v in cited.items() if where[k] != v}, {})
print(f'\nAll {len(OK)} checks passed.')
