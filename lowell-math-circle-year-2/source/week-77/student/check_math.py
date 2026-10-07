#!/usr/bin/env python3
"""Independent finite checks for every explicit Week 77 example (stdlib only)."""
from itertools import combinations, permutations
from functools import reduce
from operator import xor


def edge(a, b):
    return ''.join(sorted((a, b)))


def boundary(triangle):
    return frozenset(edge(a, b) for a, b in combinations(triangle, 2))


def parity_sum(chains):
    return reduce(xor, map(frozenset, chains), frozenset())


def subsets(items):
    items = tuple(items)
    for bits in range(1 << len(items)):
        yield tuple(item for i, item in enumerate(items) if bits >> i & 1)


def span(chains):
    return {parity_sum(choice) for choice in subsets(chains)}


def cycles(edges):
    result = set()
    for subset in subsets(edges):
        degrees = {}
        for a, b in subset:
            degrees[a] = degrees.get(a, 0) ^ 1
            degrees[b] = degrees.get(b, 0) ^ 1
        if not any(degrees.values()):
            result.add(frozenset(subset))
    return result


def components(vertices, edges):
    remaining = set(vertices)
    count = 0
    while remaining:
        count += 1
        active = {remaining.pop()}
        while active:
            a = active.pop()
            neighbors = {b if x == a else x for x, b in edges if x == a or b == a}
            new = neighbors & remaining
            remaining -= new
            active |= new
    return count


def audit_state(vertices, edges, faces):
    edges = frozenset(edges)
    assert all(set(e) <= set(vertices) for e in edges)
    assert all(boundary(f) <= edges for f in faces), 'Face arrives without its boundary'
    boundaries = span(boundary(f) for f in faces)
    all_cycles = cycles(edges)
    assert boundaries <= all_cycles
    # Independently enumerate the quotient by comparing boundary-cancelled cycles.
    classes = {frozenset(c ^ b for b in boundaries) for c in all_cycles}
    assert len(classes) & (len(classes) - 1) == 0
    holes = len(classes).bit_length() - 1
    # All boards below are planar; independently check the planar Euler count.
    assert holes == len(edges) - len(vertices) + components(vertices, edges) - len(faces)
    return holes, boundaries, all_cycles


def state_at(vertices, edge_times, face_times, time):
    edges = {e for e, t in edge_times.items() if t <= time}
    faces = {f for f, t in face_times.items() if t <= time}
    return audit_state(vertices, edges, faces)


def first_loop(vertices, edge_times, face_times):
    _, boundaries, all_cycles = state_at(vertices, edge_times, face_times, 2)
    candidates = all_cycles - boundaries
    assert len(candidates) == 1
    return candidates.pop()


def death(loop, vertices, edge_times, face_times):
    for t in sorted(set(edge_times.values()) | set(face_times.values())):
        if loop in state_at(vertices, edge_times, face_times, t)[1]:
            return t
    return None


def persistence_rank(vertices, edge_times, face_times, s, t):
    source = state_at(vertices, edge_times, face_times, s)[2]
    target_boundaries = state_at(vertices, edge_times, face_times, t)[1]
    image_cosets = {frozenset(z ^ b for b in target_boundaries) for z in source}
    return len(image_cosets).bit_length() - 1


def verify_intervals(vertices, edge_times, face_times, intervals):
    times = sorted(set(edge_times.values()) | set(face_times.values()))
    for s in times:
        for t in times:
            if s <= t:
                actual = persistence_rank(vertices, edge_times, face_times, s, t)
                expected = sum(b <= s and t < d for b, d in intervals)
                assert actual == expected, (s, t, actual, expected, intervals)



def verify_four_triangle_construction():
    """Check Problem 6 by edge-set cancellation and a separate bitmask model."""
    faces = ('ABO', 'BCO', 'CDO', 'ADO')
    edges = frozenset(('AB', 'BC', 'CD', 'AD', 'AO', 'BO', 'CO', 'DO'))
    initial = faces[:2]
    remaining = faces[2:]
    holes, filled_boundaries, graph_cycles = audit_state('ABCDO', edges, initial)
    assert holes == 2
    assert len(graph_cycles) == 16
    survivors = graph_cycles - filled_boundaries
    assert len(survivors) == 12
    lasting = {
        loop for loop in survivors
        if all(loop not in span(boundary(f) for f in initial + (first,))
               for first in remaining)
    }
    assert len(lasting) == 4
    assert all(loop in span(boundary(f) for f in faces) for loop in lasting)

    # There is exactly one unordered pair that works for both parts.
    witnesses = {}
    for pair in combinations(sorted(lasting, key=lambda z: sorted(z)), 2):
        outcomes = {}
        for order in permutations(faces):
            ft = {face: i + 1 for i, face in enumerate(order)}
            deaths = tuple(death(loop, 'ABCDO', dict.fromkeys(edges, 0), ft)
                           for loop in pair)
            comparison = (deaths[0] > deaths[1]) - (deaths[0] < deaths[1])
            outcomes.setdefault(comparison, order)
        if -1 in outcomes and 1 in outcomes:
            witnesses[pair] = outcomes
    assert len(witnesses) == 1
    pair, outcomes = next(iter(witnesses.items()))
    expected = {parity_sum(boundary(f) for f in ('ABO', 'CDO', 'ADO')),
                parity_sum(boundary(f) for f in ('BCO', 'CDO', 'ADO'))}
    assert set(pair) == expected
    assert all(all(sum(v in e for e in loop) == 2 for v in 'ABCDO') for loop in pair)
    assert pair[0] ^ pair[1] == boundary('ABO') ^ boundary('BCO')

    # Independent exhaustive model. Do not call the set-chain routines here.
    # Bits 0..7 represent AB, BC, CD, AD, AO, BO, CO, DO respectively.
    edge_order = ('AB', 'BC', 'CD', 'AD', 'AO', 'BO', 'CO', 'DO')
    triangle_masks = (0b00110001, 0b01100010, 0b11000100, 0b10011000)
    cancellation = {}
    for face_mask in range(16):
        token_mask = 0
        for i in range(4):
            if face_mask & (1 << i):
                token_mask ^= triangle_masks[i]
        cancellation[face_mask] = token_mask
    assert len(set(cancellation.values())) == 16
    bit_cycles = {
        m for m in range(256)
        if all(sum(bool(m & (1 << i)) for i, e in enumerate(edge_order) if v in e) % 2 == 0
               for v in 'ABCDO')
    }
    assert bit_cycles == set(cancellation.values())
    def can_cancel(loop_mask, available_faces):
        return any(cancellation[s] == loop_mask for s in range(16)
                   if s & available_faces == s)
    bit_lasting = {
        m for m in bit_cycles
        if not can_cancel(m, 0b0011)
        and not can_cancel(m, 0b0111)
        and not can_cancel(m, 0b1011)
        and can_cancel(m, 0b1111)
    }
    assert bit_lasting == {15, 62, 92, 109}
    bit_pairs = {}
    for a, b in combinations(sorted(bit_lasting), 2):
        signs = []
        for order in permutations(range(4)):
            available = 0
            found = {}
            for t, face in enumerate(order, 1):
                available |= 1 << face
                for loop in (a, b):
                    if loop not in found and can_cancel(loop, available):
                        found[loop] = t
            signs.append((found[a] > found[b]) - (found[a] < found[b]))
        if -1 in signs and 1 in signs:
            bit_pairs[(a, b)] = tuple(signs.count(k) for k in (-1, 0, 1))
    assert bit_pairs == {(62, 109): (6, 12, 6)}
    assert {frozenset(edge_order[i] for i in range(8) if m & (1 << i))
            for m in bit_lasting} == lasting
    assert {frozenset(edge_order[i] for i in range(8) if m & (1 << i))
            for m in (62, 109)} == set(pair)

    # Concrete replayable orders for the two printed answer spaces.
    first = frozenset(('AB', 'BO', 'CO', 'CD', 'AD'))
    second = frozenset(('AO', 'BO', 'BC', 'CD', 'AD'))
    for order, expected_deaths in (
            (('CDO', 'ADO', 'ABO', 'BCO'), (3, 4)),
            (('CDO', 'ADO', 'BCO', 'ABO'), (4, 3))):
        ft = {face: i + 1 for i, face in enumerate(order)}
        assert tuple(death(loop, 'ABCDO', dict.fromkeys(edges, 0), ft)
                     for loop in (first, second)) == expected_deaths
    print('Problem 6: 4 loops last through either first filling; exactly 1 of their 6 pairs')
    print('  permits either strict death order from no fillings. Independent enumeration:')
    print('  24 fill orders give 6 first-before-second, 12 ties, 6 second-before-first.')
    print('  Saved loops: AB BO CO CD AD; AO BO BC CD AD.')
    print('  Fill orders: CDO ADO ABO BCO; CDO ADO BCO ABO.')


def main():
    P, Q = boundary('ABC'), boundary('ACD')
    O = frozenset(('AB', 'BC', 'CD', 'AD'))
    assert parity_sum([{'XY', 'YZ'}, boundary('XYZ')]) == {'XZ'}
    assert P ^ Q == O
    # Problem 1: these are the only nonempty cycles on the complete square graph.
    _, _, all_cycles = audit_state('ABCD', P | Q, set())
    assert all_cycles - {frozenset()} == {P, Q, O}
    assert P in span([P]) and Q in span([Q])
    assert O not in span([P]) and O not in span([Q])
    assert O in span([P, Q])
    print('Problem 1: each triangle loop can die with one filling; only the outside loop survives either single filling.')

    # Problem 2: four legal choices; direct chain membership determines old-loop death.
    survivors = []
    for e2, e4 in permutations(('AD', 'AC')):
        for f5, f8 in permutations(('ABC', 'ACD')):
            et = {'AB': 0, 'BC': 0, 'CD': 0, e2: 2, e4: 4}
            ft = {f5: 5, f8: 8}
            counts = [state_at('ABCD', et, ft, t)[0] for t in (0, 2, 4, 5, 8)]
            assert counts == [0, 1, 2, 1, 0]
            old = first_loop('ABCD', et, ft)
            d = death(old, 'ABCD', et, ft)
            expected = 5 if e2 == 'AC' and f5 == 'ABC' else 8
            assert d == expected
            intervals = [(2, 8), (4, 5)] if d == 8 else [(2, 5), (4, 8)]
            verify_intervals('ABCD', et, ft, intervals)
            if d == 8:
                survivors.append((e2, e4, f5, f8))
    assert len(survivors) == 3
    print('Problem 2: 3 surviving schedules (stage 2 edge, stage 4 edge, stage 5 face, stage 8 face):', survivors)

    # Problem 3: triangles touch only at C; 4 independent edge/fill schedules.
    deaths = []
    for e2, e4 in permutations(('AB', 'DE')):
        for f5, f8 in permutations(('ABC', 'CDE')):
            et = {'AC': 0, 'BC': 0, 'CD': 0, 'CE': 0, e2: 2, e4: 4}
            ft = {f5: 5, f8: 8}
            assert [state_at('ABCDE', et, ft, t)[0] for t in (0, 2, 4, 5, 8)] == [0, 1, 2, 1, 0]
            old = first_loop('ABCDE', et, ft)
            d = death(old, 'ABCDE', et, ft)
            assert d == (5 if e2 in boundary(f5) else 8)
            deaths.append(d)
            verify_intervals('ABCDE', et, ft, [(2, d), (4, 13-d)])
    assert sorted(deaths) == [5, 5, 8, 8]
    print('Problem 3: 2 schedules kill the first loop at 5; 2 keep it until 8, with identical counts.')

    # Problem 4: simultaneous additions evaluated only at their common stage.
    et = {'AB': 0, 'BC': 0, 'CD': 0, 'AD': 2, 'AC': 4}
    ft = {'ABC': 4, 'ACD': 8}
    assert [state_at('ABCD', et, ft, t)[0] for t in (0, 2, 3, 4, 5, 8)] == [0, 1, 1, 1, 1, 0]
    verify_intervals('ABCD', et, ft, [(2, 8)])
    repairs = []
    illegal = []
    for piece in ('AC', 'ABC'):
        for moved_to in (3, 5):
            ne, nf = et.copy(), ft.copy()
            (ne if piece == 'AC' else nf)[piece] = moved_to
            try:
                counts = [state_at('ABCD', ne, nf, t)[0] for t in (0, 2, 3, 4, 5, 8)]
            except AssertionError:
                illegal.append((piece, moved_to))
                continue
            if 2 in counts:
                repairs.append((piece, moved_to))
    assert repairs == [('AC', 3), ('ABC', 5)]
    assert illegal == [('AC', 5), ('ABC', 3)]
    print('Problem 4: exactly two repairs:', repairs, '; remaining choices violate face-boundary order.')

    # Problem 5: exhaustive boundary-space inclusion for every nested face pair on all three boards.
    for faces in (('ABC', 'ACD'), ('ABC', 'CDE'), ('ABO', 'BCO', 'CDO', 'ADO')):
        for earlier in subsets(faces):
            for later in subsets(faces):
                if set(earlier) <= set(later):
                    assert span(boundary(f) for f in earlier) <= span(boundary(f) for f in later)
    print('Problem 5: a cancelling set of filled triangles remains available forever; a gone loop cannot return.')
    verify_four_triangle_construction()
    print('All finite checks passed, including inclusion-map ranks and simultaneous-stage behavior.')


if __name__ == '__main__':
    main()
