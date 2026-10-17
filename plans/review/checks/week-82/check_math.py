#!/usr/bin/env python3
"""Independent mathematical checks for Week 82 (Endless class lines).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

What it checks
- Opening examples and Problem 1: exhaustive enumeration of complete matches
  (bijections) and of all matches that may leave kids out (partial matchings),
  with the page's order rule tested on every pair of kids.
- Problems 2-4 and the guide's order-type claims: each class line is modelled
  exactly as a token word over W (an endless row 1, 2, 3, ...) and S (one star
  kid). Order invariants are computed symbolically from the word (exact, not
  sampled): which kids have infinitely many predecessors, which have no
  immediately preceding kid, whether there is a last kid, how many kids have
  only finitely many successors. Order isomorphism preserves all of these.
- Ordinal arithmetic below omega^2 (omega*a + b) is computed independently and
  compared with the invariants.
- Explicit matching rules (the guide's and my own) are given as formulas on
  every kid; their inverse, injectivity, ontoness and order preservation are
  replayed on all kids with index <= N. The formulas are uniform in n, so the
  replay is a regression check; the general argument is in math.md.
- Problem 4: all 16 arrangements of one or two endless rows and 0-2 stars,
  their order types, which pairs can be matched keeping order, and how many
  printed panels each arrangement or pair needs.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from itertools import combinations, permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    if len(here.parents) > 3 and (here.parents[3] / 'AGENTS.md').is_file() and (here.parents[3] / 'lowell-math-circle-year-2').is_dir():
        return here.parents[3]
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
OUT, FAIL = [], []
N = 3000  # replay range for formula-defined infinite matchings


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- finite part
def keeps_order_pairs(pairs):
    """pairs: list of (first-class position, second-class position).
    Page rule: any two kids in the first class appear in the same order as
    their partners in the second class. Tested on every pair."""
    return all((a1 < a2) == (b1 < b2) for (a1, b1), (a2, b2) in combinations(pairs, 2))


def complete_matches(n, m):
    """All bijections between a line of n kids and a line of m kids."""
    if n != m:
        return []
    return [list(zip(range(n), p)) for p in permutations(range(m))]


def all_matches(n, m):
    """All matchings (each kid at most one partner), including incomplete ones."""
    res = []
    for k in range(min(n, m) + 1):
        for left in combinations(range(n), k):
            for right in permutations(range(m), k):
                res.append(list(zip(left, right)))
    return res


def finite_part():
    say('== Opening examples (p. 1) ==')
    five = complete_matches(5, 5)
    check(len(five) == 120, '5-to-5: 120 complete matches')
    ident = [(i, i) for i in range(5)]
    swap = [(0, 1), (1, 0), (2, 2), (3, 3), (4, 4)]
    check(ident in five and keeps_order_pairs(ident), 'panel 1 (1-A ... 5-E) is a complete match that keeps order')
    check(swap in five and not keeps_order_pairs(swap), 'panel 2 (1-B, 2-A, 3-C, 4-D, 5-E) is complete and does not keep order')
    check([p for p in five if keeps_order_pairs(p)] == [ident], '5-to-5: the only order-keeping complete match is 1-A ... 5-E')
    check(complete_matches(5, 6) == [], '5 kids and 6: no complete match exists (pigeonhole)')
    biggest = max(len(p) for p in all_matches(5, 6))
    check(biggest == 5, '5 kids and 6: every match leaves at least one kid of the 6 out (largest match has 5 pairs)')

    say('== Problem 1 (p. 1): R1 R2 R3 with B1 B2 B3 ==')
    comp = complete_matches(3, 3)
    lists = [tuple(b + 1 for _, b in sorted(p)) for p in comp]
    guide_lists = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    check(sorted(lists) == sorted(guide_lists) and len(lists) == 6,
          'complete matches = the guide\'s six B-partner lists of R1, R2, R3')
    keep = [l for l, p in zip(lists, comp) if keeps_order_pairs(p)]
    check(keep == [(1, 2, 3)], 'only (1,2,3) keeps order, as the guide says')
    # A rule that only checks neighbours would wrongly pass some lists? (it does not for 3 kids)
    adj = [l for l in lists if all(l[i] < l[i + 1] for i in range(2))]
    check(adj == [(1, 2, 3)], 'checking neighbours only gives the same answer for 3 kids')
    say('   Other reading: "match" without "complete" (the opening shows a match that leaves F out).')
    allm = all_matches(3, 3)
    allk = [p for p in allm if keeps_order_pairs(p)]
    nonempty = [p for p in allm if p]
    nonempty_k = [p for p in allk if p]
    say(f'   matches that may leave kids out: {len(allm)} including the empty one ({len(nonempty)} non-empty)')
    say(f'   of these keep order: {len(allk)} including the empty one ({len(nonempty_k)} non-empty)')
    by_size = {k: (sum(1 for p in allm if len(p) == k), sum(1 for p in allk if len(p) == k)) for k in range(4)}
    say('   by number of pairs k: k -> (matches, order-keeping):', by_size)
    check(len(allm) == 34 and len(allk) == 20, 'partial-match reading changes Problem 1 from 6/1 to 34/20 (33/19 non-empty)')
    return {'p1_complete': len(comp), 'p1_partial': len(allm)}


# ---------------------------------------------------------------- infinite part
# A class line is a word over 'W' (an endless row of kids 1, 2, 3, ...) and
# 'S' (a single star kid).  Kid = (token index i, n) with n = 1 for a star and
# n >= 1 within a row.  The line order is lexicographic in (i, n).

def inv(word):
    """Exact order invariants of the line described by `word`."""
    # limit kids: have a predecessor but no immediately preceding kid.
    # Inside a row, kid n>1 has predecessor n-1.  The first kid of token i>0 has
    # an immediate predecessor iff token i-1 is a star (a row has no last kid).
    limits = sum(1 for i in range(1, len(word)) if word[i - 1] == 'W')
    has_last = word[-1] == 'S'
    # kids with only finitely many successors: stars after the last row.
    last_w = max(i for i, t in enumerate(word) if t == 'W')
    finite_tail = sum(1 for t in word[last_w + 1:] if t == 'S')
    # kids with infinitely many predecessors: every kid of a token after a row.
    first_w = min(i for i, t in enumerate(word) if t == 'W')
    inf_pred = 'none' if first_w == len(word) - 1 else (
        'infinitely many' if 'W' in word[first_w + 1:] else str(len(word) - 1 - first_w))
    return {'limits': limits, 'last': has_last, 'tail': finite_tail, 'inf_pred': inf_pred}


def ordinal(word):
    """Ordinal arithmetic below omega^2: (a, b) means omega*a + b."""
    a, b = 0, 0
    for t in word:
        if t == 'S':
            b += 1           # alpha + 1
        else:
            a, b = a + 1, 0  # alpha + omega absorbs any finite tail
    return (a, b)


def name(o):
    a, b = o
    head = {0: '', 1: 'ω', 2: 'ω·2'}.get(a, f'ω·{a}')
    if b == 0:
        return head or '0'
    return f'{head}+{b}' if head else str(b)


def to_canonical(word):
    """Explicit order isomorphism from the line to omega*a + b.
    Canonical kids: ('row', j, m) for j < a, m >= 1, then ('tail', k).
    Stars waiting before row j go to the front of canonical row j."""
    a, b = ordinal(word)
    fwd = {}
    pending, j, rows = [], 0, []
    for i, t in enumerate(word):
        if t == 'S':
            pending.append(i)
        else:
            rows.append((i, list(pending)))
            pending = []
    tail = pending
    for j, (i, stars) in enumerate(rows):
        for k, s in enumerate(stars):
            fwd[(s, 1)] = ('row', j, k + 1)
    tail_map = {s: ('tail', k) for k, s in enumerate(tail)}

    def f(kid):
        i, n = kid
        if word[i] == 'S':
            return fwd.get((i, 1)) or tail_map[i]
        j = [r[0] for r in rows].index(i)
        return ('row', j, n + len(rows[j][1]))

    def g(c):
        if c[0] == 'tail':
            return (tail[c[1]], 1)
        _, j, m = c
        i, stars = rows[j]
        return (stars[m - 1], 1) if m <= len(stars) else (i, m - len(stars))
    return f, g, (a, b)


def kids(word, n_max):
    return [(i, n) for i, t in enumerate(word) for n in ([1] if t == 'S' else range(1, n_max + 1))]


def canon_kids(o, n_max):
    a, b = o
    return [('row', j, m) for j in range(a) for m in range(1, n_max + 1)] + [('tail', k) for k in range(b)]


def canon_key(c):
    return (c[1], c[2]) if c[0] == 'row' else (10 ** 9, c[1])


def replay_iso(word, n_max=N):
    f, g, o = to_canonical(word)
    ks = kids(word, n_max)
    imgs = [f(k) for k in ks]
    ok_inj = len(set(imgs)) == len(imgs)
    ok_inv = all(g(f(k)) == k for k in ks)
    # onto: every canonical kid with index <= n_max - (stars before) is hit; use g
    ok_onto = all(f(g(c)) == c for c in canon_kids(o, n_max))
    ok_order = all(canon_key(imgs[x]) < canon_key(imgs[x + 1]) for x in range(len(ks) - 1))
    return ok_inj and ok_inv and ok_onto and ok_order


def to_naturals(word):
    """A size match (ignoring order) of the line with 1, 2, 3, ...:
    stars get 1..s, then the r-th of k rows' kid n gets s + k(n-1) + r + 1."""
    stars = [i for i, t in enumerate(word) if t == 'S']
    rows = [i for i, t in enumerate(word) if t == 'W']
    s, k = len(stars), len(rows)

    def f(kid):
        i, n = kid
        if word[i] == 'S':
            return stars.index(i) + 1
        return s + k * (n - 1) + rows.index(i) + 1

    def g(m):
        if m <= s:
            return (stars[m - 1], 1)
        q, r = divmod(m - s - 1, k)
        return (rows[r], q + 1)
    return f, g


def infinite_part():
    say('== Invariants and ordinal arithmetic agree (all 16 Problem 4 arrangements) ==')
    words = sorted({''.join(p) for r in (1, 2) for s in range(3) for p in permutations('W' * r + 'S' * s)},
                   key=lambda w: (w.count('W'), len(w), w))
    check(len(words) == 16, '16 arrangements of one or two endless rows and 0-2 stars')
    types = {}
    for w in words:
        o, iv = ordinal(w), inv(w)
        a, b = o
        expect = {'limits': (a - 1) + (1 if b > 0 else 0), 'last': b > 0, 'tail': b}
        agree = all(iv[k] == v for k, v in expect.items())
        iso_ok = replay_iso(w)
        f, g = to_naturals(w)
        size_ok = all(g(f(k)) == k for k in kids(w, 400)) and all(f(g(m)) == m for m in range(1, 400))
        check(agree and iso_ok and size_ok,
              f'{w:5s} type {name(o):6s} invariants {iv}; explicit order iso to canonical form and size match replayed')
        types.setdefault(o, []).append(w)
    inv_keys = {o: (inv(ws[0])['limits'], inv(ws[0])['tail']) for o, ws in types.items()}
    check(len(set(inv_keys.values())) == len(types) == 6,
          'the 6 order types are separated by the order invariants (number of limit kids, finite tail)')
    for o, ws in sorted(types.items()):
        say(f'   {name(o):6s}: {", ".join(ws)}')

    say('== Problem 2 (p. 2) ==')
    A, B, C = 'W', 'SW', 'WS'
    # Guide rule, B -> A: star -> 1, n -> n + 1.
    fB = lambda kid: 1 if kid[0] == 0 else kid[1] + 1
    gB = lambda m: (0, 1) if m == 1 else (1, m - 1)
    kb = kids(B, N)
    check(all(gB(fB(k)) == k for k in kb) and all(fB(gB(m)) == m for m in range(1, N + 1)),
          'A vs B: star -> 1, n -> n+1 is one-to-one and onto (replayed to n = %d)' % N)
    check(all(fB(kb[x]) < fB(kb[x + 1]) for x in range(len(kb) - 1)), 'A vs B: that rule keeps order')
    check(ordinal(A) == ordinal(B) == (1, 0), 'A and B both have type ω (1 + ω = ω)')
    # C -> A size match: star -> 1, n -> n + 1 (C's star is token 1).
    fC = lambda kid: 1 if kid[0] == 1 else kid[1] + 1
    gC = lambda m: (1, 1) if m == 1 else (0, m - 1)
    kc = kids(C, N)
    check(all(gC(fC(k)) == k for k in kc) and all(fC(gC(m)) == m for m in range(1, N + 1)),
          'A vs C: star -> 1, n -> n+1 is a complete match ignoring order')
    check(not all(fC(kc[x]) < fC(kc[x + 1]) for x in range(len(kc) - 1)),
          'A vs C: that rule breaks order (star is after numbered kid 1 in C, but its partner 1 is first in A)')
    check(inv(C)['last'] and not inv(A)['last'], 'A vs C: C has a last kid, A has none -> no order-keeping complete match')

    say('== Problem 3 (p. 3) ==')
    D = 'WW'  # red row, then blue row
    # E: R1 B1 R2 B2 ... ; position of Rn = 2n-1, Bn = 2n
    posE = lambda c, n: 2 * n - 1 if c == 'R' else 2 * n
    back = lambda m: ('R', (m + 1) // 2) if m % 2 else ('B', m // 2)
    dk = [('R', n) for n in range(1, N + 1)] + [('B', n) for n in range(1, N + 1)]
    check(all(back(posE(*k)) == k for k in dk) and all(posE(*back(m)) == m for m in range(1, 2 * N + 1)),
          'D vs E: namesake match is a complete match; positions in E are 2n-1 and 2n')
    check(posE('B', 1) < posE('R', 2), 'D vs E: namesake match breaks order (R2 before B1 in D; B1 at 2, R2 at 3 in E)')
    check(ordinal(D) == (2, 0) and inv(D)['limits'] == 1, 'D has type ω·2 = ω+ω; B1 is a limit kid (infinitely many predecessors, none immediately before it)')
    check(inv('W')['inf_pred'] == 'none',
          'E is one row by position (kid at position m has exactly m-1 predecessors), so no E kid has infinitely many')
    # No order-keeping match (not even one-to-one into E): if B1 went to position p,
    # R1 < ... < Rp < B1 would need p increasing positions below p.  Brute force:
    fits = [p for p in range(1, 13) if any(True for _ in combinations(range(1, p), p))]
    check(fits == [], 'for every target position p = 1..12 of B1 there is no increasing choice of places for R1..Rp below p '
          '(and in general p places are needed among p-1)')
    check(ordinal('W') == (1, 0), 'E (pairs continuing forever) has type 2·ω = ω')

    say('== Guide overview: ordinal vs surreal (natural) sum ==')
    nat = lambda x, y: (x[0] + y[0], x[1] + y[1])  # Hessenberg sum below ω^2
    one, w = (0, 1), (1, 0)
    check(ordinal('SW') == w and ordinal('WS') == (1, 1), 'ordinal: 1 + ω = ω, ω + 1 ≠ ω')
    check(nat(one, w) == nat(w, one) == (1, 1) != w,
          'natural (surreal) sum is commutative and 1 ⊕ ω = ω + 1 ≠ ω, so 1 + ω = ω does not transfer')

    say('== Problem 4 (p. 4) ==')
    same = [(x, y) for x, y in combinations(words, 2) if ordinal(x) == ordinal(y)]
    diff = [(x, y) for x, y in combinations(words, 2) if ordinal(x) != ordinal(y)]
    say(f'   pairs of different arrangements: {len(same) + len(diff)}; same type (order-keeping match): {len(same)}; '
        f'different type (match only if order may change): {len(diff)}')
    check(len(same) >= 2 and len(diff) >= 2, 'both requested kinds of pairs exist (every arrangement is countable)')
    omega_like = types[(1, 0)]
    say('   reading "each arrangement matched to one plain endless row": order-keeping ones are', omega_like)
    check(len(omega_like) >= 2, 'that reading also has at least two answers')
    check(('W', 'SW') in same or ('SW', 'W') in same, 'guide example: row alone vs star then row keeps order')
    check(('W', 'WS') in diff or ('WS', 'W') in diff, 'guide example: row alone vs row then star needs order change')

    say('   Panels needed (p. 6 prints 4 stars, 2 "this kid" panels, 2 "this whole row" panels):')

    def panels(word):
        kid = sum(1 for i in range(1, len(word)) if word[i] == 'S' and word[i - 1] == 'W')
        row = sum(1 for i in range(1, len(word)) if word[i] == 'W' and word[i - 1] == 'W')
        return kid, row
    single = max(panels(w)[0] for w in words), max(panels(w)[1] for w in words)
    say(f'   one arrangement needs at most {single[0]} kid panels and {single[1]} row panels')
    over = [(x, y) for x, y in same if panels(x)[0] + panels(y)[0] > 2 or panels(x)[1] + panels(y)[1] > 2]
    say('   same-type pairs that need more than the printed panels to lay out together:', over)
    return {'types': {name(o): ws for o, ws in types.items()}, 'same': len(same), 'diff': len(diff)}


def main():
    say('Week 82 independent math check; repository:', REPO.name)
    finite_part()
    infinite_part()
    say('')
    say(f'{len(FAIL)} failures')
    text = '\n'.join(OUT) + '\n'
    (HERE / 'check_math.py.out').write_text(text)
    print(text)
    raise SystemExit(1 if FAIL else 0)


if __name__ == '__main__':
    main()
