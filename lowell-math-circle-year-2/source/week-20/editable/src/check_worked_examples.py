"""Independent arithmetic and non-task-instance checks for K-1 examples."""
from fractions import Fraction
from types import MappingProxyType


def check_board(values, edges, circles):
    frozen = MappingProxyType(dict(values))
    before = dict(frozen)
    results = {}
    for circle in circles:
        neighbors = [b if a == circle else a for a, b in edges if circle in (a, b)]
        copied = [frozen[n] for n in neighbors]
        share = Fraction(sum(copied), len(neighbors))
        assert share == frozen[circle]
        results[circle] = {'neighbor_values': copied, 'mats': len(neighbors),
                           'spare_cubes': sum(copied), 'each_pile': int(share)}
    assert dict(frozen) == before, 'Checking must never update the board.'
    return results


single = check_board({'left': 0, 'circle': 3, 'right': 6},
                     [('left', 'circle'), ('circle', 'right')], ['circle'])
assert single['circle'] == {'neighbor_values': [0, 6], 'mats': 2,
                            'spare_cubes': 6, 'each_pile': 3}
assert (0, 6) not in [(0, 2), (2, 4), (0, 4), (2, 6)]

chain = check_board({'left': 2, 'first': 3, 'second': 4, 'right': 5},
                    [('left', 'first'), ('first', 'second'), ('second', 'right')],
                   ['first', 'second'])
assert chain['first'] == {'neighbor_values': [2, 4], 'mats': 2,
                         'spare_cubes': 6, 'each_pile': 3}
assert chain['second'] == {'neighbor_values': [3, 5], 'mats': 2,
                          'spare_cubes': 8, 'each_pile': 4}
assert (2, 5) not in [(0, 3), (3, 0), (0, 6), (6, 0), (1, 4)]
assert 5 not in range(5), 'The later five-card task only supplies 0 through 4.'

print('PASS: 0 and 6 share into two 3-cube piles, counting the zero neighbor.')
print('PASS: fixed 2--3--4--5 board checks as (2+4)/2=3 and (3+5)/2=4.')
print('PASS: all checks use the same unchanged board; neither example is an existing task instance.')
