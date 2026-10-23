#!/usr/bin/env python3
"""Independent mathematical check of Week 99 (Moving piles).

Written for the review; does not import or run the package's own
check_math.py.  The printed data below were read off the rendered student
pages; check_diagrams.py confirms them against the PDF vectors and the TeX.

Method: every least-work value is computed from first principles by
breadth-first search over pile states (a state is the tuple of counts per
bin/node; one move takes one counter across one road and costs 1).  The
gap formula, sorted matching and brute-force assignment are computed
separately and compared with the BFS value.

Covers:
  2-3 : P1 (two best records), P2, P3 (all tie-broken greedy runs), P4
        (all starts with work 4 and 7), P5 (stars and the work-6 invention),
        P6 (every 4-counter target; the guide's construction).
  4-5 : P1, P2, P3, P4 (cards, 28 distances, completeness), P5 (stars and
        the leaf formula for every start/target up to 5 counters), P6 (all
        2,000,376 triples of 4-counter arrangements on bins 0-5).
  guide: overview theorems on the line (all equal-mass pairs up to 5
        counters on 6 bins), trees (several trees), the ring example, the
        solutions table, every numeric claim.
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from collections import deque
from itertools import combinations_with_replacement, permutations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
OUT, FAILS = [], []


def say(s=''):
    OUT.append(s)


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        say('  FAIL: ' + msg)
    return cond


# ---------------------------------------------------------------- printed data
# Position strings: one bin number per counter (the guide's convention).
LINE_PAIRS = {
    ('2-3', 1, 'P1'): [('00', '24'), ('03', '12')],
    ('2-3', 2, 'P2'): [('0005', '1234'), ('1144', '0225'), ('2222', '0134')],
    ('2-3', 3, 'P3'): [('03', '25'), ('04', '25')],
    ('4-5', 1, 'P1'): [('0005', '1234'), ('1144', '0225')],
    ('4-5', 2, 'P2'): [('0055', '2233'), ('1114', '0235'), ('0235', '1144')],
    ('4-5', 3, 'P3'): [('03', '25'), ('04', '35')],
}
CARDS = ['0044', '0134', '0224', '0233', '1124', '1133', '1223', '2222']  # 4-5 P4, reading order
STAR_PAIRS = {
    ('2-3', 5): [({'A': 2, 'O': 0, 'B': 0, 'C': 1}, {'A': 0, 'O': 1, 'B': 2, 'C': 0}),
                 ({'A': 2, 'O': 0, 'B': 1, 'C': 0}, {'A': 1, 'O': 0, 'B': 0, 'C': 2})],
    ('4-5', 5): [({'A': 2, 'O': 0, 'B': 0, 'C': 1}, {'A': 0, 'O': 1, 'B': 2, 'C': 0}),
                 ({'A': 3, 'O': 0, 'B': 1, 'C': 0}, {'A': 1, 'O': 1, 'B': 0, 'C': 2})],
}
NBINS = 6

# ---------------------------------------------------------------- graphs


def line_graph(n):
    return {i: [j for j in (i - 1, i + 1) if 0 <= j < n] for i in range(n)}


def ring_graph(n):
    return {i: [(i - 1) % n, (i + 1) % n] for i in range(n)}


STAR = {'O': ['A', 'B', 'C'], 'A': ['O'], 'B': ['O'], 'C': ['O']}
STAR_NODES = ['A', 'O', 'B', 'C']


def to_counts(pos, n=NBINS):
    c = [0] * n
    for ch in pos:
        c[int(ch)] += 1
    return tuple(c)


def to_pos(counts):
    return ''.join(str(i) * k for i, k in enumerate(counts))


def bfs(graph, nodes, start):
    """Distances and numbers of shortest move records from a start state."""
    idx = {v: i for i, v in enumerate(nodes)}
    dist, ways = {start: 0}, {start: 1}
    q = deque([start])
    while q:
        s = q.popleft()
        for v in nodes:
            if s[idx[v]] == 0:
                continue
            for w in graph[v]:
                t = list(s)
                t[idx[v]] -= 1
                t[idx[w]] += 1
                t = tuple(t)
                if t not in dist:
                    dist[t] = dist[s] + 1
                    ways[t] = ways[s]
                    q.append(t)
                elif dist[t] == dist[s] + 1:
                    ways[t] += ways[s]
    return dist, ways


_cache = {}


def line_bfs(start, n=NBINS):
    key = ('line', n, start)
    if key not in _cache:
        _cache[key] = bfs(line_graph(n), list(range(n)), start)
    return _cache[key]


def work_line(a, b, n=NBINS):
    return line_bfs(to_counts(a, n), n)[0][to_counts(b, n)]


def records_line(a, b, n=NBINS):
    return line_bfs(to_counts(a, n), n)[1][to_counts(b, n)]


def gap_row(a, b, n=NBINS):
    A, B = to_counts(a, n), to_counts(b, n)
    s, row = 0, []
    for i in range(n - 1):
        s += A[i] - B[i]
        row.append(s)
    return row


def sorted_match(a, b):
    return sum(abs(int(x) - int(y)) for x, y in zip(sorted(a), sorted(b)))


def best_assignment(a, b):
    xs, ys = [int(c) for c in a], [int(c) for c in b]
    return min(sum(abs(x - y) for x, y in zip(xs, p)) for p in permutations(ys))


def greedy_runs(a, b):
    """Every outcome of 'make the shortest remaining delivery', any tie-break.
    Returns list of (total, deliveries)."""
    res = []

    def rec(cs, ts, total, hist):
        if not cs:
            res.append((total, hist))
            return
        opts = [(abs(c - t), i, j) for i, c in enumerate(cs) for j, t in enumerate(ts)]
        m = min(o[0] for o in opts)
        seen = set()
        for d, i, j in opts:
            if d != m:
                continue
            key = (cs[i], ts[j])
            if key in seen:
                continue
            seen.add(key)
            rec(cs[:i] + cs[i + 1:], ts[:j] + ts[j + 1:], total + d, hist + [f'{cs[i]}->{ts[j]}'])
    rec([int(c) for c in a], [int(c) for c in b], 0, [])
    return res


def star_state(d):
    return tuple(d[v] for v in STAR_NODES)


def star_work(a, b):
    return bfs(STAR, STAR_NODES, star_state(a))[0][star_state(b)]


def leaf_formula(a, b):
    return sum(abs(a[L] - b[L]) for L in 'ABC')


def multisets(n_counters, nbins):
    return [''.join(map(str, m)) for m in combinations_with_replacement(range(nbins), n_counters)]


# ---------------------------------------------------------------- checks

def main():
    say('Week 99 independent math check')
    say()

    # ---- shared rule diagram and the guide's launch example
    say('== Rule diagram and launch example')
    w = work_line('0', '2', 3)
    say(f'   rule diagram: one counter bin 0 -> bin 2 on three bins: work {w} (two pictured steps of cost 1)')
    check(w == 2, 'rule diagram work')
    # guide launch: bins A-D start 1,0,1,0 target 0,1,0,1
    w = bfs(line_graph(4), list(range(4)), (1, 0, 1, 0))[0][(0, 1, 0, 1)]
    say(f'   guide launch A-D 1010 -> 0101: work {w} (guide: two counter-steps)')
    check(w == 2, 'guide launch')
    say()

    # ---- line pairs: BFS, gap formula, sorted matching, assignment
    say('== Line pairs: BFS least work, gap row, sorted matching, best assignment, shortest records')
    guide_table = {  # guide p3 table: (start, target): (gap row, work)
        ('00', '24'): ([2, 2, 1, 1, 0], 6), ('03', '12'): ([1, 0, -1, 0, 0], 2),
        ('0005', '1234'): ([3, 2, 1, 0, -1], 7), ('1144', '0225'): ([-1, 1, -1, -1, 1], 5),
        ('2222', '0134'): ([-1, -2, 2, 1, 0], 6), ('0055', '2233'): ([2, 2, 0, -2, -2], 8),
        ('1114', '0235'): ([-1, 2, 1, 0, 1], 5), ('0235', '1144'): ([1, -1, 0, 1, -1], 4),
    }
    for (band, page, prob), pairs in LINE_PAIRS.items():
        for k, (a, b) in enumerate(pairs, 1):
            W_ = work_line(a, b)
            g = gap_row(a, b)
            sm, ba = sorted_match(a, b), best_assignment(a, b)
            rec = records_line(a, b)
            nopt = sum(1 for p in set(permutations(b)) if sum(abs(int(x) - int(y)) for x, y in zip(a, p)) == W_)
            say(f'   {band} p{page} {prob} pair {k}: {a} -> {b}: BFS {W_}, sum|S|={sum(map(abs, g))} gaps {g}, '
                f'sorted {sm}, assignment {ba}; optimal target-assignments {nopt}; shortest move records {rec}')
            check(W_ == sum(map(abs, g)) == sm == ba, f'{band} {prob} {a}->{b} methods disagree')
            if (a, b) in guide_table:
                gr, gw = guide_table[(a, b)]
                check(g == gr and W_ == gw, f'guide table row {a}->{b}: guide {gr},{gw}; computed {g},{W_}')
            if prob == 'P1':
                check(rec >= 2, f'{band} P1 {a}->{b}: fewer than two best records')
    say('   guide table rows: all 8 checked against BFS and the computed gap rows')
    # guide p3 'Some different matchings also tie': distinct optimal matchings once
    # identical counters are identified (a matching = multiset of (from, to) pairs)
    for (band, page, prob), pairs in LINE_PAIRS.items():
        if prob not in ('P1', 'P2'):
            continue
        for k, (a, b) in enumerate(pairs, 1):
            W_ = work_line(a, b)
            ms = {tuple(sorted(zip(a, p))) for p in permutations(b)
                  if sum(abs(int(x) - int(y)) for x, y in zip(a, p)) == W_}
            say(f'   {band} {prob} pair {k}: {a} -> {b}: distinct optimal matchings (identical counters identified): {len(ms)}'
                + (f' {sorted(ms)}' if len(ms) > 1 else f' {sorted(ms)[0]}'))
            if prob == 'P1':
                check(len(ms) == 1, f'{band} P1 {a}->{b}: optimal matching not unique')
    # a general example where two matchings do tie
    say(f'   general tie example 01 -> 12: 0->1,1->2 costs {abs(0-1)+abs(1-2)}; 0->2,1->1 costs {abs(0-2)+abs(1-1)}')
    say()

    # ---- Problem 3 greedy
    say('== Problem 3 (both bands): every tie-broken run of shortest-remaining-delivery')
    for band in ('2-3', '4-5'):
        for k, (a, b) in enumerate(LINE_PAIRS[(band, 3, 'P3')], 1):
            runs = greedy_runs(a, b)
            opt = work_line(a, b)
            outs = sorted({t for t, _ in runs})
            say(f'   {band} pair {k}: {a} -> {b}: optimum {opt}; greedy runs ' +
                '; '.join(f'{" , ".join(h)} = {t}' for t, h in runs) + f'; outcomes {outs}')
    r = {t for t, _ in greedy_runs('03', '25')}
    check(r == {6} and work_line('03', '25') == 4, 'P3 pair 1: greedy 6 vs optimum 4')
    r = {t for t, _ in greedy_runs('04', '25')}
    check(r == {3} and work_line('04', '25') == 3, '2-3 P3 pair 2: greedy optimal 3')
    r = {t for t, _ in greedy_runs('04', '35')}
    check(r == {4, 6} and work_line('04', '35') == 4, '4-5 P3 pair 2: ties give 4 or 6')
    # guide: other pairing in 2-3 pair 2 costs 7
    check(abs(4 - 2) + abs(0 - 5) == 7, 'guide 2-3 P3 other pairing 7')
    say()

    # ---- 2-3 Problem 4
    say('== Grades 2-3 Problem 4: target four counters at bin 2')
    tgt = '2222'
    allstarts = multisets(4, NBINS)
    by = {}
    for s in allstarts:
        by.setdefault(work_line(s, tgt), []).append(s)
    for v in sorted(by):
        say(f'   least work {v:2d}: {len(by[v]):3d} starts' + (f'  {by[v]}' if v in (4, 7) else ''))
    check(len(by[4]) == 16 and len(by[7]) == 19, 'guide counts 16 and 19')
    for s in ('0022', '1111', '0224'):
        check(work_line(s, tgt) == 4, f'guide work-4 example {s}')
    for s in ('0003', '0014', '0115'):
        check(work_line(s, tgt) == 7, f'guide work-7 example {s}')
    check(all(work_line(s, tgt) == sum(abs(int(c) - 2) for c in s) for s in allstarts), 'distance-to-2 formula')
    say('   guide examples 0022, 1111, 0224 (work 4) and 0003, 0014, 0115 (work 7) confirmed; '
        'work = sum of distances to bin 2 for all 126 starts')
    say()

    # ---- Stars (2-3 P5, 4-5 P5)
    say('== Problem 5 stars (both bands)')
    for (band, page), pairs in STAR_PAIRS.items():
        for k, (a, b) in enumerate(pairs, 1):
            W_ = star_work(a, b)
            lf = leaf_formula(a, b)
            say(f'   {band} pair {k}: start {a} target {b}: BFS {W_}; leaf imbalances '
                f'{[abs(a[L]-b[L]) for L in "ABC"]} sum {lf}')
            check(W_ == lf, f'{band} star pair {k}')
    check(star_work(*STAR_PAIRS[('2-3', 5)][0]) == 5, 'star first pair 5')
    check(star_work(*STAR_PAIRS[('2-3', 5)][1]) == 4, '2-3 star second pair 4')
    check(star_work(*STAR_PAIRS[('4-5', 5)][1]) == 5, '4-5 star second pair 5')
    # 2-3 invention: three counters each with least work 6
    states3 = [dict(zip(STAR_NODES, m)) for m in
               [tuple(sum(1 for c in ms if c == v) for v in range(4)) for ms in combinations_with_replacement(range(4), 3)]]
    ws = {}
    for a in states3:
        for b in states3:
            ws.setdefault(star_work(a, b), 0)
            ws[star_work(a, b)] += 1
    six = [(a, b) for a in states3 for b in states3 if star_work(a, b) == 6]
    say(f'   three-counter star pairs by least work: {dict(sorted(ws.items()))}; max {max(ws)}')
    say(f'   work-6 pairs: {len(six)}, all with no counter at O and disjoint leaf supports: '
        f'{all(a["O"] == 0 and b["O"] == 0 and all(min(a[L], b[L]) == 0 for L in "ABC") for a, b in six)}')
    check(max(ws) == 6 and len(six) > 0, '2-3 P5 work-6 invention possible')
    check(star_work({'A': 3, 'O': 0, 'B': 0, 'C': 0}, {'A': 0, 'O': 0, 'B': 3, 'C': 0}) == 6, 'guide A3->B3 = 6')
    # 4-5: leaf formula for every start/target with the same number of counters, 1..5 counters
    tot = 0
    for N in range(1, 6):
        sts = [dict(zip(STAR_NODES, tuple(sum(1 for c in ms if c == v) for v in range(4))))
               for ms in combinations_with_replacement(range(4), N)]
        for a in sts:
            d = bfs(STAR, STAR_NODES, star_state(a))[0]
            for b in sts:
                tot += 1
                check(d[star_state(b)] == leaf_formula(a, b), f'leaf formula fails {a} {b}')
    say(f'   leaf-imbalance formula equals BFS least work for all {tot} equal-total star pairs with 1-5 counters')
    say()

    # ---- 2-3 Problem 6: every target admits a start at distance exactly 5
    say('== Grades 2-3 Problem 6: can a target make least work 5 impossible?')
    bad = []
    counts_at5 = []
    for t in allstarts:
        d = line_bfs(to_counts(t))[0]
        n5 = sum(1 for s in allstarts if d[to_counts(s)] == 5)
        counts_at5.append(n5)
        if n5 == 0:
            bad.append(t)
    say(f'   targets with no start at least work 5: {bad}; fewest such starts for any target: {min(counts_at5)} '
        f'(target {allstarts[counts_at5.index(min(counts_at5))]}), most: {max(counts_at5)}')
    check(not bad, '2-3 P6: some target defeats work 5')
    # guide construction: from the target, five one-way steps toward the far end
    okc = True
    for t in allstarts:
        c = list(to_counts(t))
        s = sum(int(x) for x in t)
        right = (20 - s) >= 10
        steps = 0
        while steps < 5:
            if right:
                i = max(i for i in range(NBINS - 1) if c[i] > 0)  # any counter not at bin 5
            else:
                i = min(i for i in range(1, NBINS) if c[i] > 0)
            j = i + 1 if right else i - 1
            c[i] -= 1
            c[j] += 1
            steps += 1
        okc &= work_line(to_pos(c), t) == 5
    say(f'   guide construction (five one-direction steps from the target) gives work exactly 5 for all 126 targets: {okc}')
    check(okc, 'guide P6 construction')
    say()

    # ---- 4-5 Problem 4: cards
    say('== Grades 4-5 Problem 4: position-total-8 cards on bins 0-4')
    allc = [m for m in multisets(4, 5) if sum(int(c) for c in m) == 8]
    say(f'   all four-counter arrangements on bins 0-4 with total 8: {allc} ({len(allc)})')
    check(sorted(allc) == sorted(CARDS) and len(set(CARDS)) == 8, 'card set complete and distinct')
    say(f'   printed cards (reading order A-H): {CARDS}; none missing, none repeated: {sorted(allc) == sorted(CARDS)}')
    guide_mat = [[0, 2, 4, 4, 4, 4, 6, 8], [2, 0, 2, 2, 2, 2, 4, 6], [4, 2, 0, 2, 2, 4, 2, 4], [4, 2, 2, 0, 4, 2, 2, 4],
                 [4, 2, 2, 4, 0, 2, 2, 4], [4, 2, 4, 2, 2, 0, 2, 4], [6, 4, 2, 2, 2, 2, 0, 2], [8, 6, 4, 4, 4, 4, 2, 0]]
    mat5 = [[work_line(a, b, 5) for b in CARDS] for a in CARDS]
    mat6 = [[work_line(a, b, 6) for b in CARDS] for a in CARDS]  # same cards on the six-bin mat
    for row, lab in zip(mat5, 'ABCDEFGH'):
        say(f'   {lab}: {row}')
    check(mat5 == guide_mat, 'guide distance matrix')
    check(mat5 == mat6, 'card distances change on six bins')
    mx = max(max(r) for r in mat5)
    arg = [(CARDS[i], CARDS[j]) for i in range(8) for j in range(i + 1, 8) if mat5[i][j] == mx]
    say(f'   matrix equals the guide\'s; maximum {mx} attained only by {arg}')
    check(mx == 8 and arg == [('0044', '2222')], 'unique max pair')
    # a gap-certificate proof of the maximum: prefix counts F(i) = counters in bins <= i
    pref = {c: [sum(1 for ch in c if int(ch) <= i) for i in range(4)] for c in CARDS}
    rng = [(min(pref[c][i] for c in CARDS), max(pref[c][i] for c in CARDS)) for i in range(4)]
    say(f'   prefix counts F(0..3) over the cards range over {rng}: each gap changes by at most 2, so least work <= 4 x 2 = 8')
    check(all(hi - lo <= 2 for lo, hi in rng), 'gap argument for max 8')
    # 'no pair needs more': every card within 8 of every other also over all total-8 arrangements on 0..5
    allc6 = [m for m in multisets(4, 6) if sum(int(c) for c in m) == 8]
    mx6 = max(work_line(a, b) for a in allc6 for b in allc6)
    say(f'   (aside) with a sixth bin, {len(allc6)} total-8 arrangements; their largest least work is {mx6}')
    say()

    # ---- 4-5 Problem 6: triangle inequality over all triples
    say('== Grades 4-5 Problem 6: least work A->B + B->C versus A->C, four counters on bins 0-5')
    S = allstarts
    D = [[line_bfs(to_counts(a))[0][to_counts(b)] for b in S] for a in S]
    n = len(S)
    viol = eq = strict = 0
    for i in range(n):
        Di = D[i]
        for j in range(n):
            dij = Di[j]
            Dj = D[j]
            for k in range(n):
                v = dij + Dj[k] - Di[k]
                if v < 0:
                    viol += 1
                elif v == 0:
                    eq += 1
                else:
                    strict += 1
    say(f'   {n**3} ordered triples: {viol} with A->B + B->C < A->C, {eq} equal, {strict} strictly greater')
    check(viol == 0 and n ** 3 == 2000376, 'triangle inequality')
    dist_eq = sum(1 for i in range(n) for j in range(n) for k in range(n)
                  if len({i, j, k}) == 3 and D[i][j] + D[j][k] == D[i][k])
    say(f'   triples of three different arrangements with equality: {dist_eq}')
    e = (work_line('0000', '1111'), work_line('1111', '2222'), work_line('0000', '2222'))
    s_ = (work_line('0000', '5555'), work_line('5555', '1111'), work_line('0000', '1111'))
    say(f'   guide equality example 0000,1111,2222: {e[0]}+{e[1]} vs {e[2]}; strict example 0000,5555,1111: {s_[0]}+{s_[1]} vs {s_[2]}')
    check(e == (4, 4, 8) and s_ == (20, 16, 4), 'guide P6 examples')
    say()

    # ---- guide overview: general line theorem, tree theorem, ring example
    say('== Guide overview theorems')
    tot = 0
    for N in range(1, 6):
        ms = multisets(N, NBINS)
        for a in ms:
            d = line_bfs(to_counts(a))[0]
            for b in ms:
                tot += 1
                g = sum(map(abs, gap_row(a, b)))
                if not (d[to_counts(b)] == g == sorted_match(a, b)):
                    check(False, f'line theorem fails {a}->{b}')
    say(f'   line: BFS = sum|S_i| = sorted matching for all {tot} equal-mass pairs with 1-5 counters on 6 bins')
    # nearest-first counterexample
    check({t for t, _ in greedy_runs('03', '25')} == {6} and work_line('03', '25') == 4, 'overview greedy example')
    say('   nearest-first 0,3 -> 2,5: 6 against optimum 4 (confirmed)')
    # equal centre example
    check(work_line('0044', '2222') == 8, 'overview 0044 vs 2222 distance 8')
    say('   0044 versus 2222: equal position totals 8, least work 8 (confirmed)')

    # trees: edge-cut formula versus BFS
    def cut_formula(graph, nodes, a, b):
        tot_ = 0
        seen_edges = set()
        for u in nodes:
            for v in graph[u]:
                e_ = frozenset((u, v))
                if e_ in seen_edges:
                    continue
                seen_edges.add(e_)
                # component of u after removing edge u-v
                comp, stack = {u}, [u]
                while stack:
                    x = stack.pop()
                    for y in graph[x]:
                        if frozenset((x, y)) == e_ or y in comp:
                            continue
                        comp.add(y)
                        stack.append(y)
                tot_ += abs(sum(a[nodes.index(x)] - b[nodes.index(x)] for x in comp))
        return tot_

    trees = {
        'star3': (STAR, STAR_NODES),
        'spider 2-2-1': ({0: [1, 3, 5], 1: [0, 2], 2: [1], 3: [0, 4], 4: [3], 5: [0]}, [0, 1, 2, 3, 4, 5]),
        'caterpillar': ({0: [1], 1: [0, 2, 4], 2: [1, 3, 5], 3: [2], 4: [1], 5: [2]}, [0, 1, 2, 3, 4, 5]),
        'star4': ({0: [1, 2, 3, 4], 1: [0], 2: [0], 3: [0], 4: [0]}, [0, 1, 2, 3, 4]),
    }
    for name, (g, nodes) in trees.items():
        cnt = 0
        for N in range(1, 4):
            sts = [tuple(sum(1 for c in ms if c == v) for v in range(len(nodes)))
                   for ms in combinations_with_replacement(range(len(nodes)), N)]
            for a in sts:
                d = bfs(g, nodes, a)[0]
                for b in sts:
                    cnt += 1
                    if d[b] != cut_formula(g, nodes, a, b):
                        check(False, f'tree formula fails on {name} {a}->{b}')
        say(f'   tree {name}: edge-cut sum equals BFS for all {cnt} equal-mass pairs with 1-3 counters')
    # ring example and failure of the cut argument on a cycle
    r4 = bfs(ring_graph(4), [0, 1, 2, 3], (1, 0, 0, 0))[0][(0, 0, 0, 1)]
    l4 = bfs(line_graph(4), [0, 1, 2, 3], (1, 0, 0, 0))[0][(0, 0, 0, 1)]
    say(f'   ring of four bins, counter 0 -> 3: {r4}; open line 0-1-2-3: {l4} (guide: one and three)')
    check(r4 == 1 and l4 == 3, 'ring example')
    say()

    say(f'FAILURES: {len(FAILS)}')
    for f in FAILS:
        say('  ' + f)
    text = '\n'.join(OUT) + '\n'
    (HERE / 'check_math.py.out').write_text(text)
    print(text)
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
