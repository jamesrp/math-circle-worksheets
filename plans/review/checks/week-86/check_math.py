#!/usr/bin/env python3
"""Independent mathematical checks for Week 86 (Pursuit and escape).

Written for the math-check stage of the review. It does not import or run the
package's build.py, verify.py or check_math.py. Standard library only.

Game (as printed): finite connected graph; C places first, then R (placing on
C is immediate capture); C moves first; each turn a player stays or crosses one
road; sharing a dot is immediate capture. Two-cop version: both cops placed,
then R; on a cop turn each cop stays or crosses one road; then R moves.

Exact solver: for every cop-to-move position the least number of cop turns
that guarantees capture (or infinity), by rounds of backward induction
W_1 = {R in N[C]}, W_{k+1} = {exists cop move: capture, or every R reply in W_k}.

Checks (every board is the graph that check_pdf.py reads from the PDFs):
- Problem 1 (P5, P7) and the guide's path formula for n = 1..14.
- Problem 2 (T1, T2): values, best starts, the guide's 'move toward R' plan
  from every start, its 'start at c, within two moves' claim, and the
  component-shrinking argument; all labelled trees up to 8 dots.
- Problems 3-4 (R3-R6) and cycles C3..C14: who wins; the guide's square
  'opposite' escape and its ring escape rule replayed against every cop move;
  the odd-ring reading of 'opposite' (stay on a farthest dot) replayed with
  every tie-break, to test the guide's sentence that it is not adequate.
- Upper Problem 2 (E4, E5): every set of added roads of each size; the guide's
  one-chord projection (retraction) argument.
- Upper Problem 3: the guide's two examples; census of all connected graphs on
  the six labelled dots with at least six roads.
- Upper Problem 4 (F1, F2) and the fold theory: every fold sequence; the
  guide's sequence; fold preservation, dismantlable <=> cop-win, and the
  no-dominated-vertex evasion rule on every connected graph with <= 6 dots.
- Upper Problems 5-6 (Q6, Q8): exact two-cop values from the common start at a
  and from free placement; the guide's blocker plan replayed on C3..C14.
- The rules-page and fold-page worked examples.

Run: python3 check_math.py  (writes check_math.py.out beside itself)
"""
import itertools
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
INF = float('inf')
OUT = []
FAILS = []


def log(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg, detail=''):
    tag = 'PASS' if cond else 'FAIL'
    if not cond:
        FAILS.append(msg)
    log(f'{tag} {msg}' + (f'  [{detail}]' if detail != '' else ''))


# ---------------------------------------------------------------- graphs
def G(vertices, edges):
    adj = {v: {v} for v in vertices}
    for e in edges:
        a, b = tuple(e)
        adj[a].add(b)
        adj[b].add(a)
    return adj  # closed neighbourhoods N[v]


def ring(n):
    v = [chr(97 + i) for i in range(n)] if n <= 26 else list(range(n))
    return G(v, [(v[i], v[(i + 1) % n]) for i in range(n)])


def path(n):
    v = [chr(97 + i) for i in range(n)]
    return G(v, [(v[i], v[i + 1]) for i in range(n - 1)])


def edges_of(adj):
    return {frozenset((a, b)) for a in adj for b in adj[a] if a != b}


def add_edges(adj, extra):
    return G(list(adj), list(edges_of(adj)) + [tuple(e) for e in extra])


def connected(adj):
    vs = list(adj)
    if not vs:
        return True
    seen = {vs[0]}
    dq = deque([vs[0]])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                dq.append(w)
    return len(seen) == len(vs)


def dist_from(adj, s):
    d = {s: 0}
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if w not in d:
                d[w] = d[u] + 1
                dq.append(w)
    return d


def remove(adj, v):
    return {u: (adj[u] - {v}) for u in adj if u != v}


# ---------------------------------------------------------------- one cop
def solve1(adj, policy=None):
    """T[(c, r)] = least cop turns to guarantee capture, cop to move, c != r.
    If policy is given (function (c, r) -> c'), the cop is restricted to it."""
    V = list(adj)
    T = {}
    for c in V:
        for r in V:
            if c != r and r in adj[c] and (policy is None or policy(c, r) == r):
                T[(c, r)] = 1
    k = 1
    while True:
        new = {}
        for c in V:
            for r in V:
                if c == r or (c, r) in T:
                    continue
                moves = adj[c] if policy is None else [policy(c, r)]
                for c2 in moves:
                    if c2 == r:
                        new[(c, r)] = k + 1
                        break
                    if all((c2, r2) in T for r2 in adj[r] if r2 != c2):
                        new[(c, r)] = k + 1
                        break
        if not new:
            break
        T.update(new)
        k += 1
    return T


def start_values(adj, T):
    """value[c0] = max over R placements of capture time (0 if R must share)."""
    val = {}
    for c0 in adj:
        worst = 0
        for r0 in adj:
            if r0 != c0:
                worst = max(worst, T.get((c0, r0), INF))
        val[c0] = worst
    return val


def copwin(adj):
    T = solve1(adj)
    v = start_values(adj, T)
    return min(v.values()) < INF


def robber_policy_never_caught(adj, place, rho):
    """place(c0) -> r0 ; rho(c, r) -> r' (R's reply after C moved to c).
    Explore every cop choice; return list of capture positions reached."""
    bad = []
    seen = set()
    dq = deque()
    for c0 in adj:
        r0 = place(c0)
        if r0 == c0:
            bad.append(('placement', c0))
            continue
        dq.append((c0, r0))
    while dq:
        c, r = dq.popleft()
        if (c, r) in seen:
            continue
        seen.add((c, r))
        for c2 in adj[c]:
            if c2 == r:
                bad.append(('cop move', c, r, c2))
                continue
            r2 = rho(c2, r)
            if r2 not in adj[r] or r2 == c2:
                bad.append(('robber', c2, r, r2))
                continue
            dq.append((c2, r2))
    return bad


# ---------------------------------------------------------------- two cops
def solve2(adj, policy=None):
    """T[(c1, c2, r)] = least cop turns, cops to move, r not in {c1, c2}."""
    V = list(adj)
    states = [(a, b, r) for a in V for b in V for r in V if r != a and r != b]
    T = {}

    def cop_moves(a, b, r):
        if policy is not None:
            return [policy(a, b, r)]
        return [(x, y) for x in adj[a] for y in adj[b]]

    for (a, b, r) in states:
        if any(r in mv for mv in cop_moves(a, b, r)):
            T[(a, b, r)] = 1
    k = 1
    while True:
        new = {}
        for s in states:
            if s in T:
                continue
            a, b, r = s
            for (x, y) in cop_moves(a, b, r):
                if r in (x, y):
                    new[s] = k + 1
                    break
                if all((x, y, r2) in T for r2 in adj[r] if r2 not in (x, y)):
                    new[s] = k + 1
                    break
        if not new:
            break
        T.update(new)
        k += 1
    return T


def two_cop_value(adj, T, a, b):
    worst = 0
    for r in adj:
        if r not in (a, b):
            worst = max(worst, T.get((a, b, r), INF))
    return worst


# ---------------------------------------------------------------- folds
def dominated_pairs(adj):
    return [(v, u) for v in adj for u in adj if u != v and u in adj[v] and adj[v] <= adj[u]]


def all_fold_outcomes(adj):
    """Explore every sequence of folds; return set of frozensets of
    remaining vertex sets at dead ends."""
    ends = set()
    seen = set()
    stack = [frozenset(adj)]
    while stack:
        S = stack.pop()
        if S in seen:
            continue
        seen.add(S)
        sub = {u: adj[u] & S for u in S}
        dp = dominated_pairs(sub)
        if not dp:
            ends.add(S)
        for v, u in dp:
            stack.append(S - {v})
    return ends


def dismantlable(adj):
    S = dict(adj)
    while len(S) > 1:
        dp = dominated_pairs(S)
        if not dp:
            return False
        S = remove(S, dp[0][0])
    return True


# ---------------------------------------------------------------- utilities
def prufer_trees(n):
    """All labelled trees on n vertices (as edge lists)."""
    if n == 1:
        yield []
        return
    if n == 2:
        yield [(0, 1)]
        return
    for seq in itertools.product(range(n), repeat=n - 2):
        deg = [1] * n
        for x in seq:
            deg[x] += 1
        edges = []
        s = list(seq)
        for x in s:
            for leaf in range(n):
                if deg[leaf] == 1:
                    edges.append((leaf, x))
                    deg[leaf] -= 1
                    deg[x] -= 1
                    break
        u, w = [i for i in range(n) if deg[i] == 1]
        edges.append((u, w))
        yield edges


def toward(adj):
    """Tree policy: step to the next dot on the unique path to R."""
    D = {v: dist_from(adj, v) for v in adj}

    def pol(c, r):
        return min((w for w in adj[c] if w != c), key=lambda w: D[w][r])
    return pol


def fmt(v):
    return '∞' if v == INF else str(v)


# ================================================================ checks
def main():
    # ---------------------------------------------------------- examples
    log('== Rules-page worked example ==')
    ex = G(list('wxyz'), ['wx', 'xy', 'xz'])
    check('x' in ex['w'], 'example: C at w taking one road to x is legal')
    check('y' in ex['y'], 'example: R stays at y (staying is allowed)')
    T = solve1(ex)
    log(f'  (side fact) example star: values by C start {dict((k, fmt(v)) for k, v in start_values(ex, T).items())}')

    log('\n== Fold-page worked example (path w-x-y-z) ==')
    fp = G(list('wxyz'), ['wx', 'xy', 'yz'])
    check(fp['w'] == {'w', 'x'} and fp['x'] == {'w', 'x', 'y'}, 'w reaches {w,x}; x reaches {w,x,y}')
    check(('w', 'x') in dominated_pairs(fp), 'w -> x is a legal fold')
    after = remove(fp, 'w')
    check(edges_of(after) == {frozenset('xy'), frozenset('yz')}, 'after w -> x the map is x-y-z')

    # ---------------------------------------------------------- Problem 1
    log('\n== Problem 1 (shared and upper): paths ==')
    for n, name in ((5, 'P5'), (7, 'P7')):
        adj = path(n)
        T = solve1(adj)
        val = start_values(adj, T)
        best = min(val.values())
        starts = sorted(k for k, v in val.items() if v == best)
        log(f'  {name}: worst-case cop turns by start {dict((k, fmt(v)) for k, v in sorted(val.items()))}')
        check(best == n // 2, f'{name}: optimum is floor(n/2) = {n // 2} cop turns', best)
        check(starts == [chr(97 + n // 2)], f'{name}: unique best start is the middle dot {chr(97 + n // 2)}', starts)
        Tp = solve1(adj, toward(adj))
        vp = start_values(adj, Tp)
        check(vp[chr(97 + n // 2)] == n // 2, f'{name}: moving toward R from the middle achieves the optimum',
              vp[chr(97 + n // 2)])
        # lower bound: R at a farthest endpoint and staying
        far = max(adj, key=lambda v: dist_from(adj, chr(97 + n // 2))[v])
        check(T[(chr(97 + n // 2), far)] == n // 2, f'{name}: R at farthest endpoint {far} forces {n // 2}')
    ok = True
    det = []
    for n in range(1, 15):
        adj = path(n)
        T = solve1(adj)
        val = start_values(adj, T)
        best = min(val.values())
        starts = sorted(k for k, v in val.items() if v == best)
        mids = sorted({chr(97 + (n - 1) // 2), chr(97 + n // 2)})
        if best != n // 2 or starts != mids:
            ok = False
            det.append((n, best, starts))
    check(ok, 'guide overview: on every n-dot path (n = 1..14) the best starts are the middle dot(s), value floor(n/2)',
          det)

    # ---------------------------------------------------------- Problem 2
    log('\n== Shared Problem 2: trees T1, T2 ==')
    T1 = G(list('abcdefg'), ['ab', 'bc', 'cd', 'de', 'cf', 'fg'])
    T2 = G(list('abcdefgh'), ['ab', 'bc', 'cd', 'de', 'cf', 'fg', 'fh'])
    for name, adj in (('T1', T1), ('T2', T2)):
        T = solve1(adj)
        val = start_values(adj, T)
        best = min(val.values())
        starts = sorted(k for k, v in val.items() if v == best)
        log(f'  {name}: optimal worst-case cop turns by start {dict((k, fmt(v)) for k, v in sorted(val.items()))}')
        check(best == 2 and 'c' in starts, f'{name}: best value 2, attained at c', (best, starts))
        Tp = solve1(adj, toward(adj))
        vp = start_values(adj, Tp)
        check(all(v < INF for v in vp.values()), f'{name}: "move toward R" wins from every start')
        check(vp['c'] == 2, f'{name}: from c, "move toward R" captures within two cop moves', vp['c'])
        ecc = {v: max(dist_from(adj, v).values()) for v in adj}
        check(all(vp[v] == ecc[v] == val[v] for v in adj),
              f'{name}: toward-R capture time from each start = optimum = eccentricity')
    # Component-shrinking argument and all small trees
    ok = True
    shrink_ok = True
    for n in range(1, 9):
        for edges in prufer_trees(n):
            adj = G(list(range(n)), edges)
            pol = toward(adj)
            Tp = solve1(adj, pol)
            vp = start_values(adj, Tp)
            if any(v == INF for v in vp.values()):
                ok = False
            # shrinking: after every uncaptured cop advance R's component in G - C strictly shrinks
            for c in adj:
                for r in adj:
                    if c == r:
                        continue
                    def comp(cc, rr):
                        sub = remove(adj, cc)
                        return frozenset(dist_from(sub, rr))
                    K = comp(c, r)
                    c2 = pol(c, r)
                    if c2 == r:
                        continue
                    K2 = comp(c2, r)
                    if not (K2 < K):
                        shrink_ok = False
                    for r2 in adj[r]:
                        if r2 != c2 and r2 not in K2:
                            shrink_ok = False
    check(ok, 'guide: every labelled tree with up to 8 dots is cop-win by "move toward R" from any start')
    check(shrink_ok, 'guide: on those trees each uncaptured advance strictly shrinks R\'s component and R cannot leave it')

    # ---------------------------------------------------------- Problems 3-4
    log('\n== Shared Problems 3-4: rings ==')
    for n in range(3, 15):
        adj = ring(n)
        T = solve1(adj)
        val = start_values(adj, T)
        if n <= 6:
            log(f'  C{n}: values by start {dict((k, fmt(v)) for k, v in sorted(val.items()))}')
        if n == 3:
            check(all(v == 1 for v in val.values()), 'R3: C wins from any start, capture on the first move')
        else:
            check(all(v == INF for v in val.values()), f'C{n}: R escapes forever from every C start')
    # guide's square strategy
    sq = ring(4)
    opp = {'a': 'c', 'b': 'd', 'c': 'a', 'd': 'b'}
    bad = robber_policy_never_caught(sq, lambda c0: opp[c0], lambda c, r: opp[c] if opp[c] in sq[r] else None)
    check(not bad, 'R4: guide strategy (start opposite; stay when C stays, else move to new opposite) is never caught', bad[:3])

    def ring_rule(adj):
        def place(c0):
            return next(v for v in adj if v not in adj[c0])

        def rho(c, r):
            if r not in adj[c]:
                return r
            other = [w for w in adj[r] if w != r and w != c]
            return other[0]
        return place, rho
    for n in range(4, 15):
        adj = ring(n)
        place, rho = ring_rule(adj)
        bad = robber_policy_never_caught(adj, place, rho)
        check(not bad, f'C{n}: guide ring rule (stay if outside N[C], else step to the other neighbour) is never caught',
              bad[:2])
    # Guide: '"Opposite" is not an adequate general rule on an odd ring.'
    # Test the natural odd-ring reading of "opposite": R places on a dot across
    # from C (a farthest dot) and after each cop move goes to (or stays on) a
    # reachable dot as far from C as possible. Every tie-break is explored.
    for n in range(4, 15):
        adj = ring(n)
        D = {v: dist_from(adj, v) for v in adj}
        far = max(D['a'].values())
        caught = []
        seen = set()
        dq = deque((c0, r0) for c0 in adj for r0 in adj if D[c0][r0] == far)
        while dq:
            c, r = dq.popleft()
            if (c, r) in seen:
                continue
            seen.add((c, r))
            for c2 in adj[c]:
                if c2 == r:
                    caught.append((c, r, c2))
                    continue
                opts = [w for w in adj[r] if w != c2]
                m = max(D[c2][w] for w in opts)
                for w in opts:
                    if D[c2][w] == m:
                        dq.append((c2, w))
        dists = sorted({D[c][r] for c, r in seen})
        check(not caught, f'C{n}: "stay across from C" (start on a farthest dot, then move to or stay on a reachable '
                          f'farthest dot, any tie-break) is never caught', f'distances kept {dists}')

    # ---------------------------------------------------------- Upper Problem 2
    log('\n== Upper Problem 2: fewest added roads ==')
    for n, name in ((4, 'E4'), (5, 'E5')):
        adj = ring(n)
        nonedges = [frozenset(p) for p in itertools.combinations(adj, 2) if frozenset(p) not in edges_of(adj)]
        found = None
        for k in range(0, len(nonedges) + 1):
            good, badsets = [], []
            for S in itertools.combinations(nonedges, k):
                (good if copwin(add_edges(adj, S)) else badsets).append(S)
            log(f'  {name}: adding {k} road(s): {len(good)} cop-win, {len(badsets)} robber-win')
            if k > 0 and k <= 2:
                log('     cop-win: ' + ', '.join('+'.join(''.join(sorted(e)) for e in S) for S in good))
                log('     robber-win: ' + ', '.join('+'.join(''.join(sorted(e)) for e in S) for S in badsets))
            if good and found is None:
                found = k
            if k >= 2:
                break
        check(found == {4: 1, 5: 2}[n], f'{name}: fewest added roads = {found}')
    # guide claims
    sqd = add_edges(ring(4), ['ac'])
    T = solve1(sqd)
    check(start_values(sqd, T)['a'] == 1, 'E4 + a-c: C starts at a and catches on move one')
    e5 = add_edges(ring(5), ['ac', 'ad'])
    T = solve1(e5)
    check(start_values(e5, T)['a'] == 1, 'E5 + a-c, a-d: a is adjacent to every dot; capture on move one')
    one = add_edges(ring(5), ['ac'])
    proj = {'a': 'a', 'b': 'a', 'c': 'c', 'd': 'd', 'e': 'e'}
    sqr = G(list('acde'), ['ac', 'cd', 'de', 'ea'])
    hom = all(proj[y] in sqr[proj[x]] for x in one for y in one[x])
    check(hom, 'guide: b -> a, others fixed, maps every move or stay of the one-chord pentagon to a move or stay of square a-c-d-e')
    check(not copwin(one), 'one-chord pentagon (= F2) is robber-win')
    # crossing pairs (not covered by the guide)
    cross = add_edges(ring(5), ['ac', 'bd'])
    check(not copwin(cross), '(note) E5 + crossing chords a-c, b-d is robber-win: b and c become twins, folding b leaves square a-c-d-e',
          sorted(dominated_pairs(cross)))

    # ---------------------------------------------------------- Upper Problem 3
    log('\n== Upper Problem 3: design two six-dot maps ==')
    six = list('abcdef')
    d1 = G(six, ['ab', 'bc', 'ca', 'cd', 'de', 'ef'])
    check(len(edges_of(d1)) == 6 and connected(d1) and copwin(d1), 'guide D1: triangle a-b-c with tail c-d-e-f, six roads, cop-win')
    T = solve1(d1)
    check(start_values(d1, T)['c'] < INF, 'guide D1: starting C at c wins', fmt(start_values(d1, T)['c']))
    c6 = ring(6)
    check(len(edges_of(c6)) == 6 and not copwin(c6), 'guide D2: bare six-ring, six roads, robber-win')
    pairs = list(itertools.combinations(six, 2))
    cw = rw = 0
    rw_max_edges = 0
    for mask in range(1 << 15):
        E = [pairs[i] for i in range(15) if mask >> i & 1]
        if len(E) < 6:
            continue
        adj = G(six, E)
        if not connected(adj):
            continue
        if dismantlable(adj):
            cw += 1
        else:
            rw += 1
            rw_max_edges = max(rw_max_edges, len(E))
    log(f'  connected labelled graphs on a..f with >= 6 roads: {cw} cop-win (dismantlable), {rw} robber-win; '
        f'most roads in a robber-win one: {rw_max_edges}')
    check(cw > 0 and rw > 0, 'both kinds exist, so both D1 and D2 are possible')
    check(all(len(t) == 5 for t in prufer_trees(6)), 'every six-dot tree has 5 roads, so ">= 6 roads" excludes trees')

    # ---------------------------------------------------------- Upper Problem 4
    log('\n== Upper Problem 4: fold boards F1, F2 ==')
    F1 = G(list('abcdef'), ['ab', 'bc', 'ca', 'cd', 'de', 'af'])
    F2 = add_edges(ring(5), ['ac'])
    ends1 = all_fold_outcomes(F1)
    check(all(len(S) == 1 for S in ends1), 'F1: every sequence of legal folds ends at one dot', sorted(map(sorted, ends1)))
    S = dict(F1)
    seq = [('e', 'd'), ('d', 'c'), ('f', 'a'), ('a', 'b'), ('b', 'c')]
    okseq = True
    for v, u in seq:
        if (v, u) not in dominated_pairs(S):
            okseq = False
        S = remove(S, v)
    check(okseq and list(S) == ['c'], 'guide F1 sequence e->d, d->c, f->a, a->b, b->c is legal at every step')
    check(copwin(F1), 'F1 is cop-win (solver)')
    dp2 = dominated_pairs(F2)
    check(sorted(dp2) == [('b', 'a'), ('b', 'c')], 'F2: initially only b can fold, into a or c', dp2)
    ends2 = all_fold_outcomes(F2)
    check(ends2 == {frozenset('acde')}, 'F2: every fold sequence ends at the square a,c,d,e', sorted(map(sorted, ends2)))
    check(not dominated_pairs(remove(F2, 'b')), 'F2 after removing b: no legal fold')
    check(not copwin(F2), 'F2 is robber-win (solver)')

    log('\n== Fold theory on every connected labelled graph with <= 6 dots ==')
    tot = 0
    mism = pres = noevade = 0
    for n in range(1, 7):
        V = list(range(n))
        pairs = list(itertools.combinations(V, 2))
        for mask in range(1 << len(pairs)):
            E = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            adj = G(V, E)
            if not connected(adj):
                continue
            tot += 1
            cw_ = copwin(adj)
            if cw_ != dismantlable(adj):
                mism += 1
            for v, u in dominated_pairs(adj):
                if n > 1 and copwin(remove(adj, v)) != cw_:
                    pres += 1
            if n > 1 and not dominated_pairs(adj):
                # guide's evasion rule: place outside N[C]; stay if outside N[C], else move into N[R] - N[C]
                def place(c0, adj=adj):
                    return next((v for v in adj if v not in adj[c0]), c0)

                def rho(c, r, adj=adj):
                    if r not in adj[c]:
                        return r
                    return next(iter(sorted(adj[r] - adj[c])), r)
                if robber_policy_never_caught(adj, place, rho):
                    noevade += 1
    log(f'  connected graphs checked: {tot}')
    check(mism == 0, 'cop-win <=> dismantlable (reducible to one dot by folds)', mism)
    check(pres == 0, 'every single fold preserves cop-win / robber-win status', pres)
    check(noevade == 0, 'guide evasion rule never caught on every graph with >1 dot and no dominated dot', noevade)

    # ---------------------------------------------------------- Upper Problems 5-6
    log('\n== Upper Problems 5-6: two cops on rings ==')
    for n, name in ((6, 'Q6'), (8, 'Q8')):
        adj = ring(n)
        T = solve2(adj)
        vaa = two_cop_value(adj, T, 'a', 'a')
        best = min(two_cop_value(adj, T, x, y) for x in adj for y in adj)
        log(f'  {name}: optimal worst case from both at a = {fmt(vaa)} cop turns; best free placement = {fmt(best)}')
        if n == 6:
            check(vaa == 3, 'Q6: from both cops at a the optimal guarantee is 3 cop turns', vaa)
        check(vaa < INF, f'{name}: two cops starting together at a always win')
    # guide's blocker plan on C3..C14
    for n in range(3, 15):
        adj = ring(n)
        V = list(adj)
        a, b = V[0], V[1]
        D = None
        sub = remove(adj, a)
        Dsub = {v: dist_from(sub, v) for v in sub}

        def plan(c1, c2, r, a=a, b=b, sub=sub, Dsub=Dsub, adj=adj):
            # C1 stays at a. C2: from a go to b; then step toward R along the path ring - a.
            if c2 == a:
                return (c1, b)
            if r == a:
                return (c1, c2)
            nxt = min(sub[c2], key=lambda w: Dsub[w].get(r, 10 ** 6))
            return (c1, nxt)
        T = solve2(adj, plan)
        v = two_cop_value(adj, T, a, a)
        exact = two_cop_value(adj, solve2(adj), a, a) if n <= 10 else None
        log(f'  C{n}: guide blocker plan worst case = {fmt(v)} cop turns' + (f' (optimal {fmt(exact)})' if exact is not None else ''))
        check(v < INF, f'C{n}: guide blocker plan (C1 holds a, C2 to b then toward R) always captures')
    # one cop cannot (already checked: C_n, n >= 4, robber-win)

    log(f'\nSummary: {len(FAILS)} failures')
    for f in FAILS:
        log('  FAIL ' + f)
    (HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
