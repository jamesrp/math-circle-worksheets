#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 40 (record only).

The fix record said the new figure-eight's crossings are "59° or more". This script finds the four
self-crossings of the stated curve (cos t - 1.5 cos 3t + 0.5 sin 2t, sin t + 0.5 sin 2t - 1.5 sin 3t),
refines each by Newton's method and measures the angle between the two strands: 57.85°, 58.33°,
73.61° and 88.88°, so "about 58° or more". It checks that the card, the fix record and the comment
in figures.py now say so. No PDF changed. Run from the repository root:
    python3 plans/review/checks/week-40/check_critic_fixes.py"""
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def P(t):
    return (math.cos(t) - 1.5 * math.cos(3 * t) + 0.5 * math.sin(2 * t), math.sin(t) + 0.5 * math.sin(2 * t) - 1.5 * math.sin(3 * t))


def D(t):
    return (-math.sin(t) + 4.5 * math.sin(3 * t) + math.cos(2 * t), math.cos(t) + math.cos(2 * t) - 4.5 * math.cos(3 * t))


N = 3000
ts = [2 * math.pi * k / N for k in range(N)]
pts = [P(t) for t in ts]
angles = []
for i in range(N):
    p1, p2 = pts[i], pts[(i + 1) % N]
    for j in range(i + 2, N):
        if i == 0 and j == N - 1:
            continue
        p3, p4 = pts[j], pts[(j + 1) % N]
        den = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
        if abs(den) < 1e-15:
            continue
        a = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / den
        b = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / den
        if not (0 <= a < 1 and 0 <= b < 1):
            continue
        t1, t2 = ts[i] + a * 2 * math.pi / N, ts[j] + b * 2 * math.pi / N
        for _ in range(30):
            q1, q2, d1, d2 = P(t1), P(t2), D(t1), D(t2)
            fx, fy = q1[0] - q2[0], q1[1] - q2[1]
            det = d1[0] * -d2[1] - -d2[0] * d1[1]
            t1, t2 = t1 - (-d2[1] * fx + d2[0] * fy) / det, t2 - (-d1[1] * fx + d1[0] * fy) / det
        d1, d2 = D(t1), D(t2)
        cos = abs(d1[0] * d2[0] + d1[1] * d2[1]) / math.hypot(*d1) / math.hypot(*d2)
        angles.append(math.degrees(math.acos(min(1, cos))))
angles.sort()
check(len(angles) == 4, f'four crossings: {[round(a, 2) for a in angles]}')
check(57.5 < angles[0] < 58.5 and angles[0] < 59, f'smallest crossing {angles[0]:.2f}°: "about 58° or more", not "59° or more"')

card = (ROOT / 'plans' / 'review' / 'week-40.md').read_text()
rec = (ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-40' / 'editable' / 'review' / 'card-shoulds-2026-10-23.md').read_text()
fig = (ROOT / 'lowell-math-circle-year-2' / 'source' / 'week-40' / 'figures.py').read_text()
check('crossings of about 58° or more' in card and 'crossings of 59° or more' not in card, 'card: fix line says about 58° or more')
check('crossings at about 58° or more' in rec and '59° or more' not in rec, 'fix record says about 58° or more')
check('about 58 degrees or more' in fig and '59 degrees' not in fig, 'figures.py comment says about 58 degrees or more')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
