#!/usr/bin/env python3
"""Independent finite checks for the actual Week 5 writer-stage cities.

Uses only the Python 3 standard library. The canonical input is city-data.tex,
the exact data file read by return-visit.tex. Row and column indices in the
report are one-based. Does not claim physical fit or classroom piloting.
"""
import itertools
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def rows(flat):
    n = int(len(flat) ** .5)
    assert n*n == len(flat)
    return tuple(tuple(flat[n*r:n*(r+1)]) for r in range(n))


def is_city(city):
    n = len(city)
    want = set(range(1, n+1))
    return (all(set(r) == want for r in city)
            and all({city[r][c] for r in range(n)} == want for c in range(n)))


def all_cities(n):
    possibilities = tuple(itertools.permutations(range(1, n+1)))
    out = []
    def extend(prefix):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for candidate in possibilities:
            if all(candidate[c] not in {r[c] for r in prefix} for c in range(n)):
                extend(prefix + [candidate])
    extend([])
    return tuple(out)


def difference(a, b):
    return tuple((r+1, c+1) for r in range(len(a)) for c in range(len(a))
                 if a[r][c] != b[r][c])


def four_square_trades(city):
    n = len(city)
    out = []
    for r, s in itertools.combinations(range(n), 2):
        for c, d in itertools.combinations(range(n), 2):
            a, b = city[r][c], city[r][d]
            if city[s][c] == b and city[s][d] == a:
                changed = [list(row) for row in city]
                changed[r][c], changed[r][d] = b, a
                changed[s][c], changed[s][d] = a, b
                changed = tuple(tuple(row) for row in changed)
                assert is_city(changed)
                assert len(difference(city, changed)) == 4
                out.append(changed)
    return tuple(out)


def diagonal_condition(city):
    n = len(city)
    want = set(range(1, n+1))
    return (set(city[i][i] for i in range(n)) == want,
            set(city[i][n-1-i] for i in range(n)) == want)


def higher_neighbors(city, r, c):
    n = len(city)
    return tuple((a, b) for a, b in ((r-1,c),(r+1,c),(r,c-1),(r,c+1))
                 if 0 <= a < n and 0 <= b < n and city[a][b] > city[r][c])


def stopping_squares(city):
    n = len(city)
    return tuple((r+1,c+1) for r in range(n) for c in range(n)
                 if not higher_neighbors(city, r, c))


def route_checks(city):
    n = len(city)
    all_peaks = set(stopping_squares(city))
    max_length = 0
    ends = set()
    def walk(r, c, path):
        nonlocal max_length
        steps = higher_neighbors(city, r, c)
        if not steps:
            ends.add((r+1,c+1))
            max_length = max(max_length, len(path)-1)
            assert len(path)-1 <= n-1
        else:
            for a, b in steps:
                assert (a,b) not in path
                walk(a, b, path + ((a,b),))
    for r in range(n):
        for c in range(n):
            walk(r, c, ((r,c),))
    assert ends == all_peaks
    assert all((r+1,c+1) in all_peaks for r in range(n) for c in range(n)
               if city[r][c] == n)
    return {"stopping_squares": sorted(ends), "maximum_route_moves": max_length}


def main():
    text = (HERE/'city-data.tex').read_text()
    data = {name: rows(tuple(map(int, values.split(','))))
            for name, values in re.findall(r'\\def\\(\w+)\{([\d,]+)\}', text)}
    assert set(data) == {'CityA','CityB','CityC','DiagonalDemo','CityD','CityE'}
    assert all(is_city(city) for city in data.values())
    catalogs = {n: all_cities(n) for n in (3,4)}
    assert len(catalogs[3]) == 12 and len(catalogs[4]) == 576
    report = {"city_catalog_counts": {n: len(cities) for n,cities in catalogs.items()},
              "printed_cities": {}, "diagonal_cities": {}, "all_city_peak_histograms": {}}
    for name in ('CityA','CityB','CityC'):
        city = data[name]
        four = four_square_trades(city)
        found = tuple(other for other in catalogs[len(city)]
                      if len(difference(city, other)) == 4)
        assert set(four) == set(found), 'Every four-change city must be a rectangle trade.'
        minimum = min(len(difference(city, other)) for other in catalogs[len(city)] if other != city)
        report['printed_cities'][name] = {
            'rows': city, 'cube_total': sum(map(sum,city)),
            'four_square_changes': len(four), 'fewest_changed_squares': minimum,
            'four_change_examples': [{'rows':other,'changed_squares':difference(city,other)}
                                     for other in four]}
    assert report['printed_cities']['CityA']['four_square_changes'] == 4
    assert report['printed_cities']['CityB']['four_square_changes'] == 12
    assert report['printed_cities']['CityC']['four_square_changes'] == 0
    assert [report['printed_cities'][name]['fewest_changed_squares'] for name in ('CityA','CityB','CityC')] == [4,4,6]
    assert [report['printed_cities'][name]['cube_total'] for name in ('CityA','CityB','CityC')] == [40,40,18]
    for n, cities in catalogs.items():
        diagonals = tuple(city for city in cities if all(diagonal_condition(city)))
        report['diagonal_cities'][n] = {'count':len(diagonals),'one_example':diagonals[:1]}
        histogram = Counter(len(stopping_squares(city)) for city in cities)
        report['all_city_peak_histograms'][n] = dict(sorted(histogram.items()))
        for city in cities:
            route_checks(city)
    assert report['diagonal_cities'][3]['count'] == 0
    assert report['diagonal_cities'][4]['count'] == 48
    assert diagonal_condition(data['DiagonalDemo']) == (False,False)
    assert (tuple(data['DiagonalDemo'][i][i] for i in range(2)),
            tuple(data['DiagonalDemo'][i][1-i] for i in range(2))) == ((2,2),(1,1))
    assert report['all_city_peak_histograms'][3] == {3:8,4:4}
    assert report['all_city_peak_histograms'][4] == {4:226,5:136,6:172,7:8,8:34}
    for name in ('CityD','CityE'):
        report['printed_cities'][name] = {'rows':data[name], **route_checks(data[name])}
    assert report['printed_cities']['CityD']['stopping_squares'] == [(1,3),(2,1),(3,2)]
    assert report['printed_cities']['CityE']['stopping_squares'] == [(1,3),(2,2),(3,1),(3,3)]
    # Worked roof move: same three side-neighbor cells throughout; marker
    # changes from index 0 to index 1, where the height increases from 1 to 3.
    demo = (1,3,2)
    assert demo[1] > demo[0] and abs(1-0) == 1
    report['worked_visuals'] = {
        'height_conversion': {'cube_labels':[1,2,3], 'output_height':3},
        'diagonal_reading': {'rows':data['DiagonalDemo'], 'dashed':[2,2], 'dotted':[1,1]},
        'roof_move': {'row':demo,'before_index':0,'after_index':1,'heights':[1,3]}}
    out = HERE.parent/'math-checks.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f'PASS: actual inputs, four-square changes, both diagonals, all roof routes; {out}')


if __name__ == '__main__':
    main()
