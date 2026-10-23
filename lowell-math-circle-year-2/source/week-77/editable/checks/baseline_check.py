#!/usr/bin/env python3
"""Independent review of the final printed draft, Problems 1--5.

This was written without reading, importing, or running draft/src/check_math.py.
Inputs below were transcribed from students.pdf and the TikZ coordinates. Rather
than pair cavities visually or trust Euler's formula, enumerate edge chains,
require even degree at every vertex, enumerate triangle-boundary sums, and form
actual equivalence classes. Inclusion sends the SAME edge chain to the later
boundary quotient. All arithmetic is exact, using finite sets and integers.

Problem 5, general proof (the finite check is not its proof): if saved edge chain
L cancels against boundaries of a set T of filled triangles at stage s, that same
set T is available at every later stage. Their boundaries and L have not changed.
Thus the same cancellation certifies L is gone later. New edges and triangles do
not invalidate an existing witness. This argument applies to every legal growing
board, independent of planarity, and does not rename L as a different loop.
"""
from itertools import combinations, permutations
from math import log2
import json


def edge(a, b):
    return ''.join(sorted((a, b)))


def subsets(items):
    items = tuple(items)
    for n in range(len(items) + 1):
        for selected in combinations(items, n):
            yield frozenset(selected)


def boundary(face):
    return frozenset(edge(a, b) for a, b in combinations(face, 2))


def xor_all(chains):
    result = frozenset()
    for chain in chains:
        result ^= chain
    return result


def boundary_witnesses(faces):
    # Return EVERY possible boundary and a literal set of triangles making it.
    return {xor_all(boundary(f) for f in selected): selected
            for selected in subsets(faces)}


def cycles(vertices, edges):
    return frozenset(chain for chain in subsets(edges)
                     if all(sum(v in e for e in chain) % 2 == 0 for v in vertices))


def canonical(chain, boundaries):
    return min(tuple(sorted(chain ^ b)) for b in boundaries)


def components(vertices, edges):
    remaining = set(vertices)
    count = 0
    while remaining:
        seen = {remaining.pop()}
        todo = list(seen)
        while todo:
            v = todo.pop()
            for e in edges:
                if v in e:
                    for w in e:
                        if w not in seen:
                            seen.add(w)
                            todo.append(w)
        remaining -= seen
        count += 1
    return count


def state(vertices, edges, faces):
    edges, faces = frozenset(edges), frozenset(faces)
    assert all(boundary(f) <= edges for f in faces), (edges, faces)
    z = cycles(vertices, edges)
    b = boundary_witnesses(faces)
    assert set(b) <= z
    classes = {canonical(c, b) for c in z}
    dimension = int(log2(len(classes)))
    assert 2 ** dimension == len(classes)
    # Independently calculated chain quotient agrees with planar region formula.
    assert dimension == len(edges) - len(vertices) + components(vertices, edges) - len(faces)
    return {'edges': edges, 'faces': faces, 'cycles': z, 'boundaries': b,
            'dimension': dimension}


def filtration(vertices, edge_times, face_times, stages):
    # Faces and edges at a tied time form ONE completed subcomplex.
    assert all(edge_times[e] <= t for f, t in face_times.items() for e in boundary(f))
    return [state(vertices, [e for e, t in edge_times.items() if t <= s],
                  [f for f, t in face_times.items() if t <= s]) for s in stages]


def image_rank(earlier, later):
    assert earlier['edges'] <= later['edges']
    assert earlier['faces'] <= later['faces']
    # Actual inclusion, not matching the counts or choosing a visual child hole.
    images = {canonical(c, later['boundaries']) for c in earlier['cycles']}
    r = int(log2(len(images)))
    assert 2 ** r == len(images)
    return r


def verify_intervals(states, stages, intervals):
    # Every interval claim is checked against every inclusion map rank.
    for i, first in enumerate(states):
        for j in range(i, len(states)):
            expected = sum(b <= stages[i] and stages[j] < d for b, d in intervals)
            assert image_rank(first, states[j]) == expected, (stages[i], stages[j], intervals)


def death(saved, states, stages, born):
    for s, current in zip(stages, states):
        if s >= born:
            assert saved in current['cycles']
            if saved in current['boundaries']:
                return s
    return None


def witnesses(saved, states, stages, born):
    return {str(s): (sorted(current['boundaries'][saved])
                    if saved in current['boundaries'] else None)
            for s, current in zip(stages, states) if s >= born}


# The cancellation demonstration is a non-loop chain, explicitly introduced as
# two tokens, not falsely named a loop. Pairs XY and YZ cancel, leaving XZ.
assert frozenset({'XY', 'YZ'}) ^ boundary('XYZ') == frozenset({'XZ'})

V = 'ABCD'
E = frozenset({'AB', 'BC', 'CD', 'AD', 'AC'})
F = frozenset({'ABC', 'ACD'})
P, Q = boundary('ABC'), boundary('ACD')
O = frozenset({'AB', 'BC', 'CD', 'AD'})
assert P ^ Q == O
assert cycles(V, E) == frozenset({frozenset(), P, Q, O})

# Problem 1: exhaustive nonzero even edge chains on the square are its two
# triangles and its outer rim. All three are actual nonrepeating-edge loops.
one_fill_vanishes = [sorted(c) for c in cycles(V, E) if c and any(
    c in boundary_witnesses({f}) for f in F)]
survives_either = [sorted(c) for c in cycles(V, E) if c and all(
    c not in boundary_witnesses({f}) for f in F)]
assert {tuple(c) for c in one_fill_vanishes} == {tuple(sorted(P)), tuple(sorted(Q))}
assert survives_either == [sorted(O)]
assert (O ^ P) == Q and (O ^ Q) == P

stages = [0, 2, 4, 5, 8]
p2 = []
for first_edge, other_edge in permutations(('AD', 'AC')):
    for first_face, other_face in permutations(('ABC', 'ACD')):
        et = {'AB': 0, 'BC': 0, 'CD': 0, first_edge: 2, other_edge: 4}
        ft = {first_face: 5, other_face: 8}
        states = filtration(V, et, ft, stages)
        assert [s['dimension'] for s in states] == [0, 1, 2, 1, 0]
        first_cycles = states[1]['cycles'] - {frozenset()}
        assert len(first_cycles) == 1
        saved = next(iter(first_cycles))
        expected_death = 5 if first_edge == 'AC' and first_face == 'ABC' else 8
        assert death(saved, states, stages, 2) == expected_death
        intervals = [(2, expected_death), (4, 8 if expected_death == 5 else 5)]
        verify_intervals(states, stages, intervals)
        p2.append({'stage2': first_edge, 'stage4': other_edge, 'stage5': first_face,
                   'stage8': other_face, 'saved': sorted(saved), 'death': expected_death,
                   'boundary_witnesses_by_stage': witnesses(saved, states, stages, 2),
                   'intervals': intervals})
assert sum(r['death'] == 8 for r in p2) == 3
# Specifically, original rim O remains nonzero after either single face fills,
# and is equal there to the other triangle boundary under inclusion.
assert canonical(O, boundary_witnesses({'ABC'})) == canonical(Q, boundary_witnesses({'ABC'}))
assert canonical(O, boundary_witnesses({'ACD'})) == canonical(P, boundary_witnesses({'ACD'}))
assert canonical(O, boundary_witnesses({'ABC'})) != ()
assert canonical(O, boundary_witnesses({'ACD'})) != ()

# Problem 3: triangles share only C and no edges. The initial four edges form a
# tree; either added edge uniquely closes the first loop.
JV = 'ABCDE'
JE = frozenset({'AC', 'BC', 'CD', 'CE', 'AB', 'DE'})
JF = frozenset({'ABC', 'CDE'})
p3 = []
for first_edge, other_edge in permutations(('AB', 'DE')):
    for first_face, other_face in permutations(('ABC', 'CDE')):
        et = {'AC': 0, 'BC': 0, 'CD': 0, 'CE': 0, first_edge: 2, other_edge: 4}
        states = filtration(JV, et, {first_face: 5, other_face: 8}, stages)
        assert [s['dimension'] for s in states] == [0, 1, 2, 1, 0]
        saved = boundary('ABC' if first_edge == 'AB' else 'CDE')
        assert states[1]['cycles'] == frozenset({frozenset(), saved})
        expected_death = 5 if saved == boundary(first_face) else 8
        assert death(saved, states, stages, 2) == expected_death
        intervals = [(2, expected_death), (4, 8 if expected_death == 5 else 5)]
        verify_intervals(states, stages, intervals)
        p3.append({'stage2': first_edge, 'stage4': other_edge, 'stage5': first_face,
                   'stage8': other_face, 'saved': sorted(saved), 'death': expected_death,
                   'boundary_witnesses_by_stage': witnesses(saved, states, stages, 2),
                   'intervals': intervals})
assert sum(r['death'] == 5 for r in p3) == 2
assert sum(r['death'] == 8 for r in p3) == 2

# Problem 4: ties are not internally counted. Exactly one of the two events can
# move, to exactly one of the two target times; examine all four candidates.
tied_stages = [0, 2, 3, 4, 5, 8]
base_edges = {'AB': 0, 'BC': 0, 'CD': 0, 'AD': 2, 'AC': 4}
base_faces = {'ABC': 4, 'ACD': 8}
base_states = filtration(V, base_edges, base_faces, tied_stages)
assert [s['dimension'] for s in base_states] == [0, 1, 1, 1, 1, 0]
assert death(O, base_states, tied_stages, 2) == 8
verify_intervals(base_states, tied_stages, [(2, 8)])
p4 = []
for moved in ('AC', 'ABC'):
    for target in (3, 5):
        et, ft = dict(base_edges), dict(base_faces)
        (et if moved == 'AC' else ft)[moved] = target
        legal = all(et[e] <= t for f, t in ft.items() for e in boundary(f))
        row = {'move': moved, 'to': target, 'legal': legal}
        if legal:
            ss = filtration(V, et, ft, tied_stages)
            dims = [s['dimension'] for s in ss]
            assert 2 in dims
            short_interval = (3, 4) if moved == 'AC' else (4, 5)
            verify_intervals(ss, tied_stages, [(2, 8), short_interval])
            assert death(O, ss, tied_stages, 2) == 8
            row.update(dimensions=dims, intervals=[(2, 8), short_interval])
        p4.append(row)
assert {(r['move'], r['to']) for r in p4 if r['legal']} == {('AC', 3), ('ABC', 5)}

# Exhaust every legal subcomplex of each printed board. For each inclusion and
# each earlier cycle, a boundary witness remains usable (finite support for P5).
state_checks = []
for vertices, edges, faces in ((V, E, F), (JV, JE, JF)):
    all_states = [state(vertices, es, fs) for es in subsets(edges)
                  for fs in subsets(faces) if all(boundary(f) <= es for f in fs)]
    pairs = checked_cycles = 0
    for early in all_states:
        for late in all_states:
            if early['edges'] <= late['edges'] and early['faces'] <= late['faces']:
                pairs += 1
                for saved in early['cycles']:
                    checked_cycles += 1
                    if saved in early['boundaries']:
                        witness = early['boundaries'][saved]
                        assert witness <= late['faces']
                        assert xor_all(boundary(f) for f in witness) == saved
                        assert saved in late['boundaries']
    state_checks.append({'vertices': vertices, 'legal_states': len(all_states),
                         'inclusion_pairs': pairs, 'saved_cycle_tests': checked_cycles})

# Diagram-coordinate checks: integer tenths of centimetres from the source.
# Every pair of nonincident edges must be disjoint, including collinear contact.
def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def on_segment(a, b, c):
    return orient(a, b, c) == 0 and all(min(a[i], b[i]) <= c[i] <= max(a[i], b[i]) for i in (0, 1))


def intersects(a, b, c, d):
    o = [orient(a,b,c), orient(a,b,d), orient(c,d,a), orient(c,d,b)]
    return (o[0]*o[1] < 0 and o[2]*o[3] < 0) or any((
        o[0] == 0 and on_segment(a,b,c), o[1] == 0 and on_segment(a,b,d),
        o[2] == 0 and on_segment(c,d,a), o[3] == 0 and on_segment(c,d,b)))


square = {'A': (0,0), 'B': (62,0), 'C': (62,62), 'D': (0,62)}
joined = {'A': (0,0), 'B': (0,58), 'C': (58,29), 'D': (116,0), 'E': (116,58)}
for coords, edges, faces in ((square, E, F), (joined, JE, JF)):
    for e, f in combinations(edges, 2):
        if not set(e) & set(f):
            assert not intersects(coords[e[0]], coords[e[1]], coords[f[0]], coords[f[1]])
    for face in faces:
        assert orient(*(coords[v] for v in face)) != 0
# Distinct face interiors are disjoint: square vertices B and D lie on opposite
# sides of AC; joined faces occupy opposite closed halfplanes through C.
assert orient(square['A'], square['C'], square['B']) * orient(square['A'], square['C'], square['D']) < 0
assert max(joined[v][0] for v in 'ABC') == min(joined[v][0] for v in 'CDE') == joined['C'][0]
assert set('ABC') & set('CDE') == {'C'}
assert boundary('ABC').isdisjoint(boundary('CDE'))
assert abs(orient(*(square[v] for v in 'ABC'))) == 62*62
assert abs(orient(*(square[v] for v in 'ACD'))) == 62*62
assert max(x for x,y in joined.values()) - min(x for x,y in joined.values()) == 116
assert max(y for x,y in joined.values()) - min(y for x,y in joined.values()) == 58

# The prepared token set covers both boards; at most three copies of any edge
# occur in one test (one saved-loop copy and up to two adjacent filled faces).
prepared = {'AB', 'BC', 'CD', 'AD', 'AC', 'CE', 'DE'}
assert E | JE <= prepared
for edges, faces in ((E, F), (JE, JF)):
    assert max(1 + sum(e in boundary(f) for f in faces) for e in edges) <= 3

print(json.dumps({'result': 'PASS',
                  'problem1_one_fill_loops': sorted(one_fill_vanishes),
                  'problem1_survives_either': survives_either,
                  'problem2_all_schedules': p2, 'problem3_all_schedules': p3,
                  'problem4_all_changes': p4, 'problem5_exhaustive_checks': state_checks,
                  'general_no_resurrection_proof': 'Same finite boundary witness remains available.'}, indent=2))
