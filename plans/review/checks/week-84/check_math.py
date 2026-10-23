"""Independent check of every Week 84 student problem and every mathematical
claim in the adult guide.

Run pdf_extract.py first: the printed conversations, deals, card contents and
card sizes come from pdf_geometry.json (the delivered student PDF). Guide
statements are matched against the delivered guide PDF's text.

The models are possible-worlds models written from the page's rules, not
shortcuts:
  * Cafe: person i answers YES if every deal still publicly possible and
    agreeing with i's own card is all-YES, NO if none is, else NOT YET; after
    each answer the public set keeps the deals in which i would have said the
    same thing.
  * Headbands: in a round each doll shows PROVE BLUE iff every arrangement in
    the (unchanged) shared set that agrees with what it sees gives it B; after
    the simultaneous reveal the shared set keeps the arrangements that would
    have produced the same three replies.
  * Hidden-number grid: Alice and Bob alternate; the speaker names the larger
    person if every public world agreeing with their own number gives the same
    comparison, else says "don't know"; the public set is updated likewise.

Writes check_math.out.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log, flat, page_text  # noqa: E402

log = Log('Week 84 (Public knowledge): independent checks')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
STU = flat(page_text(PDFS['students']))
GUIDE = flat(page_text(PDFS['guide']))


def has(text, phrase, where):
    ok = flat(phrase) in text
    log.check(ok, f'{where} prints: "{phrase}"')
    return ok


# =================================================================== cafe
log('\n## Cafe (page 1, Problem 1)')


def cafe_run(deal, worlds):
    """Return the spoken answers and the public set after each answer."""
    S = set(worlds)
    answers, sets = [], []

    def answer(i, d, S):
        mine = [w for w in S if w[i] == d[i]]
        allyes = [all(c == 'Y' for c in w) for w in mine]
        return 'YES' if all(allyes) else 'NO' if not any(allyes) else 'NOT YET'

    for i in range(len(deal)):
        a = answer(i, deal, S)
        S = {w for w in S if answer(i, w, S) == a}
        answers.append(a)
        sets.append(set(S))
    return answers, sets


W3 = [''.join(t) for t in product('YN', repeat=3)]
by_conv = defaultdict(list)
for d in W3:
    a, _ = cafe_run(d, W3)
    by_conv[tuple(a)].append(d)
for conv, ds in by_conv.items():
    log(f'  {" / ".join(conv):24s} <- {", ".join(ds)}')
log.check(len(by_conv) == 4, f'exactly 4 conversations are possible with 3 people (got {len(by_conv)})')

printed = {}
for b in G[0]['boxes']:
    if b['lines'] and b['lines'][0].startswith('Conversation'):
        k = int(b['lines'][0].split()[1])
        printed[k] = tuple(re.sub(r'^\d\s+', '', ln) for ln in b['lines'][1:])
log('printed conversations:', printed)
log.check(set(printed.values()) == set(by_conv), 'the four printed conversations are exactly the four possible ones')
for k in sorted(printed):
    log(f'  Conversation {k}: fitting deals = {sorted(by_conv.get(printed[k], []))}')

# guide answer: "YYN; NYY/NYN/NNY/NNN; YNY/YNN; YYY"
m = re.search(r"Problem 1's four conversations leave, in order: ([YN/; ]+?)\. ", GUIDE)
log.check(bool(m), 'found the guide key for Problem 1')
if m:
    key = [sorted(x.split('/')) for x in m.group(1).split('; ')]
    log('guide key:', key)
    for k, ks in zip(sorted(printed), key):
        log.check(sorted(by_conv[printed[k]]) == ks, f'guide key for Conversation {k} = {ks}')

# two-person worked example on page 1
W2 = [''.join(t) for t in product('YN', repeat=2)]
box = {b['lines'][0]: b['lines'] for b in G[0]['boxes'] if b['lines']}
before = sorted(ln.replace('YES', 'Y').replace('NO', 'N').replace(' ', '') for ln in box['Before'][2:])
after = sorted(ln.replace('YES', 'Y').replace('NO', 'N').replace(' ', '') for ln in box['After'][2:])
log.check(before == sorted(W2), f'p.1 example "Before" lists all four 2-person deals {before}')
S_after = sorted(d for d in W2 if cafe_run(d, W2)[0][0] == 'NO')
log.check(after == S_after, f'p.1 example: after person 1 says NO the deals are {S_after}; printed {after}')

# guide narrative claims
log.check(all(cafe_run(d, W3)[0][0] == 'NOT YET' for d in W3 if d[0] == 'Y')
          and all(cafe_run(d, W3)[0][0] == 'NO' for d in W3 if d[0] == 'N'),
          'guide: a first NOT YET proves first preference YES; a personally NO first player says NO')
later_no_yes = [d for d in W3 if cafe_run(d, W3)[0][1] == 'NO' and d[1] == 'Y']
log.check(bool(later_no_yes), f'guide: a later NO need not come from a NO card (person 2 says NO with a YES card in {later_no_yes})')
has(GUIDE, 'Later NO need not mean the later speaker personally says NO.', 'guide p.1')
log.note('Guide p.1 wording: every later NO speaker DOES "personally say NO"; the intended fact (checked above) '
         'is about the speaker\'s own card/preference. Guide p.3 states it correctly: '
         '"Do not infer every NO speaker has preference N."')

# =================================================================== headbands
log('\n## Headbands (page 2 rules, Problems 2-4)')


def replies(world, S):
    n = len(world)
    out = []
    for i in range(n):
        matches = [w for w in S if all(w[j] == world[j] for j in range(n) if j != i)]
        out.append('P' if matches and all(w[i] == 'B' for w in matches) else 'N')
    return tuple(out)


def simulate(world, S0, rounds):
    S = set(S0)
    hist, sets = [], []
    for _ in range(rounds):
        r = replies(world, S)
        S = {w for w in S if replies(w, S) == r}
        hist.append(r)
        sets.append(set(S))
    return hist, sets


def worlds(n):
    return [''.join(t) for t in product('BR', repeat=n)]


ALL3 = worlds(3)
ANN3 = [w for w in ALL3 if 'B' in w]

# two-doll worked example
S2 = ['BB', 'BR', 'RB']
mt = [w for w in S2 if w[1] == 'R']
log.check(mt == ['BR'] and replies('BR', S2)[0] == 'P',
          f'p.2 example: doll 1 seeing R on doll 2 matches {mt} and shows PROVE BLUE')

# Problem 2: the printed deals
deals = []
for b in G[1]['boxes']:
    if b['lines'] and b['lines'][0].startswith('Deal'):
        deals.append((b['lines'][0], ''.join(d['colour'] for d in b['disks']),
                      ''.join(d['letter'] for d in b['disks']), b['labels']))
log('printed deals (name, disk colours, disk letters, position labels):', deals)
for name, col, let, lab in deals:
    log.check(col == let and lab == ['1', '2', '3'], f'{name}: disk colours match letters and are numbered 1 2 3')
    k = col.count('B')
    hist, _ = simulate(col, ANN3, 4)
    blue = {i for i in range(3) if col[i] == 'B'}
    done = next(r for r in range(4) if {i for i in range(3) if hist[r][i] == 'P'} >= blue) + 1
    log(f'  {name} {col}: ' + '; '.join(f'round {r + 1}: ' + ' '.join('PROVE' if x == 'P' else 'NOT YET' for x in h)
                                     for r, h in enumerate(hist[:done])))
    log.check(done == k, f'{name}: every blue doll can first show PROVE BLUE in round {done} = number of blues {k}')
    log.check(all(hist[r][i] == 'N' for r in range(4) for i in range(3) if col[i] == 'R'),
              f'{name}: no red doll ever shows PROVE BLUE')

# general theorem, n = 1..6
ok = True
for n in range(1, 7):
    A = [w for w in worlds(n) if 'B' in w]
    for w in A:
        k = w.count('B')
        hist, _ = simulate(w, A, n + 2)
        for i in range(n):
            first = next((r + 1 for r in range(n + 2) if hist[r][i] == 'P'), None)
            want = k if w[i] == 'B' else None
            if first != want or (first and not all(hist[r][i] == 'P' for r in range(first - 1, n + 2))):
                ok = False
log.check(ok, 'overview theorem: for n = 1..6 dolls, with k >= 1 blues the blue dolls first prove in round k '
              '(and keep proving), red dolls never')

# guide p.2: private views in BBR, round 1
views = {i + 1: sorted(w for w in ANN3 if all(w[j] == 'BBR'[j] for j in range(3) if j != i)) for i in range(3)}
log.check(views == {1: ['BBR', 'RBR'], 2: ['BBR', 'BRR'], 3: ['BBB', 'BBR']},
          f'guide p.2: private views in BBR are {views}')

# guide p.3 claims
_, sets = simulate('BBR', ANN3, 1)
v3 = sorted(w for w in sets[0] if w[:2] == 'BB')
log.check(v3 == ['BBB', 'BBR'], f'guide p.3: after round 1 in BBR the red doll still has {v3}')
v_red = sorted(w for w in ANN3 if w[0] == 'B' and w[2] == 'R')
log.check(v_red == ['BBR', 'BRR'], f'guide p.3: in BRR a red doll (doll 2) initially has both own colours {v_red}')
know_red = all(all(w[i] == 'R' for w in simulate(d, ANN3, d.count('B'))[1][-1]
                   if all(w[j] == d[j] for j in range(3) if j != i))
               for d in ANN3 for i in range(3) if d[i] == 'R')
log.check(know_red, 'guide p.1: after the blues prove, each red doll knows it is red (yet shows NOT YET)')

# sequential protocol leaks (guide p.2)


def sequential_round(world, S):
    S = set(S)
    out = []
    for i in range(3):
        def rep(w, S=S, i=i):
            m = [v for v in S if all(v[j] == w[j] for j in range(3) if j != i)]
            return 'P' if all(v[i] == 'B' for v in m) else 'N'
        r = rep(world)
        S = {w for w in S if rep(w) == r}
        out.append(r)
    return tuple(out)


seq = sequential_round('BBR', ANN3)
log.check(seq != replies('BBR', ANN3),
          f'guide p.2: sequential reveal inside a round leaks: in BBR it gives {seq}, simultaneous gives {replies("BBR", ANN3)}')

# Problem 3: groups by round-1 replies, ordered and unordered readings
log('\nProblem 3: "Put deals into groups that give the same three replies in round 1. '
    'Can later rounds separate every group?"')
H = {w: simulate(w, ANN3, 4)[0] for w in ANN3}
g_ord = defaultdict(list)
for w in ANN3:
    g_ord[H[w][0]].append(w)
log('  ordered (per doll) groups after round 1:', dict(g_ord))
log.check(len(g_ord) == 4 and sorted(map(len, g_ord.values())) == [1, 1, 1, 4],
          'ordered reading: 4 groups, {BRR}, {RBR}, {RRB}, {BBR, BRB, RBB, BBB}')
sep_round = next(r for r in range(1, 5) if len({tuple(H[w][:r]) for w in ANN3}) == 7)
log.check(sep_round == 2, f'ordered reading: all 7 reply histories differ by round {sep_round}; answer "yes"')
for w in ANN3:
    log(f'    {w}: ' + ', '.join(''.join(h) for h in H[w][:3]))

ms = lambda h: tuple(sorted(Counter(h).items()))  # noqa: E731
g_un = defaultdict(list)
for w in ANN3:
    g_un[ms(H[w][0])].append(w)
log('  unordered (which reply cards, not whose) groups after round 1:', dict(g_un))
hist_un = defaultdict(list)
for w in ANN3:
    hist_un[tuple(ms(h) for h in H[w][:4])].append(w)
never = [v for v in hist_un.values() if len(v) > 1]
log.check(bool(never), f'unordered reading: these deals keep identical reply multisets in rounds 1-4: {never}; '
                       'answer would be "no"')
log.note('The answer to Problem 3 depends on whether "the same three replies" means the same reply from each '
         'doll (yes) or the same three reply cards (no).')
has(STU, 'Put deals into groups that give the same three replies in round 1.', 'student p.3')
has(GUIDE, 'all seven deals have distinct public response histories by round 2', 'guide p.3')

# Problem 4: no announcement
stuck = True
for w in ALL3:
    hist, sets = simulate(w, ALL3, 10)
    if any('P' in h for h in hist) or any(s != set(ALL3) for s in sets):
        stuck = False
log.check(stuck, 'Problem 4: with all 8 cards and no announcement every reply is NOT YET in every round for every '
                 'deal, and no card is ever removed; answer "no"')
log.check(all(len([v for v in ALL3 if all(v[j] == w[j] for j in range(3) if j != i)]) == 2 and
              any(v[i] == 'R' for v in ALL3 if all(v[j] == w[j] for j in range(3) if j != i))
              for w in ALL3 for i in range(3)),
          'guide p.3: in every private view each doll has an own-red alternative')

# =================================================================== guide grid
log('\n## Guide p.4: bounded hidden-number grid')


def grid_run(alice, bob, top, turns):
    S = {(a, b) for a in range(top + 1) for b in range(top + 1) if a != b}
    trace = []

    def say(who, x, S):
        mine = [w for w in S if w[who] == x]
        cmp = {('A' if w[0] > w[1] else 'B') for w in mine}
        return cmp.pop() + ' larger' if len(cmp) == 1 else "don't know"

    for t in range(turns):
        who = t % 2
        x = (alice, bob)[who]
        s = say(who, x, S)
        S = {w for w in S if say(who, w[who], S) == s}
        trace.append(('Alice' if who == 0 else 'Bob', s, sorted(S)))
    return trace


tr = grid_run(3, 2, 6, 4)
for who, s, S in tr:
    rows = sorted({w[0] for w in S})
    cols = sorted({w[1] for w in S})
    log(f'  {who}: {s:12s} -> rows {rows}, cols {cols}, {len(S)} worlds' + (f' {S}' if len(S) <= 4 else ''))
log.check(tr[0][1] == "don't know" and sorted({w[0] for w in tr[0][2]}) == [1, 2, 3, 4, 5],
          "Alice's first uncertainty removes rows 0 and 6")
log.check(tr[1][1] == "don't know" and sorted({w[1] for w in tr[1][2]}) == [2, 3, 4],
          "Bob's uncertainty removes columns 0, 1, 5, 6")
log.check(tr[2][1] == "don't know" and tr[2][2] == [(3, 2), (3, 4)],
          "Alice's next uncertainty leaves only row 3: {(3,2), (3,4)}")
log.check([w for w in tr[2][2] if w[1] == 2] == [(3, 2)], 'Bob with private 2 now knows both numbers')
log.check(len({w[1] for w in tr[2][2]}) == 2, "the audience does not yet know Bob's number")
log.check(tr[3][1] == 'A larger' and tr[3][2] == [(3, 2)], 'Bob announces "Alice is larger", leaving (3,2)')
# rows 1,2 know Bob larger, rows 4,5 know Alice larger at Alice's 2nd turn
S1 = set(tr[1][2])
kn = {a: {('A' if w[0] > w[1] else 'B') for w in S1 if w[0] == a} for a in range(1, 6)}
log.check(kn == {1: {'B'}, 2: {'B'}, 3: {'A', 'B'}, 4: {'A'}, 5: {'A'}},
          f'rows 1,2 know Bob is larger, rows 4,5 know Alice is larger, row 3 does not: {kn}')
tr5 = grid_run(3, 2, 5, 4)
log('  domain 0-5, same deal: ' + '; '.join(f'{w}: {s}' for w, s, _ in tr5))
log.check([s for _, s, _ in tr5] != [s for _, s, _ in tr],
          'domain 0-5 gives a different elimination pattern (Alice knows at her 2nd turn)')
log.check(7 * 7 == 49 and 7 * 6 == 42, '49 cells in the 7 x 7 grid, 42 after the diagonal')

# =================================================================== materials
log('\n## Materials (pages 4-8) and guide setup arithmetic')
p4 = [''.join('Y' if t == 'YES' else 'N' for t in b['lines'][1].split()) for b in G[3]['boxes']]
log.check(sorted(p4) == sorted(W3), f'p.4: the eight deal cards are the eight YES/NO deals once each {p4}')
p5 = [''.join(d['colour'] for d in b['disks']) for b in G[4]['boxes']]
log.check(sorted(p5) == sorted(ALL3), f'p.5: the eight headband cards are the eight arrangements once each {p5}')
log.check(all(b['labels'] == ['1', '2', '3'] for b in G[3]['boxes'] + G[4]['boxes']),
          'pp.4-5: every card labels positions 1 2 3 left to right')
sizes = {(b['w_in'], b['h_in']) for b in G[3]['boxes'] + G[4]['boxes']}
log.check(sizes == {(3.45, 1.85)}, f'pp.4-5: configuration cards measure {sizes} in (guide: 3.45 by 1.85)')
gx = (14.55 - 4 * 3.45) / 3
gy = 3.95 - 2 * 1.85
log.check(abs(gx - 0.25) < 1e-9 and abs(gy - 0.25) < 1e-9,
          f'guide p.2: 4 x 2 display of 3.45 x 1.85 in cards is 14.55 x 3.95 in with gaps {gx:.2f} and {gy:.2f} in')

c6 = Counter(' '.join(b['lines']) for b in G[5]['boxes'])
c7 = Counter(' '.join(b['lines']) for b in G[6]['boxes'])
log('p.6 cards:', dict(c6))
log('p.7 cards:', dict(c7))
log.check(c6['YES'] >= 3 and c6['NO'] >= 3, 'p.6: 3 YES and 3 NO private cards cover every cafe deal')
log.check(c6['B BLUE'] >= 3 and c6['R RED'] >= 3, 'p.6: 3 B and 3 R headbands cover every headband deal')
need_hat = Counter()
for w in ANN3 + ALL3:
    for S0 in (ANN3, ALL3):
        if w in S0:
            for h in simulate(w, S0, 4)[0]:
                for x, c in Counter(h).items():
                    need_hat[x] = max(need_hat[x], c)
log.check(c7['PROVE BLUE'] >= need_hat['P'] and c7['NOT YET'] >= need_hat['N'],
          f'p.7: PROVE BLUE x{c7["PROVE BLUE"]}, NOT YET x{c7["NOT YET"]} cover one round of three dolls '
          f'(max needed {need_hat["P"]}, {need_hat["N"]})')
need_cafe = Counter()
for conv in printed.values():
    for x, c in Counter(conv).items():
        need_cafe[x] = max(need_cafe[x], c)
log(f'cafe reply cards needed to lay out a printed conversation: {dict(need_cafe)}; '
    f'p.7 has YES x{c7["YES"]}, NO x{c7["NO"]}, NOT YET x{c7["NOT YET"]}')
log.check(c7['NO'] >= need_cafe['NO'],
          f'p.7 reply cards suffice to lay out every printed cafe conversation (NO needed {need_cafe["NO"]}, '
          f'printed {c7["NO"]})')
log.note('Problem 1 can be solved from the printed transcripts without reply cards, so the shortfall only '
         'matters if a table acts the conversations out with cards.')
has(GUIDE, 'reply cards (pages 6--7)'.replace('--', '–'), 'guide p.2')
log.check(all(len(b['lines']) == 0 for b in G[7]['boxes'][2:]) and
          {(b['w_in'], b['h_in']) for b in G[7]['boxes'][2:]} == {(2.18, 2.3)} and
          {(b['w_in'], b['h_in']) for b in G[6]['boxes']} == {(2.18, 2.3)},
          'p.8: three empty doll slots are the size of the p.7 reply cards (2.18 x 2.30 in)')

# =================================================================== page furniture
log('\n## Page furniture')
log.check(all(p['header'] == 'Week 84 / Public knowledge / Grades 2–5' for p in G), 'all 8 headers identical')
log.check([n for p in G for n in p['problems']] == ['1', '2', '3', '4'], 'problems numbered 1-4 consecutively')
has(STU, 'Does everyone want a cup?', 'student p.1')
has(GUIDE, 'Does everyone want a drink?', 'guide p.1')

log.write(os.path.join(HERE, 'check_math.out'))
