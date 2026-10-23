"""Independent mathematical check of Week 80 (Midnight laboratory).

Does not import or run the package's check_math.py.
- Builds the switch times from the printed rule (11:00 start, given switches at
  11:30 and 11:45, then "halfway from the previous switching time to midnight")
  by replay, and only compares the closed form 1 - 2^-n against the replay.
- Card: replays flips from OFF; checks the post-switch states, that both states
  occur in every interval (1 - eps, 1), that odd/even subsequences are constant
  and different, and the guide's averages remark.
- No last switch: every switch time is followed by a later one before midnight.
- Endpoint: the printed rule constrains only times before midnight; ON and OFF
  extensions agree on every prescribed time and differ at midnight; no endpoint
  value is a left limit (continuity is impossible).
- Counter: replays halving toward END; gap halves, never reaches END,
  epsilon-N, left limit END; Problem 5's limit rule.
- Physical numbers on the 180 mm lines: marks, gaps, clock times; counter sizes
  that still leave END visible; fold error if the paper edge of the cut strip is
  used instead of the MIDNIGHT tick (tick positions read in check_diagrams.py).
- Guide claims: overview times, first-route timing, and the encore's statement
  about the Week 79 numbered-ball process (replayed from its printed rule).
Finite replays are evidence; the infinite statements are proved by hand in math.md.
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from math import ceil, log2
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo(here):
    """Four folders up from plans/review/checks/week-NN/; else walk up."""
    four_up = here.parents[3]
    if (four_up / 'AGENTS.md').is_file():
        return four_up
    for p in here.parents:
        if (p / 'AGENTS.md').is_file() and (p / 'lowell-math-circle-year-2').is_dir():
            return p
    raise SystemExit('repository not found above ' + str(here))


REPO = find_repo(HERE)
STU_TEX = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-80' / 'student' / 'students.tex'
W79_TEX = REPO / 'lowell-math-circle-year-2' / 'source' / 'week-79' / 'student' / 'students.tex'
# Re-pointed on 2026-10-23: the problem-file conversions of Weeks 80 and 79 (a7cb913) removed student/students.tex,
# and the card's shoulds and coulds (bad980d) and the critic follow-up (65fb9bc) changed the packet and guide.  The
# review checks read the copies as reviewed: week-80/archive-before-card-fixes-2026-10-23/ and the reviewed
# students.tex files kept in source/week-NN/archive-before-problem-files-2026-10-23/.
STU_TEX, W79_TEX = (REPO / 'lowell-math-circle-year-2' / 'source' / w / 'archive-before-problem-files-2026-10-23' /
                    'students.tex' for w in ('week-80', 'week-79'))
OUT, FAIL = [], []
N = 200          # switches replayed exactly
LINE_MM = 180    # endpoint ticks are 180 mm apart (confirmed from the PDF in check_diagrams.py)


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def clock(t):
    """t in [0,1] (fraction of the hour after 11:00 p.m.) -> 'hh:mm:ss' string."""
    s = t * 3600
    whole = int(s)
    frac = s - whole
    h, m, sec = 11 + whole // 3600, (whole % 3600) // 60, whole % 60
    txt = f'{h}:{m:02d}:{sec:02d}'
    if frac:
        txt += f'+{frac}s'
    return txt


say(f'repository: {REPO}')
tex = STU_TEX.read_text()
check('A light is OFF at 11:00 p.m. At 11:30 it switches ON; at 11:45 it switches OFF.' in tex,
      'printed opening read from students.tex: OFF at 11:00, ON at 11:30, OFF at 11:45')
check('halfway from the previous switching time to midnight, forever before midnight' in tex,
      'printed rule read: halfway from the previous switching time to midnight')

# ------------------------------------------------------------ switch times by replay
say('== Switch times (replay of the printed rule; 11:00 p.m. = 0, midnight = 1)')
times = [F(1, 2), F(3, 4)]             # 11:30 and 11:45 are given on the page
check(times[1] == (times[0] + 1) / 2, '11:45 is halfway from 11:30 to midnight, so the given pair fits the rule')
check(times[0] == (F(0) + 1) / 2, '11:30 is also halfway from 11:00 to midnight (11:00 is the start, not a switch)')
while len(times) < N:
    times.append((times[-1] + 1) / 2)
check(all(times[n - 1] == 1 - F(1, 2 ** n) for n in range(1, N + 1)), f'closed form t_n = 1 - 2^-n matches the replay for n = 1..{N}')
for n in range(1, 7):
    t = times[n - 1]
    say(f'   switch {n}: t = {t}, clock {clock(t)}, mark at {LINE_MM * t} mm from 11:00, gap to MIDNIGHT {LINE_MM * (1 - t)} mm')
check(clock(times[2]) == '11:52:30', 'guide overview "ON at 11:52:30": third switch time is 11:52:30')
check([LINE_MM * t for t in times[:4]] == [90, 135, F(315, 2), F(675, 4)],
      'first four marks on the 180 mm line: 90, 135, 157.5, 168.75 mm')
check(LINE_MM * (1 - times[3]) == F(45, 4), 'gap after the fourth mark is 11.25 mm (guide: "physically usable gap")')
check(all(times[n - 1] < times[n] < 1 for n in range(1, N)), f'every switch is followed by a later switch before midnight (n < {N})')
# the general step behind "no last switch": t < 1  =>  t < (t+1)/2 < 1
samples = [F(k, 997) for k in range(0, 997)] + [1 - F(1, 2 ** 300)]
check(all(t < (t + 1) / 2 < 1 for t in samples), 'for sampled t < 1, the next halfway time (t+1)/2 lies strictly between t and 1')

# ------------------------------------------------------------ card states
say('== Card (ON/OFF), post-switch states')
state, states = 'OFF', []
for n in range(1, N + 1):
    state = 'ON' if state == 'OFF' else 'OFF'
    states.append(state)
check(states[:4] == ['ON', 'OFF', 'ON', 'OFF'], 'first four post-switch states ON, OFF, ON, OFF (guide overview)')
check(states[3] == 'OFF', 'after the four marks of Problem 1 the card shows OFF')
check(all(states[n - 1] == ('ON' if n % 2 else 'OFF') for n in range(1, N + 1)), 'state after switch n is ON iff n is odd')
check(all(states[n - 1] == 'ON' for n in range(1, N + 1, 2)) and all(states[n - 1] == 'OFF' for n in range(2, N + 1, 2)),
      'odd subsequence constantly ON, even subsequence constantly OFF (guide p. 3): no common limit')


def state_at(t):
    """State at time t in [0,1) under the post-switch convention."""
    k = 0
    while k < N and times[k] <= t:
        k += 1
    if k == N:
        raise ValueError('t beyond replay')
    return 'OFF' if k == 0 else states[k - 1]


check(state_at(F(0)) == 'OFF' and state_at(F(29, 60)) == 'OFF' and state_at(F(1, 2)) == 'ON' and state_at(F(44, 60)) == 'ON'
      and state_at(F(3, 4)) == 'OFF', 'state function: OFF on [11:00, 11:30), ON on [11:30, 11:45), OFF from 11:45')
both = True
for k in range(1, 150):
    eps = F(1, 2 ** k)
    window = [times[n - 1] for n in (k + 1, k + 2)]       # both lie in (1 - eps, 1)
    both &= all(1 - eps < w < 1 for w in window) and {state_at(w) for w in window} == {'ON', 'OFF'}
check(both, 'for eps = 2^-k (k < 150) the interval (1 - eps, 1) contains an ON time and an OFF time')
# continuity at 1 impossible: whatever v is shown at 1, times arbitrarily close show the other state
cont = all(any(state_at(times[n - 1]) != v for n in (k + 1, k + 2)) for v in ('ON', 'OFF') for k in range(1, 150))
check(cont, 'neither ON nor OFF at midnight is a left limit: continuity at 1 is impossible (guide overview)')

# ------------------------------------------------------------ endpoint extensions
say('== Endpoint (Problems 3-4)')
# The printed rule's constraints: the state at 11:00, and a flip at each t_n < 1. Model each as (time, required state).
constraints = [(F(0), 'OFF')] + [(times[n - 1], states[n - 1]) for n in range(1, N + 1)]
check(all(t < 1 for t, _ in constraints), 'every constraint in the printed rule concerns a time strictly before midnight')
ext_on = dict(constraints); ext_on[F(1)] = 'ON'
ext_off = dict(constraints); ext_off[F(1)] = 'OFF'
check(all(ext_on[t] == s and ext_off[t] == s for t, s in constraints), 'both endpoint extensions satisfy every prescribed constraint')
check(ext_on[F(1)] != ext_off[F(1)], 'the two extensions differ at midnight: the rule alone does not determine the midnight state')
# "flip at midnight" or "keep the last state" rules need a state just before midnight, i.e. a last switch or a left limit
check(not any(times[n - 1] >= times[n] for n in range(1, N)), 'no last switch exists in the replay, so "the state after the last switch" is undefined')

# ------------------------------------------------------------ counter
say('== Counter (Problem 2 and Problem 5)')
pos, positions = F(0), []
for n in range(1, N + 1):
    pos = pos + (1 - pos) / 2           # halfway from its present place toward END
    positions.append(pos)
check(all(positions[n - 1] == 1 - F(1, 2 ** n) for n in range(1, N + 1)), 'counter positions equal 1 - 2^-n (replay)')
check(all((1 - positions[n]) * 2 == 1 - positions[n - 1] for n in range(1, N)), 'each move halves the remaining distance (guide p. 3)')
check(all(p < 1 for p in positions), 'the counter never reaches END after a finite number of moves')
check([LINE_MM * p for p in positions[:4]] == [LINE_MM * t for t in times[:4]],
      'on equal 180 mm lines the counter positions coincide with the time marks (strips side by side)')
ok_eps = True
for eps in [F(1, 10), F(1, 100), F(1, 1000), F(3, 10 ** 6), F(1, 10 ** 12)]:
    n_need = ceil(log2(1 / eps))
    while F(1, 2 ** n_need) >= eps:
        n_need += 1
    ok_eps &= (1 - positions[n_need - 1]) < eps and (n_need == 1 or 1 - positions[n_need - 2] >= eps)
check(ok_eps, 'for each tested tolerance eps there is a first N with gap < eps (guide: "sufficiently many halvings")')
# left limit of the counter's step function at 1 is END; for the card it does not exist
check(all(abs(1 - p) <= F(1, 2 ** n) for n, p in enumerate(positions, 1)), 'counter position at any time in [t_n, 1) is within 2^-n of END: left limit END')
say('   Problem 5 rule "use the state that the earlier states approach": counter -> END; card -> none (no limit)')

# averages (guide: "Averages of states answer a different question")
ons = [1 if s == 'ON' else 0 for s in states]
check(all(F(sum(ons[:m]), m) == (F(1, 2) if m % 2 == 0 else F(m + 1, 2 * m)) for m in range(1, N + 1)),
      'running average of post-switch states is 1/2 or (m+1)/2m: tends to 1/2, a different question from the state')

# ------------------------------------------------------------ physical numbers (not mathematics)
say('== Physical fit on the 180 mm lines (evidence for materials notes)')
for d in [6, 13, 15, 19, 22.5, 25]:
    visible = [n for n in range(1, 7) if LINE_MM * (1 - positions[n - 1]) > F(str(d)) / 2]
    say(f'   counter diameter {d} mm: END tick still uncovered after moves {visible}')
check(LINE_MM * (1 - positions[3]) > F(19, 2), 'a 19 mm counter centred at move 4 still leaves the END tick uncovered (1.75 mm)')
check(not (LINE_MM * (1 - positions[3]) > F(25, 2)), 'a 25 mm counter centred at move 4 covers the END tick')
# fold error on the cut strip: dashed cut rectangle 0..184 mm, ticks at 2 and 182 mm
tick_l, tick_r, edge_r = 2, 182, 184
true_marks, edge_marks = [], []
m_true = m_edge = F(tick_l)
for n in range(4):
    if n == 0:   # first fold: 11:00 onto MIDNIGHT; edge-to-edge gives the same crease because margins are equal
        m_true = F(tick_l + tick_r, 2); m_edge = F(0 + edge_r, 2)
    else:
        m_true = (m_true + tick_r) / 2; m_edge = (m_edge + edge_r) / 2
    true_marks.append(m_true); edge_marks.append(m_edge)
errs = [e - t for e, t in zip(edge_marks, true_marks)]
say('   fold the paper edge instead of the MIDNIGHT tick: mark errors (mm)', [str(e) for e in errs],
    '= seconds', [str(e * 20) for e in errs])
check(errs == [0, 1, F(3, 2), F(7, 4)], 'edge-aligned folding: first mark exact, then errors 1, 1.5, 1.75 mm (at most 35 s) over four marks')

# ------------------------------------------------------------ guide timing
say('== Guide p. 2 timing')
parts = {'handle strips/cards': 2, 'launch': 3, 'marks and flips': 15, 'counter': 10, 'compare what settles': 10, 'endpoint rules': 5}
check(sum(parts.values()) == 45, f'first route totals {sum(parts.values())} minutes after the movement break (fits an hour)')

# ------------------------------------------------------------ guide encore: Week 79 process
say('== Guide p. 4 encore: "each label there does settle, even though the total count does not pass to the membership limit"')
w79 = W79_TEX.read_text()
check("Each day, put the next two numbered cards in A, then move A's smallest card to B." in w79,
      'Week 79 rule read from its students.tex: add two to A, move smallest to B')
D = 400
A, B, nxt = set(), set(), 1
hist = []
for day in range(1, D + 1):
    A |= {nxt, nxt + 1}; nxt += 2
    m = min(A); A.remove(m); B.add(m)
    hist.append((frozenset(A), frozenset(B)))
check(all(len(hist[d - 1][0]) == d for d in range(1, D + 1)), '|A| after day n is n: counts grow without bound')
check(all(k in hist[d - 1][1] for k in range(1, 200) for d in range(k, D + 1)), 'label k is in B on every day >= k: each label settles (in B)')
check(all(k not in hist[d - 1][0] for k in range(1, 200) for d in range(k, D + 1)), 'no label stays in A: the limit membership of A is empty (count 0), while counts -> infinity')
# changed rule (Problem 3 of Week 79): labels also settle; the "count" statement concerns the smallest-card rule
A, B, nxt = set(), set(), 1
okc = True
for day in range(1, D + 1):
    a, b = nxt, nxt + 1; nxt += 2
    A.add(a); B.add(b)
    okc &= len(A) == day and all(k % 2 == 1 for k in A)
check(okc, 'changed rule: odd labels settle in A, so A has n cards and an infinite limit set; the encore sentence fits the smallest-card rule')

say()
say(f'{len(FAIL)} failure(s)')
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
