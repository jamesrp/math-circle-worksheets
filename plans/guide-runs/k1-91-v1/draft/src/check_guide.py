#!/usr/bin/env python3
"""Independent exhaustive checker for the final Week 91 K-1 student packet.

No student checker or generator is imported. The generic graph below implements
follow-NEXT-then-flip. A PDF digest binds the manually inspected diagrams and
page references to this exact final input. Text checks also bind computed answers
to the compiled guide, rather than checking a disconnected answer data file.
Requires Python 3 and Poppler (pdftotext, pdfinfo), no Python packages.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
STUDENT_SHA256 = 'bbf6588bb112f7eadc9f4c480e50315baa44615ad0b3da7c228d04e8082c68c8'


def find_student():
    # Portable package wins. In a run folder, discover the checkout by ancestry.
    candidate = HERE.parent / 'k-1.pdf'
    if candidate.is_file():
        return candidate
    for ancestor in HERE.parents:
        candidate = ancestor / 'plans' / 'k1-drafts' / 'week-91' / 'k-1.pdf'
        if candidate.is_file():
            return candidate
    raise FileNotFoundError('Put the verified k-1.pdf beside src/ (or guide-src/).')


def pdf_text(path):
    return subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)


def compact(text):
    return ' '.join(text.split())


def route(graph, start, n):
    """Internal vertices are integers; string vertices are absorbing exits."""
    state = list(start)
    arrivals, history = [], [tuple(state)]
    for _ in range(n):
        at = 0
        while isinstance(at, int):
            next_vertex = graph[at][state[at]]
            state[at] ^= 1
            at = next_vertex
        arrivals.append(at)
        history.append(tuple(state))
    return ''.join(arrivals), history


SWITCH = {0: ('X', 'Y')}
TREE = {0: (1, 2), 1: ('A', 'B'), 2: ('C', 'D')}
starts = {''.join('LR'[b] for b in bits): bits for bits in product((0, 1), repeat=3)}
words = {s: route(TREE, bits, 64)[0] for s, bits in starts.items()}
assert len(starts) == 2 * 2 * 2 == 8

student = find_student()
assert sha256(student.read_bytes()).hexdigest() == STUDENT_SHA256, 'Student PDF changed: re-inspect before updating this check.'
student_text = pdf_text(student)
student_pages = student_text.split('\f')
assert not student_pages[-1].strip()
student_pages.pop()
assert len(student_pages) == 7
page_map = {1: (1,), 2: (2,), 3: (3, 4), 4: (5,), 5: (6,), 6: (7, 8), 7: (9,)}
for page_no, expected in page_map.items():
    found = tuple(map(int, re.findall(r'Problem (\d+):', student_pages[page_no - 1])))
    assert found == expected, (page_no, found)
    assert 'F91-K-v1' in student_pages[page_no - 1]
assert 'send 10 counters' in compact(student_pages[0])
assert 'Copy the starting arrows with spare cards' in compact(student_pages[0])
assert '5 counters on one exit and 2 on the other' in compact(student_pages[2])
assert 'first counter lands on C' in compact(student_pages[5])
assert '8 counters' in student_pages[4] and '12 counters' in student_pages[4]
print('INPUT PASS: exact final 7-page PDF, P1-P9 page mapping and revised text verified.')

guide = HERE.parent / 'k1-guide.pdf'
guide_text = pdf_text(guide)
guide_pages = guide_text.split('\f')
assert not guide_pages[-1].strip()
guide_pages.pop()
assert len(guide_pages) == 4
for i, page in enumerate(guide_pages, 1):
    assert 'Week 91 / Rotor-router machines / K–1 adult guide' in page
    assert 'Bellingham Math Circle / Week 91 / F91-K-FAC-v1' in page
    assert re.search(rf'\b{i}\s*$', page)
info = subprocess.check_output(['pdfinfo', str(guide)], text=True)
assert re.search(r'Page size:\s+612 x 792 pts', info), info

sections = {}
for n in range(1, 10):
    match = re.search(rf'Problem {n}, student page \d+:', guide_text)
    assert match, n
    end = re.search(rf'Problem {n+1}, student page \d+:', guide_text[match.end():]) if n < 9 else None
    sections[n] = compact(guide_text[match.start():match.end() + end.start()] if end else guide_text[match.start():])


def contains(n, expected):
    assert compact(expected) in sections[n], (n, expected)


# P1 and the general alternating-pile assertion: both starts, all prefixes to 64.
switch_words = {}
for b, first in enumerate('XY'):
    w, _ = route(SWITCH, (b,), 64)
    assert not any(a == z for a, z in zip(w, w[1:]))
    for count in range(65):
        assert abs(w[:count].count('X') - w[:count].count('Y')) <= 1
    switch_words[first] = w
    contains(1, w[:10])
    assert Counter(w[:10]) == Counter(X=5, Y=5)
contains(1, 'five at each exit')
print('P1 PASS:', {k: v[:10] for k, v in switch_words.items()})

# P2: the six diagram piles were transcribed from the rendered final PDF.
p2_targets = [(2, 1), (3, 3), (2, 3), (5, 2), (5, 4), (3, 5)]
p2 = [tuple(k for k, w in switch_words.items() if tuple(w[:sum(t)].count(c) for c in 'XY') == t) for t in p2_targets]
assert p2 == [('X',), ('X', 'Y'), ('Y',), (), ('X',), ()]
contains(2, 'Piles X,Y 2,1 3,3 2,3 5,2 5,4 3,5')
contains(2, 'Start X either Y impossible X impossible')
for b in (0, 1):
    _, history = route(SWITCH, (b,), 64)
    assert all(history[n][0] != b for n in range(1, 64, 2))
print('P2 PASS:', list(zip(p2_targets, p2)))

# P3: all coin words; six printed rows, not the old five-row single-direction task.
coin7 = [''.join(x) for x in product('XY', repeat=7)]
successful = [w for w in coin7 if sorted(Counter(w).values()) == [2, 5]]
assert len(coin7) == 128 and len(successful) == 42
assert 'XXXXXYY' in successful
witness = 'XXXXXYY'
assert any(a == b for a, b in zip(witness, witness[1:]))
miss = (1 - len(successful) / len(coin7)) ** 6
assert round(100 * miss, 1) == 9.2
contains(3, 'XXXXXYY')
contains(3, '42 of the 128')
contains(3, 'six trials miss that split about 9.2%')
print(f'P3 PASS: {len(successful)}/{len(coin7)}; six-trial miss {100 * miss:.6f}%.')

# P4: exact printed counter indices and both first exits; coin conditional outcomes.
indices = (5, 8, 7, 4)
for first, w in switch_words.items():
    predicted = tuple(w[k - 1] for k in indices)
    assert predicted == (first, 'Y' if first == 'X' else 'X', first, 'Y' if first == 'X' else 'X')
contains(4, 'Counter 5 8 7 4')
contains(4, 'Card, compared with counter 1 same other same other')
contains(4, 'X, Y, X, Y')
contains(4, 'Y, X, Y, X')
coin8 = list(product('XY', repeat=8))
for first in 'XY':
    conditional = [w for w in coin8 if w[0] == first]
    for k in indices:
        assert sum(w[k-1] == 'X' for w in conditional) == len(conditional) // 2
print('P4 PASS: both starts; 256 fair-coin words, all four requested indices.')

# P5: exhaustive start/order key, all length-four windows and return states.
expected_orders = dict(LLL='ACBD', LLR='ADBC', LRL='BCAD', LRR='BDAC', RLL='CADB', RLR='DACB', RRL='CBDA', RRR='DBCA')
assert {s: w[:4] for s, w in words.items()} == expected_orders
assert len(set(expected_orders.values())) == 8
for s, w in words.items():
    _, history = route(TREE, starts[s], 64)
    for i in range(61):
        assert set(w[i:i+4]) == set('ABCD')
        assert history[i+4] == history[i]
    contains(5, f'{s} {w[:4]}')
print('P5 PASS: all 8 starts; 488 four-counter windows; state returns after four.')

# P6: exactly the six final targets, with every realizing start.
p6_targets = [(8, (2, 2, 2, 2)), (6, (2, 1, 2, 1)), (6, (2, 2, 1, 1)), (12, (3, 3, 3, 3)), (6, (1, 2, 1, 2)), (8, (3, 1, 2, 2))]
p6 = [tuple(s for s, w in words.items() if tuple(w[:n].count(c) for c in 'ABCD') == t) for n, t in p6_targets]
assert p6 == [tuple(starts), ('LLL', 'RLL'), (), tuple(starts), ('LRR', 'RRR'), ()]
labels = ['top left', 'top right', 'middle left', 'middle right', 'bottom left', 'bottom right']
for i, ((n, piles), valid) in enumerate(zip(p6_targets, p6), 1):
    assert sum(piles) == n
    answer = 'all eight' if len(valid) == 8 else ', '.join(valid) if valid else 'impossible'
    contains(6, f'{i} ({labels[i-1]}) {n} {",".join(map(str, piles))} {answer}')
for bits in starts.values():
    _, history = route(TREE, bits, 6)
    assert history[6] == (bits[0], 1-bits[1], 1-bits[2])
print('P6 PASS:', list(zip(p6_targets, p6)))

# P7: second-arrival times determine both first and last.
def second_time(word, letter):
    return [i for i, c in enumerate(word, 1) if c == letter][1]

first = {s: second_time(w, 'B') for s, w in words.items() if second_time(w, 'B') == min(second_time(w, c) for c in 'ABCD')}
last = {s: second_time(w, 'B') for s, w in words.items() if second_time(w, 'B') == max(second_time(w, c) for c in 'ABCD')}
assert first == {'LRL': 5, 'LRR': 5} and last == {'RLL': 8, 'RLR': 8}
contains(7, 'counter 5 from LRL or LRR')
contains(7, 'counter 8 from RLL or RLR')
contains(7, 'BCAD or BDAC')
contains(7, 'CADB or DACB')
print('P7 PASS:', first, last)

# P8: literal find-all task, both complete starts and the free unused card.
p8 = [s for s, w in words.items() if w[0] == 'C']
assert p8 == ['RLL', 'RRL']
contains(8, 'Exactly two complete settings: RLL and RRL')
assert all(starts[s][0] == 1 and starts[s][2] == 0 for s in p8)
print('P8 PASS:', p8)

# P9: each diagram's numbered exit pair, including both impossibilities.
p9 = {target: [s for s, w in words.items() if w[:2] == target] for target in ('AD', 'DC', 'CB', 'BA')}
assert p9 == {'AD': ['LLR'], 'DC': [], 'CB': ['RRL'], 'BA': []}
contains(9, 'A then D: LLR only')
contains(9, 'D then C: impossible')
contains(9, 'C then B: RRL only')
contains(9, 'B then A: impossible')
print('P9 PASS:', p9)

# Non-mathematical printed facts: material arithmetic and explicit limits.
assert 2 * 7 == 14 and 2 * 16 == 32 and 2 * 2 == 4
assert sum((5, 5, 3, 15, 10, 15, 7)) == 60
full = compact(guide_text)
for phrase in ('14 tree cards, 32 counters, two coins', 'Unpiloted', 'physically unrehearsed', 'including its final two lines at the top of page 3'):
    assert phrase in full, phrase
print('OUTPUT PASS: four US Letter guide pages, exact headers/footers and compiled answer text verified.')
print('All independent mathematical checks passed. No physical or classroom validation is implied.')
