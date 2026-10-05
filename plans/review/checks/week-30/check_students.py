"""Solve every base student problem (K-1, Grades 2-3, Grades 4-5) and check
the printed diagrams against the text and the mathematics.

Uses extracted.json (run extract.py first; run automatically if missing).
Output: check_students.out
"""
import json
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, reachable, ways, run_length, first_miss, show_way, Log  # noqa: E402

L = Log('check_students.out')
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    import extract
    extract.main()
X = json.load(open(os.path.join(HERE, 'extracted.json')))


def items(band, prob, kind):
    out = []
    for pg in X[band]:
        for it in pg['items']:
            if it['problem'] == prob and it['kind'] == kind:
                out.append(dict(it, page=pg['page']))
    return out


def board_targets(band, prob):
    return [int(b['target'][0]) for b in items(band, prob, 'board')]


def strip_labels(band, prob):
    return [int(s['label'][0]) for s in items(band, prob, 'strip')]


def card_labels(band, prob):
    return [int(c['label'][0]) for c in items(band, prob, 'card')]


# ------------------------------------------------------------ all cards
L.out('== Weight cards: printed number equals dot count; dots clear of the border')
for band in ('K', '23', '45'):
    for pg in X[band]:
        for it in pg['items']:
            if it['kind'] == 'card':
                n = int(it['label'][0])
                L.ok(n == it['dots'], f"{band} p.{pg['page']} P{it['problem']} card {n}: {it['dots']} dots")
                if it['bottom_gap_pt'] is not None and it['bottom_gap_pt'] < 1.0:
                    L.out(f"WARN {band} p.{pg['page']} card {n}: lowest dot is {it['bottom_gap_pt']} pt "
                          f"from the card's bottom edge (dot diameter 3 pt, border 0.7 pt): it sits on the border")
            if it['kind'] == 'board':
                L.ok(it['right_pan'] and it['equals'] == 1 and it['target_word'],
                     f"{band} p.{pg['page']} P{it['problem']} board target {it['target']}: two pans, '=', 'target' label")

# ------------------------------------------------------------ launch example (all three bands)
L.out('\n== Launch example: target 3; weights 1 and 4; "put 1 beside the target"; 3 + 1 = 4')
for band in ('K', '23', '45'):
    b = items(band, 'launch', 'board')[0]
    t = int(b['target'][0])
    left = [int(d[0]) for d in b['left_disks']]
    right = [int(d[0]) for d in b['right_disks']]
    L.ok(t == 3 and left == [1] and right == [4] and t + sum(left) == sum(right),
         f'{band}: board shows {show_way(t, left, right)}; cards {card_labels(band, "launch")}')
L.out('   note: kit {1,4} with target 3 is also a task instance (K-1 P3, 2-3 P1), ways:', ways([1, 4], 3))

# ------------------------------------------------------------ K-1
L.out('\n== K-1')
# P1
kit = [1, 3]
L.ok(card_labels('K', 1) == kit, f'P1 cards {card_labels("K", 1)}')
for t in (1, 2, 3, 4):
    w = ways(kit, t)
    L.ok(len(w) >= 1, f'P1 target {t} with 1,3: ' + '; '.join(show_way(t, *x) for x in w))
L.ok(all(t in (1, 2, 3, 4) for t in board_targets('K', 1)), f'P1 boards {board_targets("K", 1)} are requested targets')
# P2
kit = [1, 2]
r = [t for t in range(1, 6) if t in reachable(kit)]
L.out(f'P2 kit 1,2 balances {r} of 1..5; strip {strip_labels("K", 2)}; boards {board_targets("K", 2)}')
L.ok(r == [1, 2, 3], 'P2 answer 1, 2, 3 (4 and 5 impossible: total is 3)')
L.out('   boards 4 and 5 are targets that cannot be balanced (consistent with "Which targets ... can you balance?")')
# P3
a = [t for t in range(1, 7) if t in reachable([1, 4])]
b = [t for t in range(1, 7) if t in reachable([1, 3])]
L.out(f'P3 kit 1,4 -> {a}; kit 1,3 -> {b}; strip {strip_labels("K", 3)}; cards {card_labels("K", 3)}')
L.ok(len(a) == len(b) == 4, 'P3 tie: each kit balances four of 1..6, so neither balances more')
for t in board_targets('K', 3):
    L.out(f'   board target {t}: kit 1,4 {"yes" if t in a else "no"}, kit 1,3 {"yes" if t in b else "no"}')
# P4
good = []
for k in combinations([1, 2, 3, 4], 2):
    rr = [t for t in range(1, 5) if t in reachable(list(k))]
    L.out(f'P4 kit {k}: balances {rr} of 1..4')
    if rr == [1, 2, 3, 4]:
        good.append(k)
L.ok(good == [(1, 3)], f'P4 only kit: {good}')
L.ok(card_labels('K', 4) == [1, 2, 3, 4], f'P4 cards {card_labels("K", 4)}')
# P5
res = {}
for w in (8, 9, 10):
    miss = [t for t in range(5, 14) if t not in reachable([1, 3, w])]
    res[w] = miss
    L.out(f'P5 kit 1,3,{w}: misses {miss} in 5..13')
L.ok([w for w in res if not res[w]] == [9], 'P5 unique answer 9')
L.ok(strip_labels('K', 5) == list(range(5, 14)), f'P5 strip {strip_labels("K", 5)}')
L.ok(card_labels('K', 5) == [1, 3, 8, 9, 10], f'P5 cards {card_labels("K", 5)}')
for t in board_targets('K', 5):
    L.out(f'   board {t} with 1,3,9: ' + '; '.join(show_way(t, *x) for x in ways([1, 3, 9], t)))

# ------------------------------------------------------------ Grades 2-3
L.out('\n== Grades 2-3')
labs = [it['text'] for it in items('23', 1, 'label')]
strips = strip_labels('23', 1)
L.ok(labs == ['1 and 2', '1 and 3', '1 and 4'] and strips == list(range(1, 7)) * 3,
     f'P1 three labelled rows {labs}, each with boxes 1..6')
for k in ([1, 2], [1, 3], [1, 4]):
    L.out(f'P1 kit {k}: balances {[t for t in range(1, 7) if t in reachable(k)]} of 1..6')
L.out(f'P1 board target {board_targets("23", 1)}: kits that balance 2: '
      f'{[k for k in ([1, 2], [1, 3], [1, 4]) if 2 in reachable(k)]}')
# P2
ok_w = [w for w in range(1, 200) if all(t in reachable([1, 3, w]) for t in range(1, 14))]
L.ok(ok_w == [9], f'P2 whole-number w in 1..199 completing 1..13: {ok_w}')
L.ok(strip_labels('23', 2) == list(range(1, 14)), f'P2 strip {strip_labels("23", 2)}')
for t in board_targets('23', 2):
    L.out(f'   board {t} with 1,3,9: ' + '; '.join(show_way(t, *x) for x in ways([1, 3, 9], t)))
# P3
fm = {w: first_miss([1, 3, w]) for w in (8, 9, 10)}
L.ok(fm == {8: 13, 9: 14, 10: 5}, f'P3 first target each kit cannot balance: {fm}')
L.ok([it['text'] for it in items('23', 3, 'label')] == ['1, 3, 8', '1, 3, 9', '1, 3, 10'], 'P3 kit labels')
# P4
w8 = ways([1, 3, 8], 4)
w9 = ways([1, 3, 9], 4)
L.out('P4 ways to balance 4 with 1,3,8: ' + '; '.join(show_way(4, *x) for x in w8))
L.out('P4 ways to balance 4 with 1,3,9: ' + '; '.join(show_way(4, *x) for x in w9))
bt = board_targets('23', 4)
L.ok(len(w8) == 2 and len(w9) == 1 and bt == [4, 4, 4],
     'P4 two ways / one way; boards printed: 2 under "1, 3, 8" and 1 under "1, 3, 9" (board count equals way count)')
# P5
L.out('P5 counting bound: 3^3 = 27 placements; 0 once; others pair by sign -> at most 13 positive targets')
best = max(len(reachable([a, b, c])) for a in range(1, 41) for b in range(a, 41) for c in range(b, 41))
L.ok(best == 13, f'P5 most distinct positive targets of any 3-weight kit with weights <= 40 (repeats allowed): {best}')
# P6
runs = {w: run_length([1, 3, 9, w]) for w in range(1, 120)}
m = max(runs.values())
L.ok(m == 40 and [w for w in runs if runs[w] == m] == [27],
     f'P6 best fourth weight: {[w for w in runs if runs[w] == m]} with run 1..{m}; '
     f'neighbours: w=26 -> {runs[26]}, w=28 -> {runs[28]}')

# ------------------------------------------------------------ Grades 4-5
L.out('\n== Grades 4-5')
kits = [(a, b) for a in range(1, 60) for b in range(a + 1, 60)
        if all(t in reachable([a, b]) for t in range(1, 5))]
L.ok(kits == [(1, 3)], f'P1 two different weights (each < 60) covering 1..4: {kits}')
L.out(f'   boards {board_targets("45", 1)} with 1,3: ' +
      '; '.join(show_way(t, *ways([1, 3], t)[0]) for t in board_targets('45', 1)))
runs = {w: run_length([1, 3, w]) for w in range(1, 100)}
m = max(runs.values())
L.ok(m == 13 and [w for w in runs if runs[w] == m] == [9], f'P2 best w {[w for w in runs if runs[w] == m]}, run {m}')
L.out('   runs by w: ' + ', '.join(f'{w}:{runs[w]}' for w in range(1, 16)))
L.ok(strip_labels('45', 2) == list(range(1, 16)), f'P2 strip {strip_labels("45", 2)}')
# P3
dup = {t: len(ways([1, 3, 9], t)) for t in reachable([1, 3, 9])}
L.ok(set(dup.values()) == {1} and sorted(dup) == list(range(1, 14)),
     f'P3 1,3,9 balances {min(dup)}..{max(dup)}, each in exactly one way')
for t in board_targets('45', 3):
    L.out(f'   board {t}: ' + '; '.join(show_way(t, *x) for x in ways([1, 3, 9], t)))
# P4 (bound) and P5 (max count among three different weights)
best = {}
for a in range(1, 61):
    for b in range(a + 1, 61):
        for c in range(b + 1, 61):
            n = len(reachable([a, b, c]))
            best.setdefault(n, []).append((a, b, c))
top = max(best)
L.ok(top == 13, f'P4/P5 most distinct positive targets, three different weights <= 60: {top} '
     f'({len(best[13])} kits reach 13, e.g. {best[13][:4]})')
L.ok(not any(all(t in reachable(k) for t in range(1, 15)) for n in best for k in best[n]),
     'P4 no three-weight kit (<= 60) covers 1..14')
# P6
runs = {w: run_length([1, 3, 9, w]) for w in range(1, 120)}
uniq27 = all(len(ways([1, 3, 9, 27], t)) == 1 for t in range(1, 41))
L.ok([w for w in runs if runs[w] == 40] == [27] and uniq27, 'P6 add 27: run 1..40, every target in exactly one way')
# P7
kit = [1, 3, 9, 27, 81]
L.ok(run_length(kit) == 121 and all(len(ways(kit, t)) == 1 for t in range(1, 122)) and (3 ** 5 - 1) // 2 == 121,
     'P7 1,3,9,27,81 reaches 1..121 uniquely; bound (3^5-1)/2 = 121')
# Is the five-weight kit reaching 121 unique?  Necessarily all 243 values distinct and = -121..121.
# Search kits sorted a<=b<=c<=d<=e with e <= 121 using greedy necessity: run needs w1=1 etc. (prune by run)
found = []


def extend(kit, maxw):
    if len(kit) == 5:
        if run_length(kit) >= 121:
            found.append(tuple(kit))
        return
    r = run_length(kit) if kit else 0
    # a new weight w larger than 2r+1 leaves r+1 unreachable forever only if later weights are larger;
    # we keep weights sorted, so w <= 2r+1 is necessary for target r+1 (later weights are even larger).
    lo = kit[-1] if kit else 1
    for w in range(lo, min(2 * r + 1, maxw) + 1):
        extend(kit + [w], maxw)


extend([], 121)
L.ok(found == [(1, 3, 9, 27, 81)], f'P7 five-weight kits reaching 121 (sorted search): {found}')
L.save()
