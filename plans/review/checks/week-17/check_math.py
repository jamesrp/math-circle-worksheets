"""Independent mathematical check of the Week 17 base packets (machine memory)
and their adult guide.

Machines and card rows are read from the delivered student PDFs
(extract_pdf.py); every answer is recomputed with this review's own model
(dfa17.py) and compared with the claims printed in the delivered guide (text
read with pdftotext; each quoted claim is first located verbatim in the guide).
Minimum-state claims are checked three ways: Moore minimisation of a correct
machine, explicit distinguishing continuations, and (where feasible) a brute
search of every smaller machine.  The packet's own check scripts and JSON are
not used.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dfa17 as D  # noqa: E402
import extract_pdf  # noqa: E402
import pdfgeom17 as G  # noqa: E402
import repo  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('‐', '-').replace('‑', '-')).strip()


GUIDE = norm(G.text(repo.PDF['GUIDE']))


def quote(frag):
    """Locate a claim verbatim in the guide and return it."""
    f = norm(frag)
    check(f in GUIDE, 'guide text found: "%s"' % (f[:90] + ('...' if len(f) > 90 else '')))
    return f


def rows_in(s):
    return re.findall(r'\b[RB]{2,}\b', s)


def to_machine(m):
    """Machine dict read from the PDF -> dfa17 machine."""
    n = len(m['accept'])
    table = {}
    for s, a, t, _, _ in m['trans']:
        table.setdefault(s, {})[a] = t
    for s in range(n):
        check(sorted(table.get(s, {})) == ['B', 'R'],
              'drawn state %d has exactly one R arrow and one B arrow' % s)
    check(len(m['start']) == 1, 'drawn machine has exactly one start arrow')
    return D.machine(n, m['start'][0], m['accept'], {s: (table[s]['R'], table[s]['B']) for s in range(n)})


def same_lang(m, ref, name):
    ok, cex = D.equivalent(m, ref)
    check(ok, 'drawn machine recognises exactly "%s"%s' % (name, '' if ok else ' (differs on %r)' % cex))


def show(w):
    return w if w else 'empty'


def lower_bound(pred, hist, name, maxlen=8):
    """Every pair of histories has a distinguishing continuation."""
    wit = {}
    for u, v in itertools.combinations(hist, 2):
        z = D.distinguish(pred, u, v, maxlen)
        wit[(u, v)] = z
        if z is None:
            check(False, '%s: histories %s/%s distinguishable' % (name, show(u), show(v)))
    if all(z is not None for z in wit.values()):
        check(True, '%s: histories %s pairwise distinguishable (shortest witnesses %s)' % (
            name, ', '.join(show(h) for h in hist),
            '; '.join('%s/%s:%s' % (show(u), show(v), show(z)) for (u, v), z in wit.items())))
    return wit


def brute(ref, k, name):
    found, seen = D.brute_min(ref, k)
    check(found is None, '%s: none of the %d machines with at most %d states (start fixed) works' % (name, seen, k))
    return seen


PDFDATA = extract_pdf.main(quiet=True)


def page(key, p):
    return PDFDATA[key][p - 1]


def words_text(key, p):
    return ' '.join(w[0] for w in G.words(repo.PDF[key], p))


# =================================================================== K-1
say('=' * 72)
say('K-1  (week-17-k-1.pdf)')
even = D.P['even_red']
lastR, lastB = D.P['last_R'], D.P['last_B']

# ---- P1
pg = page('K1', 1)
check(len(pg['machines']) == 1, 'P1: one machine drawn')
m1 = to_machine(pg['machines'][0])
same_lang(m1, D.even_red(), 'even number of R')
check(D.run(m1, 'B') == 0 and D.run(m1, 'BR') == 1, 'P1 example "B R: start 1 -B-> 1 -R-> 2; stop at x" matches the drawing')
check(not D.accepts(m1, 'BR'), 'P1 example ends at x (NO)')
rows = [''] + [r[2] for r in pg['rows']]
check(rows == ['', 'B', 'RBR', 'RRR', 'RRRR', 'BBBRB'], 'P1 printed rows (no cards first) are ' + ', '.join(map(show, rows)))
ans = ['YES' if D.accepts(m1, w) else 'NO' for w in rows]
say('     computed P1 answers:', ans)
f = quote('In printed order the answers are YES, YES, YES, NO, YES, NO for empty, B, RBR, RRR, RRRR, BBBRB.')
check(ans == ['YES', 'YES', 'YES', 'NO', 'YES', 'NO'], 'guide P1 answers equal computed answers')
six_yes = [w for w in D.strings(6) if D.accepts(m1, w)]
check(len(six_yes) == 32, 'P1: %d six-card rows finish at check (three are asked for)' % len(six_yes))
f = quote('Three valid six-card examples are BBBBBB, RRBBBB, and RRRRBB.')
ex = rows_in(f)
check(len(set(ex)) == 3 and all(len(w) == 6 and D.accepts(m1, w) for w in ex), 'guide P1 examples are three distinct accepted six-card rows')
quote('Accept any three distinct six-card rows with 0, 2, 4, or 6 Rs')
check(all((w.count('R') in (0, 2, 4, 6)) == D.accepts(m1, w) for w in D.strings(6)), 'guide P1 criterion (0, 2, 4 or 6 Rs) is exact for six cards')
check(pg['slots'] == 18, 'P1 has 3 rows of 6 answer boxes')

# ---- P2
pg = page('K1', 2)
m2 = to_machine(pg['machines'][0])
same_lang(m2, D.last_is('R'), 'last card R')
yes4 = sorted(w for w in D.strings(4) if D.accepts(m2, w))
f = quote('The complete list is RRRR, RRBR, RBRR, RBBR, BRRR, BRBR, BBRR, BBBR.')
check(sorted(rows_in(f)) == yes4 and len(yes4) == 8, 'guide P2 list equals all %d four-card rows ending at check' % len(yes4))
check(all(D.run(m2, 'R', s) == 1 and D.run(m2, 'B', s) == 0 for s in (0, 1)),
      'guide P2: final R lands on check and final B on x from either state')
check(pg['slots'] == 48, 'P2 prints 12 four-box answer rows for 8 answers (guide: "Provide blank paper rather than treating the twelve printed slots as an answer count")')
quote('Provide blank paper rather than treating the twelve printed slots as an answer count.')
rr = sum(w.count('R') for w in yes4)
bb = sum(w.count('B') for w in yes4)
say('     materials: the eight P2 rows laid out together use %d R and %d B cards (guide stock: 12 R and 12 B per table)' % (rr, bb))
quote('If the list has repetitions, sort the physical rows by first card, then second.')
quote('12 R cards and 12 B cards about 3 cm across')

# ---- P3
pg = page('K1', 3)
check(len(pg['machines']) == 2, 'P3: two machines drawn')
a3, b3 = (to_machine(m) for m in pg['machines'])
same_lang(a3, D.even_red(), 'even number of R')
same_lang(b3, D.last_is('R'), 'last card R')
dis6 = [w for w in D.strings(6) if D.accepts(a3, w) != D.accepts(b3, w)]
quote('There are 32 such length-six rows; the task asks for six, not all 32.')
check(len(dis6) == 32, 'P3: %d six-card rows give different answers' % len(dis6))
quote('They disagree exactly when a row ends B with an even red count, or ends R with an odd red count.')
crit = lambda w: (w.endswith('B') and w.count('R') % 2 == 0) or (w.endswith('R') and w.count('R') % 2 == 1)
check(all(crit(w) == (D.accepts(a3, w) != D.accepts(b3, w)) for w in D.strings_upto(10) if w),
      'guide P3 disagreement criterion exact on all rows of length 1-10')
f1 = quote('BBBBBB, RRBBBB, RBRBBB give left YES/right NO')
f2 = quote('BBBBBR, BRBBRR, RBBBRR give left NO/right YES')
L1, L2 = rows_in(f1), rows_in(f2)
check(all(len(w) == 6 and D.accepts(a3, w) and not D.accepts(b3, w) for w in L1), 'guide P3 first three examples: left YES, right NO, six cards')
check(all(len(w) == 6 and not D.accepts(a3, w) and D.accepts(b3, w) for w in L2), 'guide P3 last three examples: left NO, right YES, six cards')
check(len(set(L1 + L2)) == 6, 'guide P3 six examples distinct')
check(pg['slots'] == 36, 'P3 has 6 rows of 6 boxes')

# ---- P4
pg = page('K1', 4)
check(len(pg['machines']) == 2 and pg['machines'][0]['start'] == [0] and not pg['machines'][1]['start'],
      'P4: two empty circles, start arrow on the left one')
sols = [m for m in D.all_machines(2) if D.equivalent(m, D.last_is('B'))[0]]
check(len(sols) == 1 and sols[0][2] == (False, True) and all(sols[0][3][(s, 'R')] == 0 and sols[0][3][(s, 'B')] == 1 for s in (0, 1)),
      'P4: exactly one two-circle machine with the given start (start x; R -> start, B -> other, from both)')
check(D.brute_min(D.last_is('B'), 2)[0] == 2, 'P4/2-3 P3: last-blue needs exactly 2 states')
quote('Use states N (start, NO) and B (YES). From either state, R goes to N and B goes to B.')
same_lang(D.machine(2, 0, [False, True], {0: (0, 1), 1: (0, 1)}), D.last_is('B'), 'last card B (guide P4 machine)')

# ---- P5
quote('Use states Clean (start, YES) and Seen (NO). Clean: B stays, R goes to Seen. Seen: both R and B stay. The exact minimum is two.')
same_lang(D.machine(2, 0, [True, False], {0: (1, 0), 1: (1, 1)}), D.no_red(), 'no red card (guide P5 machine)')
check(D.brute_min(D.no_red(), 2)[0] == 2, 'P5: no-red needs exactly 2 states')

# ---- P6
pg = page('K1', 5)
m6 = to_machine(pg['machines'][0])
same_lang(m6, D.mod_red(3), 'red count divisible by 3')
rws = [r[2] for r in pg['rows']]
words5 = words_text('K1', 5)
check('no cards' in words5, 'P6 first pair starts with "no cards"')
pairs = [('', rws[0]), (rws[1], rws[2]), (rws[3], rws[4]), (rws[5], rws[6])]
check(pairs == [('', 'R'), ('R', 'RR'), ('RR', 'RBR'), ('B', 'RRR')], 'P6 printed pairs: ' + '; '.join('%s/%s' % (show(u), show(v)) for u, v in pairs))
quote('Pair 1 empty/R: append nothing, giving YES/NO. Pair 2 R/RR: append R, giving NO/YES. Pair 3 RR/RBR: impossible. Pair 4 B/RRR: impossible.')
claims = [(0, '', True), (1, 'R', True), (2, None, False), (3, None, False)]
for i, z, possible in claims:
    u, v = pairs[i]
    same_state = D.run(m6, u) == D.run(m6, v)
    check(same_state == (not possible), 'P6 pair %d (%s/%s): %s' % (i + 1, show(u), show(v), 'possible' if possible else 'impossible (same circle)'))
    if z is not None:
        check(D.accepts(m6, u + z) != D.accepts(m6, v + z), 'P6 pair %d: appending %s separates them' % (i + 1, show(z)))
quote('For the first pair, B is also a valid nonempty witness.')
check(D.accepts(m6, 'B') != D.accepts(m6, 'RB'), 'P6 pair 1: B also separates')
quote('The last two pairs already have the same leftover red count, respectively 2 and 0.')
check([u.count('R') % 3 for u in pairs[2]] == [2, 2] and [u.count('R') % 3 for u in pairs[3]] == [0, 0], 'P6 remainders 2 and 0')

# =================================================================== 2-3
say('=' * 72)
say('Grades 2-3  (week-17-grades-2-3.pdf)')
pg = page('G23', 1)
A1, B1 = (to_machine(m) for m in pg['machines'])
same_lang(A1, D.even_red(), 'even number of R')
same_lang(B1, D.last_is('R'), 'last card R')
check(D.run(A1, 'B') == 0 and D.run(A1, 'BR') == 1 and not D.accepts(A1, 'BR'), 'P1 example "B R: start 1 -B-> 1 -R-> 2; stop: NO" matches the drawing')
one4 = sorted(w for w in D.strings(4) if D.accepts(A1, w) != D.accepts(B1, w))
f = quote('The eight rows are RRBR, RRBB, RBRR, RBRB, BRRR, BRRB, BBBR, BBBB.')
check(sorted(rows_in(f)) == one4 and len(one4) == 8, 'guide P1 list equals all %d four-card rows with exactly one YES' % len(one4))
quote('For the ending-B case the first three cards have an even red count: RRB, RBR, BRR, BBB.')
check(sorted(w for w in D.strings(3) if w.count('R') % 2 == 0) == sorted(['RRB', 'RBR', 'BRR', 'BBB']), 'P1 even-red three-card prefixes are RRB, RBR, BRR, BBB')
check(pg['lines'] == 12, 'P1 prints 12 answer lines for 8 answers (the guide does not say that 4 stay empty)')
check('twelve' not in norm(GUIDE.split('Grades 2-3 solutions for Problems 1 to 4')[1].split('Problem 2 At least one red')[0]),
      'guide 2-3 P1 section has no note about the 12 printed lines')

# ---- P2, P3
quote('Use N (start, NO) and Y (YES). N: B stays, R goes to Y. Y: R and B stay. Minimum two.')
same_lang(D.machine(2, 0, [False, True], {0: (1, 0), 1: (1, 1)}), D.seen_red(), 'at least one R (guide P2 machine)')
check(D.brute_min(D.seen_red(), 2)[0] == 2, 'P2: needs exactly 2 states')
quote('Use N (start, NO) and Y (YES). From both states, R goes to N and B to Y. Minimum two.')
same_lang(D.machine(2, 0, [False, True], {0: (0, 1), 1: (0, 1)}), D.last_is('B'), 'last card B (guide P3 machine)')
check(D.accepts(D.seen_red(), 'RBB'), 'guide P2 hint row RBB must say YES')

# ---- P4
pg = page('G23', 3)
rws = [(round(r[0]), round(r[1]), r[2]) for r in pg['rows']]
left = [r for r in rws if r[1] < 200]
right = [r for r in rws if r[1] > 200]
check('no cards' in words_text('G23', 3), 'P4 first pair starts with "no cards"')
pairs = [('', right[0][2])] + [(l[2], r[2]) for l, r in zip(left, right[1:])]
check(pairs == [('', 'R'), ('R', 'RR'), ('RR', 'RRR'), ('RBR', 'RR'), ('B', 'RRR'), ('RB', 'BR')],
      'P4 printed pairs: ' + '; '.join('%s/%s' % (show(u), show(v)) for u, v in pairs))
quote('In printed order: empty/R, append nothing -> YES/NO; R/RR, append R -> NO/YES; RR/RRR, append nothing -> NO/YES; RBR/RR, impossible; B/RRR, impossible; RB/BR, impossible.')
m3 = D.mod_red(3)
claims = [('', ('YES', 'NO')), ('R', ('NO', 'YES')), ('', ('NO', 'YES')), None, None, None]
for (u, v), c in zip(pairs, claims):
    same = D.run(m3, u) == D.run(m3, v)
    if c is None:
        check(same, 'P4 %s/%s impossible: same remainder %d' % (show(u), show(v), u.count('R') % 3))
    else:
        z, (au, av) = c
        got = ('YES' if D.accepts(m3, u + z) else 'NO', 'YES' if D.accepts(m3, v + z) else 'NO')
        check(got == (au, av), 'P4 %s/%s + %s -> %s/%s' % (show(u), show(v), show(z), au, av))
quote('The impossible pairs have equal red remainders, respectively 2, 0, and 1.')
check([pairs[i][0].count('R') % 3 for i in (3, 4, 5)] == [2, 0, 1], 'P4 impossible-pair remainders 2, 0, 1')
quote('Stopping already separates two of the first three pairs.')
check(sum(D.accepts(m3, u) != D.accepts(m3, v) for u, v in pairs[:3]) == 2, 'P4: stopping separates exactly two of the first three pairs')

# ---- P5
mod3 = D.mod_red(3)
check(D.agrees(mod3, D.mod_pred(3), 12) is None and D.minimal_size(mod3) == 3, 'P5: three-state cycle correct on all rows up to 12 and minimal')
lower_bound(D.mod_pred(3), ['', 'R', 'RR'], 'P5 groups of three')
n66 = brute(mod3, 2, 'P5 groups of three')

# ---- P6
suf = D.suffix_RB()
check(D.agrees(suf, D.P['suffix_RB'], 12) is None and D.minimal_size(suf) == 3, 'P6: suffix-RB machine correct on all rows up to 12 and minimal')
quote('From every state, R goes to R. On B: N goes to N, R goes to RB, RB goes to N.')
lower_bound(D.P['suffix_RB'], ['', 'R', 'RB'], 'P6 last two RB')
brute(suf, 2, 'P6 last two RB')
quote('Use RRB, RBB, BRB, and empty to test candidates. A machine that remembers only whether any RB appeared will wrongly accept RBB.')
anyRB = D.machine(3, 0, [False, False, True], {0: (1, 0), 1: (1, 2), 2: (2, 2)})
check(D.accepts(anyRB, 'RBB') and not D.P['suffix_RB']('RBB'), 'an "RB has appeared" machine accepts RBB, which must be NO')
check([D.P['suffix_RB'](w) for w in ('RRB', 'RBB', 'BRB', '')] == [True, False, True, False], 'P6 hint rows RRB, RBB, BRB, empty -> YES, NO, YES, NO')

# =================================================================== 4-5
say('=' * 72)
say('Grades 4-5  (week-17-grades-4-5.pdf)')
pg = page('G45', 1)
M = to_machine(pg['machines'][0])
same_lang(M, D.mod_red(3), 'red count divisible by 3')
check(D.run(M, 'R') == 1 and D.run(M, 'RB') == 1 and not D.accepts(M, 'RB'), 'P1 example "R B: start 1 -R-> 2 -B-> 2; stop: NO" matches the drawing')
yes5 = sorted(w for w in D.strings(5) if D.accepts(M, w))
f = quote('The eleven rows are BBBBB, RRRBB, RRBRB, RRBBR, RBRRB, RBRBR, RBBRR, BRRRB, BRRBR, BRBRR, BBRRR.')
check(sorted(rows_in(f)) == yes5 and len(yes5) == 11, 'guide P1 list equals all %d accepted five-card rows' % len(yes5))
check(all(w.count('R') in (0, 3) for w in yes5), 'P1: accepted five-card rows have 0 or 3 Rs')
say('     P1 page prints %d grey lines (15 short answer lines + 3 long description lines) for 11 rows' % pg['lines'])

# ---- P2
pg = page('G45', 2)
rws = [(round(r[0]), round(r[1]), r[2]) for r in pg['rows']]
left = [r for r in rws if r[1] < 200]
right = [r for r in rws if r[1] > 200]
pairs = [('', right[0][2])] + [(l[2], r[2]) for l, r in zip(left, right[1:])]
check(pairs == [('', 'R'), ('R', 'RR'), ('RR', 'BRR'), ('BBB', 'RRR')], 'P2 printed pairs: ' + '; '.join('%s/%s' % (show(u), show(v)) for u, v in pairs))
quote('empty/R: stop -> YES/NO. R/RR: append R -> NO/YES. RR/BRR: impossible. BBB/RRR: impossible.')
check(D.accepts(m3, '') and not D.accepts(m3, 'R'), 'P2 empty/R: stop -> YES/NO')
check(not D.accepts(m3, 'RR') and D.accepts(m3, 'RRR'), 'P2 R/RR + R -> NO/YES')
check(D.run(m3, 'RR') == D.run(m3, 'BRR') and D.run(m3, 'BBB') == D.run(m3, 'RRR'), 'P2 last two pairs share a state (remainders 2 and 0)')

# ---- P3 (determinism)
bad = 0
for k in (1, 2, 3):
    for m in D.all_machines(k):
        for u, v in itertools.combinations(list(D.strings_upto(3)), 2):
            if D.run(m, u) == D.run(m, v):
                if any(D.accepts(m, u + z) != D.accepts(m, v + z) for z in D.strings_upto(3)):
                    bad += 1
check(bad == 0, 'P3: in every machine with at most 3 states, rows ending on one circle never separate (continuations up to 3 cards)')

# ---- P4
mod4 = D.mod_red(4)
check(D.agrees(mod4, D.mod_pred(4), 12) is None and D.minimal_size(mod4) == 4, 'P4: four-state cycle correct and minimal')
lower_bound(D.mod_pred(4), ['', 'R', 'RR', 'RRR'], 'P4 groups of four')
n5898 = brute(mod4, 3, 'P4 groups of four')
quote('for a pair with i<j reds, append 4-i reds (or none if i=0). The first becomes a multiple of four, while the second has remainder j-i, which is 1, 2, or 3.')
ok = True
for i, j in itertools.combinations(range(4), 2):
    z = 'R' * ((4 - i) % 4)
    ok &= D.mod_pred(4)('R' * i + z) and not D.mod_pred(4)('R' * j + z) and (j + len(z)) % 4 == j - i
check(ok, 'guide P4 witness rule works for every pair 0<=i<j<=3')

# ---- P5
check(D.minimal_size(D.suffix_RB()) == 3, 'P5: suffix RB needs exactly 3 states')
quote('N and R both answer NO but react differently to B.')
check(D.accepts(suf, 'RB') and not D.accepts(suf, 'B'), 'P5: after B, history R says YES and empty says NO')

# ---- P6
for k in range(1, 11):
    mk = D.mod_red(k)
    okk = D.agrees(mk, D.mod_pred(k), 11) is None and D.minimal_size(mk) == k
    for i, j in itertools.combinations(range(k), 2):
        z = 'R' * (0 if i == 0 else k - i)
        okk &= D.mod_pred(k)('R' * i + z) and not D.mod_pred(k)('R' * j + z)
    check(okk, 'P6 m=%d: m-state cycle correct, minimal, and the guide witness (0 if i=0 else m-i Rs) separates every pair' % k)
quote('For m=1 a single YES state with both loops works')
check(D.agrees(D.machine(1, 0, [True], {0: (0, 0)}), D.mod_pred(1), 8) is None, 'P6 m=1: one YES state with both loops')
n5 = brute(D.mod_red(5), 4, 'P6 groups of five')
say('     (groups of six: lower bound from the 6 pairwise-distinguishable histories; brute search not run)')
lower_bound(D.mod_pred(6), ['R' * i for i in range(6)], 'P6 groups of six')

# ---- extension
quote('Change groups of three to exactly two reds: four states suffice (0,1,2,too many), with YES only at 2.')
ex2 = D.exactly_two_red()
check(D.agrees(ex2, D.P['exactly_two_R'], 12) is None and D.minimal_size(ex2) == 4, 'extension: exactly two reds needs exactly 4 states')
lower_bound(D.P['exactly_two_R'], ['', 'R', 'RR', 'RRR'], 'extension exactly two reds')

# =================================================================== guide
say('=' * 72)
say('Adult guide: overview, counts and page references')
quote('It rules out all 66 labeled one/two-state machines for each three-state target and all 5,898 labeled machines of up to three states for the four-cycle target.')
check(n66 == 66 and D.count_machines(1) + D.count_machines(2) == 66, 'there are 66 machines with 1 or 2 states (start fixed)')
check(n5898 == 5898 and sum(D.count_machines(k) for k in (1, 2, 3)) == 5898, 'there are 5,898 machines with 1-3 states (start fixed)')
quote('It independently finds eight length-four disagreement rows, eleven accepted length-five rows, and 32 length-six disagreement rows.')
check((len(one4), len(yes5), len(dis6)) == (8, 11, 32), 'counts 8, 11, 32')
quote('Recognizing the suffix RB needs exactly three states, recording the longest ending that is a prefix of RB: empty, R or RB.')
quote('Simpler last-card and has-seen-R tasks need two states.')
check(all(D.minimal_size(m) == 2 for m in (D.last_is('R'), D.last_is('B'), D.seen_red(), D.no_red())), 'last-card, has-seen-R and no-R targets have minimal size 2')

# student page references in the guide
for band, key, pdfkey in (('K-1', 'K1', 'K1'), ('Grades 2-3', 'G23', 'G23'), ('Grades 4-5', 'G45', 'G45')):
    where = {}
    for p in range(1, 6):
        for n in re.findall(r'Problem (\d+):', words_text(pdfkey, p)):
            where[int(n)] = p
    check(sorted(where) == [1, 2, 3, 4, 5, 6], '%s: Problems 1-6 each printed once' % band)
    sec = GUIDE.split(band + ' solutions')[1:]
    txt = ' '.join(s[:6000] for s in sec)
    refs = re.findall(r'Problem (\d) [^.]*? Student page (\d)', txt)
    seen = {}
    for n, p in refs:
        seen.setdefault(int(n), int(p))
    check(seen == where, '%s: guide "Student page" references %s match the PDF %s' % (band, seen, where))

# route note (p. 11) problem references
f = quote('K-1 can construct the last-blue or no-red machine (P4-5), then test shared continuations (P6). Grades 2-3 can connect P4 to the group-of-three machine (P5), or explore the last-RB machine (P6). Grades 4-5 can choose the state lower-bound route (P3-4 and P6) or suffix memory (P5).')
k1 = words_text('K1', 4) + ' ' + words_text('K1', 5)
g23 = ' '.join(words_text('G23', p) for p in (3, 4, 5))
g45 = ' '.join(words_text('G45', p) for p in (2, 3, 4, 5))
check('Problem 4: Use two circles to make a machine that says' in k1 and 'last card is blue' in k1 and 'no red cards appear' in k1
      and 'Problem 6: For each pair' in k1, 'route note: K-1 P4-5 are the last-blue/no-red machines and P6 the shared continuations')
check('Problem 5: Draw a machine that says YES exactly when its red cards can be put in groups of three' in g23
      and 'Problem 6: Draw a machine that says YES exactly when the last two cards are red followed by blue' in g23,
      'route note: 2-3 P5 is the group-of-three machine and P6 the last-RB machine')
check('Problem 3: Two rows have left a machine on the same circle' in g45 and 'grouped in fours' in g45
      and 'Problem 5: Find the fewest circles needed by a machine that says YES exactly when the last two cards are red followed by blue' in g45,
      'route note: 4-5 P3-4 and P6 are the lower-bound route and P5 the suffix machine')

# diagram legibility: every edge label sits by its own edge
worst = []
for key in ('K1', 'G23', 'G45', 'RV'):
    for pg_ in PDFDATA[key]:
        for mm in pg_['machines']:
            for s_, a_, t_, dist, margin in mm['trans']:
                worst.append((margin, dist, key, pg_['page'], s_, a_, t_))
worst.sort()
check(all(d < 16 for _, d, *_ in worst) and worst[0][0] > 20,
      'every edge label is within 16 pt of its edge middle and the next label is at least %.1f pt farther (%s p.%d)' % (worst[0][0], worst[0][2], worst[0][3]))

say('')
say('%d checks, %d failures' % (sum(1 for o in OUT if o.startswith(('ok', 'FAIL'))), len(FAIL)))
(HERE / 'out_check_math.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
