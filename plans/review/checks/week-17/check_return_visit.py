"""Independent check of the Week 17 return visit (student pages and adult
guide), with this review's own model (dfa17.py) and PDF reader.
Run: python3 check_return_visit.py  (writes out_check_return_visit.txt)
"""
import itertools
import random
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
    return re.sub(r'\s+', ' ', s).strip()


GUIDE = norm(G.text(repo.PDF['RVGUIDE']))


def quote(frag):
    f = norm(frag)
    check(f in GUIDE, 'guide text found: "%s"' % (f[:90] + ('...' if len(f) > 90 else '')))
    return f


def show(w):
    return w if w else 'empty'


def yn(b):
    return 'YES' if b else 'NO'


data = extract_pdf.main(quiet=True)['RV']
STUD = norm(G.text(repo.PDF['RV']))

# ------------------------------------------------------------ page 1 example
pg = data[0]
m = pg['machines'][0]
tab = {}
for s, a, t, _, _ in m['trans']:
    tab.setdefault(s, {})[a] = t
check(all(sorted(tab[s]) == ['B', 'R'] for s in tab) and m['start'] == [0], 'example machine: one start, one R and one B arrow per state')
ex = D.machine(2, 0, m['accept'], {s: (tab[s]['R'], tab[s]['B']) for s in range(2)})
check(D.equivalent(ex, D.last_is('B'))[0], 'example machine (X NO start, Y YES) says YES exactly when the last card is blue')
check(pg['rows'][0][2] == 'RBB', 'example input printed as R B B')
trace = [0]
for ch in 'RBB':
    trace.append(D.run(ex, ch, trace[-1]))
check(trace == [0, 0, 1, 1] and D.accepts(ex, 'RBB'), 'example trace X -R-> X -B-> Y -B-> Y, output YES')
check('Output: YES' in STUD, 'example output printed as YES')

# ------------------------------------------------------------ Problem 1
say('-' * 60)
say('Problem 1 (RR anywhere)')
rows1 = [r[2] for r in pg['rows'][1:]]
check(rows1 == ['RRBB', 'RBR', 'BRRB'], 'P1 test rows: ' + ', '.join(rows1))
f = quote('State N P F R P F F B N N F Stop NO NO YES')
P1 = D.machine(3, 0, [False, False, True], {0: (1, 0), 1: (2, 0), 2: (2, 2)})  # N P F from the guide table
check(D.equivalent(P1, D.factor_RR())[0] and D.agrees(P1, D.P['factor_RR'], 12) is None,
      'guide P1 table machine says YES exactly when RR has appeared (all rows to length 12)')
check(D.minimal_size(P1) == 3, 'P1: minimal size 3')
found, seen = D.brute_min(D.factor_RR(), 2)
check(found is None, 'P1: none of the %d machines with at most 2 states works' % seen)
quote('The printed test rows RRBB, RBR and BRRB should say YES, NO, YES respectively')
check([yn(D.P['factor_RR'](w)) for w in rows1] == ['YES', 'NO', 'YES'], 'P1 test rows -> YES, NO, YES')
quote('Stopping distinguishes RR from each of the other two. Appending R distinguishes empty from R: the first becomes R (NO), the second RR (YES).')
check(not D.P['factor_RR']('R') and D.P['factor_RR']('RR') and D.P['factor_RR']('RR') != D.P['factor_RR'](''),
      'P1 witnesses: stop separates RR; R separates empty/R')
# the other reading of "two red cards in a row"
alt = D.at_least_two_red()
check(D.minimal_size(alt) == 3, 'other reading ("two red cards in the row", i.e. at least two reds): also minimum 3 states')
diff = [yn(D.P['at_least_two_R'](w)) for w in rows1]
say('     under that reading the test rows give', diff, '(guide expects YES, NO, YES)')
check(D.P['at_least_two_R']('RBR') and not D.P['factor_RR']('RBR'), 'RBR is the printed row on which the two readings disagree')
uses = [m.group(0) for m in re.finditer(r'[^.?:]*\brows?\b[^.?:]*', STUD)]
say('     sentences on the student pages that use "row"/"rows":')
for u in uses:
    say('       -', u.strip())
check('two red cards in a row have appeared anywhere' in STUD, 'P1 wording located on the student page')

# return question: RBR anywhere
quote('Their R/B destinations are respectively (R-suffix, empty-suffix), (R-suffix, RB-suffix), (found, empty-suffix), (found, found); only found says YES.')
rbr = D.machine(4, 0, [False, False, False, True], {0: (1, 0), 1: (1, 2), 2: (3, 0), 3: (3, 3)})
check(D.agrees(rbr, D.P['factor_RBR'], 13) is None and D.minimal_size(rbr) == 4, 'return question: guide machine detects RBR anywhere and is minimal (4 states)')
quote('stopping separates found; endings BR and R separate the first three.')
h = ['', 'R', 'RB']
okw = True
for u, v in itertools.combinations(h, 2):
    okw &= any(D.P['factor_RBR'](u + z) != D.P['factor_RBR'](v + z) for z in ('BR', 'R'))
check(okw and all(D.P['factor_RBR']('RBR') != D.P['factor_RBR'](u) for u in h), 'return question witnesses: BR or R separates empty/R/RB; stopping separates RBR')

# ------------------------------------------------------------ Problem 2
say('-' * 60)
say('Problem 2 (both counts even)')
rows2 = [''] + [r[2] for r in data[1]['rows']]
check('No cards' in STUD and rows2 == ['', 'R', 'RB', 'RRBB', 'BBR', 'BRBR'], 'P2 table rows: ' + ', '.join(map(show, rows2)))
quote('Printed rows no cards, R, RB, RRBB, BBR, BRBR should say YES, NO, NO, YES, NO, YES respectively.')
check([yn(D.P['even_even'](w)) for w in rows2] == ['YES', 'NO', 'NO', 'YES', 'NO', 'YES'], 'P2 table answers YES, NO, NO, YES, NO, YES')
quote('EE is the YES start, every other circle NO. R switches EE↔OE and EO↔OO; B switches EE↔EO and OE↔OO.')
names = ['EE', 'OE', 'EO', 'OO']
flipR = {'EE': 'OE', 'OE': 'EE', 'EO': 'OO', 'OO': 'EO'}
flipB = {'EE': 'EO', 'EO': 'EE', 'OE': 'OO', 'OO': 'OE'}
sq = D.machine(4, 0, [True, False, False, False], {i: (names.index(flipR[n]), names.index(flipB[n])) for i, n in enumerate(names)})
check(D.agrees(sq, D.P['even_even'], 12) is None and D.minimal_size(sq) == 4, 'guide square machine correct (rows to length 12) and minimal')
found, seen = D.brute_min(D.even_even(), 3)
check(found is None, 'P2: none of the %d machines with at most 3 states works' % seen)
quote('For any two distinct pairs, append the cards that make the first pair even/even: none, R, B or RB respectively.')
H = {'': '', 'R': 'R', 'B': 'B', 'RB': 'RB'}
okp = True
for u in H:
    for v in H:
        if u != v:
            z = H[u]
            okp &= D.P['even_even'](u + z) and not D.P['even_even'](v + z)
check(okp, 'P2 witnesses separate every ordered pair of empty, R, B, RB')
# extension
quote('An exact three-state construction uses E (even red, last card not blue), F (even red, last card blue) and O (odd red). Start E; only F says YES. R sends E/F to O and O to E; B sends E/F to F and O to O.')
efo = D.machine(3, 0, [False, True, False], {0: (2, 1), 1: (2, 1), 2: (0, 2)})
check(D.agrees(efo, D.P['even_red_last_blue'], 13) is None and D.minimal_size(efo) == 3, 'extension: E/F/O machine correct and minimal (3)')
grid = D.machine(4, 0, [False, True, False, False],  # (even,notB) (even,B) (odd,notB) (odd,B)
                 {0: (2, 1), 1: (2, 1), 2: (0, 3), 3: (0, 3)})
check(D.agrees(grid, D.P['even_red_last_blue'], 12) is None, 'extension: literal 2x2 grid machine also correct')
same = all(D.accepts((4, 2, grid[2], grid[3]), z) == D.accepts((4, 3, grid[2], grid[3]), z) for z in D.strings_upto(10))
check(same, 'extension: the two odd-red grid states have identical futures')
quote('Empty, B and R need distinct states: stopping separates B, and appending B separates empty from R.')
p = D.P['even_red_last_blue']
check(p('B') != p('') and p('B') != p('R') and p('B') != p('RB'), 'extension witnesses hold')

# ------------------------------------------------------------ Problem 3
say('-' * 60)
say('Problem 3 (equal counts)')
rows3 = [r[2] for r in data[2]['rows']]
check(rows3 == ['RRBB', 'RBRB', 'BRR'], 'P3 printed rows: ' + ', '.join(rows3))
quote('Printed rows RRBB, RBRB, BRR require YES, YES, NO.')
check([yn(D.P['equal'](w)) for w in rows3] == ['YES', 'YES', 'NO'], 'P3 rows -> YES, YES, NO')
# every machine with m <= 3 states fails, and the guide's collision argument finds the failure
okall, okarg, worst = True, True, 0
for k in (1, 2, 3):
    for mm in D.all_machines(k):
        cex = D.agrees(mm, D.P['equal'], 2 * k)
        okall &= cex is not None
        fin = [D.run(mm, 'R' * i) for i in range(k + 1)]
        i, j = next((i, j) for i, j in itertools.combinations(range(k + 1), 2) if fin[i] == fin[j])
        a, b = 'R' * i + 'B' * i, 'R' * j + 'B' * i
        okarg &= D.run(mm, a) == D.run(mm, b) and (D.accepts(mm, a) != True or D.accepts(mm, b) != False)
        worst = max(worst, j, i)
check(okall, 'P3: every machine with 1-3 states is wrong on some row of length at most 2m')
check(okarg, "P3: the guide's argument (histories R^0..R^m, collision i<j, append i Bs) exposes an error in every one of them")
random.seed(17)
okr = True
for _ in range(3000):
    k = random.randint(4, 12)
    tab = {s: (random.randrange(k), random.randrange(k)) for s in range(k)}
    mm = D.machine(k, 0, [random.random() < 0.5 for _ in range(k)], tab)
    fin = [D.run(mm, 'R' * i) for i in range(k + 1)]
    i, j = next((i, j) for i, j in itertools.combinations(range(k + 1), 2) if fin[i] == fin[j])
    a, b = 'R' * i + 'B' * i, 'R' * j + 'B' * i
    okr &= not (D.accepts(mm, a) and not D.accepts(mm, b))
check(okr, 'P3: the same argument defeats 3,000 random machines with 4-12 states')
quote('Twelve cards of each label support ordinary tests and red-history collision trials for proposals with at most eight states.')
need = max(max(m_, m_ - 1) for m_ in range(1, 9))
check(need <= 12, 'collision trials for m <= 8 need at most %d cards of one colour in any single row (m reds, at most m-1 appended blues)' % need)
quote('Run the m+1 histories with 0,1,. . .,m red cards')

say('')
say('%d checks, %d failures' % (sum(1 for o in OUT if o.startswith(('ok', 'FAIL'))), len(FAIL)))
(HERE / 'out_check_return_visit.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
