#!/usr/bin/env python3
"""Check the October 23, 2026 follow-ups to Critic M's coulds for Weeks 84, 96 and 99.

Usage: python3 plans/review/checks/critic-m/check_critic_m.py   (from the repository root)

Week 99: the guide's overview says K-1 has an adult-led route on page 2 (W99-FAC-v3), and
Grades 4-5 Problem 5 labels its third, blank star pair "Extra workspace" (W99-45-v3).
Week 84: the guide's K-1 route gives a time. Week 96: the guide's K-1 route gets a
continuation, which number up to 30 makes the most rectangles, recomputed here. For each
changed PDF the text is compared with the copy archived before these fixes: only the
intended words and the footer ids may differ.
"""
import difflib, re
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y = ROOT / 'lowell-math-circle-year-2'
A = 'archive-before-critic-m-fixes-2026-10-23'
FAIL = []


def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok: FAIL.append(msg)


def words(pdf):
    return re.sub(r'\s+', ' ', ' '.join(p.get_text() for p in pymupdf.open(pdf))).strip().split(' ')


def changes(w, name):
    a, b = words(Y / f'week-{w}' / A / name), words(Y / f'week-{w}' / name)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [(' '.join(a[i1:i2]), ' '.join(b[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']


# Week 99 guide
g = pymupdf.open(Y / 'week-99/week-99-facilitator.pdf')
check('K–1 has an adult-led route on page 2.' in g[0].get_text().replace('\n', ' ') and 'No K–1 coverage' not in g[0].get_text(), '99 guide p. 1 names the K–1 route')
check('K–1 route, adult-led' in g[1].get_text(), '99 guide: the K–1 route is on page 2')
check(all('W99-FAC-v3' in p.get_text() for p in g), '99 guide footers W99-FAC-v3')
ch = [c for c in changes(99, 'week-99-facilitator.pdf') if c != ('W99-FAC-v2', 'W99-FAC-v3')]
check(ch == [('', 'K–1 has an adult-led route on page 2.'), ('K–1 coverage,', '')], f'99 guide: no other text change {ch}')

# Week 99 Grades 4-5 Problem 5
d = pymupdf.open(Y / 'week-99/week-99-grades-4-5.pdf')
p = d[4]
check('Problem 5:' in p.get_text() and all('W99-45-v3' in q.get_text() for q in d), '4-5 p. 5 is Problem 5; footers W99-45-v3')
ex = p.search_for('Extra workspace'); starts = sorted(r.y0 for r in p.search_for('start') if r.y0 > 150); works = sorted(r.y0 for r in p.search_for('work:'))
check(len(ex) == 1 and len(starts) == 3 and len(works) == 2 and works[1] < ex[0].y0 < starts[2], '"Extra workspace" sits between the second work line and the third star pair')
ch = [c for c in changes(99, 'week-99-grades-4-5.pdf') if c != ('W99-45-v2', 'W99-45-v3')]
check(ch == [('', 'Extra workspace')], f'4-5 packet: no other text change {ch}')
check(all('W99-23-v2' in q.get_text() for q in pymupdf.open(Y / 'week-99/week-99-grades-2-3.pdf')), '2-3 packet unchanged at W99-23-v2')

# Week 84 guide
ch = changes(84, 'week-84-facilitator.pdf')
check(ch == [('pages):', 'pages, about 10–15 minutes):')], f'84 guide: the K–1 route gives a time and nothing else changed {ch}')

# Week 96 guide
def rects(n): return [(a, n // a) for a in range(2, n) if n % a == 0 and a <= n // a]
best = max(len(rects(n)) for n in range(2, 31)); top = [n for n in range(2, 31) if len(rects(n)) == best]
check(best == 3 and top == [24, 30] and rects(24) == [(2, 12), (3, 8), (4, 6)] and rects(30) == [(2, 15), (3, 10), (5, 6)] and 20 + 10 >= 30,
      'up to 30, only 24 and 30 make the most rectangles (three each); 20 + 10 counters suffice')
t = re.sub(r'\s+', ' ', ' '.join(q.get_text() for q in pymupdf.open(Y / 'week-96/week-96-facilitator.pdf')))
check('To continue for about 15 more minutes, add 10 counters' in t and '24 (2 by 12, 3 by 8, 4 by 6) and 30 (2 by 15, 3 by 10, 5 by 6) make three each' in t, '96 guide: K–1 continuation printed')
ch = [c for c in changes(96, 'week-96-facilitator.pdf') if c != ('W96-FAC-v1', 'W96-FAC-v2')]
check(len(ch) == 1 and ch[0][0] == '' and ch[0][1].startswith('To continue for about 15 more minutes'), '96 guide: no other text change')
check(len(pymupdf.open(Y / 'week-96/week-96-facilitator.pdf')) == 6, '96 guide still six pages')

print('PASS' if not FAIL else f'FAILURES: {len(FAIL)}')
raise SystemExit(1 if FAIL else 0)
