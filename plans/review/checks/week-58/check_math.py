"""Independent mathematical check of Week 58 (fair division), written for this review.

Imports nothing from the writer's or guide's verifiers.
* Reads the printed inputs from the editable sources (students.tex, materials.tex):
  the A/B colour preferences, the goods in Problems 1, 2 and 5, the U/V values,
  the X/Y/Z observer table and the observer cards; checks that the delivered
  student and material PDFs (pdftotext) print the same values.
* Recomputes every answer with exact fractions:
  P1/P2 all labelled allocations, partitions and divide/choose outcomes (with ties);
  P3 the exact equal-value cuts on the 300 mm strip and the chooser's values;
  P4 the cut-and-choose guarantee on many piecewise-constant strips, and the
  join-cut countertrial; P5 whole cards, fixed halves and a fine grid of paper
  splits; P6 all 27 panel allocations; P7 the two/three-person implications
  exhaustively over small integer profiles.
* Compares the tables, counts and claims printed in the delivered facilitator
  guide (pdftotext) with the computation.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import os
import re
import subprocess
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))


def find_root():
    # committed layout: plans/review/checks/week-58/ (four folders below the repo)
    cand = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
    if os.path.isdir(os.path.join(cand, 'lowell-math-circle-year-2')):
        return cand
    d = HERE  # run-folder layout tmp/review-runs/week-58/: walk up
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
            return d
        d = os.path.dirname(d)
    raise SystemExit('repository not found above ' + HERE)


ROOT = find_root()
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-58')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-58')
STU_PDF = os.path.join(WEEK, 'week-58-students.pdf')
MAT_PDF = os.path.join(WEEK, 'week-58-materials.pdf')
GUIDE_PDF = os.path.join(WEEK, 'week-58-facilitator.pdf')
STU_TEX = os.path.join(SRC, 'student', 'students.tex')
COMMON_TEX = os.path.join(SRC, 'student', 'common.tex')
MAT_TEX = os.path.join(SRC, 'student', 'materials.tex')

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def note(msg):
    say('NOTE ' + msg)


def pdftext(path, layout=False):
    args = ['pdftotext'] + (['-layout'] if layout else []) + [path, '-']
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\u2212', '-').replace('\u2013', '-')).strip()


# --------------------------------------------------------------------------
# 1. Printed inputs
# --------------------------------------------------------------------------
say('== Printed inputs (source vs delivered PDFs)')
stu = open(STU_TEX).read()
common = open(COMMON_TEX).read()
mat = open(MAT_TEX).read()
stu_pages = pdftext(STU_PDF, layout=True).split('\f')
mat_pages = pdftext(MAT_PDF, layout=True).split('\f')

m = re.search(r'\\foreach \\x/\\name/\\r/\\b in \{0/A/(\d)/(\d),96/B/(\d)/(\d)\}', common)
PREF = {'A': {'R': int(m.group(1)), 'B': int(m.group(2))},
        'B': {'R': int(m.group(3)), 'B': int(m.group(4))}}
say('A/B colour preferences (common.tex \\prefmini):', PREF)
for name, (r, b) in [('A', (3, 1)), ('B', (1, 3))]:
    mm = re.search(r'\\prefcard\{\d+\}\{%s\}\{(\d)\}\{(\d)\}' % name, mat)
    check(mm and (int(mm.group(1)), int(mm.group(2))) == (PREF[name]['R'], PREF[name]['B']),
          'materials card %s prints red %s, blue %s, same as the student page' % (name, mm.group(1), mm.group(2)))
# delivered student pages 1-3 print "A 3 ... B 1" / "1 ... 3" in the prefmini
for p in (0, 1, 2):
    t = stu_pages[p]
    rows = [norm(l) for l in t.splitlines() if re.match(r'^\s*A\s+3\s+B\s+1\s*$', l)]
    rows2 = [norm(l) for l in t.splitlines() if re.match(r'^\s*1\s+3\s*$', l)]
    check(len(rows) == 1 and len(rows2) == 1,
          'student p.%d prefmini prints A red 3 / blue 1 and B red 1 / blue 3' % (p + 1))


def goods_between(a, b):
    seg = stu[stu.index(a):stu.index(b)]
    return [(lab, 'R' if t == '1' else 'B')
            for t, lab in re.findall(r'\\good\{[\d.]+\}\{[\d.]+\}\{(\d)\}\{(\w+)\}', seg)]


G1 = goods_between(r'\prob{1}', r'\prob{2}')
G2 = goods_between(r'\prob{2}', r'\prob{3}')
G5 = goods_between(r'\prob{5}', r'\prob{6}')
say('P1 goods:', G1, ' P2 goods:', G2, ' P5 goods:', G5)
check([g[0] for g in G1] == ['R1', 'R2', 'R3', 'B1'] and [g[1] for g in G1] == ['R', 'R', 'R', 'B'],
      'P1 goods are R1,R2,R3 (red) and B1 (blue)')
check([g[0] for g in G2] == ['R1', 'R2', 'B1', 'B2'] and [g[1] for g in G2] == ['R', 'R', 'B', 'B'],
      'P2 goods are R1,R2 (red) and B1,B2 (blue)')
check([g[0] for g in G5] == ['R1', 'R2', 'R3'] and all(g[1] == 'R' for g in G5),
      'P5 goods are R1,R2,R3, all red')
check(re.search(r'R1\s+R2\s+R3\s+B1', stu_pages[0]) is not None, 'student p.1 prints R1 R2 R3 B1')
check(re.search(r'R1\s+R2\s+B1\s+B2', stu_pages[1]) is not None, 'student p.2 prints R1 R2 B1 B2')
check(re.search(r'R1\s+R2\s+R3', stu_pages[4]) is not None, 'student p.5 prints R1 R2 R3')
uv = re.search(r'\\node\[font=\\small\] at \(\\x\+38,14\)\{(\d)\};\\valuedots\{\\x\+44\}\{14\}\{(\d)\}', stu)
check(uv and uv.group(1) == '1' and uv.group(2) == '1', 'P5 U/V cards: number 1 with 1 dot')
check(re.search(r'U\s+V\s*\n\s*1\s+1', stu_pages[4]) is not None, 'student p.5 prints U 1 and V 1')
check(mat.count(r'\redprefcard{') == 2 and re.search(r"at \(38,85\)\{1\};\\valuedots\{46\}\{85\}\{1\}", mat) is not None,
      'materials U/V cards print red value 1')

OBS = {}
for who in 'ABC':
    mm = re.search(r'^%s & (\d+) & (\d+) & (\d+)\\\\' % who, stu, re.M)
    OBS[who] = tuple(int(x) for x in mm.groups())
say('P6 observer table (students.tex):', OBS)
for who in 'ABC':
    mm = re.search(r'\\observercard\{\d+\}\{%s\}\{(\d+)\}\{(\d+)\}\{(\d+)\}' % who, mat)
    check(mm and tuple(int(x) for x in mm.groups()) == OBS[who],
          'materials observer card %s = %s matches the student table' % (who, OBS[who]))
    check(re.search(r'^\s*%s\s+%d\s+%d\s+%d\s*$' % ((who,) + OBS[who]), stu_pages[5], re.M) is not None,
          'student p.6 PDF prints row %s %s' % (who, OBS[who]))
check(re.search(r'\(#1\+45,#2\+12\)\{red: 150 mm\}', common) is not None and
      re.search(r'\(#1\+135,#2\+12\)\{blue: 150 mm\}', common) is not None and r'\strip{0}{70}' in stu,
      'strip sketch labels: red 150 mm then blue 150 mm (red on the left)')

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def alloc_scores(values, owners, n):
    """values[i][g]; owners[g] in range(n). Returns rows[i][j] = i's value of j's bundle."""
    return [[sum((values[i][g] for g in range(len(owners)) if owners[g] == j), F(0))
             for j in range(n)] for i in range(n)]


def ef(rows):
    n = len(rows)
    return all(rows[i][i] >= rows[i][j] for i in range(n) for j in range(n))


def prop(rows):
    n = len(rows)
    return all(n * rows[i][i] >= sum(rows[i]) for i in range(n))


def two_person_catalog(goods):
    labels = [g[0] for g in goods]
    vals = [[F(PREF[p][g[1]]) for g in goods] for p in ('A', 'B')]
    res = []
    for owners in itertools.product(range(2), repeat=len(goods)):
        rows = alloc_scores(vals, owners, 2)
        res.append((owners, rows, ef(rows), prop(rows)))
    return labels, vals, res


def fmt_alloc(labels, owners):
    a = ','.join(l for l, o in zip(labels, owners) if o == 0) or '-'
    b = ','.join(l for l, o in zip(labels, owners) if o == 1) or '-'
    return a, b


def divide_choose(labels, vals, divider):
    """Every partition into two trays (empty tray allowed): chooser picks a max-own tray.
    Returns list of (trays, outcomes) where outcomes = list over tie-breaks of success."""
    chooser = 1 - divider
    seen, out = set(), []
    for mask in itertools.product(range(2), repeat=len(labels)):
        key = min(mask, tuple(1 - x for x in mask))
        if key in seen:
            continue
        seen.add(key)
        trays = [tuple(i for i, x in enumerate(mask) if x == k) for k in (0, 1)]
        cv = [sum((vals[chooser][g] for g in t), F(0)) for t in trays]
        best = [k for k in (0, 1) if cv[k] == max(cv)]
        res = []
        for k in best:
            owners = [None] * len(labels)
            for g in trays[k]:
                owners[g] = chooser
            for g in trays[1 - k]:
                owners[g] = divider
            rows = alloc_scores(vals, owners, 2)
            res.append(ef(rows))
        out.append((trays, res))
    return out


# --------------------------------------------------------------------------
# 2. Problem 1
# --------------------------------------------------------------------------
say('')
say('== Problem 1: R1,R2,R3,B1; A=(3,1), B=(1,3)')
labels1, vals1, cat1 = two_person_catalog(G1)
tot = [sum(v) for v in vals1]
say('totals A,B =', tot)
check(tot == [10, 6], 'totals are 10 (A) and 6 (B)')
good1 = [(fmt_alloc(labels1, o), r) for o, r, e, p in cat1 if e]
say('envy-free allocations (A gets | B gets : A own/other ; B own/other):')
for (a, b), r in good1:
    say('   %-10s | %-8s : %s/%s ; %s/%s' % (a, b, r[0][0], r[0][1], r[1][1], r[1][0]))
check(len(cat1) == 16 and len(good1) == 4, 'exactly 4 of 16 labelled allocations are envy-free for both')
check(all(e == p for o, r, e, p in cat1), 'P1: envy-free <=> proportional on every allocation')
parts_ok = set()
for (a, b), r in good1:
    parts_ok.add(frozenset([a, b]))
check(len(parts_ok) == 4, 'the 4 successes are 4 different partitions (count is 4 under either reading)')
say('divide-and-choose, chooser takes a max-own tray (each tie-break listed):')
tie_parts = []
for d, dn in ((0, 'A'), (1, 'B')):
    for trays, res in divide_choose(labels1, vals1, d):
        if any(res):
            t = ['{' + ','.join(labels1[g] for g in tr) + '}' for tr in trays]
            say('   divider %s, trays %s | %s -> outcomes %s' % (dn, t[0], t[1], res))
            if len(res) > 1:
                tie_parts.append((dn, t))
check(len(tie_parts) == 1 and 'B1' in ''.join(tie_parts[0][1]) and
      any(x == '{R1,R2,R3}' for x in tie_parts[0][1]) and tie_parts[0][0] == 'A',
      'the only chooser tie is in the all-red / blue partition when A divides (B sees 3-3)')
two_red = [(d, trays, res) for d in (0, 1) for trays, res in divide_choose(labels1, vals1, d)
           if sorted(len(t) for t in trays) == [2, 2]]
check(all(len(res) == 1 for d, trays, res in two_red),
      'every two-red / red-plus-blue partition has a strict choice for either divider (no tie)')
check(all(res == [True] for d, trays, res in two_red if
          sum(1 for g in trays[0] if G1[g][1] == 'B') + sum(1 for g in trays[1] if G1[g][1] == 'B') == 1),
      'two-red / red-plus-blue partitions succeed whichever person divides')
# guide's "useful failed trial": A gets one red and the blue
o = (0, 1, 1, 0)
r = alloc_scores(vals1, o, 2)
check((r[0][0], r[0][1]) == (4, 6), "guide's failed trial (A: R1,B1): A sees 4 vs 6")

# --------------------------------------------------------------------------
# 3. Problem 2
# --------------------------------------------------------------------------
say('')
say('== Problem 2: R1,R2,B1,B2')
labels2, vals2, cat2 = two_person_catalog(G2)
check([sum(v) for v in vals2] == [8, 8], 'totals are 8 and 8, half 4')
good2 = [(fmt_alloc(labels2, o), r) for o, r, e, p in cat2 if e]
for (a, b), r in good2:
    say('   %-8s | %-8s : A %s/%s ; B %s/%s' % (a, b, r[0][0], r[0][1], r[1][1], r[1][0]))
check(len(good2) == 5, 'exactly 5 of 16 labelled allocations are envy-free for both')
check(sorted(o for o, r, e, p in cat2 if e) == sorted(o for o, r, e, p in cat2 if p),
      'the proportional-for-both allocations are exactly the same 5')
parts2 = {frozenset([a, b]) for (a, b), r in good2}
say('   unordered partitions among them:', len(parts2), sorted(sorted(p) for p in parts2))
check(len(parts2) == 3,
      'counted as unordered partitions ("two trays", page-1 sense) the same answers are only 3')
rev = alloc_scores(vals2, (1, 1, 0, 0), 2)
check(not ef(rev) and not prop(rev) and rev[0][0] < rev[0][1] and rev[1][1] < rev[1][0],
      'reversed colour split (A: B1,B2) fails both checks for both people')
cs = alloc_scores(vals2, (0, 0, 1, 1), 2)
mx = alloc_scores(vals2, (0, 1, 0, 1), 2)
check([cs[0][0], cs[0][1], 8, 4] == [6, 2, 8, 4] and [cs[1][1], cs[1][0]] == [6, 2],
      'saved-record rows for the colour split: (6,2,8,4) for both')
check([mx[0][0], mx[0][1]] == [4, 4] and [mx[1][1], mx[1][0]] == [4, 4],
      'saved-record rows for a mixed split: (4,4,8,4) for both')

# --------------------------------------------------------------------------
# 4. Problem 3 (strip) and the launch example
# --------------------------------------------------------------------------
say('')
say('== Problem 3: 300 mm strip, red [0,150], blue [150,300]')
L = 150


def strip_val(p, a, b):
    """value to person p of [a,b] (mm)."""
    r = max(F(0), min(F(b), F(L)) - max(F(a), F(0))) / L * PREF[p]['R']
    bl = max(F(0), min(F(b), F(2 * L)) - max(F(a), F(L))) / L * PREF[p]['B']
    return r + bl


def equal_cut(p):
    T = strip_val(p, 0, 2 * L)
    lo, hi = F(0), F(2 * L)
    # cumulative value is piecewise linear; solve exactly on each panel
    for a, b in ((0, L), (L, 2 * L)):
        va, vb = strip_val(p, 0, a), strip_val(p, 0, b)
        if va <= T / 2 <= vb and vb > va:
            return a + (T / 2 - va) * (b - a) / (vb - va)
    return None


for cutter, chooser in (('A', 'B'), ('B', 'A')):
    x = equal_cut(cutter)
    lv = {p: strip_val(p, 0, x) for p in 'AB'}
    rv = {p: strip_val(p, x, 2 * L) for p in 'AB'}
    pick = 'left' if lv[chooser] > rv[chooser] else 'right' if rv[chooser] > lv[chooser] else 'tie'
    say('   %s cuts at %s mm; A sees (%s, %s); B sees (%s, %s); %s takes %s' %
        (cutter, x, lv['A'], rv['A'], lv['B'], rv['B'], chooser, pick))
    exp = {'A': (100, (2, 2), (F(2, 3), F(10, 3)), 'right'),
           'B': (200, (F(10, 3), F(2, 3)), (2, 2), 'left')}[cutter]
    check(x == exp[0] and (lv['A'], rv['A']) == exp[1] and (lv['B'], rv['B']) == exp[2] and pick == exp[3],
          '%s-cut matches the guide: %s mm, chooser takes %s' % (cutter, exp[0], exp[3]))
    sols = [mmx for mmx in range(0, 301) if strip_val(cutter, 0, mmx) == strip_val(cutter, mmx, 300)]
    check(sols == [exp[0]], '%s: the equal-value cut is unique on a whole-mm scan (%s)' % (cutter, sols))
    own = lv[chooser] if pick == 'left' else rv[chooser]
    cown = rv[cutter] if pick == 'left' else lv[cutter]
    check(own >= 2 and cown == 2, 'both receive at least half (chooser %s, cutter %s)' % (own, cown))
# launch example: one panel worth 2, two 75 mm halves worth 1 each
check(F(2) * 75 / 150 == 1, 'page-3 launch example: 75 mm of a 150 mm panel worth 2 is worth 1')
check(all(PREF[p][c] != 2 for p in 'AB' for c in 'RB'),
      'the launch panel value 2 is not a task value (non-task instance)')

# --------------------------------------------------------------------------
# 5. Problem 4: guarantee and join-cut countertrial
# --------------------------------------------------------------------------
say('')
say('== Problem 4')
# Guarantee on random-free exhaustive family: 3 equal segments, integer densities 0..3 per person
count = 0
bad = 0
for dc in itertools.product(range(4), repeat=3):
    for dh in itertools.product(range(4), repeat=3):
        if sum(dc) == 0:
            continue
        T = sum(dc)
        # cumulative; find an x with cutter value T/2 on [0,3]
        acc, x = F(0), None
        for k, d in enumerate(dc):
            if d and acc + d >= F(T, 2):
                x = k + (F(T, 2) - acc) / d
                break
            acc += d

        def val(dens, a, b):
            return sum((dens[k] * max(F(0), min(F(b), F(k + 1)) - max(F(a), F(k))) for k in range(3)), F(0))
        cl, cr = val(dc, 0, x), val(dc, x, 3)
        hl, hr = val(dh, 0, x), val(dh, x, 3)
        for hpick in (['L'] if hl > hr else ['R'] if hr > hl else ['L', 'R']):
            h_own, h_oth = (hl, hr) if hpick == 'L' else (hr, hl)
            c_own, c_oth = (cr, cl) if hpick == 'L' else (cl, cr)
            count += 1
            if not (h_own >= h_oth and 2 * h_own >= sum(dh) and c_own >= c_oth and 2 * c_own >= T):
                bad += 1
check(bad == 0, 'cut-and-choose guarantee holds on all %d profiles/tie-breaks (3 segments, densities 0..3)' % count)
# countertrial
cut = 150
red = strip_val('A', 0, cut)
blue = strip_val('A', cut, 300)
say('   join cut, both use A: red piece %s, blue piece %s; chooser takes red' % (red, blue))
check(red == 3 and blue == 1 and blue < F(4, 2) and blue < red,
      'join-cut trial: cutter gets 1 < 2 (half) and envies 3 -> fails both checks; chooser 3 passes')

# --------------------------------------------------------------------------
# 6. Problem 5
# --------------------------------------------------------------------------
say('')
say('== Problem 5: U, V value each red at 1')
vals5 = [[F(1)] * 3, [F(1)] * 3]
n_ok = 0
hist = {}
for owners in itertools.product(range(2), repeat=3):
    rows = alloc_scores(vals5, owners, 2)
    hist[owners.count(0)] = hist.get(owners.count(0), 0) + 1
    n_ok += ef(rows) or prop(rows)
check(n_ok == 0, 'no whole-card allocation (of 8) is envy-free or proportional')
check(hist == {0: 1, 1: 3, 2: 3, 3: 1}, "U's count histogram 1,3,3,1 as the guide states")
# fixed halves H1,H2 (value 1/2 each)
vals5h = [[F(1), F(1), F(1, 2), F(1, 2)]] * 2
ok_h = [o for o in itertools.product(range(2), repeat=4) if ef(alloc_scores(vals5h, o, 2))]
check(len(ok_h) == 4 and all(o[0] != o[1] and o[2] != o[3] for o in ok_h),
      'fixed labelled halves: 4 of 16 pass, each = one whole card + one half per person')
# continuous: U gets share p of the paper (grid of 1/120)
succ = []
for wo in itertools.product(range(2), repeat=2):
    for k in range(121):
        p = F(k, 120)
        u = sum(1 for o in wo if o == 0) + p
        v = sum(1 for o in wo if o == 1) + (1 - p)
        if u >= v and v >= u:
            succ.append((wo, p))
check(len(succ) == 2 and all(w[0] != w[1] and p == F(1, 2) for w, p in succ),
      'with paper share p for U: envy-free iff one whole card each and p = 1/2')
for n in range(1, 10):
    whole_ok = any(2 * k == n for k in range(n + 1))
    split_ok = any(F(k) + F(1, 2) == F(n, 2) for k in range(n))
    check(whole_ok == (n % 2 == 0) and (split_ok or n % 2 == 0),
          'return question n=%d identical cards: whole split possible=%s, one-card split suffices' % (n, whole_ok))

# --------------------------------------------------------------------------
# 7. Problem 6
# --------------------------------------------------------------------------
say('')
say('== Problem 6: X,Y,Z panels')
V6 = [[F(x) for x in OBS[w]] for w in 'ABC']
check(all(sum(r) == 12 for r in V6), 'each observer total is 12; one third is 4')
init = alloc_scores(V6, (0, 1, 2), 3)
check(prop(init) and all(init[i][i] == 4 for i in range(3)), 'initial A:X,B:Y,C:Z proportional (4 >= 4 for all)')
envy = [(i, j) for i in range(3) for j in range(3) if init[i][j] > init[i][i]]
check(envy == [(0, 1), (1, 2), (2, 0)], 'initial: A envies B, B envies C, C envies A (nobody envy-free)')
EFs, PRs = [], []
for owners in itertools.product(range(3), repeat=3):
    rows = alloc_scores(V6, owners, 3)
    if ef(rows):
        EFs.append(owners)
    if prop(rows):
        PRs.append(owners)
say('   envy-free allocations (owner of X,Y,Z):', EFs, ' proportional:', PRs)
check(EFs == [(2, 0, 1)], 'exactly 1 of 27 is envy-free: X->C, Y->A, Z->B (A:Y, B:Z, C:X)')
check(sorted(PRs) == sorted([(0, 1, 2), (2, 0, 1)]), 'exactly 2 of 27 are proportional (initial and repaired)')
rep = alloc_scores(V6, (2, 0, 1), 3)
check(all(rep[i][i] == 8 for i in range(3)), 'repaired allocation: each own value 8')

# --------------------------------------------------------------------------
# 8. Problem 7 general claims
# --------------------------------------------------------------------------
say('')
say('== Problem 7 / overview theorems (exhaustive small profiles)')
c2 = bad2 = 0
for va in itertools.product(range(4), repeat=3):
    for vb in itertools.product(range(4), repeat=3):
        for owners in itertools.product(range(2), repeat=3):
            rows = alloc_scores([[F(x) for x in va], [F(x) for x in vb]], owners, 2)
            c2 += 1
            if ef(rows) != prop(rows):
                bad2 += 1
check(bad2 == 0, 'two people: envy-free <=> proportional on all %d cases (3 goods, values 0..3)' % c2)
c3 = bad3 = pne = 0
rng = list(itertools.product(range(3), repeat=3))
for va in rng:
    for vb in rng:
        for vc in rng:
            V = [[F(x) for x in va], [F(x) for x in vb], [F(x) for x in vc]]
            for owners in itertools.product(range(3), repeat=3):
                rows = alloc_scores(V, owners, 3)
                e, p = ef(rows), prop(rows)
                c3 += 1
                if e and not p:
                    bad3 += 1
                if p and not e:
                    pne += 1
check(bad3 == 0, 'three people: envy-free => proportional on all %d cases (3 goods, values 0..2)' % c3)
check(pne > 0, 'three people: proportional-but-not-envy-free occurs (%d cases)' % pne)
# negative values do not break either implication (sign-free algebra)
neg_bad = 0
for va in itertools.product(range(-2, 3), repeat=3):
    for vb in itertools.product(range(-2, 3), repeat=3):
        for owners in itertools.product(range(2), repeat=3):
            rows = alloc_scores([[F(x) for x in va], [F(x) for x in vb]], owners, 2)
            neg_bad += ef(rows) != prop(rows)
check(neg_bad == 0, 'two-person equivalence also holds with negative values (nonnegativity not needed)')

# --------------------------------------------------------------------------
# 9. Facilitator guide text
# --------------------------------------------------------------------------
say('')
say('== Facilitator guide (delivered PDF text)')
g = norm(pdftext(GUIDE_PDF))
for a, b, ao, at, bo, bt in [('R1,R2', 'R3,B1', 6, 4, 4, 2), ('R1,R3', 'R2,B1', 6, 4, 4, 2),
                             ('R2,R3', 'R1,B1', 6, 4, 4, 2), ('R1,R2,R3', 'B1', 9, 1, 3, 3)]:
    present = '%s %s %d/%d; %d/%d' % (a, b, ao, at, bo, bt) in g
    match = any(x == (a, b) and (r[0][0], r[0][1], r[1][1], r[1][0]) == (ao, at, bo, bt) for x, r in good1)
    check(present and match, 'guide P1 row %s | %s %d/%d; %d/%d printed and correct' % (a, b, ao, at, bo, bt))
for a, b, s in [('R1,R2', 'B1,B2', '6/2; 6/2'), ('R1,B1', 'R2,B2', '4/4; 4/4'), ('R1,B2', 'R2,B1', '4/4; 4/4'),
                ('R2,B1', 'R1,B2', '4/4; 4/4'), ('R2,B2', 'R1,B1', '4/4; 4/4')]:
    nums = [int(x) for x in re.findall(r'\d+', s)]
    match = any(x == (a, b) and [r[0][0], r[0][1], r[1][1], r[1][0]] == nums for x, r in good2)
    check(('%s %s %s' % (a, b, s)) in g and match, 'guide P2 row %s | %s %s printed and correct' % (a, b, s))
check('totals are 10 and 6' in g and 'Exactly five of the 16' in g, 'guide P1/P2 totals and counts printed')
check('A / 100 mm' in g and 'B / 200 mm' in g, 'guide P3 table prints 100 mm and 200 mm')
check(re.search(r'A 4 8 0 4 B 0 4 8 4 C 8 0 4 4', g) is not None, 'guide P6 table matches the observer values')
check('only the repaired assignment is envy-free' in g and 'Exactly two are proportional' in g,
      'guide P6 counts (1 envy-free, 2 proportional) printed')
check('Among the 2 3 = 8' in g or 'Among the 23 = 8' in g or '2^3' in g or '= 8 labeled allocations' in g,
      'guide P5 prints 8 labelled whole allocations')
# cutting error (2 + e/50, 2 - e/50) within the same colour, both cutters
okerr = True
for cutter, x0, lo, hi in (('A', 100, -100, 50), ('B', 200, -50, 100)):
    for e in range(lo, hi + 1):
        lv = strip_val(cutter, 0, x0 + e)
        if lv != 2 + F(e, 50):
            okerr = False
check(okerr and '2 + e/50' in g, "guide 'cutting error' values (2+e/50, 2-e/50) hold for both cutters")
# Visit A: which partition has the tie
m = re.search(r'The two-red / red-plus-blue partition from Problem 1 leads to a separate question about '
              r'which divider/chooser roles make success certain and why a tie matters', g)
check(m is None,
      "guide Visit A ties 'why a tie matters' to the two-red / red-plus-blue partition, "
      "but that partition has strict choices for both dividers; the tie is in the all-red / blue partition")
# overview example "above one third"
m = re.search(r'being above one third of the total need not make the own bundle largest\. Problem 6 supplies '
              r'a complete example with own value 4', g)
if m:
    note("guide overview says 'being above one third' but the cited example (own 4 of 12) is exactly one third")

say('')
say('failures: %d' % len(FAIL))
for f in FAIL:
    say('  - ' + f)
with open(os.path.join(HERE, 'out_check_math.txt'), 'w') as fh:
    fh.write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
