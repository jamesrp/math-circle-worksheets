"""Independent enumeration of the Week 47 bonus pages and bonus guide.

Run pdf_extract.py first: graphs (squares, joining edges, letters, clue
values), the start/finish rows, the marker board and the budget list are read
from pdf_geometry.json (taken from the delivered PDF).

Writes check_bonus.out.
"""
import json
import os
import re
import sys
from collections import Counter, deque
from itertools import combinations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, Log, completions, legal, page_text, path_edges, ring_edges, shortest_moves)  # noqa: E402

log = Log('Week 47 bonus: independent enumeration')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))['bonus']
GUIDE = re.sub(r'\s+', ' ', page_text(PDFS['bonus-guide']))


def tuples_in(text):
    return [tuple(int(x) for x in m.split(',')) for m in re.findall(r'\((\d+(?:,\d+)+)\)', text)]


def components(page):
    """Split a page's nodes into connected drawn graphs, each as (letters, edges, clues)."""
    nodes, edges = page['nodes'], page['edges']
    adj = {i: set() for i in range(len(nodes))}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, comps = set(), []
    for s in range(len(nodes)):
        if s in seen:
            continue
        comp, q = [], [s]
        seen.add(s)
        while q:
            v = q.pop()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        comp.sort(key=lambda k: nodes[k]['letter'])
        idx = {k: i for i, k in enumerate(comp)}
        letters = [nodes[k]['letter'] for k in comp]
        e = sorted({tuple(sorted((idx[a], idx[b]))) for a, b in edges if a in idx})
        clues = {idx[k]: int(nodes[k]['value']) for k in comp if nodes[k]['clue']}
        comps.append((letters, e, clues, min(nodes[k]['cx'] for k in comp), min(nodes[k]['cy'] for k in comp)))
    comps.sort(key=lambda c: (round(c[4], -1), c[3]))
    return comps


def dist(n, edges, s):
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    d = {s: 0}
    q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in d:
                d[w] = d[v] + 1
                q.append(w)
    return d


# ------------------------------------------------------------------ Problem 1
log.section('Bonus Problem 1: row versus rings')
comps = components(G[0])
names = ['row', 'left ring', 'right ring']
P1 = {}
for name, (letters, e, cl, _, _) in zip(names, comps):
    n = len(letters)
    sols = completions(n, e, cl)
    P1[name] = (letters, e, cl, sols)
    log.note('%s: vertices %s, edges %s, clues %s -> %d completions %s' % (
        name, letters, ['%s%s' % (letters[a], letters[b]) for a, b in e], {letters[k]: v for k, v in cl.items()}, len(sols), sols))
letters, e, cl, sols = P1['row']
log.check(letters == list('ABCDE') and e == path_edges(5) and cl == {0: 0, 3: 3}, 'row: A-B-C-D-E with A=0, D=3')
log.check(len(sols) == 3 and {s[1] for s in sols} == {1} and {s[2] for s in sols} == {2} and sorted(s[4] for s in sols) == [2, 3, 4],
          'row: B=1, C=2 forced; E in {2,3,4}; exactly three completions')
letters, e, cl, sols = P1['left ring']
log.check(sorted(e) == sorted(tuple(sorted(x)) for x in ring_edges(5)) and cl == {0: 0, 3: 3}, 'left ring: 5-cycle A-B-C-D-E-A with A=0, D=3')
log.check(sols == [] and dist(5, e, 0)[3] == 2, 'left ring: impossible; A and D are 2 steps apart through E')
letters, e, cl, sols = P1['right ring']
log.check(sorted(e) == sorted(tuple(sorted(x)) for x in ring_edges(5)) and cl == {0: 0, 3: 2}, 'right ring: 5-cycle with A=0, D=2')
maxB, maxC = max(s[1] for s in sols), max(s[2] for s in sols)
log.check(any(s[1] == maxB and s[2] == maxC for s in sols), 'right ring: B and C reach their maxima (%d, %d) at the same time' % (maxB, maxC))
g = GUIDE[GUIDE.index('1. The open row'):GUIDE.index('2. Eight moves')]
log.check(sorted(tuples_in(g)) == sorted(sols) and len(sols) == 3, 'guide P1: exactly the three ring completions %s' % tuples_in(g))
log.check('(0,1,2,2,1). The last simultaneously maximizes B and C' in g, 'guide P1: (0,1,2,2,1) maximises B and C together')

# ------------------------------------------------------------------ Problem 2
log.section('Bonus Problem 2: shortest legal change')
rows = G[1]['start_finish']
start = tuple(int(v) for v in rows[0]['values'])
target = tuple(int(v) for v in rows[1]['values'])
fixed = {i for i, f in enumerate(rows[0]['fixed']) if f}
log.check(rows[0]['title'] == 'Start' and rows[1]['title'] == 'Finish' and fixed == {0, 6} and rows[1]['fixed'] == rows[0]['fixed'],
          'rows: Start %s, Finish %s, fixed A and G' % (start, target))
log.check(start[0] == target[0] and start[6] == target[6] and legal(start, path_edges(7)) and legal(target, path_edges(7)), 'start and finish are legal with the same clues')
board = G[1]['board']
log.check(board['columns'] == 7 and board['levels'] == 5 and board['col_labels'] == list('ABCDEFG')
          and sorted(board['dots']) == [[0, 1, 0.0], [6, 1, 0.0]], 'marker board: columns A-G, levels 0-4, clue dots at A=1 and G=1')
l1 = sum(abs(a - b) for a, b in zip(start, target))
for cap in (4, 12):
    d, path = shortest_moves(start, target, 7, path_edges(7), fixed, cap)
    log.check(d == l1 == 8, 'BFS shortest = %d moves (sum of changes %d), heights capped at %d' % (d, l1, cap))
space = completions(7, path_edges(7), {0: 1, 6: 1})
log.check(len(space) == 120 and max(max(s) for s in space) == 4, 'there are %d legal rows with A=G=1 (guide: 120); tallest height %d' % (len(space), max(max(s) for s in space)))
g = GUIDE[GUIDE.index('2. Eight moves'):GUIDE.index('3. Least ring')]
route = tuples_in(g)
ok = route[0] == start and route[-1] == target and len(route) == 9 and all(legal(v, path_edges(7)) for v in route) and \
    all(sum(abs(x - y) for x, y in zip(a, b)) == 1 and a[0] == b[0] and a[6] == b[6] for a, b in zip(route, route[1:]))
log.check(ok, 'guide P2: printed 8-move route is legal step by step')
log.check(max(max(v) for v in route) <= 4, 'guide P2: the printed route fits on the 0-4 board')
# the general question: every pair of legal rows with the same clues
S = set(space)
worst = 0
for s in space:
    seen = {s: 0}
    q = deque([s])
    while q:
        v = q.popleft()
        for i in range(1, 6):
            for dl in (-1, 1):
                w = list(v)
                w[i] += dl
                w = tuple(w)
                if w in S and w not in seen:
                    seen[w] = seen[v] + 1
                    q.append(w)
    for t in space:
        worst = max(worst, seen[t] - sum(abs(a - b) for a, b in zip(s, t)))
log.check(worst == 0, 'all 120 x 120 pairs with A=G=1: shortest legal route always equals the sum of height changes')

# ------------------------------------------------------------------ overview theorems on small graphs
log.section('Bonus overview: theorems on small graphs (exhaustive)')
graphs = {
    'path5': (5, path_edges(5)), 'ring5': (5, ring_edges(5)), 'ring6': (6, ring_edges(6)),
    'star(K1,4)': (5, [(0, 1), (0, 2), (0, 3), (0, 4)]), 'branched': (6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5)]),
    'ring5+chord': (5, ring_edges(5) + [(0, 2)]), 'grid2x3': (6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]),
}
viol = Counter()
cases = 0
for gname, (n, e) in graphs.items():
    D = [dist(n, e, s) for s in range(n)]
    for k in (1, 2):
        for sites in combinations(range(n), k):
            for hs in product(range(4), repeat=k):
                cl = dict(zip(sites, hs))
                cases += 1
                sols = completions(n, e, cl, cap=3 + n)
                pair = all(abs(cl[a] - cl[b]) <= D[a][b] for a, b in combinations(sites, 2))
                if pair != bool(sols):
                    viol['feasibility'] += 1
                if not sols:
                    continue
                L = tuple(max([0] + [cl[c] - D[v][c] for c in cl]) for v in range(n))
                U = tuple(min(cl[c] + D[v][c] for c in cl) for v in range(n))
                if L not in sols or U not in sols:
                    viol['envelopes'] += 1
                if set(map(sum, sols)) != set(range(sum(L), sum(U) + 1)):
                    viol['totals'] += 1
                if len(sols) <= 60:
                    SS = set(sols)
                    for s in sols:
                        seen = {s: 0}
                        q = deque([s])
                        while q:
                            v = q.popleft()
                            for i in range(n):
                                if i in cl:
                                    continue
                                for dl in (-1, 1):
                                    w = list(v)
                                    w[i] += dl
                                    w = tuple(w)
                                    if w in SS and w not in seen:
                                        seen[w] = seen[v] + 1
                                        q.append(w)
                        for t in sols:
                            if t not in seen or seen[t] != sum(abs(a - b) for a, b in zip(s, t)):
                                viol['moves'] += 1
log.check(not viol, '%d clue sets on %s: extension <=> pairwise distance bound; L,U legal; every total from sum L to sum U occurs; shortest legal route = sum of changes %s' % (
    cases, list(graphs), dict(viol)))

# ------------------------------------------------------------------ Problem 3
log.section('Bonus Problem 3: cube budgets on the six-ring')
letters, e, cl, _, _ = components(G[2])[0]
log.check(letters == list('ABCDEF') and sorted(e) == sorted(tuple(sorted(x)) for x in ring_edges(6)) and cl == {0: 1, 3: 1},
          'ring: A-B-C-D-E-F-A with gray A=1 and D=1')
sols = completions(6, e, cl)
tot = Counter(map(sum, sols))
budgets = [int(b) for b in G[2]['budgets']]
log.note('ring: %d completions; totals by budget %s' % (len(sols), dict(sorted(tot.items()))))
log.check(budgets == [2, 5, 8, 10, 11] and G[2]['budget_slots'] == 5, 'page lists budgets 2, 5, 8, 10, 11 with five slots')
log.check([b for b in budgets if tot[b]] == [2, 5, 8, 10], 'budgets 2, 5, 8, 10 work and 11 does not (gray towers counted)')
log.check(min(tot) == 2 and max(tot) == 10 and sorted(tot) == list(range(2, 11)), 'least 2, greatest 10, every total between occurs')
white = Counter(sum(s) - 2 for s in sols)
log.note('if a child counts only the white towers: totals %s; listed budgets that work: %s' % (sorted(white), [b for b in budgets if white[b]]))
g = GUIDE[GUIDE.index('3. Least ring'):GUIDE.index('Sources, distinction')]
tp = tuples_in(g)
log.check(tp[0] == (1, 0, 0, 1, 0, 0) and tp[1] == (1, 2, 2, 1, 2, 2) and sum(tp[0]) == 2 and sum(tp[1]) == 10, 'guide P3: least and greatest rings')
log.check(tp[2] in sols and sum(tp[2]) == 5 and tp[3] in sols and sum(tp[3]) == 8, 'guide P3: witnesses %s (5) and %s (8) legal' % (tp[2], tp[3]))
counts = [int(x) for x in re.search(r'counts by budget are ([\d,]+)', g).group(1).split(',')]
log.check(counts == [tot[t] for t in range(2, 11)] and '49 rings' in g and len(sols) == 49, 'guide P3: counts %s and 49 rings' % counts)

# ------------------------------------------------------------------ guide preparation arithmetic
log.section('Bonus guide: preparation numbers')
sq = sorted({nd['side_mm'] for p in G for nd in p['nodes']})
log.check(sq == [21.87, 23.99], 'squares are %s mm (guide: 21.9 or 24.0)' % sq)
log.check(board['dx_mm'] == [24.34] and board['dy_mm'] == [20.11], 'marker board pitch %s x %s mm (guide: 24.3 and 20.1)' % (board['dx_mm'], board['dy_mm']))
log.check(5 * 12 == 60 and 5 * 7 == 35 and 5 * 2 == 10 and len('KK11') + len('3333') + len('445') == 11, 'five kits: 60 cubes, 35 markers, 10 clue markers; KK11/3333/445 = 11 children')
log.check(12 >= 11, 'twelve cubes per pair are enough to attempt the impossible budget 11')
for phrase in ('twelve stacking cubes', 'sixty cubes', 'thirty-five movable markers', 'ten clue markers', '21.9 mm or 24.0 mm', '24.3 mm and level spacing 20.1 mm', '120 permitted seven-site rows', '49 budget rings'):
    log.check(phrase in GUIDE, 'guide prints "%s"' % phrase)

log.dump(os.path.join(HERE, 'check_bonus.out'))
