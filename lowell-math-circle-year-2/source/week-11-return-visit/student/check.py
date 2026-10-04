"""Independent standard-library checks for the Week 11 student instances."""
import itertools
import json
from functools import lru_cache
from pathlib import Path


def closed_next(state):
    for i in range(3):
        if state[i] >= 2:
            out = list(state)
            out[i] -= 2
            for j in range(3):
                if j != i:
                    out[j] += 1
            yield tuple(out)


def closure(start):
    seen = {start}
    todo = [start]
    while todo:
        for nxt in closed_next(todo.pop()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return sorted(seen)


@lru_cache(None)
def avalanche_words(state):
    choices = []
    for i, label in enumerate('ABC'):
        if state[i] >= 2:
            nxt = list(state)
            nxt[i] -= 2
            if i > 0:
                nxt[i-1] += 1
            if i < 2:
                nxt[i+1] += 1
            for suffix, finish in avalanche_words(tuple(nxt)):
                choices.append((label + suffix, finish))
    return choices or [('', state)]


closed = []
convention_start = (2, 0, 0)
assert list(closed_next(convention_start)) == [(0, 1, 1)]
for state in [(3, 0, 0), (2, 1, 0), (4, 0, 0)]:
    states = closure(state)
    stable = [s for s in states if max(s) < 2]
    closed.append({'start': state, 'reachable_states': states, 'stable': stable})
assert closed[0]['stable'] == [(1, 1, 1)]
assert closed[1]['stable'] == closed[2]['stable'] == []
assert (0,2,1) in closed[1]['reachable_states']
assert (1,0,2) in closed[1]['reachable_states']

trials = []
for start in itertools.product(range(2), repeat=3):
    for added in range(3):
        perturbation = list(start)
        perturbation[added] += 1
        words = avalanche_words(tuple(perturbation))
        assert len({finish for _, finish in words}) == 1
        assert len({len(word) for word, _ in words}) == 1
        trials.append({'start': start, 'add_at': 'ABC'[added], 'words': words,
                       'length': len(words[0][0])})
max_length = max(t['length'] for t in trials)
longest = [t for t in trials if t['length'] == max_length]
assert max_length == 4
assert [(t['start'], t['add_at']) for t in longest] == [((1,1,1), 'B')]

inverse = []
for a in range(7):
    b = 6-a
    for word in map(''.join, itertools.product('AB', repeat=4)):
        state = [a,b,0]
        for label in word:
            i = 'AB'.index(label)
            if state[i] < 2:
                break
            state[i] -= 2
            state[1-i] += 1
            state[2] += 1
        else:
            if state == [1,1,4]:
                inverse.append({'start': [a,b], 'word': word})
assert len(inverse) == 8
assert sorted({tuple(t['start']) for t in inverse}) == [(0,6),(3,3),(6,0)]
result = {'convention_example': {'start': convention_start, 'word': 'A', 'finish': (0, 1, 1)},
          'closed_triangle': closed, 'avalanche_trials': trials,
          'maximum_avalanche_length': max_length, 'inverse_histories': inverse}
output = Path(__file__).resolve().parent.parent/'writer-math-check.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print('Passed: 3 closed-board starts, all 24 avalanche trials and all legal orders, 3 inverse starts and 8 histories.')
