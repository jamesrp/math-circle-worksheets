#!/usr/bin/env python3
"""Check the October 23, 2026 card fixes to Week 46 (shoulds 1-5, coulds 6-10 and 12) by
enumeration and by reading the reference PDFs.

The boards are words of length three in R and B. Every changed claim is recomputed: the
launch pair is not a task pair, the new "two different" examples exist, the K-1 Problem 4
two-instruction story, the printed toggle pairs, the three mixed stories of Grades 4-5
Problem 5 and the slot-story distribution. Nothing is imported from the builders. Run from
anywhere:
    python3 review/verify_card_shoulds_2026_10_23.py
Coulds 11 and 13 (counter size, cut cards, the bonus guide's Problem 1) are checked in the
repository by plans/review/checks/week-46/check_card_shoulds.py.
"""
import re
from collections import Counter
from itertools import product
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
CM = 72 / 2.54
WORDS = [''.join(w) for w in product('RB', repeat=3)]
checks = []


def run(start, story):
    """A story is a list of (slot, color) with color R, B or T (toggle)."""
    s = list(start)
    for slot, c in story:
        i = slot - 1
        s[i] = ('B' if s[i] == 'R' else 'R') if c == 'T' else c
    return ''.join(s)


def dist(a, b):
    return sum(x != y for x, y in zip(a, b))


def N(s):
    """Drop hyphens and a following space, so a word hyphenated at a line end still matches."""
    return re.sub(r'-\s?', '', s)


class T(str):
    """Page text whose `in` and startswith ignore hyphenation."""
    def __contains__(self, s):
        return N(s) in N(str(self))

    def startswith(self, s):
        return N(str(self)).startswith(N(s))


def text(page):
    return T(' '.join(page.get_text().split()))


k1, b23, b45 = (pymupdf.open(REF / f) for f in ('k-1.pdf', 'grades-2-3.pdf', 'grades-4-5.pdf'))
guide = pymupdf.open(REF / 'facilitator-guide.pdf')
g = [text(p) for p in guide]
pages = {(n, i + 1): text(p) for n, d in (('K-1', k1), ('2-3', b23), ('4-5', b45)) for i, p in enumerate(d)}
assert (len(k1), len(b23), len(b45)) == (4, 4, 5)
for (n, i), t in pages.items():
    assert f"W46-{ {'K-1': 'k-1', '2-3': 'grades-2-3', '4-5': 'grades-4-5'}[n] }-v4" in t, (n, i)  # v4 since the critic follow-up

# --- Should 1: the launch pair ------------------------------------------------------------
task_pairs = {('RBR', 'BRB'), ('RBR', 'RRR'), ('RRB', 'BRR'), ('BRB', 'BRB'), ('RRR', 'BBB')}
assert ('BBR', 'RBB') not in task_pairs and ('RBB', 'BBR') not in task_pairs
assert run('BBR', [(1, 'B')]) == 'BBR' and run('RBB', [(1, 'B')]) == 'BBB'
for d in (k1, b23, b45):
    words = [w[4] for w in d[0].get_text('words') if w[4] in ('R', 'B') and w[1] < 7.5 * CM]
    assert ''.join(words).count('R') == 3, words          # BBR, RBB, BBR, BBB: three reds
assert 'This pair is not on any page' in g[1] and 'What could we do next' not in g[1]
checks.append('should 1: page 1 of every band shows BBR/RBB with 1->B (BBR stays, RBB becomes BBB), a pair on '
              'no page; the guide launch uses it and no longer asks what to do next')

# --- Should 2 and 3: the guide -------------------------------------------------------------
run_ = ' '.join(g[1:3])
assert 'Each child in a pair owns one board' in run_ and 'the third child referees' in run_
assert 'About 40 minutes at the tables' in run_ and 'Stopping after' not in ' '.join(g)
assert 'K-1: Problems 1 and 2 (fewest repairs), Problem 4 (two instructions that sometimes match), then the ' \
       'random draws of Problems 6-7' in run_
route = g[-1]
assert 'K-1 P1, P2, P4 and P6-7' in route and 'each child owns one board' in route
checks.append('should 2: guide pp. 2-3 give each child one board, every instruction read aloud and applied by both, '
              'a referee at Grades 4-5; should 3: one plan for about 40 table minutes, the "sufficient" sentence '
              'gone, and a K-1 first route of P1, P2, P4 (the two-instruction story, was P5), P6, P7')

# --- Should 4: "two different" -------------------------------------------------------------
assert 'Make two different starts that end matching, and a pair that ends different.' in pages[('K-1', 3)]
assert 'Can two different starting boards match before all three slots are marked?' in pages[('2-3', 2)]
assert 'Could two different starts agree before that happens?' in pages[('4-5', 2)]
story = [(1, 'R'), (3, 'B')]
same = [(a, b) for a in WORDS for b in WORDS if a < b and run(a, story) == run(b, story)]
diff = [(a, b) for a in WORDS for b in WORDS if a < b and run(a, story) != run(b, story)]
assert ('BRB', 'RRR') in same and ('BBB', 'RRR') in diff and all(a[1] == b[1] for a, b in same)
early = [(a, b) for a in WORDS for b in WORDS if a < b and run(a, [(1, 'R')]) == run(b, [(1, 'R')])]
assert ('BRR', 'RRR') in early and all(dist(a, b) == 1 for a, b in early)
checks.append('should 4: K-1 P4, Grades 2-3 P3 and Grades 4-5 P3 ask for two different starts; after 1->R, 3->B '
              'different starts match exactly when their middle colors agree (RRR/BRB), and RRR/BRR match after '
              '1->R alone, so each question has a non-trivial answer')

# --- Should 5 and could 10: Grades 4-5 Problems 4-5 ----------------------------------------
pairs = [('RBR', 'RRR'), ('RRB', 'BRR'), ('BRB', 'BRB')]
toggles = [s for n in range(5) for s in product([(i, 'T') for i in (1, 2, 3)], repeat=n)]
for a, b in pairs:
    assert {dist(run(a, s), run(b, s)) for s in toggles} == {dist(a, b)}
tokens = [w[4] for w in b45[2].get_text('words') if w[4] in ('R', 'B')]
assert len(tokens) == 12 + 18                         # the toggle picture's two pairs, then three printed pairs
stories = [[(1, 'R'), (1, 'T'), (2, 'B'), (3, 'R')], [(3, 'B'), (2, 'T'), (1, 'R'), (2, 'T')],
           [(3, 'T'), (2, 'R'), (3, 'B'), (1, 'B'), (3, 'T')]]
finishes = [sorted({run(w, s) for w in WORDS}) for s in stories]
assert finishes == [['BBR'], ['RBB', 'RRB'], ['BRR']]
set_every_slot = [all(any(p == i and c != 'T' for p, c in s) for i in (1, 2, 3)) for s in stories]
assert set_every_slot == [True, False, True]
p5 = pages[('4-5', 4)]
assert p5.startswith('Week 46 / Two boards forget their starts / Grades 4–5 Problem 5: Allow both color-setting '
                     'instructions and toggles, as in these stories.')
assert 'Explain why it works and why every story without it fails.' in p5 and 'both directions' not in p5
assert p5.count('toggle ') == 5 and p5.count('finish') == 1 + 3          # five toggle cards; three finish boards
k = ' '.join(g[4:6])
assert 'always finishes BBR' in k and 'RBB or RRB' in k and 'always finishes BRR' in k
checks.append('should 5: Grades 4-5 P4 prints the three toggle pairs (shared toggles keep the disagreement count: '
              '1, 2, 0); P5 has its own page with three card stories, which finish BBR always, RBB or RRB (slot 2 '
              'only toggled), and BRR always, as the guide keys them; could 10: "why it works and why every story '
              'without it fails"')

# --- Coulds 6, 7, 8, 9, 12 -----------------------------------------------------------------
t2 = pages[('2-3', 2)]
assert 'above a slot' not in t2 and t2.index('Problem 2') < t2.index('mark a slot') and 'Put a small marker' not in t2
checks.append('coulds 6-7: Grades 2-3 p. 2 no longer says "above a slot", and marking slots comes in Problem 3, '
              'after Problem 2\'s stories are run')
t5 = pages[('4-5', 5)]
assert 'Thus each slot has the same chance' not in t5 and 'chosen slots' not in ' '.join(pages.values())
assert 'Suppose four draws name slots 1, 3, 1, 2, in that order.' in t5 and 'any slot story' in t5
assert 'position story' not in ' '.join(g) and 'slot story' in ' '.join(g)
final = Counter((c3, c4, c2) for c1, c2, c3, c4 in product('RB', repeat=4))
assert len(final) == 8 and set(final.values()) == {2}
assert 'can all name the same slot' in g[0] and 'revisit one slot' not in g[0]
checks.append('coulds 8, 9, 12: the Grades 4-5 draw rule is one sentence; pages and guide say "slot story"; '
              'slots 1, 3, 1, 2 give each of the 8 boards 2 of 16 color stories; the guide says ten draws "can all '
              'name the same slot"')

for c in checks:
    print('PASS', c)
