"""Writer-stage checks only. No solutions are printed on student pages."""
from itertools import product
from collections import deque


def ring_outputs(n):
    result = {}
    for presses in range(1 << n):
        state = 0
        for i in range(n):
            if presses & (1 << i):
                for offset in range(3):
                    state ^= 1 << ((i + offset) % n)
        result.setdefault(state, []).append(presses)
    return result


def distance(n, start, goal, cycle):
    edges = [(i, i + 1) for i in range(n - 1)]
    if cycle:
        edges.append((n - 1, 0))
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        state, depth = queue.popleft()
        if state == goal:
            return depth
        for a, b in edges:
            if bool(state & (1 << a)) == bool(state & (1 << b)):
                continue
            next_state = state ^ (1 << a) ^ (1 << b)
            if next_state not in seen:
                seen.add(next_state)
                queue.append((next_state, depth + 1))
    return None


def bits(*positions):
    return sum(1 << (i - 1) for i in positions)


for n in (4, 5, 6):
    outputs = ring_outputs(n)
    assert len(outputs) == (1 << n if n % 3 else 1 << (n - 2))
    assert all(len(v) == (1 if n % 3 else 4) for v in outputs.values())
    assert (1 in outputs) == (n % 3 != 0)
    assert (1 << n) - 1 in outputs
    print(f"Ring {n}: {len(outputs)} reachable targets; single-lamp target {'reachable' if 1 in outputs else 'unreachable'}")

# Three single-switch experiments identify all 512 hidden fixed panels.
observations = {(a, b, c) for a, b, c in product(range(8), repeat=3)}
assert len(observations) == 512
assert 8**2 < 512
assert bits(1, 3) ^ bits(1, 4) == bits(3, 4)

cases = [
    (bits(1), bits(6)),
    (bits(1, 2), bits(5, 6)),
    (bits(1, 3, 5), bits(2, 4, 6)),
    (bits(1, 2), bits(2, 4, 6)),
]
expected = [(5, 1), (8, 4), (3, 3), (None, None)]
for case, exp in zip(cases, expected):
    actual = (distance(6, *case, False), distance(6, *case, True))
    assert actual == exp, (case, actual, exp)
    print(f"Transport {case}: line/ring minimum {actual}")
assert bits(1, 3) ^ bits(1, 2) == bits(2, 3)
print("All writer-stage mathematical checks passed.")
