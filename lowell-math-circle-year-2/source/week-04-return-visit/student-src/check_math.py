#!/usr/bin/env python3
"""Independent finite checks for every represented Week 4 writer instance."""
import itertools
import json
import math
from collections import deque
from pathlib import Path

def meeting(n, r, b, red_hop, blue_hop):
    seen = {(r, b)}
    landings = []
    while True:
        r = (r + red_hop) % n
        b = (b + blue_hop) % n
        landings.append((r, b))
        if r == b:
            return len(landings), r, landings
        if (r, b) in seen:
            return None, None, landings
        seen.add((r, b))

assert (11+2) % 12 == 1 and (6+5) % 12 == 11
results = {}
for b, expected in [(0, (4, 8)), (1, (None, None)), (3, (3, 6))]:
    t, dot, path = meeting(12, 0, b, 2, 5)
    assert (t, dot) == expected
    results[f'meeting_blue_start_{b}'] = {'first_turn': t, 'circle': dot, 'landings': path}
for r in range(12):
    for b in range(12):
        t, dot, _ = meeting(12, r, b, 2, 5)
        assert (t is not None) == ((b-r) % math.gcd(12, 2-5) == 0)
        if t is not None:
            assert ((r+2*t) % 12, (b+5*t) % 12) == (dot, dot)

def routes(hops):
    shortest = {0: ()}
    todo = deque([0])
    while todo:
        now = todo.popleft()
        for hop in hops:
            nxt = (now+hop) % 12
            if nxt not in shortest:
                shortest[nxt] = shortest[now] + (hop,)
                todo.append(nxt)
    return shortest

assert [sum((4,4,3,4)[:i]) % 12 for i in range(5)] == [0,4,8,11,3]
for hops, targets in [((3,4), {1:4, 2:4}), ((4,6), {1:None, 2:3})]:
    paths = routes(hops)
    assert set(paths) == set(range(0,12, math.gcd(12,*hops)))
    target_details = {}
    for target, length in targets.items():
        if length is None:
            assert target not in paths
            target_details[target] = {'distance': None, 'words': []}
            continue
        assert len(paths[target]) == length
        words = [word for word in itertools.product(hops, repeat=length) if sum(word) % 12 == target]
        assert words
        for shorter in range(length):
            assert not any(sum(word)%12 == target for word in itertools.product(hops, repeat=shorter))
        target_details[target] = {'distance': length, 'words': words}
    results[f'hop_choices_{hops[0]}_{hops[1]}'] = {'reachable': sorted(paths), 'targets': target_details}

def rotations(word):
    return {word[i:]+word[:i] for i in range(len(word))}

four_before = 'RBBB'
four_after = 'BRBB'
assert four_after in rotations(four_before)
all_necklaces = {''.join('R' if i in places else 'B' for i in range(6)) for places in itertools.combinations(range(6),3)}
classes = {}
for word in all_necklaces:
    classes.setdefault(min(rotations(word)), set()).add(word)
assert len(all_necklaces) == 20 and len(classes) == 4
assert sorted(map(len, classes.values())) == [2,6,6,6]
necklace_details = {}
for representative, words in sorted(classes.items()):
    turn_matches = [k for k in range(1,6) if representative[k:]+representative[:k] == representative]
    necklace_details[representative] = {'labeled_patterns': sorted(words), 'smaller_turns_matching': turn_matches}
assert [info['smaller_turns_matching'] for info in necklace_details.values()].count([2,4]) == 1
assert sum(bool(info['smaller_turns_matching']) for info in necklace_details.values()) == 1
assert len({min(rotations(w) | rotations(w[::-1])) for w in all_necklaces}) == 3
results['necklaces'] = necklace_details
results['physical_geometry_mm'] = {
    'working_12_ring_circle_diameter': 21,
    'working_12_ring_adjacent_centers': 2*46*math.sin(math.pi/12),
    'working_12_ring_edge_gap': 2*46*math.sin(math.pi/12)-21,
    'working_6_ring_circle_diameter': 21,
    'working_6_ring_adjacent_centers': 26.5,
    'working_6_ring_edge_gap': 5.5,
    'record_6_ring_circle_diameter': 7,
}
assert results['physical_geometry_mm']['working_12_ring_edge_gap'] > 2.8
output = Path(__file__).resolve().parent / 'math-results.json'
output.write_text(json.dumps(results, indent=2) + '\n')
print(f'PASS: represented examples, 144 meeting starts, two complete hop graphs, all 20 necklaces; {output}')
