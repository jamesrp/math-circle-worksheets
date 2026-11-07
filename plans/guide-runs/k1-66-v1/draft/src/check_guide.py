#!/usr/bin/env python3
"""Independent checks for the final, visually transcribed Week 66 K-1 packet.
No student solver or source module is imported. Python 3 + Poppler are required.
The student SHA binds the transcription to the eight pages inspected by the writer.
"""
from collections import deque, defaultdict
from functools import lru_cache
from pathlib import Path
import hashlib, re, subprocess

HERE = Path(__file__).resolve().parent
EXPECTED_SHA = '24badb0fc7c0be2a0df035c5ccae1a15595a21ad93b293719422a14307c83bef'

def student_path():
    candidates = [HERE.parent / 'k-1.pdf']
    candidates += [p / 'plans/k1-drafts/week-66/k-1.pdf' for p in HERE.parents]
    for p in candidates:
        if p.is_file(): return p
    raise FileNotFoundError('Place final k-1.pdf beside src/, or run within its repository.')

# Hand-transcribed final PDF: top-left, top-right, bottom-left, bottom-right.
def state(lamps, walker): return (frozenset(lamps), walker)
TARGETS = {
 '1TL': state([0],0), '1TR': state([],-2), '1BL': state([2],2), '1BR': state([-3],-3),
 '2TL': state([2],3), '2TR': state([2],1), '2BL': state([2],0), '2BR': state([2],-1),
 '3TL': state([1,2],2), '3TR': state([-1,2],2), '3BL': state([-3,1],-3), '3BR': state([-2,3],3),
 '4TL': state([-2,1],1), '4TR': state([-2,1],0), '4BL': state([-2,1],-1), '4BR': state([-2,1],-2),
 '5top': state([0,1],0), '5bottom': state([0,1,2],0),
 '6start': state([-2,-1],-1), '6L': state([-2,-1],-2), '6R': state([-2,-1],0), '6F': state([-2],-1),
 '7start': state([-1,0,2],0), '7L': state([-1,0,2],-1), '7R': state([-1,0,2],1), '7F': state([-1,2],0),
 '8top': state([0],0), '8middle': state([],0), '8bottom': state([1],-1),
}
START = state([],0)

def move(s, m):
    lamps,p = s
    return (lamps ^ {p},p) if m == 'F' else (lamps,p + (1 if m == 'R' else -1))

def edges(s):
    for m in 'LRF':
        t = move(s,m)
        if -3 <= t[1] <= 3: yield m,t

DIST={START:0}; PRED=defaultdict(list); q=deque([START])
while q:
    s=q.popleft()
    for m,t in edges(s):
        nd=DIST[s]+1
        if t not in DIST: DIST[t]=nd; q.append(t)
        if DIST[t]==nd: PRED[t].append((s,m))
assert len(DIST)==896

def formula(s):
    lamps,p=s; lo=min(lamps|{0}); hi=max(lamps|{0})
    return len(lamps) + min(-lo + hi-lo + abs(p-hi), hi + hi-lo + abs(p-lo))
for s,d in DIST.items():
    assert d==formula(s), (s,d,formula(s))
    assert d%2 == (len(s[0])+abs(s[1]))%2
# The formula has no imposed street boundary: equality verifies all 896 bounded states.

@lru_cache(None)
def shortest(s):
    if s == START: return ('',)
    return tuple(sorted(w+m for pred,m in PRED[s] for w in shortest(pred)))

def replay(word):
    s=START
    for m in word:
        assert m in 'LRF'
        s=move(s,m)
        assert -3 <= s[1] <= 3
    return s

def place(t):
    if t=='H': return 0
    return int(t[:-1]) * (-1 if t[-1]=='L' else 1)

student=student_path()
assert hashlib.sha256(student.read_bytes()).hexdigest()==EXPECTED_SHA, 'Student PDF changed; re-inspect and update transcription.'
stext=subprocess.check_output(['pdftotext','-layout',str(student),'-'],text=True)
assert len([p for p in stext.split('\f') if p.strip()])==8
assert re.findall(r'Problem (\d+):',stext)==[str(n) for n in range(1,9)]
assert 'dot for each flip and an arrow for each step' in stext

tex=(HERE/'k1-guide.tex').read_text()
# keyrow fields: id, printed location, lit positions, walker, word, walks, flips, total.
rows=re.findall(r'\\keyrow\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}\{([LRF]+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}',tex)
assert len(rows)==24, len(rows)
assert {r[0] for r in rows} == {k for k in TARGETS if k[0] in '123467'}
for key,loc,lamps,p,word,walks,flips,total in rows:
    target=TARGETS[key]
    shown=state([] if lamps=='none' else [place(t.strip()) for t in lamps.split(',')],place(p))
    assert shown==target, (key,shown,target)
    assert replay(word)==target, (key,word)
    assert len(word)==int(total)==DIST[target]
    assert sum(m!='F' for m in word)==int(walks)
    assert word.count('F')==int(flips)==len(target[0])
    assert int(walks)+int(flips)==int(total)
    print(key, 'fewest',total,'=',walks,'steps +',flips,'flips;',word)

# Every route printed as a P5 solution, including both completeness claims.
ways=re.findall(r'\\allways\{(5top|5bottom)\}\{(\d+)\}\{([^{}]+)\}',tex)
assert len(ways)==2
for key,n,csv in ways:
    ws=tuple(sorted(csv.split(',')))
    assert len(ws)==int(n) and ws==shortest(TARGETS[key]), (key,ws,shortest(TARGETS[key]))
    assert all(len(w)==(4 if key=='5top' else 7) for w in ws)
    print(key, 'ALL shortest words:', ', '.join(ws))

for problem in (6,7):
    for m in 'LRF': assert move(TARGETS[f'{problem}start'],m)==TARGETS[f'{problem}{m}']
    ds=[DIST[TARGETS[f'{problem}{k}']] for k in ['start','L','R','F']]
    assert ds==([5,4,6,4] if problem==6 else [9,8,8,8])
assert shortest(TARGETS['4TR']) == ('LLFRRRFL', 'RFLLLFRR')
# Compare every optimal walk order used in the prose for P3/P4.
for key,expected in [('3TR',(4,8)),('3BL',(11,5)),('3BR',(7,13)),
                     ('4TL',(5,7)),('4TR',(6,6)),('4BL',(7,5)),('4BR',(8,4))]:
    lamps,p=TARGETS[key]; lo=min(lamps); hi=max(lamps)
    assert (-lo+hi-lo+abs(p-hi), hi+hi-lo+abs(p-lo))==expected

# Exact length reachability, including all unavailable candidate towers.
exact=[{START:1}]
for n in range(1,8):
    nxt=defaultdict(int)
    for s,count in exact[-1].items():
        for m,t in edges(s): nxt[t]+=count
    exact.append(nxt)
for key,candidates,yes in [('8top',range(1,5),[1,3]),('8middle',range(1,5),[2,4]),('8bottom',range(4,8),[4,6])]:
    target=TARGETS[key]
    assert [n for n in candidates if exact[n].get(target,0)]==yes
    print(key, {n:exact[n].get(target,0) for n in candidates})
for key,word in re.findall(r'\\exactword\{(8top|8middle|8bottom)\}\{([LRF]+)\}',tex):
    assert replay(word)==TARGETS[key] and exact[len(word)].get(TARGETS[key],0)
assert len(re.findall(r'\\exactword\{8',tex))==6
demo=state([],3)
for m in 'FL':
    demo=move(demo,m)
    assert demo not in TARGETS.values()
assert demo==state([3],2)  # non-home-start table demonstration
assert replay('FR')==state([0],1)  # final student P5 convention example
assert 9+8+8+8==33 and 7*2**7==896
assert '7 counters' in tex and '24 cubes' in tex and 'two spares' in tex

pdf=HERE.parent/'k1-guide.pdf'
if pdf.exists():
    gtext=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
    pages=[p for p in gtext.split('\f') if p.strip()]
    assert len(pages)==4, len(pages)
    for n,p in enumerate(pages,1):
        assert 'Week 66 / Lamplighter streets / K' in p and 'adult guide' in p
        assert 'GGT66-K-FAC-v1' in p
    for n in range(1,9): assert f'Problem {n}' in gtext
print('PASS: student identity, 8-page labels, 896-state BFS/formula/parity, 24 key rows, complete P5 lists, all P8 towers, demo, and guide structure.')
