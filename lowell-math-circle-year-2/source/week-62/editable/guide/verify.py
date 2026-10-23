#!/usr/bin/env python3
"""Independent Week 62 guide checks, reconstructed from the inspected final PDF.

No student/research answer data or builder modules are read. Standard library only.
"""
import argparse
from collections import Counter, deque
from itertools import combinations, permutations, product
import json
from pathlib import Path


def graph(vertices, pairs):
    return tuple(vertices), tuple(tuple(p) for p in pairs.split())


# Endpoint pairs transcribed independently while looking at all nine final pages.
GRAPHS = {
    'p1-path': graph('ABCD', 'AB BC CD'),
    'p1-star': graph('ABCDEF', 'AB AC AD AE AF'),
    'p2-diamond': graph('ABCD', 'AB AC BC AD BD'),
    'p2-complete': graph('ABCD', 'AB AC AD BC BD CD'),
    'p2-many-lines': graph('ABCDE', 'AC AD AE BC BD BE'),
    'p3-five-branch': graph('ABCDEF', 'AB BC CD DE EA AF'),
    'p3-six-branches': graph('ABCDEFGH', 'AB BC CD DE EF FA AG DH'),
    'p4-six-chord': graph('ABCDEFGH', 'AB BC CD DE EF FA AD BG'),
    'p4-seven-chord': graph('ABCDEFGH', 'AB BC CD DE EF FG GA AD GH'),
    'p5-disconnected': graph('ABCDEFG', 'AB BC CD DA EF'),
    'p5-odd-disconnected': graph('ABCDEFGH', 'AB BC CD DE EA CF FG'),
    'p6-tree': graph('ABCDEF', 'AB BC AD BE CF'),
    'p6-empty': graph('ABCDEF', ''),
    'p7-path': graph('ABCD', 'AB BC CD'),
    'p7-path-extra': graph('ABCD', 'AB BC CD'),
    'p8-tree': graph('ABCDEFGH', 'HA HB BC HD DE DF FG'),
    'p9-path': graph('ABCD', 'AB BC CD'),
    'p9-diamond': graph('ABCD', 'AB AC BC AD BD'),
}
SOLUTIONS = {
    'p1-path': ('AC BD', 2, 2), 'p1-star': ('A BCDEF', 2, 2),
    'p2-diamond': ('A B CD', 3, 3), 'p2-complete': ('A B C D', 4, 4),
    'p2-many-lines': ('AB CDE', 2, 2),
    'p3-five-branch': ('AC BDF E', 3, 2),
    'p3-six-branches': ('ACEH BDFG', 2, 2),
    'p4-six-chord': ('ACEGH BDF', 2, 2),
    'p4-seven-chord': ('ACEH BDF G', 3, 2),
    'p5-disconnected': ('ACEG BDF', 2, 2),
    'p5-odd-disconnected': ('ACGH BDF E', 3, 2),
    'p6-tree': ('ACE BDF', 2, 2), 'p6-empty': ('ABCDEF', 1, 1),
    'p7-path': ('AC BD', 2, 2), 'p7-path-extra': ('AC BD', 2, 2),
    'p8-tree': ('HCEF ABDG', 2, 2),
    'p9-path': ('AC BD', 2, 2), 'p9-diamond': ('A B CD', 3, 3),
}


def proper(g, assignment):
    vs, es = g
    return (set(assignment) == set(vs)
            and all(assignment[u] != assignment[v] for u, v in es))


def assignments(g, k):
    vs, es = g
    ix = {v: i for i, v in enumerate(vs)}
    for values in product(range(1, k+1), repeat=len(vs)):
        if all(values[ix[u]] != values[ix[v]] for u, v in es):
            yield dict(zip(vs, values))


def chi(g):
    return next(k for k in range(1, len(g[0])+1)
                if next(assignments(g, k), None) is not None)


def clique(g):
    vs, es = g
    edges = set(map(frozenset, es))
    return max(len(s) for n in range(1, len(vs)+1) for s in combinations(vs, n)
               if all(frozenset(p) in edges for p in combinations(s, 2)))


def slot_groups(text):
    groups = text.split()
    chars = ''.join(groups)
    assert len(chars) == len(set(chars)), 'Duplicated activity in solution'
    return {v: k for k, group_ in enumerate(groups, 1) for v in group_}


def first_fit(g, order):
    vs, es = g
    assert set(order) == set(vs) and len(order) == len(vs)
    result = {}
    for v in order:
        used = {result[u] for e in es if v in e for u in e
                if u != v and u in result}
        result[v] = next(k for k in range(1, len(vs)+1) if k not in used)
    assert proper(g, result)
    return result


def cycle(g, word):
    assert word[0] == word[-1]
    assert len(word)-1 >= 3 and len(set(word[:-1])) == len(word)-1
    edges = set(map(frozenset, g[1]))
    assert all(frozenset(e) in edges for e in zip(word, word[1:]))
    return len(word)-1


def added(g, extras):
    vs, es = g
    existing = set(map(frozenset, es))
    for e in extras:
        assert len(set(e)) == 2 and set(e) <= set(vs)
        assert frozenset(e) not in existing
    return vs, es + tuple(tuple(e) for e in extras)


def minimum_additions(g):
    vs, es = g
    existing = set(map(frozenset, es))
    missing = [e for e in combinations(vs, 2) if frozenset(e) not in existing]
    for n in range(len(missing)+1):
        answers = [s for s in combinations(missing, n)
                   if next(assignments(added(g, s), 2), None) is None]
        if answers:
            return n, answers
    raise AssertionError('No obstruction can be added')


def check_all():
    data = {'method': 'Independent endpoint transcription and exhaustive finite checks',
            'graphs': {}, 'physical_handling_tested': False, 'classroom_piloted': False}
    for name, g in GRAPHS.items():
        groups, minimum, largest = SOLUTIONS[name]
        assert proper(g, slot_groups(groups)), name
        assert chi(g) == minimum, name
        assert clique(g) == largest, name
        data['graphs'][name] = {'vertices': list(g[0]), 'edges': list(g[1]),
                               'minimum': minimum, 'clique': largest,
                               'listed_schedule': slot_groups(groups)}
    # Every explicitly printed odd-cycle certificate.
    for name, word in [('p3-five-branch', 'ABCDEA'),
                       ('p4-seven-chord', 'ADE FGA'.replace(' ', '')),
                       ('p4-seven-chord', 'ABCDEFGA'),
                       ('p5-odd-disconnected', 'ABCDEA')]:
        assert cycle(GRAPHS[name], word) % 2 == 1
    # P6: all minimal answers, not just selected witnesses.
    n, edges = minimum_additions(GRAPHS['p6-tree'])
    all_one = {''.join(e[0]) for e in edges}
    assert n == 1 and all_one == {'AC', 'AE', 'CE', 'BD', 'BF', 'DF'}
    for edge, word in [('AC', 'ABCA'), ('AE', 'ABEA'), ('CE', 'CBEC'),
                       ('BD', 'BADB'), ('BF', 'BCFB'), ('DF', 'DABCFD')]:
        assert cycle(added(GRAPHS['p6-tree'], [edge]), word) % 2 == 1
    for edge in ['AF', 'CD', 'DE', 'EF']:
        assert proper(added(GRAPHS['p6-tree'], [edge]), slot_groups('ACE BDF'))
    n, triangles = minimum_additions(GRAPHS['p6-empty'])
    assert n == 3 and len(triangles) == 20
    expected = {'ABC', 'ABD', 'ABE', 'ABF', 'ACD', 'ACE', 'ACF', 'ADE', 'ADF', 'AEF',
                'BCD', 'BCE', 'BCF', 'BDE', 'BDF', 'BEF', 'CDE', 'CDF', 'CEF', 'DEF'}
    actual = {''.join(sorted(set(v for e in s for v in e))) for s in triangles}
    assert actual == expected
    assert all(len(set(v for e in s for v in e)) == 3 for s in triangles)
    data['minimum_additions'] = {'tree': sorted(all_one), 'empty': sorted(actual)}
    # P7: both first-fit extrema and every legal repair intermediate state.
    path = GRAPHS['p7-path']
    assert first_fit(path, 'ABCD') == dict(A=1, B=2, C=1, D=2)
    repair = first_fit(path, 'ADBC')
    assert repair == dict(A=1, D=1, B=2, C=3)
    repair['D'] = 2
    assert proper(path, repair)
    repair['C'] = 1
    assert proper(path, repair) and max(repair.values()) == 2
    # P8: step table and rooted-order witness.
    tree = GRAPHS['p8-tree']
    four = first_fit(tree, 'ACBHEGFD')
    assert four == dict(A=1, C=1, B=2, H=3, E=1, G=1, F=2, D=4)
    two = first_fit(tree, 'HABDCEFG')
    assert two == dict(H=1, A=2, B=2, D=2, C=1, E=1, F=1, G=2)
    data['first_fit'] = {}
    for name in ['p7-path', 'p8-tree']:
        g = GRAPHS[name]
        degree = max(sum(v in e for e in g[1]) for v in g[0])
        counts = Counter(max(first_fit(g, order).values()) for order in permutations(g[0]))
        assert max(counts) <= degree+1
        assert min(counts) == 2 and max(counts) == (3 if name == 'p7-path' else 4)
        data['first_fit'][name] = {'maximum_degree': degree, 'all_order_counts': dict(counts)}
    assert data['first_fit']['p7-path']['all_order_counts'] == {2: 18, 3: 6}
    assert data['first_fit']['p8-tree']['all_order_counts'] == {2: 12810, 3: 26880, 4: 630}
    # P9: named labels, including choices that leave one or more slots empty.
    data['named_counts'] = {}
    for name, formula in [('p9-path', lambda k: k*(k-1)**3),
                          ('p9-diamond', lambda k: k*(k-1)*(k-2)**2)]:
        counts = {k: sum(1 for _ in assignments(GRAPHS[name], k)) for k in range(1, 5)}
        assert all(counts[k] == formula(k) for k in counts)
        assert [counts[3], counts[4]] == ([24, 108] if name == 'p9-path' else [6, 48])
        data['named_counts'][name] = counts
    assert sum(1 for _ in assignments(GRAPHS['p1-path'], 2)) == 2
    # Author-created launch and student convention states cited in the guide.
    assert proper(graph('ABH', 'AB'), slot_groups('AH B'))
    assert proper(graph('XYW', 'XW YW'), slot_groups('XY W'))
    # Optional extension: disconnected components may choose named colors independently.
    assert sum(1 for _ in assignments(GRAPHS['p5-disconnected'], 2)) == 8
    # Numeric preparation statements.
    assert 6*8+8 == 56 and 6*4+4 == 28 and 6*32+32 == 224
    assert 3*3 + 6 + 2 + 9 == 26 and 3*10 == 30
    data['guide_pages_expected'] = 10
    return data


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--report', type=Path)
    args = p.parse_args()
    result = check_all()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: 18 graphs, every listed schedule/cycle, all minimal additions, '
          '24 path orders, 40,320 tree orders, named counts and launch records.')
