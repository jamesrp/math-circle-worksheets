"""Independent check of the Week 27 adult guide (week-27-facilitator.pdf).

Every profile, candidate table, request log and answer figure is read from the
delivered PDF (pdftotext -layout for text, pdfplumber for the figures) and
checked against the student profiles in extracted.json and against my own
enumeration.  Guide pages are the printed page numbers (PDF page minus one;
the overview is unnumbered).  Output: check_guide.out
"""
import json
import os
import random
import re
import subprocess
import sys

import pdfplumber

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, WEEK, Log, blockers, stable_perfect, perfect_matchings, mname,  # noqa: E402
                    parse_m, da_all_schedules, da_outcomes, run_schedule, all_profiles, prefers, rank)

L = Log()
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract.py')], check=True)
X = json.load(open(os.path.join(HERE, 'extracted.json')))
GUIDE = os.path.join(WEEK, 'week-27-facilitator.pdf')
pdf = pdfplumber.open(GUIDE)
NP = len(pdf.pages)


def text(printed):
    pg = printed + 1
    return subprocess.run(['pdftotext', '-layout', '-f', str(pg), '-l', str(pg), GUIDE, '-'],
                          capture_output=True, text=True).stdout


def student(band, n, case=0):
    p = [p for p in X[band] if p['problem'] == n][0]['cases'][case]
    return (p['L'], p['R'])


def k1(s):
    """'A: XY; B: YX; X: AB; Y: BA' -> profile"""
    d = dict(re.findall(r'([ABXY]): ([ABXY]{2})', s))
    return ({a: list(d[a]) for a in 'AB'}, {x: list(d[x]) for x in 'XY'})


def arrows(t):
    """All 'A: X > Y > Z' lists on a page -> profile."""
    d = {}
    for who, lst in re.findall(r'\b([A-DW-Z]): ([A-DW-Z](?: > [A-DW-Z])+)', t):
        d.setdefault(who, lst.split(' > '))
    Ld = {k: v for k, v in d.items() if k in 'ABCD'}
    Rd = {k: v for k, v in d.items() if k in 'WXYZ'}
    return (Ld, Rd)


def cand_table(t):
    rows = re.findall(r'^\s*((?:[A-D][W-Z] / )+[A-D][W-Z])\s{2,}(Stable|[A-D][W-Z](?:, [A-D][W-Z])*)\s*$', t, re.M)
    return [(m, [] if b == 'Stable' else b.split(', ')) for m, b in rows]


def check_table(P, rows, tag):
    allm = {mname(M) for M in perfect_matchings(sorted(P[0]), sorted(P[1]))}
    L.check({m for m, _ in rows} == allm, f'{tag}: table covers all {len(allm)} candidates')
    for m, listed in rows:
        actual = blockers(P, parse_m(m))
        ok = (not listed and not actual) or (listed and set(listed) <= set(actual))
        extra = sorted(set(actual) - set(listed))
        L.check(ok, f'{tag}: {m}: listed {listed or "Stable"}; actual {actual or "stable"}'
                + (f'  (not listed: {", ".join(extra)})' if listed and extra else ''))


# ------------------------------------------------------------- figures
def figures(idx):
    """Figures on PDF page index idx (0 = unnumbered overview, 1..17 = printed 1..17)."""
    page = pdf.pages[idx]
    toks = []
    for c in page.curves:
        w, h = c['x1'] - c['x0'], c['bottom'] - c['top']
        if 15 < w < 25 and abs(w - h) < 0.5:
            toks.append(('L', (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2))
    for r in page.rects:
        w, h = r['x1'] - r['x0'], r['bottom'] - r['top']
        if 15 < w < 25 and abs(w - h) < 0.5:
            toks.append(('R', (r['x0'] + r['x1']) / 2, (r['top'] + r['bottom']) / 2))
    lab = []
    for side, x, y in toks:
        s = ''.join(ch['text'] for ch in page.chars if abs((ch['x0'] + ch['x1']) / 2 - x) < 8
                    and abs((ch['top'] + ch['bottom']) / 2 - y) < 8)
        lab.append((side, s, x, y))
    segs = []
    for ln in page.lines:
        (x1, y1), (x2, y2) = ln['pts']
        a = [t for t in lab if abs(t[2] - x1) < 2 and abs(t[3] - y1) < 2]
        b = [t for t in lab if abs(t[2] - x2) < 2 and abs(t[3] - y2) < 2]
        if a and b:
            p, q = a[0], b[0]
            if p[0] == 'R':
                p, q = q, p
            segs.append((p, q, bool(ln.get('dash') and ln['dash'][0])))
    lefts = sorted({round(t[2]) for t in lab if t[0] == 'L'})
    figs = []
    words = page.extract_words(extra_attrs=['fontname', 'size'])
    for lx in lefts:
        col = sorted([t for t in lab if t[0] == 'L' and round(t[2]) == lx], key=lambda t: t[3])
        # a column may hold several stacked figures (2-3 Problem 4): split on gaps
        groups = [[col[0]]]
        for t in col[1:]:
            if t[3] - groups[-1][-1][3] > 40:
                groups.append([t])
            else:
                groups[-1].append(t)
        for g in groups:
            top, bot = g[0][3], g[-1][3]
            rights = [t for t in lab if t[0] == 'R' and top - 2 <= t[3] <= bot + 2 and t[2] > g[0][2]]
            rx = min(t[2] for t in rights)
            rights = sorted([t for t in rights if abs(t[2] - rx) < 2], key=lambda t: t[3])
            solid = sorted({p[1] + q[1] for p, q, d in segs if not d and abs(p[2] - g[0][2]) < 2 and top - 2 <= p[3] <= bot + 2})
            dashed = sorted({p[1] + q[1] for p, q, d in segs if d and abs(p[2] - g[0][2]) < 2 and top - 2 <= p[3] <= bot + 2})
            cap = [w for w in words if 'Bold' in w['fontname'] and 8.5 < w['size'] < 9.6
                   and 0 < top - w['bottom'] < 45 and g[0][2] - 60 < (w['x0'] + w['x1']) / 2 < rx + 60]
            capt = ' '.join(w['text'] for w in sorted(cap, key=lambda w: (round(w['top']), w['x0'])))
            figs.append({'caption': capt, 'left': ''.join(t[1] for t in g), 'right': ''.join(t[1] for t in rights),
                         'solid': solid, 'dashed': dashed, 'x': g[0][2], 'y': top})
    return sorted(figs, key=lambda f: (round(f['y'] / 30), f['x']))


def fig_matching(f):
    return {e[0]: e[1] for e in f['solid']}


def caption_m(c):
    m = re.search(r'((?:[A-D][W-Z] / )+[A-D][W-Z])', c)
    return parse_m(m.group(1)) if m else None


L.out(f'Guide: {NP} PDF pages')
FIGS = {}
for pr in range(0, NP):
    FIGS[pr] = figures(pr)
    for f in FIGS[pr]:
        cm = caption_m(f['caption'])
        msg = f'p{pr} figure "{f["caption"]}": {f["left"]}|{f["right"]} solid {f["solid"]} dashed {f["dashed"]}'
        if cm is not None:
            L.check(cm == fig_matching(f), msg + ' (caption matches lines)')
        else:
            L.out('       ' + msg)

f5 = [f for f in FIGS[6] if f['caption'] == 'Unique stable pairing']
L.check(len(f5) == 1 and [mname(m) for m in stable_perfect(student('grades-2-3', 2))] == [mname(fig_matching(f5[0]))],
        'p6 "Unique stable pairing" figure is the only stable pairing of 2-3 P2')
f9 = {f['caption']: mname(fig_matching(f)) for f in FIGS[10]}
L.check(f9.get('Circles ask: 8 requests') == 'AW / BY / CZ / DX' and f9.get('Squares ask: 7 requests') == 'AZ / BY / CW / DX',
        f'p10 figures show the two asking results: {f9}')

# ---------------------------------------------------------------- overview and launch
L.out('=== overview (unnumbered page) and launch (p2)')
P = k1('A: XY; B: XY; X: AB; Y: AB')
L.check(blockers(P, parse_m('AX / BY')) == [] and 'BX' not in blockers(P, parse_m('AX / BY')),
        'launch: in AX/BY, B wants X but X prefers A, so BX does not block')
L.check(blockers(P, parse_m('AY / BX')) == ['AX'], 'launch: in AY/BX, A and X block')
same = [f'{b} P{n} case {i+1}' for b in ('k-1', 'grades-2-3', 'grades-4-5') for pg in X[b] if pg['problem']
        for n in [pg['problem']] for i, c in enumerate(pg['cases']) if (c['L'], c['R']) == P]
L.out(f'  NOTE: the launch profile is printed as a task in: {same}')
alt = k1('A: YX; B: XY; X: AB; Y: AB')
alt_used = [f'{b} P{pg["problem"]}' for b in ('k-1', 'grades-2-3', 'grades-4-5') for pg in X[b] if pg['problem']
            for c in pg['cases'] if (c['L'], c['R']) == alt]
L.check(not alt_used and blockers(alt, parse_m('AY / BX')) == [] and blockers(alt, parse_m('AX / BY')) == ['AY'],
        'replacement launch A: YX; B: XY; X: AB; Y: AB is printed nowhere; in AY/BX X wants A but A prefers Y; in AX/BY, A and Y block')
# proposer optimality, order independence, at most n^2 requests: all 3x3 profiles
ok_opt = ok_req = ok_fixed = True
for Pp in all_profiles('ABC', 'XYZ'):
    st = stable_perfect(Pp)
    for side in ('L', 'R'):
        out = da_outcomes(Pp, side)
        (m, counts), = out.items()
        M = parse_m(m)
        if side == 'L':
            best = all(all(rank(Pp[0][a], M[a]) <= rank(Pp[0][a], S[a]) for S in st) for a in M)
        else:
            inv = {s: a for a, s in M.items()}
            best = all(all(rank(Pp[1][s], inv[s]) <= rank(Pp[1][s], {v: k for k, v in S.items()}[s]) for S in st)
                       for s in inv)
        ok_opt &= best
        ok_req &= max(counts) <= 9
        ok_fixed &= len(counts) == 1
L.check(ok_opt, 'overview/Ext. A: each side, when asking, gets its best stable partner (all 46,656 3x3 profiles, both sides, every order)')
L.check(ok_req, 'overview: never more than n^2 = 9 requests for n = 3')
L.check(ok_fixed, 'p11 hedge: the number of requests never depends on the order of free askers (all 3x3 profiles, both sides)')

# ---------------------------------------------------------------- K-1
L.out('=== K-1 (pp. 3-5)')
t3 = text(3)
for tag, case, band_case in (('P1 top', 'Top: A: XY; B: YX; X: AB; Y: BA', ('k-1', 1, 0)),
                             ('P1 bottom', 'Bottom: A: XY; B: XY; X: AB; Y: AB', ('k-1', 1, 1)),
                             ('P2 top', 'Top: A: XY; B: YX; X: BA; Y: AB', ('k-1', 2, 0)),
                             ('P2 bottom', 'Bottom: A: YX; B: XY; X: BA; Y: AB', ('k-1', 2, 1))):
    L.check(case in t3 and k1(case) == student(*band_case), f'{tag}: guide strips "{case}" match the student page')
P = student('k-1', 1, 0)
L.check([mname(m) for m in stable_perfect(P)] == ['AX / BY'] and blockers(P, parse_m('AY / BX')) == ['AX', 'BY'],
        'P1 top: only AX/BY; crossed blocked by AX and BY; all four first choices')
P = student('k-1', 1, 1)
L.check([mname(m) for m in stable_perfect(P)] == ['AX / BY'] and blockers(P, parse_m('AY / BX')) == ['AX'],
        'P1 bottom: only AX/BY; crossed blocked by AX')
P = student('k-1', 2, 0)
L.check(len(stable_perfect(P)) == 2, 'P2 top: both pairings stable')
P = student('k-1', 2, 1)
L.check([mname(m) for m in stable_perfect(P)] == ['AY / BX'] and blockers(P, parse_m('AX / BY')) == ['AY', 'BX'],
        'P2 bottom: only AY/BX; straight blocked by AY and BX')
t4 = text(4)
rows = re.findall(r'^\s*([ABXY])\s{5,}(Stable|[A-D][W-Z] still blocks)\s{5,}(Stable|[A-D][W-Z] still blocks)\s*$', t4, re.M)
L.check(len(rows) == 4, f'P3 reversal table has 4 rows: {rows}')
for who, top, bot in rows:
    for res, case in ((top, 0), (bot, 1)):
        P = student('k-1', 3, case)
        side = 0 if who in 'AB' else 1
        Q = ({k: list(v) for k, v in P[0].items()}, {k: list(v) for k, v in P[1].items()})
        Q[side][who] = Q[side][who][::-1]
        b = blockers(Q, parse_m('AX / BY'))
        exp = 'Stable' if not b else None
        L.check((res == 'Stable' and not b) or (res != 'Stable' and res.split()[0] in b),
                f'P3 reverse {who} ({"top" if case == 0 else "bottom"}): guide "{res}", actual {b or "stable"}')
L.check('Answer: circle A and Y in the top case' in t4.replace('\n', ' '), 'P3 answer text: A and Y; bottom crossed out')
# P4
P = student('k-1', 4, 0)
ok = [o for o in (['A', 'B'], ['B', 'A']) if not blockers((P[0], {**P[1], 'Y': o}), parse_m('AX / BY'))
      and not blockers((P[0], {**P[1], 'Y': o}), parse_m('AY / BX'))]
L.check(ok == [['A', 'B']], 'P4 top: Y: A > B is the only fill')
P = student('k-1', 4, 1)
ok = [o for o in (['A', 'B'], ['B', 'A']) if not blockers((P[0], {**P[1], 'Y': o}), parse_m('AX / BY'))
      and not blockers((P[0], {**P[1], 'Y': o}), parse_m('AY / BX'))]
L.check(ok == [], 'P4 bottom: impossible (BX blocks AX/BY whatever Y says)')
# P5 / P6 rows
t5 = text(5)
p5, p6 = t5.split('Problem 6 /')
r5 = re.findall(r'^\s*([XY]{2})\s+([XY]{2})\s+([AB]{2})\s+([AB]{2})\s*$', p5, re.M)
r6 = re.findall(r'^\s*([XY]{2})\s+([XY]{2})\s+([AB]{2})\s+([AB]{2})\s*$', p6, re.M)
only, both = set(), set()
for Pp in all_profiles('AB', 'XY'):
    key = (''.join(Pp[0]['A']), ''.join(Pp[0]['B']), ''.join(Pp[1]['X']), ''.join(Pp[1]['Y']))
    s = [mname(m) for m in stable_perfect(Pp)]
    if s == ['AX / BY']:
        only.add(key)
    if len(s) == 2:
        both.add(key)
L.check(set(r5) == only and len(r5) == 7, f'P5: guide lists {len(r5)} profiles; exactly these {len(only)} make only AX/BY stable')
L.check(set(r6) == both and len(r6) == 2, f'P6: guide lists {r6}; exactly these make both stable')

# ---------------------------------------------------------------- Grades 2-3
L.out('=== Grades 2-3 (pp. 6-9)')
t6 = text(6)
L.check('A: XY; B: XY; X: AB; Y: AB' in t6 and k1('A: XY; B: XY; X: AB; Y: AB') == student('grades-2-3', 1, 0),
        'P1 top strips match')
L.check('A: XY; B: YX; X: BA; Y: AB' in t6 and k1('A: XY; B: YX; X: BA; Y: AB') == student('grades-2-3', 1, 1),
        'P1 bottom strips match')
L.check(blockers(student('grades-2-3', 1, 0), parse_m('AY / BX')) == ['AX'], 'P1 top: join A to X on AY/BX')
L.check(len(stable_perfect(student('grades-2-3', 1, 1))) == 2, 'P1 bottom: both stay')
P = arrows(t6)
L.check(P == student('grades-2-3', 2), 'P2 profile matches the student page')
L.check('the checker records all blockers' in t6.replace('\n', ' ').replace('  ', ' '),
        'P2 text says: "One witness is enough to reject a candidate; the checker records all blockers."')
check_table(P, cand_table(t6), 'P2 table')
L.check([mname(m) for m in stable_perfect(P)] == ['AY / BZ / CX'], 'P2: only AY/BZ/CX')
t7 = text(7)
P = arrows(t7)
L.check(P == student('grades-2-3', 3), 'P3 profile matches the student page')
check_table(P, cand_table(t7), 'P3 table')
st = stable_perfect(P)
L.check(sorted(mname(m) for m in st) == ['AY / BX / CZ', 'AZ / BX / CY', 'AZ / BY / CX'], 'P3: exactly three stable')
M1, M2, M3 = parse_m('AY / BX / CZ'), parse_m('AZ / BX / CY'), parse_m('AZ / BY / CX')
L.check(all(P[1][s][0] == a for a, s in M1.items()), 'P3: AY/BX/CZ gives every square its first choice')
L.check(all(P[0][a][0] == s for a, s in M3.items()), 'P3: AZ/BY/CX gives every circle its first choice')
L.check(not all(P[0][a][0] == s for a, s in M2.items()) and not all(P[1][s][0] == a for a, s in M2.items()),
        'P3 ext.: the middle one gives neither side all first choices')
chain = all(rank(P[0][a], M1[a]) >= rank(P[0][a], M2[a]) >= rank(P[0][a], M3[a]) for a in 'ABC')
L.check(chain, 'P3 ext.: circles weakly improve AY/BX/CZ -> AZ/BX/CY -> AZ/BY/CX ("same direction")')
t8 = text(8)
P = arrows(t8)
L.check(P == student('grades-2-3', 4), 'P4 profile matches the student page')
st = sorted(mname(m) for m in stable_perfect(P))
L.check(st == ['AW / BX / CY / DZ', 'AW / BX / CZ / DY', 'AX / BW / CY / DZ', 'AX / BW / CZ / DY'], f'P4: exactly these four: {st}')
blk = all(set(P[0][a][:2]) == set('WX') for a in 'AB') and all(set(P[0][a][:2]) == set('YZ') for a in 'CD') and \
    all(set(P[1][s][:2]) == set('AB') for s in 'WX') and all(set(P[1][s][:2]) == set('CD') for s in 'YZ')
L.check(blk, 'P4: everyone ranks both members of their own block first')
L.check(P[0]['A'][0] == 'W' and P[1]['W'][0] == 'B', 'P4: A wants W while W wants B, so not all eight first choices')
t9 = text(9)
P = arrows(t9)
L.out(f'  P5 guide profile {P}')
st = sorted(mname(m) for m in stable_perfect(P))
L.check(st == ['AX / BY / CZ', 'AY / BX / CZ'], f'P5 construction has exactly two stable: {st}')
rows = cand_table(t9)
check_table(P, rows, 'P5 table')
L.check(all('CZ' in blockers(P, parse_m(m)) for m, b in rows if b), 'P5: CZ blocks every rejected row')

# ---------------------------------------------------------------- Grades 4-5
L.out('=== Grades 4-5 (pp. 10-15)')
t10 = text(10)
L.check(student('grades-4-5', 1, 0) == student('k-1', 2, 0), '4-5 P1 top = K-1 P2 top profile (two stable)')
L.check(student('grades-4-5', 1, 1) == student('grades-2-3', 2), '4-5 P1 bottom lists identical to 2-3 P2 ("the printed lists are identical")')
P = arrows(t10)
L.check(P == student('grades-4-5', 2), 'P2 profile matches the student page')
oc = da_outcomes(P, 'L')
orr = da_outcomes(P, 'R')
L.check(oc == {'AW / BY / CZ / DX': {8}}, f'P2 circles ask: {oc}')
L.check(orr == {'AZ / BY / CW / DX': {7}}, f'P2 squares ask: {orr}')
st = sorted(mname(m) for m in stable_perfect(P))
L.check(st == ['AW / BY / CZ / DX', 'AZ / BY / CW / DX'], f'P2: these are the only stable matchings: {st}')
t11 = text(11)
logs = re.findall(r'^\s*(\d)\s+([A-Z]) to ([A-Z])\s+([A-Z])\s+(None|[A-Z])\s*$', t11, re.M)
circ = [r for r in logs if r[1] in 'ABCD']
sq = [r for r in logs if r[1] in 'WXYZ']
for nm, lg, side in (('circles', circ, 'L'), ('squares', sq, 'R')):
    try:
        res, hold = run_schedule(P, [(r[1], r[2]) for r in lg], side)
        ok = all((kp == r[3]) and ((fr or 'None') == r[4]) for (a, rr, kp, fr), r in zip(res, lg))
        done = len(hold) == 4
        L.check(ok and done, f'P2 {nm}-ask log ({len(lg)} steps) is legal, every "keeps"/"released" entry correct, ends with all held: {hold}')
    except ValueError as e:
        L.check(False, f'P2 {nm} log illegal: {e}')
t12 = text(12)
P = arrows(t12)
L.out(f'  P3 guide profile {P}')
res, hold = run_schedule(P, [('A', 'X'), ('B', 'X'), ('B', 'Y'), ('C', 'Z')], 'L', keep_first=True)
M = {a: r for r, a in hold.items()}
L.check(mname(M) == 'AX / BY / CZ' and blockers(P, M) == ['BX'], f'P3 changed-rule run ends AX/BY/CZ, blocked by BX: {blockers(P, M)}')
L.check(da_outcomes(P, 'L') == {'AY / BX / CZ': {4}} and not blockers(P, parse_m('AY / BX / CZ')),
        'P3: ordinary rule gives AY/BX/CZ, which is stable')
L.check(P[0]['C'][0] == 'Z' and P[1]['Z'][0] == 'C', 'P3: C and Z rank each other first')
oc = da_outcomes(P, 'L', keep_first=True)
L.out(f'  P3 note: under the changed rule the guide profile ends in {sorted(oc)} depending on who asks X first'
      ' (B first gives the stable AY / BX / CZ); the guide asks for one legal order, so this is not an error')
rob = ({'A': list('XYZ'), 'B': list('XYZ'), 'C': list('YXZ')}, {'X': list('CAB'), 'Y': list('ABC'), 'Z': list('ABC')})
oc = da_outcomes(rob, 'L', keep_first=True)
L.check(all(blockers(rob, parse_m(k)) for k in oc), f'P3 note: a profile that ends unstable in every order: {rob} -> {sorted(oc)}')
# P4
L.out('  P4: n^2 = 16 and 100 are valid bounds; the least valid bound is n^2 - n + 1 (13 for n=4, 91 for n=10):')
L.out('      once an asker makes its n-th request, all n-1 other receivers already hold someone, so that request is the last.')
P13 = ({'A': list('ZYXW'), 'B': list('XZYW'), 'C': list('ZXYW'), 'D': list('YXZW')},
       {'W': list('BCDA'), 'X': list('ACDB'), 'Y': list('BCAD'), 'Z': list('DABC')})
oc, lg = da_all_schedules(P13, 'L')
L.check(set().union(*oc.values()) == {13}, f'P4: these 4x4 lists need 13 requests in every order: {P13} -> {oc}')
L.out('    one run: ' + '; '.join(f'{a}->{r}' for a, r, kp, fr in list(lg.values())[0]))
t13 = ' '.join(text(13).split())
L.check('Exact expected answer: 16 requests; 100 with ten per side' in t13, 'p13 heading reads "Exact expected answer: 16 requests; 100 with ten per side"')
# P6
t15 = text(15)
P = arrows(t15)
M = parse_m('AX / BY / CZ')
last = sum(P[0][a][-1] == M[a] for a in M) + sum(P[1][s][-1] == a for a, s in M.items())
L.check(not blockers(P, M) and last == 3 and all(P[0][a][0] == M[a] for a in M),
        f'P6 construction {P}: stable, circles first, {last} last choices')
L.check('279,936' in t15 and '60,324' in t15 and '46,656' in t15, 'P6 census numbers quoted (checked in check_students.out: 60324 stable, max 3)')

# ---------------------------------------------------------------- extensions (p16)
L.out('=== Extension B (p16): most last-choice letters in a stable pairing')


def maxlast(n, sample=None, seed=1):
    left, right = 'ABCD'[:n], 'WXYZ'[:n]
    best = 0
    if sample is None:
        it = all_profiles(left, right)
    else:
        rng = random.Random(seed)
        it = (({a: rng.sample(right, n) for a in left}, {s: rng.sample(left, n) for s in right}) for _ in range(sample))
    for Pp in it:
        for M in stable_perfect(Pp):
            k = sum(Pp[0][a][-1] == M[a] for a in M) + sum(Pp[1][s][-1] == a for a, s in M.items())
            best = max(best, k)
    return best


L.check(maxlast(1) == 2, 'n = 1: 2')
L.check(maxlast(2) == 2, 'n = 2: 2 (exhaustive)')
L.check(maxlast(3) == 3, 'n = 3: 3 (exhaustive)')
m4 = maxlast(4, sample=20000)
P4c = ({'A': list('WXYZ'), 'B': list('XYZW'), 'C': list('YZWX'), 'D': list('ZWXY')},
       {'W': list('BCDA'), 'X': list('CDAB'), 'Y': list('DABC'), 'Z': list('ABCD')})
M = parse_m('AW / BX / CY / DZ')
k = sum(P4c[1][s][-1] == a for a, s in M.items())
L.check(m4 <= 4 and not blockers(P4c, M) and k == 4, f'n = 4: sampled max {m4}; distinct-first-choice construction gives {k}')

L.save(os.path.join(HERE, 'check_guide.out'))
