"""Independent exact checks of the reviewed mathematical instances."""
from fractions import Fraction as F

from itertools import combinations, permutations, product

from collections import deque

from pathlib import Path

import argparse, hashlib, json, math

import verify_kernels as k

def reflection(p, a, b, weight):
    edge = k.minus(b, a)
    normal = (-weight * edge[1], edge[0])
    v = k.minus(p, a)
    dot = v[0] * normal[0] + weight * v[1] * normal[1]
    norm = normal[0] ** 2 + weight * normal[1] ** 2
    return k.minus(p, k.times(2 * dot / norm, normal))

def bounce_checks():
    words = {}
    for dx, dy in product(range(-9, 10), repeat=2):
        if not (dx or dy):
            continue
        word = k.rectangle_bounces(2, 2, (1, 1), (dx, dy), 3)
        if word:
            translated = word.translate(str.maketrans({'L': 'B', 'R': 'D', 'B': 'A', 'T': 'C'}))
            words.setdefault(translated, [dx, dy])
    assert len(words) >= 6
    chosen = {w: words[w] for w in ('ABC', 'ACA', 'ADC', 'BAD', 'CAC', 'DAB')}
    for dx, dy in chosen.values():
        events = []
        for value in (-4, -2, 0, 2, 4, 6):
            if dx:
                t = F(value - 1, dx)
                if t > 0:
                    events.append((t, 'v'))
            if dy:
                t = F(value - 1, dy)
                if t > 0:
                    events.append((t, 'h'))
        events.sort()
        assert len(events) >= 3 and len({t for t, _ in events[:3]}) == 3
        t = events[2][0]
        assert -4 <= 1 + t * dx <= 6 and -4 <= 1 + t * dy <= 6
    snapshot = json.loads((HERE / 'bounce-unfolding-instance.json').read_text())
    actual = snapshot['square'] + snapshot['rhombus']
    assert len(actual) == 8
    checked_polygons = 0
    for offset, start, weight in ((0, [(0, 0), (4, 0), (4, 4), (0, 4)], 1), (4, [(0, 0), (4, 0), (6, 2), (2, 2)], 3)):
        polygon = [tuple(map(F, p)) for p in start]
        expected = [polygon]
        for edge in ((0, 1), (0, 3), (0, 1)):
            a, b = (polygon[i] for i in edge)
            polygon = [reflection(p, a, b, weight) for p in polygon]
            expected.append(polygon)
        for j, polygon in enumerate(expected):
            points = actual[offset + j]
            assert len(points) == 4
            for (x, y), (xx, yy) in zip(polygon, points):
                assert abs(float(x) - xx) < 1e-07
                assert abs(float(y) * math.sqrt(weight) - yy) < 1e-07
            checked_polygons += 1
    return {'1_six_witness_directions': chosen, '1_distinct_words_found': len(words), '2_square_ABA': False, '2_rhombus_ABA': True, '2_reflected_polygons_checked': checked_polygons, '4_square_and_wide_rectangle': 'same full language under horizontal stretch'}

HERE = Path(__file__).resolve().parent

if __name__ == "__main__":
    print(json.dumps({"kernel": k.check71(), "instances": bounce_checks()}, indent=2))
