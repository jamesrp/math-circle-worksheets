#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card shoulds in Week 44 (plans/review/week-44.md).

Usage: python3 review/verify_card_shoulds_2026_10_23.py [folder with the built PDFs]
(default: reference-pdfs/ beside this folder). Needs PyMuPDF for the PDF checks.

1. Mathematics of every changed key, by enumerating marked histories of the copying bag:
   the K-1 identity reading of Problem 1, the 3R/2B follow-up of Problem 2, the
   blue-majority bags and story counts of Problem 3, the story counts of Grades 2-3
   Problem 5, the new Grades 2-3 Problem 6 (both bags 1/5), and the counters a pair needs.
2. The problem files' wording: "color stories", "Which of these bags", the cut sentences,
   "marked histories" and "if any" in Grades 4-5, "1 red draw".
3. The built packets: v3 footers; K-1 Problem 3 has eight story rows and two bag boxes with
   rows; Grades 2-3 has five pages, a spare slot in Problem 1, a box for Problem 4, room for
   2, 6 and 8 stories in Problem 5 and the new Problem 6 on page 5.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def histories(n, bag=('R1', 'B1'), marks=()):
    """Every marked history of n copying draws: (marks drawn, final bag)."""
    if not n:
        yield marks, bag
        return
    for c in bag:
        yield from histories(n - 1, bag + (c[0] + str(len(bag)),), marks + (c,))  # a copy's mark is its birth step


def word(marks):
    return ''.join(m[0] for m in marks)


def counts(bag):
    return (sum(c[0] == 'R' for c in bag), sum(c[0] == 'B' for c in bag))


# 1. Mathematics
two = list(histories(2))
by_bag = Counter(counts(b) for _, b in two)
colour = {}
for m, b in two:
    colour.setdefault(counts(b), set()).add(word(m))
check(len(two) == 6 and set(by_bag.values()) == {2},
      'K-1 P1 key: counted by marked counters, every two-draw bag has two stories')
check({k: len(v) for k, v in colour.items()} == {(3, 1): 1, (2, 2): 2, (1, 3): 1},
      'K-1 P1 key: only 2R/2B has two color stories (RB, BR)')
ex = {tuple(word(m) for m, b in two if counts(b) == k) for k in by_bag}
check(sorted(sorted(e) for e in ex) == [['BB', 'BB'], ['BR', 'RB'], ['RR', 'RR']],
      'K-1 P1 key: the marked pairs are R1 R1 / R1 R2, R1 B1 / B1 R1, B1 B1 / B1 B2')
three = {counts(b) for _, b in histories(3)}
check(three == {(4, 1), (3, 2), (2, 3), (1, 4)} and (5, 0) not in three,
      'K-1 P2 key: three-draw bags are 4R/1B, 3R/2B, 2R/3B, 1R/4B; 3R/2B is the unprinted follow-up')
check(sorted({word(m) for m, b in histories(3) if counts(b) == (3, 2)}) == ['BRR', 'RBR', 'RRB'],
      'K-1 P2 key: 3R/2B comes from RRB, RBR or BRR')
four = list(histories(4))
stories = {}
for m, b in four:
    stories.setdefault(counts(b), set()).add(word(m))
check(len(stories[(3, 3)]) == 6 and len(stories[(3, 3)]) <= 8, 'K-1 P3: six color stories end at 3R/3B; eight rows leave two spare')
check({k for k in stories if k[1] > k[0]} == {(1, 5), (2, 4)}, 'K-1 P3 key: the blue-majority four-draw bags are 1R/5B and 2R/4B (two bag boxes)')
check([len(stories[k]) for k in ((5, 1), (4, 2), (3, 3))] == [1, 4, 6], '2-3 P5: 5R/1B, 4R/2B, 3R/3B have 1, 4 and 6 color stories (room for 2, 6, 8)')
check(len(four) == 120, '2-3 P6 key: four copying draws have 120 marked histories')
per_word = Counter(word(m) for m, _ in four)
check(per_word['RRRR'] == 24 and all(per_word[w] == 4 for w in stories[(3, 3)]),
      '2-3 P6 key: RRRR has 24 marked histories and each of the six 3R/3B stories has 4')
p51 = Fraction(sum(counts(b) == (5, 1) for _, b in four), 120)
p33 = Fraction(sum(counts(b) == (3, 3) for _, b in four), 120)
check(p51 == p33 == Fraction(1, 5), '2-3 P6 key: five red and one blue and three red and three blue both have chance 1/5')
check(Counter(word(m).count('R') for m, _ in two) == {0: 2, 1: 2, 2: 2}, '2-3 P1 key unchanged: two histories per two-draw total')
# Materials: six of each colour per pair holds K-1 P1's three bags side by side and a five-draw one-colour story.
side = [sum(c) for c in zip(*by_bag)]
five = max(max(counts(b)) for _, b in histories(5))
check(side == [6, 6] and five == 6, f'guide p. 2: K-1 P1\'s three bags together hold {side[0]} red and {side[1]} blue, and a five-draw one-color bag {five} of a color: six of each per pair')

# 2. Wording in the problem files
PROBLEMS = next(p for p in (ROOT.parent / 'problems', ROOT / 'problem-files' / 'problems') if p.is_dir())
text = {p.name: p.read_text() for p in PROBLEMS.glob('*.md')}


def student(s):
    return ''.join(x for x in re.split(r'^## ', s, flags=re.M)[1:] if x.startswith(('prompt', 'text')))


everything = ''.join(student(s) for s in text.values())
k1_rules = re.search(r'## text [^\n]*\[K-1\]\n(.*?)\n\n', text['00-rules.md'], re.S).group(1)
check('For random play' not in k1_rules, 'K-1 page 1 drops "For random play, each counter has the same chance"')
check('two different color stories?' in text['01-k1-two-draw-bags.md'], 'K-1 P1 asks about two different color stories')
check('Which of these bags can you make after three draws?' in text['02-k1-three-draw-bags.md'], 'K-1 P2 asks "Which of these bags"')
check('Each counter in the bag has the same chance of being drawn.' not in everything, '2-3 P2 drops its repeat of the random-play rule')
check('Find every color story for each final bag below.' in text['15-four-draw-bags.md'], '2-3 P5 asks for every color story')
check('which bag is more likely, if either: five red and one blue, or three red and three blue?' in text['16-which-bag.md']  # 'if either' since the critic follow-up
      and 'vanish' not in everything, '2-3 P6 is the new four-draw comparison')
check('further question' not in everything, '4-5 P6 drops "an exact argument for every length is a further question"')
check('marked stories' not in student(''.join(v for k, v in text.items() if k.startswith('2'))) and 'if any' in text['21-marked-stories.md'],
      '4-5 says "marked histories" throughout and P1 adds "if any"')

# 3. The built PDFs
try:
    import pymupdf
except ImportError:
    pymupdf = None
folder = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'reference-pdfs'
if pymupdf is None:
    print('SKIP PDF checks: PyMuPDF is not installed')
else:
    MM = 25.4 / 72
    docs = {b: pymupdf.open(folder / f'{b}.pdf') for b in ('k-1', 'grades-2-3', 'grades-4-5')}
    for b, d in docs.items():
        v = 'v4' if b == 'grades-2-3' else 'v3'  # Grades 2-3 became v4 in the critic follow-up
        check(all(f'W44-{b}-{v}' in p.get_text() for p in d), f'{b}: every page carries W44-{b}-{v}')

    def boxes(page, w, h, tol=.05):
        return sorted({(round(dr['rect'].x0 * MM / 10, 1), round(dr['rect'].y0 * MM / 10, 1)) for dr in page.get_drawings()
                       if dr['type'] == 's' and abs((dr['rect'].x1 - dr['rect'].x0) * MM / 10 - w) < tol
                       and abs((dr['rect'].y1 - dr['rect'].y0) * MM / 10 - h) < tol})

    k = docs['k-1']
    check(len(k) == 4 and len(boxes(k[2], 1.9, 1.8)) == 4 * 10 and len(boxes(k[2], 7.6, 3)) == 2,
          f'K-1 p. 3: ten four-cell rows (eight stories, two under the bag boxes) and two bag boxes')
    m = docs['grades-2-3']
    nums = [sorted(set(re.findall(r'Problem (\d):', p.get_text()))) for p in m]
    check(len(m) == 5 and nums == [['1'], ['2'], ['3', '4'], ['5'], ['6']], f'2-3: five pages with problems {nums}')
    check(len(boxes(m[0], 2.2, 1.8)) == 10 and len(boxes(m[0], 7.8, 2.6)) == 5, '2-3 p. 1: five story slots, one spare')
    check(len(boxes(m[2], 18, 4.3)) == 1, '2-3 p. 3: Problem 4 has an unlabelled box')
    check(len(boxes(m[3], 1.5, 1.8)) == 4 * 16, '2-3 p. 4: sixteen four-cell rows: 2, 6 and 8 for the three bags')
    check('five red and one blue' in ' '.join(m[4].get_text().split()), '2-3 p. 5: the new Problem 6')
    u = docs['grades-4-5']
    t = ' '.join(' '.join(p.get_text().split()) for p in u)
    check('1 red draw ' in t + ' ' and '1 red draws' not in t and 'marked stories' not in t and 'if any' in t,
          '4-5: "1 red draw", "marked histories" only, and "if any"')
print(f'{len(fails)} failure(s)')
raise SystemExit(1 if fails else 0)
