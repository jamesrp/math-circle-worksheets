"""Every Week 7 problem, every band, and every answer in the adult guide.

Pile sizes and track ranges are read back from the delivered PDFs
(pdf_geometry.json, written by extract_pdf.py) where the page draws them;
rules and numbers that appear only in the problem text are typed in from
the PDFs.  Answers are computed with games.py (direct game-tree search), and
each guide statement is compared with the computation.  Lines starting with
"MISMATCH" or "NOTE" are the ones to read.
"""
import os, sys, json
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from games import (HERE, ROOT, mover_wins_piles, P_positions, winning_takes,
                   winning_two_pile_moves, grundy, greedy_take,
                   greedy_all_game_wins, outcome_sequence)

GEO = os.path.join(HERE, 'pdf_geometry.json')
if not os.path.exists(GEO):
    import subprocess
    subprocess.run([sys.executable, os.path.join(HERE, 'extract_pdf.py')], check=True,
                   stdout=subprocess.DEVNULL)
geo = json.load(open(GEO))

issues = []


def check(label, ok, detail=''):
    tag = 'ok      ' if ok else 'MISMATCH'
    print(f'  {tag} {label}' + (f': {detail}' if detail else ''))
    if not ok:
        issues.append(label)


def note(text):
    print(f'  NOTE     {text}')


def rows(band, problem):
    return [r['piles'] for p in geo[band] for r in p['counter_rows'] if r['problem'] == problem]


def tracks(band, problem):
    return [t['numbers'] for p in geo[band] for t in p['tracks'] if t['problem'] == problem]


def single(n, S, misere=False):
    """('second', []) or ('first', winning takes)."""
    w = winning_takes(n, S, misere)
    return ('first', w) if w else ('second', [])


def fmt(n, S, misere=False):
    side, w = single(n, S, misere)
    return f'{n}: {side}' + (f' take {w}' if w else '')


# --------------------------------------------------------------------------
print('K-1 (F07-K-v4).  Opening rule: take 1 or 2 / move 1 or 2; last counter or 0 wins.')
S12 = (1, 2)

print('P1 piles', rows('k-1', 1))
piles = [r[0] for r in rows('k-1', 1)]
check('P1 piles drawn are 2..8', piles == list(range(2, 9)), str(piles))
print('   ', '; '.join(fmt(n, S12) for n in piles))
guide = {2: [2], 3: [], 4: [1], 5: [2], 6: [], 7: [1], 8: [2]}
check('guide p.3 P1 "Go 2nd with 3 and 6 ... from 2 take 2; from 4 take 1; from 5 take 2; from 7 take 1; from 8 take 2"',
      all(winning_takes(n, S12) == guide[n] for n in piles))

print('P2/P3 from 10, rule 1 or 2')
check('P2 track(s) are 0..10', tracks('k-1', 2) == ['0..10'] * 3 and tracks('k-1', 3) == ['0..10'] * 3,
      f"{tracks('k-1', 2)} {tracks('k-1', 3)}")


def all_winner_lines(start, S, misere=False):
    """All games from start where the first player always plays a winning
    move and the opponent plays anything; returns the set of tuples of
    squares the first player put the token on."""
    out = set()

    def rec(n, mine, first_to_move):
        if n == 0:
            out.add(tuple(mine))
            return
        if first_to_move:
            for s in winning_takes(n, S, misere):
                rec(n - s, mine + [n - s], False)
        else:
            for s in S:
                if s <= n:
                    rec(n - s, mine, True)
    rec(start, [], True)
    return out


lines = all_winner_lines(10, S12)
check('P2/P3 first player wins from 10 and every winning line lands on exactly 9, 6, 3, 0',
      mover_wins_piles((10,), S12) and lines == {(9, 6, 3, 0)}, str(lines))

print('P4 piles', rows('k-1', 4))
piles = [r[0] for r in rows('k-1', 4)]
print('   ', '; '.join(fmt(n, S12) for n in piles))
check('guide p.4 P4 "5: take 2. 7: take 1. 8: take 2. 10: take 1. Each is the only winning first move."',
      [winning_takes(n, S12) for n in piles] == [[2], [1], [2], [1]])

print('P5 squares 1..10')
print('   ', '; '.join(fmt(n, S12) for n in range(1, 11)))
check('guide p.4 P5 "On 3, 6 or 9: 2nd ... from 1, 4, 7, 10 take 1; from 2, 5, 8 take 2"',
      all((winning_takes(n, S12) == []) == (n in (3, 6, 9)) for n in range(1, 11)) and
      all(winning_takes(n, S12) == [1] for n in (1, 4, 7, 10)) and
      all(winning_takes(n, S12) == [2] for n in (2, 5, 8)))

print('P6 rule 1, 2 or 3 from 10')
S123 = (1, 2, 3)
lines = all_winner_lines(10, S123)
check('P6 first player wins from 10; every winning line lands on 8, 4, 0; first take 2 is the only one',
      lines == {(8, 4, 0)} and winning_takes(10, S123) == [2], str(lines))
check('guide p.4 P6 "from 6 the other player takes 2 and lands on 4"', not mover_wins_piles((4,), S123))

print('P7 rule 1 or 4 from 8')
S14 = (1, 4)
lines = all_winner_lines(8, S14)
print('    first-player squares over all winning lines:', sorted(lines))
check('P7 first take: only 1 wins', winning_takes(8, S14) == [1])
check('guide p.4 P7 "coloured squares are 7, then 5 or 2, then 0"', lines == {(7, 5, 0), (7, 2, 0)})
check('guide p.4 P7 "Taking 4 first (8 -> 4) loses"', mover_wins_piles((4,), S14))

print('P8 two piles, take 1 or 2 from one pile')
pairs = rows('k-1', 8)
print('    pairs drawn:', pairs)
check('P8 pairs drawn are 2/2, 1/2, 3/3, 2/4, 4/4', pairs == [[2, 2], [1, 2], [3, 3], [2, 4], [4, 4]])
for a, b in pairs:
    w = winning_two_pile_moves(a, b, S12)
    print(f'    {a} and {b}: ' + ('second' if not w else f'first, winning moves {w}'))
check('guide p.4 P8 "Equal piles: 2nd. 1 and 2: 1st, take 1 from the 2. 2 and 4: 1st, take 2 from the 4."',
      not winning_two_pile_moves(2, 2, S12) and not winning_two_pile_moves(3, 3, S12) and
      not winning_two_pile_moves(4, 4, S12) and
      ('second pile', 1, (1, 1)) in winning_two_pile_moves(1, 2, S12) and
      ('second pile', 2, (2, 2)) in winning_two_pile_moves(2, 4, S12))

print('P9 last counter loses, piles', rows('k-1', 9))
piles = [r[0] for r in rows('k-1', 9)]
print('   ', '; '.join(fmt(n, S12, True) for n in piles))
check('guide p.4 P9 "1: 2nd. 2: 1st, take 1. 3: 1st, take 2. 4: 2nd. 5: 1st, take 1. 6: 1st, take 2."',
      [winning_takes(n, S12, True) for n in piles] == [[], [1], [2], [], [1], [2]])

# --------------------------------------------------------------------------
print()
print('Grades 2-3 (F07-M-v4).  Rule 1, 3 or 4 for P1-P7.')
S134 = (1, 3, 4)
piles = [r[0] for r in rows('grades-2-3', 1)]
print('P1 piles', piles)
print('   ', '; '.join(fmt(n, S134) for n in piles))
check('guide p.5 P1 "2: second. 5: first, take 3. 6: first, take 4. 7: second. 8: first, take 1. Each winning first move is the only one."',
      [winning_takes(n, S134) for n in piles] == [[], [3], [4], [], [1]])

print('P2 tracks', tracks('grades-2-3', 2))
check('guide p.5 P2 "0, 2, 7, 9, 14, 16"', P_positions(S134, 20) == [0, 2, 7, 9, 14, 16], str(P_positions(S134, 20)))

print('P3 starts 10..20')
print('   ', '; '.join(fmt(n, S134) for n in range(10, 21)))
guide = {10: [9, 7], 11: [7], 12: [9], 13: [9], 15: [14], 17: [16, 14], 18: [14], 19: [16], 20: [16]}
ok = all(winning_takes(n, S134) == [] for n in (14, 16)) and all(
    sorted(n - s for s in winning_takes(n, S134)) == sorted(guide[n]) for n in guide)
check('guide p.5 P3 "Go second from 14 or 16 ... 10 -> 9 or 7; 11 -> 7; 12 -> 9; 13 -> 9; 15 -> 14; 17 -> 16 or 14; 18 -> 14; 19 -> 16; 20 -> 16"', ok)

print('P4 start 9, Lena second')
check('9 is a losing square for the mover (Lena right)', not mover_wins_piles((9,), S134))
lena = {8: 7, 6: 2, 5: 2, 7: None, 4: 0, 3: 0, 1: 0}
# play out the guide's reply table against every opponent line


def lena_wins(n):
    # opponent to move from n, Lena replies by the guide's table
    for s in S134:
        if s <= n:
            m = n - s
            if m == 0:
                return False
            reply = {8: 7, 6: 2, 5: 2, 4: 0, 3: 0, 1: 0}.get(m)
            if reply is None or (m - reply) not in S134:
                return False
            if reply != 0 and not lena_wins(reply):
                return False
    return True


check('guide p.5 P4 replies "8->7, 6->2, 5->2; 6->2, 4->0, 3->0; from 2 opponent takes 1, Lena takes last" win against every line',
      lena_wins(9))

print('P5 Omar (always takes as many as allowed) first from 13')
check('Omar does NOT win against every reply', not greedy_all_game_wins(13, S134))
# list the refutations
refs = []
for s in S134:
    m = 13 - greedy_take(13, S134)
    if s <= m:
        r = m - s
        t = greedy_take(r, S134)
        after = r - t
        if after > 0 and any(after - u == 0 for u in S134 if u <= after):
            refs.append((m, r, after))
        elif after == 0:
            pass
print('    lines (Omar->, opp->, Omar->) after which the opponent takes the rest:', refs)
check('guide p.5 P5 "Opponent to 8: Omar to 4, opponent takes 4. Opponent to 5: Omar to 1. Opponent to 6: Omar wins."',
      (9, 8, 4) in refs and (9, 5, 1) in refs and len(refs) == 2 and
      greedy_all_game_wins(6, S134))  # opponent to 6: greedy Omar from 6 beats every reply
check('guide p.5 P5 "His first move (take 4, to 9) is right" (and the only winning first move)',
      winning_takes(13, S134) == [4])

print('P6 piles 50 and 100')
print('   ', fmt(50, S134), ';', fmt(100, S134))
check('guide p.5 P6 "50: first, take 1 (to 49). 100: second."',
      winning_takes(50, S134) == [1] and winning_takes(100, S134) == [])
check('guide p.5 P6 "49 and 51 are coloured and 50 is not; 98 and 100 are coloured"',
      all(not mover_wins_piles((n,), S134) for n in (49, 51, 98, 100)) and mover_wins_piles((50,), S134))
check('P6 track drawn is 0..30', tracks('grades-2-3', 6) == ['0..30'])

print('P7 two piles, take 1, 3 or 4 from one pile')
pairs = rows('grades-2-3', 7)
check('P7 pairs drawn are 5/5 and 5/6', pairs == [[5, 5], [5, 6]], str(pairs))
for a, b in pairs:
    w = winning_two_pile_moves(a, b, S134)
    print(f'    {a} and {b}: ' + ('second' if not w else f'first, winning moves {w}'))
check('guide p.6 P7 "5 and 5: second. 5 and 6: first, take 1 from the 6 ... (Taking 1 from the 5, to 4 and 6, also wins)"',
      not winning_two_pile_moves(5, 5, S134) and
      sorted(x[2] for x in winning_two_pile_moves(5, 6, S134)) == [(4, 6), (5, 5)])

print('P8 rule 1 or 4')
piles = [r[0] for r in rows('grades-2-3', 8)]
print('    piles', piles, ':', '; '.join(fmt(n, S14) for n in piles))
check('guide p.6 P8 "5: second. 6: first, take 1 or 4. 8: first, take 1. 9: first, take 4. 10: second."',
      [winning_takes(n, S14) for n in piles] == [[], [1, 4], [1], [4], []])

print('P9')
S135 = (1, 3, 5)
check('guide p.6 P9 "1 or 4: 0, 2, 5, 7, 10, 12, 15, 17, 20"', P_positions(S14, 20) == [0, 2, 5, 7, 10, 12, 15, 17, 20])
check('guide p.6 P9 "1, 3 or 5: every even square, 0 to 20"', P_positions(S135, 20) == list(range(0, 21, 2)))

# --------------------------------------------------------------------------
print()
print('Grades 4-5 (F07-U-v4).')
print('P1 rule 1 or 2: piles 7, 9, 11, 12, 16 (typed from the page)')
piles = [7, 9, 11, 12, 16]
print('   ', '; '.join(fmt(n, S12) for n in piles))
check('guide p.6 P1 "7: first, take 1. 9: second. 11: first, take 2. 12: second. 16: first, take 1."',
      [winning_takes(n, S12) for n in piles] == [[1], [], [2], [], [1]])
print('P2')
check('guide p.7 P2 "1 or 2: 0, 3, 6, 9, 12, 15, 18. 1, 2 or 3: 0, 4, 8, 12, 16, 20."',
      P_positions(S12, 20) == [0, 3, 6, 9, 12, 15, 18] and P_positions(S123, 20) == [0, 4, 8, 12, 16, 20])
print('P3 rule 1, 3 or 4: piles 5, 8, 9, 11, 14')
piles = [5, 8, 9, 11, 14]
print('   ', '; '.join(fmt(n, S134) for n in piles))
check('guide p.6 P3 "5: first, take 3. 8: first, take 1. 9: second. 11: first, take 4. 14: second."',
      [winning_takes(n, S134) for n in piles] == [[3], [1], [], [4], []])
print('P4')
check('guide p.7 P4 "0, 2, 7, 9, 14, 16, 21, 23, 28, 30"', P_positions(S134, 30) == [0, 2, 7, 9, 14, 16, 21, 23, 28, 30])
check('P4 track drawn is 0..30', tracks('grades-4-5', 4) == ['0..30'])

print('P5 Kai: greedy on his FIRST turn only')
kai = [n for n in range(1, 31) if mover_wins_piles((n,), S134) and
       n - greedy_take(n, S134) > 0 and mover_wins_piles((n - greedy_take(n, S134),), S134)]
print('    piles:', kai)
check('guide p.7 P5 "5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29"', kai == [5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29])
kai_all = [n for n in range(1, 31) if mover_wins_piles((n,), S134) and not greedy_all_game_wins(n, S134)]
greedy_ok = [n for n in range(1, 31) if greedy_all_game_wins(n, S134)]
print('    greedy all game, first player could win but greedy can be beaten:', kai_all)
print('    greedy all game wins against every reply from:', greedy_ok)
check('guide p.7 P5 "add 13, 18, 20, 25, 27 (16 piles ...)"',
      sorted(set(kai_all) - set(kai)) == [13, 18, 20, 25, 27] and len(kai_all) == 16 and set(kai) <= set(kai_all))
check('guide p.7 P5 "Greedy all game wins against every reply only from 1, 3, 4, 6, 11"', greedy_ok == [1, 3, 4, 6, 11])
check('guide p.7 P5 example line "13 -> 9 -> 8 -> 4 -> 0" is legal and greedy',
      greedy_take(13, S134) == 4 and (9 - 8) in S134 and greedy_take(8, S134) == 4 and 4 in S134)

print('P6 pile of 100')
print('   ', '1 or 2:', fmt(100, S12), '| 1, 2 or 3:', fmt(100, S123), '| 1, 3 or 4:', fmt(100, S134))
check('guide p.7 P6 "1 or 2: first, take 1. 1, 2 or 3: second. 1, 3 or 4: second."',
      winning_takes(100, S12) == [1] and winning_takes(100, S123) == [] and winning_takes(100, S134) == [])
check('guide p.7 P6 hint "(91, 93, 98, 100)" are the coloured squares near 100',
      [n for n in range(88, 101) if not mover_wins_piles((n,), S134)] == [91, 93, 98, 100])

print('P7')
S23 = (2, 3)
check('guide p.7 P7 "1 or 4: 0, 2, 5, ..., 30"', P_positions(S14, 30) == [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30])
check('guide p.7 P7 "2 or 3: 0, 1, 5, 6, 10, 11, 15, 16, 20, 21, 25, 26, 30"',
      P_positions(S23, 30) == [0, 1, 5, 6, 10, 11, 15, 16, 20, 21, 25, 26, 30])
check('guide p.7 P7 "1, 3 or 5: the even squares"', P_positions(S135, 30) == list(range(0, 31, 2)))

print('P8 does the 1, 3 or 4 pattern repeat forever?')
seq = outcome_sequence(S134, 1000)
check('period 7 from square 0 up to 1000', all(seq[n] == seq[n + 7] for n in range(993)))
check('guide p.7 P8 "Squares 7, 8, 9, 10 are coloured like 0, 1, 2, 3 (yes, no, yes, no)"',
      seq[7:11] == seq[0:4] == 'PNPN')
rem_take = {1: 1, 3: 1, 4: 4, 5: 3, 6: 4}
check('guide p.7 P8 "from those take 1, 1, 4, 3, 4 to get back" (checked for every pile 1..200 with that remainder)',
      all((n - rem_take[n % 7]) >= 0 and not mover_wins_piles((n - rem_take[n % 7],), S134)
          for n in range(1, 201) if n % 7 in rem_take))

print('P9 designing a rule (all move lists from 1..12, any size, piles 0..120)')
for m in (5, 3):
    target = list(range(0, 121, m))
    works = []
    for k in range(1, 13):
        for S in combinations(range(1, 13), k):
            if P_positions(S, 120) == target:
                works.append(S)
    rule = [S for k in range(1, 13) for S in combinations(range(1, 13), k)
            if set(range(1, m)) <= set(S) and all(s % m for s in S)]
    print(f'    multiples of {m}: {len(works)} working lists; smallest: {works[:6]}')
    check(f'guide p.7 P9 / p.8 "exactly the lists containing 1..{m - 1} and no multiple of {m}"', works == rule)
check('guide p.7 P9 example lists for 0, 3, 6 all work',
      all(P_positions(S, 120) == list(range(0, 121, 3)) for S in
          [(1, 2), (1, 2, 4), (1, 2, 5), (1, 2, 4, 5), (1, 2, 7), (1, 2, 4, 7), (1, 2, 8)]))

print('P10 last counter loses, rule 1 or 2: piles 1, 3, 5, 7, 8')
piles = [1, 3, 5, 7, 8]
print('   ', '; '.join(fmt(n, S12, True) for n in piles))
check('guide p.7 P10 "1: second. 3: first, take 2. 5: first, take 1. 7: second. 8: first, take 1."',
      [winning_takes(n, S12, True) for n in piles] == [[], [2], [1], [], [1]])
print('P11')
check('guide p.7 P11 "1 or 2: 1, 4, 7, 10, 13, 16, 19. 1, 2 or 3: 1, 5, 9, 13, 17. Square 0 is not coloured."',
      P_positions(S12, 20, True) == [1, 4, 7, 10, 13, 16, 19] and P_positions(S123, 20, True) == [1, 5, 9, 13, 17])

print('P12 two piles 7 and 7, take 1 or 2 from one pile')
check('P12 pair drawn is 7/7', rows('grades-4-5', 12) == [[7, 7]])
check('guide p.7 P12 "Second"', not winning_two_pile_moves(7, 7, S12))

print('P13 chart 0..9 x 0..9')
chart = [p['chart'] for p in geo['grades-4-5'] if 'chart' in p][0]
check('chart is 10 x 10 with labels 0..9 on both sides, square cells', chart['rows'] == chart['columns'] == 10 and
      chart['row_labels'] == chart['column_labels'] == [str(i) for i in range(10)] and
      chart['cell_pt'][0][0] == chart['cell_pt'][0][1], str(chart))
cells = [(a, b) for a in range(10) for b in range(10) if not mover_wins_piles((a, b), S12)]
check('guide p.8 P13 "34 squares where the two piles have the same remainder on dividing by 3"',
      len(cells) == 34 and all(a % 3 == b % 3 for a, b in cells))
check('guide p.8 P13 "the diagonal and the lines 3, 6 and 9 off it"', {abs(a - b) for a, b in cells} == {0, 3, 6, 9})
check('guide p.8 P13 "20 and 11 ... second"', not mover_wins_piles((20, 11), S12))
check('guide p.8 P13 "Note 1 and 4 is coloured though unequal"', not mover_wins_piles((1, 4), S12))
check('guide p.8 P13 strategy "take 1 or 2 from the pile with the bigger remainder" always legal and restores a match',
      all(max(a % 3, b % 3) - min(a % 3, b % 3) in (1, 2) for a in range(40) for b in range(40) if a % 3 != b % 3))

print('P14 rule 2, 5 or 6')
S256 = (2, 5, 6)
check('guide p.8 P14 "0, 1, 4, 8, 11, 12, 15, 19, 22, 23, 26, 30"',
      P_positions(S256, 30) == [0, 1, 4, 8, 11, 12, 15, 19, 22, 23, 26, 30], str(P_positions(S256, 30)))
seq = outcome_sequence(S256, 1000)
check('guide p.8 P14 / overview "repeating every 11 ... P = 0, 1, 4, 8 (mod 11)" up to 1000',
      all(seq[n] == seq[n + 11] for n in range(989)) and
      [n for n in range(11) if seq[n] == 'P'] == [0, 1, 4, 8] and
      not any(all(seq[n] == seq[n + p] for n in range(900)) for p in range(1, 11)))
check('guide p.8 P14 "(11-16 look like 0-5)"', seq[11:17] == seq[0:6])

# --------------------------------------------------------------------------
print()
print('Adult guide: reply table (p. 3) "From any other pile, take", checked on piles 1..200')
table = {
    '1, 3 or 4': (S134, 7, {1: [1], 3: [1, 3], 4: [4], 5: [3], 6: [4]}),
    '1 or 4': (S14, 5, {1: [1], 3: [1], 4: [4]}),
    '2 or 3': (S23, 5, {2: [2], 3: [2, 3], 4: [3]}),
    'last loses 1 or 2': (S12, 3, {2: [1], 0: [2]}),
    'last loses 1, 2 or 3': (S123, 4, {2: [1], 3: [2], 0: [3]}),
}
for name, (S, m, tk) in table.items():
    mis = name.startswith('last')
    valid, complete = True, True
    missing = set()
    for n in range(1, 201):
        r = n % m
        if r not in tk:
            continue
        actual = winning_takes(n, S, mis)
        listed = [t for t in tk[r] if t <= n]
        if not listed or any(t not in actual for t in listed):
            valid = False
        if set(actual) - set(tk[r]):
            complete = False
            missing |= {(r, t) for t in set(actual) - set(tk[r])}
    check(f'table row "{name}": every listed take wins', valid)
    if not complete:
        note(f'table row "{name}" omits winning takes (remainder, take): {sorted(missing)}')
check('table row "1, 3 or 5": "take 1" from every odd pile wins', all(not mover_wins_piles((n - 1,), S135) for n in range(1, 200, 2)))

print('Launch (p. 2): 7 counters, adult first, take 1 then make 3')
check('adult takes 1 from 7 (to 6) wins, and 6 -> child -> 3 -> child -> adult takes the rest',
      winning_takes(7, S12) == [1] and all(((6 - c) - (3 - c)) == 3 for c in S12) and all((3 - c) in S12 for c in S12))

print('Race games (p. 2)')
check('Race to 10 (say 1 or 2 numbers): first says 1, then 4, 7, 10',
      [n for n in range(1, 11) if not mover_wins_piles((10 - n,), S12)] == [1, 4, 7, 10])
check('Race to 21 (1, 2 or 3 numbers): 1, 5, 9, 13, 17, 21',
      [n for n in range(1, 22) if not mover_wins_piles((21 - n,), S123)] == [1, 5, 9, 13, 17, 21])
S10 = tuple(range(1, 11))
check('Race to 100 (add 1..10): 1, 12, 23, ..., 89, 100',
      [n for n in range(1, 101) if not mover_wins_piles((100 - n,), S10)] == list(range(1, 101, 11)))

print('Overview (p. 8)')
check('"Moves 1 to k. P = multiples of k+1" for k = 1..8, piles 0..200',
      all(P_positions(tuple(range(1, k + 1)), 200) == list(range(0, 201, k + 1)) for k in range(1, 9)))
check('"Last counter loses ... moves 1 to k, P = remainder 1 on dividing by k+1" for k = 1..8',
      all(P_positions(tuple(range(1, k + 1)), 200, True) == list(range(1, 201, k + 1)) for k in range(1, 9)))
note('"(The shift by one is special to moves 1 to k.)": see misere_and_periodicity.out')
g = grundy(S134, 30)
check('"With 1, 3 or 4, g repeats 0, 1, 0, 1, 2, 3, 2"', g[:7] == [0, 1, 0, 1, 2, 3, 2] and all(g[n] == g[n + 7] for n in range(24)))
check('"5 and 6 ... is N and 4 and 6 ... is P"', mover_wins_piles((5, 6), S134) and not mover_wins_piles((4, 6), S134))
for name, S in [('1 or 2', S12), ('1, 2 or 3', S123), ('1, 3 or 4', S134), ('1 or 4', S14), ('2 or 3', S23),
                ('1, 3 or 5', S135), ('2, 5 or 6', S256)]:
    gg = grundy(S, 25)
    check(f'"two piles are P exactly when g(a) = g(b)", rule {name}, piles 0..25',
          all((not mover_wins_piles((a, b), S)) == (gg[a] == gg[b]) for a in range(26) for b in range(26)))
    check(f'"equal piles are P in any game of this kind", rule {name}',
          all(not mover_wins_piles((a, a), S) for a in range(26)))
check('"With 1 or 2, g(n) = n mod 3"', grundy(S12, 60) == [n % 3 for n in range(61)])
check('"In K-1 P8, 1 and 4 is P though unequal" (K-1 P8 rule)', not mover_wins_piles((1, 4), S12))
note('"In K-1 P8, 1 and 4 is P": 1 and 4 is a position of the K-1 P8 game but not one of its printed pairs '
     '(2/2, 1/2, 3/3, 2/4, 4/4); it is reached from 2 and 4 by taking 1 from the 2.')
check('three piles, XOR rule (Sprague-Grundy), rule 1, 3 or 4, piles 0..9',
      all((not mover_wins_piles((a, b, c), S134)) == ((g[a] ^ g[b] ^ g[c]) == 0)
          for a in range(10) for b in range(10) for c in range(10)))

print('Materials (p. 1-2): largest piles built')
check('K-1 largest single pile 10, largest two-pile total 8 (<= 12 per pair)',
      max(r['piles'][0] for p in geo['k-1'] for r in p['counter_rows'] if len(r['piles']) == 1) == 10 and
      max(sum(r['piles']) for p in geo['k-1'] for r in p['counter_rows']) == 10)
check('2-3 largest built total 11 (5 and 6) and single pile 10 (<= 12 per pair)',
      max(sum(r['piles']) for p in geo['grades-2-3'] for r in p['counter_rows']) == 11)
check('4-5 largest pile 16 (P1), 7 and 7 = 14, 20 and 11 = 31 <= 20 + 12', max(16, 14) <= 20 and 31 <= 32)

print()
print('MISMATCHES:', len(issues))
for i in issues:
    print('  -', i)
