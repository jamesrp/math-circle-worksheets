#!/usr/bin/env python3
"""Independent Week 78 FINAL mathematical review. Python standard library only.

Written independently of the author's checker. This file neither imports nor
executes check_math.py. It compares the plotted data with the reviewed cases,
then solves minimum-tie conditions exactly on parametrized arms. No tolerance,
bounded drawing window, integer-only assumption, or stable intersection is used.

Run from anywhere:
    python3 final-independent-check.py
    python3 final-independent-check.py --source-dir PATH_TO_PORTABLE_SOURCE

The regression is finite. The following original all-real argument supplies
what a finite regression cannot.

ALL-REAL ARGUMENT
Let L(a,b) consist of points where min(x-a,y-b,0) is attained at least twice.
The pairs of minimal terms give exactly y=b,x>=a; x=a,y>=b; and
x-a=y-b<=0. These are the east, north, and southwest rays with junction (a,b).
There are no further points: any repeated minimum contains one of those pairs.
Adding a common constant to the three scores preserves the repeated minima.

Translate the first junction to (0,0), and put the second at (h,k). For
h*k*(h-k) nonzero, the six possible strict orderings of h,k,0 give:
    k<0<h:   (h,0)          h<0<k:   (0,k)
    0<k<h:   (h-k,0)        0<h<k:   (0,k-h)
    k<h<0:   (h,h)          h<k<0:   (k,k)
These are complete singleton intersections. For example, when 0<k<h,
only the first line's east ray can meet the second: its north ray has x=0,
where the second line's southwest ray has y=k-h<0, and its southwest ray
has x=y<=0 whereas the second diagonal has x-y=h-k>0. The east ray meets
that second diagonal at (h-k,0); the second east and north rays cannot
produce another intersection. Swapping x and y, or swapping the two
junctions and translating, gives all the other strict cases. In the two
opposite-sign cases the northeast rectangle corner is the only allowed
ray-pair intersection. Hence every unaligned pair meets once, even if the
intersection lies outside the drawn grid.

On the excluded boundaries: h=0,k!=0 gives the north ray from
(0,max(0,k)); k=0,h!=0 gives the east ray from (max(0,h),0); h=k!=0 gives
the southwest ray from (min(0,h),min(0,h)). Substituting the three ray
conditions excludes extra pieces in each case. h=k=0 gives all three
rays, namely the same entire line. Thus there are no empty intersections,
exactly-two-point intersections, or bounded nontrivial shared segments.
Every shared ray includes its endpoint and every real point on it.

For the inverse problem, P belongs to L(J) exactly when -J belongs to
L(-P), since the displacement -J-(-P) is P-J. Therefore all admissible
junctions for P,Q are -(L(-P) intersection L(-Q)). Distinct unaligned
points have one junction; horizontally aligned points have the west ray
from their leftmost point; vertically aligned points the south ray from
their lowest point; slope-one aligned points the northeast ray from their
northeastern point. If P=Q, which Problem 7 excludes, the junction locus
is the union of west, south and northeast rays from P. Distinct junctions
determine distinct whole lines, since the junction is the unique point
with three local arms. Thus these infinite loci give infinitely many
lines, not multiple representations of one line.

PROBLEM-BY-PROBLEM OUTCOMES (not student hints)
Opening: min(x,y,2) has junction (2,2); (4,2) is on; (4,4) is off.
1: The two top boards have A=(4,4), with B chosen by the child. B may
   yield one point, any of three shared rays, or the identical line if B=A.
   The two bottom fixed boards have A=(2,2), B=(6,5) and A=(2,2), B=(5,6).
   They meet only at (3,2) and (2,3), respectively. All outcomes are checked.
2: Reading order: singleton (6,5); north ray from (3,6); east ray from
   (6,4); southwest ray from (2,2). Counts are 1,infinite,infinite,infinite.
3: Exactly two shared points is impossible for distinct junctions.
4: Unique junctions (2,2) and (5,5), respectively; no second line in either.
5: All junctions: (t,4),t<=2; (3,t),t<=2; (5+t,5+t),t>=0. The endpoints
   count, between-dot junctions count, and each locus continues unbounded.
6: A=(2,7), B=(10,5) meet only at (10,7), beyond the 0-8 grid.
   Lines always meet. More than one point occurs exactly when junctions
   share x, y or x-y; equality gives identical whole lines.
7: For distinct points, one line if none of those alignments holds,
   infinitely many if an alignment holds. The inverse-locus argument above
   proves existence and completeness, including noninteger coordinates.

All fixed diagrams were also visually checked at 110 dpi against their
coordinates during this review. Digital checks do not establish printing,
physical usability, pacing, or classroom readiness.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import argparse
import ast
import re

DIRECTIONS = ((1, 0), (0, 1), (-1, -1))
EXPECTED_DATA = {
    'EXAMPLE_JUNCTION': (2, 2),
    'EXAMPLE_POINTS': ((4, 2), (4, 4)),
    'TRIAL_JUNCTION': (4, 4),
    'TRIAL_FIXED_PAIRS': (((2, 2), (6, 5)), ((2, 2), (5, 6))),
    'CROPPED_PAIR': ((2, 7), (10, 5)),
    'INTERSECTION_PAIRS': (((2, 5), (6, 2)), ((3, 2), (3, 6)),
                           ((2, 4), (6, 4)), ((2, 2), (6, 6))),
    'INVERSE_GENERAL': (((2, 5), (6, 2)), ((2, 2), (6, 5))),
    'INVERSE_ALIGNED': (((2, 4), (6, 4)), ((3, 2), (3, 6)),
                        ((2, 2), (5, 5))),
}


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def neg(p):
    return (-p[0], -p[1])


def at(p, direction, t):
    return add(p, (t * direction[0], t * direction[1]))


def on_line(point, junction):
    values = (point[0] - junction[0], point[1] - junction[1], F(0))
    return values.count(min(values)) >= 2


def tie_intervals(constants, slopes):
    """All t>=0 where min(c_i+m_i*t) is repeated, as closed intervals.

    Each pair either ties at one exact t, ties forever, or never ties.
    In the forever case, intersect the third-term inequality with t>=0.
    None denotes an unbounded upper endpoint.
    """
    intervals = []
    for i, j in combinations(range(3), 2):
        dm = slopes[i] - slopes[j]
        dc = constants[i] - constants[j]
        if dm:
            t = -F(dc, dm)
            if t >= 0:
                scores = [constants[k] + slopes[k] * t for k in range(3)]
                if scores[i] == scores[j] == min(scores):
                    intervals.append((t, t))
        elif dc == 0:
            low, high, valid = F(0), None, True
            for k in range(3):
                # c_i + m_i*t <= c_k + m_k*t.
                coefficient = slopes[i] - slopes[k]
                bound = constants[k] - constants[i]
                if coefficient > 0:
                    endpoint = F(bound, coefficient)
                    high = endpoint if high is None else min(high, endpoint)
                elif coefficient < 0:
                    low = max(low, F(bound, coefficient))
                elif bound < 0:
                    valid = False
            if valid and (high is None or low <= high):
                intervals.append((low, high))
    # Merge overlapping intervals; endpoints remain included.
    intervals.sort(key=lambda pair: pair[0])
    merged = []
    for low, high in intervals:
        if merged and (merged[-1][1] is None or low <= merged[-1][1]):
            a, b = merged[-1]
            merged[-1] = (a, None if b is None or high is None else max(b, high))
        else:
            merged.append((low, high))
    return merged


def point_on_ray(point, start, direction):
    index = next(k for k in (0, 1) if direction[k])
    t = F(point[index] - start[index], direction[index])
    return t >= 0 and at(start, direction, t) == point


def canonical(pieces):
    """Keep full rays, remove singleton duplicates at ray endpoints."""
    unique = set(pieces)
    rays = [p for p in unique if p[0] == 'ray']
    return frozenset(p for p in unique if not (
        p[0] == 'point' and any(point_on_ray(p[1], r[1], r[2]) for r in rays)))


def solve_by_minima(first, second, inverse=False):
    """Find an entire intersection or inverse junction locus, exactly.

    Forward: test points X=first+t*u in L(second).
    Inverse: all junctions through first are J=first-t*u; test second in L(J).
    This computes from minimum-tie equations, not a geometric case formula.
    """
    pieces = []
    for u in DIRECTIONS:
        direction = neg(u) if inverse else u
        constants = (second[0]-first[0], second[1]-first[1], F(0)) if inverse else (
            first[0]-second[0], first[1]-second[1], F(0))
        for low, high in tie_intervals(constants, (*u, F(0))):
            start = at(first, direction, low)
            if high is None:
                pieces.append(('ray', start, direction))
            elif low == high:
                pieces.append(('point', start))
            else:
                pieces.append(('segment', start, at(first, direction, high)))
    return canonical(pieces)


def predicted_intersection(first, second):
    """Independent complete case table, translated from the proof above."""
    h, k = second[0] - first[0], second[1] - first[1]
    if h == k == 0:
        return frozenset(('ray', first, u) for u in DIRECTIONS)
    if h == 0:
        return frozenset({('ray', add(first, (0, max(0, k))), (0, 1))})
    if k == 0:
        return frozenset({('ray', add(first, (max(0, h), 0)), (1, 0))})
    if h == k:
        return frozenset({('ray', add(first, (min(0, h), min(0, h))), (-1, -1))})
    if k < 0 < h:
        relative = (h, 0)
    elif h < 0 < k:
        relative = (0, k)
    elif 0 < k < h:
        relative = (h-k, 0)
    elif 0 < h < k:
        relative = (0, k-h)
    elif k < h < 0:
        relative = (h, h)
    elif h < k < 0:
        relative = (k, k)
    else:
        raise AssertionError(('missing real case', h, k))
    return frozenset({('point', add(first, relative))})


def predicted_inverse(first, second):
    reflected = predicted_intersection(neg(first), neg(second))
    return frozenset((piece[0], neg(piece[1]), neg(piece[2])) if piece[0] == 'ray'
                     else ('point', neg(piece[1])) for piece in reflected)


def check_source_data(source_dir):
    """Read literal coordinates without running the author's Python code."""
    path = source_dir / 'data.py'
    parsed = {}
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id.isupper():
                parsed[target.id] = ast.literal_eval(node.value)
    assert parsed == EXPECTED_DATA, ('plotted coordinates changed', parsed)
    return path


def checked_pairs(cases, answers, label):
    assert len(cases) == len(answers), ('missing expected answer', label)
    return zip(cases, answers)


def fixed_cases():
    for point, expected in checked_pairs(EXPECTED_DATA['EXAMPLE_POINTS'], (True, False), 'opening'):
        assert on_line(point, EXPECTED_DATA['EXAMPLE_JUNCTION']) == expected
    for pair, meeting in checked_pairs(EXPECTED_DATA['TRIAL_FIXED_PAIRS'], ((3, 2), (2, 3)), 'fixed trials'):
        expected = frozenset({('point', meeting)})
        assert solve_by_minima(*pair) == expected
        assert predicted_intersection(*pair) == expected
    assert solve_by_minima(*EXPECTED_DATA['CROPPED_PAIR']) == frozenset({('point', (10, 7))})
    assert not (0 <= 10 <= 8 and 0 <= 7 <= 8)
    expected_intersections = (
        frozenset({('point', (6, 5))}),
        frozenset({('ray', (3, 6), (0, 1))}),
        frozenset({('ray', (6, 4), (1, 0))}),
        frozenset({('ray', (2, 2), (-1, -1))}),
    )
    for pair, expected in checked_pairs(EXPECTED_DATA['INTERSECTION_PAIRS'], expected_intersections, 'intersections'):
        assert solve_by_minima(*pair) == expected, pair
    for pair, junction in checked_pairs(EXPECTED_DATA['INVERSE_GENERAL'], ((2, 2), (5, 5)), 'inverse general'):
        assert solve_by_minima(*pair, inverse=True) == frozenset({('point', junction)}), pair
    expected_inverse = (
        frozenset({('ray', (2, 4), (-1, 0))}),
        frozenset({('ray', (3, 2), (0, -1))}),
        frozenset({('ray', (5, 5), (1, 1))}),
    )
    for pair, expected in checked_pairs(EXPECTED_DATA['INVERSE_ALIGNED'], expected_inverse, 'inverse aligned'):
        assert solve_by_minima(*pair, inverse=True) == expected, pair
    # Five valid outcomes in the open exploration, including coincident lines.
    a = EXPECTED_DATA['TRIAL_JUNCTION']
    for b in ((6, 2), (4, 6), (6, 4), (6, 6), (4, 4)):
        assert solve_by_minima(a, b) == predicted_intersection(a, b)
    # Cropping does not turn the actual intersection into an empty one.
    assert solve_by_minima((2, 5), (20, 2)) == frozenset({('point', (20, 5))})
    # An exactly shared larger pair is not sufficient.
    for t in (F(1, 5), 1, 100):
        assert not on_line((2+t, 2+t), (2, 2))


def regression():
    values = tuple(map(F, ('-3/2', '-1', '-1/3', '0', '1/4', '1/2', '1', '2')))
    locations = list(product(values, repeat=2))
    pair_count = 0
    for a, b in product(locations, repeat=2):
        actual = solve_by_minima(a, b)
        expected = predicted_intersection(a, b)
        assert actual == expected, ('intersection', a, b, actual, expected)
        inverse = solve_by_minima(a, b, inverse=True)
        inverse_expected = predicted_inverse(a, b)
        assert inverse == inverse_expected, ('inverse', a, b, inverse, inverse_expected)
        # Nonemptiness and exclusion of a two-singleton or bounded-segment result.
        assert actual and len(actual) in (1, 3)
        assert all(piece[0] in ('point', 'ray') for piece in actual)
        assert len(actual) != 3 or a == b
        pair_count += 1
    samples = list(product((F(-5), F(-1, 2), F(0), F(1, 3), F(2), F(5)), repeat=2))
    membership_count = 0
    for junction, point in product(locations, samples):
        dx, dy = point[0]-junction[0], point[1]-junction[1]
        geometric = (dy == 0 and dx >= 0) or (dx == 0 and dy >= 0) or (dx == dy and dx <= 0)
        assert on_line(point, junction) == geometric
        scores = (dx, dy, F(0))
        for shift in (F(-7, 3), F(9, 5)):
            shifted = tuple(value+shift for value in scores)
            assert (shifted.count(min(shifted)) >= 2) == geometric
        membership_count += 1
    return pair_count, membership_count



def check_diagram_source(path):
    """Audit each generated diagram macro against separately recorded points.

    Optional because cases.tex is a build output, not a portable source file.
    The visual PDF check is still required; TikZ text alone is insufficient.
    """
    text = path.read_text()
    blocks = {}
    for chunk in text.split('\\newcommand{\\')[1:]:
        name, rest = chunk.split('}{%', 1)
        blocks[name] = rest
    expected = {
        'TrialBoards': [('junction', '4', '4', 'A')]*2 + [
            ('junction', '2', '2', 'A'), ('junction', '6', '5', 'B'),
            ('junction', '2', '2', 'A'), ('junction', '5', '6', 'B')],
        'IntersectionBoards': [
            ('junction', '2', '5', 'A'), ('junction', '6', '2', 'B'),
            ('junction', '3', '2', 'A'), ('junction', '3', '6', 'B'),
            ('junction', '2', '4', 'A'), ('junction', '6', '4', 'B'),
            ('junction', '2', '2', 'A'), ('junction', '6', '6', 'B')],
        'GeneralBoards': [
            ('target', '2', '5', 'P'), ('target', '6', '2', 'Q'),
            ('target', '2', '2', 'P'), ('target', '6', '5', 'Q')],
        'AlignedBoards': [
            ('target', '2', '4', 'P'), ('target', '6', '4', 'Q'),
            ('target', '3', '2', 'P'), ('target', '3', '6', 'Q'),
            ('target', '2', '2', 'P'), ('target', '5', '5', 'Q')],
        'CroppedBoard': [('junction', '2', '7', 'A')],
    }
    board_counts = {'TrialBoards':4, 'IntersectionBoards':4, 'GeneralBoards':2,
                    'AlignedBoards':3, 'CroppedBoard':1}
    for name, points in expected.items():
        assert name in blocks, ('missing diagram', name)
        actual = re.findall(r'\\(junction|target)\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}', blocks[name])
        assert actual == points, ('plotted points mismatch', name, actual)
        assert blocks[name].count(r'\board{') == board_counts[name]
    assert '$A=(2,7)$ and $B=(10,5)$' in blocks['CroppedJunctions']
    return sum(board_counts.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--source-dir', type=Path)
    parser.add_argument('--cases-tex', type=Path, help='Optional generated diagram definitions')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    source = args.source_dir
    if source is None:
        source = next((p for p in (here, here/'final'/'src')
                       if (p/'data.py').is_file()), None)
    if source is None:
        raise SystemExit('Supply --source-dir containing the packet data.py.')
    checked = check_source_data(source)
    if args.cases_tex:
        count = check_diagram_source(args.cases_tex)
        print(f'PASS: all plotted coordinates and labels on {count} generated boards.')
    fixed_cases()
    pair_count, member_count = regression()
    print(f'PASS: fixed coordinates match {checked}')
    print('PASS: opening diagram, 2 fixed-trial boards, 4 intersection boards,')
    print('      2 inverse-generic boards, 3 inverse-aligned boards, off-window case,')
    print('      and 5 possible outcomes for the child-chosen trials.')
    print('Changed final answers: (3,2), (2,3), and off-window (10,7).')
    print(f'PASS: {pair_count} exact ordered rational pairs, forward and inverse;')
    print('      includes all strict cases, all three overlaps, and coincidence.')
    print(f'PASS: {member_count} minimum-tie/three-ray memberships and constant shifts.')
    print('General all-real proofs and Problems 1-7 outcomes are in this file docstring.')
    print('No finite regression is claimed to prove the all-real results.')


if __name__ == '__main__':
    main()
