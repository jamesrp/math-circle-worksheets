#!/usr/bin/env python3
"""Check the claims added or changed by the October 23, 2026 card fixes for Week 99.

    python3 checks/card_fixes_2026_10_23.py [folder with week-99-*.pdf]

Mathematics (standard library): least work by breadth-first search over pile states,
compared with sorted matching; uniqueness of the best matching in every printed pair;
the K-1 route key; the prefix-count bound for Grades 4-5 Problem 4. With a PDF
folder (default ../../week-99) it reads the printed wording and runs
materials/check_materials.py on week-99-materials.pdf.
"""
import itertools, subprocess, sys
from collections import Counter, deque
from pathlib import Path

BINS = 6
fails = []
def check(ok, what):
    print(('PASS ' if ok else 'FAIL ') + what)
    if not ok:
        fails.append(what)

def piles(s):
    c = Counter(int(ch) for ch in s)
    return tuple(c[i] for i in range(BINS))

def bfs(a, b):
    """Least number of single-counter moves to a neighbouring bin from piles a to piles b."""
    start, goal = piles(a), piles(b)
    seen, q = {start: 0}, deque([start])
    while q:
        s = q.popleft()
        if s == goal:
            return seen[s]
        for i in range(BINS):
            if s[i]:
                for j in (i - 1, i + 1):
                    if 0 <= j < BINS:
                        t = list(s); t[i] -= 1; t[j] += 1; t = tuple(t)
                        if t not in seen:
                            seen[t] = seen[s] + 1; q.append(t)

def sorted_work(a, b):
    return sum(abs(x - y) for x, y in zip(sorted(map(int, a)), sorted(map(int, b))))

def best_matchings(a, b):
    """Distinct optimal matchings, as multisets of (start bin, target bin) pairs."""
    xs, ys = list(map(int, a)), list(map(int, b))
    best = sorted_work(a, b)
    return {tuple(sorted(zip(xs, p))) for p in itertools.permutations(ys) if sum(abs(x - y) for x, y in zip(xs, p)) == best}

printed = {'00>24': 6, '03>12': 2, '0005>1234': 7, '1144>0225': 5, '2222>0134': 6, '0055>2233': 8, '1114>0235': 5, '0235>1144': 4}
for pair, work in printed.items():
    a, b = pair.split('>')
    check(bfs(a, b) == sorted_work(a, b) == work, f'{a} -> {b}: least work {work} (search and sorted matching agree)')
    check(len(best_matchings(a, b)) == 1, f'{a} -> {b}: the best matching is unique once identical counters are ignored')
check(len(best_matchings('01', '12')) == 2 and bfs('01', '12') == 2, 'guide example: 01 -> 12 has two best matchings (work 2)')

# K-1 route key
check(bfs('04', '22') == 4, 'K-1 key: gathering counters at 0 and 4 into bin 2 takes 4 moves')
two = [''.join(map(str, c)) for c in itertools.combinations_with_replacement(range(BINS), 2)]
check(all(any(bfs(s, t) == 3 for s in two) for t in two), f'K-1 key: every one of the {len(two)} two-counter targets has a start exactly 3 moves away')
def three_toward_far_end(t):
    pos = sorted(map(int, t)); end = 0 if sum(pos) >= 2 * (BINS - 1) - sum(pos) else BINS - 1
    step = -1 if end == 0 else 1
    for _ in range(3):
        i = next(k for k in (range(len(pos)) if step < 0 else reversed(range(len(pos)))) if pos[k] != end)
        pos[i] += step
    return ''.join(map(str, sorted(pos)))
check(all(bfs(three_toward_far_end(t), t) == 3 for t in two), 'K-1 key: three steps toward the farther end always give exactly 3')

# Grades 4-5 Problem 4: prefix counts and the bound 8
cards = ['0044', '0134', '0224', '0233', '1124', '1133', '1223', '2222']
pref = {c: [sum(int(ch) <= g for ch in c) for g in range(4)] for c in cards}
check(all(0 <= p[0] <= 2 and 0 <= p[1] <= 2 and 2 <= p[2] <= 4 and 2 <= p[3] <= 4 for p in pref.values()),
      'cards: bin 0 and bins 0-1 hold 0-2 counters, bins 0-2 and 0-3 hold 2-4')
d = {(a, b): sorted_work(a, b) for a in cards for b in cards}
check(max(d.values()) == 8 and {frozenset(k) for k, v in d.items() if v == 8} == {frozenset({'0044', '2222'})}, 'cards: maximum work 8, only 0044 and 2222')
check(all(sum(abs(pref[a][g] - pref[b][g]) for g in range(4)) == d[a, b] for a in cards for b in cards), 'cards: work equals the sum of prefix differences')

folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / 'week-99'
def text(name):
    return ' '.join(subprocess.run(['pdftotext', str(folder / name), '-'], capture_output=True, text=True).stdout.split()).replace('’', "'")
if (folder / 'week-99-grades-2-3.pdf').exists():
    t23, t45, tg = text('week-99-grades-2-3.pdf'), text('week-99-grades-4-5.pdf'), text('week-99-facilitator.pdf')
    both = t23 + ' ' + t45
    check('two best move records' not in both and 'Changing the order of moves' not in both, 'Problem 1 no longer asks for two records (both bands)')
    check(both.count('Write each move as you make it.') == 2 and 'Keep one record of your moves' not in both, 'rules: "Write each move as you make it." (both bands)')
    check(both.count('A delivery carries one counter straight to an unfilled target place.') == 2, 'Problem 3 delivery wording (both bands)')
    check('If deliveries tie' not in t23, '2-3 Problem 3: tie sentence cut')
    check('to test your way' not in t45, '4-5 Problem 5: "Make a start and target ... to test your way" cut')
    check('W99-23-v2' in t23 and 'W99-45-v2' in t45 and 'W99-FAC-v2' in tg, 'footers read v2')
    for phrase in ('K–1 route, adult-led', 'week-99-materials.pdf', 'In every printed pair the best matching is unique',
                   'A short reason no pair needs more than 8', 'First route: Problems 1–3 in both bands', 'The record is 0 → 1, 2 → 3'):
        check(phrase in tg, f'guide says: {phrase}')
    check('requested “more than one”' not in tg and 'Use an established separate K–1 activity' not in tg, 'guide: garbled plans sentence and K–1 deferral gone')
    mats = folder / 'week-99-materials.pdf'
    run = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / 'materials' / 'check_materials.py'), str(mats)],
                         capture_output=True, text=True)
    check(run.returncode == 0, 'materials: check_materials.py passes (' + run.stdout.strip().splitlines()[-1] + ')')
print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
