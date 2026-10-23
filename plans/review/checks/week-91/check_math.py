#!/usr/bin/env python3
"""Independent mathematical checks for Week 91 (Rotor-router machines).

Written for the math-check stage of the review. It does not import or run the
package's own check_math.py. Standard library only.

Model (the packet's convention): every switch shows the NEXT exit. A counter
follows the arrow, then that card flips. One counter finishes before the next
enters; cards persist between counters. Trees are complete binary trees whose
switches are listed by levels (root, then left to right). Roads are paths
0..m with absorbing endpoints; card words list interior vertices 1..m-1.

What it checks
- One switch: every 12-counter run, the four printed strings of students P1,
  and the coin comparison of P7 (all 64 length-6 words).
- Four-exit tree (students P2, P3; guide tables): all 8 states, every
  arrival order, D-first starts, the four printed targets, the guide's full
  key and its card-word convention.
- Eight-exit tree (students P4, P5, P6): all 128 states, the three printed
  targets, uniqueness of the start for each achievable order, the guide's
  witnesses ABCDEFGH and AEDFBGCH, and block/return claims for depths 1-4
  (depth 4 = 32768 states) over several consecutive blocks.
- Roads (return packet P1-P6; guide overview and keys): every state and every
  interior entry for m = 2..10; termination, the conserved score on every
  step, exact s right exits in every window of m consecutive launches, the
  printed traces (example road, P1, the P4 example), all-left words of P2 and
  P3, the guide's tables, and whether the state after one block always equals
  the state after two blocks.

Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from itertools import product, permutations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
OUT, FAIL = [], []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('PASS  ' if cond else 'FAIL  ') + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- trees
def tree_run(state, n, depth):
    """state: tuple of 'L'/'R' over 2**depth-1 switches in level order.
    Returns (leaf letters in arrival order, final state)."""
    st = list(state)
    out = []
    letters = 'ABCDEFGHIJKLMNOP'
    for _ in range(n):
        node = 0  # level-order index
        for _lvl in range(depth):
            d = st[node]
            st[node] = 'R' if d == 'L' else 'L'
            node = 2 * node + (1 if d == 'L' else 2)
        leaf = node - (2 ** depth - 1)
        out.append(letters[leaf])
    return ''.join(out), tuple(st)


def all_states(k):
    return [tuple(p) for p in product('LR', repeat=k)]


def tree_section():
    say('== One switch (depth 1) ==')
    xy = {'A': 'X', 'B': 'Y'}
    runs = {}
    for s in all_states(1):
        w, f = tree_run(s, 12, 1)
        runs[s[0]] = ''.join(xy[c] for c in w)
        say(f'  first arrow {s[0]}: {runs[s[0]]}, final card {f[0]}')
    check(set(runs.values()) == {'XYXYXYXYXYXY', 'YXYXYXYXYXYX'},
          'students P1 / guide: 12 counters give XYXY... or YXYX...')
    # every word of length 4 the switch can make, from any state, anywhere in a run
    can4 = set()
    for r in runs.values():
        for i in range(len(r) - 3):
            can4.add(r[i:i + 4])
    for w, exp in [('XYXY', True), ('XXYY', False), ('YXYX', True), ('XYYX', False)]:
        check((w in can4) == exp, f'students P1: {w} {"can" if exp else "cannot"} be made')
    # discrepancy never exceeds one
    ok = True
    for s in all_states(1):
        w, _ = tree_run(s, 40, 1)
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                seg = w[i:j]
                if abs(seg.count('A') - seg.count('B')) > 1:
                    ok = False
    check(ok, 'guide overview: any consecutive n visits to one switch differ by at most one (n <= 40)')
    # P7 coin vs switch
    sw6 = set()
    for r in runs.values():
        for i in range(len(r) - 5):
            sw6.add(r[i:i + 6])
    coin6 = {''.join(p) for p in product('XY', repeat=6)}
    say(f'  switch can make {sorted(sw6)} as six-counter words; coin can make {len(coin6)}')
    check(sw6 <= coin6 and len(coin6 - sw6) == 62 and 'XXXXXX' in coin6 - sw6,
          'students P7 / guide: coin makes all 64 words incl. XXXXXX; switch only 2; coin covers switch')
    check(abs(1 / 64 - 1 / len(coin6)) < 1e-15, 'guide: each length-6 coin word has probability 1/64')

    say('')
    say('== Four-exit tree (depth 2); card words: root, left child, right child ==')
    key = {}
    for s in all_states(3):
        w8, f8 = tree_run(s, 8, 2)
        w4, f4 = tree_run(s, 4, 2)
        key[''.join(s)] = w4
        say(f'  {"".join(s)}: first four {w4}, eight {w8}, cards after four {"".join(f4)}')
        check(w8 == w4 + w4 and f4 == s, f'{"".join(s)} repeats after four and cards return')
    guide_key = dict(zip(['LLL', 'LLR', 'LRL', 'LRR', 'RLL', 'RLR', 'RRL', 'RRR'],
                         ['ACBD', 'ADBC', 'BCAD', 'BDAC', 'CADB', 'DACB', 'CBDA', 'DBCA']))
    check(key == guide_key, 'guide P3 adult key: all eight words in the stated card order')
    dfirst = {s: w for s, w in key.items() if w[0] == 'D'}
    check(set(dfirst) == {'RLR', 'RRR'}, 'guide P2: D first iff root R and right child R (left free): RLR, RRR')
    check(dfirst == {'RLR': 'DACB', 'RRR': 'DBCA'}, 'guide P2 table: RLR -> DACB DACB, RRR -> DBCA DBCA')
    say(f'  students P2: every D-first eight-counter order: {sorted(w + w for w in dfirst.values())} '
        f'(two strips are printed)')
    achievable = set(key.values())
    for t, exp, start in [('ACBD', True, 'LLL'), ('BDAC', True, 'LRR'), ('ABCD', False, None), ('DABC', False, None)]:
        check((t in achievable) == exp, f'students P3: {t} {"possible" if exp else "impossible"}')
        if start:
            check(key[start] == t, f'guide P3: {t} from {start}')
    # guide's reason for DABC: counters 2 and 3 both in the left half
    check(all(not (w[1] in 'AB' and w[2] in 'AB') for w in achievable),
          'guide P3: two consecutive outputs never share a root half (kills ABCD at 1-2 and DABC at 2-3)')
    perms4 = {''.join(p) for p in permutations('ABCD')}
    say(f'  four-exit tree makes {len(achievable)} of {len(perms4)} orders of A-D')

    say('')
    say('== Eight-exit tree (depth 3); seven cards by levels ==')
    words = {}
    for s in all_states(7):
        w, f = tree_run(s, 8, 3)
        words.setdefault(w, []).append(''.join(s))
    ret = all(tree_run(s, 8, 3)[1] == s for s in all_states(7))
    check(ret, 'students P6 / guide: all 128 starts return every card after eight counters')
    once = all(sorted(tree_run(s, 8, 3)[0]) == list('ABCDEFGH') for s in all_states(7))
    check(once, 'students P6 / guide: eight counters reach every exit exactly once, all 128 starts')
    check(len(words) == 128 and all(len(v) == 1 for v in words.values()),
          'guide P4: each achievable eight-letter order comes from exactly one start (128 distinct orders)')
    check(words.get('AECGBFDH') == ['LLLLLLL'], 'guide P4: AECGBFDH from all seven L')
    check(words.get('HDFBGCEA') == ['RRRRRRR'], 'guide P4: HDFBGCEA from all seven R')
    check('AEBFCGDH' not in words, 'guide P4: AEBFCGDH impossible')
    w = 'AEBFCGDH'
    left = [c for c in w if c in 'ABCD']
    rootalt = all((w[i] in 'ABCD') != (w[i + 1] in 'ABCD') for i in range(7))
    check(rootalt and left[:2] == ['A', 'B'], 'guide P4: AEBFCGDH alternates at the root; left subtree gets A,B first')
    for wit in ['ABCDEFGH', 'AEDFBGCH']:
        check(wit not in words and sorted(wit) == list('ABCDEFGH'), f'guide P5 witness {wit} visits each exit once and is impossible')
    lsub = [c for c in 'AEDFBGCH' if c in 'ABCD']
    check(''.join(lsub) == 'ADBC' and 'ADBC' in achievable, 'guide P5: AEDFBGCH left subtree order A,D,B,C is legal')
    say(f'  eight-exit tree makes {len(words)} of 40320 orders of A-H')

    say('')
    say('== Complete trees, depths 1-4: blocks of 2^d from every state, three consecutive blocks ==')
    for d in range(1, 5):
        n = 2 ** d
        ok_once = ok_ret = True
        for s in all_states(2 ** d - 1):
            st = s
            for _b in range(3):
                w, f = tree_run(st, n, d)
                if sorted(w) != sorted('ABCDEFGHIJKLMNOP'[:n]):
                    ok_once = False
                if f != st:
                    ok_ret = False
                st = f
            # sliding windows: any n consecutive counters (not only aligned)
            w3, _ = tree_run(s, 3 * n, d)
            for i in range(2 * n + 1):
                if len(set(w3[i:i + n])) != n:
                    ok_once = False
        check(ok_once and ok_ret, f'depth {d}: every window of {n} consecutive counters hits each leaf once; cards return ({2 ** (2 ** d - 1)} states)')
    # unequal-depth counterexample exists
    # tree: root -> leaf P on left, switch on right with leaves Q, R ; block of 3 or 4?
    def uneq(state, n):
        st = list(state); out = []
        for _ in range(n):
            d = st[0]; st[0] = 'R' if d == 'L' else 'L'
            if d == 'L':
                out.append('P')
            else:
                e = st[1]; st[1] = 'R' if e == 'L' else 'L'
                out.append('Q' if e == 'L' else 'R')
        return ''.join(out)
    bad = [s for s in all_states(2) if len(set(uneq(s, 3))) < 3]
    check(len(bad) > 0, f'guide: unequal-depth tree fails the once-each block (e.g. start {"".join(bad[0])}: {uneq(bad[0], 3)})')


# ---------------------------------------------------------------- roads
def road_walk(state, m, s, check_score=None):
    """One counter from interior s. state: list over 1..m-1 of 'L'/'R'
    (index v-1). Returns (exit, steps). Mutates state."""
    pos = s
    steps = 0
    while 0 < pos < m:
        if check_score is not None:
            score = pos + sum(1 for c in state if c == 'R')
            if score != check_score:
                raise AssertionError('score changed')
        d = state[pos - 1]
        state[pos - 1] = 'R' if d == 'L' else 'L'
        pos += 1 if d == 'R' else -1
        steps += 1
        if steps > 10 ** 6:
            raise AssertionError('no exit')
    return pos, steps


def road_run(state, m, s, n):
    st = list(state)
    exits = []
    for _ in range(n):
        e, _ = road_walk(st, m, s)
        exits.append(e)
    return exits, ''.join(st)


def trace(state, m, s):
    """Full step trace of one counter: list of (pos, cards) after each step."""
    st = list(state); pos = s; rows = [(pos, ''.join(st))]
    while 0 < pos < m:
        d = st[pos - 1]; st[pos - 1] = 'R' if d == 'L' else 'L'
        pos += 1 if d == 'R' else -1
        rows.append((pos, ''.join(st)))
    return rows


def road_section():
    say('')
    say('== Return packet example road 0-3, entry 2, cards R,L ==')
    rows = trace('RL', 3, 2)
    say('  ' + ' -> '.join(f'{p}:{c}' for p, c in rows))
    check(rows == [(2, 'RL'), (1, 'RR'), (2, 'LR'), (3, 'LL')],
          'example: 2->1 (R,R), 1->2 (L,R), 2->3 (L,L); exit 3 with cards L,L')
    scores = [p + c.count('R') for p, c in rows]
    check(scores == [3, 3, 3, 3] and [c.count('R') for _, c in rows] == [1, 2, 1, 0],
          'guide P5 score table: right cards 1,2,1,0 and total score 3 at every stage')

    say('')
    say('== Return P1 / guide P1 / P4: road 0-4, entry 1, start LLR ==')
    st = list('LLR'); ex = []; after = []
    for i in range(12):
        e, _ = road_walk(st, 4, 1)
        ex.append(e); after.append(''.join(st))
    say(f'  exits {ex}')
    say(f'  cards after each counter {after}')
    check(ex[:8] == [0, 0, 4, 0, 0, 0, 4, 0], 'P1: eight counters exit 0,0,4,0,0,0,4,0')
    check(ex[8:12] == [0, 0, 4, 0], 'P1: next four exit 0,0,4,0')
    check(after[:4] == ['RLR', 'RRR', 'LLL', 'RLL'], 'guide P1 trace table: RLR, RRR, LLL, RLL')
    check(after[3] == 'RLL' and after[7] == 'RLL', 'guide P1/P4: cards RLL after four and after eight')
    blk = ''.join(map(str, ex[:4]))
    say(f'  first output block written as a word: {blk}')
    blk2 = ''.join(map(str, ex[4:8]))
    check(blk == blk2 == '0040', 'P4 example: both output blocks are the word 0040')
    say("  FINDING: the guide's Problem 4 says 'The first two output blocks are both 0004'; the word is 0040 "
        "(0004 is the all-left entry-1 word of Problem 2)")

    say('')
    say('== Return P2: road 0-4, entries 1,2,3 ==')
    exp_words = {1: '0004', 2: '0404', 3: '0444'}
    for s in (1, 2, 3):
        ex, _ = road_run('LLL', 4, s, 8)
        w = ''.join('0' if e == 0 else '4' for e in ex)
        say(f'  entry {s}, all-left: {w}')
        check(w == exp_words[s] * 2, f'guide P2: entry {s} all-left first four {exp_words[s]}, repeated')
        rights = {sum(1 for e in road_run(st, 4, s, 8)[0] if e == 4) for st in all_states(3)}
        check(rights == {2 * s}, f'guide P2: eight counters from entry {s} give {2 * s} right, {8 - 2 * s} left, for all 8 starts')
        orders = {tuple(road_run(st, 4, s, 8)[0]) for st in all_states(3)}
        say(f'    distinct eight-exit orders over all starts: {len(orders)}')

    say('')
    say('== Return P3: road 0-5, entries 1,2,4 (and 3) ==')
    exp5 = {1: '00005', 2: '00505', 4: '05555'}
    for s in (1, 2, 3, 4):
        rights = {sum(1 for e in road_run(st, 5, s, 5)[0] if e == 5) for st in all_states(4)}
        check(rights == {s}, f'P3: five launches from entry {s}: exactly {s} at 5 for all 16 starts (so never all five)')
        w = ''.join('0' if e == 0 else '5' for e in road_run('LLLL', 5, s, 5)[0])
        if s in exp5:
            check(w == exp5[s], f'guide P3: entry {s} all-left word {exp5[s]} (got {w})')
        else:
            say(f'  entry 3 all-left word {w}')

    say('')
    say('== All roads m = 2..10, every state, every interior entry ==')
    walks = steps_checked = 0
    ok_term = ok_score = ok_block = ok_win = True
    block1_eq_block2 = True
    crit_ok = True
    transient_examples = 0
    worst_steps = 0
    for m in range(2, 11):
        for s in range(1, m):
            for state in product('LR', repeat=m - 1):
                st = list(state)
                exits = []
                states_at = [''.join(st)]
                for k in range(3 * m):
                    sc = s + st.count('R')
                    try:
                        e, n = road_walk(st, m, s, check_score=sc)
                    except AssertionError as err:
                        if 'score' in str(err):
                            ok_score = False
                        else:
                            ok_term = False
                        break
                    walks += 1
                    steps_checked += n
                    worst_steps = max(worst_steps, n)
                    if (e + st.count('R')) != sc:
                        ok_score = False
                    exits.append(e)
                    states_at.append(''.join(st))
                # aligned blocks and every sliding window of m launches
                for i in range(0, 2 * m + 1):
                    if sum(1 for e in exits[i:i + m] if e == m) != s:
                        ok_win = False
                for b in range(3):
                    if sum(1 for e in exits[b * m:(b + 1) * m] if e == m) != s:
                        ok_block = False
                # identity mR + S_final = ns + S_initial at every n
                S0 = states_at[0].count('R')
                for n in range(len(exits) + 1):
                    R = sum(1 for e in exits[:n] if e == m)
                    if m * R + states_at[n].count('R') != n * s + S0:
                        ok_score = False
                if states_at[m] != states_at[2 * m] or states_at[2 * m] != states_at[3 * m]:
                    block1_eq_block2 = False
                if states_at[0] != states_at[m]:
                    transient_examples += 1
                # criterion: the start changes over a block iff its word has an L
                # immediately followed by an R (a two-card loop in last-exit terms)
                has_LR = 'LR' in states_at[0]
                if has_LR != (states_at[0] != states_at[m]):
                    crit_ok = False
                if 'LR' in states_at[m]:
                    crit_ok = False
    check(ok_term, 'every counter exits (all roads m<=10, all states, all entries, 3m counters each)')
    check(ok_score, 'position + right cards is unchanged by every step; mR + S_final = ns + S_initial at every n')
    check(ok_block and ok_win, 'every window of m consecutive launches has exactly s right exits (no burn-in)')
    check(block1_eq_block2, 'state after one block of m always equals the state after two and three blocks')
    check(crit_ok, 'the cards change over a block exactly when the start has L immediately before R; '
          'after one block the word is always R...RL...L (no LR)')
    say(f'  {walks} walks, {steps_checked} steps; longest single walk {worst_steps} steps')
    say(f'  (state, entry) cases whose state after one block differs from the start: {transient_examples}')

    say('')
    say('== Guide P4 and the student question: which starts change at a block boundary? ==')
    for m in (4, 5):
        for s in range(1, m):
            changed = [''.join(st) for st in product('LR', repeat=m - 1)
                       if road_run(st, m, s, m)[1] != ''.join(st)]
            say(f'  road 0-{m}, entry {s}: {len(changed)} of {2 ** (m - 1)} starts change over the first block')
    # block sizes other than m on printed roads: do equal-count blocks ever come with perpetual change?
    found = []
    for m in (4, 5):
        for s in range(1, m):
            for b in range(1, 2 * m + 1):
                for st in product('LR', repeat=m - 1):
                    ex, _ = road_run(st, m, s, 6 * b)
                    counts = [sum(1 for e in ex[k * b:(k + 1) * b] if e == m) for k in range(6)]
                    if len(set(counts)) == 1:
                        # after the first block, does the state keep changing at boundaries?
                        cur = list(st)
                        bstates = []
                        for k in range(6):
                            for _ in range(b):
                                road_walk(cur, m, s)
                            bstates.append(''.join(cur))
                        if len(set(bstates[1:])) > 1:
                            found.append((m, s, b, ''.join(st)))
    check(not found, 'printed roads: whenever block counts repeat, the state stops changing after the first block '
          f'(any block size 1..2m){"" if not found else " counterexamples " + str(found[:5])}')


def main():
    tree_section()
    road_section()
    say('')
    say(f'{len(FAIL)} failure(s)')
    for f in FAIL:
        say('  ' + f)
    (HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
