#!/usr/bin/env python3
"""Check the claims, keys and sizes changed by the October 23, 2026 card fixes (v2).

Standard library only. Reads student/students.tex (written from the problem files by
student/regenerate.py) and guide/facilitator.tex beside this file. Finite replays
corroborate the keys; the general arguments are in the adult guide.
"""
from fractions import Fraction as F
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
STRIP = 180  # mm between the end ticks on every strip
fails = []

def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        fails.append(name)

# Problem 3 keys. A card that starts OFF and flips only at marks 1 and 2 reads ON, OFF, OFF, ...
def card(flip_at, n):
    s, out = 0, []
    for k in range(1, n + 1):
        s ^= 1 if flip_at(k) else 0
        out.append(s)
    return out
two = card(lambda k: k <= 2, 200)
check('P3 key: flipping only at the first two marks gives ON, OFF, then OFF for ever',
      two[:2] == [1, 0] and set(two[1:]) == {0})
check('P3 key: never flipping settles too', set(card(lambda k: False, 200)) == {0})
every2 = card(lambda k: k % 2 == 0, 200)
check('P3 richer: flipping at every second mark shows both sides after every mark n <= 100',
      all({0, 1} <= set(every2[n:]) for n in range(100)))
pos = [F(0)]
for _ in range(200):
    pos.append(1 - pos[-1])
check('P3 key: jumping end to end moves the whole strip every time',
      all(abs(pos[k + 1] - pos[k]) == 1 for k in range(200)))
p, two_way = F(0), []
for k in range(1, 201):
    p = (p + 1) / 2 if k % 2 == 1 else p / 2  # the card turns ON at odd marks, OFF at even marks
    two_way.append(p)
check('P3 richer: the two-direction counter goes 90, 45, 112.5, 56.25 mm',
      [x * STRIP for x in two_way[:4]] == [90, 45, F(225, 2), F(225, 4)])
check('P3 richer: every move of the two-direction counter is at least 45 mm',
      all(abs(two_way[k + 1] - two_way[k]) * STRIP >= 45 for k in range(199)))
check('P3 richer: it swings between about 60 and 120 mm',
      abs(two_way[-2] * STRIP - 120) < F(1, 10**9) and abs(two_way[-1] * STRIP - 60) < F(1, 10**9))
# Overview: short moves alone do not make a counter settle. Steps of 1/k of the strip,
# turning back at each end, keep sweeping because 1 + 1/2 + 1/3 + ... grows without bound.
q, d, turns = F(0), 1, 0
for k in range(1, 20001):
    step = F(1, k)
    if not 0 <= q + d * step <= 1:
        d, turns = -d, turns + 1
    q += d * step
check('Overview: a counter with ever-shorter moves (1/k of the strip) still turns back at least 8 times',
      turns >= 8)
# Encore: halfway toward the middle from START approaches the middle (90 mm).
m = F(0)
for _ in range(60):
    m = (m + F(1, 2)) / 2
check('Encore: halfway toward the middle approaches 90 mm', abs(m * STRIP - 90) < F(1, 10**15))

# Student pages.
tex = (HERE / 'student' / 'students.tex').read_text()
check('six numbered problems, in order', [int(n) for n in re.findall(r'\\problem\{(\d+)\}', tex)] == [1, 2, 3, 4, 5, 6])
check('P2 asks "Does the counter get closer and closer to one place?"',
      'Does the counter get closer and closer to one place?' in tex and 'What place does the counter approach?' not in tex)
check('P3 prompt as on the card', 'Make up a flipping rule for a second card that does settle on one side. '
      'Make up a moving rule for the counter that does not get closer and closer to one place.' in tex)
check('P4 drops "Use the card and switching marks"', 'Use the card and switching marks' not in tex)
check('P5 says "The switches before midnight stay the same."',
      'The switches before midnight stay the same.' in tex and 'Keep every switch' not in tex)
box = re.search(r'\\draw\[rounded corners=2mm,line width=0\.7pt\] \((\d+),(\d+)\) rectangle \((\d+),(\d+)\)', tex)
panel = re.search(r'\\draw\[dashed,line width=0\.6pt\] \((\d+),(\d+)\) rectangle \((\d+),(\d+)\)', tex)
bw, bh = int(box[3]) - int(box[1]), int(box[4]) - int(box[2])
cw, ch = int(panel[3]) - int(panel[1]), int(panel[4]) - int(panel[2])
check(f'P4 MIDNIGHT box {bw} x {bh} mm holds the {cw} x {ch} mm card', (bw, bh) == (80, 58) and bw > cw and bh > ch)
check('header switches to Grades 4--5 at Problem 4 and back on the cut-out page',
      tex.index(r'\renewcommand{\band}{Grades 4--5}') < tex.index(r'\problem{4}')
      and tex.index(r'\renewcommand{\band}{Grades 2--5}') > tex.index(r'\problem{6}'))
check('footer M80-D-v2', 'M80-D-v2' in tex and 'M80-D-v1' not in tex)

# Adult guide.
guide = (HERE / 'guide' / 'facilitator.tex').read_text()
flat = ' '.join(guide.split())
for phrase in ['use Problems 1--3', 'Problems 4--6 are a Grades 4--5 continuation', 'Problem 3: a card settles',
               'ON and OFF both fit', 'this is the same obstacle Problem 6 meets', 'Problems 2 and 6',
               'rule in Problem 6 fails', 'not a proof from four drawings', 'at most 15 mm across',
               'scissors, glue', 'copy the folded marks onto the printed line', 'slide a counter from START to the fold',
               'K--1, adult-led on pages 1 and 6', r'\rhead{Adult guide}',
               'A counter that stops moving stays at one place', 'Week 80 / M80-FAC-v2']:
    check(f'guide says "{phrase}"', phrase in flat)
for phrase in ['Facilitator draft', 'part0017', 'network-toggle', 'Do not provide those prompts', 'six drawings',
               'Problems 1--2 only', 'Grades 3--5', 'five minutes considering']:
    check(f'guide no longer says "{phrase}"', phrase not in flat)
refs = [int(n) for n in re.findall(r'Problems? (\d+)', flat)] + \
       [int(n) for r in re.findall(r'Problems (\d+--\d+)', flat) for n in r.split('--')]
check('guide problem references stay within Problems 1-6', refs and max(refs) <= 6)

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
