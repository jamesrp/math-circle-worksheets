"""Independent small-model checks for the Weeks 2–10 mathematical design.

Run with Python 3; no external dependencies. These are checks of finite examples,
not replacements for the general arguments in the facilitator notes.
"""
from functools import lru_cache
from itertools import product
from math import gcd, lcm, isqrt
import json


def cycle_switches(n):
    outcomes = {}
    for presses in product((0, 1), repeat=n):
        lamps = tuple(presses[i] ^ presses[(i-1) % n] for i in range(n))
        outcomes.setdefault(lamps, []).append(presses)
    assert len(outcomes) == 2 ** (n-1)
    assert all(sum(lamps) % 2 == 0 for lamps in outcomes)
    assert all(len(solutions) == 2 for solutions in outcomes.values())
    assert all(all(a != b for a, b in zip(*solutions)) for solutions in outcomes.values())
    return {"states": len(outcomes), "press_sets_per_state": 2,
            "largest_minimum_press_count": max(min(map(sum, s)) for s in outcomes.values())}


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n+1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def permutation_order(n):
    values = [(lcm(*parts), parts) for parts in partitions(n)]
    maximum = max(v for v, _ in values)
    return {"maximum": maximum, "cycle_lengths": [p for v, p in values if v == maximum]}


def optimal_binary_queries(n):
    """Adaptive queries; feedback counts exact-position matches; no final guess needed."""
    codes = tuple(range(2**n))
    feedback = [[n-(a ^ b).bit_count() for b in codes] for a in codes]

    @lru_cache(None)
    def possible(candidates, depth):
        if len(candidates) <= 1:
            return True
        if depth == 0 or len(candidates) > (n+1)**depth:
            return False
        for query in codes:
            groups = {}
            for candidate in candidates:
                groups.setdefault(feedback[query][candidate], []).append(candidate)
            if len(groups) == 1:
                continue
            if all(possible(tuple(g), depth-1) for g in groups.values()):
                return True
        return False

    for depth in range(n+1):
        if possible(codes, depth):
            return depth
    raise AssertionError("No strategy found")


def subtraction(moves, limit):
    values = []
    for n in range(limit+1):
        options = {values[n-m] for m in moves if m <= n}
        g = 0
        while g in options:
            g += 1
        values.append(g)
    return values


def wythoff(limit):
    losing = []
    for total in range(2*limit+1):
        for a in range(limit+1):
            b = total-a
            if not a <= b <= limit:
                continue
            can_reach_losing = any(
                (a == x and b > y) or (a == y and b > x) or
                (b == x and a > y) or (b == y and a > x) or
                (a-x == b-y and a > x)
                for x, y in losing)
            if not can_reach_losing:
                losing.append((a, b))
    # floor(n*phi) computed by exact integer square root, no floating rounding.
    formula = [(0, 0)]
    for n in range(1, limit+1):
        a = (n + isqrt(5*n*n)) // 2
        if a+n <= limit:
            formula.append((a, a+n))
    assert losing == formula
    return losing[:8]


def billiards(width, height):
    # Unit time increments are exact for an integer rectangle at slope one.
    x = y = bounces = 0
    dx = dy = 1
    for t in range(1, width*height+1):
        x += dx
        y += dy
        at_x, at_y = x in (0, width), y in (0, height)
        if at_x and at_y:
            g = gcd(width, height)
            assert t == lcm(width, height)
            assert x == (width if (height//g) % 2 else 0)
            assert y == (height if (width//g) % 2 else 0)
            assert bounces == (width+height)//g-2
            return
        if at_x:
            dx *= -1
            bounces += 1
        if at_y:
            dy *= -1
            bounces += 1
    raise AssertionError("No corner")


def main():
    report = {"cycle_switches": {n: cycle_switches(n) for n in (4, 5)}}
    report["permutation_order"] = {n: permutation_order(n) for n in (4, 5, 8)}
    assert [report["permutation_order"][n]["maximum"] for n in (4, 5, 8)] == [4, 6, 15]
    orbit = []
    for step in range(12):
        seen, position = set(), 0
        while position not in seen:
            seen.add(position)
            position = (position+step) % 12
        assert len(seen) == 12//gcd(12, step)
        orbit.append(len(seen))
    report["twelve_ring_orbit_lengths"] = orbit
    deck = list(range(8))
    for count in range(1, 4):
        deck = [v for pair in zip(deck[:4], deck[4:]) for v in pair]
        assert (deck == list(range(8))) == (count == 3)
    report["eight_card_out_shuffle_order"] = 3
    report["optimal_binary_exact_match_queries"] = {n: optimal_binary_queries(n) for n in (2, 3, 4)}
    assert report["optimal_binary_exact_match_queries"] == {2: 2, 3: 3, 4: 4}
    landmarks = (0b00000, 0b00011, 0b00101, 0b01001)
    signatures = {tuple(5-(secret ^ q).bit_count() for q in landmarks)
                  for secret in range(32)}
    assert len(signatures) == 32
    assert tuple(5-(0b10110 ^ q).bit_count() for q in landmarks) == (2, 2, 2, 0)
    report["five_bit_four_query_signatures"] = len(signatures)
    values = subtraction((1, 3, 4), 1000)
    assert all((g == 0) == (n % 7 in (0, 2)) for n, g in enumerate(values))
    assert all(g == values[n % 7] for n, g in enumerate(values))
    other = subtraction((1, 3, 5), 1000)
    assert all((g == 0) == (n % 2 == 0) for n, g in enumerate(other))
    report["subtraction_134_grundy_period"] = values[:7]
    # Verify the two defining strategy properties over a finite three-pile box.
    for state in product(range(10), repeat=3):
        losing = state[0] ^ state[1] ^ state[2] == 0
        successors = [state[:i] + (smaller,) + state[i+1:]
                      for i in range(3) for smaller in range(state[i])]
        reaches_losing = any(a ^ b ^ c == 0 for a, b, c in successors)
        assert losing != reaches_losing
    report["nim_states_checked"] = 1000
    report["wythoff_pairs"] = wythoff(50)
    for width, height in product(range(1, 31), repeat=2):
        billiards(width, height)
    report["billiards_rectangles_checked"] = 900
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
